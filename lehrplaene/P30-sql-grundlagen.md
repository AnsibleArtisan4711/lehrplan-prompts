# Lehrplan: SQL-Grundlagen

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen, grundlegende Linux-Kommandozeilen-Kenntnisse (Dateien bearbeiten, `sudo`, Dienste neu starten) |
| **Gesamtumfang** | 12 Module, 120 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | SQL (ANSI-Grundlagen), PostgreSQL 15, DBeaver |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen (z. B. Linux-Administration); Verweise auf vorhandene Lehrpläne nur kurz. Administration von High-Availability-Clustern oder Replikation ist nicht Teil dieses Grundlagenkurses. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Relationale Modelle & Normalisierung | 1 | 10 |
| 2 | Installation & Labor-Aufbau (PostgreSQL) | 1 | 10 |
| 3 | DDL - Tabellen, Datentypen und Schlüssel | 1 | 10 |
| 4 | DML - INSERT, UPDATE, DELETE | 1 | 8 |
| 5 | DQL - Grundlagen der Datenabfrage (SELECT) | 1 | 10 |
| 6 | Funktionen & Aggregation | 1 | 10 |
| 7 | Joins (Verknüpfungen) | 1 | 12 |
| 8 | Unterabfragen (Subqueries) & CTEs | 2 | 10 |
| 9 | Sichten (Views) | 2 | 10 |
| 10 | Indizes und Performance-Grundlagen | 1 | 10 |
| 11 | Transaktionen (ACID) & Sperren | 1 | 10 |
| 12 | Troubleshooting, Diagnose & Backup | 1 | 10 |
| **Gesamt** | **10x Prio 1, 2x Prio 2** | | **120** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln zwingend erforderliche Kernkompetenzen. Module mit Priorität 2 dienen der Vertiefung und können bei Zeitmangel gekürzt werden.*

### 2. Quellen

* **PostgreSQL 15 Documentation**, The PostgreSQL Global Development Group, Stand 2023, URL: https://www.postgresql.org/docs/15/index.html (nicht abgerufen). Die Versionsnummer 15 entspricht dem Paket in Debian 12 (nicht geprüft).
* **ISO/IEC 9075-1:2023 (Information technology — Database languages — SQL)**, ISO, Stand 2023, URL nicht geprüft (kostenpflichtige Norm). Zur SQL-Konformität von PostgreSQL: PostgreSQL 15 Documentation, Anhang „SQL Conformance“, URL: https://www.postgresql.org/docs/15/features.html (nicht abgerufen). Kein Datenbanksystem erfüllt den Standard vollständig.
* **RFC 1918 (Address Allocation for Private Internets)**, IETF, Stand Februar 1996, URL: https://datatracker.ietf.org/doc/html/rfc1918
* **DBeaver Community Documentation**, DBeaver Corp, Stand nicht geprüft, URL: https://dbeaver.com/docs/dbeaver/ (laut Suchergebnis, nicht abgerufen; die frühere Adresse `.../docs/wiki/` ist nicht bestätigt). Zum Treiber-Manager: https://dbeaver.com/docs/dbeaver/Driver-Manager/ (laut Suchergebnis, nicht abgerufen).
* **RFC 5802** (Salted Challenge Response Authentication Mechanism, SCRAM) und **RFC 7677** (SCRAM-SHA-256), URLs: https://datatracker.ietf.org/doc/html/rfc5802, https://datatracker.ietf.org/doc/html/rfc7677 (nicht abgerufen). Grundlage der Passwortprüfung `scram-sha-256` in Modul 2.
* **PostgreSQL 15 Release Notes** (Änderung der Rechte im Schema `public`), URL: https://www.postgresql.org/docs/15/release-15.html (nicht abgerufen). Das Verhalten wurde in einer Testumgebung mit PostgreSQL 16 bestätigt (Modul 2, Aufgabe 4).
* **Microsoft Evaluation Center** (Windows 11 Enterprise Evaluation) und **Debian 12 netinst-ISO** (debian.org), URLs nicht geprüft. Die Laufzeit von 90 Tagen ist nicht bestätigt.
* Normalformen, Entity-Relationship-Modell und ACID werden nur als Begriffe verwendet; eine geprüfte Quelle liegt nicht vor.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V (lokal) auf Windows 10/11 Pro oder Enterprise mit mindestens 8 GB freiem Arbeitsspeicher und 80 GB freiem Speicherplatz (Richtwert, nicht erprobt).
**Netzwerk:** Ein privater virtueller Switch `DB-Lab` (isoliert, `192.168.100.0/24`). Jede VM hat einen Netzwerkadapter. Für die Installation vor Modul 2 und die Internet-Phase in Modul 2 hängt er am vorhandenen Hyper-V-Switch `Default Switch` (NAT, DHCP) und wird in Modul 2 auf `DB-Lab` umgestellt; danach haben die VMs keinen Internetzugang mehr.
**Namensauflösung:** Im Labor gibt es keinen DNS-Server. Die Namen `db-server.example.internal` und `db-client.example.internal` sind die Hostnamen der VMs; alle Aufgaben verwenden die IP-Adressen.

**Benötigte VMs (Erforderlich ab Modul 2):**
1. **Server-VM (`db-server.example.internal`, `192.168.100.10/24`):** Debian 12 (netinst-ISO), minimale Installation mit der Softwareauswahl „Standard-Systemwerkzeuge“, Generation-2-VM mit der Secure-Boot-Vorlage „Microsoft UEFI Certificate Authority“ (Vorlage für Linux laut Microsoft Learn), 2 GB RAM, 20 GB Festplatte (Richtwerte). Benutzer `labadmin` mit sudo (dafür das Root-Kennwort bei der Installation leer lassen; Verhalten nicht bestätigt). Die statische Adresse wird in Modul 2 eingerichtet.
2. **Client-VM (`db-client.example.internal`, `192.168.100.20/24`):** Windows 11 Enterprise Evaluation (Standard; Generation 2 mit TPM, 4 GB RAM, 64 GB Festplatte; Laufzeit von 90 Tagen nicht bestätigt). Alternativ Debian 12 mit Desktop; die Aufgaben sind für beide gleich, nur Installation und Netzwerkeinstellung von DBeaver unterscheiden sich. Die Windows-Einrichtung (lokales Konto) erfolgt vor Modul 2 mit Internet über den `Default Switch`.

Beide Betriebssysteme werden vor Modul 2 installiert (nicht in den Unterrichtseinheiten enthalten); danach wird je VM ein Hyper-V-Prüfpunkt `Basis` erstellt.

**Benötigte Software:**
* PostgreSQL 15 (Paket `postgresql` aus dem offiziellen Debian-Repository; unter Debian 12 ist das Version 15, nicht bestätigt).
* DBeaver Community Edition (kostenlos, Open Source) auf der Client-VM. DBeaver lädt den JDBC-Treiber für PostgreSQL aus dem Internet; er wird deshalb in der Internet-Phase von Modul 2 heruntergeladen.

**Vom Kursleiter bereitzustellen:** Eine fiktive Kundenrechnung und eine „Flat-File“-Tabelle für Modul 1 (Papier oder PDF).

**Datenmodell:** Die Tabellen `abteilung`, `mitarbeiter` und `projekt` mit festen Spalten werden in Modul 3 definiert; alle späteren Module verwenden diese Namen. Die SQL-Beispiele der Module 3 bis 12 wurden in einer Testumgebung mit PostgreSQL 16 unter Ubuntu ausgeführt, nicht mit PostgreSQL 15 unter Debian 12.

Alle Praxisaufgaben (außer Modul 1) sind als technische Konfigurations- und Abfrageübungen innerhalb dieses isolierten Netzwerks konzipiert, mit Ausnahme der Internet-Phase in Modul 2.


## B. Detaillierter Modulaufbau

### Modul 1: Relationale Modelle & Normalisierung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Konzepte relationaler Datenbanken erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Entity-Relationship-Modelle lesen und einfache erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende unstrukturierte Daten bis zur 3. Normalform (3NF) normalisieren.
* **Voraussetzungen:** IT-Grundkenntnisse.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Grundlagen relationaler Datenbanken und Terminologie (Tupel, Relationen, Attribute) | 3 |
| 1.2 | Entity-Relationship-Modelle (ERM) | 3 |
| 1.3 | Normalisierung (1NF, 2NF, 3NF) | 4 |

#### Praxisaufgaben (Hands-on Lab)
*(Hinweis: Für dieses Modul ist kein technisches Labor nötig.)*
1. **Fallstudie ERM:** Analysiere die vom Kursleiter bereitgestellte fiktive Kundenrechnung (Papier/PDF) und erstelle daraus ein fachliches Entity-Relationship-Modell.
2. **Fallstudie Normalisierung:** Überführe die vom Kursleiter bereitgestellte „Flat-File“-Tabelle (Mitarbeiter-, Abteilungs- und Projektdaten gemischt, z. B. mit den Spalten Mitarbeitername, E-Mail, Gehalt, Abteilungsname, Standort, Projektbezeichnung und Projektstart) schrittweise auf Papier in die 1., 2. und 3. Normalform. Das Ergebnis dient als Vorlage für die Tabellen in Modul 3.

#### Kontrollfragen
1. Was ist der Unterschied zwischen einem Attribut und einem Tupel?
2. Warum führt redundante Datenhaltung zu Anomalien (Insert, Update, Delete)?
3. Welche Bedingung muss erfüllt sein, damit sich eine Tabelle in der 2. Normalform befindet?
4. Was beschreibt die Kardinalität (z. B. 1:n) in einem ER-Modell?


### Modul 2: Installation & Labor-Aufbau (PostgreSQL)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende PostgreSQL auf einem Linux-System installieren.
  * Nach Abschluss dieses Moduls kann der Lernende den Netzwerkzugriff auf die Datenbank sicher konfigurieren (`pg_hba.conf`).
  * Nach Abschluss dieses Moduls kann der Lernende einen SQL-Client (DBeaver) mit dem Datenbankserver verbinden.
* **Voraussetzungen:** Modul 1; grundlegende Linux-Kommandozeilen-Kenntnisse; beide VMs sind installiert (Prüfpunkt `Basis`) und hängen am `Default Switch` mit Internetzugang.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Temporäre Internetphase und Installation PostgreSQL | 3 |
| 2.2 | Konfiguration von `postgresql.conf` und `pg_hba.conf` | 4 |
| 2.3 | Client-Installation und Verbindungsaufbau | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Vorbereitung - Temporäre Internetphase:** Installiere auf dem Server `postgresql` (`sudo apt update && sudo apt install -y postgresql`) und prüfe mit `sudo -u postgres psql -c "SELECT version();"` die Version. Installiere auf dem Client DBeaver Community (Installationsprogramm von dbeaver.io, nicht geprüft). Starte DBeaver einmal und lade im Treiber-Manager (Menü „Datenbank“, Bezeichnung nicht bestätigt) den Treiber für PostgreSQL herunter, damit die Verbindung später ohne Internet funktioniert. Stelle danach den Netzwerkadapter beider VMs in den Hyper-V-Einstellungen vom `Default Switch` auf den privaten Switch `DB-Lab` um. **Die VMs dürfen danach nie wieder am `Default Switch` hängen!**
2. **Statische IP-Adressen:** Ermittle auf dem Server den Adapternamen mit `ip -br a`, trage in `/etc/network/interfaces` für ihn statt `dhcp` die Zeilen `iface eth0 inet static` und `address 192.168.100.10/24` ein (ohne Gateway; Datei und Adaptername `eth0` für Debian 12 nicht bestätigt) und lade mit `sudo systemctl restart networking`. Stelle auf dem Client in den Eigenschaften des Netzwerkadapters IPv4 statisch `192.168.100.20` mit der Maske `255.255.255.0` ein (Debian-Desktop: über die Netzwerkeinstellungen). Teste mit `ping 192.168.100.10` vom Client aus.
3. **Konfiguration Netzwerkzugriff:** Konfiguriere die `postgresql.conf` (unter Debian `/etc/postgresql/15/main/`, Pfad mit `ls /etc/postgresql` prüfen), sodass der Server auf `192.168.100.10` lauscht (`listen_addresses = '192.168.100.10'`). Richte die Datei `pg_hba.conf` im selben Verzeichnis mit der Zeile `host firma labuser 192.168.100.0/24 scram-sha-256` so ein, dass Authentifizierung über Passwort (`scram-sha-256`) nur für dieses Netz erlaubt ist. Starte den Dienst mit `sudo systemctl restart postgresql` neu und prüfe mit `ss -tln` (Port 5432 auf `192.168.100.10`).
4. **Datenbanknutzer und Datenbank:** Starte auf dem Server `sudo -u postgres psql`. Lege den Nutzer mit `CREATE ROLE labuser LOGIN;` an, vergib das Passwort mit `\password labuser` (es wird als `scram-sha-256` gespeichert) und erstelle die Datenbank mit `CREATE DATABASE firma OWNER labuser;`. Die Angabe `OWNER labuser` ist nötig: Seit PostgreSQL 15 darf nur der Eigentümer der Datenbank im Schema `public` Tabellen anlegen (in einer Testumgebung mit PostgreSQL 16 bestätigt); ohne `OWNER` scheitert Modul 3 mit `permission denied for schema public`.
5. **Verbindungsaufbau:** Lege in DBeaver auf der Client-VM eine PostgreSQL-Verbindung an (Host `192.168.100.10`, Port `5432`, Datenbank `firma`, Benutzer `labuser`) und teste die Verbindung. Öffne einen SQL-Editor und führe `SELECT version();` aus.
6. **Prüfpunkt:** Erstelle auf beiden VMs den Hyper-V-Prüfpunkt `M2-fertig`.

#### Kontrollfragen
1. Welchen Zweck erfüllt die Datei `pg_hba.conf` in PostgreSQL?
2. Warum ist es ein Sicherheitsrisiko, `listen_addresses = '*'` ohne Firewall oder starke `pg_hba.conf`-Regeln in produktiven, öffentlichen Netzen zu betreiben?
3. Welcher Standard-TCP-Port wird von PostgreSQL verwendet?


### Modul 3: DDL - Tabellen, Datentypen und Schlüssel
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Tabellen mittels `CREATE TABLE` anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende passende Datentypen für verschiedene Informationen auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende Primärschlüssel (Primary Keys) und Fremdschlüssel (Foreign Keys) definieren.
* **Voraussetzungen:** Modul 2 (laufende DB und Client-Verbindung).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Data Definition Language (DDL) Grundlagen & Datentypen | 3 |
| 3.2 | Anlegen und Ändern von Tabellen (`CREATE`, `ALTER`, `DROP`) | 3 |
| 3.3 | Constraints: Primärschlüssel, Fremdschlüssel, UNIQUE, NOT NULL | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **CREATE TABLE:** Lege in der Datenbank `firma` (über DBeaver als `labuser`) drei Tabellen mit diesen Spalten an: `abteilung` (`abteilung_id`, `name` Pflicht, `standort`), `mitarbeiter` (`mitarbeiter_id`, `vorname` Pflicht, `nachname` Pflicht, `email`, `gehalt`, `abteilung_id`) und `projekt` (`projekt_id`, `bezeichnung` Pflicht, `startdatum`, `abteilung_id`). Verwende sinnvolle Datentypen (z. B. `VARCHAR`, `INTEGER`, `DATE`, `NUMERIC(10,2)` für das Gehalt). Die Schlüsselspalten `..._id` werden als `INTEGER GENERATED ALWAYS AS IDENTITY` angelegt. Die Spalte `abteilung_id` in `mitarbeiter` und `projekt` bleibt ohne `NOT NULL`. Alle späteren Module verwenden diese Namen. Speichere die Befehle in einem DBeaver-Skript `01_struktur.sql`.
2. **Constraints definieren:** Ergänze die Tabellen um Primärschlüssel (`..._id`). Erstelle in `mitarbeiter` und in `projekt` je einen Fremdschlüssel auf `abteilung` und lege auf `mitarbeiter.email` eine `UNIQUE`-Bedingung.
3. **ALTER TABLE:** Ändere die Tabelle `mitarbeiter` nachträglich ab und füge eine Spalte `einstellungsdatum` (`DATE`) hinzu, die nicht `NULL` sein darf (Tipp: Verwende den Default-Wert `CURRENT_DATE`).
4. **DROP TABLE:** Lege eine Hilfstabelle `temp_test` (eine Spalte `x INTEGER`) an und lösche sie mit `DROP TABLE temp_test;` wieder. Prüfe im DBeaver-Navigator (Aktualisieren), dass sie verschwunden ist.

#### Kontrollfragen
1. Wofür steht die Abkürzung DDL und welche SQL-Befehle gehören primär dazu?
2. Was ist der funktionale Unterschied zwischen einem `CHAR(50)` und einem `VARCHAR(50)` Datentyp?
3. Welche Bedingungen müssen erfüllt sein, damit ein Fremdschlüssel erfolgreich auf eine andere Tabelle verweisen kann?


### Modul 4: DML - INSERT, UPDATE, DELETE
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Datensätze manuell einfügen.
  * Nach Abschluss dieses Moduls kann der Lernende bestehende Daten sicher aktualisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Daten selektiv löschen, ohne unbeabsichtigt den gesamten Bestand zu entfernen.
* **Voraussetzungen:** Modul 3 (Struktur der Tabellen `abteilung`, `mitarbeiter`, `projekt` existiert).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Daten einfügen (`INSERT INTO`) | 3 |
| 4.2 | Daten aktualisieren (`UPDATE`) | 3 |
| 4.3 | Daten löschen (`DELETE`) und Sicherheitsmaßnahmen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **INSERT:** Füge 3 Abteilungen (z. B. Verwaltung, Technik, Vertrieb) in die Tabelle `abteilung` ein und ermittle die vergebenen IDs mit `SELECT`. Füge anschließend 5 fiktive Mitarbeiter (E-Mail-Adressen mit `example.com`) in die Tabelle `mitarbeiter` ein, jeweils mit Gehalt und unterschiedlichem `einstellungsdatum`. Achte auf die Foreign-Key-Abhängigkeiten (zuerst Abteilung, dann Mitarbeiter anlegen). Die Daten müssen diese Bedingungen erfüllen, weil spätere Module sie brauchen: ein Mitarbeiter heißt Müller, mindestens zwei Nachnamen beginnen mit „M“, drei Mitarbeiter gehören zur selben Abteilung, ein Mitarbeiter hat keine E-Mail-Adresse (`NULL`), jeder Mitarbeiter hat eine Abteilung. Füge außerdem 2 Projekte in `projekt` ein. Speichere alle `INSERT`-Anweisungen in einem DBeaver-Skript `02_daten.sql`.
2. **UPDATE:** Erhöhe das Gehalt des Mitarbeiters Müller mithilfe einer `WHERE`-Klausel, die den Primärschlüssel anspricht. Prüfe mit `SELECT` vorher und nachher den Wert.
3. **DELETE mit Prüfpunkt:** Füge zunächst einen Testmitarbeiter (Vorname `Test`, Nachname `Löschkandidat`) ein und ermittle seine ID. Prüfe mit `SELECT COUNT(*) FROM mitarbeiter` die Zeilenzahl. DBeaver führt Änderungen standardmäßig sofort fest aus (Auto-Commit, nicht bestätigt); ein `DELETE` ist daher nicht zurücknehmbar, der Bestand lässt sich nur mit dem Skript `02_daten.sql` neu einfügen. Lösche genau diesen Testmitarbeiter anhand seiner ID und prüfe die Zeilenzahl erneut. Versuche dann ein `DELETE` auf eine Abteilung, die noch Mitarbeiter hat, um den Foreign-Key-Constraint-Fehler zu provozieren (Meldung `violates foreign key constraint`).

#### Kontrollfragen
1. Wofür steht DML?
2. Warum sollte ein `UPDATE`- oder `DELETE`-Befehl im produktiven Einsatz fast immer eine `WHERE`-Klausel enthalten?
3. Was passiert, wenn man einen Datensatz löschen möchte, auf den noch ein Fremdschlüssel aus einer anderen Tabelle verweist (Standardverhalten ohne CASCADE)?


### Modul 5: DQL - Grundlagen der Datenabfrage (SELECT)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende spezifische Spalten aus Tabellen abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende Ergebnismengen mit logischen Operatoren filtern.
  * Nach Abschluss dieses Moduls kann der Lernende Ausgaben sortieren und limitieren.
* **Voraussetzungen:** Modul 4 (Tabelle enthält Daten).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Der `SELECT`-Befehl, Aliasse (`AS`) und die logische Verarbeitungsreihenfolge (`FROM`, `WHERE`, `SELECT`) | 3 |
| 5.2 | Filtern mit `WHERE`, logische Operatoren (`AND`, `OR`, `NOT`) und Pattern Matching (`LIKE`) | 4 |
| 5.3 | Sortieren (`ORDER BY`) und Limitieren (`LIMIT` / `OFFSET`) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Daten abfragen:** Erstelle Abfragen, die nur die Namen und das Einstellungsdatum aller Mitarbeiter ausgeben. Vergib sinnvolle Aliasnamen für die Ausgabe (z.B. `AS "Eintritt"`).
2. **Filtern:** Schreibe ein SQL-Statement, das nur Mitarbeiter einer bestimmten Abteilung findet, deren Nachname mit „M“ beginnt (`LIKE 'M%'`). Erweitere die Bedingung danach mit `OR` (zusätzlich alle Mitarbeiter mit einem Gehalt über 4000) und mit `NOT` (aber nicht die Mitarbeiter einer bestimmten Abteilung).
3. **Paginierung:** Sortiere die Mitarbeiter alphabetisch (`ORDER BY nachname`) und lasse dir nur die ersten drei Datensätze anzeigen (`LIMIT 3`). Zeige die nächsten Datensätze mit `OFFSET 3` an und sortiere in einer weiteren Abfrage absteigend nach Gehalt (`DESC`).

#### Kontrollfragen
1. In welcher Reihenfolge verarbeitet die Datenbank-Engine (logisch) die Klauseln `SELECT`, `FROM` und `WHERE`?
2. Was ist der Unterschied zwischen dem Operator `=` und dem Operator `LIKE`?
3. Wie sortiert man eine Ausgabe absteigend?


### Modul 6: Funktionen & Aggregation
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Skalarfunktionen auf Daten anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Daten aggregieren (Summen, Durchschnitte, Anzahl).
  * Nach Abschluss dieses Moduls kann der Lernende gruppierte Daten mit `HAVING` filtern.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Skalarfunktionen (z. B. UPPER, LOWER, COALESCE) | 3 |
| 6.2 | Aggregatfunktionen (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`) | 4 |
| 6.3 | Gruppierung (`GROUP BY`) und Filterung von Gruppen (`HAVING`) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Skalarfunktionen:** Formatiere die Ausgabe der Nachnamen durchgehend als Großbuchstaben (`UPPER`) und ersetze die `NULL`-Werte der E-Mail-Spalte mit `COALESCE` durch den Text 'Nicht angegeben'.
2. **Aggregation:** Berechne die Gesamtanzahl aller Mitarbeiter (`COUNT`), das durchschnittliche Gehalt (`AVG`) sowie die Summe, das Minimum und das Maximum des Gehalts (`SUM`, `MIN`, `MAX`).
3. **GROUP BY:** Gruppiere die Mitarbeiter nach Abteilungs-ID und ermittle die Anzahl der Mitarbeiter pro Abteilung. Filtere die Ausgabe mit `HAVING`, sodass nur Abteilungen mit mehr als einem Mitarbeiter angezeigt werden.

#### Kontrollfragen
1. Warum führt der Befehl `SELECT abteilung_id, COUNT(*) FROM mitarbeiter;` (ohne GROUP BY) zu einem Syntax- oder Logikfehler?
2. Was ist der Unterschied zwischen der `WHERE`- und der `HAVING`-Klausel?
3. Welche Aufgabe erfüllt die Funktion `COALESCE`?


### Modul 7: Joins (Verknüpfungen)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Daten aus mehreren Tabellen zusammenführen.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen Inner und Outer Joins erklären und anwenden.
* **Voraussetzungen:** Modul 3 und Modul 4 (die Tabellen `abteilung`, `mitarbeiter` und `projekt` haben Daten mit Foreign-Key-Relation).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Konzept der Joins, Tabellen-Aliasse und kartesisches Produkt (`CROSS JOIN`) | 4 |
| 7.2 | `INNER JOIN` | 4 |
| 7.3 | `OUTER JOINS` (`LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`) | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **INNER JOIN:** Erstelle eine Abfrage, die Vorname, Nachname und den **Namen der Abteilung** (aus der Tabelle `abteilung`) nebeneinander anzeigt. Verwende Tabellen-Aliasse (z.B. `FROM mitarbeiter m INNER JOIN abteilung a ON ...`).
2. **LEFT JOIN Vorbereitung:** Füge einen neuen Mitarbeiter hinzu, dem keine Abteilung zugewiesen ist (`abteilung_id` bleibt `NULL`; die Spalte wurde in Modul 3 ohne `NOT NULL` angelegt), und eine neue Abteilung `Archiv` ohne Mitarbeiter.
3. **LEFT JOIN Ausführung:** Führe einen `LEFT JOIN` von `mitarbeiter` auf `abteilung` aus. Identifiziere den Mitarbeiter ohne Abteilung (er zeigt NULL-Werte für Abteilungsspalten).
4. **RIGHT JOIN und FULL JOIN:** Finde mit einem `RIGHT JOIN` die Abteilung ohne Mitarbeiter. Zeige mit einem `FULL JOIN` und passender `WHERE`-Bedingung beide Sonderfälle (Mitarbeiter ohne Abteilung und Abteilung ohne Mitarbeiter) in einer Ergebnismenge.
5. **Kartesisches Produkt:** Führe `SELECT COUNT(*) FROM mitarbeiter CROSS JOIN abteilung` aus und vergleiche das Ergebnis mit dem Produkt der Zeilenzahlen beider Tabellen.
6. **Join über `projekt`:** Verknüpfe `projekt` per `INNER JOIN` mit `abteilung` und zeige Projektbezeichnung und Abteilungsname.

#### Kontrollfragen
1. Welche Zeilen liefert ein `INNER JOIN` zurück?
2. Warum würde man einen `LEFT JOIN` einem `INNER JOIN` vorziehen?
3. Was versteht man unter einem "Kartesischen Produkt" (CROSS JOIN) und warum sollte es bei großen Tabellen vermieden werden?


### Modul 8: Unterabfragen (Subqueries) & CTEs
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende verschachtelte Abfragen in WHERE-, FROM- und SELECT-Klauseln einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Common Table Expressions (CTEs) für bessere Lesbarkeit nutzen.
* **Voraussetzungen:** Modul 5, Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Subqueries in der `WHERE`-, `FROM`- und `SELECT`-Klausel (skalare Unterabfragen, abgeleitete Tabellen) | 3 |
| 8.2 | Korrelierte Unterabfragen | 4 |
| 8.3 | Common Table Expressions (`WITH`-Klausel / CTEs) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **WHERE-Subquery:** Finde alle Mitarbeiter, deren Gehalt höher ist als der Durchschnitt aller Gehälter (Subquery `SELECT AVG(...) FROM ...` im WHERE-Block). Gib in der `SELECT`-Liste zusätzlich den Durchschnitt per skalarer Unterabfrage aus.
2. **Korrelierte Subquery:** Finde für jede Abteilung den Mitarbeiter mit dem höchsten Gehalt innerhalb dieser spezifischen Abteilung.
3. **FROM-Subquery:** Zähle die Mitarbeiter je Abteilung in einer Unterabfrage in der `FROM`-Klausel und filtere die äußere Abfrage auf Abteilungen mit mindestens einem Mitarbeiter.
4. **CTE:** Schreibe die Abfrage aus Aufgabe 1 um und verwende dazu das `WITH`-Statement, um die Durchschnittsberechnung als benannte temporäre Hilfstabelle voranzustellen.

#### Kontrollfragen
1. Was unterscheidet eine "korrelierte" Unterabfrage von einer "nicht-korrelierten" Unterabfrage bezüglich der Performance?
2. In welchen Klauseln des Haupt-Statements kann eine skalare Unterabfrage (liefert genau 1 Wert) stehen?
3. Welchen primären Vorteil bietet eine CTE (`WITH`) gegenüber tief verschachtelten Subqueries?


### Modul 9: Sichten (Views)
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Datenbank-Sichten anlegen und abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen logischen Views und Materialized Views (PostgreSQL-spezifisch) erklären.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Konzept und Einsatzszenarien von Views | 3 |
| 9.2 | Anlegen und Verwalten (`CREATE VIEW`, `DROP VIEW`) | 3 |
| 9.3 | Materialized Views in PostgreSQL | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **CREATE VIEW:** Erstelle eine Abfrage mit Join (`LEFT JOIN`, damit Mitarbeiter ohne Abteilung erhalten bleiben), die sensible Mitarbeiterdaten (wie Gehälter) ausblendet und nur Name, Abteilung und E-Mail anzeigt. Speichere dies als `VIEW vw_mitarbeiterliste`.
2. **View abfragen:** Führe ein einfaches `SELECT * FROM vw_mitarbeiterliste` aus.
3. **Materialized View:** Erstelle eine `MATERIALIZED VIEW` über eine aggregierte Statistik (z.B. Mitarbeiteranzahl pro Abteilung) und probiere den Befehl `REFRESH MATERIALIZED VIEW` aus, nachdem du einen Datensatz in der Basistabelle geändert hast.
4. **DROP VIEW:** Entferne die View probeweise mit `DROP VIEW vw_mitarbeiterliste;` und lege sie mit dem Befehl aus Aufgabe 1 erneut an.

#### Kontrollfragen
1. Speichert ein Standard-View die Daten physisch auf der Festplatte?
2. Warum nutzt man Sichten im Hinblick auf Sicherheit und Berechtigungsmanagement?
3. In welchem Szenario ist ein "Materialized View" einem Standard-View vorzuziehen?


### Modul 10: Indizes und Performance-Grundlagen
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Indizes zur Beschleunigung von Abfragen anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ausführungsplan einer Abfrage mittels `EXPLAIN` grob analysieren.
* **Voraussetzungen:** Modul 5 (Daten aus Modul 4, darunter der Mitarbeiter Müller).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Funktionsweise von Indizes (B-Tree-Grundlagen) | 3 |
| 10.2 | Indizes anlegen und entfernen (`CREATE INDEX`, `DROP INDEX`) | 4 |
| 10.3 | Ausführungspläne lesen (`EXPLAIN`, `EXPLAIN ANALYZE`) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Testdaten erzeugen:** Mit nur wenigen Zeilen wählt PostgreSQL immer einen Sequential Scan; ein Index bringt dort nichts. Erzeuge daher 100000 Testzeilen und aktualisiere die Statistik:
   ```sql
   INSERT INTO mitarbeiter (vorname, nachname, email, gehalt, abteilung_id)
   SELECT 'Test' || g, 'Name' || (g % 5000), 'test' || g || '@example.com',
          2000 + (g % 3000), (SELECT MIN(abteilung_id) FROM abteilung)
   FROM generate_series(1, 100000) AS g;
   ANALYZE mitarbeiter;
   ```
2. **Baseline messen:** Nutze `EXPLAIN ANALYZE SELECT * FROM mitarbeiter WHERE nachname = 'Müller';` und dokumentiere den Plan (erwartet: "Seq Scan") und die `Execution Time`.
3. **Index erstellen:** Erstelle einen Index auf die Spalte Nachname (`CREATE INDEX idx_mitarbeiter_nachname ON mitarbeiter(nachname);`).
4. **Vergleich:** Führe das `EXPLAIN ANALYZE`-Kommando aus Aufgabe 2 erneut aus. Prüfe, ob nun ein "Index Scan" oder "Bitmap Index Scan" anstelle des "Seq Scan" verwendet wird (in einer Testumgebung mit PostgreSQL 16 erschien ein Bitmap Index Scan; welche Variante der Planer wählt, hängt von der Statistik ab), und vergleiche die `Execution Time`.
5. **Rückbau:** Prüfe mit `SELECT COUNT(*) FROM mitarbeiter WHERE vorname LIKE 'Test%';`, dass genau 100000 Testzeilen vorhanden sind, und lösche sie mit `DELETE FROM mitarbeiter WHERE vorname LIKE 'Test%';`. Entferne danach den Index mit `DROP INDEX idx_mitarbeiter_nachname;` und prüfe, dass wieder nur die ursprünglichen Mitarbeiter vorhanden sind.

#### Kontrollfragen
1. Warum sollte man nicht einfach auf jede Spalte einer Tabelle einen Index legen?
2. Welchen Einfluss hat ein Index auf DML-Operationen (`INSERT`, `UPDATE`, `DELETE`)?
3. Was zeigt der Befehl `EXPLAIN` in PostgreSQL?


### Modul 11: Transaktionen (ACID) & Sperren
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das ACID-Prinzip erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Transaktionsblöcke steuern (`BEGIN`, `COMMIT`, `ROLLBACK`).
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip von Sperren (Locks) und Deadlocks im Ansatz verstehen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Das ACID-Prinzip in relationalen Datenbanken | 3 |
| 11.2 | Transaktionssteuerung (`BEGIN`, `COMMIT`, `ROLLBACK`) | 4 |
| 11.3 | Nebenläufigkeit, Table/Row Locks und Deadlocks (Grundlagen) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Sicherung anlegen:** Lege vor den Übungen eine Sicherungskopie an: `CREATE TABLE mitarbeiter_sicherung AS SELECT * FROM mitarbeiter;` und prüfe die Zeilenzahl beider Tabellen. DBeaver führt Änderungen standardmäßig sofort fest aus (nicht bestätigt); stelle für die folgenden Aufgaben den Transaktionsmodus auf „Manuell“ (Bezeichnung und Ort nicht bestätigt) und beende jede Transaktion ausdrücklich mit `COMMIT` oder `ROLLBACK`. Sollten Daten verloren gehen, stellst du sie mit `DELETE FROM mitarbeiter;` und `INSERT INTO mitarbeiter OVERRIDING SYSTEM VALUE SELECT * FROM mitarbeiter_sicherung;` wieder her.
2. **Rollback testen:** Öffne ein SQL-Skript. Starte eine Transaktion mit `BEGIN;`. Lösche per `DELETE` alle Datensätze der Mitarbeitertabelle. Mache einen `SELECT` (Tabelle ist leer). Setze ein `ROLLBACK;` ab. Prüfe per `SELECT`, ob die Daten wieder da sind.
3. **Commit:** Starte eine Transaktion (`BEGIN;`), füge einen Datensatz hinzu und bestätige diese permanent mit `COMMIT;`.
4. **Locks und Isolation:** Öffne **zwei** unabhängige Verbindungen (zwei SQL-Editor-Tabs; legt DBeaver für den zweiten Tab keine eigene Verbindung an, erstelle eine zweite Verbindung `firma-2`; nicht bestätigt). Starte in Tab 1 `BEGIN;` und ändere eine Zeile (UPDATE), mach aber *kein* COMMIT. Lies in Tab 2 dieselbe Zeile per `SELECT` (sie zeigt noch den alten Wert; Standard-Isolation `READ COMMITTED`). Versuche in Tab 2 dieselbe Zeile per UPDATE zu ändern. Beobachte, wie Tab 2 "hängt", bis Tab 1 ein `COMMIT` oder `ROLLBACK` durchführt.
5. **Deadlock provozieren:** Starte in Tab 1 `BEGIN;` und ändere die Zeile mit `mitarbeiter_id = 1`; starte in Tab 2 `BEGIN;` und ändere die Zeile mit `mitarbeiter_id = 2`. Ändere dann in Tab 1 die Zeile 2 (Tab 1 wartet) und in Tab 2 die Zeile 1. PostgreSQL erkennt den Deadlock nach kurzer Zeit und bricht eine der beiden Transaktionen mit `ERROR: deadlock detected` ab. Beende beide Transaktionen mit `ROLLBACK;`.
6. **Rückbau:** Prüfe, dass `mitarbeiter` und `mitarbeiter_sicherung` wieder dieselbe Anzahl Zeilen haben (abgesehen vom Datensatz aus Aufgabe 3), und lösche die Sicherung mit `DROP TABLE mitarbeiter_sicherung;`.

#### Kontrollfragen
1. Wofür stehen die Buchstaben in ACID?
2. Welcher SQL-Befehl verwirft alle Änderungen innerhalb eines laufenden Transaktionsblocks?
3. Was passiert, wenn zwei Transaktionen sich gegenseitig blockieren und auf die Freigabe des jeweils anderen warten (Begriff)?


### Modul 12: Troubleshooting, Diagnose & Backup
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende logische Backups einer Datenbank erstellen und wiederherstellen.
  * Nach Abschluss dieses Moduls kann der Lernende PostgreSQL-Logs zur Fehlersuche heranziehen.
* **Voraussetzungen:** Alle Pflichtmodule; Zugriff auf die Linux-Shell der Server-VM (`192.168.100.10`) über die Hyper-V-Konsole mit dem Benutzer `labadmin` (sudo).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Backups mit `pg_dump` | 3 |
| 12.2 | Wiederherstellung (Restore) mit `psql` oder `pg_restore` | 4 |
| 12.3 | Analyse von Datenbank-Logs unter Linux | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Backup erstellen:** Logge dich auf der Linux-Server-VM an der Hyper-V-Konsole ein. Sichere die Datenbank `firma` mit `pg_dump` in eine SQL-Datei: `sudo -u postgres pg_dump firma > ~/firma_backup.sql` und zusätzlich im Custom-Format: `sudo -u postgres pg_dump -Fc firma > ~/firma_backup.dump`. Prüfe die Dateien mit `ls -l` und öffne die SQL-Datei mit `less` (suche nach `CREATE TABLE` und `COPY`).
2. **Restore-Test in eine neue Datenbank:** Lege mit `sudo -u postgres createdb -O labuser firma_restore` eine Testdatenbank an und stelle die SQL-Datei mit `sudo -u postgres psql -d firma_restore -v ON_ERROR_STOP=1 < ~/firma_backup.sql` wieder her. Vergleiche die Zeilenzahl von `mitarbeiter` in `firma_restore` und in `firma` (`sudo -u postgres psql -d <Datenbank> -c "SELECT COUNT(*) FROM mitarbeiter;"`). Ein Restore der Datei in die bestehende Datenbank `firma` würde viele Fehler (`already exists`) erzeugen, weil alle Objekte noch existieren (in einer Testumgebung 18 Fehler); deshalb wird in eine neue Datenbank wiederhergestellt.
3. **Restore aus dem Custom-Format:** Zeige mit `pg_restore -l ~/firma_backup.dump` den Inhalt des Archivs. Lege mit `createdb` die Datenbank `firma_restore2` an und stelle sie mit `sudo -u postgres pg_restore -d firma_restore2 --exit-on-error < ~/firma_backup.dump` wieder her. Simuliere einen Datenverlust, indem du `firma_restore` mit `sudo -u postgres dropdb firma_restore` löschst (Testdatenbank, nicht `firma`), und stelle sie aus der SQL-Datei wie in Aufgabe 2 wieder her. Prüfe die Zeilenzahlen.
4. **Log-Analyse:** Provoziere einen fehlgeschlagenen Login in DBeaver (falsches Passwort). Suche mit `sudo tail -n 20 /var/log/postgresql/postgresql-15-main.log` (Dateiname mit `ls /var/log/postgresql/` prüfen, für Debian 12 nicht bestätigt) die Einträge `FATAL: password authentication failed for user "labuser"` und die zugehörige `DETAIL`-Zeile mit der passenden Zeile der `pg_hba.conf`.
5. **Fehlersuche `pg_hba.conf`:** Sichere die Datei (`sudo cp /etc/postgresql/15/main/pg_hba.conf /etc/postgresql/15/main/pg_hba.conf.bak`). Ändere die Netzangabe in der Zeile für `firma` auf `192.168.101.0/24`, lade mit `sudo systemctl reload postgresql` neu und verbinde DBeaver erneut. Notiere die Fehlermeldung (erwartet: `no pg_hba.conf entry for host "192.168.100.20"`) und suche denselben Eintrag im Log. Stelle die Datei aus der Sicherung wieder her, lade neu und prüfe die Verbindung.
6. **Rückbau:** Lösche die Testdatenbanken mit `sudo -u postgres dropdb firma_restore` und `sudo -u postgres dropdb firma_restore2` (Namen vor dem Ausführen mit `\l` prüfen).

#### Kontrollfragen
1. Warum reicht es nicht aus, einfach die rohen Dateien aus dem Installationsordner (`/var/lib/postgresql/...`) im laufenden Betrieb wegzukopieren?
2. Was ist der Unterschied zwischen einem Dump, der reine SQL-Statements (`INSERT`) enthält, und einem Custom-Format-Dump in PostgreSQL?
3. In welchem Verzeichnis legt PostgreSQL unter Debian standardmäßig seine Logfiles ab?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (120 UE), Prioritäten (10x P1, 2x P2), Module und Lerneinheiten blieben unverändert (nachgerechnet). Aufgaben kamen hinzu; ob die Stunden dafür reichen, ist unerprobt (besonders Modul 2, 7, 11 und 12). Die SQL-Befehle der Module 3 bis 12 sowie `pg_dump`, `pg_restore`, die Log-Meldungen und die Fehlermeldung zur `pg_hba.conf` wurden auf einer PostgreSQL-16-Instanz unter Ubuntu ausgeführt, nicht mit PostgreSQL 15 unter Debian 12. Hyper-V, Windows, DBeaver und die Netzwerkkonfiguration wurden nicht ausgeführt.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf | Vorkenntnis Linux-Kommandozeile | Modul 2 setzte sie voraus, der Kopf nannte nur „IT-Grundlagen“ |
| A.2 | SCRAM-RFCs, PostgreSQL-15-Release-Notes, Evaluationsmedien ergänzt, DBeaver-Adresse und PostgreSQL-Konformität präzisiert, „nicht abgerufen“ vermerkt | `scram-sha-256` hatte keine Quelle; die ISO-Norm hatte keine Ersatz-URL; die DBeaver-Adresse ist nicht bestätigt |
| A.3 | Installation beider Betriebssysteme, Benutzer `labadmin`, statische Adressen, ein Adapter pro VM (Wechsel von `Default Switch` auf `DB-Lab`), Namensauflösung, Datenmodell, Material des Kursleiters | Die Installation der VMs, die Adressen und der Benutzer waren nirgends geplant; „externen Switch entfernen“ hätte den Switch des Hosts betroffen; die FQDNs sind ohne DNS nicht auflösbar |
| Modul 1 | Aufgaben 1 und 2 | Die „vorgegebene“ Rechnung und Flat-File-Tabelle hatte niemand bereitgestellt; die Flat-File-Tabelle bildet jetzt das Modell der Module 3 bis 12 ab |
| Modul 2 | Voraussetzungen, Aufgaben 1 bis 6 | DBeaver lädt den JDBC-Treiber beim ersten Verbindungsaufbau aus dem Internet (ohne Internet scheitert Aufgabe 3, in der Internet-Phase wurde er nicht geholt); IP-Konfiguration fehlte; Dateipfade und die `pg_hba.conf`-Zeile fehlten; ohne `OWNER labuser` kann `labuser` seit PostgreSQL 15 im Schema `public` keine Tabellen anlegen (Modul 3 wäre gescheitert); das Passwort setzt `\password` statt im Klartext; kein Prüfpunkt |
| Modul 3 | Aufgaben 1 bis 4 | Die Spalten wurden nirgends festgelegt, spätere Module brauchen aber `vorname`, `nachname`, `email`, `gehalt` und `einstellungsdatum`; die Tabelle `projekt` wurde nie verwendet; `UNIQUE` und `DROP` (Einheiten 3.2 und 3.3) hatten keine Aufgabe |
| Modul 4 | Aufgaben 1 bis 3 | Testdaten für spätere Module (Müller, Nachnamen mit „M“, drei Mitarbeiter in einer Abteilung, ein NULL-Wert) waren nicht festgelegt; das `DELETE` löschte einen echten Datensatz ohne Rückweg (DBeaver schreibt standardmäßig sofort fest); die Aufgabe wurde auf einen Testmitarbeiter und ein Einfüge-Skript umgestellt |
| Modul 5 | Einheit 5.1, Aufgaben 2 und 3 | Frage 1 (Reihenfolge von `FROM`, `WHERE`, `SELECT`) hatte keine Entsprechung in den Einheiten; `OR`, `NOT`, `OFFSET` und `DESC` aus den Einheiten und Fragen wurden nie geübt |
| Modul 6 | Aufgaben 1 und 2 | `COALESCE` auf Namen ist wirkungslos (die Spalten sind `NOT NULL`); das gewünschte Gehalt war nicht festgelegt ("sonst simuliere es"); `SUM`, `MIN`, `MAX` wurden nie geübt |
| Modul 7 | Voraussetzungen, Einheit 7.1, Aufgaben 1 bis 6 | `RIGHT JOIN` und `FULL JOIN` (Einheit 7.3) und das kartesische Produkt (Frage 3) hatten keine Aufgabe; die Nullbarkeit von `abteilung_id` war offen; `projekt` ohne Verwendung |
| Modul 8 | Einheit 8.1, Aufgaben 1 bis 4 | Das Lernziel nennt `FROM`, aber nur `WHERE` und `SELECT` wurden geübt |
| Modul 9 | Aufgaben 1 und 4 | `INNER JOIN` hätte Mitarbeiter ohne Abteilung ausgeblendet; `DROP VIEW` (Einheit 9.2) hatte keine Aufgabe |
| Modul 10 | Voraussetzungen, Aufgaben 1 bis 5 | Mit 5 Zeilen wählt PostgreSQL immer einen Seq Scan, der Index bringt nichts; das Lernziel „Index beschleunigt Abfragen“ wäre nie gezeigt worden (neu: 100000 Testzeilen mit `generate_series`); mit Index erscheint ein Bitmap Index Scan statt Index Scan (Testumgebung); Rückbau der Testdaten und des Index fehlte |
| Modul 11 | Einheit 11.3, Aufgaben 1 bis 6 | `DELETE` aller Zeilen ohne Sicherung; Deadlocks (Lernziel, Frage 3) kamen in keiner Aufgabe vor; Isolation (ACID) wurde nicht gezeigt; Verhalten von DBeaver bei `BEGIN` im Auto-Commit ist unklar |
| Modul 12 | Voraussetzungen, Aufgaben 1 bis 6 | Der Restore der ganzen Sicherungsdatei in die bestehende Datenbank erzeugt 18 Fehler (Testumgebung); `DROP TABLE mitarbeiter` scheitert, wenn Views aus Modul 9 davon abhängen; `pg_restore` und das Custom-Format (Einheit 12.2, Frage 2) wurden nie geübt; das Lernziel „Fehlersuche“ bestand nur aus dem Lesen einer Logdatei; kein Rückbau der Testdatenbanken |

**Bewertung des Prüfvermerks der ersten Fassung:** Das Format mit „Geprüft“, „Stichprobe“ und „Fehler gefunden/korrigiert“ wurde diesmal eingehalten, der Inhalt aber nicht. Punkt 1 ist korrekt. Punkt 2 ist nicht erfüllt: Die Behauptung „alle VMs definiert“ übersieht Installation, Adressen, Benutzer und den JDBC-Treiber; die angegebene „Korrektur“ (Zusatz „Erforderlich ab Modul 2“) ist kein gefundener Fehler. Punkt 3 ist nicht erfüllt: „mit URL hinterlegt“ stimmt für die ISO-Norm nicht, `scram-sha-256` fehlte. Punkt 4 ist nicht erfüllt: Die Spalten, `projekt`, die Nullbarkeit und die Rechte im Schema `public` wurden nicht beachtet, und `DROP TABLE` in Modul 12 kollidiert mit Modul 9. Punkt 5 ist nicht erfüllt: „Alle in der UE genannten Begriffe kommen als Aufgabe vor“ ist falsch (Outer Joins, `FROM`-Subquery, Deadlocks, `DROP`, `pg_restore`). Punkt 6 ist teilweise erfüllt: Der Rückbau des Internet-Zugangs stand drin, die Testdaten und die Test-Datenbanken nicht. Punkt 7 ist erfüllt (ein Server, ein Client). Punkt 8 ist nicht erfüllt: Der JDBC-Treiber braucht Internet, und die Windows-Installation war nicht geplant. Punkt 9 ist nicht erfüllt: Das `DELETE` in Modul 4 und in Modul 11 hatte keinen Rückweg, und die Reihenfolge in Modul 12 ist nur für eine Datenbank ohne Views richtig. Der Hinweis „Stichprobe: Modul 7 ergibt 12 UE“ war richtig, die Stichproben der anderen Punkte nannten Selbstverständliches.

**Hinweise und offene Punkte:**

* **Nicht bestätigt, vor Kursstart auf Debian 12 mit PostgreSQL 15 prüfen:** Pfade `/etc/postgresql/15/main/` und `/var/log/postgresql/postgresql-15-main.log`; Konfiguration über `/etc/network/interfaces` und der Adaptername `eth0`; sudo für `labadmin` bei leerem Root-Kennwort; Auto-Commit-Verhalten von DBeaver bei `BEGIN`; Treiber-Manager und Transaktionsmodus (Menünamen); ob DBeaver für den zweiten Editor-Tab eine eigene Verbindung öffnet; Laufzeit der Windows-Evaluation (90 Tage).
* Bei Zeitmangel kann Aufgabe 5 in Modul 11 (Deadlock) und Aufgabe 5 in Modul 12 (`pg_hba.conf`) entfallen.