#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liest den Aufbau der eigenen Uebungsreihen E01-E06 aus ihren lokalen Repository-Ordnern
und schreibt ihn in daten/uebungen.json (Feld "module").

Handgepflegt in daten/uebungen.json: id, titel, slug, thema, repo, lokal (Ordner des Repositories).
Erzeugt wird: je Modul die Einheiten (E01: Steps; E02-E06: Uebungen mit Teilen, Schritten, Lernzielen,
Kontrollfragen, Skripten und Stellen mit "nicht bestaetigt").

Aufruf (im Repository-Ordner):
    python tools/uebungen_einlesen.py                  # alle Reihen, Ordner aus dem Feld "lokal"
    python tools/uebungen_einlesen.py E03              # nur eine Reihe
    python tools/uebungen_einlesen.py E03 --pfad E03=D:\\Anderer\\Ordner

Danach: python tools/build_prompts.py. Nur Standardbibliothek, Python 3.8 oder neuer.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKER = ("nicht bestätigt", "sinngemäß")


def kurz(text, n=200):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def ohne_md(text):
    """Entfernt Links, Fettdruck und Backticks fuer Titel."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*`]", "", text).strip()


def lies(pfad):
    return pathlib.Path(pfad).read_text(encoding="utf-8")


def abschnitt(zeilen, kopf, stufe="## "):
    """Zeilen zwischen der Ueberschrift 'kopf' und der naechsten Ueberschrift gleicher Stufe."""
    aus, ein = [], False
    for z in zeilen:
        if z.startswith(stufe) and not z.startswith(stufe + "#"):
            if ein:
                break
            ein = z[len(stufe):].strip().startswith(kopf)
            continue
        if ein:
            aus.append(z)
    return aus


def punkte(zeilen):
    erg = []
    for z in zeilen:
        h = re.match(r"- (.*)", z)
        if h:
            erg.append(kurz(h.group(1), 220))
    return erg


def lade_uebung(pfad):
    zeilen = lies(pfad).split("\n")
    u = {"datei": pathlib.Path(pfad).name, "titel": "", "stufe": "", "zeit": "", "werkzeuge": "",
         "voraussetzungen": [], "lernziele": [], "teile": [], "kontrollfragen": [], "nicht_bestaetigt": []}
    h = re.match(r"# (.*)", zeilen[0])
    u["titel"] = re.sub(r"^(Übung )?\d+\.\d+[:\s]+", "", h.group(1)).strip()
    for z in zeilen[:20]:
        k = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|$", z)
        if k:
            name, wert = k.group(1), ohne_md(k.group(2))
            if name == "Stufe":
                u["stufe"] = wert
            elif name.startswith("Geschätzte Zeit"):
                u["zeit"] = wert
            elif name.startswith("Werkzeug"):
                u["werkzeuge"] = wert
    u["lernziele"] = punkte(abschnitt(zeilen, "Lernziele"))
    u["voraussetzungen"] = punkte(abschnitt(zeilen, "Voraussetzungen"))
    # Teile und Schritte aus "## Aufgabe"
    teil = None
    in_code = False
    for z in abschnitt(zeilen, "Aufgabe"):
        if z.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        t = re.match(r"### Teil (\d+): (.*)", z)
        if t:
            teil = {"nr": int(t.group(1)), "titel": t.group(2).strip(), "schritte": []}
            u["teile"].append(teil)
            continue
        s = re.match(r"\*\*(\d+(?:\.\d+)?)\.? (.+?)\*\*:?", z) or re.match(r"\*\*(\d+(?:\.\d+)?)\.? ([^*]+?):\*\*", z)
        if s:
            if teil is None:
                teil = {"nr": 1, "titel": "Aufgabe", "schritte": []}
                u["teile"].append(teil)
            teil["schritte"].append({"nr": s.group(1), "titel": ohne_md(s.group(2)).rstrip(":")})
    # Kontrollfragen
    ein = False
    for z in zeilen:
        if z.startswith("**Kontrollfragen"):
            ein = True
            continue
        if ein:
            if z.startswith("## "):
                break
            f = re.match(r"\d+\. (.*)", z)
            if f:
                u["kontrollfragen"].append(kurz(f.group(1), 220))
    # Stellen "nicht bestaetigt"
    teil_name = ""
    for z in zeilen:
        t = re.match(r"### (Teil \d+.*)", z)
        if t:
            teil_name = t.group(1)
        if z.startswith("> ") or z.startswith("|") and "**Stand" in z:
            continue
        if any(m in z for m in MARKER) and not z.startswith(">"):
            u["nicht_bestaetigt"].append({"teil": teil_name, "text": kurz(z.strip(), 220)})
    return u


def lade_skripte(readme):
    """Zeilen '| `datei` | Zweck |' aus der Modul-README."""
    erg = []
    for z in lies(readme).split("\n"):
        k = re.match(r"\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|$", z)
        if k:
            erg.append({"datei": k.group(1), "zweck": kurz(k.group(2), 200)})
    return erg


def lade_modul_readme(readme):
    text = lies(readme)
    zeilen = text.split("\n")
    kopf = re.match(r"# Modul (\d+): (.*)", zeilen[0])
    nr, titel = (int(kopf.group(1)), kopf.group(2).strip()) if kopf else (None, zeilen[0].lstrip("# ").strip())
    beschr = next((z.strip("* ") for z in zeilen[1:6] if z.startswith("*")), "")
    steps = []
    for z in zeilen:
        k = re.match(r"\|\s*(\d+\.\d+)\s*\|\s*\[(.*?)\]\((.*?)\)\s*\|", z)
        if k:
            steps.append({"nr": k.group(1), "titel": ohne_md(k.group(2)), "datei": k.group(3)})
    return nr, titel, beschr, steps


def ordner_titel(name):
    """'01-packet-tracer' -> 'Packet Tracer' (nur Notfall, wenn die README keinen Titel hat)."""
    return re.sub(r"^\d+-", "", name).replace("-", " ").title()


def einlesen_reihe(r, wurzel):
    wurzel = pathlib.Path(wurzel)
    module = []
    if r["art"] == "steps":  # E01: docs/NN-<slug>/README.md mit Step-Tabelle, scripts/README.md
        skripte = {}
        sr = wurzel / "scripts" / "README.md"
        if sr.exists():
            for z in lies(sr).split("\n"):
                k = re.match(r"\|\s*\[`([^`]+)`\]\([^)]*\)\s*\|\s*\[(\d+\.\d+)\]", z)
                if k:
                    skripte.setdefault(k.group(2), []).append("scripts/" + k.group(1))
        for ordner in sorted((wurzel / "docs").iterdir()):
            if not (ordner.is_dir() and (ordner / "README.md").exists()):
                continue
            nr, titel, beschr, steps = lade_modul_readme(ordner / "README.md")
            for s in steps:
                s["skripte"] = skripte.get(s["nr"], [])
            module.append({"nr": nr, "ordner": ordner.name, "titel": titel, "beschreibung": beschr,
                           "einheiten": steps})
        anhang = wurzel / "docs" / "anhang-remote-management.md"
        if anhang.exists():
            titel = re.match(r"# (.*)", lies(anhang).split("\n")[0]).group(1)
            module.append({"nr": None, "ordner": "anhang", "titel": ohne_md(titel), "beschreibung": "",
                           "einheiten": [{"nr": "A", "titel": ohne_md(titel), "datei": anhang.name, "skripte": []}]})
    else:  # E02-E06: NN-<slug>/README.md plus Uebungsdokumente 'NN.N-*.md'
        for ordner in sorted(p for p in wurzel.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
            readme = ordner / "README.md"
            nr = int(ordner.name[:2])
            titel = ordner_titel(ordner.name)
            beschr = ""
            if readme.exists():
                kopf = re.match(r"# Modul (\d+):? (.*)", lies(readme).split("\n")[0])
                if kopf:
                    titel = kopf.group(2).strip()
                for z in lies(readme).split("\n"):
                    if z.startswith("## Beschreibung"):
                        beschr = "(siehe README)"
            docs = sorted(ordner.glob("[0-9][0-9].[0-9]-*.md"))
            einheiten = []
            for d in docs:
                u = lade_uebung(d)
                u["nr"] = d.name[:4]
                einheiten.append(u)
            skripte = lade_skripte(readme) if readme.exists() else []
            geplant = ""
            if readme.exists():
                for z in lies(readme).split("\n"):
                    if z.startswith("Geplant:"):
                        geplant = z[len("Geplant:"):].strip()
            module.append({"nr": nr, "ordner": ordner.name, "titel": titel, "beschreibung": "",
                           "einheiten": einheiten, "skripte": skripte, "geplant": geplant})
    return module


def main():
    args = sys.argv[1:]
    pfade = {}
    ids = []
    i = 0
    while i < len(args):
        if args[i] == "--pfad":
            k, v = args[i + 1].split("=", 1)
            pfade[k.upper()] = v
            i += 2
        else:
            ids.append(args[i].upper())
            i += 1
    datei = ROOT / "daten" / "uebungen.json"
    reihen = json.loads(datei.read_text(encoding="utf-8"))
    for r in reihen:
        if ids and r["id"] not in ids:
            continue
        wurzel = pfade.get(r["id"], r["lokal"])
        if not pathlib.Path(wurzel).is_dir():
            print("Übersprungen %s: Ordner nicht gefunden: %s" % (r["id"], wurzel))
            continue
        r["module"] = einlesen_reihe(r, wurzel)
        n = sum(len(m["einheiten"]) for m in r["module"])
        print("%s: %d Module, %d Einheiten" % (r["id"], len(r["module"]), n))
    datei.write_text(json.dumps(reihen, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
