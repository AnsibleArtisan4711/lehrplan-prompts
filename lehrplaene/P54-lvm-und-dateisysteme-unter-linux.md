# Lehrplan: LVM und Dateisysteme unter Linux

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Terminal, Dateien, Benutzer, `sudo`) |
| **Gesamtumfang** | 8 Module, 104 UE (zu 45 Minuten; 78 Stunden) |
| **Fokus-Technologien** | Debian/Ubuntu Linux; Partitionierung (MBR, GPT); LVM (Physical Volumes, Volume Groups, Logical Volumes); Dateisysteme ext4 und XFS; Mount-Optionen und `fstab`; Quotas; Fehlerdiagnose und Reparatur; Überwachung des Speicherplatzes |
| **Thematische Abgrenzung (Out of Scope)** | Btrfs, ZFS und Snapshots sind der Kurs „Btrfs, ZFS und Snapshots“ dieses Repositories; NAS, SAN, iSCSI und RAID-Theorie der Kurs „NAS, SAN, iSCSI und RAID“; Backup-Konzepte der Kurs „Backup-Konzept“. Software-RAID mit `mdadm` und LVM-Snapshots werden nur als Überblick behandelt. Nicht behandelt: Verschlüsselung (LUKS), Thin Provisioning, LVM-Cache, Root-Dateisystem auf LVM bei der Installation, Cluster-Dateisysteme |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Partitionierung: MBR und GPT | 1 | 12 |
| 2 | Physical Volumes, Volume Groups und Logical Volumes | 1 | 14 |
| 3 | Dateisysteme ext4 und XFS im Vergleich | 1 | 14 |
| 4 | Dateisysteme vergrößern und verkleinern | 1 | 14 |
| 5 | Mount-Optionen und fstab | 1 | 12 |
| 6 | Quotas | 2 | 12 |
| 7 | Fehlerdiagnose und Reparatur | 1 | 14 |
| 8 | Überwachung des Speicherplatzes | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **104** |

**Priorität 1** (Pflicht) sind die Module 1 bis 5, 7 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 6 (Quotas). Fällt Modul 6 weg, verringert sich der Gesamtumfang auf 92 UE; kein Pflichtmodul setzt Modul 6 voraus.

### 2. Quellen

**Nicht gelesen:** Die Handbücher von LVM, ext4, XFS und `mdadm` wurden **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt; verbindlich ist die Dokumentation der eingesetzten Version. Zahlen (Größen, Belegung) sind Annahmen oder erfundene Beispieldaten.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container, Kernel 6.18.44):** `lvm2` 2.03.16 (nur Physical Volumes und Volume Groups), `e2fsprogs` 1.47.0, `xfsprogs` (Version nicht erfasst), `fdisk` (`sfdisk`), `util-linux`, Python 3. **Nicht ausführbar im Container:** Logical Volumes und LVM-Snapshots (Device-Mapper fehlt), Software-RAID mit `mdadm` (kein `md`), Quotas (ein Dateisystem mit Quota-Option ließ sich nicht einbinden) sowie die Vergrößerung von ext4 im eingehängten Zustand. Die entsprechenden Teile sind Modelle oder Textdateien mit der Kennzeichnung „nicht ausgeführt“ und **nicht bestätigt**. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-LVM`, `10.54.0.0/24`).

**VM:** `lv01` (**erforderlich**, `10.54.0.2`): Linux-Server (Debian oder Ubuntu Server) mit den Paketen `lvm2`, `xfsprogs`, `quota`, `fdisk` und `mdadm`; vier zusätzliche virtuelle Platten (z. B. je 2 GB) für Partitionen, Volume Groups und Dateisysteme.

**Internetphase:** Für die Installation der Pakete braucht `lv01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es werden nur erfundene Beispieldaten verwendet.

**Prüfpunkt (Checkpoint):** Vor Modul 4 und vor Modul 7 von `lv01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte arbeiten im Test-Container mit Image-Dateien unter `/tmp/p54`, die als Loop-Geräte eingebunden und am Ende entfernt werden, und binden `lab.sh` ein. Im Hyper-V-Labor verwenden Sie stattdessen die zusätzlichen Platten (z. B. `/dev/sdb`) und können Logical Volumes, Quotas und `mdadm` tatsächlich ausprobieren.

## B. Detaillierter Modulaufbau

### Modul 1: Partitionierung: MBR und GPT

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine GPT- und eine MBR-Tabelle mit `sfdisk` anlegen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Größengrenzen von MBR und GPT aus Sektorgröße und Adressbreite berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Partitionen mit `lsblk` und `blkid` identifizieren.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor `lv01` aufbauen.
* **Voraussetzungen:** Linux-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Partitionstabellen anlegen und lesen mit `sfdisk` (`partition.sh`) | 4 |
| 1.2 | Grenzen von MBR und GPT berechnen (`grenzen.py`) | 3 |
| 1.3 | Partitionen, Geräte und Bezeichnungen im System: `lsblk`, `blkid`, UUID (Fachwissen) | 2 |
| 1.4 | Labor aufbauen: `lv01` mit vier Platten, privater Switch | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **GPT und MBR anlegen (Einheit 1.1):** Führen Sie `bash partition.sh` aus. Erklären Sie, wie die GPT-Tabelle mit zwei Partitionen (50 MiB und der Rest) entsteht, und was sich ändert, wenn dieselbe Platte als `dos` (MBR) mit vier Partitionen zu je 20 MiB neu aufgeteilt wird.
2. **Grenzen berechnen (Einheit 1.2):** Führen Sie `python3 grenzen.py` aus. Erklären Sie, warum MBR bei 512-Byte-Sektoren höchstens 2 TiB adressiert und was mit einer 3-TiB-Platte geschieht.
3. **Geräte lesen (Einheit 1.3):** Führen Sie auf `lv01` `lsblk -f` und `blkid` aus. Erklären Sie die Spalten und warum in `fstab` die UUID dem Gerätenamen `/dev/sdb1` vorzuziehen ist.
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie `lv01` mit vier zusätzlichen Platten (je 2 GB) und dem Switch `Lab-LVM` auf und installieren Sie `lvm2`, `xfsprogs`, `quota`, `fdisk` und `mdadm`.

#### Kontrollfragen

1. Wie viele Sektoren kann MBR adressieren, und welche Größe ergibt das bei 4096-Byte-Sektoren?
2. Wozu dient bei GPT die zweite Tabelle am Plattenende (Fachwissen)?
3. Warum ist die UUID in der `fstab` stabiler als der Gerätename?
4. Was geschieht mit den vorhandenen Daten, wenn eine Partitionstabelle neu angelegt wird?

### Modul 2: Physical Volumes, Volume Groups und Logical Volumes

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den dreistufigen Aufbau von LVM (Physical Volume, Volume Group, Logical Volume) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Physical Volumes und eine Volume Group anlegen und mit `pvs` und `vgs` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Verteilung von Extents und die Aufrundung auf Extent-Größen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen Aufbau für gegebene Platten planen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Physical Volumes und Volume Group anlegen, Belegung lesen (`lvm_vg.sh`) | 4 |
| 2.2 | Extents verteilen: Modell einer Volume Group (`lvm_modell.py`) | 3 |
| 2.3 | Logical Volumes anlegen und verwalten: Befehle als Text (`beispiel_lv.txt`, nicht ausgeführt) | 3 |
| 2.4 | Aufbau für `lv01` planen: Platten, Gruppen, Größen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Volume Group anlegen (Einheit 2.1):** Führen Sie `bash lvm_vg.sh` aus. Erklären Sie, warum zwei Platten à 300 MiB jeweils 296 MiB (74 Extents) ergeben, und was `vgextend` ändert. Erklären Sie die Fehlermeldung bei `lvcreate`.
2. **Extents im Modell (Einheit 2.2):** Führen Sie `python3 lvm_modell.py` aus. Erklären Sie, warum der Logical Volume `log` mit 150 MiB 152 MiB belegt und warum das Modell 150 statt 148 Extents hat.
3. **Befehle lesen (Einheit 2.3):** Lesen Sie `beispiel_lv.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben, und führen Sie die Befehle auf `lv01` aus.
4. **Aufbau planen (Einheit 2.4):** Planen Sie für `lv01` mit vier Platten à 2 GB eine Volume Group `vgdaten` mit Logical Volumes für Daten, Protokolle und Reserve, und begründen Sie die Größen und den freien Rest.

#### Kontrollfragen

1. Wozu dient die Zwischenschicht der Volume Group?
2. Was ist ein Extent, und warum werden Größen darauf aufgerundet?
3. Warum bleiben beim Anlegen eines Physical Volumes einige MiB ungenutzt?
4. Was bedeutet `vgextend`, und was geschieht dabei mit vorhandenen Daten?

### Modul 3: Dateisysteme ext4 und XFS im Vergleich

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ext4 und XFS anlegen und mit `blkid`, `df`, `tune2fs` und `xfs_info` beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied bei der Vergabe von Inodes erklären.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, welche Aussagen geprüft (L) und welche Fachwissen (F) sind.
  * Nach Abschluss dieses Moduls kann der Lernende für einen Einsatz ein Dateisystem begründet wählen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | ext4 und XFS anlegen, Typ und Belegung lesen (`fs_vergleich.sh`) | 4 |
| 3.2 | Inodes: ext4 fest, XFS dynamisch (`fs_vergleich.sh`, Abschnitt 3) | 2 |
| 3.3 | Vergleichstabelle mit Status L/F lesen (`vergleich.py`) | 3 |
| 3.4 | Auswahlkriterien: Einsatzfälle begründen | 3 |
| 3.5 | Journal und Konsistenz: Grundlagen (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dateisysteme anlegen (Einheit 3.1):** Führen Sie `bash fs_vergleich.sh` aus. Erklären Sie die Ausgaben von `blkid`, `df`, `tune2fs` und `xfs_info`, besonders Blockgröße, Journal und Anzahl der Inodes.
2. **Inodes (Einheit 3.2):** Erklären Sie anhand von Abschnitt 3, warum ext4 81 936 Inodes und XFS 163 840 ausweist und was das für viele kleine Dateien bedeutet. Wie ändert sich das Bild, wenn die Zahl der Inodes bei ext4 beim Anlegen klein gewählt wird (siehe Modul 8)?
3. **Tabelle lesen (Einheit 3.3):** Führen Sie `python3 vergleich.py` aus. Erklären Sie, welche Zeilen mit L und welche mit F gekennzeichnet sind und warum.
4. **Einsatz begründen (Einheit 3.4):** Wählen Sie für drei Fälle (Dateiserver mit vielen kleinen Dateien, Archiv mit großen Videodateien, kleines Systemlaufwerk) ein Dateisystem und begründen Sie die Wahl in je drei Sätzen. Nennen Sie, was Sie dafür noch prüfen müssten.
5. **Journal (Einheit 3.5):** Erklären Sie mit eigenen Worten, was ein Journal tut, und warum ein Journal keine Datensicherung ersetzt.

#### Kontrollfragen

1. Was bedeutet es, dass XFS Inodes dynamisch vergibt?
2. Welche Angaben der Tabelle in `vergleich.py` wurden im Lauf geprüft?
3. Warum zeigt `df` für ein neues ext4 weniger nutzbaren Platz als die Imagegröße?
4. Welche Werkzeuge prüfen ext4 und XFS?

### Modul 4: Dateisysteme vergrößern und verkleinern

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein ext4- und ein XFS-Dateisystem nach der Vergrößerung des Datenträgers anpassen.
  * Nach Abschluss dieses Moduls kann der Lernende ein ext4-Dateisystem sicher verkleinern (prüfen, verkleinern).
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum XFS nicht verkleinert wird.
  * Nach Abschluss dieses Moduls kann der Lernende einen Ablaufplan mit Sicherung und Rückfallweg schreiben.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | ext4 und XFS nach der Vergrößerung des Datenträgers anpassen (`vergroessern.sh`) | 4 |
| 4.2 | ext4 verkleinern: Reihenfolge und Risiko (`vergroessern.sh`) | 3 |
| 4.3 | XFS verkleinern: Einschränkung beobachten (`vergroessern.sh`) | 2 |
| 4.4 | Mit LVM: `lvextend -r` und `lvreduce` im Zusammenhang (Fachwissen, nicht ausgeführt) | 3 |
| 4.5 | Ablaufplan für eine Vergrößerung auf `lv01` schreiben | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vergrößern (Einheit 4.1):** Führen Sie `bash vergroessern.sh` aus. Erklären Sie die Reihenfolge: zuerst den Datenträger vergrößern, dann das Dateisystem anpassen (`resize2fs`, `xfs_growfs`), und was `df` vorher und nachher zeigt.
2. **ext4 verkleinern (Einheit 4.2):** Erklären Sie Abschnitt 4: Warum muss ext4 zum Verkleinern ausgehängt und mit `e2fsck -f` geprüft werden? Prüfen Sie, dass die 20-MiB-Datei erhalten bleibt.
3. **XFS verkleinern (Einheit 4.3):** Erklären Sie Abschnitt 5: Was meldet `xfs_growfs -D`, und welche Wege gibt es, ein XFS-Dateisystem kleiner zu bekommen (Fachwissen)?
4. **Mit LVM (Einheit 4.4):** Lesen Sie die Vorgehensweise in der Erweiterung und schreiben Sie auf, in welcher Reihenfolge Logical Volume und Dateisystem beim Vergrößern und beim Verkleinern bearbeitet werden müssen. Kennzeichnen Sie, was nicht geprüft ist.
5. **Ablaufplan (Einheit 4.5):** Schreiben Sie einen Ablaufplan für die Vergrößerung von `daten` auf `lv01` mit Sicherung, Prüfung, Durchführung und Kontrolle.

#### Kontrollfragen

1. In welcher Reihenfolge werden Datenträger und Dateisystem beim Vergrößern bearbeitet?
2. Warum ist Verkleinern riskanter als Vergrößern?
3. Warum wurde ext4 im Lauf ausgehängt vergrößert?
4. Was meldete `xfs_growfs -D` beim Verkleinern?

### Modul 5: Mount-Optionen und fstab

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung von `noexec` und `ro` und den Weg über `remount` beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die sechs Felder einer `fstab`-Zeile nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine `fstab` mit `findmnt --verify` und eigenen Prüfungen kontrollieren.
  * Nach Abschluss dieses Moduls kann der Lernende Optionen für ein Datenverzeichnis begründen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Optionen `noexec`, `ro` und `remount` beobachten (`mount_optionen.sh`) | 4 |
| 5.2 | Aufbau der `fstab`: sechs Felder, UUID statt Gerätename (Fachwissen, `fstab_pruefen.py`) | 3 |
| 5.3 | `fstab` prüfen mit `findmnt --verify` (`mount_optionen.sh`) | 2 |
| 5.4 | Sichere Standardoptionen für Datenverzeichnisse planen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Optionen beobachten (Einheit 5.1):** Führen Sie `bash mount_optionen.sh` aus. Erklären Sie, warum das Skript mit `noexec` nicht läuft, wie `ro` das Schreiben verhindert und was `remount` ändert.
2. **fstab-Zeilen prüfen (Einheit 5.2):** Führen Sie `python3 fstab_pruefen.py` aus. Erklären Sie jede Warnung und korrigieren Sie die fehlerhaften Zeilen.
3. **fstab verifizieren (Einheit 5.3):** Erklären Sie die Ausgabe von `findmnt --verify` in Abschnitt 5: Welche zwei Fehler meldet das Werkzeug, und warum ist die Prüfung vor dem Neustart wichtig?
4. **Optionen planen (Einheit 5.4):** Planen Sie für `/daten`, `/var/log` und `/backup` jeweils Dateisystem und Mount-Optionen (z. B. `noexec`, `nosuid`, `nodev`) und begründen Sie die Wahl.

#### Kontrollfragen

1. Welche sechs Felder hat eine `fstab`-Zeile?
2. Was bewirkt `noexec`, und was bewirkt es nicht?
3. Warum kann ein Fehler in der `fstab` das Starten des Systems verhindern?
4. Worin unterscheidet sich `mount -o remount` von aus- und wieder einhängen?

### Modul 6: Quotas

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen weicher und harter Grenze erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Quota-Befehle für ext4 und XFS lesen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Quotas für einen Dateiserver planen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Weiche und harte Grenze, Karenzzeit im Modell (`quota_modell.py`) | 4 |
| 6.2 | Quota-Befehle für ext4 und XFS lesen (`beispiel_quota.txt`, nicht ausgeführt) | 4 |
| 6.3 | Quotas planen: Benutzer, Gruppen, Projekte und Verzeichnisse | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Modell (Einheit 6.1):** Führen Sie `python3 quota_modell.py` aus. Erklären Sie die Entscheidungen bei 5, 12 und 16 MB und die Wirkung der Karenzzeit.
2. **Befehle lesen (Einheit 6.2):** Lesen Sie `beispiel_quota.txt` und erklären Sie jeden Befehl für ext4 und für XFS. Führen Sie sie auf `lv01` aus und vergleichen Sie die Ergebnisse mit Ihren Erwartungen.
3. **Quotas planen (Einheit 6.3):** Planen Sie für einen Dateiserver mit 500 GB Quotas für 20 Benutzer und drei Projektverzeichnisse; legen Sie weiche und harte Grenzen fest und begründen Sie sie.

#### Kontrollfragen

1. Was geschieht bei Überschreiten der weichen und was bei Überschreiten der harten Grenze?
2. Wozu dient die Karenzzeit?
3. Worin unterscheiden sich Benutzer-, Gruppen- und Projekt-Quota?

### Modul 7: Fehlerdiagnose und Reparatur

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Dateisystem im Nur-Lesen-Modus prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler in ext4 mit `e2fsck` und in XFS mit `xfs_repair` beheben.
  * Nach Abschluss dieses Moduls kann der Lernende die Exitcodes von `e2fsck` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Vorgehen bei Dateisystemfehlern festlegen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | ext4 beschädigen und mit `e2fsck` reparieren (`fsck_ext4.sh`) | 4 |
| 7.2 | Exitcodes von `e2fsck` lesen (`fsck_ext4.sh`) | 2 |
| 7.3 | XFS prüfen und reparieren (`xfs_repair.sh`) | 4 |
| 7.4 | Vorgehen bei Dateisystemfehlern: Sicherung, Nur-Lesen-Prüfung, Reparatur | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **ext4 reparieren (Einheit 7.1):** Führen Sie `bash fsck_ext4.sh` aus. Erklären Sie jede Phase von `e2fsck`, den gemeldeten Fehler (Linkzähler) und die Wirkung von `-n` und `-y`.
2. **Exitcodes (Einheit 7.2):** Erklären Sie die Exitcodes 4 und 1 aus den Abschnitten 3 und 4 und warum ein Skript sie auswerten sollte.
3. **XFS reparieren (Einheit 7.3):** Führen Sie `bash xfs_repair.sh` aus. Erklären Sie, was „bad primary superblock“ und „found candidate secondary superblock“ bedeuten.
4. **Vorgehen festlegen (Einheit 7.4):** Schreiben Sie eine Anleitung für den Fall „Dateisystem lässt sich nicht einhängen“: Sicherung des Images, Nur-Lesen-Prüfung, Reparatur, Kontrolle, Dokumentation.

#### Kontrollfragen

1. Warum soll ein Dateisystem vor der Prüfung ausgehängt sein?
2. Was ist der Unterschied zwischen `e2fsck -n` und `e2fsck -y`?
3. Was bedeutet Exitcode 4 bei `e2fsck`?
4. Wie findet `xfs_repair` ein Dateisystem, dessen primärer Superblock zerstört ist?

### Modul 8: Überwachung des Speicherplatzes

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Platz und Inodes mit `df` und `df -i` lesen und die Ursache von „No space left on device“ bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende mit `du` und `find` Platzverbraucher finden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Prüfskript mit Warn- und Kritisch-Schwelle und Exitcode lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Software-RAID und LVM-Snapshots als Überblick einordnen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Platz und Inodes mit `df` lesen, „No space left“ trotz freiem Platz (`platz.sh`) | 4 |
| 8.2 | Größte Verzeichnisse und Dateien finden (`du`, `find`, `platz.sh`) | 2 |
| 8.3 | Schwellenwerte prüfen: Skript mit Exitcode (`schwelle.py`) | 3 |
| 8.4 | Software-RAID und LVM-Snapshots im Überblick (`beispiel_mdadm_snapshot.txt`, nicht ausgeführt) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Platz und Inodes (Einheit 8.1):** Führen Sie `bash platz.sh` aus. Erklären Sie, warum `touch` bei 15 MiB freiem Platz mit „No space left on device“ scheitert, und wie `df -i` die Ursache zeigt.
2. **Platzverbraucher finden (Einheit 8.2):** Erklären Sie die Befehle `du -ak … | sort -rn` und `find -size +2M` aus Abschnitt 4.
3. **Schwellen prüfen (Einheit 8.3):** Führen Sie `python3 schwelle.py` aus. Erklären Sie die Schwellen 80 % und 90 %, die Exitcodes 0, 1, 2 und warum `/backup` bei 45 % Platz kritisch ist.
4. **Überblick (Einheit 8.4):** Lesen Sie `beispiel_mdadm_snapshot.txt` und erklären Sie, wozu `mdadm` und ein LVM-Snapshot dienen und was sie nicht ersetzen. Kennzeichnen Sie, was nicht geprüft ist.

#### Kontrollfragen

1. Wie kann ein Dateisystem „voll“ sein, obwohl `df -h` freien Platz zeigt?
2. Welche Schwellen und Exitcodes verwendet `schwelle.py`?
3. Warum ersetzt RAID keine Datensicherung?
4. Wozu dient ein LVM-Snapshot, und was begrenzt seine Lebensdauer?
