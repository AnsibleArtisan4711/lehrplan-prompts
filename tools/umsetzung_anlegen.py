#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legt aus einem Lehrplan in lehrplaene/ einen Umsetzungsordner an: je Modul ein Unterordner
mit Checkliste, Protokollvorlage, Fehlerprotokoll und Ablageordnern fuer Screenshots, Notizen
und Ausgaben. Dazu eine Uebersicht, eine Liste der als "nicht bestaetigt" markierten Befehle
und ein Abschlussordner.

Aufruf (im Repository-Ordner):
    python tools/umsetzung_anlegen.py P46            # Ziel: <Ordner ueber dem Repo>/Umsetzung
    python tools/umsetzung_anlegen.py P46 D:\\Umsetzung

Vorhandene Dateien werden nie ueberschrieben (Hinweis in der Ausgabe), vorhandene Ordner
bleiben unveraendert. Nur Standardbibliothek, Python 3.8 oder neuer.
"""
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


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pid = sys.argv[1].upper()
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
