#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt aus daten/kurse.json, daten/rahmen.json und rahmen/prompt-vorlage.txt
alle Dateien in prompts/ sowie die Tabelle in README.md.

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


def lade(pfad):
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def prompt_text(kurs, rahmen, vorlage):
    umfang = rahmen["umfang_klein"] if kurs["umfang"] == "klein" else rahmen["umfang_gross"]
    hinweis = kurs["hinweis"].strip()
    return vorlage.format(
        titel=kurs["titel"],
        zielgruppe=rahmen["zielgruppe"],
        vorkenntnisse=kurs["vorkenntnisse"],
        umfang=umfang,
        themen=kurs["themen"],
        abgrenzung=kurs["abgrenzung"].strip() or rahmen["abgrenzung_standard"],
        praxis=kurs["praxis"],
        hinweis_zeile=("Hinweis: " + hinweis + "\n") if hinweis else "",
    ).rstrip("\n")


def datei_name(kurs):
    return "%s-%s.md" % (kurs["id"], kurs["slug"])


def prompt_datei(kurs, rahmen, vorlage):
    return "# %s – %s\n\nPriorität %s, %s.\n\n```text\n%s\n```\n" % (
        kurs["id"], kurs["titel"], kurs["prio"], kurs["gruppe"],
        prompt_text(kurs, rahmen, vorlage))


def tabelle(kurse):
    zeilen = ["| Nr | Prio | Themengebiet | Kurs | Status | Prompt |",
              "|---|---|---|---|---|---|"]
    for i, k in enumerate(kurse, 1):
        zeilen.append("| %d | %s | %s | %s | %s | [%s](prompts/%s) |" % (
            i, k["prio"], k["gruppe"], k["titel"], k["status"], k["id"], datei_name(k)))
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
    neu = MARK_A + "\n" + tabelle(kurse) + "\n" + MARK_B
    readme.write_text(muster.sub(lambda m: neu, text), encoding="utf-8", newline="\n")
    print("%d Prompts und README-Tabelle erzeugt." % len(kurse))


if __name__ == "__main__":
    main()
