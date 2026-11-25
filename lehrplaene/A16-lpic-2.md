# Lehrplan: LPIC-2

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | LPIC-1 oder gleichwertige Linux-Kenntnisse (Kommandozeile, Benutzer, Dateisysteme, Netzwerk-Grundlagen) |
| **Gesamtumfang** | 12 Module, 110 UE (zu 45 Minuten; 82,5 Stunden) |
| **Fokus-Technologien** | Linux-Administration im Netzwerk (Prüfungsvorbereitung LPIC-2): Kernel, Speicher, Netzwerk, DNS, Web, Samba/NFS, DHCP, PAM, LDAP, Mail, Sicherheit; Debian/Ubuntu |
| **Thematische Abgrenzung (Out of Scope)** | LPIC-1 (Grundlagen) steht im selben Repository und wird vorausgesetzt. Spezialthemen wie Active-Directory-Domänen mit Samba, Virtualisierung, Container, Hochverfügbarkeit und Kryptografie-Infrastrukturen gehören zu LPIC-3. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2/3) | Stunden (UE) |
|---|---|---|---|
| 1 | LPIC-2 Grundlagen und Linux Engineer Operating Model | 1 | 8 |
| 2 | Capacity Planning and Performance Analysis | 1 | 9 |
| 3 | Linux Kernel and System Startup | 1 | 10 |
| 4 | Filesystems, Devices and Advanced Storage | 1 | 10 |
| 5 | Advanced Networking Configuration | 1 | 10 |
| 6 | System Maintenance, Source Builds and Backup | 1 | 8 |
| 7 | DNS Services with BIND | 1 | 9 |
| 8 | Web and Proxy Services | 1 | 9 |
| 9 | File Sharing with Samba and NFS | 1 | 9 |
| 10 | Network Client Management and Authentication | 1 | 10 |
| 11 | E-Mail Services and System Security | 1 | 10 |
| 12 | LPIC-2 Exam Readiness und Abschluss-Lab | 3 | 8 |
| **Gesamt** | 12 Module | 11 × Priorität 1, 0 × Priorität 2, 1 × Priorität 3 | **110** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11. **Priorität 3** (nur bei Zeit, entfällt zuerst) ist Modul 12 (Wiederholung und Abschluss-Labor); ohne Modul 12 verringert sich der Gesamtumfang von 110 auf 102 UE.

### 2. Quellen

**Gelesen (lpi.org, 25.11.2026, Seite „LPIC-2 Overview“):** LPIC-2 besteht aus den Prüfungen 201-450 und 202-450, aktuelle Version der Prüfungsziele 4.5. Die Seite nennt keine neue Version und kein Datum. Themenüberschriften Prüfung 201: Capacity Planning; Linux Kernel; System Startup; Filesystem and Devices; Advanced Storage Device Administration; Networking Configuration; System Maintenance. Themenüberschriften Prüfung 202: Domain Name Server; Web Services; File Sharing; Network Client Management; E-Mail Services; System Security.

**Zuordnung (meine Annahme, nur auf Ebene der Themenüberschriften):** Modul 2 zu Capacity Planning, Modul 3 zu Linux Kernel und System Startup, Modul 4 zu Filesystem and Devices und Advanced Storage Device Administration, Modul 5 zu Networking Configuration, Modul 6 zu System Maintenance, Modul 7 zu Domain Name Server, Modul 8 zu Web Services, Modul 9 zu File Sharing, Modul 10 zu Network Client Management, Modul 11 zu E-Mail Services und System Security.

**Nicht gelesen:** Die einzelnen Prüfungsziele (Nummern, Gewichtungen, Wissensgebiete) der Version 4.5 und alle weiteren Quellen. Aussagen zu Befehlen, Dateien und Pfaden sind Fachwissen, soweit sie nicht im Container ausgeführt wurden, und **nicht bestätigt**. Prüfungsfragen werden nicht wiedergegeben. **Getestet mit (Ubuntu 24.04.5, Cloud-Container, root, ohne systemd als init):** BIND 9.18.39, Apache 2.4.58, nginx 1.24.0, Squid 6.14, Samba 4.19.5, Postfix 3.8.6, Dovecot 2.3.21, ISC dhcpd 4.4.3-P1, OpenLDAP slapd 2.6.10, mdadm 4.3, OpenVPN, vsftpd 3.0.5, OpenSSH, nftables, iproute2.

### 3. Labor-Setup & Rahmenbedingungen

**Labor laut Lehrplan:** Eine Linux-Server-VM (Debian oder Ubuntu Server) und eine Linux-Client-VM auf einem privaten Hyper-V-Switch ohne Verbindung zum Heimnetz; Snapshots vor jeder Übung. Das Hyper-V-Labor wurde **nicht** aufgebaut.

**Skripte:** Alle Übungsskripte laufen unter Linux als root im Sandkasten `/tmp/lpic2` mit eigenen Konfigurationsdateien, Ports über 1024 (z. B. DNS 5301, Web 8081 bis 8084, Samba 4455, LDAP 3389, FTP 2121, SSH 2222) und eigenen Netzwerk-Namensräumen, räumen am Ende auf und legen nur kurzlebige Testkonten an. **Nie auf einem Produktivsystem ausführen.**

## B. Detaillierter Modulaufbau

### Modul 1: LPIC-2 Grundlagen und Linux Engineer Operating Model

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rolle und Prüfungsstruktur von LPIC-2 nennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Dienste des Kurses mit Versionen im Labor inventarisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Befehle mit eingebauter Hilfe prüfen, bevor sie ausgeführt werden.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungen mit einem festen Protokoll dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler nach Schema eingrenzen: Symptom, Eingrenzung, Prüfung, Ursache.
* **Voraussetzungen:** LPIC-1 oder gleichwertige Kenntnisse.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | LPIC-2 Rollenbild | 1 |
| 1.2 | Exam Struktur | 1 |
| 1.3 | Voraussetzungen | 1 |
| 1.4 | Lab Umgebung | 1 |
| 1.5 | Mixed Network Mindset | 1 |
| 1.6 | Command Line Discipline | 1 |
| 1.7 | Dokumentation und Betrieb | 1 |
| 1.8 | Grundlagen-Troubleshooting | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rolle und Prüfungsstruktur (Einheiten 1.1 und 1.2):** Beschreibe in vier Sätzen die Rolle eines Linux-Engineers und welche beiden Prüfungen zu LPIC-2 gehören. Ordne den Themenüberschriften der beiden Prüfungen jeweils ein Modul dieses Kurses zu.
2. **Voraussetzungen und Labor (Einheiten 1.3 und 1.4):** Führe `bash grundlagen.sh` aus und lies in Schritt 1 die Versionen von BIND, Apache, nginx, Squid, Samba, Postfix, Dovecot, dhcpd, slapd und mdadm. Notiere, welche Dienste in deinem Labor noch zu installieren wären.
3. **Netzwerk-Denkweise und Kommandozeile (Einheiten 1.5 und 1.6):** Lies in Schritt 2 den Umgang mit `type`, `help` und `--help`. Erkläre, warum man bei unbekannten Befehlen zuerst die Hilfe liest, und lege eine Regel fest, wie du Befehle mit Wirkung auf Produktivsysteme vorher prüfst.
4. **Dokumentation und Fehlersuche (Einheiten 1.7 und 1.8):** Erkläre in Schritt 3 die Felder des Änderungsprotokolls. Lies in Schritt 4 die Fehlermeldungen von `named-checkconf` für die kaputte und die gute Datei und beschreibe die Eingrenzung in vier Schritten.

#### Kontrollfragen

1. Welche beiden Prüfungen gehören laut lpi.org zu LPIC-2?
2. Wodurch zeigt `named-checkconf` einen Fehler an?
3. Warum steht im Änderungsprotokoll ein Feld „Rollback“?
4. Was sagt `type -a ls` im Container?

### Modul 2: Capacity Planning and Performance Analysis

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Auslastung von CPU, Speicher, Platte und Netz messen.
  * Nach Abschluss dieses Moduls kann der Lernende Messwerte von `vmstat`, `mpstat`, `free` und `iostat` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffsprotokolle nach Zeit auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende den künftigen Bedarf linear hochrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Leistungsprobleme nach Schema eingrenzen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Resource Usage Measurement | 1 |
| 2.2 | CPU Analysis | 1 |
| 2.3 | Memory Analysis | 1,25 |
| 2.4 | Disk and I/O Analysis | 1 |
| 2.5 | Network Performance | 1,25 |
| 2.6 | Log-based Capacity Planning | 1 |
| 2.7 | Predict Future Needs | 1 |
| 2.8 | Performance Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Messung und CPU (Einheiten 2.1 und 2.2):** Führe `bash kapazitaet.sh` aus. Lies in Schritt 1 die Last der letzten 1, 5 und 15 Minuten und die Spalten von `vmstat`. Erkläre in Schritt 2, warum `mpstat` bei zwei laufenden Endlosschleifen mehr als 50 Prozent Benutzeranteil zeigt.
2. **Speicher und Platte (Einheiten 2.3 und 2.4):** Erkläre in Schritt 3 die Spalten `used`, `buff/cache` und `available` in `free -m` und was `pswpin`/`pswpout` bedeuten. Lies in Schritt 4 den Durchsatz des Schreibtests und die Zähler aus `/proc/diskstats` und `iostat`.
3. **Netz und Protokolle (Einheiten 2.5 und 2.6):** Lies in Schritt 5 die RX- und TX-Zähler von `lo` und die Zusammenfassung von `ss -s`. Werte in Schritt 6 das Zugriffsprotokoll aus: Anfragen je Stunde und häufigste Quelle.
4. **Vorhersage und Leistungsfehler (Einheiten 2.7 und 2.8):** Erkläre in Schritt 7 die lineare Hochrechnung (Anstieg, Monat 12, Erreichen von 100 GB). Beschreibe in Schritt 8 ein Vorgehen, wenn ein System langsam ist (Last, Zustände der Prozesse, Verursacher).

#### Kontrollfragen

1. Woran erkennt man, dass der Arbeitsspeicher knapp wird?
2. Was zeigt die Spalte `wa` in `vmstat`?
3. Welche Stunde hat im Beispielprotokoll die meisten Anfragen?
4. Wann sind 100 GB in der Hochrechnung erreicht?

### Modul 3: Linux Kernel and System Startup

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Komponenten und Version des Kernels benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Modulkonfiguration (`modprobe.d`) prüfen, ohne Module zu laden.
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzungen für das Übersetzen eines Kernels einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Laufzeitparameter mit `sysctl` lesen und im Namensraum ändern.
  * Nach Abschluss dieses Moduls kann der Lernende Bootvorgang, initramfs, Bootloader und Rettungsmodus erklären.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Kernel Components | 1,25 |
| 3.2 | Module Management | 1,25 |
| 3.3 | Kernel Compilation | 1,25 |
| 3.4 | Runtime Kernel Tuning | 1,25 |
| 3.5 | System Startup | 1,25 |
| 3.6 | Bootloader | 1,25 |
| 3.7 | System Recovery | 1,25 |
| 3.8 | Kernel/Boot Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kernel und Module (Einheiten 3.1 und 3.2):** Führe `bash kernel.sh` aus. Lies in Schritt 1 die Kernel-Version und erkläre, warum `/boot` im Container leer ist und `/lib/modules` fehlt. Erkläre in Schritt 2 die Direktiven `blacklist`, `options`, `alias` und `install` in `modprobe-test.conf` und warum `lsmod` hier scheitert.
2. **Kompilieren und Laufzeitparameter (Einheiten 3.3 und 3.4):** Lies in Schritt 3 die Versionen von `gcc` und `make` und die Kerneloptionen aus `/proc/config.gz`. Beschreibe die Schritte zum Kompilieren eines Kernels (nicht ausgeführt). Erkläre in Schritt 4, warum die Änderung von `net.ipv4.ip_forward` im Namensraum den Wert des Hosts nicht ändert.
3. **Systemstart und Bootloader (Einheiten 3.5 und 3.6):** Erkläre in Schritt 5 den Inhalt des selbst gebauten initramfs und die Zeilen `linux` und `initrd` des GRUB-Eintrags. Nenne, welche Werkzeuge des Bootloaders im Container fehlen.
4. **Wiederherstellung und Fehlersuche (Einheiten 3.7 und 3.8):** Lies in Schritt 6 und 7 die Targets `rescue` und `emergency`. Beschreibe ein Vorgehen bei einem System, das nach einem Kernel-Update nicht mehr startet (älteren Kernel wählen, Rettungsmodus, initramfs neu erzeugen).

#### Kontrollfragen

1. Warum scheitert `modprobe -n -v loop` im Container?
2. Was ändert `sysctl -w` im Unterschied zu einer Datei unter `/etc/sysctl.d/`?
3. Was enthält ein initramfs?
4. Worin unterscheidet sich `rescue.target` von `emergency.target`?

### Modul 4: Filesystems, Devices and Advanced Storage

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ext4 und XFS anlegen, einhängen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateisysteme vergrößern.
  * Nach Abschluss dieses Moduls kann der Lernende Gerätekennungen und udev-Regeln prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende RAID und LVM einordnen und die Grenzen im Container benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Speicherwerkzeuge für iSCSI und Multipath erkennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Linux Filesystem Operations | 1,25 |
| 4.2 | Filesystem Maintenance | 1,25 |
| 4.3 | Filesystem Options | 1,25 |
| 4.4 | Device Management | 1,25 |
| 4.5 | RAID | 1,25 |
| 4.6 | LVM | 1,25 |
| 4.7 | Advanced Storage Access | 1,25 |
| 4.8 | Storage Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Anlegen und Einhängen (Einheiten 4.1 und 4.2):** Führe `bash dateisysteme.sh` aus. Erkläre in Schritt 1, warum XFS mindestens 300 MB braucht und ext4 nicht. Lies in Schritt 2 die Mount-Optionen (`noatime`, `nodev`, `inode64`) und die Größen der beiden Dateisysteme.
2. **Wartung und Optionen (Einheiten 4.3 und 4.4):** Erkläre in Schritt 3 die Befehle `e2fsck -fn`, `tune2fs -l`, `tune2fs -m 1` und `xfs_repair -n` und warum sie ausgehängt arbeiten. Beschreibe die Schritte zum Vergrößern des ext4 von 64 MB auf 128 MB.
3. **Geräte, RAID und LVM (Einheiten 4.5 und 4.6):** Lies in Schritt 4 die Prüfung der udev-Regeln. Erkläre in Schritt 5 und 6, was im Container mit mdadm und LVM geht und was nicht, und schreibe die Befehle für ein RAID 1 und eine logische Partition für die VM auf.
4. **Speicherzugriff und Fehlersuche (Einheiten 4.7 und 4.8):** Lies in Schritt 7 die Liste der Werkzeuge für iSCSI und Multipath. Beschreibe in Schritt 8 das Vorgehen bei einem beschädigten Dateisystem (Bad magic number, Backup-Superblöcke).

#### Kontrollfragen

1. Wie groß ist das ext4-Dateisystem nach dem Vergrößern?
2. Was meldet `lvcreate` im Container?
3. Wodurch unterscheidet sich `xfs_repair -n` von `xfs_repair`?
4. Was bedeutet `Fail: 0` bei `udevadm verify`?

### Modul 5: Advanced Networking Configuration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Adressen und Routen in Namensräumen einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende IPv6-Adressen schreiben und Netze unterteilen.
  * Nach Abschluss dieses Moduls kann der Lernende statische Routen und Policy-Routing setzen.
  * Nach Abschluss dieses Moduls kann der Lernende Bridges einrichten; Bonding und VLAN in der VM einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Pakete mit nftables filtern und mit `tcpdump` mitschneiden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Basic Networking Configuration | 1,25 |
| 5.2 | IPv4 and IPv6 | 1,25 |
| 5.3 | Advanced Routing | 1,25 |
| 5.4 | Bonding | 1,25 |
| 5.5 | Bridges and VLANs | 1,25 |
| 5.6 | Network Troubleshooting Tools | 1,25 |
| 5.7 | Firewall Interaction | 1,25 |
| 5.8 | Networking Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Grundkonfiguration und IPv6 (Einheiten 5.1 und 5.2):** Führe `bash netzwerk.sh` aus. Erkläre in Schritt 1, warum der Ping zwischen zwei Netzen über den Router `ttl=63` zeigt. Schreibe in Schritt 2 die Adresse `2001:db8:0:0:0:0:0:1` in Kurzform und berechne, wie viele /64-Netze in einem /48 liegen.
2. **Routing (Einheiten 5.3 und 5.4):** Lies in Schritt 3 die statische Route, die Regel mit Tabelle 100 und die Ausgabe von `ip route get`. Erkläre, wann Policy-Routing nötig ist.
3. **Bonding, Bridges und VLAN (Einheiten 5.5 und 5.6):** Lies in Schritt 4, was im Container gelingt (Bridge) und was nicht (Bonding, VLAN). Schreibe für die VM Netplan-Beispiele für ein Bond im Modus active-backup und ein VLAN 10.
4. **Firewall und Fehlersuche (Einheiten 5.7 und 5.8):** Erkläre in Schritt 5 die Tabelle `inet filter` mit der Regel für Port 8080 und lies in Schritt 6, warum Port 8081 antwortet und 8080 nicht. Beschreibe in Schritt 7 die Eingrenzung bei entfernter Route.

#### Kontrollfragen

1. Was zeigt `ttl=63`?
2. Wie lautet die Kurzform von `2001:0db8:0000:0000:0000:0000:0000:0001`?
3. Was bewirkt `ip rule add from 10.50.9.1 table 100`?
4. Welche Regel verhindert den Zugriff auf Port 8080?

### Modul 6: System Maintenance, Source Builds and Backup

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Software aus dem Quellcode übersetzen und in ein eigenes Präfix installieren.
  * Nach Abschluss dieses Moduls kann der Lernende gemeinsame Bibliotheken bauen und mit `ldconfig` auffindbar machen.
  * Nach Abschluss dieses Moduls kann der Lernende vollständige, inkrementelle und hardlink-basierte Sicherungen erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Benachrichtigung und zeitgesteuerte Wartung einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Übersetzungs- und Bibliotheksfehler lesen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Build from Source | 1 |
| 6.2 | Package and Source Integration | 1 |
| 6.3 | Shared Libraries | 1 |
| 6.4 | Backup Concepts | 1 |
| 6.5 | Backup Tools | 1 |
| 6.6 | System Notifications | 1 |
| 6.7 | Maintenance Automation | 1 |
| 6.8 | Maintenance Troubleshooting | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Quellcode und Paketintegration (Einheiten 6.1 und 6.2):** Führe `bash wartung.sh` aus. Erkläre in Schritt 1 den Ablauf von `tar`, `make`, `make install` mit `DESTDIR` und `PREFIX`. Lies in Schritt 2, warum `apt-get build-dep` ohne `deb-src` scheitert und was `dpkg -S` über `make` meldet.
2. **Bibliotheken und Sicherungskonzepte (Einheiten 6.3 und 6.4):** Erkläre in Schritt 3 die Fehlermeldung beim Start von `lib/main`, die Wirkung von `LD_LIBRARY_PATH` und von `ldconfig -C ... -f ...`. Beschreibe in Schritt 4 den Unterschied zwischen Voll-, inkrementeller und Hardlink-Sicherung.
3. **Werkzeuge und Benachrichtigung (Einheiten 6.5 und 6.6):** Lies in Schritt 5 die Ausgabe von `cpio`, `dd` und `sha256sum`. Erkläre in Schritt 6, wie `logger` eine Meldung ins Systemprotokoll schreibt, und prüfe die Cron-Zeile mit `MAILTO`.
4. **Automatisierung und Fehlersuche (Einheiten 6.7 und 6.8):** Erkläre in Schritt 7 die Unit-Dateien `sicherung.service` und `sicherung.timer` und `OnCalendar`. Lies in Schritt 8 die Fehlermeldungen von `gcc` (fehlende Header-Datei, fehlendes `main`) und beschreibe die Prüfung mit `ldd`.

#### Kontrollfragen

1. Wozu dient `DESTDIR` bei `make install`?
2. Warum findet `lib/main` die Bibliothek zuerst nicht?
3. Was enthält die inkrementelle Sicherung?
4. Was bewirkt `rsync --link-dest`?

### Modul 7: DNS Services with BIND

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zonen- und Konfigurationsdateien von BIND schreiben und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Primär- und einen Zweitserver mit Zonenübertragung betreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Cache-Server mit Weiterleitung konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Schlüssel erzeugen und eine Zone mit DNSSEC signieren.
  * Nach Abschluss dieses Moduls kann der Lernende DNS mit `dig` und `host` testen und typische Fehler lesen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | DNS Grundlagen | 1 |
| 7.2 | BIND Installation and Layout | 1 |
| 7.3 | Zone Files | 1,25 |
| 7.4 | Zone Transfers | 1 |
| 7.5 | Caching and Forwarding | 1,25 |
| 7.6 | DNS Security | 1 |
| 7.7 | DNS Testing | 1 |
| 7.8 | DNS Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Grundlagen und Aufbau (Einheiten 7.1 und 7.2):** Führe `bash dns.sh` aus. Erkläre in Schritt 1 und 2 die Aufgabe von DNS und die Dateien von BIND (`named.conf`, `named.conf.options`, `named.conf.local`, Zonendateien) und lies die Programme `named`, `rndc`, `named-checkconf`, `named-checkzone`.
2. **Zonendatei und Übertragung (Einheiten 7.3 und 7.4):** Lies in Schritt 3 die Zonendatei: SOA, NS, MX, A, CNAME und die Rückwärtszone (PTR). Erkläre in Schritt 5 die Übertragung zum Zweitserver (Seriennummer, `AXFR`, `also-notify`).
3. **Zwischenspeicher und Weiterleitung (Einheiten 7.5 und 7.6):** Erkläre in Schritt 6, wie der Cache-Server auf Port 5303 Anfragen an den Primärserver weiterleitet (`forwarders`, `forward only`) und woran man in der zweiten Antwort den Cache erkennt (TTL).
4. **DNSSEC, Test und Fehlersuche (Einheiten 7.7 und 7.8):** Lies in Schritt 8 die Erzeugung von KSK und ZSK und die Signierung (RRSIG, DNSKEY, DS). Werte in Schritt 4 und 9 die Antworten aus (`aa`, `NXDOMAIN`, `REFUSED`) und beschreibe die Fehlersuche mit `named-checkzone` und `dig`.

#### Kontrollfragen

1. Was bedeutet das Flag `aa` in der Antwort?
2. Wann übernimmt der Zweitserver Änderungen?
3. Was meldet `named-checkzone` bei `192.0.2.300`?
4. Warum antwortet der Primärserver für `www.fremd.example` mit `REFUSED`?

### Modul 8: Web and Proxy Services

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Apache mit mehreren Virtual Hosts und Basic-Authentifizierung konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende HTTPS mit selbst erzeugtem Zertifikat einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Squid als Proxy mit Zugriffsregeln betreiben.
  * Nach Abschluss dieses Moduls kann der Lernende nginx als Webserver und Reverse Proxy konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationsfehler und belegte Ports erkennen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Apache Basics | 1 |
| 8.2 | Virtual Hosts | 1 |
| 8.3 | Apache HTTPS | 1,25 |
| 8.4 | Access Control and Auth | 1 |
| 8.5 | Squid Proxy | 1,25 |
| 8.6 | Nginx Web Server | 1 |
| 8.7 | Nginx Reverse Proxy | 1 |
| 8.8 | Web Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Apache und Virtual Hosts (Einheiten 8.1 und 8.2):** Führe `bash web.sh` aus. Erkläre in Schritt 1 die zwei Virtual Hosts (`ServerName`, `DocumentRoot`) und wie der Header `Host` den Host auswählt. Lies die Prüfung mit `apache2ctl -t` und `-S`.
2. **HTTPS und Zugriffskontrolle (Einheiten 8.3 und 8.4):** Lies in Schritt 1 die Antworten 401, 200, 401 für `/intern/` und erkläre `AuthType Basic` und `Require valid-user`. Erkläre in Schritt 2 die Direktiven `SSLEngine`, `SSLCertificateFile`, `SSLProtocol` und warum `curl` ohne `-k` den Rückgabewert 60 liefert.
3. **Squid und nginx (Einheiten 8.5 und 8.6):** Erkläre in Schritt 3 die Regeln `acl`, `http_access deny` und `allow localhost` und die Protokollzeilen `TCP_DENIED/403` und `TCP_MISS/200`. Lies in Schritt 4 `nginx -t`, die Antworten auf `/` und `/proxy/` und den Header `Server`.
4. **Reverse Proxy und Fehlersuche (Einheiten 8.7 und 8.8):** Erkläre `proxy_pass` und `upstream`. Lies in Schritt 5 die Fehlermeldungen von Apache („No MPM loaded“), nginx (`unexpected "}"`) und die Meldung bei belegtem Port („Address already in use“) und beschreibe die Fehlersuche (Konfigurationstest, Protokoll, `ss`).

#### Kontrollfragen

1. Welchen Statuscode liefert `/intern/` ohne Anmeldung, mit richtigem und mit falschem Kennwort?
2. Was meldet Squid für `test.gesperrt.example`?
3. Was bedeutet `curl`-Rückgabewert 60?
4. Wie unterscheidet nginx als Reverse Proxy die Pfade `/` und `/proxy/`?

### Modul 9: File Sharing with Samba and NFS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Samba-Konfiguration schreiben und mit `testparm` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Samba-Benutzer anlegen und eine Freigabe mit `smbclient` nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Zugriffsfehler (`NT_STATUS_...`) deuten.
  * Nach Abschluss dieses Moduls kann der Lernende NFS-Exporte verwalten und die Sicherheitsoptionen einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateifreigaben absichern und Fehler eingrenzen.
* **Voraussetzungen:** Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Samba Overview | 1 |
| 9.2 | smb.conf | 1 |
| 9.3 | Samba Users and Permissions | 1,25 |
| 9.4 | Samba Client Tools | 1 |
| 9.5 | NFS Overview | 1,25 |
| 9.6 | NFS Server Configuration | 1 |
| 9.7 | File Sharing Security | 1 |
| 9.8 | File Sharing Troubleshooting | 1,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Samba-Überblick und smb.conf (Einheiten 9.1 und 9.2):** Führe `bash freigaben.sh` aus. Erkläre in Schritt 1 und 2 die Abschnitte `[global]`, `[daten]` und `[nur-lesen]` und lies die Prüfung mit `testparm`, auch bei der Datei mit falschen Parametern.
2. **Benutzer, Rechte und Client (Einheiten 9.3 und 9.4):** Erkläre in Schritt 3, warum für Samba ein Linux-Konto und ein getrenntes Samba-Kennwort (`smbpasswd`, `pdbedit`) nötig sind. Lies in Schritt 4, was `smbclient -L`, `ls`, `put` und `mkdir` liefern.
3. **NFS und Sicherheit (Einheiten 9.5 und 9.6):** Erkläre in Schritt 7 die Exportzeile mit `rw`, `sync`, `no_subtree_check`, `root_squash` und `all_squash` und warum der NFS-Server hier nur über `exportfs` verwaltet wurde. Lies die Fehler in Schritt 5 und ordne sie zu.
4. **Wartung und Fehlersuche (Einheiten 9.7 und 9.8):** Lies in Schritt 6 `smbstatus` und die Sperrdateien. Beschreibe in Schritt 5 und 8 die Fehlersuche bei `NT_STATUS_LOGON_FAILURE`, `NT_STATUS_BAD_NETWORK_NAME`, `NT_STATUS_ACCESS_DENIED` und `NT_STATUS_ACCOUNT_DISABLED`.

#### Kontrollfragen

1. Was meldet Samba bei falschem Kennwort?
2. Was bedeutet `NT_STATUS_BAD_NETWORK_NAME`?
3. Wodurch wird `put` in `[nur-lesen]` abgewiesen?
4. Was bewirkt `root_squash` in `/etc/exports`?

### Modul 10: Network Client Management and Authentication

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen DHCP-Server konfigurieren, prüfen und eine Adressvergabe beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende PAM-Dienstdateien mit Steuerwerten schreiben und mit `pamtester` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen OpenLDAP-Server mit eigener Konfiguration betreiben und mit den LDAP-Werkzeugen abfragen und ändern.
  * Nach Abschluss dieses Moduls kann der Lernende die Integration von LDAP in NSS und PAM einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende typische DHCP-, PAM- und LDAP-Fehler lesen.
* **Voraussetzungen:** Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | DHCP Server | 1,25 |
| 10.2 | DHCP Troubleshooting | 1,25 |
| 10.3 | PAM Concepts | 1,25 |
| 10.4 | PAM Configuration | 1,25 |
| 10.5 | LDAP Client Usage | 1,25 |
| 10.6 | OpenLDAP Server | 1,25 |
| 10.7 | Authentication Integration | 1,25 |
| 10.8 | Auth Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **DHCP-Server und Fehlersuche (Einheiten 10.1 und 10.2):** Führe `bash anmeldung.sh` aus. Erkläre in Schritt 1 den Aufbau von `dhcpd.conf` (`subnet`, `range`, `option routers`, feste Adresse) und lies die Fehlermeldung für `falsch.conf`. Beschreibe in Schritt 2 den Ablauf DISCOVER, OFFER, REQUEST, ACK und lies die vergebene Adresse und Route.
2. **PAM-Konzepte und -Konfiguration (Einheiten 10.3 und 10.4):** Erkläre in Schritt 3 die Steuerwerte `required` und `requisite` an den Diensten `lpic2-a` und `lpic2-b` und das Ergebnis für `pamana` und `pamben`. Lies in Schritt 4 die Fehlermeldung bei unbekanntem Modul und den Aufbau von `common-auth`.
3. **LDAP-Client und Server (Einheiten 10.5 und 10.6):** Erkläre in Schritt 5 die Konfiguration (`database mdb`, `suffix`, `rootdn`, `access`). Lies in Schritt 6 Suche mit Filter, Ändern mit `ldapmodify` und die Prüfung mit `ldapwhoami`; erkläre, warum `userPassword` anonym nicht sichtbar ist.
4. **Anmeldeintegration und Fehlersuche (Einheiten 10.7 und 10.8):** Erkläre in Schritt 7, was für eine Anmeldung über LDAP nötig wäre (NSS-Zeile, `pam_ldap` oder SSSD) und warum das hier nicht ausgeführt wurde. Ordne in Schritt 8 die Fehlercodes 32, 49 und 68 sowie „Can't contact LDAP server (-1)“ zu.

#### Kontrollfragen

1. Welche Meldungen kommen bei der DHCP-Vergabe in welcher Reihenfolge?
2. Warum scheitert `pamben` beim Dienst `lpic2-b`?
3. Was bedeutet LDAP-Fehler 49?
4. Was bedeutet LDAP-Fehler 32?

### Modul 11: E-Mail Services and System Security

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Postfix-Konfiguration, Aliase, virtuelle Adressen und Transportwege prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Dovecot-Konfiguration für IMAP/POP3 prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Linux als Router mit NAT einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende FTP, SSH (nur Schlüssel) und OpenVPN betreiben und testen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherheitsfehler in Konfigurationen erkennen.
* **Voraussetzungen:** Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Mail Server Concepts | 1,25 |
| 11.2 | Postfix Basics | 1,25 |
| 11.3 | Mail Delivery | 1,25 |
| 11.4 | Mailbox Access | 1,25 |
| 11.5 | Router Configuration | 1,25 |
| 11.6 | FTP Services | 1,25 |
| 11.7 | SSH and OpenVPN | 1,25 |
| 11.8 | Security Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Mail-Konzepte und Postfix (Einheiten 11.1 und 11.2):** Führe `bash mail-sicherheit.sh` aus. Erkläre die Rollen MTA, MDA und MUA und lies in Schritt 2 die Werte der eigenen `main.cf` (`myhostname`, `mydestination`, `inet_interfaces`, `virtual_alias_maps`, `transport_maps`).
2. **Zustellung und Postfachzugriff (Einheiten 11.3 und 11.4):** Lies in Schritt 3 die Abfragen mit `postmap -q` (Alias, virtuelle Adressen mit zwei Empfängern, Transportweg) und erkläre den Rückgabewert 1 für unbekannte Adressen. Erkläre in Schritt 4 die Dovecot-Einstellungen `protocols`, `mail_location`, `ssl`, `disable_plaintext_auth`.
3. **Router mit NAT und FTP (Einheiten 11.5 und 11.6):** Erkläre in Schritt 5, warum die Anfrage ohne NAT scheitert (keine Rückroute am Server) und warum der Server mit Masquerade die Router-Adresse sieht. Lies in Schritt 6 den FTP-Test (Anmeldung, Upload, falsches Kennwort, anonym) und erkläre die Direktiven von `vsftpd.conf`.
4. **SSH, OpenVPN und Fehlersuche (Einheiten 11.7 und 11.8):** Erkläre in Schritt 7 die Konfiguration von `sshd` (`AllowUsers`, `PasswordAuthentication no`, `PermitRootLogin no`) und die Ergebnisse (Schlüssel erfolgreich, Kennwort und root abgewiesen) sowie den OpenVPN-Tunnel mit statischem Schlüssel. Ordne in Schritt 8 die Meldungen „Bad configuration option“ und „No such file“ zu.

#### Kontrollfragen

1. Was liefert `postmap -q verkauf@lab.example`?
2. Welche Quelladresse sieht der Server nach `masquerade`?
3. Wie wird der Zugriff auf SSH mit Kennwort verhindert?
4. Was zeigt `grep -c 'Initialization Sequence Completed'` im OpenVPN-Protokoll?

### Modul 12: LPIC-2 Exam Readiness und Abschluss-Lab

* **Priorität:** 3 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Werkzeuge der Module 2 bis 11 wiederholen und deren Vorhandensein prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende für jeden Dienst den Befehl zum Prüfen der Konfiguration nennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein kleines Gesamtlabor aus Namensauflösung, Router und Webserver betreiben.
  * Nach Abschluss dieses Moduls kann der Lernende drei Fehler nach Schema eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen eigenen Lernplan mit Werkzeug, Konfigurationsdatei und Fehlerbild je Modul anlegen.
* **Voraussetzungen:** Module 1 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Exam 201 Review | 1 |
| 12.2 | Exam 202 Review | 1 |
| 12.3 | Command Drill | 1 |
| 12.4 | Config File Drill | 1 |
| 12.5 | Mixed Network Lab | 1 |
| 12.6 | Troubleshooting Scenario Lab | 1 |
| 12.7 | Exam Strategy | 1 |
| 12.8 | Career Roadmap | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rückblick auf die Prüfungen (Einheiten 12.1 und 12.2):** Führe `bash abschluss.sh` aus. Lies in Schritt 1 die Übersicht der Werkzeuge je Modul und ordne jedes Modul den Themenüberschriften der Prüfungen 201 und 202 zu. Markiere die Themen, in denen du unsicher bist. Es werden keine Prüfungsfragen gesammelt.
2. **Befehle und Konfigurationsdateien (Einheiten 12.3 und 12.4):** Lies in Schritt 2 die Prüfbefehle `named-checkconf`, `nginx -t`, `testparm`, `dhcpd -t`, `sshd -t`, `visudo -cf` und ergänze für Apache, Postfix, Dovecot und slapd je einen Prüfbefehl aus den Modulen 8 bis 11.
3. **Gesamtlabor und Fehlerszenario (Einheiten 12.5 und 12.6):** Erkläre in Schritt 3 den Weg einer Anfrage: Namensauflösung (`dig`), Router, Webserver (`curl`) und `traceroute`. Löse in Schritt 4 die drei Fehler (ungültige Adresse in der Zone, fehlende Rückroute, falscher Port) mit den Prüfwerkzeugen.
4. **Strategie und Laufbahn (Einheiten 12.7 und 12.8):** Lege in Schritt 5 deinen Lernplan als Tabelle an (Modul, Prüfwerkzeug, Konfigurationsdatei, Fehlerbild), plane Wiederholungen in Abständen und notiere, welche Themen du im Labor praktisch geübt hast. Überlege die nächsten Schritte (LPIC-3).

#### Kontrollfragen

1. Wie prüft man die Syntax einer nginx-Konfiguration vor dem Neuladen?
2. Welches Werkzeug zeigt den Weg über den Router in Schritt 3?
3. Welches Symptom hat eine fehlende Rückroute am Server?
4. Warum sind im Skript keine Prüfungsfragen enthalten?
