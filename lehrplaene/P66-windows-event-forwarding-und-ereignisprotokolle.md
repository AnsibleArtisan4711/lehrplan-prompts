# Lehrplan: Windows-Ereignisweiterleitung und Ereignisprotokolle

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Windows-Administration (Ereignisanzeige, Gruppenrichtlinien, Dienste); Grundlagen von XML; Netzwerkgrundlagen |
| **Gesamtumfang** | 8 Module, 45 UE (zu 45 Minuten; 33,75 Stunden) |
| **Fokus-Technologien** | Aufbau von Windows-Ereignissen und Protokollkanälen, Ereignisabfragen (XPath-Stil), Auswertung von Anmeldeereignissen, Abonnements der Ereignisweiterleitung (Windows Event Forwarding), Filter und Mengenplanung, Aufbewahrung und Nachweis der Unverändertheit, Umsetzung nach Syslog, Erkennungsregeln |
| **Thematische Abgrenzung (Out of Scope)** | Es wird **kein Windows** ausgeführt: Die Übungen arbeiten mit erfundenen Ereignissen im Aufbau von Windows-Ereignissen und mit Python als Modell. Nicht behandelt: Betrieb eines Sammlers (`wecsvc`), Zertifikatsbetrieb, SIEM-Produkte, Sysmon, Auditrichtlinien im Detail. Befehle (`wecutil`, `winrm`, `wevtutil`) stehen als Text. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Ereignisse und Protokollkanäle | 1 | 5 |
| 2 | Ereignisabfragen im XPath-Stil | 1 | 6 |
| 3 | Anmeldeereignisse auswerten | 1 | 6 |
| 4 | Abonnements der Ereignisweiterleitung | 1 | 6 |
| 5 | Filter und Mengenplanung | 1 | 5 |
| 6 | Aufbewahrung und Nachweis | 1 | 6 |
| 7 | Weiterleitung nach Syslog | 2 | 5 |
| 8 | Erkennungsregeln und Abschlussprojekt | 1 | 6 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **45** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Weiterleitung nach Syslog). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 40 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Gelesen:** Die Seite zu `wecutil` (Microsoft Learn, [Wecutil.exe](https://learn.microsoft.com/windows/win32/wec/wecutil)) wurde vollständig gelesen; die Beispiel-XML-Dateien für Abonnements stammen im Aufbau von dort. **Nur Suchauszüge gelesen** (nicht die ganzen Seiten): [Setting up a Source Initiated Subscription](https://learn.microsoft.com/windows/win32/wec/setting-up-a-source-initiated-subscription), [Use Windows Event Forwarding to help with intrusion detection](https://learn.microsoft.com/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection), [Appendix L: Events to monitor](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor) und Beiträge zu den Ereignissen 4625, 4740 und 1102. Die Ereignis-IDs 4720 und 7045 sowie Anmeldetypen stammen aus Fachwissen und sind **nicht** belegt. Alle Ereignisse, Namen und Adressen sind erfunden.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** Python 3 mit `lxml`, `xmllint`, Bash. **Nicht ausgeführt:** Windows, `wecutil`, `winrm`, `wevtutil`, Gruppenrichtlinien, Syslog-Server oder -Weiterleitungsprodukte.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Logs`, `10.66.0.0/24`).

**VM 1:** `dc01` (**erforderlich**, `10.66.0.10`): Windows Server als Domänencontroller mit Gruppenrichtlinien.

**VM 2:** `wec01` (**erforderlich**, `10.66.0.11`): Windows Server als Ereignissammler (Domänenmitglied).

**VM 3:** `pc01` (**erforderlich**, `10.66.0.21`): Windows-Client als Ereignisquelle (Domänenmitglied). Optional: `log01` (Linux) für Modul 7.

**Internetphase:** Für die Installation der Pakete braucht `log01` vorübergehend Internetzugang; danach wird er entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 4 von `dc01`, `wec01` und `pc01` Prüfpunkte anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte erzeugen erfundene Ereignisse selbst (`gen_events.py`) und arbeiten unter `/tmp/p66`; sie brauchen kein Windows.

## B. Detaillierter Modulaufbau

### Modul 1: Ereignisse und Protokollkanäle

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines Ereignisses (System und Nutzdaten) lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse nach Kanal und Computer zählen.
  * Nach Abschluss dieses Moduls kann der Lernende häufige Ereignis-IDs einordnen.
* **Voraussetzungen:** Ereignisanzeige kennen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Aufbau | 3 |
| 1.2 | Zählen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbau (Einheit 1.1):** Führen Sie `bash ereignisse.sh` aus. Beschreiben Sie anhand von Schritt 1 die Felder `Provider`, `EventID`, `Level`, `TimeCreated`, `Channel`, `Computer` und die Nutzdaten.
2. **Zählen (Einheit 1.2):** Werten Sie Schritt 2 und 3 aus: Welcher Kanal ist am häufigsten, und welche IDs gehören zu Anmeldungen?

#### Kontrollfragen

1. Was steht im Teil `System`?
2. Wo stehen Benutzername und Adresse?
3. Welche Kanäle enthält der Beispielbestand?
4. Was bedeutet 4625?

### Modul 2: Ereignisabfragen im XPath-Stil

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Abfragen nach ID, Computer und Nutzdaten schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Bedingungen mit `and` und `or` verbinden.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen von XPath 1.0 bei Zeitvergleichen erkennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Einfache Abfragen | 2 |
| 2.2 | Kombination | 2 |
| 2.3 | Zeit und Stufe | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einfache Abfragen (Einheit 2.1):** Führen Sie `bash abfragen.sh` aus. Erklären Sie die Ausdrücke aus Schritt 1 bis 3.
2. **Kombination (Einheit 2.2):** Erklären Sie die Abfrage in Schritt 4 und schreiben Sie eine eigene für Benutzer `ben` auf `pc01`.
3. **Zeit und Stufe (Einheit 2.3):** Erklären Sie Schritt 5: Warum liefert der Vergleich der Zeichenkette keine Treffer, und wie wird der Zeitraum im Modell geprüft?

#### Kontrollfragen

1. Was bedeutet `*[System[(EventID=4625)]]`?
2. Wie verbindet man Bedingungen?
3. Warum scheitert der Zeitvergleich im Modell?
4. Was bleibt unverifiziert?

### Modul 3: Anmeldeereignisse auswerten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldeerfolge und -fehler je Benutzer zählen.
  * Nach Abschluss dieses Moduls kann der Lernende Serien von Fehlversuchen je Adresse erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Kontosperre dem Auslöser zuordnen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Zählen | 2 |
| 3.2 | Serie erkennen | 2 |
| 3.3 | Sperre | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zählen (Einheit 3.1):** Führen Sie `bash anmeldungen.sh` aus. Erklären Sie Schritt 1 bis 3: Welcher Benutzer fällt auf, und woran sieht man die Quelle?
2. **Serie erkennen (Einheit 3.2):** Erklären Sie Schritt 4: Wie arbeitet die Prüfung „mindestens 5 in 60 Sekunden“?
3. **Sperre (Einheit 3.3):** Erklären Sie Schritt 5 und überlegen Sie, wie man die Sperre vom Tippfehler unterscheidet.

#### Kontrollfragen

1. Wie unterscheiden sich Typ 2 und Typ 3?
2. Warum ist die Adresse wichtig?
3. Was sagt Ereignis 4740?
4. Sind Schwelle und Zeitfenster verbindlich?

### Modul 4: Abonnements der Ereignisweiterleitung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Abonnement-XML-Datei lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die beiden Abonnementarten unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Sammler und Quelle laut Dokumentation einrichten (als Text).
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Datei prüfen | 2 |
| 4.2 | Fehlerfall | 2 |
| 4.3 | Einrichtung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Datei prüfen (Einheit 4.1):** Führen Sie `bash abonnement.sh` aus. Erklären Sie die Elemente `SubscriptionType`, `Delivery`, `Query`, `LogFile` und `AllowedSourceDomainComputers` aus Schritt 1 und 2.
2. **Fehlerfall (Einheit 4.2):** Erklären Sie Schritt 3: Warum meldet das Prüfwerkzeug einen Fehler?
3. **Einrichtung (Einheit 4.3):** Ordnen Sie die Befehle aus Schritt 4 den Rechnern (Quelle, Sammler) zu und beschreiben Sie, wie man prüft, ob Ereignisse ankommen.

#### Kontrollfragen

1. Was ist ein source-initiated Abonnement?
2. Was ist ein collector-initiated Abonnement?
3. In welches Protokoll werden Ereignisse geschrieben?
4. Welche Befehle prüfen den Stand?

### Modul 5: Filter und Mengenplanung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Filtermengen nach Anteil am Bestand vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache Mengenabschätzung rechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Rauschen erkennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Filtermengen | 3 |
| 5.2 | Hochrechnung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Filtermengen (Einheit 5.1):** Führen Sie `bash filter.sh` aus. Erklären Sie Schritt 1: Welche Filter liefern welchen Anteil?
2. **Hochrechnung (Einheit 5.2):** Erklären Sie Schritt 2 und 3: Welche Annahmen stecken in der Rechnung, und wie ordnet man das Ergebnis ein?

#### Kontrollfragen

1. Warum nicht alles weiterleiten?
2. Welche Annahmen nutzt die Hochrechnung?
3. Welche Faustregel nennt die Dokumentation?
4. Warum die Zahlen messen?

### Modul 6: Aufbewahrung und Nachweis

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Aufbewahrungsfrist mit Trockenlauf umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Prüfsummenlisten als Nachweis nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende Rotation nach Größe beschreiben.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Frist | 2 |
| 6.2 | Nachweis | 2 |
| 6.3 | Rotation | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Frist (Einheit 6.1):** Führen Sie `bash archiv.sh` aus. Erklären Sie Schritt 1 und 2: Welche Dateien fallen unter die Frist, und was zeigt der Trockenlauf?
2. **Nachweis (Einheit 6.2):** Erklären Sie Schritt 3 bis 5: Wie erkennt man später fehlende und veränderte Dateien?
3. **Rotation (Einheit 6.3):** Erklären Sie Schritt 6 und nennen Sie ein Risiko beim Überschreiben des ältesten Eintrags.

#### Kontrollfragen

1. Wozu ein Trockenlauf?
2. Was belegt die Prüfsummenliste?
3. Warum zeigt Schritt 4 „Datei fehlt“?
4. Wer legt rechtliche Fristen fest?

### Modul 7: Weiterleitung nach Syslog

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse in eine Syslog-Zeile umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Priorität aus Facility und Schweregrad berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Informationsverlust beim Umsetzen benennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Umsetzung | 3 |
| 7.2 | Priorität und Prüfung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Umsetzung (Einheit 7.1):** Führen Sie `bash syslog.sh` aus. Erklären Sie den Aufbau einer Zeile aus Schritt 1.
2. **Priorität und Prüfung (Einheit 7.2):** Erklären Sie Schritt 2 bis 5: Wie entsteht die Zahl in spitzen Klammern, und was geht verloren?

#### Kontrollfragen

1. Wie berechnet sich die Priorität?
2. Welche Annahmen stecken im Modell?
3. Was geht verloren?
4. Wurde ein Produkt getestet?

### Modul 8: Erkennungsregeln und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Erkennungsregeln als Daten formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende Alarme nach Schwere zusammenfassen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlalarme prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abschlussprojekt planen.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Regeln | 2 |
| 8.2 | Fehlalarme | 2 |
| 8.3 | Abschlussprojekt | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regeln (Einheit 8.1):** Führen Sie `bash erkennung.sh` aus. Erklären Sie die fünf Regeln und ihre Alarme in Schritt 1.
2. **Fehlalarme (Einheit 8.2):** Erklären Sie Schritt 2 und 3: Warum lösen die Tippfehler von anna und ben keinen Alarm aus?
3. **Abschlussprojekt (Einheit 8.3):** Setzen Sie die Aufgabenliste aus Schritt 4 um und schreiben Sie einen Bericht mit offenen Punkten.

#### Kontrollfragen

1. Welche Regel meldet die Serie?
2. Wie viele Alarme entstehen?
3. Warum ist 1102 hoch eingestuft?
4. Was gehört in den Bericht?
