# Lehrplan: IDS und IPS mit Suricata

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen; TCP/IP-Grundlagen (Adressen, Ports, Verbindungsaufbau); Linux-Grundlagen (Kommandozeile, Dateien); HTTP, DNS und TLS im Überblick |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Suricata (getestet mit 7.0.3), Regelsyntax, Offline-Analyse von Mitschnitten (`-r`), Protokollfelder für HTTP, DNS und TLS, `eve.json`, Schwellwerte und Ausnahmen, IPS-Modus im Überblick, Regelverwaltung, Betrieb und Auswertung |
| **Thematische Abgrenzung (Out of Scope)** | Zentrales Logging (Graylog, Elastic Stack) ist ein eigener Kurs; OPNsense-Konfiguration nur soweit nötig (eigener Kurs). Nicht behandelt: Betrieb im Hochgeschwindigkeitsnetz (Leistungsoptimierung), Lua-Skripte, Dateiextraktion im Detail. Nur im isolierten Labor und mit eigenen Systemen: keine Tests gegen fremde Systeme |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | IDS und IPS: Suricata im Überblick | 1 | 12 |
| 2 | Regeln schreiben | 1 | 14 |
| 3 | Mitschnitte offline analysieren | 1 | 14 |
| 4 | Protokolle und Felder: HTTP, DNS, TLS | 1 | 14 |
| 5 | Tuning und Fehlalarme | 1 | 12 |
| 6 | IPS-Betrieb im Überblick | 2 | 12 |
| 7 | Regelverwaltung | 1 | 10 |
| 8 | Betrieb, Auswertung und Abschlussprojekt | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 5, 7 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 6 (IPS-Betrieb). Fällt Modul 6 weg, verringert sich der Gesamtumfang auf 88 UE; kein Pflichtmodul setzt Modul 6 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Suricata (Regelsyntax, Konfiguration, `suricata-update`) wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt; verbindlich ist die Dokumentation der eingesetzten Version. Zahlen, Namen und Daten sind erfundene Beispieldaten.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container, kein systemd):** Suricata 7.0.3 im Offline-Modus (`-r`) auf Mitschnitten, die `tcpdump` an der Loopback-Schnittstelle aufnahm (Verkehr zu einem Python-Webserver, einem kleinen DNS-Server, `openssl s_server` und geschlossenen Ports); `curl`, `openssl`, Python 3. **Nicht ausgeführt:** Inline-Betrieb (NFQ, AF_PACKET im IPS-Modus), `suricata-update` und Regelquellen (brauchen Internet), Betrieb als Dienst, echte Netzwerke, Leistungsmessung.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-IDS`, `10.62.0.0/24`).

**VM:** `ids01` (**erforderlich**, `10.62.0.2`): Linux-Server (Debian oder Ubuntu) mit Suricata; optional `web01` und `cl01` als Verkehrsquellen im selben Netz.

**Internetphase:** Für die Installation von Suricata (und `suricata-update`) braucht `ids01` vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 5 und vor Modul 6 von `ids01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte erzeugen Verkehr nur über die Loopback-Schnittstelle des Rechners, auf dem sie laufen, und werten ihn mit Suricata im Offline-Modus aus. Auf `ids01` wird stattdessen Verkehr zwischen den VMs mitgeschnitten (`tcpdump -w`) und ausgewertet. **Nur eigene Systeme untersuchen.**

## B. Detaillierter Modulaufbau

### Modul 1: IDS und IPS: Suricata im Überblick

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen IDS und IPS erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Version und Fähigkeiten von Suricata abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende die Konfiguration mit `-T` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Ausgabedateien `fast.log` und `eve.json` lesen.
* **Voraussetzungen:** TCP/IP-Grundlagen; Linux-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Fähigkeiten prüfen | 3 |
| 1.2 | Erster Lauf | 3 |
| 1.3 | Ereignisarten | 3 |
| 1.4 | Labor planen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fähigkeiten prüfen (Einheit 1.1):** Führen Sie `bash grundlagen.sh` aus. Lesen Sie Schritt 1 und 2: Welche Version läuft, und welche Modi (`NFQ`, `AF_PACKET`) sind eingebaut?
2. **Erster Lauf (Einheit 1.2):** Erklären Sie Schritt 3 bis 5: Wie entsteht der Mitschnitt, warum meldet die eine Regel genau einmal, und was steht in `fast.log`?
3. **Ereignisarten (Einheit 1.3):** Erklären Sie Schritt 6 und 7: Welche Ereignisarten schreibt Suricata in `eve.json`, obwohl nur eine Regel geladen ist?
4. **Labor planen (Einheit 1.4):** Planen Sie `ids01` in Hyper-V (privater Switch, Internetphase für die Installation) und halten Sie fest, welche Verkehrsquellen Sie benötigen.

#### Kontrollfragen

1. Worin unterscheiden sich IDS und IPS?
2. Was ist der Offline-Modus?
3. Wozu dient `-T`?
4. Welche Ereignisarten stehen ohne passende Regel in `eve.json`?

### Modul 2: Regeln schreiben

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Regel (Aktion, Protokoll, Adressen, Optionen) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln mit `content`, `flow`, `startswith` und `nocase` schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlermeldungen bei fehlerhaften Regeln deuten.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Regelaufbau | 5 |
| 2.2 | Treffer vergleichen | 3 |
| 2.3 | Fehler lesen | 3 |
| 2.4 | Eigene Regel | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regelaufbau (Einheit 2.1):** Führen Sie `bash regeln.sh` aus. Zerlegen Sie eine Regel aus Schritt 1 in Kopf (Aktion, Protokoll, Adressen) und Optionen.
2. **Treffer vergleichen (Einheit 2.2):** Erklären Sie Schritt 2 und 3: Warum trifft Regel 1000002 zweimal, Regel 1000001 aber nur einmal?
3. **Fehler lesen (Einheit 2.3):** Erklären Sie Schritt 4 und 5: Welche Meldung erscheint bei einem unbekannten Schlüsselwort und bei fehlender `sid`?
4. **Eigene Regel (Einheit 2.4):** Schreiben Sie eine Regel, die Anfragen an `/index.html` meldet, und prüfen Sie sie mit `suricata -T`.

#### Kontrollfragen

1. Welche Teile hat der Regelkopf?
2. Was bewirkt `startswith`?
3. Was bewirkt `flow:established,to_server`?
4. Warum braucht jede Regel eine `sid`?

### Modul 3: Mitschnitte offline analysieren

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Mitschnitt mit `tcpdump` kennzahlenmäßig beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Flows und Anwendungsprotokolle aus `eve.json` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wiederholbarkeit einer Auswertung prüfen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Mitschnitt beschreiben | 5 |
| 3.2 | Flows lesen | 3 |
| 3.3 | Wiederholbarkeit | 3 |
| 3.4 | Eigener Mitschnitt | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Mitschnitt beschreiben (Einheit 3.1):** Führen Sie `bash pcap_analyse.sh` aus. Erklären Sie Schritt 1: Welche Ports kommen vor und was bedeuten die Paketzahlen?
2. **Flows lesen (Einheit 3.2):** Erklären Sie Schritt 3: Warum haben die Ports 21, 22, 23 und 3389 nur zwei Pakete und keine Anwendungsprotokoll-Angabe?
3. **Wiederholbarkeit (Einheit 3.3):** Erklären Sie Schritt 4 und 5: Was zeigt der zweite Lauf, und was passiert ohne Regeln?
4. **Eigener Mitschnitt (Einheit 3.4):** Planen Sie, wie Sie auf `ids01` den Verkehr zwischen `cl01` und `web01` mitschneiden (`tcpdump -w`) und danach offline auswerten.

#### Kontrollfragen

1. Warum eignet sich der Offline-Modus zum Üben?
2. Was ist ein Flow?
3. Was ergibt ein Lauf ohne Regeln?
4. Warum haben geschlossene Ports nur zwei Pakete?

### Modul 4: Protokolle und Felder: HTTP, DNS, TLS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Regeln auf `dns.query`, `tls.sni` und HTTP-Felder schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die Ereignisse `dns`, `tls` und `http` in `eve.json` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenze der Sicht bei verschlüsseltem Verkehr nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Felder nutzen | 5 |
| 4.2 | Trefferbild | 3 |
| 4.3 | Ereignisse lesen | 3 |
| 4.4 | Regel für Ihr Netz | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Felder nutzen (Einheit 4.1):** Führen Sie `bash protokolle.sh` aus. Erklären Sie für jede Regel aus Schritt 1, welches Feld sie prüft.
2. **Trefferbild (Einheit 4.2):** Erklären Sie Schritt 2: Warum fehlt die Meldung zu Regel 1000404 (`tls.cert_subject`)?
3. **Ereignisse lesen (Einheit 4.3):** Erklären Sie Schritt 3 bis 5 und vergleichen Sie, was Suricata zu DNS, TLS und HTTP protokolliert.
4. **Regel für Ihr Netz (Einheit 4.4):** Schreiben Sie eine Regel, die DNS-Abfragen auf eine Domain Ihrer Wahl meldet, und prüfen Sie sie mit `-T`.

#### Kontrollfragen

1. Welches Feld prüft `dns.query`?
2. Warum zeigt `subject` bei TLS 1.3 keinen Wert?
3. Was meldet 1000402?
4. Warum ist HTTP lesbarer als TLS?

### Modul 5: Tuning und Fehlalarme

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende laute Regeln mit `threshold` begrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Meldungen mit `suppress` unterdrücken.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung einer `pass`-Regel erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln gezielt abschalten.
* **Voraussetzungen:** Modul 2; Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Ausgangslage | 3 |
| 5.2 | Begrenzen | 3 |
| 5.3 | Unterdrücken | 3 |
| 5.4 | Ausnahme und Abschalten | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ausgangslage (Einheit 5.1):** Führen Sie `bash tuning.sh` aus. Erklären Sie Schritt 1: Warum meldet Regel 1000501 so oft?
2. **Begrenzen (Einheit 5.2):** Vergleichen Sie in Schritt 2 die Regeln 1000502 und 1000503.
3. **Unterdrücken (Einheit 5.3):** Erklären Sie Schritt 3: Was bewirkt die `suppress`-Zeile und was kann sie nicht?
4. **Ausnahme und Abschalten (Einheit 5.4):** Erklären Sie Schritt 4 und 5: Welche Meldungen verschwinden durch die `pass`-Regel, welche bleiben, und warum?

#### Kontrollfragen

1. Was bewirkt `threshold:type limit, count 2`?
2. Wann nimmt man `suppress` statt die Regel zu löschen?
3. Was geschieht mit Meldungen nach einer `pass`-Regel?
4. Wie schaltet man eine Regel ab?

### Modul 6: IPS-Betrieb im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aktionen `alert`, `drop` und `reject` unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Suricata inline betrieben wird.
  * Nach Abschluss dieses Moduls kann der Lernende die Risiken eines IPS (Fehlalarme, Ausfall) nennen.
* **Voraussetzungen:** Modul 2; Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Fähigkeit prüfen | 4 |
| 6.2 | Aktionen vergleichen | 4 |
| 6.3 | Risiken abwägen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fähigkeit prüfen (Einheit 6.1):** Führen Sie `bash ips.sh` aus. Erklären Sie Schritt 1 und lesen Sie die Datei `ips_nfqueue.txt`.
2. **Aktionen vergleichen (Einheit 6.2):** Erklären Sie Schritt 3 und 4: Wie unterscheiden sich die Aktionen in `fast.log` und `eve.json`?
3. **Risiken abwägen (Einheit 6.3):** Beschreiben Sie, was ein Fehlalarm im IPS-Betrieb bewirkt und warum „bypass“ bei der Warteschlange eine Entscheidung ist.

#### Kontrollfragen

1. Was unterscheidet `drop` von `alert`?
2. Was zeigt `[wDrop]` in `fast.log`?
3. Warum verwirft der Offline-Lauf nichts?
4. Welches Risiko hat ein IPS gegenüber einem IDS?

### Modul 7: Regelverwaltung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Regeldateien über `rule-files` einbinden.
  * Nach Abschluss dieses Moduls kann der Lernende doppelte SIDs und Fassungen (`rev`) erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Konfiguration und Regeln vor dem Einsatz prüfen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Standardkonfiguration | 4 |
| 7.2 | Doppelte Kennungen | 2 |
| 7.3 | Fassungen | 2 |
| 7.4 | Verwaltung planen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Standardkonfiguration (Einheit 7.1):** Führen Sie `bash regelverwaltung.sh` aus. Erklären Sie Schritt 1: Wo liegen die Regeln und welche Datei wird geladen?
2. **Doppelte Kennungen (Einheit 7.2):** Erklären Sie Schritt 3 und 4: Was geschieht, wenn dieselbe `sid` in zwei Dateien steht?
3. **Fassungen (Einheit 7.3):** Erklären Sie Schritt 5 und die Warnung zu Regel 1000703 aus Schritt 4.
4. **Verwaltung planen (Einheit 7.4):** Lesen Sie `regelquellen.txt` und beschreiben Sie, wie Sie Regelquellen beziehen, aktualisieren und einzelne Regeln abschalten würden.

#### Kontrollfragen

1. Wie bindet man eigene Regeldateien ein?
2. Was passiert bei zwei Regeln mit gleicher `sid`?
3. Wozu `-T` vor dem Neustart?
4. Warum Quellen und Lizenzen prüfen?

### Modul 8: Betrieb, Auswertung und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Kennzahlen aus `stats.log` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Bericht aus `eve.json` erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Regelsatz für ein kleines Netz zusammenstellen und prüfen.
* **Voraussetzungen:** Module 2 bis 5; Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Regelsatz lesen | 3 |
| 8.2 | Kennzahlen | 3 |
| 8.3 | Bericht | 3 |
| 8.4 | Abschlussprojekt | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regelsatz lesen (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie den Regelsatz in Schritt 1: Welches Risiko deckt jede Regel ab?
2. **Kennzahlen (Einheit 8.2):** Erklären Sie Schritt 2: Was sagen `decoder.pkts`, `flow.total`, `detect.alert` und die `app_layer`-Zähler?
3. **Bericht (Einheit 8.3):** Erklären Sie Schritt 3 und 4 und formulieren Sie zwei Sätze für eine Leitung, die nicht technisch ist.
4. **Abschlussprojekt (Einheit 8.4):** Stellen Sie für ein erfundenes kleines Netz (Webserver, DNS-Server, Administrationszugang) einen Regelsatz mit fünf bis acht Regeln zusammen, begründen Sie jede Regel und beschreiben Sie, wie Sie Fehlalarme begrenzen.

#### Kontrollfragen

1. Was zählt `detect.alert`?
2. Was ist der Unterschied zwischen Priorität und Schweregrad in der Auswertung?
3. Wozu dient der Bericht?
4. Warum Regeln begründen?
