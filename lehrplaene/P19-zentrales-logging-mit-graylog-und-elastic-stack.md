# Lehrplan: Zentrales Logging mit Graylog und Elastic Stack

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Shell, Dienste, Textdateien); JSON lesen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Logquellen (syslog, Windows-Ereignisprotokoll), Erfassung und Weiterleitung, Graylog (Inputs, Streams, Pipelines), Elastic Stack im Überblick, Suchen und Auswertungen, Warnungen, Aufbewahrung und Datenschutz, Betrieb |
| **Thematische Abgrenzung (Out of Scope)** | `rsyslog` 8.2312, `logrotate`, `logger` und `jq` laufen in den Übungen **wirklich** (Ubuntu 24.04). **Graylog, Elasticsearch/OpenSearch, Logstash, Beats und MongoDB werden nicht ausgeführt**; deren Module (3 bis 5, Teile von 7) sind **Modelle in Python** (GELF über echte UDP-Datagramme auf `127.0.0.1`, Streams, Pipeline-Stufen, Abfragen mit der Schreibweise von Elasticsearch auf einem selbstgebauten Index). Die Logdaten der Module 5 bis 8 sind erfunden (feste Zufallsfolge). Lizenzmodelle und Versionsstände wurden **nicht** geprüft und sind mit „Stand prüfen“ gekennzeichnet. Nicht behandelt: Cluster-Betrieb, Hochverfügbarkeit, Sicherheitsüberwachung (SIEM) im Detail, Metriken (siehe P17 und P18). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Logquellen und Formate | 1 | 12 |
| 2 | Erfassung und Weiterleitung | 1 | 14 |
| 3 | Graylog: Aufbau, Inputs und GELF | 1 | 14 |
| 4 | Graylog: Streams und Pipelines | 1 | 14 |
| 5 | Elastic Stack im Überblick | 1 | 12 |
| 6 | Suchen und Auswerten | 1 | 12 |
| 7 | Warnungen | 2 | 10 |
| 8 | Aufbewahrung, Datenschutz und Betrieb | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Warnungen). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Gelesen:** Für diese Übungsreihe wurden **keine** Seiten der Herstellerdokumentation von Graylog oder Elastic gelesen. Aufbau, Schreibweisen (Pipeline-Regeln, Logstash- und Filebeat-Beispiele) und Standardports stammen aus Fachwissen und sind **nicht bestätigt**; die Formate GELF 1.1 und Syslog (RFC 3164/5424) wurden gegen das echte Verhalten von `rsyslog` beziehungsweise gegen den eigenen Prüfer in der Übung getestet, nicht gegen Graylog. **Lizenzmodelle und Versionsstände** von Graylog, Elasticsearch, OpenSearch und Kibana ändern sich: vor einem Einsatz mit Datum auf der Herstellerseite prüfen (hier nicht geprüft).

**Getestet mit (Ubuntu 24.04, Cloud-Container, kein systemd):** `rsyslog` 8.2312 (Module `imudp`, `imtcp`, `imfile`, `mmanon`, `mmjsonparse`), `logger`, `logrotate`, `jq`, Python 3 (Standardbibliothek). **Nicht ausgeführt:** Graylog, MongoDB, Elasticsearch, OpenSearch, Logstash, Beats, Kibana, `journalctl`, Windows, Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Logging`, `10.19.0.0/24`).

**VM 1:** `log01` (**erforderlich**, `10.19.0.10`): Ubuntu Server (LTS) als Log-Server; **ausreichend RAM** (Richtwert 8 GB oder mehr, Herstellerangaben prüfen) und Plattenplatz; Rechte: `sudo`.

**VM 2:** `lin01` (**erforderlich**, `10.19.0.21`): Ubuntu Server als Logquelle mit `rsyslog`.

**VM 3:** `win01` (**erforderlich**, `10.19.0.31`): Windows als Logquelle (Ereignisprotokoll; Module 1 und 3 nur als Beschreibung).

**Internetphase:** Für die Installation der Pakete braucht `log01` vorübergehend Internetzugang; danach wird er entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 5 und vor Modul 8 von `log01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte starten ihre eigenen `rsyslog`-Instanzen auf `127.0.0.1` (Ports 15514 UDP, 15515 TCP, 15517 UDP, 12201 UDP) und arbeiten unter `/tmp/p19`; sie brauchen weder die VMs noch Graylog.

## B. Detaillierter Modulaufbau

### Modul 1: Logquellen und Formate

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Syslog-Meldungen nach RFC 3164 und RFC 5424 unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Facility, Severity und PRI auswerten und nachrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine `rsyslog`-Konfiguration mit `rsyslogd -N1` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Windows-Ereignisprotokoll und journald als weitere Quellen einordnen.
* **Voraussetzungen:** Linux-Shell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Meldungen senden und lesen | 4 |
| 1.2 | PRI nachrechnen | 4 |
| 1.3 | Fehlerbild und weitere Quellen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Meldungen senden und lesen (Einheit 1.1):** Führen Sie `bash logquellen.sh` aus. Erklären Sie die vier Rohzeilen aus Schritt 3: Woran erkennt man das alte und das neue Format?
2. **PRI nachrechnen (Einheit 1.2):** Rechnen Sie Schritt 4 und 5 nach: Wie ergibt sich `PRI` aus Facility und Severity, und welche Facility und Severity haben die vier Meldungen?
3. **Fehlerbild und weitere Quellen (Einheit 1.3):** Erklären Sie Schritt 6 und 7: Was meldet `rsyslogd -N1` bei einer kaputten Konfiguration, und was wurde in Schritt 7 **nicht** ausgeführt?

#### Kontrollfragen

1. Wie berechnet sich `PRI`?
2. Woran erkennt man das neue Format (RFC 5424)?
3. Wofür dient `rsyslogd -N1`?
4. Wurde `journalctl` getestet?

### Modul 2: Erfassung und Weiterleitung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Meldungen mit `rsyslog` per UDP und TCP weiterleiten.
  * Nach Abschluss dieses Moduls kann der Lernende Filter nach Schweregrad setzen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien mit `imfile` überwachen.
  * Nach Abschluss dieses Moduls kann der Lernende Pufferung bei Ausfall des Ziels erklären und Fehler suchen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Weiterleiten und filtern | 6 |
| 2.2 | Dateien lesen | 4 |
| 2.3 | Ausfall und Fehlerbild | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Weiterleiten und filtern (Einheit 2.1):** Führen Sie `bash weiterleitung.sh` aus. Erklären Sie Schritt 2: Warum kommen nur 2 von 4 Meldungen am Server an?
2. **Dateien lesen (Einheit 2.2):** Erklären Sie Schritt 3: Wie liest `imfile` die Anwendungsdatei, und welchen Schweregrad und welche Facility tragen die Zeilen?
3. **Ausfall und Fehlerbild (Einheit 2.3):** Erklären Sie Schritt 4 und 5: Was geschieht mit den Meldungen während des Ausfalls, und wie finden Sie einen falschen Zielport?

#### Kontrollfragen

1. Warum kommen nur zwei Meldungen an?
2. Was tut `imfile`?
3. Was geschieht bei Ausfall des Servers?
4. Was ist der Nachteil von UDP?

### Modul 3: Graylog: Aufbau, Inputs und GELF

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Bausteine von Graylog (Server, MongoDB, Suchindex) benennen.
  * Nach Abschluss dieses Moduls kann der Lernende GELF-Nachrichten mit Pflichtfeldern bilden und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Komprimierung und Zerlegung großer Datagramme erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Syslog-Zeilen und Windows-Ereignisse in GELF umsetzen.
* **Voraussetzungen:** Modul 1; Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | GELF-Nachricht und Prüfer | 6 |
| 3.2 | Größe und Zerlegung | 4 |
| 3.3 | Umsetzung und Aufbau | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **GELF-Nachricht und Prüfer (Einheit 3.1):** Führen Sie `bash gelf.sh` aus. Erklären Sie Schritt 1 und 2: Welche Felder sind Pflicht, und welche Regeln für Zusatzfelder verletzen die sechs Fehlerfälle?
2. **Größe und Zerlegung (Einheit 3.2):** Erklären Sie Schritt 3 und 4: Wie viel spart die Komprimierung, wie wird eine große Nachricht zerlegt, und was geschieht mit einem verlorenen Teil?
3. **Umsetzung und Aufbau (Einheit 3.3):** Erklären Sie Schritt 5 und 6: Wie werden Syslog-Zeile und Windows-Ereignis zu GELF, und was ist an Schritt 6 **nicht** bestätigt?

#### Kontrollfragen

1. Welche Felder braucht GELF 1.1 mindestens?
2. Wie heißen Zusatzfelder?
3. Warum werden große Nachrichten zerlegt?
4. Wurde Graylog ausgeführt?

### Modul 4: Graylog: Streams und Pipelines

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Streams mit Regeln (any/all) definieren und Nachrichten zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Pipeline-Stufen zum Zerlegen, Klassifizieren und Verwerfen anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende die Bedeutung der Reihenfolge der Stufen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Regel in der Regelsprache von Graylog lesen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Streams | 6 |
| 4.2 | Pipeline | 4 |
| 4.3 | Reihenfolge und Regelsprache | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Streams (Einheit 4.1):** Führen Sie `bash streams.sh` aus. Erklären Sie Schritt 1 und 2: Wie unterscheiden sich `any` und `all`, und warum ist die Summe der Zuordnungen größer als die Zahl der Nachrichten?
2. **Pipeline (Einheit 4.2):** Erklären Sie Schritt 3: Was tun die drei Stufen, und was bedeuten die Trefferzahlen der Regeln?
3. **Reihenfolge und Regelsprache (Einheit 4.3):** Erklären Sie Schritt 4 und 5: Warum findet die Klassifizierung in Stufe 0 nichts, und was steht in der Beispielregel?

#### Kontrollfragen

1. Warum 3111 Zuordnungen bei 2721 Nachrichten?
2. Was bewirkt „aus Default entfernt“?
3. Warum Stufen?
4. Ist die Regelsprache in Schritt 5 geprüft?

### Modul 5: Elastic Stack im Überblick

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Index, Mapping und Feldtypen (`keyword`, `text`, `long`, `date`) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Abfragen mit `match`, `term`, `range` und `bool` formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende Aggregationen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Ergebnisse unabhängig mit `jq` gegenprüfen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Index und Mapping | 3 |
| 5.2 | Abfragen | 3 |
| 5.3 | Aggregationen und Gegenprobe | 3 |
| 5.4 | Bausteine | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Index und Mapping (Einheit 5.1):** Führen Sie `bash elastic.sh` aus. Erklären Sie Schritt 1: Welche Feldtypen hat der Index, und warum ist `nachricht` ein `text`-Feld, `host` aber ein `keyword`?
2. **Abfragen (Einheit 5.2):** Erklären Sie Schritt 2: Warum liefert `match` auf „failed password“ 171, mit `und` aber 70 Treffer, und warum findet `term` mit „Failed“ nichts?
3. **Aggregationen und Gegenprobe (Einheit 5.3):** Erklären Sie Schritt 3 und 4: Welche Rechner, Quellen und Mittelwerte ergeben sich, und wie bestätigt `jq` die Zahlen?
4. **Bausteine (Einheit 5.4):** Erklären Sie Schritt 5: Welche Aufgabe haben Beats, Logstash, Elasticsearch und Kibana, und was ist **nicht** bestätigt?

#### Kontrollfragen

1. Wann `term`, wann `match`?
2. Warum findet `term` „Failed“ nichts?
3. Wozu dient `bool` mit `filter`?
4. Was zeigt die Gegenprobe?

### Modul 6: Suchen und Auswerten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse zählen, ordnen und im Verlauf darstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Portscan und Passwortraten in den Daten finden.
  * Nach Abschluss dieses Moduls kann der Lernende Median und 95. Perzentil der Antwortzeiten bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerbilder bei falschen Feldnamen erkennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Zählen und Verlauf | 4 |
| 6.2 | Angriffsmuster | 4 |
| 6.3 | Antwortzeiten und Fehlerbild | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zählen und Verlauf (Einheit 6.1):** Führen Sie `bash auswerten.sh` aus. Erklären Sie Schritt 1 bis 3: Welche Auffälligkeiten zeigt der Stundenverlauf?
2. **Angriffsmuster (Einheit 6.2):** Erklären Sie Schritt 4 und 5: Wie erkennt man den Portscan (10.18.0.77) und die Passwortraten (10.18.0.99), und was geschah nach den Fehlschlägen?
3. **Antwortzeiten und Fehlerbild (Einheit 6.3):** Erklären Sie Schritt 6 bis 8: Warum ist die Stunde 16 Uhr auffällig, und warum liefert ein falscher Feldname nur 0 Treffer?

#### Kontrollfragen

1. Welche Stunde hat die meisten Ereignisse?
2. Wie erkennt man einen Portscan?
3. Was ist im Fall 10.18.0.99 besonders ernst?
4. Warum ist der Mittelwert der Antwortzeit schlecht?

### Modul 7: Warnungen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Warnregeln als Daten beschreiben (Schwelle, Zeitfenster, Gruppierung, Sperrzeit).
  * Nach Abschluss dieses Moduls kann der Lernende Alarmfluten durch Sperrzeiten verhindern.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlalarme prüfen und Schwellen begründen.
  * Nach Abschluss dieses Moduls kann der Lernende Stille (ausgefallene Quellen) erkennen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Regeln und Alarme | 4 |
| 7.2 | Sperrzeit und Fehlalarme | 3 |
| 7.3 | Stille und Selbsttest | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regeln und Alarme (Einheit 7.1):** Führen Sie `bash warnungen.sh` aus. Erklären Sie Schritt 1 und 2: Welche drei Alarme entstehen, und warum genau zu diesen Zeiten?
2. **Sperrzeit und Fehlalarme (Einheit 7.2):** Erklären Sie Schritt 3 und 4: Warum entstehen ohne Sperrzeit 178 statt 3 Alarme, und was zeigt der Test mit zu niedriger Schwelle?
3. **Stille und Selbsttest (Einheit 7.3):** Erklären Sie Schritt 5 bis 7: Was bedeutet eine Lücke von 95,5 Minuten bei `srv02`, und was prüft der Selbsttest?

#### Kontrollfragen

1. Warum eine Sperrzeit?
2. Was zeigt „Schwelle zu niedrig“?
3. Was bedeutet eine lange Lücke ohne Ereignis?
4. Wurde Graylog verwendet?

### Modul 8: Aufbewahrung, Datenschutz und Betrieb

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rotation mit `logrotate` einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Aufbewahrungsfristen umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Pseudonymisierung und Anonymisierung unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Speicherbedarf abschätzen und Unverändertheit belegen.
* **Voraussetzungen:** Modul 1; Modul 2; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Rotation und Fristen | 3 |
| 8.2 | Datenschutz | 3 |
| 8.3 | Nachweis und Planung | 3 |
| 8.4 | Abnahme | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rotation und Fristen (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1 und 2: Welche Dateien bleiben, was ist mit „Lauf 1“, und was löscht die Fristregel?
2. **Datenschutz (Einheit 8.2):** Erklären Sie Schritt 3, 4 und 7: Wie unterscheiden sich Pseudonymisierung und Anonymisierung (`mmanon`), und welche Felder können Personen betreffen?
3. **Nachweis und Planung (Einheit 8.3):** Erklären Sie Schritt 5 und 6: Wie erkennt die Hash-Kette eine geänderte Zeile, und wie wird der Speicherbedarf berechnet?
4. **Abnahme (Einheit 8.4):** Erklären Sie Schritt 8: Welche Prüfpunkte sind OK, und welcher ist absichtlich ein FEHLER?

#### Kontrollfragen

1. Warum bleiben nur 3 alte Dateien?
2. Pseudonymisierung oder Anonymisierung?
3. Wie erkennt die Hash-Kette Manipulation?
4. Ist die Datenschutz-Inventur Rechtsberatung?
