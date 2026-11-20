# Lehrplan: NoSQL-Datenbanken und Redis

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Datenbankgrundlagen (Tabellen, Abfragen); Linux-Grundlagen (Kommandozeile); Grundbegriffe der Netzwerksicherheit |
| **Gesamtumfang** | 8 Module, 45 UE (zu 45 Minuten; 33,75 Stunden) |
| **Fokus-Technologien** | NoSQL-Arten im Überblick, Redis (Datentypen, Ablaufzeiten, Persistenz mit RDB und AOF, Replikation, Absicherung mit Kennwort und ACL, Transaktionen, Speichergrenze), Dokumentenmodell als Vergleich |
| **Thematische Abgrenzung (Out of Scope)** | Redis wird real ausgeführt (Version 7.0.15 aus den Paketquellen von Ubuntu 24.04). **MongoDB wird nicht ausgeführt**: Das Dokumentenmodell wird an einem kleinen Python-Modell gezeigt, die Beispielbefehle sind Text. Nicht behandelt: Redis Cluster, Sentinel, TLS, Module, Streams, Cassandra, Graphdatenbanken. Lizenz und Version von Redis und MongoDB: mit Stand prüfen (siehe Quellen) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | NoSQL-Überblick und Redis-Start | 1 | 5 |
| 2 | Redis-Datentypen | 1 | 6 |
| 3 | Ablaufzeiten und Zwischenspeicher | 1 | 5 |
| 4 | Persistenz mit RDB und AOF | 1 | 6 |
| 5 | Replikation | 1 | 6 |
| 6 | Absicherung von Redis | 1 | 6 |
| 7 | Dokumentenmodell (Vergleich) | 2 | 5 |
| 8 | Transaktionen, Speicher und Betrieb | 1 | 6 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **45** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Dokumentenmodell). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 40 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Redis und MongoDB wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden durch Läufe im Test-Container bestätigt. **Lizenz:** Eine Websuche zeigte nur Schlagzeilen (Artikel nicht geöffnet), nach denen Redis 8 im Jahr 2025 wieder unter einer Open-Source-Lizenz (AGPLv3) angeboten wird, zum Beispiel [The Register](https://www.theregister.com/2025/05/01/redis_returns_to_open_source/) und [Redis-Blog](https://redis.io/blog/agplv3/). Für die getestete Version 7.0.15 und für andere Versionen wurde die Lizenz **nicht** geprüft. Daten sind erfunden.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** Redis 7.0.15 (`redis-server`, `redis-cli`), Python 3, Bash. **Nicht ausgeführt:** MongoDB, Redis Cluster oder Sentinel, TLS, Windows.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-NoSQL`, `10.67.0.0/24`).

**VM 1:** `redis01` (**erforderlich**, `10.67.0.2`): Linux-Server mit Redis (Paket der Distribution).

**VM 2:** `redis02` (**erforderlich** ab Modul 5, `10.67.0.3`): zweiter Redis-Server als Replikat. Optional: `mongo01` für Modul 7 (nicht Teil der geprüften Übungen).

**Internetphase:** Für die Installation der Pakete brauchen die VMs vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 4 von `redis01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte starten Redis selbst auf `127.0.0.1` (Ports 6399 und 6400) und räumen am Ende auf; sie brauchen keine Rechte.

## B. Detaillierter Modulaufbau

### Modul 1: NoSQL-Überblick und Redis-Start

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende NoSQL-Arten nennen und vom relationalen Modell abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Redis-Server starten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Schlüssel setzen, lesen, suchen und löschen.
* **Voraussetzungen:** Datenbankgrundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Start | 3 |
| 1.2 | Schlüssel | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Start (Einheit 1.1):** Führen Sie `bash start.sh` aus. Erklären Sie Schritt 1 und 2: Wie prüfen Sie Version und Erreichbarkeit, und was bedeutet `redis_mode:standalone`?
2. **Schlüssel (Einheit 1.2):** Erklären Sie Schritt 3 und 4: Warum nutzt man in Betrieb `SCAN` statt `KEYS`, und was liefern `DEL` und `EXISTS`?

#### Kontrollfragen

1. Was ist das Schlüssel-Wert-Modell?
2. Warum Doppelpunkte in Schlüsselnamen?
3. Was liefert `PING`?
4. Wann ist Redis gegenüber SQL ungeeignet?

### Modul 2: Redis-Datentypen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zeichenketten, Listen, Hashes, Mengen und sortierte Mengen verwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Zähler atomar erhöhen.
  * Nach Abschluss dieses Moduls kann der Lernende Typfehler erkennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Zähler und Liste | 2 |
| 2.2 | Hash und Menge | 2 |
| 2.3 | Rangliste und Fehler | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zähler und Liste (Einheit 2.1):** Führen Sie `bash datentypen.sh` aus. Erklären Sie Schritt 1 und 2: Welche Ergebnisse liefern `INCR`, `INCRBY`, `RPUSH`, `LPOP`?
2. **Hash und Menge (Einheit 2.2):** Erklären Sie Schritt 3 und 4: Was liefern `HGETALL`, `SINTER` und `SUNION`?
3. **Rangliste und Fehler (Einheit 2.3):** Erklären Sie Schritt 5 und 6: Wie funktioniert die sortierte Menge, und warum erscheint `WRONGTYPE`?

#### Kontrollfragen

1. Warum ist `INCR` atomar?
2. Welcher Typ passt für ein Benutzerprofil?
3. Was passiert beim Hinzufügen eines vorhandenen Elements zu einer Menge?
4. Wie wird eine sortierte Menge geordnet?

### Modul 3: Ablaufzeiten und Zwischenspeicher

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ablaufzeiten setzen, lesen und aufheben.
  * Nach Abschluss dieses Moduls kann der Lernende das Muster Cache-Aside erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Wirkung von `SET` auf den Ablauf kennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | TTL | 3 |
| 3.2 | Cache und Überschreiben | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **TTL (Einheit 3.1):** Führen Sie `bash ablauf.sh` aus. Erklären Sie Schritt 1 bis 4: Was bedeuten die Werte -1 und -2, und was passiert nach dem Ablauf?
2. **Cache und Überschreiben (Einheit 3.2):** Erklären Sie Schritt 5 und 6: Wie arbeitet das Cache-Muster, und warum entfällt der Ablauf bei `SET` ohne `EX`?

#### Kontrollfragen

1. Was liefert `TTL` bei einem Schlüssel ohne Ablauf?
2. Was liefert `TTL` bei einem nicht vorhandenen Schlüssel?
3. Was bewirkt `PERSIST`?
4. Was ist Cache-Aside?

### Modul 4: Persistenz mit RDB und AOF

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Datenverlust ohne Persistenz zeigen.
  * Nach Abschluss dieses Moduls kann der Lernende RDB-Abbild und AOF-Protokoll unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten bei hartem Prozessende beschreiben.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Ohne Persistenz | 2 |
| 4.2 | RDB | 2 |
| 4.3 | AOF | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ohne Persistenz (Einheit 4.1):** Führen Sie `bash persistenz.sh` aus. Erklären Sie Schritt 1: Was passiert mit den Daten beim Neustart?
2. **RDB (Einheit 4.2):** Erklären Sie Schritt 2 und 3: Welche Daten überleben, welche nicht, und warum?
3. **AOF (Einheit 4.3):** Erklären Sie Schritt 4 und 5: Was steht im Protokoll, und warum ist x nach dem harten Ende 2?

#### Kontrollfragen

1. Wann ist RDB ausreichend?
2. Was bewirkt `appendfsync always`?
3. Ersetzt Persistenz die Datensicherung?
4. Warum fehlt c nach dem harten Ende?

### Modul 5: Replikation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Replikat einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Schreibschutz-Fehlermeldung erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Übernahme von Hand durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen der Replikation nennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Verbinden | 2 |
| 5.2 | Lesen und Schreiben | 2 |
| 5.3 | Ausfall und Übernahme | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verbinden (Einheit 5.1):** Führen Sie `bash replikation.sh` aus. Erklären Sie Schritt 1: Woran erkennt man `role` und `master_link_status`?
2. **Lesen und Schreiben (Einheit 5.2):** Erklären Sie Schritt 2 und 3: Welche Wirkung hat ein Schreibvorgang an der Hauptinstanz, und warum scheitert er am Replikat?
3. **Ausfall und Übernahme (Einheit 5.3):** Erklären Sie Schritt 4 bis 6: Was bewirkt `REPLICAOF NO ONE`, und welche Risiken bleiben?

#### Kontrollfragen

1. Warum ist das Replikat schreibgeschützt?
2. Was bedeutet asynchron?
3. Ersetzt die Replikation eine Sicherung?
4. Warum startet die Hauptinstanz mit `repl-diskless-sync-delay 0`?

### Modul 6: Absicherung von Redis

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Bindung an Adressen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Kennwort setzen und die Wirkung zeigen.
  * Nach Abschluss dieses Moduls kann der Lernende ACL-Benutzer mit eingeschränkten Rechten anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Hinweise zu Kennwörtern im Argument beachten.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Bindung und Kennwort | 2 |
| 6.2 | ACL-Benutzer | 2 |
| 6.3 | Rechte lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bindung und Kennwort (Einheit 6.1):** Führen Sie `bash sicherheit.sh` aus. Erklären Sie Schritt 1 und 2: Was bedeutet `bind 127.0.0.1`, und was liefert `NOAUTH`?
2. **ACL-Benutzer (Einheit 6.2):** Erklären Sie Schritt 3: Welche Befehle und Schlüssel darf `leser`, und welche Fehler erscheinen sonst?
3. **Rechte lesen (Einheit 6.3):** Lesen Sie Schritt 4 und formulieren Sie die Rechte von `leser` in einem Satz.

#### Kontrollfragen

1. Warum nicht an alle Adressen binden?
2. Was bedeutet `NOPERM`?
3. Warum ist `--pass` im Argument riskant?
4. Wurde TLS getestet?

### Modul 7: Dokumentenmodell (Vergleich)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Dokumentenmodell vom relationalen Modell abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Suchen und Änderungen an verschachtelten Feldern verstehen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen des Modells benennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Modell lesen | 3 |
| 7.2 | Projektion und Ändern | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Modell lesen (Einheit 7.1):** Führen Sie `bash dokumente.sh` aus. Erklären Sie Schritt 1 und 2: Warum haben die Dokumente verschiedene Felder, und welche Suchen liefern welche Namen?
2. **Projektion und Ändern (Einheit 7.2):** Erklären Sie Schritt 3 bis 5: Was bedeutet `adresse.plz`, und warum liefert der unbekannte Operator einen Fehler?

#### Kontrollfragen

1. Was ist ein Dokument?
2. Was bedeutet `adresse.plz`?
3. Wurde MongoDB getestet?
4. Wo sind Dokumentdatenbanken schwächer?

### Modul 8: Transaktionen, Speicher und Betrieb

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende MULTI/EXEC einsetzen und Fehler erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Pub/Sub als Nachrichtenkanal zeigen.
  * Nach Abschluss dieses Moduls kann der Lernende Speichergrenze und Verdrängungsrichtlinie einstellen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abschlussprojekt planen.
* **Voraussetzungen:** Modul 3; Modul 4; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Transaktion und Pub/Sub | 2 |
| 8.2 | Speichergrenze | 2 |
| 8.3 | Abschlussprojekt | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Transaktion und Pub/Sub (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1 bis 3: Warum ergibt die Überweisung 70 und 30, und was bewirkt der unbekannte Befehl?
2. **Speichergrenze (Einheit 8.2):** Erklären Sie Schritt 4 bis 6: Was bewirken `allkeys-lru` und `noeviction`, und was zeigt der Slowlog?
3. **Abschlussprojekt (Einheit 8.3):** Bearbeiten Sie die Aufgabenliste aus Schritt 7 und schreiben Sie einen Bericht mit offenen Punkten.

#### Kontrollfragen

1. Was bewirkt `MULTI`/`EXEC`?
2. Was bewirkt `allkeys-lru`?
3. Was bewirkt `noeviction`?
4. Was ist Pub/Sub?
