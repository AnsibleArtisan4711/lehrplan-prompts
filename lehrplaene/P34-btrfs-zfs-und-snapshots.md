# Lehrplan: Btrfs, ZFS und Snapshots

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Terminal, Dateien, Benutzer); Grundkenntnisse zu Dateisystemen und RAID (Kurs „NAS, SAN, iSCSI und RAID“) |
| **Gesamtumfang** | 10 Module, 108 UE (zu 45 Minuten; 81 Stunden) |
| **Fokus-Technologien** | Btrfs (Linux-Kernel, `btrfs-progs`) mit Praxisübungen; ZFS (OpenZFS) als Konzept, Modell und Befehlsüberblick; Snapshots, Replikation, Prüfsummen und Wiederherstellung |
| **Thematische Abgrenzung (Out of Scope)** | Software-RAID mit mdadm, ext4/XFS, NFS und iSCSI stehen im Kurs „NAS, SAN, iSCSI und RAID“ dieses Repositories; das Backup-Konzept (RPO, RTO, 3-2-1-1-0) im Kurs „Backup-Konzept“. Nicht behandelt: ZFS-Verschlüsselung, ZFS-Volumes (zvol), Deduplizierung, Btrfs raid5/raid6 im Betrieb, Btrfs-Verschlüsselung, Ceph und andere verteilte Dateisysteme, Betriebssysteminstallation auf Btrfs oder ZFS (Root-Dateisystem) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Copy-on-Write | 1 | 10 |
| 2 | Btrfs und ZFS im Vergleich | 1 | 10 |
| 3 | Pools, Subvolumes und Datasets | 1 | 12 |
| 4 | Snapshots und Klone | 1 | 12 |
| 5 | Replikation mit send und receive | 1 | 12 |
| 6 | Prüfsummen und Scrub | 1 | 10 |
| 7 | Kompression | 2 | 8 |
| 8 | Speicherverwaltung und Quoten | 1 | 12 |
| 9 | Wiederherstellung | 1 | 12 |
| 10 | Typische Fehler und ihre Diagnose | 1 | 10 |
| **Gesamt** | 10 Module | 9 × Priorität 1, 1 × Priorität 2 | **108** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8 bis 10; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Kompression). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 100 UE; kein Pflichtmodul setzt Modul 7 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Btrfs (`btrfs-progs`, Kernel-Dokumentation) und von OpenZFS wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch die Läufe im Labor bestätigt; verbindlich ist die Dokumentation der installierten Version. Zahlen (Größen, Datenmengen) sind Annahmen oder erfundene Beispieldaten.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container, Kernel 6.18.44):** `btrfs-progs` v6.6.3 mit Loop-Geräten, `compsize` (Paket `btrfs-compsize`), Python 3. **ZFS wurde nicht ausgeführt**: Im Container gibt es weder das Kernelmodul noch die Programme `zpool` und `zfs`. Alle ZFS-Inhalte sind Python-Modelle und Textdateien mit der Kennzeichnung „nicht ausgeführt“; die Befehle und Eigenschaften stammen aus Fachwissen und sind **nicht bestätigt**. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-FS`, `10.34.0.0/24`).

**VM:** `fs01` (**erforderlich**, `10.34.0.2`): Linux-Server (Debian oder Ubuntu Server) mit `btrfs-progs`; vier zusätzliche virtuelle Platten (z. B. je 2 GB) für Pools und Dateisysteme; optional das Paket `zfsutils-linux` für die ZFS-Übungen (Paketname und Verfügbarkeit sind nicht bestätigt).

**Internetphase:** Für die Installation der Pakete braucht `fs01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es werden nur erfundene Beispieldaten verwendet.

**Prüfpunkt (Checkpoint):** Vor Modul 6 und vor Modul 9 von `fs01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte arbeiten im Test-Container mit Image-Dateien unter `/tmp/p34`, die als Loop-Geräte eingebunden und am Ende entfernt werden, und binden `lab.sh` ein. Im Hyper-V-Labor verwenden Sie stattdessen die zusätzlichen Platten (z. B. `/dev/sdb`).

## B. Detaillierter Modulaufbau

### Modul 1: Copy-on-Write

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Copy-on-Write-Verfahren mit eigenen Worten erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zum Überschreiben an Ort und Stelle am Beispiel eines Absturzes beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende mit Reflinks gemeinsam genutzte Blöcke erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Vor- und Nachteile von Copy-on-Write nennen.
* **Voraussetzungen:** Linux-Grundlagen; Grundkenntnisse zu Dateisystemen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Überschreiben gegen Copy-on-Write: Absturz mitten in einer Änderung (`cow_modell.py`) | 3 |
| 1.2 | Reflinks und gemeinsame Blöcke in Btrfs sichtbar machen (`cow_btrfs.sh`) | 3 |
| 1.3 | Vorteile und Kosten von Copy-on-Write: Snapshots, Fragmentierung, Platzbedarf (Fachwissen) | 2 |
| 1.4 | Labor aufbauen: `fs01` mit vier Platten, privater Switch | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Absturz im Modell (Einheit 1.1):** Führen Sie `python3 cow_modell.py` aus und erklären Sie, warum das Überschreiben nach einem Absturz einen halb geänderten Zustand hinterlassen kann, Copy-on-Write aber nicht.
2. **Reflink untersuchen (Einheit 1.2):** Führen Sie `bash cow_btrfs.sh` aus. Erklären Sie die Spalten `Total`, `Exclusive` und `Set shared` in jedem Schritt und woran Sie mit `filefrag` erkennen, dass zwei Dateien dieselben Blöcke nutzen.
3. **Vor- und Nachteile (Einheit 1.3):** Erstellen Sie eine Tabelle mit je drei Vorteilen und Nachteilen von Copy-on-Write (z. B. für Datenbanken und virtuelle Platten) und kennzeichnen Sie, was Sie belegen können und was nicht bestätigt ist.
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie `fs01` mit vier zusätzlichen Platten (je 2 GB) und dem Switch `Lab-FS` auf, installieren Sie `btrfs-progs` und prüfen Sie mit `btrfs --version` die Installation.

#### Kontrollfragen

1. Warum ist bei Copy-on-Write ein halb geschriebener Zustand nach einem Absturz unwahrscheinlicher?
2. Wie kann ein Snapshot entstehen, ohne Daten zu kopieren?
3. Warum kann Copy-on-Write bei häufig überschriebenen großen Dateien zu Fragmentierung führen?
4. Was bedeutet `Set shared` in der Ausgabe von `btrfs filesystem du`?

### Modul 2: Btrfs und ZFS im Vergleich

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Btrfs und ZFS nach Aufbau, Funktionen und Einbindung vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende unterscheiden, welche Aussagen im Labor geprüft und welche nur Fachwissen sind.
  * Nach Abschluss dieses Moduls kann der Lernende Version, Prüfsummenverfahren und Blockgrößen eines Btrfs-Dateisystems auslesen.
  * Nach Abschluss dieses Moduls kann der Lernende Kriterien für die Auswahl nennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Gemeinsamkeiten und Unterschiede in der Übersicht (`vergleich.py`) | 3 |
| 2.2 | Btrfs im Labor ansehen: Version, Kernel-Unterstützung, Super-Block; ZFS-Verfügbarkeit prüfen (`btrfs_info.sh`) | 3 |
| 2.3 | Lizenz, Einbindung in das Betriebssystem und Speicherbedarf (Fachwissen) | 2 |
| 2.4 | Auswahlkriterien für einen Einsatz entwickeln | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Übersicht lesen (Einheit 2.1):** Führen Sie `python3 vergleich.py` aus und erklären Sie, welche Aussagen mit „L“ (geprüft) und welche mit „F“ (Fachwissen) gekennzeichnet sind und warum ZFS vollständig „F“ ist.
2. **Btrfs ansehen (Einheit 2.2):** Führen Sie `bash btrfs_info.sh` aus und erklären Sie jeden Abschnitt der Ausgabe: Versionen, Kernel, ZFS-Prüfung, Super-Block (`csum_type`, `sectorsize`, `nodesize`) und `btrfs filesystem df`.
3. **Lizenz und Betrieb recherchieren (Einheit 2.3):** Recherchieren Sie in der Dokumentation von OpenZFS und im Kernel-Handbuch zu Btrfs, wie beide in Linux eingebunden werden und was das für Updates bedeutet. Notieren Sie Quelle und Abrufdatum und markieren Sie bestätigte Aussagen.
4. **Auswahl begründen (Einheit 2.4):** Wählen Sie für drei Fälle (Dateiserver mit Snapshots, Virtualisierungshost, Heimserver mit zwei Platten) ein System und begründen Sie die Wahl in je drei Sätzen. Nennen Sie, was Sie dafür noch prüfen müssten.

#### Kontrollfragen

1. Warum ist es wichtig, bei jeder Aussage zu wissen, ob sie geprüft oder nur Fachwissen ist?
2. Was bedeutet `csum_type crc32c` im Super-Block?
3. Warum konnte ZFS im Test-Container nicht ausgeführt werden?
4. Welche organisatorischen Faktoren (außer Technik) beeinflussen die Wahl des Dateisystems?

### Modul 3: Pools, Subvolumes und Datasets

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Btrfs-Dateisystem über mehrere Platten anlegen und die Belegung lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Subvolumes anlegen, auflisten und gezielt einbinden.
  * Nach Abschluss dieses Moduls kann der Lernende das ZFS-Modell aus Pool, vdev und Dataset erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen Aufbau für gegebene Platten planen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Btrfs: ein Dateisystem über mehrere Platten (raid1), Subvolumes, `subvol`-Einbindung (`btrfs_pool.sh`) | 4 |
| 3.2 | ZFS im Modell: Pool, vdev, Dataset und vererbte Eigenschaften (`zfs_modell.py`) | 3 |
| 3.3 | ZFS-Befehle im Überblick (`beispiel_zfs.txt`, nicht ausgeführt) | 2 |
| 3.4 | Aufbau für `fs01` planen: Platten, Profile, Subvolumes | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Btrfs-Spiegel anlegen (Einheit 3.1):** Führen Sie `bash btrfs_pool.sh` aus. Erklären Sie `Data ratio`, `Device allocated` und `Device unallocated` und warum zwei Platten à 300 MiB im Spiegel nur etwa 300 MiB nutzbar machen.
2. **Subvolumes (Einheit 3.1):** Erklären Sie anhand von Abschnitt 2 bis 4 den Unterschied zwischen einem Subvolume und einem gewöhnlichen Verzeichnis, und wie `-o subvol=daten` eingesetzt wird.
3. **ZFS-Modell (Einheit 3.2):** Führen Sie `python3 zfs_modell.py` aus. Erklären Sie, warum der Pool `tank` nur ein vdev-Ausfall je Paar verträgt, und wie Eigenschaften an Datasets vererbt werden.
4. **ZFS-Befehle lesen (Einheit 3.3):** Lesen Sie `beispiel_zfs.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben, und prüfen Sie die Befehle mit `man zpool` und `man zfs` auf einem Testsystem.
5. **Aufbau planen (Einheit 3.4):** Planen Sie für `fs01` mit vier Platten à 2 GB einen Aufbau (z. B. Spiegel für Daten, Subvolumes für Dienste) und begründen Sie Profile und Nutzkapazität.

#### Kontrollfragen

1. Warum erzeugt ein Spiegel nutzbar nur die Kapazität einer Platte?
2. Was unterscheidet ein Subvolume von einem Verzeichnis?
3. Warum sollte man vdevs in einem ZFS-Pool nicht aus unterschiedlich ausfallsicheren Teilen mischen?
4. Was bedeutet „Eigenschaft erben“ bei Datasets?

### Modul 4: Snapshots und Klone

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Snapshots und Klone in Btrfs anlegen, nutzen und löschen.
  * Nach Abschluss dieses Moduls kann der Lernende den Platzbedarf von Snapshots nach Änderungen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Aufbewahrungsregel formulieren und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Snapshots keine Datensicherung sind.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Btrfs-Snapshots: schreibgeschützt und beschreibbar, Platzbedarf (`snapshots_btrfs.sh`) | 4 |
| 4.2 | Aufbewahrung planen: welche Snapshots werden behalten? (`rotation.py`) | 3 |
| 4.3 | ZFS im Modell: Snapshots, Klone und die Platzabrechnung (`zfs_snapshots_modell.py`) | 3 |
| 4.4 | Snapshots sind kein Backup: Grenzen erklären (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Snapshots ausprobieren (Einheit 4.1):** Führen Sie `bash snapshots_btrfs.sh` aus. Erklären Sie die Werte von `Exclusive` und `Set shared` vor und nach der Änderung und warum der schreibgeschützte Snapshot nicht verändert werden kann.
2. **Aufbewahrung prüfen (Einheit 4.2):** Führen Sie `python3 rotation.py` aus, ändern Sie die Regel (z. B. 14 tägliche, 8 wöchentliche) und prüfen Sie, welche Snapshots behalten werden. Was passiert, wenn der Snapshot von heute fehlt?
3. **ZFS-Modell (Einheit 4.3):** Führen Sie `python3 zfs_snapshots_modell.py` aus und erklären Sie, warum der „used“-Wert eines Snapshots sich nach dem Löschen eines anderen ändern kann.
4. **Grenzen beschreiben (Einheit 4.4):** Nennen Sie fünf Fälle, in denen ein Snapshot nicht ausreicht (z. B. Plattenausfall, Dateisystemfehler, versehentliches Löschen des Pools, Verschlüsselungstrojaner) und die passende Ergänzung.

#### Kontrollfragen

1. Warum belegt ein frischer Snapshot praktisch keinen Platz?
2. Warum wächst der Platzbedarf, wenn die Originaldaten geändert werden?
3. Wann ist ein beschreibbarer Snapshot (Klon) sinnvoll?
4. Warum reichen Snapshots auf demselben Datenträger nicht als Sicherung?

### Modul 5: Replikation mit send und receive

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Snapshots mit `btrfs send` und `btrfs receive` vollständig und inkrementell übertragen.
  * Nach Abschluss dieses Moduls kann der Lernende die Größe der Datenströme vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende die gemeinsame Basis für eine inkrementelle Übertragung bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Übertragung auf ein zweites System planen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Btrfs send/receive: vollständig und inkrementell (`send_receive_btrfs.sh`) | 4 |
| 5.2 | Gemeinsame Basis finden und Befehle planen (`replikationsplan.py`) | 3 |
| 5.3 | ZFS `send`/`receive` im Überblick (Textausgabe des Plans, nicht ausgeführt) | 2 |
| 5.4 | Übertragung auf ein anderes System planen: SSH, Zeitplan, Prüfung (Fachwissen) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vollständig und inkrementell (Einheit 5.1):** Führen Sie `bash send_receive_btrfs.sh` aus. Vergleichen Sie die Größen der Datenströme und erklären Sie, warum der zweite Strom viel kleiner ist und wozu `-p` dient.
2. **Gemeinsame Basis (Einheit 5.2):** Führen Sie `python3 replikationsplan.py` aus und erklären Sie jeden der vier Fälle. Wann ist eine vollständige Übertragung nötig?
3. **ZFS-Befehle prüfen (Einheit 5.3):** Lesen Sie die ZFS-Zeilen des Plans (`zfs send -i`, `zfs receive`) und markieren Sie sie als nicht ausgeführt. Prüfen Sie die Schreibweise in `man zfs` auf einem Testsystem.
4. **Übertragung planen (Einheit 5.4):** Planen Sie die tägliche Übertragung von `fs01` auf ein zweites System mit `ssh` (Befehlszeile, Konto mit minimalen Rechten, Fehlerbehandlung, Prüfung des Ergebnisses). Nicht in diesem Material geprüft.

#### Kontrollfragen

1. Warum muss der Snapshot für `btrfs send` schreibgeschützt sein?
2. Was passiert, wenn der Elternsnapshot im Ziel fehlt?
3. Warum ist eine inkrementelle Übertragung für große Datenmengen vorteilhaft?
4. Wie prüfen Sie, dass Quelle und Ziel übereinstimmen?

### Modul 6: Prüfsummen und Scrub

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Prüfsummen schleichende Datenfehler aufdecken.
  * Nach Abschluss dieses Moduls kann der Lernende einen Scrub ausführen und die Ausgabe lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Selbstheilung im Spiegel von der reinen Erkennung ohne Kopie unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerzähler (`device stats`) auswerten.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Prüfsummen und schleichende Datenfehler im Modell (`pruefsumme_modell.py`) | 3 |
| 6.2 | Btrfs-Scrub: Fehler erkennen und im Spiegel reparieren, ohne Spiegel nur erkennen (`scrub_btrfs.sh`) | 5 |
| 6.3 | Scrub planen und Fehlerzähler auswerten (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Modell lesen (Einheit 6.1):** Führen Sie `python3 pruefsumme_modell.py` aus. Erklären Sie, warum ein gekipptes Bit ohne Prüfsumme unbemerkt bleibt und wie die zweite Kopie die Reparatur ermöglicht.
2. **Spiegel reparieren (Einheit 6.2):** Führen Sie `bash scrub_btrfs.sh` aus. Erklären Sie `Error summary`, `Corrected`, `Uncorrectable` und die Fehlerzähler von `btrfs device stats` in Abschnitt 3.
3. **Ohne Spiegel (Einheit 6.2):** Erklären Sie Abschnitt 4: Welche Fehlermeldungen entstehen beim Lesen der beschädigten Datei und warum ist das besser als falsche Daten?
4. **Scrub planen (Einheit 6.3):** Planen Sie den Scrub für `fs01` (Häufigkeit, Zeitpunkt, Meldung bei Fehlern, Reaktion bei steigenden Zählern). Begründen Sie Ihre Wahl; nicht in diesem Material geprüft.

#### Kontrollfragen

1. Warum erkennt ein klassisches Dateisystem ohne Prüfsummen manche Datenfehler nicht?
2. Warum kann Btrfs im Spiegel (raid1) reparieren, im Profil single nicht?
3. Wie oft sollte ein Scrub laufen und was kostet er?
4. Was bedeutet es, wenn die Fehlerzähler einer Platte steigen?

### Modul 7: Kompression

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Kompression von Btrfs per Mount-Option einschalten.
  * Nach Abschluss dieses Moduls kann der Lernende den Platzgewinn mit `compsize` messen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum der Nutzen von der Art der Daten abhängt.
  * Nach Abschluss dieses Moduls kann der Lernende bereits vorhandene Daten nachträglich komprimieren.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Btrfs-Kompression einschalten und messen (`kompression_btrfs.sh`) | 4 |
| 7.2 | Wann lohnt sich Kompression? Daten im Vergleich (`kompression_modell.py`) | 2 |
| 7.3 | ZFS-Kompression im Überblick (Fachwissen, nicht bestätigt) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kompression messen (Einheit 7.1):** Führen Sie `bash kompression_btrfs.sh` aus. Vergleichen Sie die Verfahren `zstd`, `zlib` und `lzo` für Text und für Zufallsdaten und erklären Sie, warum Zufallsdaten nicht schrumpfen.
2. **Daten im Vergleich (Einheit 7.2):** Führen Sie `python3 kompression_modell.py` aus und erklären Sie die vier Datenarten. Warum sind verschlüsselte oder bereits komprimierte Daten ungeeignet?
3. **ZFS prüfen (Einheit 7.3):** Recherchieren Sie die Kompressionsverfahren von OpenZFS und die Eigenschaft `compression` in der Dokumentation. Notieren Sie Quelle und Abrufdatum und kennzeichnen Sie, was bestätigt ist.

#### Kontrollfragen

1. Warum belegt `lzo` im Lauf fast so viel Platz wie unkomprimierte Daten?
2. Was bewirkt `compress-force` im Gegensatz zu `compress`?
3. Wann kann Kompression die Geschwindigkeit sogar erhöhen?
4. Warum wirkt die Mount-Option nur auf neu geschriebene Daten?

### Modul 8: Speicherverwaltung und Quoten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Platzbelegung eines Btrfs-Dateisystems mit mehreren Werkzeugen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Quoten für Subvolumes setzen und die Wirkung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Platten im laufenden Betrieb hinzufügen und entfernen sowie das Profil wechseln.
  * Nach Abschluss dieses Moduls kann der Lernende die ZFS-Eigenschaften quota, refquota und reservation unterscheiden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Platzbelegung richtig lesen: `df`, `filesystem df`, `usage` (`speicher_btrfs.sh`) | 3 |
| 8.2 | Quoten mit qgroups (`quoten_btrfs.sh`) | 3 |
| 8.3 | Platten hinzufügen und entfernen, Balance, Profil wechseln (`erweitern_btrfs.sh`) | 3 |
| 8.4 | ZFS im Modell: quota, refquota und reservation (`quoten_zfs_modell.py`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Platz lesen (Einheit 8.1):** Führen Sie `bash speicher_btrfs.sh` aus. Erklären Sie, warum `df` bei zwei gespiegelten Platten nur die Größe einer Platte zeigt und warum nach dem Löschen der Datei der Platz erst nach dem Löschen des Snapshots frei wird.
2. **Quoten (Einheit 8.2):** Führen Sie `bash quoten_btrfs.sh` aus. Erklären Sie die Fehlermeldung `Disk quota exceeded`, die Spalten von `btrfs qgroup show` und das Aufheben der Grenze.
3. **Erweitern und Verkleinern (Einheit 8.3):** Führen Sie `bash erweitern_btrfs.sh` aus. Erklären Sie, wozu die Balance nach `device add` dient, und was bei `device remove` geschieht.
4. **ZFS-Quoten (Einheit 8.4):** Führen Sie `python3 quoten_zfs_modell.py` aus und erklären Sie den Unterschied zwischen `quota` und `refquota` anhand von Fall 1 und 2 sowie die Grenze bei Reservierungen.

#### Kontrollfragen

1. Warum sagt `df` bei Btrfs nicht die ganze Wahrheit über freien Platz?
2. Was ist bei Quoten der Unterschied zwischen `Referenced` und `Exclusive`?
3. Warum braucht man nach dem Hinzufügen einer Platte eine Balance?
4. Welches Risiko besteht bei Reservierungen, deren Summe die Poolgröße übersteigt?

### Modul 9: Wiederherstellung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Dateien und Verzeichnisse aus einem Snapshot zurückholen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Subvolume durch Austausch auf einen Snapshot zurücksetzen.
  * Nach Abschluss dieses Moduls kann der Lernende bei Plattenausfall den Spiegel degradiert einbinden und die Platte ersetzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wiederherstellungswege von ZFS benennen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Einzelne Dateien aus einem Snapshot zurückholen (`restore_btrfs.sh`) | 3 |
| 9.2 | Ein Subvolume auf einen Snapshot zurücksetzen (`rollback_btrfs.sh`) | 3 |
| 9.3 | Ausfall einer Platte im Spiegel: degradiert einbinden, ersetzen, Profile angleichen (`ausfall_btrfs.sh`) | 4 |
| 9.4 | ZFS: Rollback, Klon und Plattenersatz im Überblick (`beispiel_zfs_wiederherstellung.txt`, nicht ausgeführt) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dateien zurückholen (Einheit 9.1):** Führen Sie `bash restore_btrfs.sh` aus. Erklären Sie, wie Sie gelöschte und veränderte Dateien zurückholen und warum `cp --reflink=always` bei der großen Datei keinen zusätzlichen Platz braucht.
2. **Rollback (Einheit 9.2):** Führen Sie `bash rollback_btrfs.sh` aus. Beschreiben Sie die Schritte und warum der Snapshot als Rückfallpunkt unverändert bleibt.
3. **Plattenausfall (Einheit 9.3):** Führen Sie `bash ausfall_btrfs.sh` aus. Erklären Sie, warum das normale Einbinden fehlschlägt, was `-o degraded` bewirkt und warum danach eine Balance mit `soft` nötig ist.
4. **ZFS vergleichen (Einheit 9.4):** Lesen Sie `beispiel_zfs_wiederherstellung.txt`, ordnen Sie jedem Btrfs-Schritt den ZFS-Befehl zu und kennzeichnen Sie, dass nichts ausgeführt wurde. Prüfen Sie die Befehle mit `man zfs` auf einem Testsystem.

#### Kontrollfragen

1. Warum sollte ein Rollback nur nach einer Sicherung des defekten Zustands erfolgen?
2. Warum soll ein degradierter Spiegel nur kurz und möglichst nur lesend betrieben werden?
3. Warum ist der Wiederherstellungstest wichtiger als die Sicherung selbst?
4. Welche Rolle spielt der Scrub nach dem Austausch einer Platte?

### Modul 10: Typische Fehler und ihre Diagnose

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Platz trotz gelöschter Dateien belegt bleibt, und den Ursachen nachgehen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler bei send/receive erkennen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlermeldungen einer Ursache zuordnen und den nächsten Schritt nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen automatischer Diagnose benennen.
* **Voraussetzungen:** Modul 5; Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | „No space left on device“ trotz gelöschter Dateien: Snapshots und Platzbelegung (`fehler_platz.sh`) | 4 |
| 10.2 | Fehler bei send/receive: nicht schreibgeschützt, Elternsnapshot fehlt, Name existiert (`fehler_send.sh`) | 3 |
| 10.3 | Meldungen deuten: Ursachen und nächste Schritte (`diagnose.py`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Platz bleibt belegt (Einheit 10.1):** Führen Sie `bash fehler_platz.sh` aus. Erklären Sie jeden Abschnitt und beschreiben Sie, welche Befehle Sie nutzen, um die Ursache zu finden, bevor Sie etwas löschen.
2. **send/receive-Fehler (Einheit 10.2):** Führen Sie `bash fehler_send.sh` aus und ordnen Sie jede Fehlermeldung der Ursache und der Lösung zu.
3. **Meldungen deuten (Einheit 10.3):** Führen Sie `python3 diagnose.py beispiel_meldungen.txt` aus. Erweitern Sie die Regelliste um zwei eigene Meldungen aus Ihrem Labor und beschreiben Sie, warum die Zeile „Meldung die niemand kennt“ als unbekannt gemeldet wird.

#### Kontrollfragen

1. Warum ist es gefährlich, bei vollem Dateisystem einfach Snapshots zu löschen?
2. Warum ist `diagnose.py` kein Ersatz für das Lesen der Dokumentation?
3. Welche Fehler lassen sich durch Planung (z. B. Aufbewahrungsregeln, Überwachung) vermeiden?
4. Warum sind unveränderte Fehlermeldungen wichtig, wenn man Hilfe sucht?
