# Lehrplan: MariaDB und PostgreSQL Administration

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Terminal, Dateien, Benutzer); SQL-Grundlagen (Kurs „SQL-Grundlagen“) |
| **Gesamtumfang** | 10 Module, 108 UE (zu 45 Minuten; 81 Stunden) |
| **Fokus-Technologien** | MariaDB und PostgreSQL auf Debian/Ubuntu (Pakete der Distribution); Verwaltung mit den Kommandozeilenprogrammen (`mariadb`, `psql`, `mariadb-dump`, `pg_dump`, `mariabackup`, `pg_basebackup`) |
| **Thematische Abgrenzung (Out of Scope)** | SQL-Grundlagen (SELECT, JOIN, Datenmodell) werden vorausgesetzt und stehen im Kurs „SQL-Grundlagen“ dieses Repositories; die Administration von Microsoft SQL Server steht im Kurs „SQL Server Administration“. Nicht behandelt: Datenbankentwurf, Anwendungsentwicklung, Galera-Cluster und Patroni im Detail, logische Replikation, Partitionierung, Erweiterungen wie PostGIS, Cloud-Datenbankdienste, andere Datenbanksysteme (z. B. MySQL, SQLite, MongoDB) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Installation und Aufbau | 1 | 10 |
| 2 | Konfiguration | 1 | 10 |
| 3 | Benutzer und Rechte | 1 | 12 |
| 4 | Speicher und Wartung | 1 | 10 |
| 5 | Sicherung und Wiederherstellung | 1 | 14 |
| 6 | Leistungsanalyse | 1 | 10 |
| 7 | Sicherheit: Zugriffskontrolle und TLS | 1 | 12 |
| 8 | Replikation in Grundzügen | 2 | 12 |
| 9 | Updates | 1 | 8 |
| 10 | Überwachung | 1 | 10 |
| **Gesamt** | 10 Module | 9 × Priorität 1, 1 × Priorität 2 | **108** |

**Priorität 1** (Pflicht) sind die Module 1 bis 7, 9 und 10; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 8 (Replikation in Grundzügen). Fällt Modul 8 weg, verringert sich der Gesamtumfang auf 96 UE; kein Pflichtmodul setzt Modul 8 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von MariaDB und PostgreSQL (Referenzhandbücher, Release-Hinweise, Support-Zeiträume der Versionen) wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch die Läufe im Labor bestätigt; verbindlich ist die Dokumentation der installierten Version. Zahlen (Datenmengen, Durchsatz, Verbindungen) sind Annahmen oder erfundene Beispieldaten.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container, ohne systemd):** MariaDB 10.11.14 (`mariadbd`, `mariabackup`, `mariadb-dump`), PostgreSQL 16.15, Python 3. Die MariaDB-Instanzen wurden direkt mit `mariadbd` gestartet, die PostgreSQL-Cluster mit `pg_createcluster` und `pg_ctlcluster`. Die Unterschiede zu Debian oder Ubuntu mit systemd (Dienstverwaltung mit `systemctl`, andere Versionen, Standard-Zeichensatz) wurden **nicht** getestet. Alle Namen, Kennwörter und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-DB`, `10.31.0.0/24`).

**VMs:** `db01` (**erforderlich**, `10.31.0.2`): Linux-Server (Debian oder Ubuntu Server) mit MariaDB und PostgreSQL; eine zusätzliche virtuelle Platte für Sicherungen (z. B. 10 GB). `db02` (**erforderlich ab Modul 8**, `10.31.0.3`): zweiter Linux-Server als Replikat. `client01` (**erforderlich ab Modul 3**, `10.31.0.20`): Linux-Client mit `mariadb`- und `psql`-Client.

**Internetphase:** Für die Installation der Pakete braucht jede VM vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es werden nur erfundene Beispieldaten verwendet.

**Prüfpunkt (Checkpoint):** Vor Modul 5 und vor Modul 9 von `db01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung (Modul 5).

**Skripte:** Die Skripte laufen im Test-Container mit Instanzen unter `/tmp/p31` (Ports 3311/3312 und 5441/5442) und binden `lab.sh` ein. Im Hyper-V-Labor verwenden Sie stattdessen die Dienste der Pakete (`systemctl`) und die Standardpfade.

## B. Detaillierter Modulaufbau

### Modul 1: Installation und Aufbau

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Pakete, Programme und Standardpfade beider Systeme nennen.
  * Nach Abschluss dieses Moduls kann der Lernende das Prozessmodell von MariaDB (ein Prozess mit Threads) und PostgreSQL (Hauptprozess mit Hilfsprozessen) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Version, Datenverzeichnis, Port und Zeichensatz abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Installation für `db01` planen.
* **Voraussetzungen:** Linux-Grundlagen; SQL-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Pakete, Programme und Standardpfade unter Debian/Ubuntu; Prozessmodell beider Systeme (`installation.sh`) | 3 |
| 1.2 | Versionen, Datenverzeichnis, Port und Zeichensatz abfragen (`abfragen.sh`) | 3 |
| 1.3 | Dienste und Cluster verwalten: `systemctl` (MariaDB) und `pg_lsclusters` (PostgreSQL) im Überblick (Fachwissen) | 2 |
| 1.4 | Labor aufbauen: `db01`, privater Switch | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Pakete und Pfade erkunden (Einheit 1.1):** Führen Sie `bash installation.sh` im Testlabor aus (oder prüfen Sie auf `db01` mit `dpkg -l` und `ls`) und tragen Sie für beide Systeme Programme, Konfigurationsdateien und Datenverzeichnis in eine Tabelle ein.
2. **Prozessmodelle vergleichen (Einheit 1.1):** Beschreiben Sie anhand von Abschnitt 5 und 6 der Ausgabe, wie sich ein MariaDB-Prozess und ein PostgreSQL-Cluster im Prozessbaum unterscheiden und was das für Überwachung und Fehlersuche bedeutet.
3. **Instanz abfragen (Einheit 1.2):** Führen Sie `bash abfragen.sh` aus und erklären Sie jede Zeile der Ausgabe. Warum zeigt MariaDB hier `latin1` und PostgreSQL `SQL_ASCII`? Prüfen Sie auf `db01`, was die Pakete tatsächlich einstellen.
4. **Dienste verwalten (Einheit 1.3):** Schreiben Sie auf, mit welchen Befehlen Sie auf `db01` Dienste starten, stoppen und Statusmeldungen lesen (nicht in diesem Material geprüft; Fachwissen) und welche Protokolle Sie bei einem Startfehler ansehen.
5. **Labor aufbauen (Einheit 1.4):** Bauen Sie `db01` mit einer zusätzlichen Platte und dem Switch `Lab-DB` auf, installieren Sie beide Systeme aus den Paketquellen und prüfen Sie mit `ping` die Verbindung zu `client01`.

#### Kontrollfragen

1. Warum läuft PostgreSQL mit mehreren Prozessen, MariaDB dagegen als ein Prozess mit vielen Threads?
2. Wozu dient `pg_lsclusters` und warum gibt es unter Debian mehrere Cluster nebeneinander?
3. Warum ist der Standard-Zeichensatz bei der Einrichtung wichtig und später schwer zu ändern?
4. Warum lauschen beide Dienste standardmäßig nur auf 127.0.0.1 bzw. localhost?

### Modul 2: Konfiguration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Konfigurationsdateien beider Systeme und ihre Reihenfolge nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungen dauerhaft und im laufenden Betrieb vornehmen und unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende mit `pg_settings` Herkunft und Neustartbedarf eines Parameters prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Konfigurationsdatei auf riskante Werte prüfen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | MariaDB: Konfigurationsdateien, Startoptionen, `SET GLOBAL` und Dauerhaftigkeit (`konfiguration.sh`) | 3 |
| 2.2 | PostgreSQL: `postgresql.conf`, `ALTER SYSTEM`, `pg_settings`, `reload` und Neustart (`konfiguration.sh`) | 3 |
| 2.3 | Wichtige Parameter: Speicher und Verbindungen (Fachwissen, nicht bestätigt) | 2 |
| 2.4 | Konfiguration prüfen (`konfig_pruefen.py`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dauerhaft oder nur zur Laufzeit (Einheit 2.1):** Führen Sie `bash konfiguration.sh` aus. Erklären Sie für MariaDB, warum `SET GLOBAL max_connections` den Neustart nicht überlebt, und wie Sie den Wert dauerhaft setzen.
2. **Neustart oder Reload (Einheit 2.2):** Erklären Sie anhand von Abschnitt 5 der Ausgabe, warum `work_mem` nach `pg_reload_conf()` gilt, `max_connections` dagegen nicht, und was `pending_restart` anzeigt.
3. **Parameter bewerten (Einheit 2.3):** Wählen Sie je System vier Parameter für Speicher und Verbindungen aus (z. B. `innodb_buffer_pool_size`, `shared_buffers`, `work_mem`) und beschreiben Sie, was ein zu kleiner und ein zu großer Wert bewirkt (nicht bestätigt, Dokumentation lesen).
4. **Konfiguration prüfen (Einheit 2.4):** Führen Sie `python3 konfig_pruefen.py beispiel_mariadb.cnf` und `python3 konfig_pruefen.py beispiel_postgresql.conf` aus, beheben Sie jeden Hinweis in einer Kopie der Datei und prüfen Sie erneut (Rückgabecode 0).

#### Kontrollfragen

1. Wo steht, in welcher Datei ein Parameter in PostgreSQL gesetzt wurde?
2. Warum sollte man `ALTER SYSTEM` und manuelle Änderungen an `postgresql.conf` nicht beliebig mischen?
3. Was bedeutet es, wenn `pending_restart` den Wert `t` hat?
4. Warum ist `SET GLOBAL` für Tests praktisch, für den Betrieb aber nicht ausreichend?

### Modul 3: Benutzer und Rechte

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Konten und Rollen in MariaDB und PostgreSQL unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte nach dem Prinzip der geringsten Rechte vergeben.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte anzeigen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende riskante Konten (Host `%`, ohne Kennwort, Superuser) finden.
* **Voraussetzungen:** Modul 2; SQL-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | MariaDB: Konten (Name@Host), Rollen und Rechte (`rechte_mariadb.sh`) | 3 |
| 3.2 | PostgreSQL: Rollen, Schemas, GRANT, `pg_hba.conf` und das Schema `public` (`rechte_postgres.sh`) | 3 |
| 3.3 | Riskante Konten finden (`rechte_bericht.sh`) | 3 |
| 3.4 | Rollenkonzept entwerfen: Auswertung, Anwendung, Verwaltung (Fachwissen) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **MariaDB-Rechte nachvollziehen (Einheit 3.1):** Führen Sie `bash rechte_mariadb.sh` aus. Erklären Sie, warum `anna` lesen, aber nicht schreiben darf, und was die Meldung `localhost` statt `127.0.0.1` bedeutet.
2. **PostgreSQL-Rechte nachvollziehen (Einheit 3.2):** Führen Sie `bash rechte_postgres.sh` aus. Erklären Sie die Fehlermeldungen in Abschnitt 2 und 3 und lesen Sie die Ausgabe von `\dp` Zeile für Zeile.
3. **Bericht auswerten (Einheit 3.3):** Führen Sie `bash rechte_bericht.sh` aus, listen Sie alle riskanten Konten beider Systeme auf und schreiben Sie je Konto, wie Sie es beheben (Kennwort, Host einschränken, Rechte entziehen).
4. **Rollenkonzept (Einheit 3.4):** Entwerfen Sie ein Rollenkonzept für drei Gruppen (Auswertung nur lesend, Anwendung lesen und schreiben, Verwaltung) für beide Systeme und beschreiben Sie, wie Sie es mit `GRANT` umsetzen.

#### Kontrollfragen

1. Warum sind Rollen besser als Einzelrechte je Benutzer?
2. Was bedeutet in MariaDB ein Konto mit dem Host `%`?
3. Warum darf ein normaler Benutzer in PostgreSQL ab Version 15 im Schema `public` keine Tabellen mehr anlegen?
4. Warum soll die Anwendung nicht mit dem Administratorkonto arbeiten?

### Modul 4: Speicher und Wartung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum nach `DELETE` der Platz nicht sofort frei wird.
  * Nach Abschluss dieses Moduls kann der Lernende in MariaDB `ANALYZE` und `OPTIMIZE` einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende in PostgreSQL `VACUUM`, `VACUUM FULL` und Autovacuum unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Größen von Datenbanken, Tabellen und Indizes ermitteln.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | MariaDB/InnoDB: Dateien, Größen, freier Platz, `ANALYZE` und `OPTIMIZE` (`wartung_mariadb.sh`) | 3 |
| 4.2 | PostgreSQL: MVCC, tote Zeilen, `VACUUM`, `VACUUM FULL`, Autovacuum (`wartung_postgres.sh`) | 4 |
| 4.3 | Größenübersicht erstellen (`groessen.sh`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Platz nach dem Löschen (Einheit 4.1):** Führen Sie `bash wartung_mariadb.sh` aus und erklären Sie, warum `data_length` und die Datei `posten.ibd` nach dem Löschen von 80 % der Zeilen gleich groß bleiben und was `OPTIMIZE TABLE` ändert.
2. **Tote Zeilen (Einheit 4.2):** Führen Sie `bash wartung_postgres.sh` aus. Erklären Sie die Spalten `lebend` und `tot` in jedem Schritt und warum nur `VACUUM FULL` die Datei verkleinert, obwohl `VACUUM` den Platz wiederverwendbar macht.
3. **Autovacuum bewerten (Einheit 4.2):** Lesen Sie die Autovacuum-Einstellungen aus Abschnitt 5 und berechnen Sie, ab wie vielen toten Zeilen Autovacuum eine Tabelle mit 100000 Zeilen bearbeitet (Schwelle + Faktor × Zeilenzahl).
4. **Größenübersicht (Einheit 4.3):** Führen Sie `bash groessen.sh` aus und erstellen Sie eine Übersicht je Tabelle (Daten, Index, Gesamt) für beide Systeme. Wo liegt der Unterschied bei den Größenangaben?

#### Kontrollfragen

1. Warum ist `VACUUM FULL` im Betrieb heikel?
2. Warum reicht in MariaDB `DELETE` nicht, um Plattenplatz zurückzugeben?
3. Wozu dient `ANALYZE` für den Abfrageplaner?
4. Warum schaltet man Autovacuum normalerweise nicht ab?

### Modul 5: Sicherung und Wiederherstellung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende logische und physische Sicherungen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherungen mit den Programmen beider Systeme anlegen und wiederherstellen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Wiederherstellung bis kurz vor einen Fehler (Point-in-Time) durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Sicherungsplan anhand von RPO und RTO bewerten.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Logische Sicherung: `mariadb-dump` und `pg_dump`/`pg_restore` (`sicherung_logisch.sh`) | 4 |
| 5.2 | Physische Sicherung: `mariabackup` und `pg_basebackup` (`sicherung_physisch.sh`) | 4 |
| 5.3 | Wiederherstellung bis zu einem Zeitpunkt: Binärprotokoll und WAL-Archiv (`pitr_mariadb.sh`, `pitr_postgres.sh`) | 4 |
| 5.4 | Sicherungsplan: RPO und RTO (`sicherungsplan.py`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Logische Sicherung (Einheit 5.1):** Führen Sie `bash sicherung_logisch.sh` aus. Erklären Sie die Rolle von `--single-transaction` und die Unterschiede zwischen SQL-Datei und Custom-Format (`-Fc`) bei der Wiederherstellung einzelner Tabellen.
2. **Physische Sicherung (Einheit 5.2):** Führen Sie `bash sicherung_physisch.sh` aus. Beschreiben Sie die drei Schritte `--backup`, `--prepare`, `--copy-back` und die Wiederherstellung bei PostgreSQL. Warum muss der Dienst für das Zurückkopieren angehalten sein?
3. **Point-in-Time (Einheit 5.3):** Führen Sie `bash pitr_mariadb.sh` und `bash pitr_postgres.sh` aus. Beschreiben Sie für beide Systeme, was die Grundlage der Wiederherstellung ist (Binärprotokoll bzw. WAL-Archiv) und wie der Zeitpunkt festgelegt wird.
4. **Sicherungsplan bewerten (Einheit 5.4):** Führen Sie `python3 sicherungsplan.py` aus, ändern Sie die Annahmen (Datenmenge, Durchsatz) und entscheiden Sie, welche Variante für die Ziele „höchstens 15 Minuten Datenverlust, höchstens 2 Stunden Ausfall“ geeignet ist.

#### Kontrollfragen

1. Warum ist eine Sicherung ohne getestete Wiederherstellung unsicher?
2. Wann ist eine logische Sicherung, wann eine physische vorzuziehen?
3. Warum braucht eine Wiederherstellung bis zu einem Zeitpunkt zusätzlich zur Vollsicherung die Protokolle?
4. Warum gehört die Sicherung auf ein anderes System als die Datenbank?

### Modul 6: Leistungsanalyse

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende langsame Abfragen finden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Ausführungsplan mit `EXPLAIN` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende durch einen Index eine Abfrage beschleunigen und das belegen.
  * Nach Abschluss dieses Moduls kann der Lernende die Cache-Trefferquote beider Systeme berechnen und einordnen.
* **Voraussetzungen:** Modul 4; SQL-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | MariaDB: Slow-Query-Log, `EXPLAIN`, Index (`analyse_mariadb.sh`) | 4 |
| 6.2 | PostgreSQL: `EXPLAIN (ANALYZE)`, Index, `pg_stat_statements` (`analyse_postgres.sh`) | 4 |
| 6.3 | Cache-Trefferquote lesen und bewerten (`cache_trefferquote.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **MariaDB analysieren (Einheit 6.1):** Führen Sie `bash analyse_mariadb.sh` aus. Vergleichen Sie `type`, `key` und `rows` vor und nach dem Index und finden Sie die Abfrage im Slow-Query-Log.
2. **PostgreSQL analysieren (Einheit 6.2):** Führen Sie `bash analyse_postgres.sh` aus. Vergleichen Sie die Pläne vor und nach dem Index (Seq Scan, Bitmap Index Scan) und lesen Sie `pg_stat_statements`.
3. **Trefferquote bewerten (Einheit 6.3):** Führen Sie `bash cache_trefferquote.sh` aus, berechnen Sie die Trefferquote von Hand nach und beschreiben Sie, warum ein fester Zielwert ohne Kenntnis der Anwendung nicht sinnvoll ist.

#### Kontrollfragen

1. Warum kann ein Index Schreibvorgänge verlangsamen?
2. Was bedeutet `type=ALL` bei MariaDB und `Seq Scan` bei PostgreSQL?
3. Warum sind die Schätzwerte im Plan (`rows`) wichtig und woher kommen sie?
4. Warum misst man vor und nach einer Änderung?

### Modul 7: Sicherheit: Zugriffskontrolle und TLS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende festlegen, wer sich von wo mit welcher Methode anmelden darf.
  * Nach Abschluss dieses Moduls kann der Lernende zu offene Regeln erkennen und entschärfen.
  * Nach Abschluss dieses Moduls kann der Lernende TLS in beiden Systemen einrichten und die Nutzung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine kleine Sicherheitsprüfung durchführen und auswerten.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Zugriffskontrolle: Lauschadressen, `pg_hba.conf`, Anmeldemethoden (`zugriff.sh`) | 4 |
| 7.2 | TLS: Testzertifikat, TLS in MariaDB und PostgreSQL, TLS erzwingen (`tls.sh`) | 4 |
| 7.3 | Sicherheitsprüfung durchführen (`sicherheit_pruefen.sh`) | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zugriff begrenzen (Einheit 7.1):** Führen Sie `bash zugriff.sh` aus. Erklären Sie, wer sich in Abschnitt 3 mit welcher Methode anmelden darf, und warum die `trust`-Regel für `0.0.0.0/0` in Abschnitt 4 gefährlich ist.
2. **TLS einrichten (Einheit 7.2):** Führen Sie `bash tls.sh` aus. Beschreiben Sie, wie TLS in beiden Systemen eingeschaltet und erzwungen wird, und warum das selbstsignierte Zertifikat nur für Tests taugt.
3. **Prüfung auswerten (Einheit 7.3):** Führen Sie `bash sicherheit_pruefen.sh` aus, erstellen Sie eine Maßnahmenliste (je Warnung: Ursache, Maßnahme, Priorität) und beheben Sie die Warnungen in der Testinstanz.

#### Kontrollfragen

1. Warum reicht ein starkes Kennwort ohne TLS nicht aus?
2. Was passiert, wenn in `pg_hba.conf` eine zu offene Regel vor einer strengen steht?
3. Warum darf die private Schlüsseldatei nur für den Dienst lesbar sein?
4. Warum ist ein Konto ohne Kennwort ein Risiko, auch wenn der Dienst nur lokal lauscht?

### Modul 8: Replikation in Grundzügen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende asynchrone und synchrone Replikation unterscheiden und die Folgen für den Datenverlust nennen.
  * Nach Abschluss dieses Moduls kann der Lernende in MariaDB ein Replikat mit GTID einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende in PostgreSQL einen Standby mit `pg_basebackup` und Slot einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende ein Replikat zum neuen Primär machen und die Risiken (Split-Brain) benennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Konzept: asynchron und synchron, Verzögerung, Datenverlust (`replikation_modell.py`) | 3 |
| 8.2 | MariaDB: Primär und Replikat mit GTID (`repl_mariadb.sh`) | 3 |
| 8.3 | PostgreSQL: Streaming-Replikation mit Slot (`repl_postgres.sh`) | 3 |
| 8.4 | Umschalten auf das Replikat (`umschalten.sh`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verlust im Modell (Einheit 8.1):** Führen Sie `python3 replikation_modell.py` aus und erklären Sie, warum bei asynchroner Replikation bestätigte Transaktionen verloren gehen können und was synchrone Replikation dafür kostet.
2. **MariaDB-Replikat (Einheit 8.2):** Führen Sie `bash repl_mariadb.sh` aus. Erklären Sie `master_use_gtid=slave_pos`, die Anzeige von `show slave status` und das Verhalten in Abschnitt 5 (Replikat gestoppt).
3. **PostgreSQL-Standby (Einheit 8.3):** Führen Sie `bash repl_postgres.sh` aus. Erklären Sie die Rolle von `-R`, `standby.signal`, dem Slot und `pg_stat_replication`.
4. **Umschalten (Einheit 8.4):** Führen Sie `bash umschalten.sh` aus. Beschreiben Sie je System die Schritte zum Umschalten und was mit Anwendungen und dem alten Primär geschehen muss.

#### Kontrollfragen

1. Warum ist ein Replikat keine Datensicherung?
2. Wozu dient ein Replikationsslot und welches Risiko entsteht bei einem dauerhaft getrennten Standby?
3. Was ist Split-Brain?
4. Warum kann man auf einem Replikat lesen, aber nicht schreiben?

### Modul 9: Updates

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Minor- und Major-Updates beider Systeme unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Update-Ablauf mit Sicherung und Rückfallplan planen.
  * Nach Abschluss dieses Moduls kann der Lernende `mariadb-upgrade` einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Wechsel per Dump und Restore durchführen und nachbereiten.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Minor- und Major-Updates unterscheiden (`update_planer.py`) | 3 |
| 9.2 | Nach dem Update prüfen: `mariadb-upgrade`; PostgreSQL-Wechsel per Dump und Restore (`update_pruefung.sh`) | 3 |
| 9.3 | Update-Ablauf und Rückfallplan schreiben (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Updates einordnen (Einheit 9.1):** Führen Sie `python3 update_planer.py` aus und ordnen Sie fünf eigene Versionspaare ein. Prüfen Sie die Regeln in der Dokumentation der Hersteller (nicht bestätigt) und notieren Sie die Quelle.
2. **Nachbereitung (Einheit 9.2):** Führen Sie `bash update_pruefung.sh` aus. Erklären Sie, was `mariadb-upgrade` prüft, und warum nach einem Dump/Restore in PostgreSQL `ANALYZE` nötig ist.
3. **Ablauf schreiben (Einheit 9.3):** Schreiben Sie für `db01` einen Update-Ablauf mit Sicherung, Prüfpunkt, Update, Prüfung und Rückfallplan (nicht in diesem Material getestet).

#### Kontrollfragen

1. Warum werden Minor-Updates (Fehlerbehebungen) zeitnah, Major-Updates aber geplant eingespielt?
2. Wozu dient ein Rückfallplan und was gehört dazu?
3. Warum testet man ein Major-Update zuerst an einer Kopie?
4. Warum sind Prüfpunkte der VM kein Ersatz für eine Datensicherung?

### Modul 10: Überwachung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende wichtige Kennzahlen beider Systeme abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende Blockierungen und lange Abfragen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler im Protokoll finden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Plugin mit Schwellwerten und Rückgabecodes (0, 1, 2, 3) auswerten.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | MariaDB: Statusvariablen, Prozessliste, Fehlerprotokoll (`ueberwachung_mariadb.sh`) | 3 |
| 10.2 | PostgreSQL: `pg_stat_activity`, Sperren, Statistik, Protokoll (`ueberwachung_postgres.sh`) | 3 |
| 10.3 | Ein Überwachungs-Plugin mit Schwellwerten und Rückgabecodes (`check_datenbank.py`) | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **MariaDB überwachen (Einheit 10.1):** Führen Sie `bash ueberwachung_mariadb.sh` aus. Erklären Sie `Threads_connected`, `Max_used_connections`, `Aborted_connects` und `Slow_queries` und nennen Sie je einen Schwellwert-Vorschlag (Begründung nennen).
2. **PostgreSQL überwachen (Einheit 10.2):** Führen Sie `bash ueberwachung_postgres.sh` aus. Erklären Sie, wie Sie in `pg_stat_activity` eine blockierte Abfrage und ihren Blockierer finden.
3. **Plugin einsetzen (Einheit 10.3):** Führen Sie `bash lauf.sh` aus. Erklären Sie die Rückgabecodes und die Ausgabe nach dem Strich (Leistungsdaten), und erweitern Sie das Plugin um eine zweite Prüfung (z. B. Verzögerung eines Replikats oder Dateisystemauslastung).

#### Kontrollfragen

1. Warum sind Rückgabecodes für Überwachungssysteme wichtiger als Text?
2. Warum genügt „Dienst läuft“ als Prüfung nicht?
3. Warum sind Trends oft aussagekräftiger als einzelne Werte?
4. Wo finden Sie in beiden Systemen Anmeldefehler?
