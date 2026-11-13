#!/usr/bin/env python3
"""Setzt GitHub-Topics bei Repositories, die noch keine haben.

Vorgaben stehen in daten/topics.json (je Repository eine Liste, dazu die
gemeinsamen Topics). Das Skript
  * liest alle Repositories des Besitzers mit der GitHub-CLI (gh),
  * setzt Topics NUR dort, wo noch keine gesetzt sind (vorhandene bleiben),
  * meldet Repositories ohne Vorgabe, statt Topics zu erfinden,
  * ändert ohne --anwenden nichts (Trockenlauf).

Voraussetzung: GitHub-CLI installiert und angemeldet (gh auth login).

Aufruf:
  python tools/topics_setzen.py              Trockenlauf
  python tools/topics_setzen.py --anwenden   Topics wirklich setzen
  python tools/topics_setzen.py --besitzer NAME --datei PFAD
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

TOPIC_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")  # GitHub: Kleinbuchstaben, Ziffern, Bindestrich, max. 50 Zeichen
MAX_TOPICS = 20                                       # GitHub: höchstens 20 Topics je Repository


def gh(*args):
    """Ruft gh auf und gibt die Standardausgabe zurück; bricht bei Fehlern ab."""
    try:
        r = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    except FileNotFoundError:
        sys.exit("Fehler: gh (GitHub-CLI) wurde nicht gefunden. Installieren und mit „gh auth login“ anmelden.")
    if r.returncode != 0:
        sys.exit(f"Fehler bei „gh {' '.join(args)}“:\n{r.stderr.strip()}")
    return r.stdout


def topics_von(eintrag):
    """Topic-Namen aus dem Feld repositoryTopics (kann null sein)."""
    roh = eintrag.get("repositoryTopics") or []
    namen = []
    for t in roh:
        namen.append(t["name"] if isinstance(t, dict) and "name" in t else (t.get("topic", {}).get("name") if isinstance(t, dict) else t))
    return [n for n in namen if n]


def vorgabe(name, cfg):
    """Topic-Liste für ein Repository laut Konfiguration oder None."""
    spezifisch = cfg["repos"].get(name)
    if spezifisch is None:
        return None
    liste = [] if name in cfg.get("ohne_gemeinsam", []) else list(cfg.get("gemeinsam", []))
    for t in spezifisch:
        if t not in liste:
            liste.append(t)
    return liste


def pruefen(cfg):
    """Prüft die Konfiguration auf gültige Topic-Namen und die Obergrenze."""
    fehler = []
    for name in cfg["repos"]:
        liste = vorgabe(name, cfg)
        if len(liste) > MAX_TOPICS:
            fehler.append(f"{name}: {len(liste)} Topics (höchstens {MAX_TOPICS})")
        for t in liste:
            if not TOPIC_RE.match(t):
                fehler.append(f"{name}: ungültiges Topic „{t}“")
    return fehler


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--anwenden", action="store_true", help="Topics wirklich setzen (ohne: Trockenlauf)")
    ap.add_argument("--besitzer", help="GitHub-Konto (Standard: Wert aus der Konfigurationsdatei)")
    ap.add_argument("--datei", default=str(Path(__file__).resolve().parent.parent / "daten" / "topics.json"),
                    help="Konfigurationsdatei (Standard: daten/topics.json)")
    a = ap.parse_args()

    cfg = json.loads(Path(a.datei).read_text(encoding="utf-8"))
    besitzer = a.besitzer or cfg["besitzer"]
    fehler = pruefen(cfg)
    if fehler:
        sys.exit("Konfiguration fehlerhaft:\n  " + "\n  ".join(fehler))

    daten = json.loads(gh("repo", "list", besitzer, "--limit", "300", "--json",
                          "name,repositoryTopics,isArchived,visibility"))
    print(f"{len(daten)} Repositories von {besitzer} gefunden. {'ANWENDEN' if a.anwenden else 'Trockenlauf (es wird nichts geändert)'}\n")

    gesetzt, uebersprungen, ohne_vorgabe, archiviert = [], [], [], []
    for e in sorted(daten, key=lambda x: x["name"]):
        name = e["name"]
        if name in cfg.get("ignorieren", []):
            continue
        if e.get("isArchived"):
            archiviert.append(name)
            continue
        vorhanden = topics_von(e)
        if vorhanden:
            uebersprungen.append((name, vorhanden))
            continue
        neu = vorgabe(name, cfg)
        if neu is None:
            ohne_vorgabe.append(name)
            continue
        print(f"[{'setze' if a.anwenden else 'würde setzen'}] {name}: {', '.join(neu)}")
        if a.anwenden:
            args = ["repo", "edit", f"{besitzer}/{name}"]
            for t in neu:
                args += ["--add-topic", t]
            gh(*args)
        gesetzt.append(name)

    print()
    for name, t in uebersprungen:
        print(f"[hat schon Topics, unverändert] {name}: {', '.join(t)}")
    for name in ohne_vorgabe:
        print(f"[keine Vorgabe in topics.json, übersprungen] {name}")
    for name in archiviert:
        print(f"[archiviert, übersprungen] {name}")
    print(f"\nErgebnis: {len(gesetzt)} {'gesetzt' if a.anwenden else 'würden gesetzt'}, "
          f"{len(uebersprungen)} unverändert (hatten Topics), {len(ohne_vorgabe)} ohne Vorgabe.")
    if not a.anwenden and gesetzt:
        print("Zum Setzen: python tools/topics_setzen.py --anwenden")


if __name__ == "__main__":
    main()
