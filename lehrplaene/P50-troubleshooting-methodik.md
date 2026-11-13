# Lehrplan: Troubleshooting-Methodik

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen (Windows und Linux auf Anwenderebene, Grundbegriffe der Netzwerktechnik) |
| **Gesamtumfang** | 8 Module, 47 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Fehlersuche in Windows und Linux: systematisches Vorgehen, Ping, Routenverfolgung, Namensauflösung, Portprüfung, Ereignisanzeige, `Get-WinEvent`, `journalctl`; optional Python 3 für kleine Auswertehilfen |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen: Kein Aufbau von Netzwerk-, Server- oder Monitoring-Infrastruktur, keine Vertiefung von Netzwerkgrundlagen, Windows-Server-Administration, Linux-Administration oder Monitoring; hier geht es um die Methode der Fehlersuche und die Auswertung. Keine Sicherheitsvorfall-Bearbeitung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Systematisches Vorgehen bei der Fehlersuche | 1 | 5 |
| 2 | Informationen sammeln und Zeitleiste erstellen | 1 | 6 |
| 3 | Hypothesen bilden und Fehler eingrenzen | 1 | 6 |
| 4 | Werkzeuge für Netzwerkfehler | 1 | 7 |
| 5 | Protokolle und Ereignisanzeige auswerten | 1 | 7 |
| 6 | Typische Fehlerbilder in Netzwerk, Server und Client | 1 | 7 |
| 7 | Dokumentieren und mit Anwendern kommunizieren | 1 | 5 |
| 8 | Übungsfälle: Fehler suchen im Labor | 2 | 4 |
| **Gesamt** | **7 Pflichtmodule, 1 Vertiefungsmodul** | | **47** |

*Hinweis zur Priorisierung: Modul 8 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 8 voraus.* 1 UE = 45 Minuten.

### 2. Quellen und Stand

* **Microsoft Learn, `Get-WinEvent`** (<https://learn.microsoft.com/powershell/module/microsoft.powershell.diagnostics/get-winevent>) und **„Creating Get-WinEvent queries with FilterHashtable“** (<https://learn.microsoft.com/powershell/scripting/samples/creating-get-winevent-queries-with-filterhashtable>), gelesen am 13.11.2026: Schlüssel `LogName`, `ProviderName`, `ID`, `Level`, `StartTime`, `EndTime`; Level 1 Critical, 2 Error, 3 Warning, 4 Informational, 5 Verbose.
* **Microsoft Learn, `Test-NetConnection`** (<https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>), gelesen am 13.11.2026: Parameter `ComputerName`, `Port`, `CommonTCPPort`, `InformationLevel`, `TraceRoute`.
* **`journalctl` (man7.org)** (<https://man7.org/linux/man-pages/man1/journalctl.1.html>): Seite in der Suche gefunden, **nicht abgerufen und nicht geprüft**.
* **`ping`, `tracert`/`traceroute`, `nslookup`, `ipconfig`, `ip`, `ss`, `systemctl`:** Fachwissen des Verfassers, **Optionen und Ausgabeformate nicht geprüft**. Vor dem Kurs in der Hilfe des Systems nachlesen.
* **RFC 1918** (IETF, Februar 1996) für private Adressen und **RFC 2606** (IETF, Juni 1999, Datum nicht geprüft) für `example.com`; **RFC 5737** (Fachwissen, nicht abgerufen) für die Dokumentationsadressen `198.51.100.0/24` und `203.0.113.0/24`.

### 3. Labor-Setup & Rahmenbedingungen

* **Labor (nur für Modul 8 nötig):** 1× Windows-Server-VM (`SRV01`, `10.80.0.10`), 1× Linux-Server-VM (`LNX01`, `10.80.0.20`), 1× Windows-11-Client-VM (`CL01`) und ein privater Hyper-V-Switch. Die Fehler werden vorab vom Dozenten eingebaut. Laborwerte sind frei erfunden und keine Zugangsdaten.
* **Ohne Labor** sind alle Module mit den mitgelieferten, erfundenen Beispieldateien (Ereignisse, Protokoll, Testergebnisse, Routenverfolgung) lösbar. Python 3 wird nur für kleine Auswertehilfen verwendet (nur Standardbibliothek).
* **Fiktives Unternehmen:** Bergfried Metallbau GmbH (Graz), 30 Mitarbeitende, Labornetz `10.80.0.0/24`, Namen unter `lab.internal`. Alle Angaben sind frei erfunden.
* **Einschränkungen/Rückbau:** Fehler nur im Labor einbauen; nach der Übung Snapshot zurücksetzen. Keine Änderungen an Produktivsystemen.
* **Material des Dozenten:** Fehlerszenarien für Modul 8 und echte Beispielprotokolle; mitgelieferte Beispiele sind erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Systematisches Vorgehen bei der Fehlersuche
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf der Fehlersuche (Symptom erfassen, Hypothese bilden, prüfen, beheben, bestätigen, dokumentieren) in der richtigen Reihenfolge nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Störungsmeldung in Symptom, Erwartung und Ist-Zustand zerlegen und den Fehler reproduzieren oder die Nicht-Reproduzierbarkeit begründen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlersuche von Raten und Herumprobieren unterscheiden und den Grund nennen.
* **Voraussetzungen:** IT-Grundlagen.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Ablauf der Fehlersuche und typische Denkfehler | 2 |
| 1.2 | Symptom, Erwartung, Ist-Zustand; Reproduzieren | 2 |
| 1.3 | Eine Änderung nach der anderen; Rückfallweg; Abschluss prüfen | 1 |

#### Praxisaufgaben
1. **Ablauf ordnen:** Bringe sechs durcheinander geratene Schritte einer Fehlersuche in die richtige Reihenfolge und begründe zwei Plätze.
2. **Störungsmeldung zerlegen:** Zerlege drei Meldungen in Symptom, Erwartung und Ist-Zustand und formuliere je zwei Rückfragen.
3. **Reproduzieren:** Beschreibe für einen sporadischen Fehler, wie du ihn reproduzierbar machst oder die Beobachtung vorbereitest.

#### Kontrollfragen
1. Warum ist „neu starten“ keine Ursachenbehebung?
2. Was heißt „Fehler reproduzieren“?
3. Warum nur eine Änderung auf einmal?

### Modul 2: Informationen sammeln und Zeitleiste erstellen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Störung mit Zeitpunkt, Betroffenen, Fehlermeldung und letzter Änderung vollständig erfassen.
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse mehrerer Systeme zu einer gemeinsamen Zeitleiste zusammenführen und mögliche Auslöser kennzeichnen.
  * Nach Abschluss dieses Moduls kann der Lernende Hinweise von Beweisen unterscheiden und die Aussagekraft von Zeitstempeln (Zeitzone, Uhrabweichung) einschätzen.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Die richtigen Fragen: Wer, was, wann, wo, was wurde geändert? | 2 |
| 2.2 | Quellen: Anwender, Tickets, Änderungen, Protokolle | 2 |
| 2.3 | Zeitleiste erstellen und auswerten | 2 |

#### Praxisaufgaben
1. **Erfassungsbogen:** Fülle einen Erfassungsbogen für die Störung „Intranet-Seite lädt nicht“ aus der Anwendermeldung aus und markiere die offenen Punkte.
2. **Zeitleiste mit Skript:** Führe zwei Ereignisprotokolle mit `ereignisse_zeitleiste.py` zusammen und nenne die zwei auffälligsten Ereignisse vor dem Symptom.
3. **Eigene Zeitleiste:** Ergänze die Zeitleiste um zwei weitere Quellen (Anwendermeldung, Änderungsliste) und beschrifte jede Zeile mit Quelle und Sicherheit.

#### Kontrollfragen
1. Warum zuerst fragen, was geändert wurde?
2. Welche Probleme machen Zeitstempel verschiedener Systeme?
3. Wie unterscheidest du Hinweis und Beweis?

### Modul 3: Hypothesen bilden und Fehler eingrenzen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende aus Symptomen prüfbare Hypothesen ableiten und nach Wahrscheinlichkeit und Prüfaufwand ordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Verfahren von unten nach oben, von oben nach unten und Halbieren (Divide and Conquer) unterscheiden und passend wählen.
  * Nach Abschluss dieses Moduls kann der Lernende mit einer Schichtenliste (Verbindung, Adresse, Erreichbarkeit, Namensauflösung, Port und Dienst, Anwendung) einen Fehler eingrenzen und dabei Vergleich mit einem funktionierenden System nutzen.
* **Voraussetzungen:** Modul 1 und 2; Grundkenntnisse zu IP-Adressen und DNS.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Hypothesen: prüfbar formulieren und ordnen | 2 |
| 3.2 | Eingrenzungsverfahren im Vergleich | 2 |
| 3.3 | Schichtenliste anwenden: Messwerte auswerten | 2 |

#### Praxisaufgaben
1. **Hypothesen ordnen:** Leite aus dem Symptom „Intranet lädt nicht“ fünf Hypothesen ab und ordne sie nach Wahrscheinlichkeit und Prüfaufwand.
2. **Verfahren wählen:** Wähle für vier Situationen ein Eingrenzungsverfahren und begründe die Wahl.
3. **Schichtenliste auswerten:** Lies `messwerte.csv` mit `eingrenzen.py` und nenne je Fall die erste Abweichung und den nächsten Schritt.

#### Kontrollfragen
1. Was macht eine Hypothese prüfbar?
2. Wann ist Halbieren sinnvoll?
3. Warum bedeutet die erste Abweichung nicht sicher den Ort der Ursache?

### Modul 4: Werkzeuge für Netzwerkfehler
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende IP-Konfiguration eines Windows- und eines Linux-Systems prüfen und die Ausgabe lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Ping, Routenverfolgung, Namensauflösung und Portprüfung (inklusive Test-NetConnection) gezielt einsetzen und die Aussagegrenzen der Ergebnisse nennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Ausgabe einer Routenverfolgung auswerten (Hops, Zeitüberschreitung, Sprünge).
* **Voraussetzungen:** Modul 3; Grundkenntnisse zu IP, DNS und Ports.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | IP-Konfiguration prüfen (Windows und Linux) | 1 |
| 4.2 | Ping und Routenverfolgung | 2 |
| 4.3 | Namensauflösung prüfen | 1 |
| 4.4 | Ports und Dienste prüfen (Test-NetConnection) | 2 |
| 4.5 | Ergebnisse auswerten: Aussagegrenzen | 1 |

#### Praxisaufgaben
1. **IP-Konfiguration lesen:** Beschreibe für Windows und Linux, welche Angaben der IP-Konfiguration du prüfst und welche Werte im Labornetz zu erwarten sind.
2. **Routenverfolgung auswerten:** Starte `traceroute_auswertung.py` und beantworte Fragen zu den zwei Beispieldateien.
3. **Namensauflösung und Port:** Erkläre, wie du mit Ping, Namensauflösung und Test-NetConnection Fall A aus Modul 3 prüfst, und schreibe die Befehle auf.
4. **Aussagegrenzen:** Ordne zehn Aussagen als „folgt aus dem Ergebnis“ oder „folgt nicht“ ein.

#### Kontrollfragen
1. Was zeigt ein erfolgreicher Ping nicht?
2. Warum beide Richtungen prüfen, wenn nur ein Client betroffen ist?
3. Wofür dient `Test-NetConnection` mit `-Port`?
4. Wann hilft die Routenverfolgung?

### Modul 5: Protokolle und Ereignisanzeige auswerten
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende in der Ereignisanzeige Protokoll, Quelle, Ereignis-ID und Stufe unterscheiden und gezielt filtern.
  * Nach Abschluss dieses Moduls kann der Lernende mit `Get-WinEvent` und `FilterHashtable` Ereignisse nach Protokoll, Stufe und Zeitraum abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende unter Linux Dienstprotokolle mit `journalctl` lesen und Anwendungsprotokolle mit einem Skript zusammenfassen.
* **Voraussetzungen:** Modul 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Ereignisanzeige: Protokolle, Quellen, Stufen | 2 |
| 5.2 | `Get-WinEvent` mit FilterHashtable | 2 |
| 5.3 | Linux: `journalctl` und Dienstprotokolle | 1 |
| 5.4 | Anwendungsprotokolle zusammenfassen | 2 |

#### Praxisaufgaben
1. **Ereignisanzeige:** Beschreibe den Weg zu den Protokollen „System“ und „Anwendung“ und die Bedeutung der Stufen.
2. **Get-WinEvent:** Schreibe zwei Abfragen mit FilterHashtable und erkläre jeden Schlüssel.
3. **Linux-Protokoll:** Formuliere drei `journalctl`-Abfragen für den Webdienst `nginx` und kennzeichne, was du prüfen musst.
4. **Anwendungsprotokoll:** Starte `protokoll_pruefen.py` auf `app_protokoll.log` und beantworte vier Fragen.

#### Kontrollfragen
1. Wofür steht die Ereignis-ID?
2. Welche Level-Zahl hat „Error“ bei `Get-WinEvent`?
3. Warum sind Folgefehler gefährlich für die Auswertung?
4. Was prüfst du vor dem Vergleich von Zeitstempeln?

### Modul 6: Typische Fehlerbilder in Netzwerk, Server und Client
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehlerbilder im Netzwerk (Adresse, Gateway, DNS, Firewall, Switch) erkennen und der Schicht zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehlerbilder auf Servern (Dienst gestoppt, Platte voll, Zertifikat abgelaufen, falsche Berechtigung) und Clients (Profil, Konto, Zeit, Updates) erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende zu einem Fehlerbild die ersten drei Prüfschritte und eine Behebung mit Rückfallweg beschreiben.
* **Voraussetzungen:** Modul 3 bis 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Netzwerkfehler: Adresse, Gateway, DNS, Firewall | 2 |
| 6.2 | Serverfehler: Dienst, Speicher, Zertifikat, Berechtigung | 3 |
| 6.3 | Clientfehler: Konto, Profil, Zeit, Updates | 2 |

#### Praxisaufgaben
1. **Netzwerk-Fehlerbilder:** Ordne fünf Fehlerbilder einer Schicht zu und nenne den ersten Prüfschritt.
2. **Serverfehler:** Beschreibe für vier Serverfehlerbilder Symptom, Prüfschritt, Behebung und Rückfallweg.
3. **Clientfehler:** Beurteile drei Clientfälle und entscheide, welche Informationen du noch brauchst.

#### Kontrollfragen
1. Warum kann ein falsches Datum viele Fehler auslösen?
2. Was heißt Rückfallweg?
3. Welche Behebungen brauchen eine Freigabe?

### Modul 7: Dokumentieren und mit Anwendern kommunizieren
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Störungsbearbeitung nachvollziehbar dokumentieren (Symptom, Prüfschritte, Ergebnis, Ursache, Behebung).
  * Nach Abschluss dieses Moduls kann der Lernende mit Anwendern verständlich und ohne Schuldzuweisung kommunizieren, Statusmeldungen schreiben und Eskalation begründen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Lösung für die Wissensablage so aufbereiten, dass ein Kollege sie wiederverwenden kann.
* **Voraussetzungen:** Modul 1 bis 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Dokumentation während der Fehlersuche | 2 |
| 7.2 | Kommunikation mit Anwendern und Statusmeldungen | 2 |
| 7.3 | Eskalation und Wissensablage | 1 |

#### Praxisaufgaben
1. **Ticketnotiz:** Schreibe aus dem Material der Zeitleiste (Modul 2) eine Ticketnotiz in fünf Teilen.
2. **Anwender informieren:** Schreibe eine Statusmeldung und eine Abschlussmeldung für Anwender.
3. **Eskalation und Wissensablage:** Entscheide, wann du eskalierst, und schreibe einen Wissensartikel in sieben Zeilen.

#### Kontrollfragen
1. Warum notierst du Uhrzeiten bei Prüfschritten?
2. Was gehört nicht in eine Anwendermeldung?
3. Wann ist ein Wissensartikel brauchbar?

### Modul 8: Übungsfälle: Fehler suchen im Labor
* **Priorität:** 2 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen vorab eingebauten Fehler im Labor nach dem Ablauf der Module 1 bis 7 selbstständig eingrenzen und dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende den eigenen Lösungsweg mit der Musterlösung vergleichen und Abweichungen begründen.
* **Voraussetzungen:** Module 1 bis 7; Labor aus 1× Windows-Server-VM (`SRV01`), 1× Linux-Server-VM (`LNX01`), 1× Windows-11-Client-VM (`CL01`) und privatem Hyper-V-Switch (Laborvariante; ohne Labor mit den Fallbeschreibungen).

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Fall 1: Namensauflösung | 2 |
| 8.2 | Fall 2: Dienst oder Port | 2 |

#### Praxisaufgaben
1. **Fall 1: Namensauflösung:** Suche den Fehler zu „Intranet lädt nicht“ und dokumentiere deinen Weg.
2. **Fall 2: Dienst oder Port:** Entwickle selbst einen zweiten Fehlerfall und tausche ihn mit einem Kollegen.

#### Kontrollfragen
1. Woran erkennst du, dass die Suche gut war, auch wenn die Ursache spät gefunden wurde?
2. Warum tauschst du Fälle mit einem Kollegen?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P50 erstellt (Annahmen: Bergfried Metallbau GmbH, Labor nur für Modul 8, Beispieldateien erfunden). Stunden: 5+6+6+7+7+7+5+4 = 47 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 7×1, 1×2.

**Nicht bestätigt:** Alle Befehlsoptionen und Ausgabeformate außer den auf Microsoft Learn gelesenen Angaben zu `Get-WinEvent` und `Test-NetConnection`; die Schichtenliste ist ein Kurshilfsmittel, keine Norm; `journalctl`-Handbuchseite nicht abgerufen.

**Offen:** Zeitaufwand unerprobt; Labor nicht aufgebaut; der Lehrplan wurde von Matija noch nicht geprüft.
