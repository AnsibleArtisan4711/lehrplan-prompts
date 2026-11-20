# Lehrplan: PowerShell Desired State Configuration (DSC)

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); PowerShell-Kenntnisse |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Konzept deklarativer Konfiguration, DSC-Konfigurationen und Ressourcen, Local Configuration Manager, Push und Pull, eigene Ressourcen, Prüfen auf Abweichungen, Einordnung gegenüber Ansible und Gruppenrichtlinien |
| **Thematische Abgrenzung (Out of Scope)** | **PowerShell und DSC wurden nicht ausgeführt** (nicht installierbar im Cloud-Container, kein Windows). Gezeigt wird ein **Lernmodell in Python** (`dscsim.py`) mit den Ressourcentypen `File`, `Setting` und `Service` (Dateien und JSON-Dateien statt Windows), einem LCM-Modell, Pull-Verzeichnis und Drift-Prüfung. **PowerShell-Beispiele in den Skripten sind Text, nicht ausgeführt und in der Syntax nicht geprüft.** Die PowerShell-Grundlagen stehen im vorhandenen Kurs „PowerShell“. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Konzept der deklarativen Konfiguration | 1 | 12 |
| 2 | Konfigurationen und Ressourcen | 1 | 14 |
| 3 | Local Configuration Manager (LCM) | 1 | 12 |
| 4 | Push und Pull | 1 | 14 |
| 5 | Eigene Ressourcen | 1 | 12 |
| 6 | Auf Abweichungen prüfen und korrigieren | 1 | 14 |
| 7 | Einordnung gegenüber Ansible, Gruppenrichtlinien und Microsoft DSC 3 | 2 | 10 |
| 8 | Abschlussprojekt | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Einordnung gegenüber Ansible, Gruppenrichtlinien und Microsoft DSC 3). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Stand der DSC-Versionen (20.11.2026, Unsicherheit gekennzeichnet):** Gelesen wurden nur Suchauszüge von Microsoft Learn (Übersichtsseiten zu DSC, zum Local Configuration Manager und zur Installation von DSC 3), nicht die vollständigen Seiten. Danach gibt es vier Versionen: **Microsoft DSC 3.0** (neu, plattformübergreifend, eigenständiges Programm ohne Abhängigkeit von PowerShell, Konfigurationen in JSON/YAML, **kein** LCM), **PowerShell DSC 3.0 (Vorschau)** für Azure Machine Configuration unter Linux, **PowerShell DSC 2.0** (seit PowerShell 7.2 nicht mehr im Paket, Modul `PSDesiredStateConfiguration` 2.0.5 aus dem PowerShell Gallery) und **PowerShell DSC 1.1** (ältere Version aus Windows PowerShell 5.1). Die Installationsseite nennt in ihren Downloadlinks 3.3.0-rc.2 (Release-Kandidat). **Nicht bestätigt:** Support- und Laufzeitende von DSC 1.1, die „Zukunft“ der Versionen, Lizenzen, Einzelheiten der Syntax. **Getestet mit (Ubuntu 24.04, Cloud-Container):** Python 3.13 mit PyYAML (Modell `dscsim.py`). **Nicht ausgeführt:** PowerShell, Windows PowerShell, DSC 1.1 und 3.x, Windows Server, Azure.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-DSC`, `10.60.0.0/24`).

**VM 1:** `dsc01` (**erforderlich**, `10.60.0.10`): Windows Server als Pull-Server und Ziel.

**VM 2:** `dsc02` (**erforderlich**, `10.60.0.11`): weiterer Windows-Zielserver.

**Internetphase:** Für Updates und Module braucht `dsc01` vorübergehend Internetzugang; danach wird er entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 4 und Modul 6 von beiden VMs einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux mit dem Modell `dscsim.py` und arbeiten unter `/tmp/p24`; sie brauchen weder Windows noch PowerShell. Im Labor ersetzt man die Modell-Befehle durch die entsprechenden PowerShell-Cmdlets (nicht geprüft).

## B. Detaillierter Modulaufbau

### Modul 1: Konzept der deklarativen Konfiguration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende imperative und deklarative Konfiguration unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Get, Test und Set als Operationen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Idempotenz an einem Beispiel zeigen.
  * Nach Abschluss dieses Moduls kann der Lernende den Stand der DSC-Versionen mit Datum wiedergeben und Unsicherheit benennen.
* **Voraussetzungen:** PowerShell-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Imperativ und deklarativ | 4 |
| 1.2 | Get, Test, Set | 4 |
| 1.3 | Versionen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Imperativ und deklarativ (Einheit 1.1):** Führen Sie `bash konzept.sh` aus. Erklären Sie Schritt 1 und 2: Warum wächst die Datei im imperativen Skript, aber nicht bei der deklarativen Konfiguration?
2. **Get, Test, Set (Einheit 1.2):** Erklären Sie Schritt 3 und 4: Was liefern Test, Set und Get, und warum ändert der zweite Lauf nichts?
3. **Versionen (Einheit 1.3):** Erklären Sie Schritt 5: Welche vier Versionen von DSC werden genannt, und was ist nicht bestätigt?

#### Kontrollfragen

1. Was ist der Unterschied zwischen imperativ und deklarativ?
2. Was macht Test?
3. Welche vier DSC-Versionen werden genannt?
4. Was ist über die Zukunft von DSC 1.1 bekannt?

### Modul 2: Konfigurationen und Ressourcen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Konfiguration mit mehreren Ressourcen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Abhängigkeiten (`dependsOn`) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Kompilieren und Prüfsumme beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler beim Kompilieren deuten.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Reihenfolge | 6 |
| 2.2 | Prüfsumme | 4 |
| 2.3 | Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Reihenfolge (Einheit 2.1):** Führen Sie `bash konfiguration.sh` aus. Erklären Sie Schritt 1 bis 3: Warum steht `File/Startseite` im Ergebnis vor `Service/Web`?
2. **Prüfsumme (Einheit 2.2):** Erklären Sie die Prüfsummendatei in Schritt 2: Wozu dient sie (Hinweis Modul 4)?
3. **Fehler (Einheit 2.3):** Erklären Sie Schritt 4 bis 7: Welche Fehler meldet das Modell, und wie lauten sie?

#### Kontrollfragen

1. Wie wird die Reihenfolge bestimmt?
2. Was enthält die Prüfsummendatei?
3. Was meldet das Modell bei einem Zyklus?
4. Wie meldet es einen unbekannten Typ?

### Modul 3: Local Configuration Manager (LCM)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aufgabe des LCM erklären.
  * Nach Abschluss dieses Moduls kann der Lernende RefreshMode, ConfigurationMode und RefreshFrequencyMins unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Einstellungen im Modell setzen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende gelesene Quellen von Fachwissen trennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Vorgaben | 4 |
| 3.2 | Fehlerfälle | 4 |
| 3.3 | Quellen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorgaben (Einheit 3.1):** Führen Sie `bash lcm.sh` aus. Beschreiben Sie anhand von Schritt 1 und 2 die Vorgabewerte und die Änderungen.
2. **Fehlerfälle (Einheit 3.2):** Erklären Sie Schritt 3: Welche Werte lässt das Modell nicht zu?
3. **Quellen (Einheit 3.3):** Erklären Sie Schritt 4: Welche Angaben stammen aus Microsoft Learn (Suchauszug), welche sind Fachwissen?

#### Kontrollfragen

1. Welche Vorgaben hat das Modell?
2. Welche Werte nennt die Dokumentation für RefreshMode?
3. Welche Werte hat ConfigurationMode?
4. Hat Microsoft DSC 3.0 einen LCM?

### Modul 4: Push und Pull

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Push und Pull unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Pull-Verzeichnis mit Konfiguration und Prüfsumme bereitstellen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Aktualisierung der Konfiguration nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerfälle (Prüfsumme, fehlende Datei) deuten.
* **Voraussetzungen:** Modul 2; Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Push | 6 |
| 4.2 | Pull | 4 |
| 4.3 | Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Push (Einheit 4.1):** Führen Sie `bash pushpull.sh` aus. Erklären Sie Schritt 1: Wie wird die Konfiguration angewendet?
2. **Pull (Einheit 4.2):** Erklären Sie Schritt 2 bis 4: Wie holt der Knoten die Konfiguration, und was geschieht bei einer neuen Fassung?
3. **Fehler (Einheit 4.3):** Erklären Sie Schritt 5 und 6: Warum wird die Konfiguration nicht übernommen?

#### Kontrollfragen

1. Wie unterscheiden sich Push und Pull?
2. Was passiert beim zweiten Abfragen?
3. Was zeigt die neue Fassung?
4. Was meldet das Modell bei beschädigter Datei?

### Modul 5: Eigene Ressourcen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer eigenen Ressource (Get, Test, Set) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine eigene Ressource im Modell einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Anforderungen an Test und Set nennen.
  * Nach Abschluss dieses Moduls kann der Lernende das PowerShell-Gegenstück beschreiben (als Fachwissen).
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Aufbau | 4 |
| 5.2 | Einsatz | 4 |
| 5.3 | Regeln | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbau (Einheit 5.1):** Führen Sie `bash ressourcen.sh` aus. Erklären Sie Schritt 1: Welche drei Funktionen hat die Ressource, und was ist der Schlüssel?
2. **Einsatz (Einheit 5.2):** Erklären Sie Schritt 2 und 3: Warum ist der Typ zuerst unbekannt, und was ändert die Umgebungsvariable `DSC_MODULES`?
3. **Regeln (Einheit 5.3):** Erklären Sie Schritt 4 bis 6: Welche Regeln gelten für Test und Set?

#### Kontrollfragen

1. Welche Funktionen hat eine Ressource?
2. Was ist der Schlüssel der Ressource `Notiz`?
3. Was darf Test nicht tun?
4. Wie wird die Ressource im Modell bekannt gemacht?

### Modul 6: Auf Abweichungen prüfen und korrigieren

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Abweichungen (Drift) mit Test finden.
  * Nach Abschluss dieses Moduls kann der Lernende die Modi ApplyOnly, ApplyAndMonitor und ApplyAndAutoCorrect unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende den Rückgabecode des Tests deuten.
  * Nach Abschluss dieses Moduls kann der Lernende entscheiden, welche Knoten nur melden und welche korrigieren.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Drift herbeiführen | 6 |
| 6.2 | Die drei Modi | 4 |
| 6.3 | Bewertung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Drift herbeiführen (Einheit 6.1):** Führen Sie `bash drift.sh` aus. Erklären Sie Schritt 2 und 3: Welche Abweichungen entstehen, und wie meldet sie `test`?
2. **Die drei Modi (Einheit 6.2):** Erklären Sie Schritt 4 bis 6: Was bewirkt jeder Modus?
3. **Bewertung (Einheit 6.3):** Erklären Sie Schritt 8: Wann ist Abweichung kein Fehler?

#### Kontrollfragen

1. Welche Abweichungen entstehen?
2. Welchen Rückgabecode liefert `test` bei Abweichung?
3. Was macht ApplyAndMonitor?
4. Was macht ApplyAndAutoCorrect?

### Modul 7: Einordnung gegenüber Ansible, Gruppenrichtlinien und Microsoft DSC 3

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein DSC-3-Konfigurationsdokument (YAML) lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Ansible, Gruppenrichtlinien und DSC vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende sagen, was aus Quellen belegt und was Fachwissen ist.
  * Nach Abschluss dieses Moduls kann der Lernende die Auswahl von Randbedingungen abhängig machen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Dokument lesen | 4 |
| 7.2 | Vergleich | 3 |
| 7.3 | Quellenlage | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dokument lesen (Einheit 7.1):** Führen Sie `bash einordnung.sh` aus. Erklären Sie Schritt 1: Welche Ressourcen enthält das Dokument, und was ist an der Angabe nicht geprüft?
2. **Vergleich (Einheit 7.2):** Erklären Sie Schritt 3: Wie unterscheiden sich die Ansätze (Fachwissen)?
3. **Quellenlage (Einheit 7.3):** Erklären Sie Schritt 4: Was wurde gelesen, was nicht?

#### Kontrollfragen

1. Welche Typen nennt das Dokument?
2. Was ist an Schritt 1 nicht geprüft?
3. Wodurch unterscheidet sich Ansible von DSC?
4. Welche Empfehlung wird gegeben?

### Modul 8: Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Konfiguration mit eigener Ressource bereitstellen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Knoten im Pull-Modus mit AutoCorrect betreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Drift erkennen und korrigieren lassen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Abnahmeliste anwenden.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Bereitstellen | 4 |
| 8.2 | Drift | 4 |
| 8.3 | Abnahme | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bereitstellen (Einheit 8.1):** Führen Sie `bash abschluss.sh` aus. Erklären Sie Schritt 1 und 2: Welche vier Ressourcen hat die Konfiguration, und wie wird sie übernommen?
2. **Drift (Einheit 8.2):** Erklären Sie Schritt 3 und 4: Welche Abweichungen entstehen, und wie werden sie korrigiert?
3. **Abnahme (Einheit 8.3):** Erklären Sie Schritt 5: Was prüft die Abnahmeliste?

#### Kontrollfragen

1. Welche Ressourcen hat das Projekt?
2. Wie wird die Konfiguration übernommen?
3. Welche Abweichungen entstehen?
4. Was prüft die Abnahmeliste?
