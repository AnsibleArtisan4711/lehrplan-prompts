#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legt aus einem Lehrplan in lehrplaene/ (P01-P52) oder einem Fach aus daten/faecher.json
(K01-K16) oder einer Uebungsreihe aus daten/uebungen.json (E01-E06) einen Umsetzungsordner an: je Modul ein Unterordner
mit Checkliste, Protokollvorlage, Fehlerprotokoll und Ablageordnern fuer Screenshots, Notizen
und Ausgaben. Dazu eine Uebersicht, eine Liste der als "nicht bestaetigt" markierten Befehle
und ein Abschlussordner.

Aufruf (im Repository-Ordner):
    python tools/umsetzung_anlegen.py P46            # Ziel: <Ordner ueber dem Repo>/Umsetzung
    python tools/umsetzung_anlegen.py P46 D:\\Umsetzung
    python tools/umsetzung_anlegen.py K07            # Fach aus daten/faecher.json (nur Modulliste)
    python tools/umsetzung_anlegen.py E03            # Uebungsreihe aus daten/uebungen.json

Bei K01-K16 gibt es keinen Lehrplan mit Praxisaufgaben im Repository, nur Modultitel und
Stunden. Die Checklisten sind deshalb schlanker; Aufgaben, Lernziele und Kontrollfragen
stehen im Skript des Moduls (Fach-Repository oder Lehrplan-Ordner).

Vorhandene Dateien werden nie ueberschrieben (Hinweis in der Ausgabe), vorhandene Ordner
bleiben unveraendert. Nur Standardbibliothek, Python 3.8 oder neuer.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKER = "nicht bestätigt"
UNTERORDNER = ("screenshots", "notizen", "ausgaben")


def slug(text, laenge=50):
    text = text.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.replace(a, b)
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > laenge:
        text = text[:laenge]
        if "-" in text:
            text = text[: text.rindex("-")]
    return text.rstrip("-")


def kurz(text, n=220):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def zeilen_ohne_code(zeilen):
    """Liefert (Zeile, in_code) ; Codezaeune selbst zaehlen als Code."""
    ein = False
    for z in zeilen:
        if z.lstrip().startswith("```"):
            ein = not ein
            yield z, True
        else:
            yield z, ein


def lade_modul(name, block):
    zeilen = block.split("\n")
    m = {"nr": 0, "titel": "", "prio": "", "zeit": "", "lernziele": [], "voraus": "",
         "einheiten": [], "aufgaben": [], "fragen": []}
    erg = re.match(r"### Modul (\d+): (.*)", zeilen[0])
    m["nr"], m["titel"] = int(erg.group(1)), erg.group(2).strip()
    abschnitt = ""
    aktuell = None
    in_lz = False
    for z, code in zeilen_ohne_code(zeilen[1:]):
        if not code:
            if "Überprüfbare Lernziele" in z:
                in_lz = True
                continue
            if in_lz:
                if re.match(r"\s+\* ", z):
                    m["lernziele"].append(z.strip()[2:].strip())
                    continue
                if z.strip():
                    in_lz = False
            if z.startswith("#### "):
                abschnitt = "aufgaben" if "Praxisaufgaben" in z else "fragen" if "Kontrollfragen" in z \
                    else "einheiten" if "Lerneinheiten" in z else ""
                aktuell = None
                continue
            h = re.match(r"\* \*\*Priorität:\*\* (.*)", z)
            if h:
                m["prio"] = h.group(1).strip()
            h = re.match(r"\* \*\*Zeitaufwand:\*\* (.*)", z)
            if h:
                m["zeit"] = h.group(1).strip()
            h = re.match(r"\* \*\*Voraussetzungen:\*\* (.*)", z)
            if h:
                m["voraus"] = h.group(1).strip()
            if abschnitt == "einheiten":
                h = re.match(r"\|\s*\*{0,2}(\d+\.\d+)\*{0,2}\s*\|(.*)\|\s*([\d,.]+)\s*\|\s*$", z)
                if h:
                    m["einheiten"].append((h.group(1), h.group(2).strip(), h.group(3)))
            if abschnitt == "aufgaben":
                h = re.match(r"(\d+)\. (.*)", z)
                if h:
                    titel = re.match(r"\*\*(.+?)\*\*", h.group(2))
                    if titel:
                        titel = re.match(r"(.+?)[:\s]*$", titel.group(1))
                    aktuell = {"nr": int(h.group(1)), "titel": (titel.group(1) if titel else kurz(h.group(2), 80)),
                               "text": [z]}
                    m["aufgaben"].append(aktuell)
                    continue
            if abschnitt == "fragen":
                h = re.match(r"(\d+)\. (.*)", z)
                if h:
                    m["fragen"].append(h.group(2).strip())
                    continue
        if abschnitt == "aufgaben" and aktuell is not None:
            aktuell["text"].append(z)
    for a in m["aufgaben"]:
        a["marker"] = [kurz(t, 240) for t in a["text"] if MARKER in t]
        a["anzahl"] = sum(t.count(MARKER) for t in a["text"])
    return m


def lade_lehrplan(pfad):
    text = pfad.read_text(encoding="utf-8")
    titel = re.match(r"# Lehrplan: (.*)", text).group(1).strip()
    teil_b = text.index("\n## B.")
    teil_c = text.find("\n## C.")
    a = text[:teil_b]
    b = text[teil_b: teil_c if teil_c > 0 else len(text)]
    # Labor-Setup
    lab = ""
    h = re.search(r"^### \d+\. Labor-Setup.*$", a, re.M)
    if h:
        lab = a[h.end():]
    teile = re.split(r"(?m)^(?=### Modul \d+:)", b)
    module = [lade_modul(pfad.name, t.rstrip().rstrip("-").rstrip()) for t in teile if t.startswith("### Modul")]
    return titel, lab, module


def labor_punkte(lab):
    """Obere Aufzaehlungspunkte '* **Name:** ...' des Labor-Setups."""
    punkte = []
    for z in lab.split("\n"):
        h = re.match(r"\*\s+\*\*(.+?)\*\*:?\s*(.*)", z)
        if h:
            punkte.append((h.group(1).strip().rstrip(":"), kurz(h.group(2), 160)))
    if not punkte:
        for z in lab.split("\n"):
            h = re.match(r"\*\s+(.+)", z)
            if h:
                punkte.append((kurz(h.group(1), 160), ""))
    return punkte


def tabellen(lab):
    zeilen, aus = lab.split("\n"), []
    for z in zeilen:
        if z.startswith("|"):
            aus.append(z)
        elif aus and aus[-1] != "":
            aus.append("")
    return "\n".join(aus).strip()


def pruefpunkte(lab):
    for z in lab.split("\n"):
        if re.match(r"\* \*\*Prüfpunkte", z):
            return sorted(set(c for c in re.findall(r"`([^`]+)`", z) if "-" in c))
    return []


def schreibe(pfad, text, bericht):
    if pfad.exists():
        bericht.append("vorhanden, nicht überschrieben: %s" % pfad)
        return
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(text.rstrip("\n") + "\n", encoding="utf-8", newline="\n")


def modul_ordner(m):
    return "%02d-%s" % (m["nr"], slug(m["titel"]))


def checkliste_modul(m, punkte, kid):
    z = ["# Modul %d: %s – Checkliste" % (m["nr"], m["titel"]), "",
         "Quelle: `lehrplaene/%s`. Priorität %s, Zeitaufwand %s." % (kid, m["prio"] or "?", m["zeit"] or "?"), "",
         "## Vorbereitung", "",
         "- [ ] Voraussetzungen erfüllt: %s" % (kurz(m["voraus"], 300) or "laut Lehrplan"), ]
    for p in punkte:
        z.append("- [ ] Prüfpunkt/Checkpoint `%s` vorhanden oder wird in diesem Modul angelegt" % p)
    z += ["", "## Lerneinheiten", ""]
    for nr, inhalt, h in m["einheiten"]:
        z.append("- [ ] %s (%s UE): %s" % (nr, h, kurz(inhalt, 140)))
    z += ["", "## Praxisaufgaben", ""]
    for a in m["aufgaben"]:
        n = " – %d Befehl(e)/Angabe(n) „%s“" % (a["anzahl"], MARKER) if a["anzahl"] else ""
        z.append("- [ ] Aufgabe %d: %s%s" % (a["nr"], a["titel"], n))
    z += ["", "## Lernziele (erreicht, wenn Aufgabe und Beleg vorliegen)", ""]
    for i, l in enumerate(m["lernziele"], 1):
        z.append("- [ ] Lernziel %d: %s" % (i, re.sub(r"^Nach Abschluss dieses Moduls kann der Lernende ", "", l)))
    z += ["", "## Kontrollfragen", ""]
    for i, f in enumerate(m["fragen"], 1):
        z.append("- [ ] Frage %d beantwortet: %s" % (i, kurz(f, 120)))
    z += ["", "## Abschluss", "",
          "- [ ] Screenshots und Ausgaben in `screenshots/` und `ausgaben/` abgelegt, Dateinamen siehe `protokoll.md`",
          "- [ ] Kennwörter und echte Namen auf Screenshots geprüft",
          "- [ ] Fehler in `fehlerprotokoll.md` eingetragen",
          "- [ ] Befehle mit „%s“ in `../befehle-nicht-bestaetigt.md` nachgetragen" % MARKER,
          "- [ ] Abweichungen vom Lehrplan in `../99-abschluss/lehrplan-korrekturen.md` nachgetragen", ""]
    return "\n".join(z)


def protokoll_modul(m):
    z = ["# Modul %d: %s – Protokoll" % (m["nr"], m["titel"]), "",
         "| Feld | Eintrag |", "|---|---|", "| Datum | |", "| Dauer (tatsächlich) | |",
         "| Umgebung / Versionen | |", "| Ausgangszustand (Checkpoint) | |", "| Endzustand (Checkpoint) | |", ""]
    for a in m["aufgaben"]:
        pre = "m%02d-a%d" % (m["nr"], a["nr"])
        z += ["## Aufgabe %d: %s" % (a["nr"], a["titel"]), "",
              "- Datum / Dauer: ",
              "- Durchführung (Kurzprotokoll, Abweichungen): ",
              "- Ausgabe / Ergebnis (Datei in `ausgaben/`): ",
              "- Belege: `screenshots/%s-<kurz>.png`" % pre,
              "- Ergebnis: [ ] erfüllt  [ ] mit Abweichung  [ ] nicht erfüllt"]
        for t in a["marker"]:
            z.append("- „%s“: %s  → [ ] bestätigt  [ ] korrigiert  [ ] Fehler" % (MARKER, t))
        z.append("")
    z += ["## Notizen", "", "(freier Text; Dateien in `notizen/`)", ""]
    return "\n".join(z)


FEHLER = """# Modul {nr}: {titel} – Fehlerprotokoll

| Nr | Datum | Aufgabe | Symptom / Meldung | Ursache | Lösung | Dauer | Beleg |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
"""


def uebersicht(kid, titel, module, lab_vorhanden):
    z = ["# Umsetzung: %s" % titel, "",
         "Lehrplan: `lehrplaene/%s` im Repository `lehrplan-prompts`." % kid, "",
         "## Fortschritt", "",
         "| Ordner | Modul | UE | Aufgaben | Fragen | Befehle „%s“ | Erledigt |" % MARKER,
         "|---|---|---|---|---|---|---|"]
    if lab_vorhanden:
        z.append("| `00-labor-setup` | Labor-Setup | | | | | [ ] |")
    for m in module:
        z.append("| `%s` | %s | %s | %d | %d | %d | [ ] |" % (
            modul_ordner(m), m["titel"], m["zeit"], len(m["aufgaben"]), len(m["fragen"]),
            sum(a["anzahl"] for a in m["aufgaben"])))
    z += ["| `99-abschluss` | Abschluss | | | | | [ ] |", "",
          "## Ablage", "",
          "Jeder Modulordner enthält `checkliste.md`, `protokoll.md`, `fehlerprotokoll.md` und die Ordner",
          "`screenshots/`, `notizen/` und `ausgaben/` (Konsolenausgaben, Konfigurationsdateien, Exporte).", "",
          "Screenshot-Namen: `mNN-aN-<kurz>.png`, zum Beispiel `m04-a2-diskpart-ergebnis.png`.", "",
          "## Vor dem Veröffentlichen", "",
          "- Keine Kennwörter, Lizenzschlüssel, echten Namen oder Adressen in Screenshots und Ausgaben.",
          "- Erst `99-abschluss/checkliste.md` abarbeiten, dann Status in `daten/kurse.json` auf „aufbereitet“ setzen.", ""]
    return "\n".join(z)


def nicht_bestaetigt(kid, module):
    z = ["# Befehle und Angaben mit „%s“" % MARKER, "",
         "Quelle: `lehrplaene/%s`. Jede Zeile nach dem Ausführen ausfüllen." % kid, "",
         "| Modul | Aufgabe | Stelle im Lehrplan | Version / Umgebung | Datum | Ergebnis (bestätigt / korrigiert / Fehler) | Notiz |",
         "|---|---|---|---|---|---|---|"]
    n = 0
    for m in module:
        for a in m["aufgaben"]:
            for t in a["marker"]:
                n += 1
                z.append("| %d | %d | %s | | | | |" % (m["nr"], a["nr"], t.replace("|", "\\|")))
    z += ["", "Gefunden: %d Stellen in den Praxisaufgaben (weitere stehen in den Abschnitten Quellen, Labor-Setup und Prüfvermerk)." % n, ""]
    return "\n".join(z)


def lade_fach(kid):
    """Fach K01-K16 aus daten/faecher.json; liefert (Fach, Module im Format der Lehrpläne)."""
    faecher = json.loads((ROOT / "daten" / "faecher.json").read_text(encoding="utf-8"))
    fach = next((f for f in faecher if f["id"] == kid), None)
    if fach is None:
        sys.exit("Fehler: kein Fach %s in daten/faecher.json" % kid)
    module = [{"nr": m["nr"], "titel": m["titel"], "zeit": "ca. %s h" % ("%g" % m["stunden"]).replace(".", ",")}
              for m in fach["module"]]
    return fach, module


def quelle_fach(fach):
    z = "`faecher/%s-%s.md` im Repository `lehrplan-prompts`" % (fach["id"], fach["slug"])
    if fach["repo"]:
        z += ", Übungsmaterial im Repository `%s`" % fach["repo"]
    return z


def checkliste_fach_modul(m, fach):
    return "\n".join([
        "# Modul %d: %s – Checkliste" % (m["nr"], m["titel"]), "",
        "Fach: %s (%s). Zeitaufwand %s. Quelle: %s." % (fach["titel"], fach["id"], m["zeit"], quelle_fach(fach)), "",
        "## Vorbereitung", "",
        "- [ ] Voraussetzung erfüllt: %s" % (fach["voraussetzung"] or "keine angegeben"),
        "- [ ] Laborumgebung bereit (siehe `../00-labor-setup/checkliste.md`)", "",
        "## Durcharbeiten", "",
        "- [ ] Skriptkapitel des Moduls gelesen",
        "- [ ] Übungen des Moduls durchgeführt (Aufgaben laut Skript, Belege in `screenshots/` und `ausgaben/`)",
        "- [ ] Lernziele laut Skript erreicht",
        "- [ ] Kontrollfragen laut Skript beantwortet", "",
        "## Abschluss", "",
        "- [ ] Screenshots und Ausgaben abgelegt, Dateinamen siehe `protokoll.md`",
        "- [ ] Kennwörter und echte Namen auf Screenshots geprüft",
        "- [ ] Fehler in `fehlerprotokoll.md` eingetragen",
        "- [ ] Abweichungen und Fehler im Skript in `../99-abschluss/lehrplan-korrekturen.md` nachgetragen", ""])


def protokoll_fach_modul(m):
    return "\n".join([
        "# Modul %d: %s – Protokoll" % (m["nr"], m["titel"]), "",
        "| Feld | Eintrag |", "|---|---|", "| Datum | |", "| Dauer (tatsächlich) | |",
        "| Umgebung / Versionen | |", "| Ausgangszustand (Checkpoint) | |", "| Endzustand (Checkpoint) | |", "",
        "## Übung 1: (Titel laut Skript)", "",
        "- Datum / Dauer: ",
        "- Durchführung (Kurzprotokoll, Abweichungen): ",
        "- Ausgabe / Ergebnis (Datei in `ausgaben/`): ",
        "- Belege: `screenshots/m%02d-a1-<kurz>.png`" % m["nr"],
        "- Ergebnis: [ ] erfüllt  [ ] mit Abweichung  [ ] nicht erfüllt", "",
        "(Block für weitere Übungen kopieren und die Nummer erhöhen.)", "",
        "## Notizen", "", "(freier Text; Dateien in `notizen/`)", ""])


def uebersicht_fach(fach, module):
    z = ["# Umsetzung: %s (%s)" % (fach["titel"], fach["id"]), "",
         "Quelle: %s." % quelle_fach(fach), "",
         "## Fortschritt", "",
         "| Ordner | Modul | Zeit | Erledigt |", "|---|---|---|---|",
         "| `00-labor-setup` | Labor-Setup | | [ ] |"]
    for m in module:
        z.append("| `%s` | %s | %s | [ ] |" % (modul_ordner(m), m["titel"], m["zeit"]))
    z += ["| `99-abschluss` | Abschluss | | [ ] |", "",
          "## Ablage", "",
          "Jeder Modulordner enthält `checkliste.md`, `protokoll.md`, `fehlerprotokoll.md` und die Ordner",
          "`screenshots/`, `notizen/` und `ausgaben/` (Konsolenausgaben, Konfigurationsdateien, Exporte).", "",
          "Screenshot-Namen: `mNN-aN-<kurz>.png`, zum Beispiel `m04-a2-diskpart-ergebnis.png`.", "",
          "## Vor dem Veröffentlichen", "",
          "- Keine Kennwörter, Lizenzschlüssel, echten Namen oder Adressen in Screenshots und Ausgaben.",
          "- Erst `99-abschluss/checkliste.md` abarbeiten.", ""]
    return "\n".join(z)


def schreibe_gemeinsam(ziel, bericht, abschluss_zeilen):
    ab = ziel / "99-abschluss"
    schreibe(ab / "checkliste.md", "\n".join(["# Abschluss – Checkliste", ""] + abschluss_zeilen + [""]), bericht)
    schreibe(ab / "lehrplan-korrekturen.md", "\n".join([
        "# Korrekturen am Lehrplan aus der Umsetzung", "",
        "| Nr | Modul / Aufgabe | Stelle im Lehrplan | Was war falsch oder fehlte | Korrektur | eingearbeitet |",
        "|---|---|---|---|---|---|", "| 1 | | | | | [ ] |", ""]), bericht)
    for u in UNTERORDNER:
        schreibe(ab / u / ".gitkeep", "", bericht)


def main_fach(kid, ziel_basis):
    fach, module = lade_fach(kid)
    ziel = ziel_basis / ("%s-%s" % (fach["id"], fach["slug"]))
    ordner = [modul_ordner(m) for m in module]
    if len(ordner) != len(set(ordner)):
        sys.exit("Fehler: doppelte Modulordner in %s" % kid)
    bericht = []
    schreibe(ziel / "README.md", uebersicht_fach(fach, module), bericht)
    schreibe(ziel / "00-labor-setup" / "checkliste.md", "\n".join([
        "# Labor-Setup – Checkliste", "",
        "Quelle: Skript des Fachs (%s). Das Labor-Setup steht im ersten Kapitel bzw. in der Einleitung." % quelle_fach(fach), "",
        "## Bestandteile", "",
        "- [ ] Labor-Setup gemäß Skript vorbereitet (Einzelpunkte hier eintragen)", "",
        "## Ist-Werte", "", "| Bezeichnung | Ist-Wert | Anmerkung |", "|---|---|---|", "| | | |", ""]), bericht)
    for u in UNTERORDNER:
        schreibe(ziel / "00-labor-setup" / u / ".gitkeep", "", bericht)
    for m in module:
        o = ziel / modul_ordner(m)
        schreibe(o / "checkliste.md", checkliste_fach_modul(m, fach), bericht)
        schreibe(o / "protokoll.md", protokoll_fach_modul(m), bericht)
        schreibe(o / "fehlerprotokoll.md", FEHLER.format(nr=m["nr"], titel=m["titel"]), bericht)
        for u in UNTERORDNER:
            schreibe(o / u / ".gitkeep", "", bericht)
    schreibe_gemeinsam(ziel, bericht, [
        "- [ ] Alle Modulchecklisten abgehakt",
        "- [ ] Korrekturen am Skript in `lehrplan-korrekturen.md` gesammelt und eingearbeitet",
        "- [ ] Screenshots und Ausgaben auf Kennwörter, Schlüssel und echte Namen geprüft",
        "- [ ] Entscheidung: Übungsmaterial in das Fach-Repository übernehmen (öffentlich oder privat, Lizenz)",
        "- [ ] Fach im Excel-Stundenplan als erledigt markiert"])
    print("Angelegt: %s (%d Module)" % (ziel, len(module)))
    for b in bericht:
        print("Hinweis:", b)


def lade_reihe(eid):
    reihen = json.loads((ROOT / "daten" / "uebungen.json").read_text(encoding="utf-8"))
    r = next((x for x in reihen if x["id"] == eid), None)
    if r is None:
        sys.exit("Fehler: keine Übungsreihe %s in daten/uebungen.json" % eid)
    if not r.get("module"):
        sys.exit("Fehler: %s hat keinen Aufbau. Zuerst `python tools/uebungen_einlesen.py %s` ausführen." % (eid, eid))
    return r


def quelle_reihe(r):
    return "`uebungen/%s-%s.md` im Repository `lehrplan-prompts`, Material im Repository `%s`" % (r["id"], r["slug"], r["repo"])


def mit_material(r):
    return [m for m in r["module"] if m["einheiten"]]


def modul_name(m):
    return "Modul %d: %s" % (m["nr"], m["titel"]) if m["nr"] is not None else m["titel"]


def abschluss_modul(ordner_hinweis="../"):
    return ["", "## Abschluss", "",
            "- [ ] Screenshots und Ausgaben abgelegt, Dateinamen siehe `protokoll.md`",
            "- [ ] Kennwörter, echte Namen, Domains und Adressen auf Screenshots geprüft",
            "- [ ] Fehler in `fehlerprotokoll.md` eingetragen",
            "- [ ] Abweichungen von der Anleitung in `%s99-abschluss/lehrplan-korrekturen.md` nachgetragen" % ordner_hinweis, ""]


def checkliste_reihe_modul(r, m):
    z = ["# %s – Checkliste" % modul_name(m), "",
         "Reihe: %s (%s). Quelle: %s." % (r["titel"], r["id"], quelle_reihe(r)), ""]
    if r["art"] == "steps":
        z += ["## Steps", "", "Je Step: Anleitung lesen, nachbauen, Ergebnis prüfen, Beleg ablegen.", ""]
        for e in m["einheiten"]:
            z.append("- [ ] Step %s: %s (`%s`)" % (e["nr"], e["titel"], e["datei"]))
            for sk in e.get("skripte", []):
                z.append("  - [ ] Skript `%s` geprüft oder ausgeführt" % sk)
        z += ["", "## Gesamtprüfung des Moduls", "",
              "- [ ] Alle Steps real umgesetzt oder als „nur dokumentiert“ gekennzeichnet (siehe `protokoll.md`)",
              "- [ ] Zusammenspiel der Steps geprüft (Verbindung, Anmeldung, Test laut Anleitung)"]
        return "\n".join(z + abschluss_modul())
    for e in m["einheiten"]:
        z += ["## Übung %s: %s" % (e["nr"], e["titel"]), "",
              "Stufe: %s. Geschätzte Zeit: %s. Werkzeuge: %s." % (e["stufe"] or "?", e["zeit"] or "?", e["werkzeuge"] or "?"), "",
              "### Vorbereitung", ""]
        for v in e["voraussetzungen"]:
            z.append("- [ ] %s" % v)
        z += ["- [ ] Isolierte Testumgebung bereit, kein Zugriff auf Heimnetz oder produktive Systeme", ""]
        z += ["### Teile und Schritte", ""]
        for t in e["teile"]:
            z.append("**Teil %d: %s**" % (t["nr"], t["titel"]))
            z.append("")
            for s_ in t["schritte"]:
                z.append("- [ ] Schritt %s: %s" % (s_["nr"], s_["titel"]))
            z.append("")
        if m.get("skripte"):
            z += ["### Skripte", ""]
            for sk in m["skripte"]:
                z.append("- [ ] `%s`: %s" % (sk["datei"], kurz(sk["zweck"], 120)))
            z.append("")
        z += ["### Prüfen", "",
              "- [ ] Prüfbefehle laut Abschnitt „Prüfbefehle“ der Übung ausgeführt, Ausgabe in `ausgaben/` abgelegt",
              "- [ ] Ergebnis mit der Musterlösung verglichen (erst nach eigenem Versuch ansehen)", "",
              "### Lernziele (erreicht, wenn Schritt und Beleg vorliegen)", ""]
        for i, l in enumerate(e["lernziele"], 1):
            z.append("- [ ] Lernziel %d: %s" % (i, l))
        z += ["", "### Kontrollfragen", ""]
        for i, f in enumerate(e["kontrollfragen"], 1):
            z.append("- [ ] Frage %d beantwortet: %s" % (i, kurz(f, 120)))
        z += ["", "### Erweiterungen (optional)", "", "- [ ] Erweiterungen aus der Übung bearbeitet oder bewusst ausgelassen", ""]
    z += abschluss_modul()
    z.insert(-2, "- [ ] Stellen mit „nicht bestätigt“ in `../befehle-nicht-bestaetigt.md` nachgetragen")
    return "\n".join(z)


def protokoll_reihe_modul(r, m):
    z = ["# %s – Protokoll" % modul_name(m), "",
         "| Feld | Eintrag |", "|---|---|", "| Datum | |", "| Dauer (tatsächlich) | |",
         "| Umgebung / Versionen | |", "| Ausgangszustand (Checkpoint) | |", "| Endzustand (Checkpoint) | |", ""]
    if r["art"] == "steps":
        z += ["Screenshot-Namen: `m%02d-sN-<kurz>.png` (N = Step-Nummer).\n" % (m["nr"] or 0)]
        for e in m["einheiten"]:
            z += ["## Step %s: %s" % (e["nr"], e["titel"]), "",
                  "- Datum / Dauer: ",
                  "- Tatsächlich umgesetzt: [ ] ja  [ ] teilweise  [ ] nur dokumentiert / geplant",
                  "- Durchführung (Kurzprotokoll, Abweichungen von der Anleitung): ",
                  "- Ausgabe / Ergebnis (Datei in `ausgaben/`): ",
                  "- Belege: `screenshots/m%02d-s%s-<kurz>.png`" % (m["nr"] or 0, e["nr"].split(".")[-1]),
                  "- Ergebnis: [ ] erfüllt  [ ] mit Abweichung  [ ] nicht erfüllt", ""]
    else:
        z += ["Screenshot-Namen: `mNN-aN-<kurz>.png` (N = Nummer des Teils).", ""]
        for e in m["einheiten"]:
            for t in e["teile"]:
                z += ["## Teil %d: %s" % (t["nr"], t["titel"]), "",
                      "- Schritte: %s" % (", ".join(s_["nr"] for s_ in t["schritte"]) or "–"),
                      "- Datum / Dauer: ",
                      "- Durchführung (Kurzprotokoll, Abweichungen): ",
                      "- Ausgabe / Ergebnis (Datei in `ausgaben/`): ",
                      "- Belege: `screenshots/m%02d-a%d-<kurz>.png`" % (m["nr"], t["nr"]),
                      "- Ergebnis: [ ] erfüllt  [ ] mit Abweichung  [ ] nicht erfüllt"]
                for nb in e["nicht_bestaetigt"]:
                    if nb["teil"].startswith("Teil %d" % t["nr"]):
                        z.append("- „nicht bestätigt“: %s  → [ ] bestätigt  [ ] korrigiert  [ ] Fehler" % nb["text"])
                z.append("")
    z += ["## Notizen", "", "(freier Text; Dateien in `notizen/`)", ""]
    return "\n".join(z)


def uebersicht_reihe(r):
    z = ["# Umsetzung: %s (%s)" % (r["titel"], r["id"]), "", "Quelle: %s." % quelle_reihe(r), "",
         "## Fortschritt", "", "| Ordner | Modul | Einheiten | Erledigt |", "|---|---|---|---|",
         "| `00-labor-setup` | Labor-Setup | | [ ] |"]
    for m in r["module"]:
        if m["einheiten"]:
            z.append("| `%s` | %s | %d | [ ] |" % (m["ordner"], m["titel"], len(m["einheiten"])))
    z.append("| `99-abschluss` | Abschluss | | [ ] |")
    offen = [m for m in r["module"] if not m["einheiten"]]
    if offen:
        z += ["", "## Noch ohne Material im Repository", ""]
        for m in offen:
            z.append("- Modul %s: %s%s" % (m["nr"], m["titel"], (" – geplant: " + m["geplant"]) if m.get("geplant") else ""))
    z += ["", "## Ablage", "",
          "Jeder Modulordner enthält `checkliste.md`, `protokoll.md`, `fehlerprotokoll.md` und die Ordner",
          "`screenshots/`, `notizen/` und `ausgaben/`. Die Modulordner heißen wie im Repository.", "",
          "## Vor dem Veröffentlichen", "",
          "- Keine Kennwörter, Lizenzschlüssel, echten Namen, Domains oder Adressen in Screenshots und Ausgaben.",
          "- Erst `99-abschluss/checkliste.md` abarbeiten.", ""]
    return "\n".join(z)


def nicht_bestaetigt_reihe(r):
    z = ["# Befehle und Angaben mit „nicht bestätigt“ oder „sinngemäß“", "",
         "Quelle: Übungen der Reihe %s. Jede Zeile nach dem Ausführen ausfüllen." % r["id"], "",
         "| Modul | Übung | Teil | Stelle in der Anleitung | Version / Umgebung | Datum | Ergebnis (bestätigt / korrigiert / Fehler) |",
         "|---|---|---|---|---|---|---|"]
    n = 0
    for m in r["module"]:
        for e in m["einheiten"]:
            for nb in e.get("nicht_bestaetigt", []):
                n += 1
                z.append("| %s | %s | %s | %s | | | |" % (m["nr"], e["nr"], nb["teil"] or "–", nb["text"].replace("|", "\\|")))
    z += ["", "Gefunden: %d Stellen (Prüfbefehle, Hinweise und Erweiterungen eingeschlossen)." % n, ""]
    return "\n".join(z)


def main_reihe(eid, ziel_basis):
    r = lade_reihe(eid)
    ziel = ziel_basis / ("%s-%s" % (r["id"], r["slug"]))
    bericht = []
    schreibe(ziel / "README.md", uebersicht_reihe(r), bericht)
    if any(e.get("nicht_bestaetigt") for m in r["module"] for e in m["einheiten"]):
        schreibe(ziel / "befehle-nicht-bestaetigt.md", nicht_bestaetigt_reihe(r), bericht)
    z = ["# Labor-Setup – Checkliste", "", "Quelle: Voraussetzungen der Übungen (%s)." % quelle_reihe(r), "",
         "## Bestandteile", ""]
    gesehen = set()
    for m in r["module"]:
        for e in m["einheiten"]:
            for v in e.get("voraussetzungen", []):
                if v not in gesehen:
                    gesehen.add(v)
                    z.append("- [ ] %s" % v)
            if e.get("werkzeuge") and e["werkzeuge"] not in gesehen:
                gesehen.add(e["werkzeuge"])
                z.append("- [ ] Werkzeuge: %s" % e["werkzeuge"])
    if not gesehen:
        z.append("- [ ] Laborumgebung gemäß Modul 00 (Topologie, Ressourcen, Namenskonvention) vorbereitet")
    z += ["", "## Ist-Werte", "", "| Bezeichnung | Ist-Wert | Anmerkung |", "|---|---|---|", "| | | |", ""]
    schreibe(ziel / "00-labor-setup" / "checkliste.md", "\n".join(z), bericht)
    for u in UNTERORDNER:
        schreibe(ziel / "00-labor-setup" / u / ".gitkeep", "", bericht)
    for m in mit_material(r):
        o = ziel / m["ordner"]
        schreibe(o / "checkliste.md", checkliste_reihe_modul(r, m), bericht)
        schreibe(o / "protokoll.md", protokoll_reihe_modul(r, m), bericht)
        schreibe(o / "fehlerprotokoll.md", FEHLER.format(nr=m["nr"] if m["nr"] is not None else "A", titel=m["titel"]), bericht)
        for u in UNTERORDNER:
            schreibe(o / u / ".gitkeep", "", bericht)
    zeilen = ["- [ ] Alle Modulchecklisten abgehakt"]
    if any(e.get("nicht_bestaetigt") for m in r["module"] for e in m["einheiten"]):
        zeilen.append("- [ ] `../befehle-nicht-bestaetigt.md` vollständig ausgefüllt")
    zeilen += ["- [ ] Korrekturen an der Anleitung in `lehrplan-korrekturen.md` gesammelt und im Repository `%s` eingearbeitet" % r["repo"],
               "- [ ] Screenshots und Ausgaben auf Kennwörter, Schlüssel, echte Namen und Domains geprüft"]
    if r["art"] == "steps":
        zeilen.append("- [ ] Lebenslauf: nur real Umgesetztes als umgesetzt nennen, den Rest als geplant (siehe Protokolle)")
    schreibe_gemeinsam(ziel, bericht, zeilen)
    print("Angelegt: %s (%d Module)" % (ziel, len(mit_material(r))))
    for b in bericht:
        print("Hinweis:", b)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pid = sys.argv[1].upper()
    if re.match(r"E\d+$", pid):
        pid = "E%02d" % int(pid[1:])
        return main_reihe(pid, pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT.parent / "Umsetzung")
    if re.match(r"K\d+$", pid):
        pid = "K%02d" % int(pid[1:])
        return main_fach(pid, pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT.parent / "Umsetzung")
    treffer = sorted((ROOT / "lehrplaene").glob(pid + "-*.md"))
    if not treffer:
        sys.exit("Fehler: keine Datei lehrplaene/%s-*.md" % pid)
    datei = treffer[0]
    ziel_basis = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT.parent / "Umsetzung"
    titel, lab, module = lade_lehrplan(datei)
    if not module:
        sys.exit("Fehler: keine Module gefunden in %s" % datei.name)
    ziel = ziel_basis / datei.stem
    bericht = []
    cp = pruefpunkte(lab)
    punkte = labor_punkte(lab)

    schreibe(ziel / "README.md", uebersicht(datei.name, titel, module, True), bericht)
    schreibe(ziel / "befehle-nicht-bestaetigt.md", nicht_bestaetigt(datei.name, module), bericht)

    if True:
        z = ["# Labor-Setup – Checkliste", "", "Quelle: Abschnitt „Labor-Setup“ in `lehrplaene/%s`." % datei.name, "",
             "## Bestandteile", ""]
        for name, text in punkte:
            z.append("- [ ] **%s**: %s" % (name, text) if text else "- [ ] %s" % name)
        if not punkte:
            z.append("- [ ] Labor-Setup gemäß Abschnitt „Labor-Setup“ des Lehrplans vorbereitet (dort keine Einzelpunkte gegliedert)")
        if cp:
            z += ["", "## Prüfpunkte (Checkpoints)", ""] + ["- [ ] `%s`" % c for c in cp]
        tab = tabellen(lab)
        if tab:
            z += ["", "## Soll-Werte aus dem Lehrplan", "", tab]
        z += ["", "## Ist-Werte", "", "| Bezeichnung | Ist-Wert | Anmerkung |", "|---|---|---|", "| | | |", ""]
        schreibe(ziel / "00-labor-setup" / "checkliste.md", "\n".join(z), bericht)
        for u in UNTERORDNER:
            schreibe(ziel / "00-labor-setup" / u / ".gitkeep", "", bericht)

    for m in module:
        ordner = ziel / modul_ordner(m)
        mit = [c for c in cp if any(c in t for a in m["aufgaben"] for t in a["text"])
               or c in m["voraus"]]
        schreibe(ordner / "checkliste.md", checkliste_modul(m, mit, datei.name), bericht)
        schreibe(ordner / "protokoll.md", protokoll_modul(m), bericht)
        schreibe(ordner / "fehlerprotokoll.md", FEHLER.format(nr=m["nr"], titel=m["titel"]), bericht)
        for u in UNTERORDNER:
            schreibe(ordner / u / ".gitkeep", "", bericht)

    ab = ziel / "99-abschluss"
    schreibe(ab / "checkliste.md", "\n".join([
        "# Abschluss – Checkliste", "",
        "- [ ] Alle Modulchecklisten abgehakt",
        "- [ ] `../befehle-nicht-bestaetigt.md` vollständig ausgefüllt",
        "- [ ] Korrekturen am Lehrplan in `lehrplan-korrekturen.md` gesammelt und in `lehrplaene/` eingearbeitet",
        "- [ ] Screenshots und Ausgaben auf Kennwörter, Schlüssel und echte Namen geprüft",
        "- [ ] Offene Punkte aus dem Prüfvermerk (Abschnitt C des Lehrplans) bearbeitet oder bewusst offen gelassen",
        "- [ ] Entscheidung: öffentlich oder privat, Lizenz (CC BY 4.0 für Texte, Code getrennt)",
        "- [ ] Status in `daten/kurse.json` auf „aufbereitet“, nach dem Push auf „gepusht“", ""]), bericht)
    schreibe(ab / "lehrplan-korrekturen.md", "\n".join([
        "# Korrekturen am Lehrplan aus der Umsetzung", "",
        "| Nr | Modul / Aufgabe | Stelle im Lehrplan | Was war falsch oder fehlte | Korrektur | eingearbeitet |",
        "|---|---|---|---|---|---|", "| 1 | | | | | [ ] |", ""]), bericht)
    for u in UNTERORDNER:
        schreibe(ab / u / ".gitkeep", "", bericht)

    print("Angelegt: %s (%d Module)" % (ziel, len(module)))
    for b in bericht:
        print("Hinweis:", b)


if __name__ == "__main__":
    main()
