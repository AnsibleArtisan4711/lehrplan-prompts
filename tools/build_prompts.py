#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt aus daten/kurse.json, daten/rahmen.json und rahmen/prompt-vorlage.txt
alle Dateien in prompts/ sowie die Tabelle in README.md (mit Link auf lehrplaene/).
Aus daten/faecher.json entstehen die Modulübersichten in faecher/ (K01-K16) und die
zweite Tabelle in README.md; aus daten/uebungen.json (E01-E06, erzeugt von
tools/uebungen_einlesen.py) die Seiten in uebungen/ und die dritte Tabelle. Aus den Feldern
"repo" und "ordner" in daten/kurse.json entstehen die Spalte "Repository" und die
Zuordnung Kurse -> Themen-Repositories.

Aufruf (im Repository-Ordner):  python tools/build_prompts.py
Nur Standardbibliothek, Python 3.8 oder neuer.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARK_A = "<!-- TABELLE-START -->"
MARK_B = "<!-- TABELLE-ENDE -->"
FMARK_A = "<!-- FAECHER-START -->"
FMARK_B = "<!-- FAECHER-ENDE -->"
GITHUB = "https://github.com/AnsibleArtisan4711/"


def repo_name(x):
    """Name des Themen-Repositories, mit Kursordner, wenn das Feld "ordner" gesetzt ist."""
    return x["repo"] + ("/" + x["ordner"] if x.get("ordner") else "")


def repo_url(x):
    """Adresse des Repositories; bei Kursordnern direkt auf den Ordner."""
    return GITHUB + x["repo"] + ("/tree/main/" + x["ordner"] if x.get("ordner") else "")
UMARK_A = "<!-- UEBUNGEN-START -->"
UMARK_B = "<!-- UEBUNGEN-ENDE -->"
RMARK_A = "<!-- REPOS-START -->"
RMARK_B = "<!-- REPOS-ENDE -->"


def lade(pfad):
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def prompt_text(kurs, rahmen, vorlage):
    umfang = rahmen["umfang_klein"] if kurs["umfang"] == "klein" else rahmen["umfang_gross"]
    hinweis = kurs["hinweis"].strip()
    themen = kurs["themen"].strip().rstrip(".")
    # Kurse ohne technisches Labor bekommen das Thema nicht automatisch angehängt.
    hat_labor = not kurs["labor"].startswith("kein technisches Labor")
    if hat_labor and "roubleshoot" not in themen and "Fehlersuche" not in themen:
        themen += "; Troubleshooting und Diagnosewerkzeuge"
    return vorlage.format(
        titel=kurs["titel"],
        fokus=kurs["fokus"],
        vorkenntnisse=kurs["vorkenntnisse"],
        umfang=umfang,
        themen=themen,
        abgrenzung=kurs["abgrenzung"].strip() or rahmen["abgrenzung_standard"],
        labor=kurs["labor"],
        hinweis_zeile=("Zusätzliche Hinweise: " + hinweis + "\n") if hinweis else "",
    ).rstrip("\n")


def datei_name(kurs):
    return "%s-%s.md" % (kurs["id"], kurs["slug"])


def prompt_datei(kurs, rahmen, vorlage):
    return "# %s – %s\n\nPriorität %s, %s.\n\n```text\n%s\n```\n" % (
        kurs["id"], kurs["titel"], kurs["prio"], kurs["gruppe"],
        prompt_text(kurs, rahmen, vorlage))


def lehrplan_datei(kurs):
    return ROOT / "lehrplaene" / datei_name(kurs)


def repo_zelle(k):
    """Gepusht: Link auf den Kursordner. Sonst: das geplante Themen-Repository."""
    if k["status"] == "gepusht":
        return "[%s](%s)" % (repo_name(k), repo_url(k))
    return "`%s` (geplant)" % k["repo"]


def tabelle(kurse, rahmen):
    zeilen = ["| Nr | Prio | Themengebiet | Kurs | Status | Prompt | Lehrplan | Repository |",
              "|---|---|---|---|---|---|---|---|"]
    for i, k in enumerate(kurse, 1):
        if lehrplan_datei(k).exists():
            lehrplan = "[%s](lehrplaene/%s)" % (k["id"], datei_name(k))
        else:
            lehrplan = "–"
        zeilen.append("| %d | %s | %s | %s | %s | [%s](prompts/%s) | %s | %s |" % (
            i, k["prio"], k["gruppe"], k["titel"], k["status"], k["id"], datei_name(k), lehrplan,
            repo_zelle(k)))
    return "\n".join(zeilen)


def repo_tabelle(kurse, vorhanden):
    """Zuordnung Kurse -> Themen-Repository, in der Reihenfolge des ersten Auftretens."""
    reihe = []
    for k in kurse:
        if k["repo"] not in reihe:
            reihe.append(k["repo"])
    zeilen = ["| Repository | Kurse |", "|---|---|"]
    for r in reihe:
        eintraege = []
        for k in kurse:
            if k["repo"] != r:
                continue
            e = "%s %s" % (k["id"], k["titel"])
            if k["status"] == "gepusht":
                e += " (gepusht)"
            eintraege.append(e)
        name = "[%s](%s)" % (r, GITHUB + r) if r in vorhanden else "`%s` (noch nicht angelegt)" % r
        zeilen.append("| %s | %s |" % (name, "; ".join(eintraege)))
    return "\n".join(zeilen)


def uebersicht(kurse, rahmen):
    """Zähler und Legende zu den Statuswerten, steht vor der Tabelle."""
    zahlen = ", ".join("%d %s" % (sum(1 for k in kurse if k["status"] == s), s)
                       for s in rahmen["status_werte"])
    zeilen = ["Stand der %d Kurse: %s." % (len(kurse), zahlen), "",
              "Bedeutung der Status:", ""]
    for s in rahmen["status_werte"]:
        zeilen.append("- **%s**: %s" % (s, rahmen["status_legende"][s]))
    zeilen.append("")
    zeilen.append("Spalte „Repository“: bei gepusht der Link auf den Kursordner, sonst das geplante "
                  "Themen-Repository (Feld `repo` in `daten/kurse.json`).")
    zeilen.append("")
    return "\n".join(zeilen)

def zahl(x):
    """Stunden ohne unnötige Nachkommastellen, mit Komma."""
    return ("%g" % x).replace(".", ",")


def fach_datei(fach):
    return "%s-%s.md" % (fach["id"], fach["slug"])


def fach_seite(fach):
    z = ["# %s – %s" % (fach["id"], fach["titel"]), "",
         "- Typ: %s, Bereich: %s" % (fach["typ"], fach["bereich"]),
         "- Umfang: %d Module, ca. %s Stunden" % (len(fach["module"]), zahl(fach["stunden"])),
         "- Voraussetzung / Empfehlung: %s" % (fach["voraussetzung"] or "keine")]
    if fach["repo"]:
        z.append("- Übungsmaterial: [%s](%s)" % (repo_name(fach), repo_url(fach)))
    z += ["", "## Module", "", "| Nr | Modul | ca. Stunden |", "|---|---|---|"]
    for m in fach["module"]:
        z.append("| %d | %s | %s |" % (m["nr"], m["titel"], zahl(m["stunden"])))
    z += ["", "Die Stunden je Modul sind gleichmäßig aus der Gesamtdauer verteilt und gerundet; die Summe kann um",
          "unter eine Stunde von der Gesamtdauer abweichen. Quelle: Fächerübersicht (Excel) des Autors; Umlaute in den Modultiteln ergänzt.",
          "", "Umsetzungsordner anlegen: `python tools/umsetzung_anlegen.py %s`" % fach["id"], ""]
    return "\n".join(z)


def faecher_tabelle(faecher):
    zeilen = ["| Nr | Fach | Typ | Bereich | Module | Stunden | Voraussetzung | Repository |",
              "|---|---|---|---|---|---|---|---|"]
    for f in faecher:
        repo = "[%s](%s)" % (repo_name(f), repo_url(f)) if f["repo"] else "–"
        zeilen.append("| [%s](faecher/%s) | %s | %s | %s | %d | %s | %s | %s |" % (
            f["id"], fach_datei(f), f["titel"], f["typ"], f["bereich"], len(f["module"]),
            zahl(f["stunden"]), f["voraussetzung"] or "–", repo))
    kern = sum(1 for f in faecher if f["typ"] == "Kern")
    kopf = "%d Fächer: %d Kern, %d Erweiterung; zusammen %d Module, ca. %s Stunden.\n\n" % (
        len(faecher), kern, len(faecher) - kern, sum(len(f["module"]) for f in faecher),
        zahl(sum(f["stunden"] for f in faecher)))
    return kopf + "\n".join(zeilen)


def uebung_datei(r):
    return "%s-%s.md" % (r["id"], r["slug"])


def anzahl_einheiten(r):
    return sum(len(m["einheiten"]) for m in r.get("module", []))


def uebung_seite(r):
    z = ["# %s – %s" % (r["id"], r["titel"]), "",
         "- Thema: %s" % r["thema"],
         "- Repository: [%s](%s)" % (repo_name(r), repo_url(r)),
         "- Umfang: %d Module, davon %d mit Material; %d Einheiten" % (
             len(r.get("module", [])), sum(1 for m in r.get("module", []) if m["einheiten"]),
             anzahl_einheiten(r)), ""]
    for m in r.get("module", []):
        nr = "Modul %d" % m["nr"] if m["nr"] is not None else "Anhang"
        z += ["## %s: %s" % (nr, m["titel"]), ""]
        if not m["einheiten"]:
            z += ["Noch kein Material.%s" % ((" Geplant: " + m["geplant"]) if m.get("geplant") else ""), ""]
            continue
        if r["art"] == "steps":
            z += ["| Step | Thema |", "|---|---|"] + ["| %s | %s |" % (e["nr"], e["titel"]) for e in m["einheiten"]]
            z.append("")
            continue
        for e in m["einheiten"]:
            z += ["### %s %s" % (e["nr"], e["titel"]), "",
                  "- Stufe: %s; geschätzte Zeit: %s" % (e["stufe"] or "–", e["zeit"] or "–"),
                  "- Teile: %s" % ("; ".join("%d %s (%d Schritte)" % (t["nr"], t["titel"], len(t["schritte"]))
                                            for t in e["teile"]) or "–"),
                  "- Lernziele: %d, Kontrollfragen: %d" % (len(e["lernziele"]), len(e["kontrollfragen"]))]
            if m.get("skripte"):
                z.append("- Skripte: " + ", ".join("`%s`" % s["datei"] for s in m["skripte"]))
            z.append("")
    z += ["Aufbau gelesen aus den Dateien des Repositories (`python tools/uebungen_einlesen.py`).",
          "Umsetzungsordner anlegen: `python tools/umsetzung_anlegen.py %s`" % r["id"], ""]
    return "\n".join(z)


def uebungen_tabelle(reihen):
    zeilen = ["| Nr | Übung | Thema | Module | Einheiten | Repository |", "|---|---|---|---|---|---|"]
    for r in reihen:
        zeilen.append("| [%s](uebungen/%s) | %s | %s | %d | %d | [%s](%s) |" % (
            r["id"], uebung_datei(r), r["titel"], r["thema"],
            len(r.get("module", [])), anzahl_einheiten(r),
            repo_name(r), repo_url(r)))
    return "\n".join(zeilen)


def main():
    rahmen = lade(ROOT / "daten" / "rahmen.json")
    kurse = lade(ROOT / "daten" / "kurse.json")
    vorlage = (ROOT / "rahmen" / "prompt-vorlage.txt").read_text(encoding="utf-8").rstrip("\n")

    ids = [k["id"] for k in kurse]
    if len(ids) != len(set(ids)):
        sys.exit("Fehler: doppelte IDs in daten/kurse.json")
    for k in kurse:
        if k["status"] not in rahmen["status_werte"]:
            sys.exit("Fehler: unbekannter Status %r bei %s" % (k["status"], k["id"]))
    for k in kurse:
        if k["status"] == "Lehrplan erstellt" and not lehrplan_datei(k).exists():
            sys.exit("Fehler: Status 'Lehrplan erstellt', aber lehrplaene/%s fehlt" % datei_name(k))
    for k in kurse:
        if not k.get("repo"):
            sys.exit("Fehler: Feld 'repo' fehlt bei %s" % k["id"])
        if k["status"] == "gepusht" and not k.get("ordner"):
            sys.exit("Fehler: Status 'gepusht', aber Feld 'ordner' fehlt bei %s" % k["id"])
    for s in rahmen["status_werte"]:
        if s not in rahmen.get("status_legende", {}):
            sys.exit("Fehler: Legende fehlt für Status %r in daten/rahmen.json" % s)

    faecher = lade(ROOT / "daten" / "faecher.json")
    fids = [f["id"] for f in faecher]
    if len(fids) != len(set(fids)) or any(i in ids for i in fids):
        sys.exit("Fehler: doppelte IDs in daten/faecher.json")
    for f in faecher:
        if [m["nr"] for m in f["module"]] != list(range(1, len(f["module"]) + 1)):
            sys.exit("Fehler: Modulnummern in %s nicht lückenlos ab 1" % f["id"])

    uebungen = lade(ROOT / "daten" / "uebungen.json")
    uids = [u["id"] for u in uebungen]
    if len(uids) != len(set(uids)) or any(i in ids or i in fids for i in uids):
        sys.exit("Fehler: doppelte IDs in daten/uebungen.json")

    ordner = ROOT / "prompts"
    ordner.mkdir(exist_ok=True)
    erwartet = set()
    for k in kurse:
        name = datei_name(k)
        erwartet.add(name)
        (ordner / name).write_text(prompt_datei(k, rahmen, vorlage), encoding="utf-8", newline="\n")
    for alt in ordner.glob("P*.md"):
        if alt.name not in erwartet:
            print("Hinweis: verwaiste Datei, bitte prüfen und von Hand löschen:", alt.name)

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    muster = re.compile(re.escape(MARK_A) + r".*?" + re.escape(MARK_B), re.S)
    if not muster.search(text):
        sys.exit("Fehler: Markierungen %s und %s fehlen in README.md" % (MARK_A, MARK_B))
    neu = MARK_A + "\n" + uebersicht(kurse, rahmen) + "\n" + tabelle(kurse, rahmen) + "\n" + MARK_B
    readme.write_text(muster.sub(lambda m: neu, text), encoding="utf-8", newline="\n")
    # Fächer K01-K16
    fo = ROOT / "faecher"
    fo.mkdir(exist_ok=True)
    for f in faecher:
        (fo / fach_datei(f)).write_text(fach_seite(f), encoding="utf-8", newline="\n")
    for alt in fo.glob("K*.md"):
        if alt.name not in {fach_datei(f) for f in faecher}:
            print("Hinweis: verwaiste Datei, bitte prüfen und von Hand löschen:", alt.name)
    fm = re.compile(re.escape(FMARK_A) + r".*?" + re.escape(FMARK_B), re.S)
    text = readme.read_text(encoding="utf-8")
    if not fm.search(text):
        sys.exit("Fehler: Markierungen %s und %s fehlen in README.md" % (FMARK_A, FMARK_B))
    fneu = FMARK_A + "\n" + faecher_tabelle(faecher) + "\n" + FMARK_B
    readme.write_text(fm.sub(lambda m: fneu, text), encoding="utf-8", newline="\n")
    # Übungen E01-E06
    uo = ROOT / "uebungen"
    uo.mkdir(exist_ok=True)
    for u in uebungen:
        (uo / uebung_datei(u)).write_text(uebung_seite(u), encoding="utf-8", newline="\n")
    for alt in uo.glob("E*.md"):
        if alt.name not in {uebung_datei(u) for u in uebungen}:
            print("Hinweis: verwaiste Datei, bitte prüfen und von Hand löschen:", alt.name)
    um = re.compile(re.escape(UMARK_A) + r".*?" + re.escape(UMARK_B), re.S)
    text = readme.read_text(encoding="utf-8")
    if not um.search(text):
        sys.exit("Fehler: Markierungen %s und %s fehlen in README.md" % (UMARK_A, UMARK_B))
    uneu = UMARK_A + "\n" + uebungen_tabelle(uebungen) + "\n" + UMARK_B
    readme.write_text(um.sub(lambda m: uneu, text), encoding="utf-8", newline="\n")
    # Zuordnung Kurse -> Themen-Repositories
    vorhanden = ({f["repo"] for f in faecher if f["repo"]} | {u["repo"] for u in uebungen}
                 | {k["repo"] for k in kurse if k["status"] == "gepusht"})
    rm = re.compile(re.escape(RMARK_A) + r".*?" + re.escape(RMARK_B), re.S)
    text = readme.read_text(encoding="utf-8")
    if not rm.search(text):
        sys.exit("Fehler: Markierungen %s und %s fehlen in README.md" % (RMARK_A, RMARK_B))
    rneu = RMARK_A + "\n" + repo_tabelle(kurse, vorhanden) + "\n" + RMARK_B
    readme.write_text(rm.sub(lambda m: rneu, text), encoding="utf-8", newline="\n")
    print("%d Prompts, %d Fächer, %d Übungsreihen und README-Tabellen erzeugt." % (len(kurse), len(faecher), len(uebungen)))


if __name__ == "__main__":
    main()
