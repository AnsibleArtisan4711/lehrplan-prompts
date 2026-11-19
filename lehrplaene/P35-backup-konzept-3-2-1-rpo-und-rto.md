# Lehrplan: Backup-Konzept (3-2-1, RPO und RTO)

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Grundkenntnisse in Linux (Shell, Dateisystem) und Windows Server (Datenträger, PowerShell-Grundlagen); keine Backup-Software erforderlich |
| **Gesamtumfang** | 13 Module, 116 UE (zu 45 Minuten; 87 Stunden) |
| **Fokus-Technologien** | Konzeptionelle Grundlagen (RPO, RTO, 3-2-1-1-0, Sicherungsarten, Aufbewahrung), praktische Umsetzung mit Bordmitteln (`tar`, `rsync`, `robocopy`, `wbadmin`) und `restic`, Verschlüsselung (`gpg`, `openssl`, restic), unveränderliche Kopien, Restore-Tests, Konsistenz von Datenbanken (SQLite als Beispiel), Dokumentation eines Backup-Konzepts |
| **Thematische Abgrenzung (Out of Scope)** | Keine Produkt-Schulung zu Veeam und anderen Kommerzprodukten (siehe Veeam-Übung im selben Repository), keine Notfallplanung und Wiederanlauf-Reihenfolge (siehe Lehrplan P36), keine Cloud-Backup-Dienste, keine Bandtechnik, keine Hardware-RAID-Konfiguration |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Grundlagen: Warum Backup, Schutzziele und Ursachen für Datenverlust | 1 | 6 |
| 2 | RPO und RTO: Ziele festlegen und prüfen | 1 | 9 |
| 3 | Die 3-2-1-Regel und 3-2-1-1-0 | 1 | 8 |
| 4 | Sicherungsarten: voll, inkrementell, differenziell | 1 | 9 |
| 5 | Linux: versionierte Sicherung mit rsync und Hardlinks | 1 | 10 |
| 6 | Windows: Sicherung mit wbadmin und robocopy | 1 | 10 |
| 7 | restic: verschlüsselte, deduplizierende Sicherung | 1 | 10 |
| 8 | Aufbewahrung: Großvater-Vater-Sohn und Löschregeln | 1 | 8 |
| 9 | Verschlüsselung von Sicherungen und Schlüsselverwaltung | 1 | 8 |
| 10 | Unveränderbare Kopien und Schutz vor Ransomware | 1 | 9 |
| 11 | Restore-Tests, Prüfsummen und Fehlersuche | 1 | 10 |
| 12 | Datenbanken konsistent sichern (SQLite als Beispiel) | 2 | 6 |
| 13 | Backup-Konzept dokumentieren, überwachen und berichten | 1 | 13 |
| **Gesamt** | 13 Module | 12 × Priorität 1, 1 × Priorität 2 | **116** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 12 (Datenbanken). Fällt Modul 12 weg, verringert sich der Gesamtumfang auf 110 UE.

### 2. Quellen

Geprüft (auf Microsoft Learn am 19.11.2026 gelesen): Befehlsreferenzen zu `wbadmin` (Unterbefehle `start backup`, `get versions`, `get items`, `start recovery`, `start systemstatebackup`) und `robocopy` (Optionen `/MIR`, `/L`, `/R`, `/W`, `/LOG`, `/NP`, `/B`, `/ZB`, `/MT`) sowie `vssadmin` und `diskshadow`. Die Aufrufe der Linux-Werkzeuge (`tar`, `rsync`, `restic`, `gpg`, `openssl`, `sqlite3`, `chattr`) wurden nicht gegen Handbücher gelesen, sondern im Labor ausgeführt (Versionen: restic 0.16.4, rsync 3.2.7, tar 1.35, gpg 2.4.4, openssl 3.0.13, Python 3.13, SQLite 3.45.1). Für die Regel „3-2-1“ und die Erweiterung „3-2-1-1-0“, für Normen (z. B. ISO/IEC 27001) und Empfehlungen des BSI gibt es **keine geprüfte Quelle**; die Aussagen sind Fachwissen und mit „nicht bestätigt“ gekennzeichnet. Es werden keine Versionsnummern von Windows Server behauptet, die nicht auf Microsoft Learn gelesen wurden.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V (Windows Server oder Windows 11 Pro) auf dem Hostsystem; alternativ lassen sich die Linux-Module (2 bis 5, 7 bis 13) auf einer beliebigen Debian- oder Ubuntu-Maschine durchführen.

**VMs:** `srv-win01` (Windows Server, Standard mit Desktopdarstellung, 4 GB RAM, drei virtuelle Platten: Systemplatte, `E:` als Sicherungsziel, `F:` als „Offline“-Kopie), `srv-lin01` (Debian 12, 2 GB RAM, Quelle der Daten) und `bkp01` (Debian 12, 2 GB RAM, Sicherungsziel über SSH).

**Netz:** privater Switch `Lab-Internal-Net`, Adressbereich `192.168.10.0/24` (statisch, ohne DHCP und DNS), Namensauflösung über `/etc/hosts` bzw. `hosts`-Datei, Domäne bzw. Zone `labor.example.internal`. Kein Zugriff aufs Internet während der Übungen.

**Internetphase:** Vor Kursbeginn einmalig (Zugriff aufs Internet erlaubt): Pakete `restic`, `rsync`, `gnupg`, `sqlite3`, `openssh-server`, `python3` auf `srv-lin01` und `bkp01` installieren; in Debian 12 ist die restic-Version vermutlich älter als die im Labor verwendete (nicht bestätigt), die Übungen nutzen nur Befehle, die in beiden Versionen vorkommen. Danach Internet trennen.

**Zugangsdaten:** Kennwörter und Schlüssel sind Laborwerte und werden vom Lernenden selbst vergeben; echte Kennwörter gehören nicht in Übungen. **Ausgangszustand je Modul:** Prüfpunkt der VMs anlegen (Hyper-V-Prüfpunkt); **Rückbau:** Prüfpunkt wiederherstellen oder die Arbeitsordner `~/backup/mNN` löschen und `chattr -R -i` auf geschützte Ordner anwenden (Modul 10).

**Hinweis zur Testumgebung der Ausarbeitung:** Das Labor wurde nicht in Hyper-V aufgebaut; die Linux-Skripte wurden in einem Cloud-Container ausgeführt, das Windows-Skript nur auf Syntaxfehler geprüft.

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen: Warum Backup, Schutzziele und Ursachen für Datenverlust

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende vier Ursachen für Datenverlust nennen und je eine passende Schutzmaßnahme zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Backup, Archiv, Replikation und RAID voneinander abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Schutzziele auf ein Backup anwenden und zwei typische Konzeptfehler benennen.
* **Voraussetzungen:** Keine; Grundverständnis von Servern und Dateien.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Ursachen für Datenverlust (Hardwaredefekt, Bedienfehler, Schadsoftware, Brand, Diebstahl), Abgrenzung Backup, Archiv, Replikation und RAID | 2 |
| 1.2 | Schutzziele Verfügbarkeit, Integrität, Vertraulichkeit im Backup-Kontext; Begriffe Sicherung, Wiederherstellung, Aufbewahrung | 2 |
| 1.3 | Fallstudie: Ausfall ohne Konzept und typische Fehler (nie getestet, Sicherung am selben Ort) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ursachen und Gegenmaßnahmen (Einheit 1.1):** Ordnen Sie den Ursachen „Festplattendefekt“, „versehentliches Löschen“, „Ransomware“, „Brand im Serverraum“ je eine Gegenmaßnahme zu und begründen Sie in einem Satz, warum RAID allein jeweils nicht genügt.
2. **Begriffe abgrenzen (Einheit 1.2):** Erstellen Sie eine Tabelle mit den Spalten „Backup“, „Archiv“, „Replikation“, „RAID“ und den Zeilen „schützt vor Hardwaredefekt“, „schützt vor Löschen oder Verschlüsseln“, „enthält ältere Stände“. Tragen Sie ja, nein oder bedingt ein und begründen Sie die Einträge mit „bedingt“.
3. **Fallstudie auswerten (Einheit 1.3):** Lesen Sie die Fallstudie im Hinweisteil der Übung (Firma ohne getestetes Backup). Nennen Sie drei Fehler im Vorgehen und je eine Maßnahme, die ihn verhindert hätte.

#### Kontrollfragen

1. Warum ist RAID kein Ersatz für ein Backup?
2. Wodurch unterscheidet sich eine Replikation von einem Backup, wenn eine Datei versehentlich gelöscht wird?
3. Welches Schutzziel ist bei einem verschlüsselten, aber nie getesteten Backup besonders gefährdet?
4. Nennen Sie zwei Gründe, warum ein Backup auf derselben Platte wie die Quelle kaum schützt.

### Modul 2: RPO und RTO: Ziele festlegen und prüfen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende RPO und RTO definieren und an einem Beispiel unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende aus Sicherungsintervall und Datenmenge den schlimmsten Datenverlust und die Wiederherstellungsdauer abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Ziel-Soll-Ist-Ergebnis lesen und eine Maßnahme für verfehlte Ziele vorschlagen.
* **Voraussetzungen:** Modul 1; Python 3 auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Definition RPO (tolerierbarer Datenverlust) und RTO (tolerierbare Ausfallzeit); Unterschied zu Maximaler Ausfallzeit | 2 |
| 2.2 | Ziele aus Geschäftsprozessen ableiten und mit Sicherungsintervall und Wiederherstellungsdauer abgleichen | 3 |
| 2.3 | Praxis: Skript `rpo_rto.py` auf eine Systemliste anwenden, Ergebnis deuten | 3 |
| 2.4 | Maßnahmen bei verfehlten Zielen (Intervall verkürzen, Bandbreite, Priorisierung) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ziele erklären (Einheit 2.1):** Erklären Sie RPO und RTO für den Dateiserver FS01 (nächtliche Sicherung um 02:00 Uhr, Ausfall um 16:00 Uhr) in je zwei Sätzen und nennen Sie den tatsächlichen Datenverlust.
2. **Skript ausführen (Einheit 2.3):** Führen Sie `python3 rpo_rto.py systeme.csv` aus, lesen Sie die Tabelle und nennen Sie die Systeme, die ein Ziel verfehlen, mit der Spalte, die den Fehler verursacht.
3. **Daten ändern (Einheit 2.3):** Ändern Sie in `systeme.csv` das Sicherungsintervall der ERP-Datenbank so, dass das RPO erreicht wird, und führen Sie das Skript erneut aus. Notieren Sie, welche Auswirkung die Änderung auf den Betrieb hat (Last, Platzbedarf).
4. **Maßnahme vorschlagen (Einheit 2.4):** Für MAIL01 ist das RTO nicht erreichbar, weil die Wiederherstellung zu lange dauert. Nennen Sie zwei Maßnahmen und bewerten Sie jeweils Kosten und Wirkung.

#### Kontrollfragen

1. Wie groß kann der Datenverlust im schlimmsten Fall bei einer nächtlichen Sicherung sein?
2. Warum ist die Wiederherstellungsdauer meist länger als die Sicherungsdauer?
3. Welche Bestandteile hat die Zeit bis zum wieder nutzbaren System neben dem Kopieren der Daten?
4. Wodurch unterscheiden sich RPO und RTO in dem, was sie begrenzen?

### Modul 3: Die 3-2-1-Regel und 3-2-1-1-0

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Regel 3-2-1 und ihre Erweiterung anhand eines Kopienbestands anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende aus einer Bestandsliste erkennen, welche Teilregel verletzt ist.
  * Nach Abschluss dieses Moduls kann der Lernende eine kostenbewusste Zielarchitektur für ein kleines Unternehmen skizzieren.
* **Voraussetzungen:** Module 1 und 2; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Regel 3-2-1: drei Kopien, zwei Medientypen, eine Kopie an anderem Ort; Zählweise und typische Missverständnisse | 2 |
| 3.2 | Erweiterung 3-2-1-1-0: eine Kopie offline oder unveränderlich, null Fehler beim Restore-Test | 2 |
| 3.3 | Praxis: Skript `dreizweieins.py` auf einen Kopienbestand anwenden und Lücken schließen | 3 |
| 3.4 | Kosten-Nutzen: Kopien, Medien und Orte für ein kleines Unternehmen auswählen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regel zählen (Einheit 3.1):** Ein Dateiserver hat Produktivdaten, eine nächtliche Kopie auf eine zweite Platte im selben Server und eine wöchentliche USB-Kopie im Serverraum. Prüfen Sie die Regel 3-2-1 und benennen Sie die verletzten Teile.
2. **Skript anwenden (Einheit 3.3):** Führen Sie `python3 dreizweieins.py kopien.csv` aus und beschreiben Sie je System, welche Teilregeln erfüllt sind.
3. **Lücken schließen (Einheit 3.3):** Ändern Sie `kopien.csv` so, dass das System mit den meisten Verstößen alle Teilregeln erfüllt, und erklären Sie jede Änderung mit Kosten und Aufwand.
4. **Zielarchitektur (Einheit 3.4):** Skizzieren Sie für eine Firma mit 20 Arbeitsplätzen, einem Dateiserver und einer Datenbank eine Architektur nach 3-2-1-1-0 (Quelle, Ziele, Medien, Orte) mit einer Kostenschätzung als Größenordnung.

#### Kontrollfragen

1. Zählt die Produktivkopie bei „3 Kopien“ mit?
2. Warum genügt „zwei Platten“ nicht als „zwei Medientypen“, wenn beide im selben Server stecken?
3. Was bedeutet die „1“ für offline oder unveränderlich in 3-2-1-1-0, und gegen welche Bedrohung hilft sie?
4. Was bedeutet die „0“ in 3-2-1-1-0, und wie stellt man sie fest?

### Modul 4: Sicherungsarten: voll, inkrementell, differenziell

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die drei Sicherungsarten voneinander abgrenzen und die benötigte Wiederherstellungskette angeben.
  * Nach Abschluss dieses Moduls kann der Lernende mit `tar --listed-incremental` eine Vollsicherung und zwei inkrementelle Sicherungen erzeugen und zurückspielen.
  * Nach Abschluss dieses Moduls kann der Lernende die Folgen eines Kettenbruchs benennen.
* **Voraussetzungen:** Module 2 und 3; GNU tar und bash auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Vollsicherung, inkrementelle und differenzielle Sicherung; Archivbit, Zeitstempel und Änderungsliste | 2 |
| 4.2 | Rechenmodell: Platzbedarf, Sicherungsdauer und Wiederherstellungskette im Vergleich | 2 |
| 4.3 | Praxis: Sicherungskette mit GNU `tar --listed-incremental` erstellen und zurückspielen | 4 |
| 4.4 | Synthetische Vollsicherung und Konsequenzen für die Kette (Überblick) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kette bestimmen (Einheit 4.1):** Für eine Vollsicherung am Sonntag und tägliche Sicherungen: Welche Sicherungen braucht man für die Wiederherstellung am Donnerstag bei inkrementeller und bei differenzieller Sicherung?
2. **Rechenmodell (Einheit 4.2):** Führen Sie `python3 sicherungsarten.py` aus und vergleichen Sie Platzbedarf und Anzahl der Wiederherstellungsschritte. Nennen Sie je einen Vor- und Nachteil für jede Art.
3. **Kette mit tar (Einheit 4.3):** Führen Sie `bash inkrementell.sh` aus und lesen Sie jeden Schritt: Vollsicherung, Änderung, Sicherung 1, Löschen und Ändern, Sicherung 2. Stellen Sie danach in der richtigen Reihenfolge wieder her und vergleichen Sie mit dem Stand zum Zeitpunkt der letzten Sicherung.
4. **Kettenbruch (Einheit 4.3):** Löschen Sie in einer Kopie der Übung die erste inkrementelle Sicherung und stellen Sie die zweite wieder her. Beschreiben Sie, was passiert und was daraus für Aufbewahrung folgt.

#### Kontrollfragen

1. Wie viele Archive braucht man bei inkrementeller Sicherung am vierten Tag nach der Vollsicherung?
2. Warum wächst die differenzielle Sicherung von Tag zu Tag?
3. Wozu dient die „snar“-Datei (Snapshot-Datei) von GNU tar?
4. Was geschieht mit Dateien, die zwischen zwei Sicherungen gelöscht wurden, bei der Wiederherstellung mit `--listed-incremental`?

### Modul 5: Linux: versionierte Sicherung mit rsync und Hardlinks

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende mit rsync `--link-dest` versionierte Sicherungen anlegen und den Platzbedarf erklären.
  * Nach Abschluss dieses Moduls kann der Lernende am Hardlink-Zähler erkennen, ob eine Datei geändert wurde.
  * Nach Abschluss dieses Moduls kann der Lernende Rückgabewerte von rsync einordnen und einen unvollständigen Lauf erkennen.
* **Voraussetzungen:** Modul 4; rsync und bash auf `srv-lin01`, Ziel auf einem Dateisystem mit Hardlinks.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | rsync: Optionen `-a`, `--delete`, `--link-dest`, `-n`, `--stats`, `-i`; Quick-Check über Größe und Zeitstempel | 3 |
| 5.2 | Prinzip der Hardlink-Snapshots: jede Sicherung ein vollständiger Baum, geringer Platzbedarf | 2 |
| 5.3 | Praxis: Skript `backup_linux.sh` ausführen, drei Tage simulieren, Ergebnisse messen (Links, Platz) | 3 |
| 5.4 | Fehlerbehandlung: Teilsicherung (`.partial`), Rückgabewerte 23 und 24, Protokoll | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Trockenlauf (Einheit 5.1):** Führen Sie `rsync -ain --delete QUELLE/ ZIEL/` aus und lesen Sie die Ausgabe mit den Änderungsmarken (`>f+++++++++` für neue Datei). Erklären Sie die ersten beiden Zeichen.
2. **Drei Tage simulieren (Einheit 5.3):** Führen Sie `bash demo_snapshots.sh` aus. Es legt drei Sicherungen an (Erstsicherung, 5 geänderte und 1 neue Datei, 1 gelöschte Datei). Notieren Sie je Sicherung `du -sh` einzeln und für alle zusammen.
3. **Hardlinks lesen (Einheit 5.2):** Vergleichen Sie mit `stat -c "%h %i"` den Hardlink-Zähler einer unveränderten und einer geänderten Datei und erklären Sie den Unterschied.
4. **Gelöschte Datei (Einheit 5.3):** Stellen Sie die am Tag 3 gelöschte Datei aus der Sicherung von Tag 2 wieder her und zeigen Sie, dass sie in Tag 3 fehlt.
5. **Fehlerfall (Einheit 5.4):** Brechen Sie einen Lauf ab (Strg+C) und zeigen Sie, dass nur ein Ordner `.partial` entsteht und `latest` auf die letzte vollständige Sicherung zeigt.

#### Kontrollfragen

1. Warum belegen drei vollständige Sicherungen kaum mehr Platz als eine?
2. Wie erkennt man an der Linkanzahl, ob eine Datei zwischen zwei Sicherungen geändert wurde?
3. Was bedeutet der rsync-Rückgabewert 24, und warum zählt das Skript ihn als Erfolg?
4. Was kann passieren, wenn zwei Änderungen einer Datei innerhalb derselben Sekunde und mit gleicher Größe erfolgen?

### Modul 6: Windows: Sicherung mit wbadmin und robocopy

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherung mit `wbadmin start backup` planen und die vorhandenen Sicherungen mit `get versions` anzeigen.
  * Nach Abschluss dieses Moduls kann der Lernende mit `robocopy` im Trockenlauf prüfen, was kopiert oder gelöscht würde, und die Rückgabewerte deuten.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle der Schattenkopien für konsistente Sicherungen erklären.
* **Voraussetzungen:** Modul 4; `srv-win01` mit den zusätzlichen Platten `E:` und `F:`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Windows Server Backup: Unterbefehle von `wbadmin` (`start backup`, `get versions`, `get items`, `start recovery`, `start systemstatebackup`) | 3 |
| 6.2 | `robocopy` für Dateikopien: Optionen `/E`, `/MIR`, `/L`, `/R`, `/W`, `/LOG`, `/NP`, Rückgabewerte | 3 |
| 6.3 | Skript `sicherung_windows.ps1`: Trockenlauf, Prüfungen und Protokoll | 2 |
| 6.4 | Schattenkopien (VSS) und Konsistenz: `vssadmin`, `diskshadow` (Überblick) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Trockenlauf (Einheit 6.3):** Führen Sie `.\sicherung_windows.ps1` ohne Schalter aus und lesen Sie die ausgegebenen Befehle und den robocopy-Trockenlauf (`/L`). Welche Dateien würden kopiert?
2. **Sicherung ausführen (Einheit 6.1):** Fügen Sie `-Ausfuehren` hinzu, sichern Sie `D:\Daten` mit wbadmin nach `E:` und per robocopy nach `F:\Kopie`. Prüfen Sie mit `wbadmin get versions` die Sicherung.
3. **Rückgabewerte (Einheit 6.2):** Ändern Sie eine Datei und führen Sie robocopy erneut aus. Notieren Sie den Rückgabewert und ordnen Sie ihn mit der Dokumentation (Werte 0 bis 7 Erfolg, ab 8 Fehler) ein.
4. **Schattenkopien (Einheit 6.4):** Zeigen Sie mit `vssadmin list writers` und `vssadmin list providers` die Komponenten für konsistente Sicherung. Beschreiben Sie in zwei Sätzen, wozu ein Writer dient.

#### Kontrollfragen

1. Wozu dient `robocopy /L`, und warum sollte man vor `/MIR` immer einen Trockenlauf machen?
2. Was bewirkt die Option `/MIR` bei Dateien, die im Ziel, aber nicht mehr in der Quelle vorhanden sind?
3. Welcher Unterbefehl von `wbadmin` zeigt die vorhandenen Sicherungen an?
4. Warum soll das wbadmin-Ziel nicht dasselbe Laufwerk wie die Quelle sein?

### Modul 7: restic: verschlüsselte, deduplizierende Sicherung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein restic-Repository anlegen, Sicherungen erstellen und Snapshots lesen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum eine unveränderte zweite Sicherung kaum Platz benötigt.
  * Nach Abschluss dieses Moduls kann der Lernende eine Wiederherstellung durchführen und mit Prüfsummen gegen das Original vergleichen.
* **Voraussetzungen:** Module 4 und 5; restic auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Repository, Snapshot, Deduplizierung und Verschlüsselung; `restic init`, `backup`, `snapshots` | 3 |
| 7.2 | Vergleich von Ständen: `diff`, `stats`, Aufbau des Repositorys | 2 |
| 7.3 | Wiederherstellen: `restore` und Prüfung gegen das Original | 3 |
| 7.4 | Typische Fehler: falsches Kennwort, `check`, Sperren (Locks) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Repository und Sicherungen (Einheit 7.1):** Führen Sie `bash restic_demo.sh` aus. Lesen Sie die Ausgabe der drei Sicherungen: wie viele Dateien sind neu, geändert oder unverändert, wie viel wird hinzugefügt?
2. **Stände vergleichen (Einheit 7.2):** Nutzen Sie `restic diff` zwischen Sicherung 1 und 2 und nennen Sie die geänderten Dateien.
3. **Wiederherstellung prüfen (Einheit 7.3):** Stellen Sie den letzten Stand in einen neuen Ordner wieder her und vergleichen Sie per `sha256sum` mit dem Original.
4. **Fehlerbild (Einheit 7.4):** Rufen Sie `restic snapshots` mit falschem Kennwort auf und notieren Sie Meldung und Rückgabewert.

#### Kontrollfragen

1. Warum fügt die dritte Sicherung ohne Änderungen 0 Byte hinzu, obwohl ein neuer Snapshot entsteht?
2. Was passiert mit den Daten im Repository, wenn das Kennwort verloren geht?
3. Wozu dient `restic check`, und was prüft es ohne `--read-data` nicht?
4. Warum sollte man eine Wiederherstellung immer in einen neuen, leeren Ordner testen?

### Modul 8: Aufbewahrung: Großvater-Vater-Sohn und Löschregeln

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine GFS-Aufbewahrungsregel formulieren und ihre Wirkung simulieren.
  * Nach Abschluss dieses Moduls kann der Lernende mit `restic forget --dry-run` prüfen, was gelöscht würde, bevor `--prune` Platz freigibt.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Löschen von Sicherungen eine kontrollierte, geprüfte Handlung ist.
* **Voraussetzungen:** Modul 7; Python 3 und restic auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Aufbewahrungsfristen, Speicherbedarf und das Schema Großvater-Vater-Sohn (täglich, wöchentlich, monatlich) | 2 |
| 8.2 | Simulation: `gfs.py` mit verschiedenen Regeln, Rechnung zum Platzbedarf | 3 |
| 8.3 | restic: `forget --dry-run`, `--keep-daily/-weekly/-monthly`, `--prune` | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regel simulieren (Einheit 8.2):** Führen Sie `python3 gfs.py 400 7 4 12` aus. Wie viele der 400 täglichen Sicherungen werden behalten, und wie weit reicht der älteste behaltene Stand zurück?
2. **Regel ändern (Einheit 8.2):** Wiederholen Sie mit `7 4 3` (nur drei Monate). Vergleichen Sie Anzahl und ältesten Stand und beurteilen Sie die Folgen für eine Aufbewahrungsvorgabe von einem Jahr.
3. **Trockenlauf mit restic (Einheit 8.3):** Führen Sie `bash restic_forget.sh` aus. Lesen Sie die Spalte „Reasons“ im Trockenlauf und erklären Sie, warum der Stand vom 2026-02-09 gleich mehrere Gründe hat.
4. **Platz freigeben (Einheit 8.3):** Vergleichen Sie die Snapshot-Liste vor und nach `forget --prune` und führen Sie danach `restic check` aus.

#### Kontrollfragen

1. Warum ist `forget --dry-run` vor jedem echten Löschlauf Pflicht?
2. Was ist der Unterschied zwischen `forget` ohne und mit `--prune`?
3. Welche Rolle spielt die gesetzliche oder vertragliche Aufbewahrungsfrist bei der Wahl der Regel?
4. Warum kann eine zu knappe Regel ein Problem für einen späten Restore-Wunsch werden (z. B. unbemerkter Fehler vor mehreren Wochen)?

### Modul 9: Verschlüsselung von Sicherungen und Schlüsselverwaltung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Archiv mit gpg und openssl verschlüsseln und wieder entschlüsseln.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied in der Fehlererkennung bei falschem Kennwort und bei beschädigtem Chiffrat erklären.
  * Nach Abschluss dieses Moduls kann der Lernende restic-Schlüssel hinzufügen und entfernen und die Regel „aktuellen Schlüssel nicht löschen“ erklären.
* **Voraussetzungen:** Modul 7; gpg, openssl und restic auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Warum Sicherungen verschlüsseln; Risiko Schlüsselverlust und Kennwortverwaltung | 2 |
| 9.2 | `gpg --symmetric` und `openssl enc` mit PBKDF2: Befehle, Unterschiede, Manipulationserkennung | 3 |
| 9.3 | restic: mehrere Schlüssel, `key add`, `key remove`, Sperre bei aktuellem Schlüssel | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **gpg (Einheit 9.2):** Führen Sie `bash verschluesselung.sh` aus. Prüfen Sie, ob im verschlüsselten Archiv der Klartext „Vertrauliche“ vorkommt, und notieren Sie Größe vorher und nachher.
2. **Falsches Kennwort (Einheit 9.2):** Notieren Sie den Rückgabewert und die Meldung bei falschem Kennwort und bei einem veränderten Byte im Chiffrat.
3. **openssl (Einheit 9.2):** Entschlüsseln Sie die openssl-Datei und vergleichen Sie mit dem Original. Nennen Sie die Parameter `-pbkdf2` und `-iter`, und erklären Sie, wozu sie dienen.
4. **restic-Schlüssel (Einheit 9.3):** Fügen Sie einen zweiten Schlüssel hinzu, entfernen Sie den ersten (angemeldet mit dem zweiten) und zeigen Sie, dass das alte Kennwort danach nicht mehr funktioniert. Versuchen Sie, den aktuell verwendeten Schlüssel zu entfernen, und notieren Sie die Meldung.

#### Kontrollfragen

1. Warum darf der Schlüssel nicht nur im Backup selbst liegen?
2. Warum meldet gpg bei verändertem Chiffrat einen Fehler, während reines AES-CBC ohne Integritätsprüfung Datenmüll liefern kann?
3. Wozu dient ein zweiter restic-Schlüssel im Betrieb?
4. Welche Folgen hat der Verlust aller Kennwörter für ein restic-Repository?

### Modul 10: Unveränderbare Kopien und Schutz vor Ransomware

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Weg erklären, auf dem Ransomware Sicherungen auf erreichbaren Zielen zerstört.
  * Nach Abschluss dieses Moduls kann der Lernende mit `chattr +i` eine Kopie vor Überschreiben und Löschen schützen und die Wirkung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen des Schutzes benennen.
* **Voraussetzungen:** Module 3 und 5; `srv-lin01` mit ext4 und root-Rechten.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Ransomware und Sicherungen: Angriffsweg, Löschen und Verschlüsseln erreichbarer Ziele | 2 |
| 10.2 | Schutzprinzipien: Trennung, Offline, Append-only, Unveränderlichkeit (WORM), eigene Zugangsdaten | 3 |
| 10.3 | Praxis: `ransomware_sim.sh` mit `chattr +i` im Laborordner | 3 |
| 10.4 | Grenzen: wer kann den Schutz aufheben, Zeitfenster, Überwachung | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Simulation lesen (Einheit 10.3):** Führen Sie `bash ransomware_sim.sh` aus. Das Skript „verschlüsselt“ Dateien im Ordner `produktiv/` (durch Umbenennen und Überschreiben). Lesen Sie, was im offenen und im geschützten Ziel nach dem nächsten planmäßigen Lauf steht.
2. **Löschversuch (Einheit 10.3):** Notieren Sie Meldung und Rückgabewert beim Löschversuch einer geschützten Datei als root.
3. **Wiederherstellung (Einheit 10.3):** Stellen Sie aus dem geschützten Ziel wieder her und zeigen Sie den Inhalt.
4. **Grenzen beschreiben (Einheit 10.4):** Nennen Sie drei Wege, auf denen ein Angreifer mit Administratorrechten das Attribut doch entfernen könnte, und je eine Gegenmaßnahme.

#### Kontrollfragen

1. Warum genügt ein Netzlaufwerk mit Schreibrechten nicht als Schutz vor Ransomware?
2. Was bewirkt `chattr +i`, und warum schlägt `rm` auch für root fehl?
3. Warum ist eine Spiegelung mit `--delete` auf ein erreichbares Ziel gefährlich?
4. Was ist der Vorteil einer Offline-Kopie gegenüber einer unveränderlichen Kopie am selben System?

### Modul 11: Restore-Tests, Prüfsummen und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Restore-Test mit Prüfsummen-Manifest durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum `restic check` ohne `--read-data` Schäden an Datenpaketen nicht erkennt.
  * Nach Abschluss dieses Moduls kann der Lernende häufige Rückgabewerte der Werkzeuge deuten.
* **Voraussetzungen:** Module 5, 7 und 9; sha256sum und restic auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Warum nur ein getestetes Backup ein Backup ist; Teststrategie (Stichprobe, Vollständigkeit, Häufigkeit) | 2 |
| 11.2 | Prüfsummen-Manifest vor der Sicherung und Vergleich nach der Wiederherstellung | 3 |
| 11.3 | restic: `check` und `check --read-data`, beschädigtes Repository erkennen | 3 |
| 11.4 | Typische Rückgabewerte und Fehlerbilder von rsync, tar und restic | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Manifest und Restore (Einheit 11.2):** Führen Sie `bash restore_test.sh` aus. Lesen Sie, wie viele Abweichungen der Vergleich der Prüfsummen ergibt.
2. **Beschädigung erkennen (Einheit 11.3):** Das Skript beschädigt ein Byte im größten Datenpaket des Repositorys. Notieren Sie Rückgabewert und Ausgabe von `restic check` und `restic check --read-data`.
3. **Rückgabewerte (Einheit 11.4):** Ordnen Sie die Rückgabewerte der letzten Ausgabe zu (rsync Quelle fehlt, tar Datei fehlt, restic falsches Kennwort, Repository fehlt).
4. **Testplan (Einheit 11.1):** Schreiben Sie einen Restore-Testplan für drei Systeme (Häufigkeit, Umfang, Verantwortliche Rolle, Protokollvorlage).

#### Kontrollfragen

1. Warum liefert `restic check` ohne `--read-data` Rückgabewert 0, obwohl ein Datenpaket beschädigt ist?
2. Wann ist ein Stichprobentest ausreichend, wann nicht?
3. Was bedeutet der tar-Rückgabewert 2?
4. Welche Rolle spielt der Test der „0“ in 3-2-1-1-0?

### Modul 12: Datenbanken konsistent sichern (SQLite als Beispiel)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende drei Sicherungsverfahren einer laufenden SQLite-Datenbank vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherung mit `integrity_check` und einer fachlichen Prüfsumme überprüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Verfahren grundsätzlich auf andere Datenbanken übertragen.
* **Voraussetzungen:** Modul 7; Python 3 auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Konsistenz: Warum das Kopieren einer laufenden Datenbankdatei riskant ist; Transaktionen, Journal und WAL | 2 |
| 12.2 | Verfahren: Backup-API, Textdump, Snapshot des Dateisystems; Wiederherstellung und `integrity_check` | 3 |
| 12.3 | Übertragung auf PostgreSQL und andere Datenbanken (`pg_dump`, Überblick, nicht ausgeführt) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Lauf mit parallelem Schreiber (Einheit 12.2):** Führen Sie `python3 db_sicherung.py ./lab12 DELETE` und danach `… WAL` aus. Lesen Sie die drei Prüfungen (blockweise Kopie, Backup-API, Textdump).
2. **Ergebnis deuten (Einheit 12.2):** Beschreiben Sie, warum die Anzahl der Buchungen in den drei Sicherungen unterschiedlich ist, obwohl alle konsistent sind.
3. **Übertragung (Einheit 12.3):** Nennen Sie für PostgreSQL die entsprechenden Verfahren (Dump, kontinuierliche Archivierung, Snapshot) und deren Grenzen.

#### Kontrollfragen

1. Warum ist „konsistent“ nicht dasselbe wie „aktuell“?
2. Wozu dient die Prüfung „Summe der Salden“ zusätzlich zu `integrity_check`?
3. Warum fehlt eine fehlerhafte Kopie in dieser Übung, obwohl das Risiko besteht?
4. Welchen Vorteil hat ein Textdump bei einem Versionswechsel der Datenbank?

### Modul 13: Backup-Konzept dokumentieren, überwachen und berichten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 13 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Backup-Konzept mit allen Bausteinen für ein kleines Unternehmen schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Statusbericht aus Laufdaten erzeugen und Befunde ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende Konzept und Praxis (Skripte, Tests) widerspruchsfrei dokumentieren.
* **Voraussetzungen:** Module 1 bis 11 (Modul 12 optional).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Bausteine eines Backup-Konzepts: Systeme, Ziele (RPO/RTO), Verfahren, Orte, Aufbewahrung, Verschlüsselung, Tests, Verantwortliche | 4 |
| 13.2 | Überwachung: Statusbericht aus Läufen, Alter, Fehlerstatus und Restore-Test-Alter, Rückgabewert für Monitoring | 3 |
| 13.3 | Abschlussprojekt: Konzept für ein fiktives Unternehmen schreiben und mit dem Berichtsskript prüfen | 6 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bericht lesen (Einheit 13.2):** Führen Sie `python3 bericht.py laeufe.csv "2026-11-19 08:00"` aus. Nennen Sie je Job den Befund und die erste Maßnahme.
2. **Regeln anpassen (Einheit 13.2):** Ändern Sie die Grenzen (maximales Alter, Restore-Test-Alter) im Skript und erklären Sie die Begründung.
3. **Konzept schreiben (Einheit 13.1):** Schreiben Sie für die fiktive Firma „Alpenwerk Beispiel“ (20 Arbeitsplätze, Dateiserver, ERP-Datenbank, Mailserver, Webserver) ein Backup-Konzept auf zwei bis drei Seiten mit: Schutzbedarf je System, RPO/RTO, Verfahren, 3-2-1-1-0-Architektur, Aufbewahrung, Verschlüsselung und Schlüsselverwaltung, Restore-Tests, Überwachung, Verantwortlichkeiten.
4. **Konsistenz prüfen (Einheit 13.3):** Prüfen Sie Ihr Konzept gegen die Skripte: Passt jede Angabe zu den Ergebnissen aus den Modulen 2, 3 und 8 (Zahlen, Aufbewahrung)? Notieren Sie Abweichungen.

#### Kontrollfragen

1. Welche Angaben gehören unbedingt in ein Backup-Konzept?
2. Warum ist „letzter Restore-Test“ ein Überwachungswert?
3. Wie macht man aus dem Berichtsskript eine automatische Überwachung?
4. Welche Widersprüche zwischen Konzept und Praxis sind besonders gefährlich?
