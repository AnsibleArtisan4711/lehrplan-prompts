# Lehrplan: cloud-init und VM-Vorlagen

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Konzept von Vorlagen (Golden Image), cloud-init (user-data, Netzwerk, Pakete, Skripte), Seed-Medium (NoCloud), Abbildformate für Hyper-V, Proxmox und Cloud, Sysprep für Windows, Packer in Grundzügen, Wartung und Aktualisierung von Vorlagen |
| **Thematische Abgrenzung (Out of Scope)** | **Geprüft wurden die Konfigurationsdateien und die Werkzeuge, nicht der Start einer VM.** Echt ausgeführt wurden `cloud-init schema`, `cloud-init devel render`, `devel net-convert` und `devel make-mime`, `cloud-localds` (Seed-Abbild), `isoinfo`, `qemu-img` und `xmllint`. **Nicht ausgeführt:** ein echter Start einer VM mit cloud-init, Hyper-V, Proxmox, Cloud-Anbieter, Sysprep, Packer. Die Linux-Grundlagen sind in vorhandenen Lehrplänen behandelt. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Konzept der Vorlagen (Golden Image) | 1 | 10 |
| 2 | cloud-init: Grundlagen und user-data | 1 | 14 |
| 3 | user-data in der Praxis | 1 | 14 |
| 4 | Netzwerkkonfiguration mit cloud-init | 1 | 12 |
| 5 | Seed-Medium (NoCloud) | 1 | 12 |
| 6 | Vorlagenformate für Hyper-V, Proxmox und Cloud | 1 | 12 |
| 7 | Sysprep für Windows und Packer in Grundzügen | 2 | 12 |
| 8 | Wartung von Vorlagen und Abschlussprojekt | 1 | 14 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Sysprep und Packer). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 88 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von cloud-init, Hyper-V, Proxmox und Packer wurde **nicht** gelesen; Aussagen dazu (Stufen, Datenquellen, Befehle, Menünamen, Sysprep-Optionen) stammen aus Fachwissen und sind als solche gekennzeichnet. Versionen und Lizenzen wurden nicht geprüft. **Getestet mit (Ubuntu 24.04, Cloud-Container, ohne systemd):** `cloud-init` 26.2 (Paket `cloud-init` 26.2-0ubuntu1~24.04.2), `cloud-image-utils` (`cloud-localds`), `genisoimage` (`isoinfo`), `qemu-utils` (`qemu-img`), `libxml2-utils` (`xmllint`), Python 3.13 mit `python-hcl2` 8.2.0. **Nicht ausgeführt:** VM-Start, Hyper-V, Proxmox, Cloud, Windows, Sysprep, Packer.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Vorlagen`, `10.50.0.0/24`).

**VM 1:** `bau01` (**erforderlich**, `10.50.0.10`): Ubuntu Server als Arbeitsplatz mit `cloud-init`, `cloud-image-utils`, `qemu-utils`.

**Ausgangsabbild:** ein Linux-Cloud-Abbild (Cloud-Image) einer Distribution; Herkunft und Prüfsumme sind vor der Verwendung zu prüfen.

**Ziel:** ein Virtualisierungshost (Hyper-V oder Proxmox), auf dem aus der Vorlage Klone gestartet werden.

**Internetphase:** Zum Herunterladen von Abbildern und Paketen braucht `bau01` vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 4 und Modul 8 von `bau01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux und arbeiten unter `/tmp/p23`; sie brauchen die VMs nicht. Im Labor werden Seed-Abbild und Klon an eine VM gehängt.

## B. Detaillierter Modulaufbau

### Modul 1: Konzept der Vorlagen (Golden Image)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Gedanken der Vorlage und des Klons erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Abbilddatei mit Differenzdatenträger (Backing File) anlegen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Versionsstände mit Prüfsumme festhalten.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken beim Verändern einer Vorlage nennen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Vorlage und Klone | 4 |
| 1.2 | Kette und Prüfsumme | 3 |
| 1.3 | Veränderung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorlage und Klone (Einheit 1.1):** Führen Sie `bash vorlage.sh` aus. Erklären Sie Schritt 2 und 3: Was ist die virtuelle Größe, und worauf verweisen `web01.qcow2` und `web02.qcow2`?
2. **Kette und Prüfsumme (Einheit 1.2):** Erklären Sie Schritt 4 und 5: Was zeigt die Backing-Kette, und was hält die Prüfsummendatei fest?
3. **Veränderung (Einheit 1.3):** Erklären Sie Schritt 6: Woran fällt eine veränderte Kopie auf, und warum werden neue Versionen als neue Datei angelegt?

#### Kontrollfragen

1. Was ist ein Differenzdatenträger?
2. Was bedeutet virtuelle Größe?
3. Wozu die Prüfsumme?
4. Warum neue Versionen als neue Datei?

### Modul 2: cloud-init: Grundlagen und user-data

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von cloud-init erklären.
  * Nach Abschluss dieses Moduls kann der Lernende user-data mit der Kopfzeile `#cloud-config` schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien mit `cloud-init schema` prüfen und Fehler lesen.
  * Nach Abschluss dieses Moduls kann der Lernende mehrteilige Daten und Jinja-Vorlagen einordnen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Schema | 6 |
| 2.2 | Kopfzeile und MIME | 4 |
| 2.3 | Jinja und Ablauf | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Schema (Einheit 2.1):** Führen Sie `bash grundlagen.sh` aus. Erklären Sie Schritt 1 und 2: Wie meldet `cloud-init schema` eine gültige und eine fehlerhafte Datei, und was bedeuten E1 und E2?
2. **Kopfzeile und MIME (Einheit 2.2):** Erklären Sie Schritt 3 und 4: Was geschieht ohne `#cloud-config`, und welche Teile enthält die mehrteilige Datei?
3. **Jinja und Ablauf (Einheit 2.3):** Erklären Sie Schritt 5 und 6: Wie wird aus der Vorlage `hostname: web-lab`, und was ist über den Ablauf in Stufen bekannt (und nicht geprüft)?

#### Kontrollfragen

1. Wie erkennt man gültige user-data?
2. Was findet das Schema?
3. Was meldet es ohne Kopfzeile?
4. Was zeigt das Beispiel zu Jinja?

### Modul 3: user-data in der Praxis

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Benutzer, SSH-Schlüssel und Kennwortsperre festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Pakete, Dateien und Befehle einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler (Typen, Tippfehler) erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherheitsregeln für user-data nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Datei lesen | 6 |
| 3.2 | Fehler | 4 |
| 3.3 | Sicherheit | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Datei lesen (Einheit 3.1):** Führen Sie `bash userdata.sh` aus. Beschreiben Sie anhand von Schritt 1 bis 3, welche Aufgaben die Schlüssel `users`, `packages`, `write_files` und `runcmd` übernehmen.
2. **Fehler (Einheit 3.2):** Erklären Sie Schritt 4: Welche Fehler meldet das Schema, und wie korrigieren Sie sie?
3. **Sicherheit (Einheit 3.3):** Erklären Sie Schritt 5: Was gehört nicht in user-data, und was bewirken `ssh_pwauth: false` und `lock_passwd: true`?

#### Kontrollfragen

1. Welche Schlüssel hat die Beispieldatei?
2. Wie müssen `permissions` in `write_files` angegeben werden?
3. Welcher Typ ist `runcmd`?
4. Was gehört nicht in user-data?

### Modul 4: Netzwerkkonfiguration mit cloud-init

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine network-config (Version 2) mit fester Adresse und mit DHCP schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die Datei mit dem Schema prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ihre Umsetzung in netplan-Text erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen einer reinen Dateiprüfung nennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Statische Adresse | 4 |
| 4.2 | DHCP und Tippfehler | 4 |
| 4.3 | Grenze | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Statische Adresse (Einheit 4.1):** Führen Sie `bash netzwerk.sh` aus. Erklären Sie Schritt 1 bis 3: Welche Angaben enthält die Konfiguration, und wie sieht die Umsetzung in netplan aus?
2. **DHCP und Tippfehler (Einheit 4.2):** Erklären Sie Schritt 4 und 5: Wie lautet die DHCP-Variante, und was meldet das Schema bei `adress`?
3. **Grenze (Einheit 4.3):** Erklären Sie Schritt 6: Was wurde nicht geprüft?

#### Kontrollfragen

1. Welche Angaben enthält die statische Konfiguration?
2. Was meldet das Schema bei `adress`?
3. In welche Datei wird umgesetzt?
4. Was bleibt ungeprüft?

### Modul 5: Seed-Medium (NoCloud)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende user-data, meta-data und network-config zu einem Seed-Abbild zusammenfassen.
  * Nach Abschluss dieses Moduls kann der Lernende die Bezeichnung `cidata` und den Inhalt prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle der `instance-id` erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Datenquellen einordnen.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Seed bauen | 4 |
| 5.2 | Inhalt prüfen | 4 |
| 5.3 | Neue Instanz | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Seed bauen (Einheit 5.1):** Führen Sie `bash seed.sh` aus. Erklären Sie Schritt 1 bis 3: Welche Dateien enthält das Abbild, und welche Bezeichnung trägt es?
2. **Inhalt prüfen (Einheit 5.2):** Erklären Sie Schritt 4: Wie wurde die Übereinstimmung geprüft?
3. **Neue Instanz (Einheit 5.3):** Erklären Sie Schritt 5 und 6: Wofür dient die `instance-id`, und was wurde nicht getestet?

#### Kontrollfragen

1. Welche Bezeichnung trägt das Abbild?
2. Welche Dateien liegen im Abbild?
3. Wofür dient die `instance-id`?
4. Was wurde nicht geprüft?

### Modul 6: Vorlagenformate für Hyper-V, Proxmox und Cloud

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Abbildformate (qcow2, VHDX, VHD, VMDK, raw) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abbild mit `qemu-img convert` umwandeln.
  * Nach Abschluss dieses Moduls kann der Lernende Gleichheit mit `qemu-img compare` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Unterschiede der Plattformen nennen (mit Kennzeichnung als Fachwissen).
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Umwandeln | 4 |
| 6.2 | Größen und Vergleich | 4 |
| 6.3 | Plattformen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Umwandeln (Einheit 6.1):** Führen Sie `bash formate.sh` aus. Erklären Sie Schritt 1 und 2: Welche Formate entstehen, und welchem Hypervisor ordnen Sie sie zu?
2. **Größen und Vergleich (Einheit 6.2):** Erklären Sie Schritt 3 und 4: Warum weicht die Größe des VHD-Abbilds ab, und was meldet `qemu-img compare`?
3. **Plattformen (Einheit 6.3):** Erklären Sie Schritt 5: Was ist Fachwissen, was wurde geprüft?

#### Kontrollfragen

1. Welche Formate entstehen?
2. Warum ist VHD größer?
3. Was meldet `qemu-img compare`?
4. Wurden Hyper-V oder Proxmox geprüft?

### Modul 7: Sysprep für Windows und Packer in Grundzügen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Sysprep erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Antwortdatei (XML) auf Wohlgeformtheit prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Packer-HCL-Datei lesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Grundgedanken reproduzierbarer Abbilder beschreiben.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Sysprep | 4 |
| 7.2 | Antwortdatei | 4 |
| 7.3 | Packer | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Sysprep (Einheit 7.1):** Führen Sie `bash sysprep.sh` aus. Erklären Sie Schritt 1: Was bewirkt Sysprep (Fachwissen), und was wurde nicht ausgeführt?
2. **Antwortdatei (Einheit 7.2):** Erklären Sie Schritt 2 und 3: Was prüft `xmllint`, und was meldet es bei einem nicht geschlossenen Element?
3. **Packer (Einheit 7.3):** Erklären Sie Schritt 4 bis 6: Welche Blöcke hat die Datei, und warum reicht der Parser nicht als Prüfung?

#### Kontrollfragen

1. Wozu dient Sysprep?
2. Was prüft `xmllint --noout`?
3. Welche Blöcke hat die Packer-Datei?
4. Warum reicht der Parser nicht?

### Modul 8: Wartung von Vorlagen und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Vorlage verallgemeinern (Maschinenkennung, Hostschlüssel, Protokolle).
  * Nach Abschluss dieses Moduls kann der Lernende Versionen von Vorlagen verwalten und alte Stände entfernen.
  * Nach Abschluss dieses Moduls kann der Lernende Klon, Seed-Medium und Prüfsumme zu einem Abschlussprojekt zusammenführen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Abnahmeliste anwenden.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Verallgemeinern | 6 |
| 8.2 | Versionspflege | 4 |
| 8.3 | Abschlussprojekt | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verallgemeinern (Einheit 8.1):** Führen Sie `bash abschluss.sh` aus. Erklären Sie Schritt 1 bis 3: Was entfernt das Skript, und warum?
2. **Versionspflege (Einheit 8.2):** Erklären Sie Schritt 4: Welche Versionen bleiben, und wie wird die Vorlage geprüft?
3. **Abschlussprojekt (Einheit 8.3):** Erklären Sie Schritt 5: Welche Punkte prüft die Abnahmeliste?

#### Kontrollfragen

1. Warum wird die machine-id geleert?
2. Warum werden Hostschlüssel entfernt?
3. Welche Versionen bleiben?
4. Was prüft die Abnahmeliste?
