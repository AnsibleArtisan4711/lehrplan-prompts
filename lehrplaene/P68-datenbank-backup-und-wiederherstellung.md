# Lehrplan: Datenbank-Backup und Wiederherstellung

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | SQL-Grundlagen; Linux-Grundlagen (Kommandozeile, Bash); Grundbegriffe von Datenbankservern (PostgreSQL oder MariaDB) |
| **Gesamtumfang** | 8 Module, 45 UE (zu 45 Minuten; 33,75 Stunden) |
| **Fokus-Technologien** | Sicherungskonzept (RPO, RTO), logische Sicherungen mit `pg_dump` und `mariadb-dump`, SQLite-Sicherung, Wiederherstellungstest, Komprimierung, Verschlüsselung und Aufbewahrung, Sicherungsskript, Offsite-Kopien (Modell) und Abschlussprojekt mit gemessenem Datenverlust |
| **Thematische Abgrenzung (Out of Scope)** | Real ausgeführt wurden PostgreSQL 16, MariaDB 10.11, SQLite, `gzip` und `age` 1.1.1 im Cloud-Container. Physische Sicherungen (`mariabackup`, `pg_basebackup`) und die Wiederherstellung zu einem Zeitpunkt (PITR) gehören zur Übungsreihe P31 (MariaDB und PostgreSQL Administration) und werden hier nur verwiesen. **Offsite-Speicher, Objektsperren und `cron` wurden nicht ausgeführt** (Modell und Text). `zstd` war nicht verfügbar. Rechtliche Aufbewahrungsfristen wurden nicht geprüft |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Sicherungskonzept: RPO und RTO | 1 | 5 |
| 2 | Logische Sicherung mit pg_dump und mariadb-dump | 1 | 6 |
| 3 | SQLite sichern | 1 | 6 |
| 4 | Wiederherstellungstest | 1 | 5 |
| 5 | Komprimierung, Verschlüsselung und Aufbewahrung | 1 | 6 |
| 6 | Sicherungsskript | 1 | 6 |
| 7 | Offsite-Kopien und 3-2-1-Regel | 2 | 5 |
| 8 | Abschlussprojekt: Datenverlust messen | 1 | 6 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **45** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Offsite und 3-2-1-Regel). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 40 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von PostgreSQL, MariaDB, SQLite und `age` wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden durch Läufe im Test-Container bestätigt. Die 3-2-1-Regel und die Aufbewahrung nach Generationen sind allgemeine Praxisregeln (Fachwissen, nicht belegt). Daten sind erfunden.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** PostgreSQL 16, MariaDB 10.11, `sqlite3`, `gzip`, `age` 1.1.1, `flock`, Python 3, Bash. **Nicht ausgeführt:** Offsite-Speicher, Objektsperre (WORM), `cron`, `zstd`, Windows.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-DBBackup`, `10.68.0.0/24`).

**VM 1:** `db01` (**erforderlich**, `10.68.0.2`): Linux-Server mit PostgreSQL und MariaDB (Pakete der Distribution).

**VM 2:** `db02` (**erforderlich** ab Modul 4, `10.68.0.3`): Testinstanz für Wiederherstellungen. Optional: `sicherung01` als Sicherungsziel (Modul 6 und 7).

**Internetphase:** Für die Installation der Pakete brauchen die VMs vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 4 von `db01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte legen eigene Instanzen unter `/tmp/p68` an (PostgreSQL-Ports 5481 und 5482, MariaDB-Ports 3381 und 3382) und räumen am Ende auf; sie brauchen Administratorrechte und einen Testrechner.

## B. Detaillierter Modulaufbau

### Modul 1: Sicherungskonzept: RPO und RTO

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende RPO und RTO erklären und aus Anforderungen ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende die Wiederherstellungsdauer grob abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Sicherungsverfahren nach RPO wählen.
* **Voraussetzungen:** SQL-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Anforderungen | 3 |
| 1.2 | Verfahren | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Anforderungen (Einheit 1.1):** Führen Sie `bash konzept.sh` aus. Erklären Sie Schritt 1 und 2: Was bedeuten RPO und RTO, und wie ist die Dauer in Schritt 2 berechnet?
2. **Verfahren (Einheit 1.2):** Erklären Sie Schritt 3 und 4: Warum bekommt `shop` eine fortlaufende Protokollsicherung, und woher kommen die 7,0 GB je Tag?

#### Kontrollfragen

1. Was ist der RPO?
2. Was ist der RTO?
3. Warum ist die berechnete Dauer nur eine Untergrenze?
4. Sind die Regeln des Modells ein Standard?

### Modul 2: Logische Sicherung mit pg_dump und mariadb-dump

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Formate von `pg_dump` unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende nur Schema, nur Daten oder eine einzelne Tabelle sichern und zurückholen.
  * Nach Abschluss dieses Moduls kann der Lernende Optionen von `mariadb-dump` nutzen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Formate | 2 |
| 2.2 | Schema und Daten | 2 |
| 2.3 | MariaDB | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Formate (Einheit 2.1):** Führen Sie `bash logisch.sh` aus. Erklären Sie Schritt 1 und 2: Welche Formate entstehen, und was zeigt `pg_restore -l`?
2. **Schema und Daten (Einheit 2.2):** Erklären Sie Schritt 3 und 4: Wie trennen Sie Schema und Daten, und wie holen Sie nur eine Tabelle zurück?
3. **MariaDB (Einheit 2.3):** Erklären Sie Schritt 5 und 6: Was bewirken `--no-data`, `--where` und `--single-transaction`?

#### Kontrollfragen

1. Wann ist das Format Custom sinnvoll?
2. Was liefert `pg_restore -l`?
3. Was enthält ein Dump nicht?
4. Wann liefert `--single-transaction` einen konsistenten Stand?

### Modul 3: SQLite sichern

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende sichere Online-Sicherungen von SQLite erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende die Gefahr beim Kopieren einer geöffneten Datenbank zeigen.
  * Nach Abschluss dieses Moduls kann der Lernende Prüfsumme und `integrity_check` unterscheiden.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Sichere Methoden | 2 |
| 3.2 | Unsicheres Kopieren | 2 |
| 3.3 | Beschädigung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Sichere Methoden (Einheit 3.1):** Führen Sie `bash sqlite.sh` aus. Erklären Sie Schritt 1 bis 3: Wie arbeiten `.backup` und `VACUUM INTO`?
2. **Unsicheres Kopieren (Einheit 3.2):** Erklären Sie Schritt 4: Warum fehlen 100 Zeilen in der kopierten Hauptdatei?
3. **Beschädigung (Einheit 3.3):** Erklären Sie Schritt 5: Warum erkennt `integrity_check` die Änderung in der Mitte nicht, die Prüfsumme aber schon?

#### Kontrollfragen

1. Was ist der WAL-Modus?
2. Warum reicht Kopieren der Hauptdatei nicht?
3. Was prüft `integrity_check`?
4. Was erkennt eine Prüfsumme?

### Modul 4: Wiederherstellungstest

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherung in einer getrennten Instanz einspielen.
  * Nach Abschluss dieses Moduls kann der Lernende Zeilenzahl, Summe und Prüfsumme vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende abgeschnittene Sicherungen erkennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | PostgreSQL | 3 |
| 4.2 | Beschädigte Sicherung | 1 |
| 4.3 | MariaDB | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **PostgreSQL (Einheit 4.1):** Führen Sie `bash wiederherstellungstest.sh` aus. Erklären Sie Schritt 1 und 2: Warum nutzt der Vergleich eine Zeilenprüfsumme?
2. **Beschädigte Sicherung (Einheit 4.2):** Erklären Sie Schritt 3: Warum meldet `pg_restore -l` den Schaden nicht, das Einspielen aber schon?
3. **MariaDB (Einheit 4.3):** Erklären Sie Schritt 4 bis 6: Woran erkennen Sie einen abgeschnittenen MariaDB-Dump?

#### Kontrollfragen

1. Warum nie in die Produktion zurückspielen?
2. Warum reichen Anzahl und Summe nicht?
3. Wie erkennt man einen abgeschnittenen MariaDB-Dump?
4. Was gehört zur Dokumentation des Tests?

### Modul 5: Komprimierung, Verschlüsselung und Aufbewahrung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Sicherungen komprimieren und die Größen vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende mit `age` verschlüsseln und entschlüsseln.
  * Nach Abschluss dieses Moduls kann der Lernende eine Aufbewahrung nach Generationen berechnen.
* **Voraussetzungen:** Modul 2; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Komprimieren und Verschlüsseln | 2 |
| 5.2 | Entschlüsseln | 2 |
| 5.3 | Aufbewahrung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Komprimieren und Verschlüsseln (Einheit 5.1):** Führen Sie `bash verschluesselung_und_aufbewahrung.sh` aus. Erklären Sie Schritt 1 und 2: Warum steht in der verschlüsselten Datei kein `CREATE TABLE`?
2. **Entschlüsseln (Einheit 5.2):** Erklären Sie Schritt 3 und 4: Was zeigt die gleiche Prüfsumme, und was bewirkt der falsche Schlüssel?
3. **Aufbewahrung (Einheit 5.3):** Erklären Sie Schritt 5 und 6: Wie kommen 11 behaltene Dateien aus 120 zustande?

#### Kontrollfragen

1. Warum liegt der private Schlüssel nicht auf dem Sicherungsserver?
2. Was passiert ohne privaten Schlüssel?
3. Was bedeutet 7/4/3?
4. Sind die Fristen rechtlich geprüft?

### Modul 6: Sicherungsskript

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Sicherungsskript mit Sperrdatei und Rückgabecodes schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende unvollständige Dateien vermeiden.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler melden und Prüfsummen schreiben.
* **Voraussetzungen:** Modul 2; Modul 3; Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Lauf | 2 |
| 6.2 | Sperre | 2 |
| 6.3 | Fehlerfall | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Lauf (Einheit 6.1):** Führen Sie `bash sicherungsskript.sh` aus. Erklären Sie Schritt 1 und 2: Welche Dateien entstehen, und was prüft `sha256sum -c`?
2. **Sperre (Einheit 6.2):** Erklären Sie Schritt 3: Warum meldet der zweite Aufruf „läuft bereits“ und liefert den Rückgabecode 2?
3. **Fehlerfall (Einheit 6.3):** Erklären Sie Schritt 4 und 5: Warum bleibt keine halbe Datei zurück, und was gehört zur Einplanung?

#### Kontrollfragen

1. Wozu dient `flock`?
2. Warum erst in eine `.tmp`-Datei schreiben?
3. Welche Rückgabecodes nutzt das Skript?
4. Wurde `cron` ausgeführt?

### Modul 7: Offsite-Kopien und 3-2-1-Regel

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die 3-2-1-Regel auf einen Bestand anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen von Dateirechten für schreibgeschützte Kopien erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Rollen für Schreiben und Löschen trennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | 3-2-1 | 3 |
| 7.2 | Schutz vor Löschung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **3-2-1 (Einheit 7.1):** Führen Sie `bash offsite.sh` aus. Erklären Sie Schritt 1 und 2: Warum erfüllt `shop-db`, `buchhaltung` aber nicht die Regel?
2. **Schutz vor Löschung (Einheit 7.2):** Erklären Sie Schritt 3 und 4: Warum hilft `chmod 444` gegen den Administrator nicht, und welche Rollen sieht das Modell vor?

#### Kontrollfragen

1. Was bedeutet 3-2-1?
2. Warum umgeht root Dateirechte?
3. Was leistet eine Objektsperre?
4. Warum trennt man Schreib- und Löschrecht?

### Modul 8: Abschlussprojekt: Datenverlust messen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf Sicherung, Unfall, Wiederherstellung durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende verlorene Daten (RPO-Folge) zählen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wiederherstellungsdauer messen und bewerten.
* **Voraussetzungen:** Modul 2; Modul 4; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Ablauf | 2 |
| 8.2 | Wiederherstellung | 2 |
| 8.3 | Verbesserung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ablauf (Einheit 8.1):** Führen Sie `bash abschlussprojekt.sh` aus. Erklären Sie Schritt 1 bis 4: Welche Daten sind zum Zeitpunkt der Sicherung vorhanden, und welche kommen danach hinzu?
2. **Wiederherstellung (Einheit 8.2):** Erklären Sie Schritt 5 und 6: Wie viele Bestellungen sind verloren, und was sagt das über den RPO?
3. **Verbesserung (Einheit 8.3):** Schreiben Sie einen Bericht mit Verbesserungsvorschlägen aus Schritt 7 und mit den offenen Punkten.

#### Kontrollfragen

1. Warum gehen 40 Bestellungen verloren?
2. Was verringert den Verlust?
3. Warum wird die Sekundenzahl nicht festgehalten?
4. Was gehört in den Bericht?
