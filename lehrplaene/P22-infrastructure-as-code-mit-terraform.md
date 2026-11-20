# Lehrplan: Infrastructure as Code mit Terraform

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Grundlagen einer Cloud- oder Virtualisierungsplattform |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Konzept und HCL, Provider, Ressourcen und Datenquellen, Variablen und Ausgaben, Plan und Apply mit Abhängigkeitsgraph, State und Remote State, Module, Importieren, Zusammenspiel mit Ansible und cloud-init, Sicherheit der Zugangsdaten |
| **Thematische Abgrenzung (Out of Scope)** | **Terraform und OpenTofu wurden nicht ausgeführt.** Echt ist nur das Einlesen der HCL-Dateien (Bibliothek `python-hcl2`). Plan, Zustand, Abhängigkeiten, Apply, Import und Drift sind ein **Lernmodell in Python** (`tfsim.py`) mit genau einem Ressourcentyp (`local_file`). Die Ausgaben des Modells sind deutsch und **nicht** das Format des echten Werkzeugs. Providerspezifisches (Hyper-V, Proxmox, Cloud) wurde nicht getestet. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Konzept und die Sprache HCL | 1 | 12 |
| 2 | Provider, Ressourcen und Datenquellen | 1 | 12 |
| 3 | Variablen, lokale Werte und Ausgaben | 1 | 12 |
| 4 | Plan, Apply und der Abhängigkeitsgraph | 1 | 14 |
| 5 | State und Remote State | 1 | 14 |
| 6 | Module | 1 | 14 |
| 7 | Import und Zusammenspiel mit cloud-init und Ansible | 2 | 10 |
| 8 | Sicherheit der Zugangsdaten und Abschlussprojekt | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Import und Zusammenspiel mit cloud-init und Ansible). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Stand Lizenz und Fork (20.11.2026):** Nach einer Übersichtsseite (Wikipedia „OpenTofu“, vom Abrufwerkzeug zusammengefasst) stellte HashiCorp Terraform von der MPL auf die Business Source License (BUSL) um; im August 2023 entstand der Fork OpenTF, später OpenTofu, unter der MPL 2.0 bei der Linux Foundation. Dieselbe Seite nennt OpenTofu 1.12.3 (18.06.2026) als aktuelle Version; das kann inzwischen überholt sein. **Nicht geprüft:** der Wortlaut der Lizenzen, die aktuelle Terraform-Version, Preise und Nutzungsbedingungen, die Dokumentation beider Werkzeuge. **Getestet mit (Ubuntu 24.04, Cloud-Container):** Python 3.13 mit `python-hcl2` 8.2.0; Modul 7 zusätzlich `cloud-init` 26.2 (`cloud-init schema`) und `ansible-core` 2.22.0 (`ansible-inventory`). **Nicht ausgeführt:** Terraform, OpenTofu, Provider, Hyper-V, Proxmox, Cloud.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-IaC`, `10.40.0.0/24`).

**VM 1:** `iac01` (**erforderlich**, `10.40.0.10`): Ubuntu Server als Arbeitsplatz mit Terraform oder OpenTofu und Git.

**Ziel:** ein lokaler Virtualisierungshost (Hyper-V oder Proxmox) als Ziel der Ressourcen; ein Cloud-Konto nur optional (Testkonto, Kostenobergrenze setzen).

**Internetphase:** Für die Installation des Werkzeugs und der Provider braucht `iac01` vorübergehend Internetzugang; danach wird er entfernt. Zugangsdaten gehören nicht in den Quelltext (Modul 8).

**Prüfpunkt (Checkpoint):** Vor Modul 4 von `iac01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung; der Zustand (State) ist gesondert zu sichern.

**Skripte:** Die Skripte laufen unter Linux mit dem Modell `tfsim.py` und arbeiten unter `/tmp/p22`; sie brauchen weder die VM noch Terraform. Im Labor ersetzt man `tf …` durch `terraform …` bzw. `tofu …` und `local_file` durch einen Provider des Ziels.

## B. Detaillierter Modulaufbau

### Modul 1: Konzept und die Sprache HCL

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende deklarative Konfiguration von einem Skript abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer HCL-Datei (Blöcke, Attribute) lesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf validate, plan, apply beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Stand zu Lizenz und Fork mit Datum wiedergeben.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | HCL lesen | 4 |
| 1.2 | Ablauf | 4 |
| 1.3 | Fehler und Stand | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **HCL lesen (Einheit 1.1):** Führen Sie `bash konzept.sh` aus. Beschreiben Sie anhand von Schritt 1 und 2, welche Blöcke die Datei enthält und welche Attribute die Ressource hat.
2. **Ablauf (Einheit 1.2):** Erklären Sie Schritt 3 und 4: Was zeigen validate, plan und apply, und warum meldet der zweite Plan keine Änderung?
3. **Fehler und Stand (Einheit 1.3):** Erklären Sie Schritt 5 und 6: Was meldet der Parser bei fehlender Klammer, und was ist über Lizenz und Fork bekannt (mit Stand)?

#### Kontrollfragen

1. Was bedeutet deklarativ?
2. Welche Blöcke hat die Beispieldatei?
3. Was meldet der zweite Plan?
4. Was ist bei Lizenz und Fork zu beachten?

### Modul 2: Provider, Ressourcen und Datenquellen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ressourcen und Datenquellen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende mehrere Instanzen mit `count` erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende Reihenfolge mit Verweisen und `depends_on` steuern.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler bei fehlenden Daten und unbekannten Typen deuten.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Ressourcen und Datenquelle | 4 |
| 2.2 | count verkleinern | 4 |
| 2.3 | Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ressourcen und Datenquelle (Einheit 2.1):** Führen Sie `bash ressourcen.sh` aus. Erklären Sie Schritt 1 bis 3: Woher stammt der Inhalt von `knoten-2.txt`, und warum entsteht `uebersicht` zuletzt?
2. **count verkleinern (Einheit 2.2):** Erklären Sie Schritt 4: Was geschieht, wenn `anzahl` von 3 auf 2 sinkt?
3. **Fehler (Einheit 2.3):** Erklären Sie Schritt 5 und 6: Wann tritt der Fehler der Datenquelle auf, und was meldet das Modell bei einem unbekannten Typ?

#### Kontrollfragen

1. Was ist der Unterschied zwischen `resource` und `data`?
2. Wie heißen die Instanzen bei `count = 3`?
3. Was geschieht bei `anzahl=2`?
4. Wann wird die Datenquelle gelesen?

### Modul 3: Variablen, lokale Werte und Ausgaben

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Variablen mit Typ, Vorgabe und `sensitive` deklarieren.
  * Nach Abschluss dieses Moduls kann der Lernende Werte per `-var` übergeben.
  * Nach Abschluss dieses Moduls kann der Lernende lokale Werte und Ausgaben einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, dass sensible Werte im Zustand und in Zieldateien trotzdem lesbar sind.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Variablen | 4 |
| 3.2 | Sensible Werte | 4 |
| 3.3 | Änderungen und Typfehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Variablen (Einheit 3.1):** Führen Sie `bash variablen.sh` aus. Erklären Sie Schritt 1 und 2: Welche Variable hat keine Vorgabe, und was meldet das Modell ohne Wert?
2. **Sensible Werte (Einheit 3.2):** Erklären Sie Schritt 3 bis 5: Was wird im Plan und bei `output` verborgen, und was steht trotzdem in der Zieldatei?
3. **Änderungen und Typfehler (Einheit 3.3):** Erklären Sie Schritt 6 und 7: Warum wird die Ressource bei `umgebung=prod` ersetzt, und was meldet das Modell bei `anzahl=viele`?

#### Kontrollfragen

1. Was bewirkt `sensitive = true`?
2. Was passiert bei fehlendem Wert?
3. Warum wird `konfig` bei `prod` ersetzt?
4. Wie reagiert das Modell auf `anzahl=viele`?

### Modul 4: Plan, Apply und der Abhängigkeitsgraph

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Reihenfolge aus den Verweisen zwischen Ressourcen ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende Plan lesen: erstellen, ändern, ersetzen, löschen.
  * Nach Abschluss dieses Moduls kann der Lernende „bekannt nach apply“ erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Zyklen erkennen und auflösen.
* **Voraussetzungen:** Modul 2; Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Graph | 6 |
| 4.2 | Plan lesen | 4 |
| 4.3 | Ersetzen, Löschen, Zyklus | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Graph (Einheit 4.1):** Führen Sie `bash plan.sh` aus. Erklären Sie Schritt 1 und 2: Warum entsteht die Reihenfolge `db`, `app`, `start`, obwohl alle drei in beliebiger Reihenfolge stehen könnten?
2. **Plan lesen (Einheit 4.2):** Erklären Sie Schritt 3 bis 5: Was bedeutet „(bekannt nach apply)“, und warum ändert eine Portänderung nur `db`?
3. **Ersetzen, Löschen, Zyklus (Einheit 4.3):** Erklären Sie Schritt 6 bis 8: Warum wird `app` ersetzt und `start` geändert, in welcher Reihenfolge wird gelöscht, und was meldet das Modell bei einem Zyklus?

#### Kontrollfragen

1. Woraus ergibt sich die Reihenfolge?
2. Was bedeutet „bekannt nach apply“?
3. Warum ändert sich `start`, wenn `app` ersetzt wird?
4. In welcher Reihenfolge wird gelöscht?

### Modul 5: State und Remote State

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wozu der Zustand (State) dient.
  * Nach Abschluss dieses Moduls kann der Lernende Drift erkennen und beseitigen.
  * Nach Abschluss dieses Moduls kann der Lernende Sperren (Locking) und gemeinsamen Zustand erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken für sensible Werte im Zustand nennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Zustand ansehen | 6 |
| 5.2 | Drift | 4 |
| 5.3 | Sperre und gemeinsamer Zustand | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zustand ansehen (Einheit 5.1):** Führen Sie `bash state.sh` aus. Erklären Sie Schritt 1 bis 3: Was steht in der Zustandsdatei, und wann erhöht sich die `serial`?
2. **Drift (Einheit 5.2):** Erklären Sie Schritt 4: Welche Abweichungen erkennt der Plan, und was macht das Apply daraus?
3. **Sperre und gemeinsamer Zustand (Einheit 5.3):** Erklären Sie Schritt 5 bis 7: Was verhindert die Sperre, und was passiert ohne die gemeinsame Zustandsdatei?

#### Kontrollfragen

1. Wozu dient der Zustand?
2. Was steht trotz `sensitive` im Zustand?
3. Wann erhöht sich die `serial`?
4. Was bewirkt die Sperre?

### Modul 6: Module

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Modul mit Eingaben und Ausgaben schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende dasselbe Modul mehrfach aufrufen.
  * Nach Abschluss dieses Moduls kann der Lernende Adressen von Modul-Ressourcen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Pflichteingaben und Änderungen im Aufruf deuten.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Modul lesen | 6 |
| 6.2 | Reihenfolge und Adressen | 4 |
| 6.3 | Änderung und Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Modul lesen (Einheit 6.1):** Führen Sie `bash module.sh` aus. Erklären Sie Schritt 1 und 2: Welche Eingaben und Ausgaben hat das Modul `seite`, und wie unterscheiden sich die beiden Aufrufe?
2. **Reihenfolge und Adressen (Einheit 6.2):** Erklären Sie Schritt 3 bis 5: Warum steht die Sitemap am Ende, und wie heißen die Ressourcen im Zustand?
3. **Änderung und Fehler (Einheit 6.3):** Erklären Sie Schritt 6 und 7: Was ändert sich bei geändertem `text`, und was meldet das Modell bei fehlender Pflichteingabe?

#### Kontrollfragen

1. Wie heißt die Ressource im Aufruf `start`?
2. Warum steht `sitemap` zuletzt?
3. Was ändert sich bei geändertem `text` von `kontakt`?
4. Was meldet das Modell bei fehlendem `name`?

### Modul 7: Import und Zusammenspiel mit cloud-init und Ansible

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein vorhandenes Objekt in die Verwaltung importieren.
  * Nach Abschluss dieses Moduls kann der Lernende user-data für cloud-init mit Terraform erzeugen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Ansible-Inventar aus Terraform erzeugen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Aufgabenteilung zwischen Terraform, cloud-init und Ansible erklären.
* **Voraussetzungen:** Modul 4; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Import | 4 |
| 7.2 | cloud-init prüfen | 3 |
| 7.3 | Ansible und Aufgabenteilung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Import (Einheit 7.1):** Führen Sie `bash zusammenspiel.sh` aus. Erklären Sie Schritt 1 und 2: Was zeigt der Plan vor und nach dem Import, und was meldet das Modell ohne passende Ressource?
2. **cloud-init prüfen (Einheit 7.2):** Erklären Sie Schritt 3 bis 5: Welche Dateien entstehen, und wie findet `cloud-init schema` den Tippfehler?
3. **Ansible und Aufgabenteilung (Einheit 7.3):** Erklären Sie Schritt 6 und 7: Wie liest Ansible das Inventar, und wer macht was?

#### Kontrollfragen

1. Was bewirkt ein Import?
2. Was prüft `cloud-init schema`?
3. Welche Dateien entstehen?
4. Wer macht was?

### Modul 8: Sicherheit der Zugangsdaten und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Geheimnisse im Quelltext finden und vermeiden.
  * Nach Abschluss dieses Moduls kann der Lernende sensible Werte über die Umgebung übergeben.
  * Nach Abschluss dieses Moduls kann der Lernende Zustand und Variablendateien von der Versionsverwaltung ausschließen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abschlussprojekt mit Abnahmeliste prüfen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Geheimnisse im Quelltext | 4 |
| 8.2 | Besser machen | 4 |
| 8.3 | Abschlussprojekt | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Geheimnisse im Quelltext (Einheit 8.1):** Führen Sie `bash abschluss.sh` aus. Erklären Sie Schritt 1 und 2: Was findet die Suche, und warum ist das ein Problem?
2. **Besser machen (Einheit 8.2):** Erklären Sie Schritt 3 und 4: Wie gelangt das Kennwort über `TF_VAR_kennwort` in die Konfiguration, und was bleibt trotzdem im Zustand?
3. **Abschlussprojekt (Einheit 8.3):** Erklären Sie Schritt 5 bis 7: Was zeigt die Abnahmeliste, und wie wird Drift erkannt?

#### Kontrollfragen

1. Warum gehört ein Kennwort nicht in die `.tf`-Datei?
2. Wie übergibt man es besser?
3. Was bleibt trotzdem unsicher?
4. Was prüft die Abnahmeliste?
