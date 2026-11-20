# Lehrplan: Monitoring mit PRTG

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Windows- und Linux-Grundlagen (Dienste, Firewall) sind hilfreich |
| **Gesamtumfang** | 8 Module, 96 UE (zu 45 Minuten; 72 Stunden) |
| **Fokus-Technologien** | Aufbau und Installation, Sensoren und Geräte, Abfragen per WMI, SNMP und SSH, Benachrichtigungen, Karten und Berichte, Abhängigkeiten, eigene Sensoren (Skripte), Lizenzmodell der Gratisstufe und Betrieb |
| **Thematische Abgrenzung (Out of Scope)** | **PRTG selbst läuft nur unter Windows und wurde in dieser Übungsreihe nicht ausgeführt.** Echt ausgeführt werden: `snmpd` mit `snmpget`/`snmpwalk`, ein lokaler HTTP-Server mit TCP-/HTTP-Prüfungen, Skripte für eigene Sensoren (XML/JSON, geprüft mit `xmllint`, `jq`, Python), Auswertungen und eine `tar`-Sicherung. Das Verhalten von PRTG (Status, Benachrichtigung, Abhängigkeiten, Lizenz) ist ein **Modell in Python** nach den Angaben im Lehrplan. Die Übung 02.1 im Repository „veeam-backup-uebung“ nutzt PRTG im Backup-Kontext; hier stehen die Grundlagen. Nicht behandelt: Cluster, Remote-Probes im Detail, REST-API, Sensorfabrik. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Aufbau und Installation | 1 | 10 |
| 2 | Sensoren und Geräte | 1 | 12 |
| 3 | Abfragen per WMI, SNMP und SSH | 1 | 14 |
| 4 | Benachrichtigungen | 1 | 12 |
| 5 | Karten und Berichte | 2 | 10 |
| 6 | Abhängigkeiten | 1 | 10 |
| 7 | Eigene Sensoren mit Skripten | 1 | 16 |
| 8 | Lizenzmodell der Gratisstufe und Betrieb | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **96** |

**Priorität 1** (Pflicht) sind die Module 1 bis 4 und 6 bis 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 5 (Karten und Berichte). Fällt Modul 5 weg, verringert sich der Gesamtumfang auf 86 UE; kein Pflichtmodul setzt Modul 5 voraus.

### 2. Quellen

**Gelesen (20.11.2026):** Die Handbuchseite „Available Licenses“ (Paessler, `paessler.com/manuals/prtg/available_licenses`) für die Lizenzstufen, die Seite „EXE/Script Advanced Sensor“ für Ablageort, Dateiendungen und Zeitlimit sowie die Seite „Custom Sensors“ für das XML-/JSON-Format; gelesen wurden jeweils nur die von einem Abrufwerkzeug zusammengefassten Teile, nicht die ganzen Seiten. **Nicht gelesen** und daher **nicht bestätigt:** Menünamen und Einstellungen der PRTG-Oberfläche, Standardports (zum Beispiel 23560 für die Probe), Systemanforderungen, Verhalten bei Überschreitung der Sensorgrenze, Platzhalter für Benachrichtigungen, Ort der Sicherungsdaten. **Stand der Lizenzangaben:** 20.11.2026; prüfen Sie die Bedingungen vor dem Einsatz erneut.

**Getestet mit (Ubuntu 24.04, Cloud-Container):** `snmpd`/`snmpget`/`snmpwalk`/`snmpset` (net-snmp 5.9.4), Python 3, `jq`, `xmllint`, `curl`, `nc`, `tar`. **Nicht ausgeführt:** PRTG, Windows, WMI, SSH-Sensoren, Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-PRTG`, `10.20.0.0/24`).

**VM 1:** `prtg01` (**erforderlich**, `10.20.0.10`): Windows Server mit PRTG; Rechte: lokale Administration.

**VM 2:** `win01` (**erforderlich**, `10.20.0.31`): Windows als überwachtes Gerät (WMI, Modul 3).

**VM 3:** `lin01` (**erforderlich**, `10.20.0.21`): Ubuntu Server als überwachtes Gerät mit `snmpd` und SSH.

**Internetphase:** Für den Download von PRTG und für Pakete braucht `prtg01` bzw. `lin01` vorübergehend Internetzugang; danach wird er entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 4 und vor Modul 8 von `prtg01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux auf `127.0.0.1` (Ports 11162 UDP, 18201, 18202) und arbeiten unter `/tmp/p20`; sie brauchen weder die VMs noch PRTG.

## B. Detaillierter Modulaufbau

### Modul 1: Aufbau und Installation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Core Server, Probe, Sensor und Gerät unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen vor der Installation prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Installation als Checkliste planen.
  * Nach Abschluss dieses Moduls kann der Lernende belegte Ports vor der Installation erkennen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Bausteine | 4 |
| 1.2 | Vorabprüfung | 3 |
| 1.3 | Installationsplan | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bausteine (Einheit 1.1):** Führen Sie `bash aufbau.sh` aus. Beschreiben Sie anhand von Schritt 1, welche Verbindung von wo nach wo geht und wo Sensoren laufen.
2. **Vorabprüfung (Einheit 1.2):** Erklären Sie Schritt 2 und 3: Warum schlagen drei der vier Fälle fehl, und was prüft Schritt 3 wirklich?
3. **Installationsplan (Einheit 1.3):** Lesen Sie Schritt 4 und ordnen Sie jedem Punkt einen Prüfpunkt zu („woran sehe ich, dass es geklappt hat?“).

#### Kontrollfragen

1. Wo laufen die Sensoren?
2. Warum scheitert die Linux-VM in der Vorabprüfung?
3. Was bedeutet „frei“ in Schritt 3?
4. Welche Lizenzstufe gilt nach dem Test?

### Modul 2: Sensoren und Geräte

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Sensorarten nach Zweck wählen (Ping, Port, HTTP, SNMP).
  * Nach Abschluss dieses Moduls kann der Lernende Statuswerte aus Messwert und Grenzen ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten bei einzelnen Fehlversuchen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Sensorbudget gegen die Grenze von 100 planen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Sensorarten und echte Prüfungen | 4 |
| 2.2 | Statuslogik | 4 |
| 2.3 | Sensorbudget | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Sensorarten und echte Prüfungen (Einheit 2.1):** Führen Sie `bash sensoren.sh` aus. Ordnen Sie die Sensorarten aus Schritt 1 zu und erklären Sie die vier echten Prüfungen aus Schritt 2.
2. **Statuslogik (Einheit 2.2):** Erklären Sie Schritt 3 und 4: Warum ist 100 ms noch „Up“ und 101 ms „Warning“, und was ändert sich, wenn zwei Fehlversuche nötig sind?
3. **Sensorbudget (Einheit 2.3):** Rechnen Sie Schritt 5 nach. Mit welcher Maßnahme kommen Sie unter 100 Sensoren, und was verlieren Sie dabei?

#### Kontrollfragen

1. Welchen Status liefert ein Port, hinter dem nichts lauscht?
2. Was liefert der HTTP-Aufruf auf einen unbekannten Pfad?
3. Warum „Down (teilweise)“?
4. Wie viele Sensoren hat das Beispiel?

### Modul 3: Abfragen per WMI, SNMP und SSH

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SNMP v2c mit Community lesen und Fehlerbilder deuten.
  * Nach Abschluss dieses Moduls kann der Lernende OIDs mit Nummern und Namen abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende SSH-Sensoren als Befehle auf dem Ziel verstehen.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für WMI auf einem Windows-Ziel nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | SNMP lesen | 6 |
| 3.2 | Fehlerbilder | 4 |
| 3.3 | SSH und WMI | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **SNMP lesen (Einheit 3.1):** Führen Sie `bash abfragen.sh` aus. Erklären Sie Schritt 1: Welche Werte liefern die drei Abfragen, und wie sind sie aufgebaut?
2. **Fehlerbilder (Einheit 3.2):** Erklären Sie Schritt 2 bis 4: Warum gibt es bei falscher Community nur eine Zeitüberschreitung, und was bedeuten „No Such Object“ und „noAccess“?
3. **SSH und WMI (Einheit 3.3):** Erklären Sie Schritt 5 bis 7: Was liest ein SNMP-Sensor, was führt ein SSH-Sensor aus, und was muss für WMI stimmen?

#### Kontrollfragen

1. Was meldet `snmpget` bei falscher Community?
2. Was bedeutet „No Such Object available on this agent“?
3. Warum scheitert `snmpset` mit der Lese-Community?
4. Wurde WMI ausgeführt?

### Modul 4: Benachrichtigungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Auslöser mit Verzögerung, Wiederholung und Eskalation beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende kurze Störungen von echten Ausfällen trennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Webhook mit JSON auslösen.
  * Nach Abschluss dieses Moduls kann der Lernende die Zahl der Meldungen mit Abhängigkeiten begrenzen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Ablauf und Verzögerung | 4 |
| 4.2 | Eskalation | 4 |
| 4.3 | Zustellung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ablauf und Verzögerung (Einheit 4.1):** Führen Sie `bash benachrichtigung.sh` aus. Erklären Sie Schritt 1 und 2: Wann geht die erste Meldung, wann die Wiederholungen, und warum löst der kurze Ausfall nichts aus?
2. **Eskalation (Einheit 4.2):** Erklären Sie Schritt 3: Wer wird wann benachrichtigt, wenn der Ausfall 20 Minuten dauert?
3. **Zustellung (Einheit 4.3):** Erklären Sie Schritt 4 bis 6: Was zeigt der echte Webhook-Aufruf, was geschieht bei unerreichbarem Empfänger, und warum helfen Abhängigkeiten?

#### Kontrollfragen

1. Warum eine Verzögerung vor der Meldung?
2. Wann geht Stufe 2?
3. Was bedeutet der Rückgabewert 7 von `curl`?
4. Wie viele Meldungen entstehen bei 40 Sensoren eines Geräts?

### Modul 5: Karten und Berichte

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Verfügbarkeit in Prozent aus Ausfallzeiten berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Zielmarke (99,9 %) in erlaubte Ausfallsekunden umrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Bericht sortiert als Tabelle ausgeben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Statuskarte als SVG erzeugen und prüfen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Verfügbarkeit | 4 |
| 5.2 | Berichtstabelle | 3 |
| 5.3 | Statuskarte | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verfügbarkeit (Einheit 5.1):** Führen Sie `bash berichte.sh` aus. Rechnen Sie Schritt 1 und 2 nach: Welche Sensoren verfehlen 99,9 %, und wie viele Sekunden Ausfall pro Woche sind erlaubt?
2. **Berichtstabelle (Einheit 5.2):** Erklären Sie Schritt 3: Nach welcher Spalte ist sortiert, und was sagt „mittlere Dauer“ aus Schritt 1 über die Art der Ausfälle?
3. **Statuskarte (Einheit 5.3):** Erklären Sie Schritt 4 und 5: Wie entsteht die Karte, und woran erkennt `xmllint` eine kaputte Datei?

#### Kontrollfragen

1. Wie viele Sekunden Ausfall erlaubt 99,9 % in einer Woche?
2. Welche Sensoren verfehlen die Marke?
3. Was meldet `xmllint` bei einer unvollständigen Datei?

### Modul 6: Abhängigkeiten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Abhängigkeitsbaum für ein Netz entwerfen.
  * Nach Abschluss dieses Moduls kann der Lernende Folgemeldungen durch Pausieren vermeiden.
  * Nach Abschluss dieses Moduls kann der Lernende Zyklen in Abhängigkeiten erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Fallen erklären (falsch gewählter Elternsensor).
* **Voraussetzungen:** Modul 2; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Baum entwerfen | 4 |
| 6.2 | Ausfälle durchspielen | 3 |
| 6.3 | Zyklen und Fallen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Baum entwerfen (Einheit 6.1):** Führen Sie `bash abhaengigkeiten.sh` aus. Beschreiben Sie den Baum aus Schritt 1 und begründen Sie, warum der Switch Elternteil der Server ist.
2. **Ausfälle durchspielen (Einheit 6.2):** Erklären Sie Schritt 2 und 3: Was wird gemeldet und was pausiert, wenn der Switch ausfällt, und was, wenn nur ein Dienst ausfällt?
3. **Zyklen und Fallen (Einheit 6.3):** Erklären Sie Schritt 4 und 5: Warum ist ein Zyklus ein Fehler, und welche Gefahr birgt ein falscher Elternsensor?

#### Kontrollfragen

1. Was wird bei einem Ausfall des Switches gemeldet?
2. Was geschieht bei Ausfall nur von `HTTP srv01`?
3. Was ist die Gefahr eines falschen Elternsensors?

### Modul 7: Eigene Sensoren mit Skripten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 16 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Skript mit gültiger XML-Antwort für einen Skriptsensor schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die gleiche Antwort als JSON erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerantworten (`error`, `text`) liefern.
  * Nach Abschluss dieses Moduls kann der Lernende Ausgaben mit einem Prüfer kontrollieren und Zeitlimits beachten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | XML-Antwort | 4 |
| 7.2 | JSON und Fehlerantwort | 4 |
| 7.3 | Prüfer | 4 |
| 7.4 | Zeitlimit und Ablage | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **XML-Antwort (Einheit 7.1):** Führen Sie `bash skripte.sh` aus. Erklären Sie Schritt 1: Welche Tags enthält die Antwort, und welche davon sind in der Herstellerdokumentation bestätigt?
2. **JSON und Fehlerantwort (Einheit 7.2):** Erklären Sie Schritt 2 und 3: Wie sieht dieselbe Antwort als JSON aus, und wie meldet ein Skript, dass die Messung selbst scheiterte?
3. **Prüfer (Einheit 7.3):** Erklären Sie Schritt 4: Welche Regeln prüft der Prüfer, und welche Fälle fallen durch?
4. **Zeitlimit und Ablage (Einheit 7.4):** Erklären Sie Schritt 5 und 6: Was bedeutet der Rückgabewert 124, und wo muss ein Skript liegen?

#### Kontrollfragen

1. Welche Tags sind Pflicht je Kanal?
2. Was bedeutet `float` = 1?
3. Wie meldet ein Skript einen Fehler?
4. Was bedeutet 124 bei `timeout`?
5. Wo liegt ein Skript für die Windows-Probe?

### Modul 8: Lizenzmodell der Gratisstufe und Betrieb

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Lizenzstufen mit Stand nennen (Test, Freeware, kommerziell).
  * Nach Abschluss dieses Moduls kann der Lernende das Testende berechnen und die Folgen kennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Sensorbudget mit Ampel planen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherung wiederherstellen und mit Prüfsummen belegen.
* **Voraussetzungen:** Modul 2; Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Lizenzstufen | 4 |
| 8.2 | Sensorbudget | 4 |
| 8.3 | Sicherung und Abnahme | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Lizenzstufen (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1 und 2: Welche Stufen gibt es, was gilt nach dem Test, und was ist **nicht** bestätigt?
2. **Sensorbudget (Einheit 8.2):** Rechnen Sie Schritt 3 nach. Warum ist die Ampel „gelb“, und wann wird sie „rot“?
3. **Sicherung und Abnahme (Einheit 8.3):** Erklären Sie Schritt 4 und 5: Wie belegen Prüfsummen die Wiederherstellung, und welche Zeile der Abnahmeliste ist ein Fehler?

#### Kontrollfragen

1. Wie lange dauert der Test, und was gilt danach?
2. Wie viele Sensoren hat das geplante Budget?
3. Was passiert bei Überschreitung der Grenze?
4. Woran erkennt man eine gelungene Wiederherstellung?
