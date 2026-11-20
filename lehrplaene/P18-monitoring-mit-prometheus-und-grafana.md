# Lehrplan: Monitoring mit Prometheus und Grafana

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Linux-Grundlagen (Shell, Dienste, Dateien bearbeiten); Grundlagen von Netzwerken (IP-Adressen, Ports, HTTP); YAML und JSON lesen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Metriken und Zeitreihen, Prometheus (Konfiguration, Scraping, PromQL), Exporter (`node_exporter`, eigene Exporter, `windows_exporter` als Konfiguration), Alarmregeln und Alertmanager, Grafana-Dashboards (Bereitstellung als Dateien), Aufbewahrung und Speicher, Betrieb und Sicherung |
| **Thematische Abgrenzung (Out of Scope)** | Prometheus, Alertmanager und `node_exporter` laufen in den Übungen **wirklich** (Pakete von Ubuntu 24.04); die Messreihen der Module 3, 5, 6 und 7 sind erfunden und werden mit `promtool` eingespielt. **Grafana und `windows_exporter` werden nicht ausgeführt.** Nicht behandelt: Hochverfügbarkeit, Langzeitspeicher (Thanos, Mimir), Kubernetes, Tracing, Logs (siehe P19), Zabbix (siehe P17). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Metriken und Zeitreihen | 1 | 12 |
| 2 | Prometheus und Scraping | 1 | 14 |
| 3 | Abfragen mit PromQL | 1 | 14 |
| 4 | Exporter: node_exporter, eigene Exporter und windows_exporter | 1 | 14 |
| 5 | Alarmregeln und Alertmanager | 1 | 12 |
| 6 | Grafana-Dashboards | 1 | 12 |
| 7 | Aufbewahrung und Speicher | 2 | 10 |
| 8 | Betrieb, Sicherung und Abschlussprojekt | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Aufbewahrung und Speicher). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Gelesen:** Für diese Übungsreihe wurden **keine** Seiten der Herstellerdokumentation vollständig gelesen. Aufbau, Befehle und Optionen stammen aus Fachwissen und wurden, soweit es die installierten Programme betrifft, durch Ausführen geprüft (`promtool`, `amtool`, `prometheus`, `prometheus-alertmanager`, `prometheus-node-exporter`). **Standardports** (9090, 9093, 9100, 9182, 3000), die **Installation von Grafana** und der Aufbau der Dashboard-JSON-Dateien sind Fachwissen und **nicht bestätigt**.\n\n**Getestet mit (Ubuntu 24.04, Cloud-Container, kein systemd):** Prometheus 2.45.3, Alertmanager 0.26.0 (mit `amtool`), `node_exporter` 1.7.0 (Ubuntu-Pakete), `promtool`, Python 3 mit `bcrypt` und `yaml`, `jq`, `curl`. **Nicht ausgeführt:** Grafana, `windows_exporter`, Dienste unter systemd, Windows, Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Monitoring`, `10.18.0.0/24`).

**VM 1:** `mon01` (**erforderlich**, `10.18.0.10`): Ubuntu Server (LTS) mit Prometheus, Alertmanager und Grafana; Rechte: `sudo`.

**VM 2:** `lin01` (**erforderlich**, `10.18.0.21`): Ubuntu Server als überwachter Host mit `node_exporter`.

**VM 3:** `win01` (optional, `10.18.0.31`): Windows als überwachter Host mit `windows_exporter` (Modul 4, nur als Konfiguration).

**Internetphase:** Für die Installation der Pakete brauchen `mon01` und `lin01` vorübergehend Internetzugang; danach wird der Zugang entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 5 und vor Modul 8 von `mon01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte starten ihre eigenen Prozesse auf `127.0.0.1` (Ports 19090 bis 19101) und arbeiten unter `/tmp/p18`; sie brauchen weder die VMs noch Grafana.

## B. Detaillierter Modulaufbau

### Modul 1: Metriken und Zeitreihen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Textformat von Metriken lesen (`HELP`, `TYPE`, Labels).
  * Nach Abschluss dieses Moduls kann der Lernende Zähler (counter) und Messwert (gauge) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Zeitreihen zählen und die Kardinalität abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Metriken mit `promtool check metrics` prüfen.
* **Voraussetzungen:** Linux-Shell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Textformat lesen | 4 |
| 1.2 | Zähler und Messwert | 4 |
| 1.3 | Kardinalität und Namensprüfung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Textformat lesen (Einheit 1.1):** Führen Sie `bash metriken.sh` aus. Beschreiben Sie anhand von Schritt 1 und 2 den Aufbau einer Metrik und nennen Sie die Metrikarten im Bestand.
2. **Zähler und Messwert (Einheit 1.2):** Erklären Sie Schritt 3: Wie unterscheidet sich das Verhalten eines Zählers von dem eines Messwerts, und warum braucht man `rate()`?
3. **Kardinalität und Namensprüfung (Einheit 1.3):** Rechnen Sie Schritt 4 nach und erklären Sie die Beanstandungen in Schritt 5. Welche Regeln verletzt die absichtlich schlechte Metrik?

#### Kontrollfragen

1. Was steht in `# TYPE`?
2. Wann ist ein Wert ein Zähler?
3. Was ist eine Zeitreihe?
4. Warum sind viele Labelwerte ein Problem?

### Modul 2: Prometheus und Scraping

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Konfiguration (`prometheus.yml`) aufbauen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Ziele (`static_configs`, `file_sd_configs`) und Labels festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Zustand der Ziele und die Metrik `up` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationsfehler mit `promtool check config` finden.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Konfiguration prüfen | 6 |
| 2.2 | Ziele und `up` | 4 |
| 2.3 | Ziele per Datei | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration prüfen (Einheit 2.1):** Führen Sie `bash scraping.sh` aus. Erklären Sie die Konfiguration aus Schritt 1 (`global`, `external_labels`, `scrape_configs`, `relabel_configs`) und die Fehlermeldung aus Schritt 2.
2. **Ziele und `up` (Einheit 2.2):** Erklären Sie Schritt 3 und 4: Welche Ziele gibt es, welche Labels tragen sie, und was bedeutet der Wert von `up`?
3. **Ziele per Datei (Einheit 2.3):** Erklären Sie Schritt 5 und 6: Wie kommt ein neues Ziel ohne Neustart hinzu, und woran erkennt man Zeitreihen im Speicher?

#### Kontrollfragen

1. Wie oft sammelt Prometheus Werte?
2. Was bedeutet `up` = 0?
3. Wozu dienen `external_labels`?
4. Wie kommen Ziele ohne Neustart hinzu?
5. Was prüft `promtool check config`?

### Modul 3: Abfragen mit PromQL

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zeitreihen mit Label-Filtern auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende Zähler mit `rate()` auswerten und mit `sum by` zusammenfassen.
  * Nach Abschluss dieses Moduls kann der Lernende Auslastung, Platzprognose und Fehlerquote berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Histogramme mit `histogram_quantile` auswerten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Auswählen und Filtern | 6 |
| 3.2 | Rechnen mit Zählern | 4 |
| 3.3 | Anwendungsmetriken | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auswählen und Filtern (Einheit 3.1):** Führen Sie `bash promql.sh` aus. Erklären Sie Schritt 1: Was liefern `up`, `up{job="node"}` und `up{instance=~"srv.*"} == 0`?
2. **Rechnen mit Zählern (Einheit 3.2):** Erklären Sie Schritt 2 bis 4: `rate()`, `sum by`, die CPU- und Speicherformeln und die Plattenprognose mit `predict_linear`.
3. **Anwendungsmetriken (Einheit 3.3):** Erklären Sie Schritt 5 bis 7: Fehlerquote, 95. Perzentil mit `histogram_quantile`, `offset`, `topk`, `absent` und die Zahl der Messpunkte einer Bereichsabfrage.

#### Kontrollfragen

1. Was macht `rate(x[5m])`?
2. Wozu dient `sum by (instance)`?
3. Wofür braucht man `histogram_quantile`?
4. Was liefert `absent(...)`?
5. Wie viele Messpunkte liefert eine Bereichsabfrage über 10 Minuten bei Schritt 60 s?

### Modul 4: Exporter: node_exporter, eigene Exporter und windows_exporter

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Textfile-Collector für Skriptwerte nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen eigenen Exporter im Textformat liefern und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Alter einer Sicherung mit `time()` abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Windows-Ziel in der Konfiguration beschreiben (nicht ausgeführt).
* **Voraussetzungen:** Modul 2; Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Textfile-Collector | 6 |
| 4.2 | Eigener Exporter | 4 |
| 4.3 | Windows-Ziel | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Textfile-Collector (Einheit 4.1):** Führen Sie `bash exporter.sh` aus. Erklären Sie Schritt 1 und 2: Warum wird die Datei erst unter anderem Namen geschrieben und dann umbenannt?
2. **Eigener Exporter (Einheit 4.2):** Erklären Sie Schritt 3 und 4: Welche Metrikarten liefert der eigene Exporter, und wie kommt Prometheus an beide Ziele?
3. **Windows-Ziel (Einheit 4.3):** Erklären Sie Schritt 5: Was steht in der Konfiguration für `win01`, und was wurde dabei **nicht** geprüft?

#### Kontrollfragen

1. Wozu dient der Textfile-Collector?
2. Warum Datei umbenennen?
3. Wie fragt man das Alter der letzten Sicherung ab?
4. Welche Art ist `uebung_abrufe_total`?
5. Wurde `windows_exporter` ausgeführt?

### Modul 5: Alarmregeln und Alertmanager

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Alarmregeln mit `for` und Labels schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln mit `promtool test rules` automatisch prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Routing, Hemmung und Stummschaltung im Alertmanager einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Benachrichtigungen an einen Webhook senden.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Regeln und Tests | 4 |
| 5.2 | Fehlschlagender Test | 4 |
| 5.3 | Routing, Hemmung, Stummschaltung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regeln und Tests (Einheit 5.1):** Führen Sie `bash alarmierung.sh` aus. Erklären Sie die drei Regeln aus Schritt 1 und den Regeltest aus Schritt 2: Warum feuert `HostDown` erst nach 6 Minuten, nicht nach 4?
2. **Fehlschlagender Test (Einheit 5.2):** Erklären Sie Schritt 3: Warum schlägt der Test fehl, und was zeigt die Ausgabe?
3. **Routing, Hemmung, Stummschaltung (Einheit 5.3):** Erklären Sie Schritt 4 bis 7: Welcher Alarm geht an welchen Empfänger, welcher wird gehemmt, und was bewirkt die Stummschaltung?

#### Kontrollfragen

1. Was bewirkt `for: 2m`?
2. Was macht `routes test`?
3. Was bedeutet Hemmung (inhibition)?
4. Was ist der Unterschied zwischen Hemmung und Stummschaltung?

### Modul 6: Grafana-Dashboards

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Datenquelle und Dashboards als Dateien bereitstellen (Provisioning).
  * Nach Abschluss dieses Moduls kann der Lernende ein Dashboard als JSON mit Variable und Panels lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Panel-Abfragen gegen Prometheus prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Schwellwerte und Fehlerbilder („No data“) erklären.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Provisioning | 4 |
| 6.2 | Dashboard-JSON | 4 |
| 6.3 | Abfragen prüfen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Provisioning (Einheit 6.1):** Führen Sie `bash grafana.sh` aus. Erklären Sie Schritt 1: Was steht in den beiden Bereitstellungsdateien, und welche Rolle hat `uid`?
2. **Dashboard-JSON (Einheit 6.2):** Erklären Sie Schritt 2 und 6: Welche Panels gibt es, wie ist die Variable `$instance` definiert, und wie sind die Schwellwerte gesetzt?
3. **Abfragen prüfen (Einheit 6.3):** Erklären Sie Schritt 3 bis 5: Wie ersetzt Grafana `$instance` und `$__rate_interval`, und warum bleibt ein Panel bei falschem Wert leer?

#### Kontrollfragen

1. Was ist Provisioning?
2. Wozu dient `$instance`?
3. Wurde Grafana ausgeführt?
4. Warum zeigt ein Panel „No data“?

### Modul 7: Aufbewahrung und Speicher

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Blöcke der Zeitreihendatenbank und ihre Kennzahlen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Aufbewahrungszeit und -größe festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Recording Rules schreiben und testen.
  * Nach Abschluss dieses Moduls kann der Lernende Speicherbedarf abschätzen, Schnappschuss erstellen, Reihen löschen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Blöcke und Analyse | 5 |
| 7.2 | Regeln, Aufbewahrung, Verwaltung | 5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Blöcke und Analyse (Einheit 7.1):** Führen Sie `bash speicher.sh` aus. Erklären Sie Schritt 1 und 2: Was zeigen `promtool tsdb list` und `analyze`?
2. **Regeln, Aufbewahrung, Verwaltung (Einheit 7.2):** Erklären Sie Schritt 3 bis 7: Recording Rule mit Test, Startoptionen für die Aufbewahrung, Rechenbeispiel, Schnappschuss und Löschen von Reihen.

#### Kontrollfragen

1. Wie lange hebt Prometheus Daten auf?
2. Wozu dient eine Recording Rule?
3. Wie sichert man laufende Daten?
4. Was bleibt nach dem Löschen von Reihen?

### Modul 8: Betrieb, Sicherung und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zustand mit `/-/healthy` und `/-/ready` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Konfiguration im Betrieb neu laden und Fehler abfangen.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriff mit Basic Auth schützen.
  * Nach Abschluss dieses Moduls kann der Lernende Daten sichern und auf einer Kopie wiederherstellen; ein Abschlussprojekt prüfen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Zustand und Neuladen | 4 |
| 8.2 | Zugriffsschutz und Sicherung | 4 |
| 8.3 | Abschlussprojekt | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zustand und Neuladen (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1 bis 3: Was zeigen die Zustandsabfragen, und was passiert bei einem Neuladen mit gültiger und mit fehlerhafter Konfiguration?
2. **Zugriffsschutz und Sicherung (Einheit 8.2):** Erklären Sie Schritt 4 und 5: Wie schützt `web.yml` den Zugang, und wie wird die Sicherung wiederhergestellt?
3. **Abschlussprojekt (Einheit 8.3):** Setzen Sie im Labor den Mini-Stack um (Prometheus, `node_exporter`, Alarmregel, Alertmanager, Sicherung) und prüfen Sie ihn mit einer Liste wie in Schritt 6. Schreiben Sie einen Bericht mit offenen Punkten.

#### Kontrollfragen

1. Was ist der Unterschied zwischen `healthy` und `ready`?
2. Was geschieht bei fehlerhafter Konfiguration und Reload?
3. Wie wird das Passwort in `web.yml` gespeichert?
4. Warum die Sicherung testen?
