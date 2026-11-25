# Lehrplan: LPIC-1

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und grundlegende Linux-Kommandozeilen-Kenntnisse |
| **Gesamtumfang** | 12 Module, 112 UE (zu 45 Minuten; 84 Stunden) |
| **Fokus-Technologien** | Linux-Administration (Prüfungsvorbereitung LPIC-1), Debian/Ubuntu Linux; RPM-Werkzeuge im Vergleich |
| **Thematische Abgrenzung (Out of Scope)** | Der Kurs „Linux Essentials“ im selben Repository behandelt die Einstiegsstufe; LPIC-2 und LPIC-3 bauen darauf auf. Netzwerkdienste wie DNS, Web, Samba und Mail sind LPIC-2. Containern und Virtualisierung widmen sich LPIC-3 und andere Kurse. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | LPIC-1 Grundlagen und Linux System Architecture | 1 | 8 |
| 2 | Linux Installation, Partitionierung und Boot Management | 1 | 10 |
| 3 | Package Management Debian und RPM/YUM | 1 | 9 |
| 4 | GNU/Unix Command Line Essentials | 1 | 10 |
| 5 | Processes, Text Processing und Regular Expressions | 1 | 10 |
| 6 | Filesystems, Permissions und FHS | 1 | 10 |
| 7 | Shells, Bash Environment und Scripting | 1 | 9 |
| 8 | User Interfaces, X11 und Accessibility | 2 | 7 |
| 9 | Administrative Tasks und Localisation | 1 | 10 |
| 10 | Essential System Services | 1 | 9 |
| 11 | Networking Fundamentals und Client DNS | 1 | 10 |
| 12 | Security und LPIC-1 Exam Readiness | 1 | 10 |
| **Gesamt** | 12 Module | 11 × Priorität 1, 1 × Priorität 2 | **112** |

**Priorität 1** (Pflicht) sind alle Module außer Modul 8. **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 8 (Benutzeroberflächen, X11 und Barrierefreiheit). Fällt Modul 8 weg, verringert sich der Gesamtumfang von 112 auf 105 UE.

### 2. Quellen

**Gelesen (lpi.org, 25.11.2026):** Die Seite „Exam 101 Objectives“ nennt für LPIC-1 die Prüfungen 101-500 und 102-500, Version 5.0 der Prüfungsziele („currently released“) und die Themenbereiche 101 bis 110 (System Architecture; Linux Installation and Package Management; GNU and Unix Commands; Devices, Linux Filesystems, Filesystem Hierarchy Standard; Shells and Shell Scripting; User Interfaces and Desktops; Administrative Tasks; Essential System Services; Networking Fundamentals; Security). Die Seite nennt keine Nachfolgeversion.

**Zuordnung (meine Annahme, nur auf Ebene der Themenüberschriften):** Modul 1 zu 101, Modul 2 und 3 zu 102, Modul 4 und 5 zu 103, Modul 6 zu 104, Modul 7 zu 105, Modul 8 zu 106, Modul 9 zu 107, Modul 10 zu 108, Modul 11 zu 109, Modul 12 zu 110.

**Nicht gelesen:** Die einzelnen Prüfungsziele (Nummern, Gewichtungen, Wissensgebiete) von Version 5.0 und alle weiteren Quellen. Aussagen zu Befehlen, Dateien und Pfaden sind Fachwissen, soweit sie nicht im Container ausgeführt wurden, und **nicht bestätigt**. Prüfungsfragen werden nicht wiedergegeben. **Getestet mit (Ubuntu 24.04.5, Cloud-Container, root, ohne systemd als init):** Bash 5.2, GNU coreutils, util-linux, e2fsprogs, dpkg/apt, RPM 4.18.2, Xvfb, rsyslog, logrotate, Postfix 3.8.6 (nur Konfiguration), OpenSSH, GnuPG, iproute2.

### 3. Labor-Setup & Rahmenbedingungen

**Labor laut Lehrplan:** Eine Linux-Server-VM (Debian oder Ubuntu Server) und eine Linux-Client-VM auf einem privaten Hyper-V-Switch ohne Verbindung zum Heimnetz; Snapshots vor jeder Übung mit Partitionen, Benutzern oder Netzwerk. Das Hyper-V-Labor wurde **nicht** aufgebaut.

**Skripte:** Alle Übungsskripte laufen unter Linux als root im Sandkasten `/tmp/lpic1` (Image-Dateien auf Loop-Geräten, eigene Namensräume, eigene `--root`-Verzeichnisse) und räumen am Ende auf; sie verändern weder echte Platten noch die echten Benutzerdateien. **Nie auf einem Produktivsystem ausführen.** `shutdown`, `reboot`, `halt` und `poweroff` werden nirgends aufgerufen.

## B. Detaillierter Modulaufbau

### Modul 1: LPIC-1 Grundlagen und Linux System Architecture

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rolle und Aufbau der Zertifizierung LPIC-1 nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Hardware, Kernel, Module und udev in einer Ausgabe wiederfinden.
  * Nach Abschluss dieses Moduls kann der Lernende die Stufen des Bootprozesses von der Firmware bis zu init/systemd benennen.
  * Nach Abschluss dieses Moduls kann der Lernende systemd-Targets den klassischen Runlevels zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Befehle zum Herunterfahren kennen, ohne sie im Labor auszuführen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | LPIC-1 Rollenbild | 1 |
| 1.2 | Linux System Architecture | 1 |
| 1.3 | Kernel und Modules | 1 |
| 1.4 | udev und device discovery | 1 |
| 1.5 | Bootprozess | 1 |
| 1.6 | runlevels und systemd targets | 1 |
| 1.7 | Shutdown und Reboot | 1 |
| 1.8 | Architecture Troubleshooting | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rolle und Architektur (Einheiten 1.1 und 1.2):** Beschreibe in drei Sätzen, wofür LPIC-1 steht und welche beiden Prüfungen dazugehören. Führe danach `bash architektur.sh` aus und ordne in Schritt 1 Architektur, Anzahl der CPUs, Arbeitsspeicher und Auslagerungsspeicher der Ausgabe zu.
2. **Kernel, Module und udev (Einheiten 1.3 und 1.4):** Erkläre anhand von Schritt 2 und 3, was ein Kernel-Modul ist und warum `modinfo loop` im Container scheitert. Beschreibe, was `udevadm info` über `/dev/null` meldet und welche Aufgabe udev beim Erkennen von Geräten hat.
3. **Bootprozess und Targets (Einheiten 1.5 und 1.6):** Beschreibe anhand von Schritt 4 und 5 die Stufen vom Einschalten bis zu `init`. Ordne mit der Ausgabe der Runlevel-Verknüpfungen die Targets `graphical`, `multi-user` und `reboot` den Runlevels 5, 3 und 6 zu und erkläre, warum `who -r` im Container nichts liefert.
4. **Herunterfahren und Fehlersuche (Einheiten 1.7 und 1.8):** Nenne nach Schritt 6, welche Befehle zum Herunterfahren existieren und warum das Skript sie nur mit `--help` aufruft. Beschreibe ein Vorgehen, mit dem du ein System eingrenzt, das nach einem Kernel-Update nicht mehr startet (Firmware, Bootloader, Kernel, init).

#### Kontrollfragen

1. Was meldet `ps -p 1` im Container, und was wäre auf einer normalen Installation zu erwarten?
2. Wodurch erkennt man im Skript, dass kein UEFI-Zugriff besteht?
3. Welchem Runlevel entspricht `graphical.target`?
4. Welche Aufgabe hat udev?

### Modul 2: Linux Installation, Partitionierung und Boot Management

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Partitionstabelle (GPT) in einer Image-Datei anlegen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende ext4 und Swap auf einem Loop-Gerät erstellen und einhängen.
  * Nach Abschluss dieses Moduls kann der Lernende Bezeichner (Label, Typ) mit `blkid` abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende gemeinsame Bibliotheken mit `ldd` und `ldconfig` untersuchen.
  * Nach Abschluss dieses Moduls kann der Lernende GRUB 2 einordnen und erkennen, ob ein System virtualisiert läuft.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Disk Layout Design | 1,25 |
| 2.2 | Partitionierung | 1,25 |
| 2.3 | Filesystems erstellen | 1,25 |
| 2.4 | Mount Grundlagen | 1,25 |
| 2.5 | GRUB2 Installation | 1,25 |
| 2.6 | Shared Libraries | 1,25 |
| 2.7 | Virtualization Guest Basics | 1,25 |
| 2.8 | Installation Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Layout und Partitionstabelle (Einheiten 2.1 und 2.2):** Entwirf ein Plattenlayout für einen kleinen Server (`/boot`, `/`, `/home`, `/var`, Swap) mit Begründung. Führe `bash partition.sh` aus und lies die GPT-Tabelle in Schritt 1: Start, Ende, Größe und Typ beider Partitionen.
2. **Dateisystem und Mount (Einheiten 2.3 und 2.4):** Erkläre in Schritt 2 und 3, was `mkfs.ext4 -q -L daten`, `mkswap` und `mount` bewirken und was `blkid` über Label und Typ meldet. Nenne den Unterschied zwischen einem Bezeichner wie `/dev/loop0` und einem Label.
3. **GRUB 2 und Bibliotheken (Einheiten 2.5 und 2.6):** Erkläre anhand von Schritt 5, warum im Container keine GRUB-Werkzeuge vorhanden sind und was `grub-install` und `grub-mkconfig` auf einer VM täten. Lies in Schritt 4 die Bibliotheken von `ls` und erkläre die Aufgabe von `ldconfig`.
4. **Gast und Fehlersuche (Einheiten 2.7 und 2.8):** Erkläre, woran Schritt 5 erkennt, dass Linux als Gast läuft (`hypervisor`-Flag, `systemd-detect-virt`). Beschreibe ein Vorgehen, wenn die Installation nach dem Partitionieren nicht bootet (Bootloader fehlt, falsche Partition, EFI-Partition fehlt).

#### Kontrollfragen

1. Welche Typen haben die beiden Partitionen in Schritt 1?
2. Was zeigt `blkid` für das Loop-Gerät mit Label „daten“?
3. Welchen Zweck hat `ldconfig`?
4. Wodurch unterscheidet sich eine Bibliothek in `ldd`-Ausgabe von einem Programm?

### Modul 3: Package Management Debian und RPM/YUM

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Pakete mit `dpkg` und `apt-cache` abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Paket herunterladen, inspizieren und entpacken, ohne es zu installieren.
  * Nach Abschluss dieses Moduls kann der Lernende Abhängigkeiten und Gegenabhängigkeiten ermitteln.
  * Nach Abschluss dieses Moduls kann der Lernende ein RPM-Paket bauen, abfragen, installieren und überprüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Bedeutung von `dnf`/`yum` gegenüber `apt` einordnen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Debian Package Basics | 1 |
| 3.2 | APT | 1 |
| 3.3 | APT Repositories | 1,25 |
| 3.4 | RPM Basics | 1 |
| 3.5 | YUM/DNF | 1,25 |
| 3.6 | Package Queries | 1 |
| 3.7 | Dependency Management | 1 |
| 3.8 | Package Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **dpkg und apt abfragen (Einheiten 3.1 und 3.2):** Führe `bash pakete.sh` aus. Erkläre in Schritt 1, was `dpkg -s`, `dpkg -S` und `dpkg -L` liefern und warum `dpkg -S /bin/ls` nichts findet, `dpkg -S /usr/bin/ls` aber schon. Beschreibe in Schritt 2 den Kandidaten und die Versionstabelle von `apt-cache policy`.
2. **Paketquellen und RPM (Einheiten 3.3 und 3.4):** Erkläre, wo APT seine Paketquellen konfiguriert. Baue anhand von Schritt 5 das Demopaket, lies mit `rpm -qpi` und `rpm -qpl` seine Daten und installiere es in das Testverzeichnis `rroot`.
3. **YUM/DNF und Abfragen (Einheiten 3.5 und 3.6):** Erkläre, wofür `yum` und `dnf` bei RPM-Systemen stehen und warum sie hier nicht vorhanden sind. Lies in Schritt 5 aus, welche Datei dem Paket gehört (`rpm -qf`) und wie sich `rpm -V` nach einer Änderung verhält.
4. **Abhängigkeiten und Fehlersuche (Einheiten 3.7 und 3.8):** Erkläre anhand von Schritt 4 `apt-cache depends`, `rdepends` und die Simulation `apt-get -s`. Beschreibe die Schritte bei einem Fehler wie „unmet dependencies“ oder gesperrter Paketdatenbank.

#### Kontrollfragen

1. Warum findet `dpkg -S /bin/ls` kein Paket?
2. Was zeigt `rpm -V` nach einer Änderung an der Datei?
3. Wodurch unterscheidet sich `apt-get download` von `apt-get install`?
4. Was bewirkt `apt-get -s install tree`?

### Modul 4: GNU/Unix Command Line Essentials

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Umgebungsvariablen setzen, exportieren und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien kopieren, verschieben und löschen.
  * Nach Abschluss dieses Moduls kann der Lernende Text mit `cut`, `sort`, `uniq`, `tr` und `wc` filtern.
  * Nach Abschluss dieses Moduls kann der Lernende Pipes und Umleitungen für Standardausgabe und Standardfehlerausgabe einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Rückgabewerte und typische Fehler an der Befehlszeile lesen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Shell Basics | 1,25 |
| 4.2 | Environment | 1,25 |
| 4.3 | File Management | 1,25 |
| 4.4 | Text anzeigen | 1,25 |
| 4.5 | Text Filter | 1,25 |
| 4.6 | Pipes | 1,25 |
| 4.7 | Redirection | 1,25 |
| 4.8 | CLI Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Shell und Umgebung (Einheiten 4.1 und 4.2):** Führe `bash befehlszeile.sh` aus. Erkläre in Schritt 1, warum `FOO` in der Kindshell leer, `BAR` aber gesetzt ist, und was `type cd ls` über eingebaute Befehle und Programme sagt.
2. **Dateien und Text (Einheiten 4.3 und 4.4):** Beschreibe die Wirkung von `cp`, `mv` und `rm -r` in Schritt 2 und lies in Schritt 3 mit `cat`, `head`, `tail` und `cut` Teile der CSV-Datei.
3. **Filter und Pipes (Einheiten 4.5 und 4.6):** Erkläre die Pipeline `cut -d';' -f1 | sort | uniq -c` und `sort -t';' -k2 -n -r` in Schritt 3. Nenne, was `tr 'a-c' 'A-C'` und `wc -l` tun.
4. **Umleitung und Fehlersuche (Einheiten 4.7 und 4.8):** Erkläre in Schritt 4 den Unterschied zwischen `>`, `2>`, `&>`, `>>` und `tee`. Erkläre in Schritt 5 den Rückgabewert 1 und warum `FALSCH=1 bash -c ...` die Variable nur für diesen Aufruf setzt.

#### Kontrollfragen

1. Warum ist `FOO` in der Kindshell leer?
2. Was bewirkt `2>` im Unterschied zu `>`?
3. Wofür steht Rückgabewert 1 nach `cat nichtda.txt`?
4. Was macht `uniq -c` und warum steht davor `sort`?

### Modul 5: Processes, Text Processing und Regular Expressions

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Prozesse mit `ps` und `pgrep` auflisten und den Zustand lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Signale senden und Rückgabewerte nach Signalen deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Hintergrundjobs steuern.
  * Nach Abschluss dieses Moduls kann der Lernende Prioritäten mit `nice` und `renice` setzen.
  * Nach Abschluss dieses Moduls kann der Lernende Text mit `grep`, `sed`, `awk` und im Stapelbetrieb mit `ex` bearbeiten.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Process Listing | 1,25 |
| 5.2 | Signals und kill | 1,25 |
| 5.3 | Job Control | 1,25 |
| 5.4 | Priorities | 1,25 |
| 5.5 | grep und Regex | 1,25 |
| 5.6 | sed und awk Basics | 1,25 |
| 5.7 | vi/vim Basics | 1,25 |
| 5.8 | Process/Text Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prozesse und Signale (Einheiten 5.1 und 5.2):** Führe `bash prozesse.sh` aus. Lies in Schritt 1 und 2 den Zustand des `sleep`-Prozesses (`S`, `T`) und erkläre, warum der Rückgabewert nach `kill -TERM` 143 ist. Nenne die Nummern der Signale TERM, KILL und CONT aus der Ausgabe von `kill -l`.
2. **Jobs und Prioritäten (Einheiten 5.3 und 5.4):** Erkläre in Schritt 3 die Ausgabe von `jobs` und das Beenden mit `kill %1`. Beschreibe in Schritt 4 die Wirkung von `nice -n 10` und `renice -n 15` auf die Spalte `NI` in `ps`.
3. **grep, sed und awk (Einheiten 5.5 und 5.6):** Erkläre in Schritt 5 und 6 die Ausdrücke `grep -E 'Failed|Accepted'`, `grep -oE` und `grep -v`. Beschreibe die Wirkung von `sed 's/10\.0\.0\./NETZ./'` und von `awk '/Failed/ {n[$11]++} ...'`.
4. **vi im Stapelbetrieb und Fehlersuche (Einheiten 5.7 und 5.8):** Erkläre in Schritt 7, was `ex -s` mit den Befehlen `%s/alt/neu/g`, `2d` und `wq` mit der Datei macht. Beschreibe die Schritte, mit denen du einen hängenden Prozess behandelst (Signalreihenfolge TERM vor KILL).

#### Kontrollfragen

1. Wofür steht der Zustand `T` in `ps`?
2. Was bedeutet Rückgabewert 143?
3. Welche Nice-Werte stehen vor und nach `renice` in der Ausgabe?
4. Was bewirkt `grep -v sshd`?

### Modul 6: Filesystems, Permissions und FHS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Dateisystem mit `e2fsck` und `tune2fs` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Mount-Optionen (`noexec`, `ro`, `nosuid`) setzen und ihre Wirkung beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende Belegung mit `df` und `du` ermitteln.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte, Besitzer, Setgid und Sticky-Bit setzen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende harte und symbolische Links unterscheiden und die Verzeichnisse des FHS nennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Filesystem Integrity | 1,25 |
| 6.2 | Mount und /etc/fstab | 1,25 |
| 6.3 | Mount Options | 1,25 |
| 6.4 | Disk Usage | 1,25 |
| 6.5 | Permissions | 1,25 |
| 6.6 | Ownership und Special Bits | 1,25 |
| 6.7 | Links und FHS | 1,25 |
| 6.8 | Filesystem Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prüfung, Mount und fstab (Einheiten 6.1 und 6.2):** Führe `bash dateisystem.sh` aus. Lies in Schritt 1 das Ergebnis von `e2fsck -fn` und `tune2fs -l`. Erkläre in Schritt 2, welche Zeile in `/etc/fstab` zu den Optionen `noexec,nosuid` gehören würde, und warum der Aufruf von `prog.sh` scheitert.
2. **Mount-Optionen und Belegung (Einheiten 6.3 und 6.4):** Beschreibe die Wirkung von `remount,ro` (Schritt 2) und lies in Schritt 3 mit `df` und `du` Größe, Belegung und Inodes. Nenne den Unterschied zwischen `df` und `du`.
3. **Rechte, Besitzer und Sonderbits (Einheiten 6.5 und 6.6):** Erkläre in Schritt 4 die Oktalwerte 640, 750 und 600 aus `umask 077`, Setgid auf einem Verzeichnis (`drwxr-s---`) und das Sticky-Bit (`drwxrwxrwt`). Erkläre, wie `chown nobody:nogroup` wirkt.
4. **Links, FHS und Fehlersuche (Einheiten 6.7 und 6.8):** Erkläre in Schritt 5 den Unterschied zwischen hartem und symbolischem Link nach dem Löschen des Originals. Nenne zu fünf Verzeichnissen des Dateisystem-Hierarchie-Standards ihren Zweck. Beschreibe die Schritte bei „Read-only file system“ und „No space left on device“.

#### Kontrollfragen

1. Wodurch scheitert der Start von `prog.sh` in Schritt 2?
2. Warum funktioniert der harte Link nach `rm original`, der symbolische nicht?
3. Was bewirkt das Setgid-Bit auf einem Verzeichnis?
4. Was zeigt das Sticky-Bit (`t`) bei `/tmp`?

### Modul 7: Shells, Bash Environment und Scripting

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aliase und Funktionen in einer Startdatei definieren.
  * Nach Abschluss dieses Moduls kann der Lernende ein Skript mit Variablen, Parametern, Schleifen und `case` schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Befehlsersetzung `$(...)` und Arithmetik `$((...))` einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende mit `set -euo pipefail` und `trap` robuste Skripte schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Skripte mit `bash -n`, `bash -x` und `shellcheck` prüfen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Shell Environment Customizing | 1 |
| 7.2 | Aliases und Functions | 1 |
| 7.3 | Script Basics | 1,25 |
| 7.4 | Variables und Parameters | 1 |
| 7.5 | Control Flow | 1,25 |
| 7.6 | Command Substitution | 1 |
| 7.7 | Script Robustness | 1 |
| 7.8 | Scripting Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Umgebung, Aliase, Funktionen (Einheiten 7.1 und 7.2):** Führe `bash skripte.sh` aus. Erkläre in Schritt 1, wie die Startdatei `rc.sh` Aliase, eine Funktion und eine exportierte Variable setzt und welche Dateien auf einem echten System dafür zuständig sind (`~/.bashrc`, `~/.profile`).
2. **Skriptgrundlagen und Variablen (Einheiten 7.3 und 7.4):** Lies `demo.sh` in Schritt 2: Wofür stehen `$0`, `$#`, `$1` und `${1:-Welt}`? Erkläre die Ausgabe beim Aufruf ohne und mit Parameter.
3. **Kontrollfluss und Ersetzung (Einheiten 7.5 und 7.6):** Beschreibe `if`, `for`, `case` und `while` in `demo.sh` und die Ausgabe `1 4 9`. Erkläre `$(date -u +%Y)` und `${#heute}`.
4. **Robustheit und Fehlersuche (Einheiten 7.7 und 7.8):** Erkläre in Schritt 3 die Wirkung von `set -euo pipefail` und `trap ... EXIT` sowie die Rückgabewerte 1 und 127. Lies in Schritt 4 die Warnungen von `shellcheck` zu `schlecht.sh` und erkläre `bash -n` und `bash -x`.

#### Kontrollfragen

1. Was ist `$#` in einem Skript?
2. Was bewirkt `set -u`?
3. Wozu dient `trap ... EXIT`?
4. Was findet `shellcheck` an `for f in $(ls *.txt)`?

### Modul 8: User Interfaces, X11 und Accessibility

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen X-Server (Xvfb) starten und mit `xdpyinfo` abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende die Variable `DISPLAY` und die Datei `XAUTHORITY` erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Display-Manager, Desktop-Umgebungen und Sitzungstypen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Barrierefreiheit als Aufgabe der Benutzeroberfläche einordnen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | X11 Grundlagen | 0,75 |
| 8.2 | X11 Konfiguration | 0,75 |
| 8.3 | Display Manager | 1 |
| 8.4 | Graphical Desktops | 1 |
| 8.5 | Remote X Concepts | 1 |
| 8.6 | Accessibility | 0,75 |
| 8.7 | GUI Troubleshooting | 1 |
| 8.8 | Exam Focus | 0,75 |

#### Praxisaufgaben (Hands-on Lab)

1. **X11 und Konfiguration (Einheiten 8.1 und 8.2):** Führe `bash grafik.sh` aus. Erkläre in Schritt 1 und 2, was Xvfb ist und was `xdpyinfo` über Anzeige, Auflösung (800x600) und Farbtiefe meldet. Beschreibe, wie der Client über `DISPLAY` den Server findet.
2. **Display-Manager und Desktops (Einheiten 8.3 und 8.4):** Lies in Schritt 4, warum es im Container keine Sitzungsdateien (`xsessions`) und keinen Display-Manager gibt. Nenne die Aufgabe eines Display-Managers und zwei Desktop-Umgebungen.
3. **Remote-X und Barrierefreiheit (Einheiten 8.5 und 8.6):** Erkläre in Schritt 3, welche Aufgabe `xauth` und das Cookie `MIT-MAGIC-COOKIE-1` für den Zugriff über das Netzwerk haben. Nenne zwei Hilfen der Barrierefreiheit auf einem Linux-Desktop.
4. **Fehlersuche und Prüfungsfokus (Einheiten 8.7 und 8.8):** Beschreibe, wie du vorgehst, wenn ein X-Programm „cannot open display“ meldet (DISPLAY, Server läuft, Cookie). Nenne Schritt 5 als Beispiel für das saubere Beenden des Servers.

#### Kontrollfragen

1. Was sagt `DISPLAY=:77` aus?
2. Wozu dient `xauth`?
3. Welche Aufgabe hat ein Display-Manager?
4. Warum gibt es im Container kein `xsessions`-Verzeichnis?

### Modul 9: Administrative Tasks und Localisation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Gruppen und Benutzer in einem Sandkasten anlegen, ändern und löschen.
  * Nach Abschluss dieses Moduls kann der Lernende die Dateien `passwd`, `shadow` und `group` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Skeleton-Verzeichnis, `login.defs` und Kennwortalterung (`chage`) einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Cron-Zeilen schreiben und auf Syntax prüfen; `at` und `anacron` abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Sprache, Zeitzone und Zeichensatz einordnen.
* **Voraussetzungen:** Modul 8 oder Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | User Accounts | 1,25 |
| 9.2 | Group Management | 1,25 |
| 9.3 | Account Files | 1,25 |
| 9.4 | Skeleton und Defaults | 1,25 |
| 9.5 | Cron | 1,25 |
| 9.6 | at und anacron | 1,25 |
| 9.7 | Localisation | 1,25 |
| 9.8 | Admin Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Benutzer und Gruppen (Einheiten 9.1 und 9.2):** Führe `bash benutzer.sh` aus. Erkläre in Schritt 1 die Befehle `groupadd`, `useradd` und `usermod` mit `-R` (Sandkasten) und lies in Schritt 2 die Zeilen für `ana` und `ben` in `passwd` und `group`. Nenne die sieben Felder von `passwd`.
2. **Kontodateien, Skeleton, Standards (Einheiten 9.3 und 9.4):** Erkläre, warum `shadow` den Wert `$6$labsalt$...` enthält und `ben` ein `!` hat, und warum `passwd` die Rechte 644, `shadow` aber 640 hat. Lies in Schritt 3 das Skeleton, `UID_MIN` und `PASS_MAX_DAYS`.
3. **Cron, at und anacron (Einheiten 9.5 und 9.6):** Erkläre die Cron-Zeile `30 2 * * 1-5 /usr/local/bin/sicherung.sh`. Erkläre in Schritt 6, wie `crontab -n` einen Fehler wie „bad minute“ anzeigt und wofür `at` und `anacron` verwendet werden.
4. **Lokalisierung und Fehlersuche (Einheiten 9.7 und 9.8):** Erkläre in Schritt 7 die Locale `C.UTF-8`, die Umstellung der Zeitzone mit `TZ=Europe/Vienna` (CEST/CET) und die Zeichenumsetzung mit `iconv`. Beschreibe ein Vorgehen, wenn sich ein Benutzer nicht anmelden kann (Konto gesperrt, Shell, Kennwortablauf, Heimatverzeichnis).

#### Kontrollfragen

1. Wie viele Felder hat eine Zeile in `/etc/passwd`, und welche ist die UID?
2. Wofür steht `!` im Kennwortfeld von `shadow`?
3. Welche Zeit meint `30 2 * * 1-5`?
4. Was bewirkt `chage -M 90`?

### Modul 10: Essential System Services

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zeitzonen und die Konfiguration der Zeitsynchronisation (chrony) lesen.
  * Nach Abschluss dieses Moduls kann der Lernende rsyslog mit eigener Konfiguration prüfen und Meldungen mit `logger` erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende Logrotation mit `logrotate -d` und `-f` nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Werte eines Mail-Transport-Agenten (Postfix) und Aliase lesen.
  * Nach Abschluss dieses Moduls kann der Lernende eine systemd-Unit prüfen und den Status von Diensten einordnen.
* **Voraussetzungen:** Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | System Time | 1 |
| 10.2 | Time Synchronization | 1 |
| 10.3 | System Logging | 1,25 |
| 10.4 | Log Rotation | 1 |
| 10.5 | MTA Basics | 1,25 |
| 10.6 | Printing Basics | 1 |
| 10.7 | Service Management | 1 |
| 10.8 | Service Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zeit und Synchronisation (Einheiten 10.1 und 10.2):** Führe `bash dienste.sh` aus. Erkläre in Schritt 1 und 2 die Zeitumstellung (`01:30 UTC` ergibt `03:30 CEST`) und was `chronyd -p` mit `pool`, `makestep` und `rtcsync` aus der Konfiguration liest. Erkläre, warum `timedatectl` und `hwclock` im Container nicht laufen.
2. **Protokollierung und Rotation (Einheiten 10.3 und 10.4):** Erkläre in Schritt 3 die Regeln `local0.*` und `*.warning` der rsyslog-Konfiguration und lies, in welcher Datei die zwei `logger`-Meldungen landen. Beschreibe in Schritt 4 die Direktiven `rotate 2`, `size 1k`, `compress` und die Datei `app.log.1.gz`.
3. **Mail und Drucken (Einheiten 10.5 und 10.6):** Beschreibe in Schritt 5 die Postfix-Werte `mail_version`, `myorigin` und `inet_interfaces`. Erkläre die Aliasdatei und `postmap -q`. Erkläre, warum Druckdienste (CUPS) hier nicht ausgeführt wurden.
4. **Dienste und Fehlersuche (Einheiten 10.7 und 10.8):** Lies in Schritt 6 die Unit `uebung.service` und die Meldung von `systemd-analyze verify`. Erkläre, warum `systemctl status` im Container scheitert, und beschreibe das Vorgehen bei einem Dienst, der nicht startet (`status`, Journal, Konfigurationsprüfung).

#### Kontrollfragen

1. Welche Zeit zeigt `TZ=Europe/Vienna` für `2026-03-29 01:30 UTC`?
2. In welche Datei schreibt die Regel `local0.*`?
3. Was bewirkt `logrotate -f`?
4. Wie prüft man eine Konfiguration von rsyslog vor dem Start?

### Modul 11: Networking Fundamentals und Client DNS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Adressen, Routen und Weiterleitung in getrennten Netzwerk-Namensräumen einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende mit `ip`, `ss`, `traceroute` und `ping` Verbindungen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Standardroute setzen und den Weg mit `ip route get` ermitteln.
  * Nach Abschluss dieses Moduls kann der Lernende die Namensauflösung über `nsswitch.conf`, `hosts` und `resolv.conf` einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Netzwerkfehler eingrenzen.
* **Voraussetzungen:** Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | TCP/IP Grundlagen | 1,25 |
| 11.2 | IP Configuration | 1,25 |
| 11.3 | Persistent Network Configuration | 1,25 |
| 11.4 | Routing | 1,25 |
| 11.5 | Network Troubleshooting Tools | 1,25 |
| 11.6 | DNS Client Configuration | 1,25 |
| 11.7 | Hostname und Hosts | 1,25 |
| 11.8 | Network Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **TCP/IP und Adressen (Einheiten 11.1 und 11.2):** Führe `bash netzwerk.sh` aus. Lies in Schritt 1 die Adressen von Client (`192.168.10.2/24`), Router (zwei Schnittstellen) und Server und erkläre, wann zwei Rechner im selben Netz liegen.
2. **Persistente Konfiguration und Routing (Einheiten 11.3 und 11.4):** Erkläre in Schritt 2 und 3, warum der erste Ping scheitert (`Network is unreachable`), was die Standardroute und `ip_forward` ändern und wie `ip route get` die Route bestimmt. Beschreibe, wie solche Einstellungen auf einer VM dauerhaft werden (Netplan oder `/etc/network/interfaces`; nicht ausgeführt).
3. **Werkzeuge und DNS-Client (Einheiten 11.5 und 11.6):** Lies in Schritt 4 `ss -ltn`, den HTTP-Abruf mit Status 200, `traceroute` und `ip neigh`. Erkläre in Schritt 5, wie `getent hosts` den Namen über `hosts` auflöst und was die Zeile `hosts: files dns` aussagt.
4. **Hostname und Fehlersuche (Einheiten 11.7 und 11.8):** Beschreibe in Schritt 6 die Rolle von `/etc/hostname`. Erkläre die Meldung `communications error ... timed out` im DNS-Test und beschreibe ein Vorgehen der Fehlersuche von der Schicht 1 bis zur Namensauflösung.

#### Kontrollfragen

1. Warum scheitert der erste Ping?
2. Was zeigt `ttl=63` im Ping?
3. Was bedeutet `hosts: files dns`?
4. Welche Wirkung hat `net.ipv4.ip_forward=1`?

### Modul 12: Security und LPIC-1 Exam Readiness

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende sudo-Regeln mit `visudo -c` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende SSH-Schlüssel erzeugen und die Serverkonfiguration mit `sshd -t` und `sshd -T` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Daten mit GnuPG verschlüsseln und signieren und Signaturen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Archiv sichern, prüfen und wiederherstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien mit Sonderrechten und lauschende Dienste finden.
* **Voraussetzungen:** Modul 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Security Administration | 1,25 |
| 12.2 | sudo und su | 1,25 |
| 12.3 | Host Security | 1,25 |
| 12.4 | SSH Security | 1,25 |
| 12.5 | GPG und Encryption | 1,25 |
| 12.6 | Backups | 1,25 |
| 12.7 | Exam Review 101/102 | 1,25 |
| 12.8 | Exam Strategy | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Administration und sudo (Einheiten 12.1 und 12.2):** Führe `bash sicherheit.sh` aus. Erkläre in Schritt 1 die Regel `ana ALL=(root) DIENSTE` und `%admins ALL=(ALL) ALL` und die Syntaxfehler in `schlecht.sudoers`. Erkläre, warum man `sudoers` nur mit `visudo` bearbeitet.
2. **Host- und SSH-Sicherheit (Einheiten 12.3 und 12.4):** Lies in Schritt 2 und 3 die Schlüsselerzeugung mit `ssh-keygen` und die ausgegebenen Werte von `sshd -T` (`permitrootlogin no`, `passwordauthentication no`). Erkläre, was der falsche Parameter `PermitRootLogn` auslöst.
3. **GPG und Backups (Einheiten 12.5 und 12.6):** Erkläre in Schritt 4 die Abfolge Schlüssel, Verschlüsseln, Entschlüsseln, Signieren und Prüfen und warum eine geänderte Datei zu „BAD signature“ führt. Beschreibe in Schritt 5 Sicherung, Prüfsumme und Wiederherstellung mit `tar`, `sha256sum` und `diff -r`.
4. **Wiederholung und Strategie (Einheiten 12.7 und 12.8):** Lies in Schritt 6 die Dateien mit gesetztem SUID-Bit und die Zahl der lauschenden Sockets und nenne, welche Befehle in den Modulen 1 bis 12 du noch nicht sicher beherrschst. Erstelle daraus einen Lernplan; keine Prüfungsfragen sammeln.

#### Kontrollfragen

1. Warum `visudo` und nicht ein normaler Editor?
2. Was zeigt `sshd -T` im Unterschied zu `sshd -t`?
3. Was passiert mit der Signatur, wenn die Datei danach geändert wird?
4. Wozu dient die Prüfsumme der Sicherung?
