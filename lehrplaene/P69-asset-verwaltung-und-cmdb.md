# Lehrplan: Asset-Verwaltung und CMDB

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen; Grundkenntnisse im IT-Betrieb; einfache Linux-Befehle (Shell, Paketverwaltung) |
| **Gesamtumfang** | 8 Module, 45 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | GLPI (Open Source, Asset-Verwaltung und Ticketsystem), Ubuntu Server 24.04 LTS, Apache, PHP, MariaDB; GLPI Agent (optional) |
| **Thematische Abgrenzung (Out of Scope)** | ITIL-Theorie, Ticketsysteme im Detail und Lizenzmanagement sind eigene Kurse (nur kurze Verweise); keine Auswahl-Studie zu Werkzeugen (Snipe-IT und i-doit werden nur genannt); keine Zertifizierungsvorbereitung; keine Rechtsberatung (Datenschutz nur als Rahmen). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Begriffe und Lebenszyklus | 1 | 5 |
| 2 | Laboraufbau und Installation von GLPI | 1 | 7 |
| 3 | Datenmodell: Typen, Standorte, Beziehungen | 1 | 6 |
| 4 | Erfassung: manuell und per Import, Datenqualität | 1 | 6 |
| 5 | Automatische Inventarisierung | 2 | 6 |
| 6 | Tickets, Berechtigungen und Verknüpfungen | 1 | 4 |
| 7 | Berichte, Bestandsaufnahme und Kennzahlen | 1 | 6 |
| 8 | Verantwortung, Datenschutz und Sicherung | 1 | 5 |
| **Gesamt** | **7 Pflichtmodule, 1 Vertiefungsmodul** | | **45** |

*Hinweis zur Priorisierung: Modul 5 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 5 voraus: Der Bestand wird in Modul 4 manuell und per Import aufgebaut.*

### 2. Quellen

* **GLPI-Installationsvoraussetzungen** (glpi-install.readthedocs.io, <https://glpi-install.readthedocs.io/en/latest/prerequisites.html>, abgerufen am 13.11.2026): für GLPI 11.0.x mindestens PHP 8.2 und MariaDB 10.6 oder MySQL 8.0; Pflicht-Erweiterungen von PHP siehe Modul 2. Die genaue aktuelle GLPI-Version ist **nicht geprüft** (laut GLPI-Hilfeseite existiert auch ein Zweig 12.0.x mit PHP 8.3 als Minimum).
* **GLPI Inventory und GLPI Agent** (GLPI-Hilfe, <https://help.glpi-project.org/doc-plugins/plugins-glpi/glpi-inventory>, abgerufen am 13.11.2026): beschreibt Agenten-Module und natives Inventar; **URL-Pfad der Agenten und unterstützte Betriebssysteme stehen dort nicht** und sind vor dem Kurs in der Agent-Dokumentation nachzulesen.
* **GLPI-Hilfe, Installation** (<https://help.glpi-project.org/procedures/install_glpi.md>): nur als Suchtreffer gesehen, nicht abgerufen.
* **ITIL 4 Foundation / Practice Guide Service Configuration Management** (PeopleCert, früher AXELOS): *Stand nicht geprüft, keine geprüfte Quelle*; Begriffe Asset, Configuration Item (CI) und CMDB werden mit festen Kursdefinitionen verwendet.
* **DSGVO** (Verordnung (EU) 2016/679) für Modul 8: nur als Rahmen genannt, Wortlaut nicht geprüft; keine Rechtsberatung.
* **RFC 1918** (IETF, Februar 1996) für private Adressen und **RFC 2606** (IETF, Juni 1999, Datum nicht geprüft) für `example.com`.
* **Snipe-IT, i-doit:** nur als Alternativen genannt, nicht geprüft.

### 3. Labor-Setup & Rahmenbedingungen

* **Hypervisor:** Hyper-V, privater virtueller Switch `Private-Switch` ohne Verbindung zum Heimnetz; für Modul 2 temporär ein Switch mit Internet (`Default Switch` unter Windows Client oder externer Switch).
* **VMs (Annahmen):**

| VM | Rolle | Adresse | Ressourcen |
| :--- | :--- | :--- | :--- |
| `asset-srv` | Ubuntu 24.04 LTS Server mit GLPI | `192.168.110.10/24` | 2 vCPU, 4 GB RAM, 30 GB Platte, Benutzer `labadmin` |
| `win-client` | Windows 11 Evaluation | `192.168.110.20/24` | 4 GB RAM |
| `lx-client` | Linux-Client (Ubuntu Desktop oder Server) | `192.168.110.30/24` | 2 GB RAM |

* **Namen:** `asset.example.internal` (hosts-Dateien), fiktives Unternehmen **Bergfeld Maschinenbau GmbH** mit zwei Standorten (Wien, Graz).
* **Vor Modul 1 (nicht Teil der UE):** alle drei VMs sind installiert und starten; Generation 2, Ubuntu-VM mit Secure-Boot-Vorlage „Microsoft UEFI Certificate Authority“.
* **Material des Dozenten:** (1) CSV-Datei mit etwa 20 Geräten und einigen eingebauten Fehlern (Modul 4), (2) Soll-Liste und Ist-Liste für eine Bestandsaufnahme (Modul 7). Beispiele liegen der Übungsreihe bei und sind frei erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Begriffe und Lebenszyklus
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Asset, Configuration Item (CI) und CMDB definieren und gegeneinander abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende den Lebenszyklus eines Geräts und einer Software beschreiben und den Datenänderungen je Phase zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Asset-Verwaltung von Ticketsystem und Lizenzmanagement abgrenzen.
* **Voraussetzungen:** keine.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Asset, Configuration Item, CMDB: Begriffe und Nutzen | 2 |
| 1.2 | Lebenszyklus von Geräten und Software | 2 |
| 1.3 | Abgrenzung zu Ticketsystem und Lizenzmanagement | 1 |

#### Praxisaufgaben
1. **Begriffe ordnen:** Ordne acht Beispiele (Laptop, Mailserver-Dienst, Wartungsvertrag, Software-Lizenz, Schreibtisch, Switch, Datenbank, Handbuch) jeweils „Asset“, „CI“, „beides“ oder „weder noch“ zu und begründe.
2. **Lebenszyklus:** Beschreibe den Lebenszyklus eines Laptops (Planung bis Entsorgung) und nenne je Phase, welche Angaben in der Verwaltung geändert werden.
3. **Abgrenzung:** Nenne je einen Fall, der in die Asset-Verwaltung, ins Ticketsystem und ins Lizenzmanagement gehört, und zeige, wo sich alle drei berühren.

#### Kontrollfragen
1. Was unterscheidet ein Asset von einem Configuration Item?
2. Wozu dient eine CMDB, und was ist sie nicht?
3. Warum ist der Status „im Lager“ von „in Betrieb“ zu unterscheiden?

### Modul 2: Laboraufbau und Installation von GLPI
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Architektur (Webserver, PHP, Datenbank) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende GLPI mit seinen Abhängigkeiten installieren und das Web-Setup durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor ohne Internet betreiben und einen Rückkehrpunkt anlegen.
* **Voraussetzungen:** VMs laut A.3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Architektur und Anforderungen (PHP-Version, Datenbank, Erweiterungen) | 1 |
| 2.2 | Netzwerk, Namensauflösung und Installation der Abhängigkeiten | 2 |
| 2.3 | GLPI herunterladen, Datenbank anlegen, Web-Setup | 2 |
| 2.4 | Erste Absicherung, Rückbau des Internetzugangs, Checkpoint | 2 |

#### Praxisaufgaben
1. **Netzwerk:** Konfiguriere die drei VMs auf `192.168.110.x/24`, trage `192.168.110.10 asset.example.internal` in die hosts-Dateien ein und gib `asset-srv` temporär Internet (zweite Schnittstelle, Netplan, `dhcp4: true`).
2. **Abhängigkeiten:** Installiere Apache, MariaDB und PHP samt den Pflicht-Erweiterungen laut A.2. Prüfe die PHP-Version gegen die Mindestversion.
3. **GLPI:** Lege Datenbank und Datenbankbenutzer an (eigenes Kennwort), lade das GLPI-Release von der Projektseite, entpacke es in das Webverzeichnis, setze Eigentümer und Rechte und durchlaufe den Web-Installer.
4. **Absicherung und Rückbau:** Ändere die Standardkennwörter der Beispielkonten, entferne die zweite Schnittstelle, prüfe die Isolation und lege einen Checkpoint `nach-Modul-2` an.

#### Kontrollfragen
1. Welche Aufgaben haben Webserver, PHP und Datenbank bei GLPI?
2. Warum müssen Standardkennwörter nach der Installation geändert werden?
3. Warum ist ein Checkpoint keine Datensicherung?

### Modul 3: Datenmodell: Typen, Standorte, Beziehungen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Asset-Typen, Pflichtfelder und Statuswerte festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Standorte, Hersteller und Zuständige modellieren.
  * Nach Abschluss dieses Moduls kann der Lernende Beziehungen zwischen CIs abbilden und Auswirkungen ableiten.
* **Voraussetzungen:** Modul 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Asset-Typen, Felder und Namenskonvention | 2 |
| 3.2 | Standorte, Hersteller, Status, Zuständige | 2 |
| 3.3 | Beziehungen und Abhängigkeiten (CI-Modell) | 2 |

#### Praxisaufgaben
1. **Konzept:** Lege auf Papier fest: Typen (Computer, Monitor, Netzwerkgerät, Drucker, Server), Pflichtfelder, Status (Planung, im Lager, in Betrieb, in Reparatur, ausgemustert) und eine Namenskonvention `<Standort>-<Typ>-<Nr>` (z. B. `WIE-NB-001`).
2. **Stammdaten:** Lege in GLPI die Standorte Wien und Graz, drei Hersteller und die Status an.
3. **Beziehungen:** Modelliere die Abhängigkeiten ERP-Anwendung → Datenbankserver → Switch → Gateway als Tabelle (Quelle, Ziel, Art) und lege sie in GLPI an, soweit das Werkzeug es erlaubt (Menü *nicht bestätigt*). Leite ab: Was fällt aus, wenn der Switch ausfällt?

#### Kontrollfragen
1. Warum braucht man eine Namenskonvention?
2. Welche Auswirkung hat ein fehlendes Pflichtfeld auf die Datenqualität?
3. Wie hilft die Beziehungsdarstellung bei der Auswirkungsanalyse?

### Modul 4: Erfassung: manuell und per Import, Datenqualität
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Assets manuell erfassen.
  * Nach Abschluss dieses Moduls kann der Lernende Daten per CSV importieren.
  * Nach Abschluss dieses Moduls kann der Lernende Datenqualitätsprobleme (Dubletten, fehlende Felder, Schreibweisen) finden und beheben.
* **Voraussetzungen:** Modul 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Manuelle Erfassung und Regeln | 2 |
| 4.2 | CSV-Import und Feldzuordnung | 2 |
| 4.3 | Datenqualität: Dubletten, Pflichtfelder, Konventionen | 2 |

#### Praxisaufgaben
1. **Manuell:** Erfasse fünf Geräte nach der Namenskonvention (Seriennummer, Standort, Zuständiger, Status).
2. **Datenqualität vorab:** Prüfe die Beispieldatei `assets-beispiel.csv` mit `datenqualitaet.py`, liste die Fehler und korrigiere sie in einer Kopie.
3. **Import:** Importiere die bereinigte Datei per CSV-Import (Menü *nicht bestätigt*) und prüfe Anzahl und Stichproben.

#### Kontrollfragen
1. Warum prüft man Daten vor dem Import?
2. Woran erkennt man Dubletten?
3. Was kann schiefgehen, wenn die Feldzuordnung falsch ist?

### Modul 5: Automatische Inventarisierung
* **Priorität:** 2 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende agentenbasierte und agentenlose Inventarisierung unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Agenten auf einem Windows- und einem Linux-Client einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende automatisch erfasste Daten mit dem manuellen Bestand abgleichen.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Konzepte: Agent, SNMP, Netzwerkerkennung | 2 |
| 5.2 | Agent einrichten und Inventar senden | 2 |
| 5.3 | Abgleich und Abweichungen | 2 |

#### Praxisaufgaben
1. **Konzept:** Vergleiche Agent und agentenlose Erfassung in einer Tabelle (Vorteile, Grenzen, Sicherheit).
2. **Agent:** Richte den GLPI Agent auf `win-client` und `lx-client` ein, sende das Inventar an `asset-srv` und prüfe, ob beide Geräte erscheinen (Installationsschritte, Pfad und Betriebssystemunterstützung *nicht bestätigt*, in der Agent-Dokumentation nachlesen).
3. **Abgleich:** Vergleiche die automatisch erfassten Daten (Name, Seriennummer, Betriebssystem) mit dem manuellen Eintrag und dokumentiere Abweichungen mit Ursache.

#### Kontrollfragen
1. Warum erfasst ein Agent nur eingeschaltete Geräte?
2. Welche Sicherheitsfragen stellt die Kommunikation zwischen Agent und Server?
3. Wann sind manuelle Daten die „Wahrheit“, wann das Inventar?

### Modul 6: Tickets, Berechtigungen und Verknüpfungen
* **Priorität:** 1 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Tickets mit Assets verknüpfen.
  * Nach Abschluss dieses Moduls kann der Lernende Profile und Berechtigungen für Techniker und Anwender einrichten.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Tickets und Assets verknüpfen | 2 |
| 6.2 | Profile, Benutzer und Sichtbarkeit | 2 |

#### Praxisaufgaben
1. **Ticket:** Lege ein Ticket „Notebook WIE-NB-001 startet nicht“ an und verknüpfe es mit dem Gerät. Prüfe, dass der Verlauf am Gerät sichtbar ist.
2. **Profile:** Lege einen Techniker und einen Anwender (Self-Service) an, teste, was der Anwender sieht und was nicht (Menüs *nicht bestätigt*).

#### Kontrollfragen
1. Welchen Nutzen hat die Verknüpfung von Ticket und Asset?
2. Warum sollen Anwender nicht alle Assets sehen?

### Modul 7: Berichte, Bestandsaufnahme und Kennzahlen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Suchen und Berichte erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Bestandsaufnahme durchführen und Soll mit Ist vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Kennzahlen zur Datenqualität berechnen.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Suchen, Berichte, Exporte | 2 |
| 7.2 | Bestandsaufnahme (Inventur): Ablauf und Abweichungen | 2 |
| 7.3 | Kennzahlen: Vollständigkeit, Aktualität, Dubletten | 2 |

#### Praxisaufgaben
1. **Bericht:** Erzeuge Berichte „Geräte je Standort“ und „Geräte ohne Zuständigen“ und exportiere sie als CSV.
2. **Inventur:** Vergleiche `inventur-soll.csv` (Verwaltung) mit `inventur-ist.csv` (Zählung vor Ort) mit `inventur.py`. Liste fehlende, unbekannte und abweichende Geräte und lege Maßnahmen fest.
3. **Kennzahlen:** Berechne Vollständigkeit (Anteil Pflichtfelder gefüllt) und Aktualität (letzte Prüfung höchstens 365 Tage her, Stichtag 30.11.2026) für die Beispielliste.

#### Kontrollfragen
1. Was ist der Unterschied zwischen „fehlend“ und „unbekannt“ bei der Inventur?
2. Warum ist Aktualität eine eigene Kennzahl?
3. Wer entscheidet, ob ein fehlendes Gerät ausgebucht wird?

### Modul 8: Verantwortung, Datenschutz und Sicherung
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Verantwortlichkeiten für die Datenpflege festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende personenbezogene Daten in der Verwaltung erkennen und ein Löschkonzept skizzieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherung und Wiederherstellung der Daten planen und prüfen.
* **Voraussetzungen:** Modul 4 und 6.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Rollen und Prozesse der Datenpflege (RACI) | 2 |
| 8.2 | Datenschutz: personenbezogene Daten, Löschfristen | 1 |
| 8.3 | Sicherung und Wiederherstellung (Datenbank und Dateien) | 2 |

#### Praxisaufgaben
1. **RACI:** Erstelle eine RACI-Tabelle für Anlage, Änderung, Ausmusterung und Inventur von Assets.
2. **Datenschutz:** Markiere im Datenmodell die Felder, die Personen betreffen (Zuständiger, Benutzer, Kontakt), und entwirf ein Löschkonzept mit Fristen (Fristen als Annahme, keine Rechtsberatung).
3. **Sicherung:** Plane die Sicherung der Datenbank (`mysqldump`) und der GLPI-Dateien, führe sie aus und stelle sie auf einer zweiten Datenbank wieder her (Befehle *nicht bestätigt* im Labor).

#### Kontrollfragen
1. Warum braucht jedes Asset einen Verantwortlichen?
2. Welche Daten in der Asset-Verwaltung sind personenbezogen?
3. Woran erkennt man, dass eine Sicherung wirklich funktioniert?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde ohne Gem-Entwurf direkt aus dem Prompt P69 erstellt (Annahmen: GLPI als Werkzeug, Bergfeld Maschinenbau GmbH, Labor mit drei VMs). Stunden: 5+7+6+6+6+4+6+5 = 45 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 7×1, 1×2.

**Nicht bestätigt:** Menüpfade und Bezeichnungen in GLPI, CSV-Import-Dialog, Installationsschritte des GLPI Agent, Pfad für Agenten-Daten, aktuelle GLPI-Version, Paketnamen der PHP-Erweiterungen unter Ubuntu 24.04. Die Lernenden notieren Abweichungen.

**Offen:** Der Zeitaufwand ist unerprobt. Der Lehrplan wurde von Matija noch nicht geprüft.
