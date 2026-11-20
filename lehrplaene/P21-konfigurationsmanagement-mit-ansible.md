# Lehrplan: Konfigurationsmanagement mit Ansible

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen und SSH |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Konzept (agentenlos, idempotent), Inventare, Ad-hoc-Befehle, Playbooks, Variablen, Schleifen und Bedingungen, Vorlagen (Jinja2) und Handler, Rollen, Ansible Vault, Windows-Hosts per WinRM, Tests und Fehlersuche |
| **Thematische Abgrenzung (Out of Scope)** | **Ausgeführt wurde `ansible-core` mit der Verbindungsart `local`:** alle „Hosts“ des Inventars sind der Übungsrechner selbst, ihre Dateien liegen getrennt unter `/tmp/p21/ziel/<Host>/`. **SSH-Verbindungen zu anderen Rechnern, Paketinstallation, Dienste (`systemd`), Windows und WinRM wurden nicht ausgeführt.** Linux- und Bash-Grundlagen sind in vorhandenen Lehrplänen (Linux Essentials, Bash) behandelt. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Konzept und Inventare | 1 | 12 |
| 2 | Ad-hoc-Befehle und Playbooks | 1 | 14 |
| 3 | Variablen, Schleifen und Bedingungen | 1 | 14 |
| 4 | Vorlagen (Jinja2) und Handler | 1 | 12 |
| 5 | Rollen | 1 | 12 |
| 6 | Ansible Vault | 1 | 10 |
| 7 | Windows-Hosts per WinRM | 2 | 12 |
| 8 | Tests, Fehlersuche und Abschlussprojekt | 1 | 14 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Windows-Hosts per WinRM). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 88 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Ansible, der Sammlungen (`ansible.windows`) und von Jinja2 wurde **nicht** gelesen; Aussagen dazu stammen aus Fachwissen und den echten Ausgaben der Skripte. Versionen, Lizenzen und Supportzeiträume wurden **nicht** geprüft. **Getestet mit (Ubuntu 24.04, Cloud-Container, ohne systemd):** `ansible-core` 2.22.0 und das Sammelpaket `ansible` 15.0.0 (mit `ansible.windows` 3.9.2) aus PyPI, `pywinrm` 0.5.0, `yamllint`, Python 3.13. **Nicht ausgeführt:** SSH zu anderen Hosts, Windows, WinRM-Verbindung, `ansible-lint` (Installation scheiterte), Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Ansible`, `10.30.0.0/24`).

**VM 1:** `ctl01` (**erforderlich**, `10.30.0.10`): Ubuntu Server als Control Node mit Ansible.

**VM 2 und 3:** `web01` (`10.30.0.21`) und `db01` (`10.30.0.22`) (**erforderlich**): Ubuntu Server als verwaltete Hosts mit SSH und Python 3.

**VM 4:** `win01` (**nur für Modul 7**, `10.30.0.31`): Windows Server mit aktiviertem WinRM.

**Internetphase:** Für die Installation von Ansible und Paketen brauchen die VMs vorübergehend Internetzugang; danach wird er entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 3 und vor Modul 7 von `ctl01` und den Zielen einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux mit Verbindungsart `local` und arbeiten unter `/tmp/p21`; sie brauchen die VMs nicht. Im Labor ersetzt man `ansible_connection=local` durch SSH-Zugang zu `web01` und `db01`.

## B. Detaillierter Modulaufbau

### Modul 1: Konzept und Inventare

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende agentenlos und idempotent erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Inventar mit Gruppen, Untergruppen und Gruppenvariablen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Hosts mit Mustern auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende die Idempotenz an einem Auftrag beobachten.
* **Voraussetzungen:** IT-Grundlagen; Linux-Grundlagen und SSH.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Inventar lesen | 4 |
| 1.2 | Muster | 4 |
| 1.3 | Idempotenz und Ablauf | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Inventar lesen (Einheit 1.1):** Führen Sie `bash konzept.sh` aus. Beschreiben Sie anhand von Schritt 2 und 3 die Gruppen und erklären Sie, woher `ziel_wurzel` für `web01` kommt.
2. **Muster (Einheit 1.2):** Erklären Sie Schritt 4: Welche Hosts wählen `web:db` und `all:!db`, und wie wählen Sie nur `db01` aus?
3. **Idempotenz und Ablauf (Einheit 1.3):** Erklären Sie Schritt 5 und 6: Warum meldet der zweite Lauf keine Änderung, und was bedeutet „agentenlos“ für den Ablauf auf dem Ziel?

#### Kontrollfragen

1. Was bedeutet idempotent?
2. Woher bekommt `web01` die Variable `ziel_wurzel`?
3. Welche Hosts wählt das Muster `all:!db`?
4. Was heißt agentenlos?

### Modul 2: Ad-hoc-Befehle und Playbooks

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Modul ad hoc auf mehrere Hosts anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Playbook mit Play und Tasks lesen und schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Syntaxprüfung, Trockenlauf und Aufgabenliste einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerverhalten und Rückgabecode erklären.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Ad-hoc | 5 |
| 2.2 | Playbook lesen | 3 |
| 2.3 | Trockenlauf und Idempotenz | 3 |
| 2.4 | Fehler | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ad-hoc (Einheit 2.1):** Führen Sie `bash playbooks.sh` aus. Erklären Sie Schritt 1 und 2: Warum meldet `copy` zuerst `CHANGED`, und warum meldet `command` immer `CHANGED`?
2. **Playbook lesen (Einheit 2.2):** Erklären Sie Schritt 3 und 4 Zeile für Zeile: `hosts`, `gather_facts`, `loop`, `item` und die Aufgabenliste.
3. **Trockenlauf und Idempotenz (Einheit 2.3):** Vergleichen Sie Schritt 5 bis 7: Was zeigt der Trockenlauf, was ändert er nicht, und was melden die zwei echten Läufe?
4. **Fehler (Einheit 2.4):** Erklären Sie Schritt 8: Was passiert nach einer fehlgeschlagenen Aufgabe, und welchen Rückgabecode liefert das Playbook?

#### Kontrollfragen

1. Was ändert der Trockenlauf `--check`?
2. Warum zeigt `command` immer `CHANGED`?
3. Was melden die zwei echten Läufe?
4. Welchen Rückgabecode liefert ein Playbook mit fehlgeschlagener Aufgabe?

### Modul 3: Variablen, Schleifen und Bedingungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Variablen aus Gruppen und Hosts mit Vorrang erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Schleifen und Bedingungen in Tasks einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Ergebnisse mit register weiterverwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Filter und `default` für sichere Ausdrücke nutzen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Variablen und Vorrang | 6 |
| 3.2 | Schleife, Bedingung, register | 4 |
| 3.3 | Ausdrücke und Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Variablen und Vorrang (Einheit 3.1):** Führen Sie `bash variablen.sh` aus. Erklären Sie Schritt 1 und 2: Warum hat `web02` den Port 8081, `web01` 8080 und `db01` 80, und was bewirkt `-e port=9999`?
2. **Schleife, Bedingung, register (Einheit 3.2):** Erklären Sie Schritt 3: Warum wird die Portdatei auf `db01` übersprungen, und warum zählt `find` auf `web01` vier Dateien, auf `db01` drei?
3. **Ausdrücke und Fehler (Einheit 3.3):** Erklären Sie Schritt 5 und 6: Was liefern die Filter und `default`, und was meldet Ansible bei einer undefinierten Variable?

#### Kontrollfragen

1. Welche Variable gewinnt: Host, Gruppe oder `all`?
2. Warum wird die Portdatei auf `db01` übersprungen?
3. Was liefert `{{ gibt_es_nicht | default('Vorgabe') }}`?
4. Meldet der zweite Lauf Änderungen?

### Modul 4: Vorlagen (Jinja2) und Handler

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Jinja2-Vorlage mit Variablen, Schleife und Bedingung lesen.
  * Nach Abschluss dieses Moduls kann der Lernende das `template`-Modul einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Handler mit `notify` nur bei Änderungen auslösen.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungen mit `--check --diff` vorab ansehen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Vorlage lesen | 4 |
| 4.2 | Handler | 4 |
| 4.3 | Änderung und Vorschau | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorlage lesen (Einheit 4.1):** Führen Sie `bash vorlagen.sh` aus. Erklären Sie Schritt 1 und 4: Welche Zeilen der Vorlage werden wie ersetzt, und was bewirken `for` und `if`?
2. **Handler (Einheit 4.2):** Erklären Sie Schritt 3 und 5: Wann läuft der Handler, und warum läuft er im zweiten Lauf nicht?
3. **Änderung und Vorschau (Einheit 4.3):** Erklären Sie Schritt 6 bis 8: Welcher Host ändert sich, wie zeigt `--diff` den Unterschied, und was macht `flush_handlers`?

#### Kontrollfragen

1. Wann läuft ein Handler?
2. Warum läuft er im zweiten Lauf nicht?
3. Was zeigt `--check --diff`?
4. Was bewirkt `meta: flush_handlers`?

### Modul 5: Rollen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Rolle (tasks, defaults, templates, handlers, meta) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Rolle anlegen, füllen und einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Rollenabhängigkeiten nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende Teile mit Tags ausführen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Rollengerüst | 4 |
| 5.2 | Einsatz und Abhängigkeit | 4 |
| 5.3 | Tags und Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rollengerüst (Einheit 5.1):** Führen Sie `bash rollen.sh` aus. Beschreiben Sie anhand von Schritt 1 und 2, wofür jeder Ordner der Rolle dient.
2. **Einsatz und Abhängigkeit (Einheit 5.2):** Erklären Sie Schritt 3 und 4: Wie überschreiben die Rollenvariablen die `defaults`, und warum läuft `basis` vor `webserver`?
3. **Tags und Fehler (Einheit 5.3):** Erklären Sie Schritt 5 und 6: Was bewirken `--tags` und `--skip-tags`, und was meldet Ansible bei einer unbekannten Rolle?

#### Kontrollfragen

1. Welche Variablen stehen in `defaults`?
2. Warum läuft `basis` zuerst?
3. Was bewirkt `--tags verzeichnis`?
4. Was meldet Ansible bei einer unbekannten Rolle?

### Modul 6: Ansible Vault

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Datei mit Ansible Vault verschlüsseln und wieder lesbar machen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Playbook mit Kennwortdatei ausführen.
  * Nach Abschluss dieses Moduls kann der Lernende einzelne Werte mit `encrypt_string` schützen.
  * Nach Abschluss dieses Moduls kann der Lernende Kennwörter aus der Ausgabe und der Versionsverwaltung heraushalten.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Verschlüsseln | 4 |
| 6.2 | Fehlerbilder | 3 |
| 6.3 | Einzelwerte, Wechsel, Ablage | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verschlüsseln (Einheit 6.1):** Führen Sie `bash vault.sh` aus. Erklären Sie Schritt 1 und 2: Woran erkennt man eine verschlüsselte Datei, und wie nutzt das Playbook die Werte?
2. **Fehlerbilder (Einheit 6.2):** Erklären Sie Schritt 3: Was meldet Ansible ohne und mit falschem Kennwort?
3. **Einzelwerte, Wechsel, Ablage (Einheit 6.3):** Erklären Sie Schritt 4 bis 6: Wofür ist `encrypt_string` gedacht, was tun `rekey` und `decrypt`, und was steht in `.gitignore`?

#### Kontrollfragen

1. Woran erkennt man eine Vault-Datei?
2. Was meldet Ansible ohne Kennwort?
3. Wozu dient `no_log: true`?
4. Warum steht die Kennwortdatei in `.gitignore`?

### Modul 7: Windows-Hosts per WinRM

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Verbindungsart `winrm` im Inventar festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Windows-Module (`ansible.windows`) lesen und in Playbooks einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Unterschiede zu Linux-Zielen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende das Fehlerbild bei nicht erreichbarem WinRM deuten.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Inventar und Variablen | 4 |
| 7.2 | Module und Syntax | 4 |
| 7.3 | Fehlerbild | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Inventar und Variablen (Einheit 7.1):** Führen Sie `bash windows.sh` aus. Erklären Sie Schritt 1: Welche Variablen setzen die Verbindungsart, und warum steht das Kennwort als Verweis auf eine Vault-Variable?
2. **Module und Syntax (Einheit 7.2):** Erklären Sie Schritt 2 bis 4: Was liefert `ansible-doc` zu `win_feature`, und was prüft `--syntax-check` ohne Verbindung?
3. **Fehlerbild (Einheit 7.3):** Erklären Sie Schritt 5: Was bedeutet `UNREACHABLE`, und welchen Rückgabecode liefert der Aufruf?

#### Kontrollfragen

1. Welche Verbindungsart braucht ein Windows-Host?
2. Warum `ansible_winrm_server_cert_validation: ignore`?
3. Wurde ein Windows-Host angesprochen?
4. Welchen Rückgabecode liefert ein nicht erreichbares Ziel?

### Modul 8: Tests, Fehlersuche und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Playbooks mit yamllint, Syntaxprüfung, Trockenlauf und Idempotenztest prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Eingaben mit `assert` absichern.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler mit `block/rescue` abfangen und mit `debug` suchen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abschlussprojekt mit Vorlage, Handler und Abnahmeliste abnehmen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Projekt und Tests | 6 |
| 8.2 | Fehlersuche | 4 |
| 8.3 | Fehler abfangen und Abnahme | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Projekt und Tests (Einheit 8.1):** Führen Sie `bash tests.sh` aus. Erklären Sie Schritt 1 bis 3: Was prüfen yamllint, `--syntax-check`, `--check` und der Idempotenztest?
2. **Fehlersuche (Einheit 8.2):** Erklären Sie Schritt 4 und 5: Warum bricht der Lauf mit `-e app_port=80` ab, und wie sieht man Variablen und Fakten an?
3. **Fehler abfangen und Abnahme (Einheit 8.3):** Erklären Sie Schritt 6 bis 8: Was bewirken `rescue` und `always`, und welche Punkte prüft die Abnahmeliste?

#### Kontrollfragen

1. Wie prüft man Idempotenz automatisch?
2. Was passiert bei `-e app_port=80`?
3. Was bewirkt `rescue`?
4. Warum bleibt `db01` unberührt?
