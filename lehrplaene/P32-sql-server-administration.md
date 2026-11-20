# Lehrplan: SQL Server Administration

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); SQL-Grundlagen (Kurs „SQL-Grundlagen“) und Windows-Server-Grundlagen |
| **Gesamtumfang** | 10 Module, 108 UE (zu 45 Minuten; 81 Stunden) |
| **Fokus-Technologien** | Microsoft SQL Server (Developer- oder Evaluation-Edition) auf Windows Server; Verwaltung mit SQL Server Management Studio und T-SQL |
| **Thematische Abgrenzung (Out of Scope)** | SQL-Grundlagen (SELECT, JOIN, Datenmodell) werden vorausgesetzt und stehen im Kurs „SQL-Grundlagen“ dieses Repositories. Nicht behandelt: Datenbankentwurf, Entwicklung von Anwendungen, Reporting Services, Integration Services, Analysis Services, Azure SQL, SQL Server unter Linux, Verschlüsselungsschlüssel-Verwaltung im Detail |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Installation und Editionen | 1 | 10 |
| 2 | Instanzen, Datenbanken und Dateien | 1 | 10 |
| 3 | Anmeldungen, Benutzer und Rechte | 1 | 12 |
| 4 | Recovery-Modelle und Sicherungsarten | 1 | 12 |
| 5 | Wiederherstellung planen und üben | 1 | 14 |
| 6 | Wartungspläne: Prüfen, Indexpflege und Statistiken | 1 | 10 |
| 7 | SQL Server Agent: Aufträge, Zeitpläne und Benachrichtigungen | 1 | 10 |
| 8 | Leistungsanalyse: Wartezeiten und Blockierungen | 1 | 12 |
| 9 | Hochverfügbarkeit im Überblick | 2 | 8 |
| 10 | Sicherheit und Härtung | 1 | 10 |
| **Gesamt** | 10 Module | 9 × Priorität 1, 1 × Priorität 2 | **108** |

**Priorität 1** (Pflicht) sind die Module 1 bis 8 und 10; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 9 (Hochverfügbarkeit im Überblick). Fällt Modul 9 weg, verringert sich der Gesamtumfang auf 100 UE; kein Pflichtmodul setzt Modul 9 voraus.

### 2. Quellen

**Gelesen (Abruf 20.11.2026):** Seiten der Microsoft-Learn-Dokumentation zu den Editionen von SQL Server 2025 (Enterprise, Standard, Enterprise Developer, Standard Developer, Evaluation mit 180 Tagen, Express mit 50 GB je Datenbank in 2025 gegenüber 10 GB in 2022 und früher, 1 Sockel/4 Kerne, Pufferpool 1.410 MB; Standard 2025: 4 Sockel/32 Kerne/256 GB, 2022: 24 Kerne/128 GB; Web Edition laut Dokumentation eingestellt) und zur Reihenfolge der Wiederherstellung (Protokollfragment sichern, Vollsicherung, Differenzsicherung, Protokollsicherungen lückenlos, `STOPAT`; Berechtigungen zum Wiederherstellen: `sysadmin`, `dbcreator` oder `dbo`). Lizenz- und Editionsstand ändern sich; vor dem Einsatz die aktuelle Seite prüfen.

**Nicht gelesen:** die übrige SQL-Server-Dokumentation (Agent, Wartung, Leistungsanalyse, Hochverfügbarkeit, Sicherheit). **Es wurde kein SQL Server verwendet.** Alle Skripte sind **Python-Modelle mit erfundenen Daten**, die im Cloud-Container liefen; die `.sql`-Dateien enthalten **nicht ausgeführte** T-SQL-Beispiele aus Fachwissen. Syntax, Systemsichten, Prozedurnamen und Standardwerte außerhalb der oben genannten Punkte sind **nicht bestätigt**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-SQL`, `10.32.0.0/24`).

**VMs:** `sql01` (**erforderlich**, `10.32.0.2`): Windows Server mit SQL Server in der **Developer-** oder **Evaluation-Edition** (Evaluation: zeitlich begrenzt, laut Dokumentation 180 Tage; Developer nur für Entwicklung und Test, nicht produktiv); zusätzliche virtuelle Platten für Daten, Protokoll und Sicherungen (Größen frei wählbar, z. B. 20 GB). `win11` (**erforderlich ab Modul 2**, `10.32.0.20`): Windows 11 mit SQL Server Management Studio.

**Internetphase:** Für den Download der Installationsmedien und Updates braucht `sql01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es werden nur erfundene Beispieldaten verwendet.

**Prüfpunkt (Checkpoint):** Vor Modul 4 und vor Modul 5 von `sql01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung (Modul 4).

**Skripte:** Die Python-Skripte sind Modelle und laufen ohne Verbindung zu SQL Server (nur Python 3). Die `.sql`-Dateien sind **nicht ausgeführt**; Pfade (`D:\Daten`, `E:\Log`, `F:\Sicherung`) sind Annahmen und im Labor anzupassen.

## B. Detaillierter Modulaufbau

### Modul 1: Installation und Editionen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Editionen und ihre wichtigsten Grenzen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Edition anhand von Anforderungen auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Installation planen.
  * Nach Abschluss dieses Moduls kann der Lernende Version und Edition einer Instanz abfragen.
* **Voraussetzungen:** Windows-Server-Grundlagen; SQL-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Editionen und ihre Grenzen: Enterprise, Standard, Developer, Evaluation, Express (`editionen.py`) | 3 |
| 1.2 | Installation planen: Dienstkonten, Sortierung, Pfade, Authentifizierungsmodus (Fachwissen) | 3 |
| 1.3 | Version und Edition abfragen (`beispiel_installation.sql`) | 2 |
| 1.4 | Labor aufbauen: `sql01` mit Platten, privater Switch | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Edition wählen (Einheit 1.1):** Führen Sie `python3 editionen.py` aus und begründen Sie für jeden der vier Fälle, welche Edition Sie wählen. Prüfen Sie die Grenzen auf der aktuellen Dokumentationsseite (Stand und Quelle notieren).
2. **Installation planen (Einheit 1.2):** Legen Sie für `sql01` fest: Dienstkonto, Pfade für Daten, Protokoll und Sicherung (getrennte Platten), Authentifizierungsmodus, Sortierung. Begründen Sie jede Wahl in einem Satz (Fachwissen, nicht bestätigt).
3. **Instanz abfragen (Einheit 1.3):** Beschreiben Sie, welche Angaben `beispiel_installation.sql` liefern soll, und führen Sie es nach der Installation in SSMS aus (nicht in diesem Material geprüft).
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie `sql01` mit drei zusätzlichen virtuellen Platten und den Switch `Lab-SQL` auf und prüfen Sie mit `ping` die Verbindung zu `win11`.

#### Kontrollfragen

1. Warum ist die Developer-Edition nicht für den Produktivbetrieb erlaubt?
2. Warum ist bei Express die Grenze je Datenbank wichtig?
3. Warum werden Daten, Protokoll und Sicherung auf getrennte Platten gelegt?
4. Warum prüft man die Dokumentation zum Editionsstand vor der Auswahl?

### Modul 2: Instanzen, Datenbanken und Dateien

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Systemdatenbanken und Benutzerdatenbanken unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Daten- und Protokolldatei erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Wachstumseinstellungen vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Datenbank anlegen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Instanz, Systemdatenbanken und Benutzerdatenbanken; Daten- und Protokolldateien | 3 |
| 2.2 | Dateigrößen und Wachstum: Prozent oder feste Größe (`autogrowth.py`) | 3 |
| 2.3 | Datenbank anlegen (`beispiel_datenbank.sql`) | 2 |
| 2.4 | Zugriff aus `win11`: Verbindung mit SSMS, Port und Firewall (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dateien erklären (Einheit 2.1):** Erklären Sie, wofür die Dateien `.mdf` und `.ldf` dienen (Fachwissen) und warum sie auf getrennten Platten liegen sollen.
2. **Wachstum vergleichen (Einheit 2.2):** Führen Sie `python3 autogrowth.py` aus und vergleichen Sie 10 %, 256 MB und 1024 MB. Begründen Sie, welche Einstellung Sie wählen.
3. **Datenbank anlegen (Einheit 2.3):** Passen Sie `beispiel_datenbank.sql` an Ihre Pfade an und führen Sie es auf `sql01` aus (nicht in diesem Material geprüft).
4. **Verbindung planen (Einheit 2.4):** Beschreiben Sie, welche Angaben (Servername, Port, Anmeldung) und welche Firewall-Regel für die Verbindung von `win11` nötig sind (nicht bestätigt).

#### Kontrollfragen

1. Warum ist Prozentwachstum bei großen Dateien problematisch?
2. Wozu dient die Protokolldatei?
3. Warum legt man Dateien vorab in ausreichender Größe an?
4. Warum gehören keine Benutzerdaten in `master`?

### Modul 3: Anmeldungen, Benutzer und Rechte

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldung, Benutzer und Rolle unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Windows- und SQL-Authentifizierung vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Rechte-Übersicht auf riskante Muster prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte nach dem Prinzip der geringsten Rechte vergeben.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Anmeldung (Login), Datenbankbenutzer und Rollen; Windows- und SQL-Authentifizierung | 3 |
| 3.2 | Server- und Datenbankrollen; Prinzip der geringsten Rechte | 3 |
| 3.3 | Rechte-Übersicht prüfen (`rechte_pruefen.py`) | 3 |
| 3.4 | Anmeldung, Benutzer und Rolle anlegen (`beispiel_rechte.sql`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe abgrenzen (Einheit 3.1):** Erklären Sie an einem Beispiel den Weg von der Anmeldung über den Datenbankbenutzer zur Rolle bis zum Recht auf eine Tabelle.
2. **Rechte prüfen (Einheit 3.3):** Führen Sie `python3 rechte_pruefen.py beispiel_rechte.csv` aus und beheben Sie jeden Hinweis in einer Kopie der CSV. Prüfen Sie erneut.
3. **Rollenkonzept (Einheit 3.2):** Entwerfen Sie ein Rollenkonzept für drei Gruppen (Auswertung nur lesend, Anwendung lesen und schreiben, Datenbankverwaltung) und ordnen Sie jeder Gruppe Rollen zu.
4. **Anlegen (Einheit 3.4):** Passen Sie `beispiel_rechte.sql` an und führen Sie es auf `sql01` aus (nicht in diesem Material geprüft).

#### Kontrollfragen

1. Warum sollten Anwendungen nicht als `sysadmin` laufen?
2. Warum bevorzugt man Windows-Gruppen gegenüber einzelnen SQL-Anmeldungen?
3. Was bedeutet `db_owner` in einer Datenbank?
4. Warum sollte `sa` deaktiviert oder umbenannt werden?

### Modul 4: Recovery-Modelle und Sicherungsarten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Recovery-Modelle unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Sicherungsarten und ihre Abhängigkeiten erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Verlustzeit und Volumen einer Strategie rechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherungen anlegen und prüfen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Recovery-Modelle: SIMPLE, FULL, BULK_LOGGED (Fachwissen) | 3 |
| 4.2 | Sicherungsarten: Voll-, Differenz- und Protokollsicherung | 3 |
| 4.3 | Verlustzeit und Volumen (`recovery_modelle.py`) | 3 |
| 4.4 | Sicherungen anlegen und prüfen (`beispiel_sicherung.sql`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Modelle zuordnen (Einheit 4.1):** Ordnen Sie drei Datenbanken (Test, Kundendaten, Berichtsdatenbank mit nächtlichem Import) einem Recovery-Modell zu und begründen Sie.
2. **Strategie rechnen (Einheit 4.3):** Führen Sie `python3 recovery_modelle.py` aus und ändern Sie Datenbankgröße und Änderungsrate. Welche Strategie erfüllt „höchstens 15 Minuten Datenverlust“?
3. **Abhängigkeiten zeichnen (Einheit 4.2):** Zeichnen Sie eine Woche mit Voll-, Differenz- und Protokollsicherungen und markieren Sie, was zur Wiederherstellung von Mittwoch 12:00 nötig ist.
4. **Sicherungen anlegen (Einheit 4.4):** Passen Sie `beispiel_sicherung.sql` an und führen Sie es aus. Prüfen Sie mit `RESTORE VERIFYONLY` (nicht in diesem Material geprüft).

#### Kontrollfragen

1. Warum ist die Protokollsicherung im Modell SIMPLE nicht möglich?
2. Warum genügt `RESTORE VERIFYONLY` nicht als Nachweis der Wiederherstellbarkeit?
3. Warum gehören Sicherungen nicht auf dieselbe Platte wie die Datenbank?
4. Welche Rolle hat `CHECKSUM` bei der Sicherung?

### Modul 5: Wiederherstellung planen und üben

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Reihenfolge der Wiederherstellung nennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Plan aus einer Sicherungskette ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende Lücken in der Protokollkette erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die nötigen Berechtigungen nennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Reihenfolge der Wiederherstellung: Protokollfragment, Voll-, Differenz-, Protokollsicherungen, `STOPAT` (Microsoft Learn, Abruf 20.11.2026) | 3 |
| 5.2 | Plan aus der Sicherungskette berechnen (`restore_plan.py`) | 3 |
| 5.3 | Lücken in der Protokollkette erkennen und ihre Folgen | 3 |
| 5.4 | Wiederherstellung durchführen (`beispiel_restore.sql`); Berechtigungen | 3 |
| 5.5 | Abschlussübung: Wiederherstellungsprotokoll schreiben | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Reihenfolge erklären (Einheit 5.1):** Erklären Sie, warum zuerst das Protokollfragment gesichert wird und warum bei allen Schritten außer dem letzten `NORECOVERY` steht.
2. **Plan lesen (Einheit 5.2):** Führen Sie `python3 restore_plan.py` aus und beschreiben Sie für jedes der drei Ziele den Plan und die Warnung.
3. **Lücke bewerten (Einheit 5.3):** Beim Ziel „17.11. 20:00“ fehlt `log_003`. Beschreiben Sie, bis wann die Wiederherstellung möglich ist und was Sie tun würden.
4. **Protokoll schreiben (Einheit 5.5):** Schreiben Sie ein Wiederherstellungsprotokoll (Ziel, Zeitpunkt, Schritte, Ergebnis, Prüfung der Daten) für einen Übungslauf auf `sql01` (nicht in diesem Material geprüft).
5. **Wiederherstellung üben (Einheit 5.4):** Passen Sie `beispiel_restore.sql` an, prüfen Sie die nötigen Berechtigungen und führen Sie die Wiederherstellung in einem Übungslauf auf `sql01` aus (nicht in diesem Material geprüft).

#### Kontrollfragen

1. Wozu dient `STOPAT`?
2. Was passiert, wenn eine Protokollsicherung in der Kette fehlt?
3. Wer darf eine Datenbank wiederherstellen?
4. Warum übt man die Wiederherstellung regelmäßig?

### Modul 6: Wartungspläne: Prüfen, Indexpflege und Statistiken

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Wartungsaufgaben und ihren Zweck nennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Wartungsfenster planen.
  * Nach Abschluss dieses Moduls kann der Lernende Überschneidungen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wartung überwachen.
* **Voraussetzungen:** Module 4 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Wartungsaufgaben: Konsistenzprüfung, Indexpflege, Statistiken, Sicherungen | 3 |
| 6.2 | Wartungsfenster planen und Überschneidungen finden (`wartungsfenster.py`) | 3 |
| 6.3 | Aufgaben als T-SQL (`beispiel_wartung.sql`) | 2 |
| 6.4 | Überwachung der Wartung: Dauer, Fehler, Platz | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufgaben erklären (Einheit 6.1):** Erklären Sie in je einem Satz Zweck von Konsistenzprüfung, Indexpflege und Statistik-Aktualisierung (Fachwissen).
2. **Plan prüfen (Einheit 6.2):** Führen Sie `python3 wartungsfenster.py` aus und beheben Sie die Überschneidungen durch geänderte Startzeiten. Passt das Ergebnis ins Fenster?
3. **T-SQL lesen (Einheit 6.3):** Erklären Sie die drei Anweisungen in `beispiel_wartung.sql` und nennen Sie Risiken (Last, Sperren).
4. **Überwachung planen (Einheit 6.4):** Legen Sie fest, wie Sie Fehler der Wartung bemerken (Benachrichtigung, Protokoll, Zuständiger).

#### Kontrollfragen

1. Warum läuft die Konsistenzprüfung nicht gleichzeitig mit der Vollsicherung?
2. Warum sind Statistiken für Abfragepläne wichtig?
3. Warum darf die Protokollsicherung während der Wartung nicht ausfallen?
4. Was geschieht, wenn das Wartungsfenster überschritten wird?

### Modul 7: SQL Server Agent: Aufträge, Zeitpläne und Benachrichtigungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Auftrag, Schritt, Zeitplan und Operator unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende nächste Ausführungen berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende fehlende Benachrichtigungen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Auftrag anlegen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Aufgaben des Agents: Aufträge, Schritte, Zeitpläne, Operatoren | 3 |
| 7.2 | Aufträge und nächste Ausführungen berechnen (`agent_jobs.py`) | 3 |
| 7.3 | Auftrag als T-SQL anlegen (`beispiel_agent.sql`) | 2 |
| 7.4 | Benachrichtigung bei Fehlern und Verlauf lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe zuordnen (Einheit 7.1):** Zeichnen Sie Auftrag, Schritte, Zeitplan und Operator in einem Bild und beschriften Sie.
2. **Aufträge auswerten (Einheit 7.2):** Führen Sie `python3 agent_jobs.py beispiel_jobs.csv` aus und erklären Sie die nächsten Läufe und Hinweise.
3. **Auftrag anlegen (Einheit 7.3):** Erklären Sie die Aufrufe in `beispiel_agent.sql` und legen Sie den Auftrag auf `sql01` an (nicht in diesem Material geprüft).
4. **Benachrichtigung (Einheit 7.4):** Legen Sie fest, wer bei einem Fehler des Auftrags „Protokollsicherung“ benachrichtigt wird und wie die Benachrichtigung versendet wird (nicht bestätigt).

#### Kontrollfragen

1. Warum braucht jeder wichtige Auftrag eine Benachrichtigung bei Fehlern?
2. Was ist ein Operator?
3. Warum wird ein deaktivierter Auftrag trotzdem aufgelistet?
4. Warum sollten Aufträge unter einem Konto mit minimalen Rechten laufen?

### Modul 8: Leistungsanalyse: Wartezeiten und Blockierungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein systematisches Vorgehen zur Leistungsanalyse beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Wartezeiten nach Anteil auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Blockierungen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen ableiten und prüfen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Vorgehen: Symptom, Messung, Ursache, Maßnahme | 3 |
| 8.2 | Wartezeiten auswerten (`wartezeiten.py`) | 3 |
| 8.3 | Blockierungen und Sitzungen erkennen (`beispiel_leistung.sql`) | 3 |
| 8.4 | Maßnahmen und Messung danach | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorgehen beschreiben (Einheit 8.1):** Beschreiben Sie in fünf Schritten, wie Sie bei der Meldung „die Anwendung ist langsam“ vorgehen.
2. **Wartezeiten auswerten (Einheit 8.2):** Führen Sie `python3 wartezeiten.py beispiel_waits.csv` aus und beschreiben Sie, welche zwei Wait-Typen den größten Anteil haben und welche Ursachen sie nahelegen.
3. **Blockierung erkennen (Einheit 8.3):** Erklären Sie die zweite Abfrage in `beispiel_leistung.sql` und was ein Wert in `blocking_session_id` bedeutet (nicht ausgeführt).
4. **Maßnahmen ableiten (Einheit 8.4):** Leiten Sie zwei Maßnahmen für die Beispieldaten ab und beschreiben Sie, wie Sie deren Wirkung messen.

#### Kontrollfragen

1. Warum zeigen Wait-Statistiken nur Symptome?
2. Warum werden Hintergrund-Waits ausgeschlossen?
3. Was kann eine Blockierung auslösen?
4. Warum misst man vor und nach einer Änderung?

### Modul 9: Hochverfügbarkeit im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Verfügbarkeit in Ausfallzeit umrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Verfahren und ihre Wirkung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende ein Verfahren nach Anforderung auswählen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Verfügbarkeit und Ausfallzeit: Prozentwerte in Stunden umrechnen (`verfuegbarkeit.py`) | 3 |
| 9.2 | Verfahren im Überblick: Log Shipping, Failover-Cluster-Instanz, Verfügbarkeitsgruppe | 3 |
| 9.3 | Auswahl nach Anforderung und Kosten | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ausfallzeit rechnen (Einheit 9.1):** Rechnen Sie 99,9 % und 99,99 % in Ausfallminuten pro Jahr um und prüfen Sie mit `python3 verfuegbarkeit.py`.
2. **Abhängigkeit rechnen (Einheit 9.1):** Berechnen Sie die Gesamtverfügbarkeit von Server, Speicher und Netzwerk (je 99,9 %) und vergleichen Sie mit dem Ergebnis des Skripts.
3. **Verfahren zuordnen (Einheit 9.2):** Ordnen Sie drei Anforderungen („Umschaltung in Minuten“, „zweiter Standort“, „einfach und günstig“) einem Verfahren zu (Fachwissen, nicht bestätigt).
4. **Entscheidung (Einheit 9.3):** Begründen Sie für `sql01` in fünf Sätzen, ob Hochverfügbarkeit nötig ist.

#### Kontrollfragen

1. Warum ist Hochverfügbarkeit kein Ersatz für Sicherungen?
2. Warum sinkt die Gesamtverfügbarkeit bei in Reihe geschalteten Komponenten?
3. Was unterscheidet Log Shipping von einer Verfügbarkeitsgruppe?
4. Warum sollte der Bedarf an Verfügbarkeit mit dem Fachbereich geklärt werden?

### Modul 10: Sicherheit und Härtung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die wichtigsten Angriffsflächen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Checkliste auswerten und priorisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende einen Maßnahmenplan schreiben.
* **Voraussetzungen:** Module 3 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Angriffsfläche: Konten, Netzwerk, Verschlüsselung, Aktualisierungen | 3 |
| 10.2 | Checkliste auswerten (`sicherheit_pruefen.py`) | 3 |
| 10.3 | Maßnahmen als T-SQL (`beispiel_sicherheit.sql`) | 2 |
| 10.4 | Abschlussübung: Maßnahmenplan für `sql01` | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Angriffsflächen nennen (Einheit 10.1):** Nennen Sie sechs Angriffsflächen eines SQL Servers und je eine Maßnahme (Fachwissen).
2. **Checkliste auswerten (Einheit 10.2):** Führen Sie `python3 sicherheit_pruefen.py beispiel_stand.csv` aus und sortieren Sie die offenen Punkte nach Risiko.
3. **Maßnahme beschreiben (Einheit 10.3):** Beschreiben Sie, was die Anweisungen in `beispiel_sicherheit.sql` bewirken würden (nicht ausgeführt).
4. **Maßnahmenplan (Einheit 10.4):** Schreiben Sie einen Plan für die offenen Punkte mit Reihenfolge, Aufwand, Risiko und Prüfung.

#### Kontrollfragen

1. Warum sollte die Verbindung zum Server verschlüsselt sein?
2. Warum ist die Verschlüsselung der Sicherungen wichtig?
3. Warum begrenzt man Rechte des Dienstkontos?
4. Warum ist ein „unbekannt“ in der Checkliste ein offener Punkt?
