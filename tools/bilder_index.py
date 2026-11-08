#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt ein Verzeichnis aller Bilder in Markdown-Dateien eines Ordners.

Aufruf (im Repository-Ordner):
    python tools/bilder_index.py                     # Ordner: <Ordner ueber dem Repo>/Umsetzung
    python tools/bilder_index.py D:\\Umsetzung\\P46-betriebssystem-rollout-mdt-mecm-und-alternativen

Schreibt <Ordner>/bilder-index.md mit
  - Tabelle aller verlinkten Bilder (Ordner, Datei, Aufgabe, Beschreibung, Groesse, Link),
  - Bildern in Ordnern "screenshots", die nirgends verlinkt sind,
  - Links auf Bilder, die es nicht gibt,
  - Bildern ueber 1 MB.
Bilder werden nie veraendert. Die Datei bilder-index.md wird bei jedem Lauf neu geschrieben.
Nur Standardbibliothek, Python 3.8 oder neuer.
"""
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENDUNGEN = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}
GRENZE = 1024 * 1024
INDEX = "bilder-index.md"
BILD = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def rel(pfad, basis):
    r = pathlib.Path(pfad).resolve().relative_to(basis.resolve())
    return urllib.parse.quote(r.as_posix())


def kb(n):
    return "%.0f KB" % (n / 1024) if n < GRENZE else "%.1f MB" % (n / GRENZE)


def lies_bilder(md):
    """Liefert (Zeilennummer, Aufgabe/Abschnitt, Alt, Ziel) fuer jedes Bild, Codebloecke ausgenommen."""
    treffer, ueberschrift, code = [], "", False
    for nr, zeile in enumerate(md.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
        if zeile.lstrip().startswith("```"):
            code = not code
            continue
        if code:
            continue
        h = re.match(r"#{1,6}\s+(.*)", zeile)
        if h:
            ueberschrift = h.group(1).strip()
        for m in BILD.finditer(zeile):
            treffer.append((nr, ueberschrift, m.group(1).strip(), m.group(2)))
    return treffer


def main():
    basis = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "Umsetzung"
    if not basis.is_dir():
        sys.exit("Fehler: Ordner nicht gefunden: %s" % basis)
    basis = basis.resolve()

    verlinkt, fehlend, zeilen = set(), [], []
    for md in sorted(basis.rglob("*.md")):
        if md.name == INDEX:
            continue
        for nr, abschnitt, alt, ziel in lies_bilder(md):
            if re.match(r"[a-z]+://", ziel, re.I):
                continue
            pfad = (md.parent / urllib.parse.unquote(ziel.split("#")[0])).resolve()
            ort = md.parent.relative_to(basis).as_posix() or "."
            if pfad.is_file():
                verlinkt.add(pfad)
                zeilen.append((ort, md.name, abschnitt, alt or "(ohne Beschreibung)",
                               pfad.stat().st_size, rel(pfad, basis), pfad.name))
            else:
                fehlend.append((md.relative_to(basis).as_posix(), nr, ziel))

    vorhanden = [p.resolve() for p in basis.rglob("*") if p.is_file()
                 and p.suffix.lower() in ENDUNGEN and "screenshots" in p.parts]
    unverlinkt = sorted(p for p in vorhanden if p not in verlinkt)
    gross = sorted(((p, p.stat().st_size) for p in vorhanden if p.stat().st_size > GRENZE),
                   key=lambda x: -x[1])

    z = ["# Bilder-Index", "",
         "Automatisch erzeugt mit `tools/bilder_index.py`, nicht von Hand ändern.", "",
         "- Verlinkte Bilder: %d" % len(zeilen),
         "- Bilder ohne Verlinkung: %d" % len(unverlinkt),
         "- Links auf fehlende Bilder: %d" % len(fehlend),
         "- Bilder über 1 MB: %d" % len(gross), ""]
    z += ["## Verlinkte Bilder", "",
          "| Ordner | Datei | Abschnitt | Beschreibung | Größe | Bild |", "|---|---|---|---|---|---|"]
    for ort, md, abschnitt, alt, groesse, link, name in zeilen:
        z.append("| %s | %s | %s | %s | %s | [%s](%s) |" % (
            ort, md, abschnitt.replace("|", "\\|"), alt.replace("|", "\\|"), kb(groesse), name, link))
    if not zeilen:
        z.append("| | | | (keine Bilder verlinkt) | | |")
    z += ["", "## Bilder ohne Verlinkung", ""]
    z += ["- [%s](%s)" % (p.relative_to(basis).as_posix(), rel(p, basis)) for p in unverlinkt] or ["keine"]
    z += ["", "## Links auf fehlende Bilder", ""]
    z += ["- `%s`, Zeile %d: `%s`" % f for f in fehlend] or ["keine"]
    z += ["", "## Bilder über 1 MB", ""]
    z += ["- [%s](%s) (%s)" % (p.relative_to(basis).as_posix(), rel(p, basis), kb(s)) for p, s in gross] or ["keine"]
    (basis / INDEX).write_text("\n".join(z) + "\n", encoding="utf-8", newline="\n")
    print("Geschrieben: %s (%d Bilder, %d unverlinkt, %d fehlend, %d über 1 MB)" % (
        basis / INDEX, len(zeilen), len(unverlinkt), len(fehlend), len(gross)))


if __name__ == "__main__":
    main()
