# Lehrplan: Linux-Server-Härtung

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Shell, Dateien und Rechte, Pakete installieren, Dienste starten) |
| **Gesamtumfang** | 13 Module, 112 UE (zu 45 Minuten; 84 Stunden) |
| **Fokus-Technologien** | Debian/Ubuntu Linux (Debian 12, Ubuntu Server 24.04 LTS) |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Firewall-Technik (nftables, iptables) steht im Kurs „Linux-Firewall mit nftables und iptables“, Kryptografie und TLS im Kurs „Kryptografie, Zertifikate und TLS“, Grundbegriffe der IT-Sicherheit im Kurs „IT-Sicherheitsgrundlagen“. Nicht behandelt: Härtung von Containern und Kubernetes, Kernel-Kompilierung, Verschlüsselung der Datenträger, zentrale Benutzerverwaltung (LDAP, FreeIPA) und zentrale Protokollsammlung (SIEM) über das Konzept hinaus |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Härtungskonzept, Baselines und Labor | 1 | 8 |
| 2 | Benutzer, Gruppen und Konten | 1 | 9 |
| 3 | PAM: Passwortqualität und Kontosperre | 1 | 9 |
| 4 | sudo: Rechte vergeben und protokollieren | 1 | 8 |
| 5 | SSH-Härtung | 1 | 10 |
| 6 | Dienste, Pakete und Kernel-Parameter | 1 | 9 |
| 7 | Dateirechte, ACLs und Mount-Optionen | 1 | 9 |
| 8 | Mandatory Access Control: AppArmor und SELinux | 1 | 8 |
| 9 | Host-Firewall für den Server | 1 | 7 |
| 10 | Protokollierung und auditd | 1 | 10 |
| 11 | Updates und automatische Sicherheitsupdates | 1 | 8 |
| 12 | Integritätsprüfung (AIDE) und Schutz vor Dauerangriffen (fail2ban) | 2 | 7 |
| 13 | Härtung prüfen, Fehlersuche und Abschlussprojekt | 1 | 10 |
| **Gesamt** | 13 Module | 12 × Priorität 1, 1 × Priorität 2 | **112** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 12 (Integritätsprüfung mit AIDE und Schutz vor Dauerangriffen mit fail2ban). Fällt Modul 12 weg, verringert sich der Gesamtumfang auf 105 UE; kein Pflichtmodul setzt Modul 12 voraus.

### 2. Quellen

**Keine Quelle wurde gegen das Original gelesen.** Die Befehle und Ausgaben stammen aus Läufen im Labor-Container (Ubuntu 24.04, OpenSSH 9.6p1, sudo 1.9.15p5, Lynis 3.0.9, auditd 3.1.2, AIDE 0.18.6, fail2ban 1.0.2, unattended-upgrades 2.9.1, ssh-audit 3.9.0, AppArmor-Parser 4.0.1). Die Handbuchseiten der Programme (`sshd_config(5)`, `sudoers(5)`, `pam.conf(5)`, `auditctl(8)` und andere) sowie die **CIS Benchmarks** (Center for Internet Security) und die Herstellerleitfäden von Debian und Ubuntu sind **nicht** gelesen; Adressen und Versionsstände sind nicht geprüft. Wo eine Aussage über das Beobachtete hinausgeht, ist sie in der Übung mit „nicht bestätigt“ gekennzeichnet.

Die Benchmarks des CIS sind frei verfügbar nach Registrierung; ihre Nummerierung und ihre Maßnahmen werden hier **nicht** übernommen (Urheberrecht). Die Kursmaßnahmen sind eigene Formulierungen.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Haertung`, `10.14.0.0/24`).

**VMs:** `vm01` (**erforderlich**, ab Modul 1): frisch installierter Linux-Server, Debian 12 oder Ubuntu Server 24.04 LTS, 2 vCPU, 2 GB RAM, 20 GB Platte, `10.14.0.1`, Konto mit `sudo`-Recht, OpenSSH-Server installiert. `cl01` (**erforderlich**, ab Modul 5): zweiter Linux-Rechner oder Windows-Rechner mit SSH-Client, `10.14.0.2`; dient als Verwaltungsrechner und als Angreifer-Ersatz (Module 5, 9).

**Internetphase:** Vor Modul 1 erhält `vm01` vorübergehend eine zweite Netzwerkkarte an einem externen Switch (NAT); es werden installiert: `lynis`, `auditd`, `acl`, `libpam-pwquality`, `apparmor-utils` (unter Ubuntu bereits vorhanden), `nftables`, `unattended-upgrades`, `aide`, `fail2ban`, `openssh-server`, `python3-pip` (für `ssh-audit`). Danach wird die Karte entfernt. Für Modul 11 wird die Internetphase einmal wiederholt (Paketquellen), anschließend wieder entfernt.

**Prüfpunkt (Checkpoint):** Vor jedem Modul mit Änderungen an SSH, PAM, sudo oder der Firewall einen Hyper-V-Prüfpunkt von `vm01` anlegen und eine zweite SSH-Sitzung geöffnet lassen, damit ein Fehler nicht aussperrt. Die Prüfpunkte am Kursende löschen.

**SELinux:** Debian und Ubuntu verwenden standardmäßig AppArmor; SELinux ist ein Zusatzpaket und wird in Modul 8 nur in den Grundbegriffen behandelt (keine Aufgabe setzt eine laufende SELinux-Installation voraus).

**Skripte:** Die Beispielskripte liefen in einem Container mit Netzwerk-Namespaces (`lab.sh`) und ändern dort Dateien unter `/etc`; sie räumen auf. Auf `vm01` stattdessen die Befehle der Aufgaben einzeln eingeben, nicht die Skripte ungeprüft ausführen.

## B. Detaillierter Modulaufbau

### Modul 1: Härtungskonzept, Baselines und Labor

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Begriffe Angriffsfläche, Least Privilege und Defense in Depth an Beispielen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck einer Baseline (CIS Benchmark) beschreiben und zwei Profilstufen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende den Ausgangszustand eines Servers mit Lynis messen und die Kennzahlen festhalten.
  * Nach Abschluss dieses Moduls kann der Lernende ein Härtungsprotokoll mit Soll, Ist und begründeter Ausnahme führen.
* **Voraussetzungen:** Linux-Grundlagen; IP-Adressen und Subnetze.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Ziele und Grenzen der Härtung: Angriffsfläche, Least Privilege, Defense in Depth, Standardwerte der Distribution | 2 |
| 1.2 | Sicherheitsbaselines: CIS Benchmarks (Profilstufen), Herstellerleitfäden, Lynis als Messwerkzeug | 2 |
| 1.3 | Praxis: Labor aufbauen und Ausgangszustand messen (`baseline_messung.sh`) | 2 |
| 1.4 | Härtungsprotokoll: Soll-Ist-Tabelle, Abweichungen und Ausnahmen begründen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prinzipien zuordnen (Einheit 1.1):** Ordnen Sie fünf Maßnahmen (z. B. nicht benötigten Dienst abschalten, SSH nur mit Schlüssel, getrennte Konten für Verwaltung, Protokollierung, automatische Updates) den Prinzipien Angriffsfläche verkleinern, Least Privilege und Defense in Depth zu und begründen Sie jede Zuordnung in einem Satz.
2. **Baseline wählen (Einheit 1.2):** Legen Sie fest, welche Baseline (CIS Level 1 oder Level 2, Herstellerleitfaden) für den Kursserver gelten soll, und begründen Sie die Wahl mit dem Einsatzzweck (Webserver, Dateiserver, Bastion-Host).
3. **Ausgangszustand messen (Einheit 1.3):** Bauen Sie `vm01` nach der Laborbeschreibung auf. Führen Sie `lynis audit system --quick` aus (oder `bash baseline_messung.sh`) und halten Sie Härtungsindex, Zahl der Warnungen und Zahl der Vorschläge fest. Notieren Sie drei Vorschläge, die Sie nicht verstehen.
4. **Härtungsprotokoll anlegen (Einheit 1.4):** Legen Sie eine Tabelle mit den Spalten Maßnahme, Soll, Ist (Ausgangszustand), Datum, Ausnahme und Begründung an und tragen Sie die Messwerte aus Aufgabe 3 ein. Planen Sie, welche Maßnahme in welchem Modul folgt.

#### Kontrollfragen

1. Warum ist ein hoher Lynis-Härtungsindex kein Beweis für einen sicheren Server?
2. Was ist der Unterschied zwischen dem Verkleinern der Angriffsfläche und Defense in Depth?
3. Warum wird eine Baseline nicht blind angewendet, sondern gegen den Einsatzzweck abgewogen?
4. Welche Angaben gehören in die Begründung einer Ausnahme?

### Modul 2: Benutzer, Gruppen und Konten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau von `/etc/passwd` und `/etc/shadow` erklären und die Rechte der Dateien begründen.
  * Nach Abschluss dieses Moduls kann der Lernende Konten anlegen, sperren, mit Ablaufdatum versehen und mit Skripten auf UID 0 und leere Passwörter prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Dienstkonten ohne Anmelde-Shell einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende ein Kontenkonzept (persönlich, Dienst, Gruppe) entwerfen.
* **Voraussetzungen:** Modul 1; Linux-Kenntnisse zu Benutzern und Gruppen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Kontodateien `/etc/passwd`, `/etc/shadow`, `/etc/group`: Aufbau, Rechte, Passwort-Hashes (SHA-512, yescrypt) | 2 |
| 2.2 | Systemkonten, Anmelde-Shells, Sperren (`usermod -L`, `nologin`), Ablauf (`chage`), `login.defs` | 2 |
| 2.3 | Praxis: Konten anlegen, prüfen und sperren (`konten_pruefen.sh`) | 3 |
| 2.4 | Konzept: persönliche Konten, Dienstkonten, Gruppen, Verzicht auf gemeinsame Konten | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kontodateien lesen (Einheit 2.1):** Lesen Sie auf `vm01` je eine Zeile aus `/etc/passwd` und `/etc/shadow` und erklären Sie jedes Feld. Prüfen Sie mit `ls -l`, welche Rechte `/etc/shadow` hat, und erklären Sie, warum `/etc/passwd` lesbar sein darf.
2. **Sperren und Ablauf (Einheit 2.2):** Legen Sie ein Testkonto an, sperren Sie es mit `usermod -L`, setzen Sie mit `chage` ein Höchstalter von 90 Tagen und zeigen Sie das Ergebnis mit `chage -l` und `passwd -S`. Ändern Sie danach die Shell auf `/usr/sbin/nologin`.
3. **Konten prüfen (Einheit 2.3):** Führen Sie `bash konten_pruefen.sh` aus (oder die Befehle einzeln) und erklären Sie jede der sieben Prüfungen. Legen Sie auf `vm01` selbst ein Testkonto mit leerem Passwortfeld und ein zweites Konto mit UID 0 an, finden Sie beide mit `awk` und löschen Sie sie wieder.
4. **Kontenkonzept (Einheit 2.4):** Entwerfen Sie für ein Team aus zwei Administratoren und einer Webanwendung das Kontenkonzept: Namensschema, Gruppen, Dienstkonto, Umgang mit `root`. Halten Sie fest, wer sich wann wie anmelden darf.

#### Kontrollfragen

1. Warum steht das Passwort-Hash nicht in `/etc/passwd`?
2. Wie erkennt man an `/etc/shadow`, dass ein Konto gesperrt ist, und wie, dass es kein Passwort hat?
3. Was bewirkt die Shell `/usr/sbin/nologin` bei einem Dienstkonto, und was nicht?
4. Warum ist ein zweites Konto mit UID 0 gefährlicher als ein zweites Administratorkonto mit `sudo`?
5. Welches Hash-Verfahren verwendet Ubuntu 24.04 im Test für neue Passwörter, und woran erkennt man es?

### Modul 3: PAM: Passwortqualität und Kontosperre

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer PAM-Dienstdatei lesen und die Kontrollflags `required`, `requisite`, `sufficient` und `[success=1 default=bad]` erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Passwortregeln mit `pwquality.conf` festlegen und mit `pwscore` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Kontosperre mit `pam_faillock` einrichten und ein Konto entsperren.
  * Nach Abschluss dieses Moduls kann der Lernende eine Änderung an PAM so testen, dass man sich nicht aussperrt.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Aufbau von PAM: Modultypen (auth, account, password, session), Kontrollflags, Dateien in `/etc/pam.d` | 3 |
| 3.2 | Passwortqualität mit `pam_pwquality` und `pwquality.conf` (Länge, Zeichenklassen, Wörterbuch) | 2 |
| 3.3 | Kontosperre bei Fehlversuchen mit `pam_faillock` (Schwelle, Sperrzeit, Entsperren) | 2 |
| 3.4 | Praxis: Passwortqualität und Kontosperre mit eigenem PAM-Dienst testen (`pam_test.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **PAM-Datei lesen (Einheit 3.1):** Öffnen Sie `/etc/pam.d/sshd` und `/etc/pam.d/common-auth` auf `vm01`. Ordnen Sie jede Zeile einem Modultyp zu und erklären Sie die Kontrollflags. Zeichnen Sie den Ablauf einer Anmeldung als Folge der Module.
2. **Passwortregeln (Einheit 3.2):** Legen Sie unter `/etc/security/pwquality.conf.d/` eine Datei mit Mindestlänge 12, mindestens drei Zeichenklassen und höchstens zwei gleichen Zeichen hintereinander an. Prüfen Sie fünf Beispielpasswörter mit `pwscore` und erklären Sie jede Ablehnung.
3. **Kontosperre einrichten (Einheit 3.3):** Legen Sie einen eigenen PAM-Dienst `p14-test` mit `pam_faillock` (drei Fehlversuche, 60 Sekunden Sperre) an und testen Sie ihn mit `pamtester`. Zeigen Sie die Fehlversuche mit `faillock` und entsperren Sie das Konto mit `faillock --reset`.
4. **Skript auswerten (Einheit 3.4):** Führen Sie `bash pam_test.sh` aus und erklären Sie jede Ausgabe. Beschreiben Sie, wie Sie eine Änderung an `/etc/pam.d/common-auth` auf `vm01` sicher testen (zweite Sitzung, Sicherung, Prüfpunkt).

#### Kontrollfragen

1. Was bedeutet `required` im Unterschied zu `requisite`?
2. Warum steht `pam_faillock` mit `preauth` vor `pam_unix` und mit `authfail` danach?
3. Wie viele Zeichenklassen kennt `pwquality` (`minclass`), und welche?
4. Warum prüft `pwscore` ein Passwort nicht gegen die Regeln, die in `/etc/pam.d` stehen?
5. Welche Gefahr hat eine Kontosperre für Dienstkonten oder für root?

### Modul 4: sudo: Rechte vergeben und protokollieren

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine sudoers-Regel lesen und schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte mit Befehlsaliasen auf das Nötige beschränken.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln mit `visudo -cf` und `sudo -l -U` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Befehle erkennen, die aus sudo eine Shell machen, und die Protokollierung einrichten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | `sudo` und `su` im Vergleich; Syntax der `sudoers`-Regeln (Benutzer, Rechner, Zielbenutzer, Befehle) | 2 |
| 4.2 | Least Privilege mit `Cmnd_Alias`, `Defaults`, `sudoers.d` und Prüfung mit `visudo -c` | 2 |
| 4.3 | Praxis: Regeln schreiben, prüfen und testen (`sudo_test.sh`) | 2 |
| 4.4 | Fallstricke: Shell-Ausbrüche, `NOPASSWD`, Umgebungsvariablen, Protokolle und Auswertung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regel lesen (Einheit 4.1):** Lesen Sie `/etc/sudoers` und das Verzeichnis `/etc/sudoers.d` auf `vm01` und erklären Sie jede aktive Zeile. Vergleichen Sie `su -` und `sudo -i` in Bezug auf Protokollierung und Passwort.
2. **Eingeschränkte Rechte (Einheit 4.2):** Schreiben Sie in `/etc/sudoers.d/` eine Datei, die dem Konto `t14ops` genau zwei Befehle als root erlaubt (mit vollem Pfad), mit eigener Protokolldatei. Prüfen Sie sie mit `visudo -cf`, setzen Sie die Rechte 0440 und listen Sie die Rechte mit `sudo -l -U t14ops`.
3. **Skript auswerten (Einheit 4.3):** Führen Sie `bash sudo_test.sh` aus. Erklären Sie, warum der Aufruf von `cat /etc/shadow` scheitert, und was bei einer Datei mit Syntaxfehler (Abschnitt 2) passiert. Prüfen Sie die Protokolldatei.
4. **Ausbrüche prüfen (Einheit 4.4):** Erklären Sie für `vi`, `less`, `find` und `awk`, warum eine sudo-Freigabe daraus eine Root-Shell machen kann, und beschreiben Sie zwei Gegenmaßnahmen (`NOEXEC`, `sudoedit`, andere Werkzeuge).

#### Kontrollfragen

1. Warum soll eine sudoers-Datei immer mit `visudo` bearbeitet werden?
2. Warum muss in der Regel der volle Pfad des Befehls stehen?
3. Was bewirkt `use_pty` und was `logfile`?
4. Welche Gefahr hat `NOPASSWD`, und wann ist es trotzdem vertretbar?

### Modul 5: SSH-Härtung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Schlüsselanmeldung einrichten und die Passwortanmeldung abschalten.
  * Nach Abschluss dieses Moduls kann der Lernende eine `sshd_config` mit `sshd -t` prüfen und mit `sshd -T` die wirksamen Werte lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldungen auf Gruppen beschränken und Weiterleitungen sperren.
  * Nach Abschluss dieses Moduls kann der Lernende die Konfiguration mit `ssh-audit` bewerten und die Ergebnisse deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen so einführen, dass man sich nicht aussperrt.
* **Voraussetzungen:** Modul 2; zweiter Rechner `cl01` mit SSH-Client.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | SSH-Grundlagen: Protokoll, Host- und Benutzerschlüssel, Schlüsseltypen, `authorized_keys` | 2 |
| 5.2 | Wichtige Optionen in `sshd_config`: Anmeldung, Benutzer, Weiterleitungen, Algorithmen, Protokollierung | 3 |
| 5.3 | Praxis: gehärteten sshd aufbauen und testen (`ssh_haertung.sh`), Bewertung mit `ssh-audit` | 3 |
| 5.4 | Anmeldung absichern: `AllowGroups`, `Match`, Zwei-Faktor (Überblick), Aussperren vermeiden | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Schlüssel einrichten (Einheit 5.1):** Erzeugen Sie auf `cl01` ein Schlüsselpaar mit `ssh-keygen -t ed25519`, installieren Sie den öffentlichen Schlüssel für ein Testkonto auf `vm01` und melden Sie sich damit an. Notieren Sie den Fingerabdruck des Server-Hostschlüssels und vergleichen Sie ihn mit der Meldung beim ersten Verbinden.
2. **Härtung schreiben (Einheit 5.2):** Schreiben Sie unter `/etc/ssh/sshd_config.d/` eine Datei, die Root-Anmeldung und Passwortanmeldung verbietet, `MaxAuthTries` auf 3 setzt, Weiterleitungen und X11 verbietet und nur Mitglieder einer Gruppe zulässt. Prüfen Sie mit `sshd -t`, lesen Sie die Werte mit `sshd -T` und laden Sie den Dienst neu, ohne die laufende Sitzung zu schließen.
3. **Skript auswerten (Einheit 5.3):** Führen Sie `bash ssh_haertung.sh` aus und erklären Sie, warum die drei Anmeldeversuche (Konto außerhalb der Gruppe, root, Passwort) scheitern und die Weiterleitung nicht funktioniert. Bewerten Sie den Ausgangszustand und den gehärteten sshd mit `ssh-audit` und vergleichen Sie die Zahl der Fehler und Warnungen.
4. **Sicher einführen (Einheit 5.4):** Beschreiben Sie in einer Checkliste, wie Sie die SSH-Härtung auf `vm01` einführen, ohne sich auszusperren (zweite Sitzung, `sshd -t`, Prüfpunkt, Test mit neuem Fenster, Rückfall). Skizzieren Sie, wie ein zweiter Faktor (z. B. TOTP mit einem PAM-Modul) hinzukäme (nicht umsetzen).

#### Kontrollfragen

1. Warum prüft man vor jedem Neuladen von sshd mit `sshd -t`?
2. Was ist der Unterschied zwischen `sshd -t` und `sshd -T`?
3. Warum genügt `PasswordAuthentication no` allein nicht, wenn `KbdInteractiveAuthentication yes` bleibt?
4. Was bewirkt `AllowGroups`, und was passiert mit allen anderen Konten, auch mit root?
5. Wovor schützt ein Hostschlüssel-Abgleich beim ersten Verbinden?

### Modul 6: Dienste, Pakete und Kernel-Parameter

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende lauschende Dienste mit `ss` einem Prozess zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende nicht benötigte Dienste abschalten und Dienste auf eine Adresse binden.
  * Nach Abschluss dieses Moduls kann der Lernende Kernel-Parameter prüfen, setzen und dauerhaft festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende unnötige Pakete erkennen und entfernen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Angriffsfläche inventarisieren: lauschende Dienste (`ss -tulpn`), laufende Dienste (`systemctl`), installierte Pakete | 3 |
| 6.2 | Dienste und Pakete reduzieren: abschalten, maskieren, entfernen; Sandboxing von Diensten mit systemd (Überblick) | 2 |
| 6.3 | Kernel-Parameter mit `sysctl`: Netzwerk- und Speicherschutz, dauerhafte Konfiguration in `/etc/sysctl.d` | 2 |
| 6.4 | Praxis: Dienste inventarisieren, Ports prüfen, `sysctl` vergleichen (`dienste_sysctl.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Inventar erstellen (Einheit 6.1):** Listen Sie auf `vm01` mit `ss -tulpn` alle lauschenden Dienste auf, mit `systemctl list-unit-files --state=enabled` die aktivierten Dienste und mit `apt list --installed` die Pakete (Zahl). Ordnen Sie jeden lauschenden Port einem Zweck zu und markieren Sie nicht benötigte.
2. **Dienste reduzieren (Einheit 6.2):** Schalten Sie einen nicht benötigten Dienst mit `systemctl disable --now` ab, maskieren Sie ihn mit `systemctl mask`, binden Sie einen Dienst in dessen Konfiguration auf `127.0.0.1` und prüfen Sie jeweils mit `ss` und von `cl01` mit `nc -z`.
3. **Kernel-Parameter (Einheit 6.3):** Legen Sie `/etc/sysctl.d/99-haertung.conf` mit den Parametern aus `dienste_sysctl.sh` (Abschnitt 4) an, laden Sie sie mit `sysctl --system` und vergleichen Sie Ist und Soll. Erklären Sie die Bedeutung von `rp_filter`, `accept_redirects` und `tcp_syncookies`.
4. **Skript auswerten (Einheit 6.4):** Führen Sie `bash dienste_sysctl.sh` aus und erklären Sie jede Ausgabe. Beschreiben Sie, welche Parameter im Namespace gesetzt werden konnten, welche nicht, und warum das Skript auf dem Host kein `sysctl -p` ausführt.

#### Kontrollfragen

1. Was ist der Unterschied zwischen `systemctl disable` und `systemctl mask`?
2. Warum ist ein Dienst, der nur auf `127.0.0.1` lauscht, weniger angreifbar?
3. Was bewirkt `net.ipv4.conf.all.rp_filter = 1`?
4. Warum ändern `sysctl`-Einstellungen im Namespace nicht den Host?
5. Warum ist „deinstallieren“ stärker als „abschalten“?

### Modul 7: Dateirechte, ACLs und Mount-Optionen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende setgid- und Sticky-Verzeichnisse für Gruppen- und Ablageverzeichnisse einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende ACLs setzen und mit `getfacl` lesen, einschließlich Standard-ACL.
  * Nach Abschluss dieses Moduls kann der Lernende Dateisysteme mit `noexec`, `nosuid` und `nodev` einhängen und die Wirkung testen.
  * Nach Abschluss dieses Moduls kann der Lernende SUID/SGID-Dateien finden und bewerten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Klassische Rechte: `umask`, SUID, SGID, Sticky-Bit; sichere Rechte für Konfigurationsdateien und Heimatverzeichnisse | 3 |
| 7.2 | ACLs (`setfacl`, `getfacl`, Standard-ACL) und Dateiattribute (`chattr +i`) | 2 |
| 7.3 | Mount-Optionen `noexec`, `nosuid`, `nodev`; getrennte Partitionen (`/tmp`, `/var`, `/home`) | 2 |
| 7.4 | Praxis: Rechte, ACLs und Mount-Optionen an einem Test-Dateisystem prüfen (`rechte_acl.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rechte prüfen (Einheit 7.1):** Prüfen Sie auf `vm01` die Rechte von `/etc/shadow`, `/etc/ssh/sshd_config`, `/etc/sudoers.d` und `/root`. Finden Sie mit `find` alle SUID- und SGID-Dateien und weltweit schreibbare Verzeichnisse ohne Sticky-Bit. Erklären Sie fünf der SUID-Programme.
2. **ACL anlegen (Einheit 7.2):** Legen Sie ein Gruppenverzeichnis mit setgid an, geben Sie einem Benutzer außerhalb der Gruppe per `setfacl` Leserechte (mit Standard-ACL für neue Dateien) und prüfen Sie mit `getfacl`, dass er lesen, aber nicht schreiben darf. Setzen Sie bei einer Konfigurationsdatei `chattr +i` und versuchen Sie, sie zu löschen.
3. **Mount-Optionen testen (Einheit 7.3):** Hängen Sie ein Loop-Dateisystem mit `nodev,nosuid,noexec` ein, legen Sie ein Skript und eine Programmkopie darauf ab und starten Sie beides. Erklären Sie, warum `sh skript.sh` trotz `noexec` funktioniert. Planen Sie, welche Verzeichnisse auf `vm01` eigene Mount-Optionen bekommen sollen.
4. **Skript auswerten (Einheit 7.4):** Führen Sie `bash rechte_acl.sh` aus und erklären Sie jeden der acht Abschnitte. Notieren Sie, welche Ausgabe die Wirkung von setgid, Sticky-Bit und ACL zeigt.

#### Kontrollfragen

1. Was bewirkt das setgid-Bit auf einem Verzeichnis?
2. Wozu dient das Sticky-Bit auf `/tmp`?
3. Warum schützt `noexec` nicht vollständig vor dem Ausführen von Skripten?
4. Welche Rolle spielt die ACL-Maske (`mask::`)?
5. Warum ist `chattr +i` kein Ersatz für Rechte?

### Modul 8: Mandatory Access Control: AppArmor und SELinux

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen DAC und MAC erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein AppArmor-Profil lesen und die Modi enforce und complain unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Profil auf Syntax prüfen und in den Kernel laden (in der VM).
  * Nach Abschluss dieses Moduls kann der Lernende SELinux-Kontext, -Modus und -Boolean in Grundzügen beschreiben und von AppArmor abgrenzen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | DAC und MAC im Vergleich: Idee der verbindlichen Zugriffskontrolle, Linux Security Modules | 2 |
| 8.2 | AppArmor: Profile, Modi (enforce, complain), Syntax, Werkzeuge (`aa-status`, `aa-genprof`, `apparmor_parser`) | 3 |
| 8.3 | SELinux: Grundbegriffe (Kontext, Typ, Modus, Boolean), Unterschied zu AppArmor | 2 |
| 8.4 | Praxis: Zustand prüfen und ein Profil auf Syntax prüfen (`profil_syntax.sh`) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **DAC und MAC unterscheiden (Einheit 8.1):** Erklären Sie an einem Beispiel (ein Webserver-Prozess, der durch einen Fehler fremde Dateien lesen will), was DAC (Dateirechte) verhindert und was erst MAC verhindert.
2. **Profil schreiben und prüfen (Einheit 8.2):** Schreiben Sie ein AppArmor-Profil für ein kleines Programm (nur lesen unter `/etc/t14app/`, schreiben in eine Protokolldatei, Zugriff auf `/etc/shadow` verboten, TCP erlaubt). Prüfen Sie die Syntax mit `apparmor_parser -Q -K`, laden Sie es in der VM im Modus complain und zeigen Sie es mit `aa-status`.
3. **SELinux einordnen (Einheit 8.3):** Erklären Sie in je zwei Sätzen: Sicherheitskontext (`user:role:type:level`), Modi (enforcing, permissive, disabled), Boolean. Notieren Sie, was `getenforce` und `sestatus` auf `vm01` melden, und warum Debian/Ubuntu dort in der Regel „disabled“ zeigen.
4. **Skript auswerten (Einheit 8.4):** Führen Sie `bash profil_syntax.sh` aus und erklären Sie jede Ausgabe, insbesondere warum `aa-status` im Testsystem „apparmor not present“ meldet.

#### Kontrollfragen

1. Warum kann ein Prozess mit der UID eines Dienstes trotz korrekter Dateirechte durch MAC weiter eingeschränkt werden?
2. Was ist der Unterschied zwischen dem Modus enforce und complain in AppArmor?
3. Worin unterscheiden sich AppArmor und SELinux bei der Zuordnung von Regeln (Pfad oder Kontext)?
4. Wann ist eine Syntaxprüfung ohne Kernel nützlich, und was prüft sie nicht?

### Modul 9: Host-Firewall für den Server

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Server-Regelwerk mit Default-Drop in nftables lesen und schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende SSH nur aus dem Verwaltungsnetz und mit Rate-Limit erlauben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Firewall-Änderung so einführen, dass man sich nicht aussperrt.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen eines Frontends wie `ufw` benennen.
* **Voraussetzungen:** Modul 5; Grundlagen nftables aus dem Kurs „Linux-Firewall mit nftables und iptables“ (nur Überblick nötig).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Grundsatz „alles verbieten, was nicht erlaubt ist“ auf einem Server; Verwaltungsnetz, Dienste, Protokollierung (Verweis: Kurs „Linux-Firewall mit nftables und iptables“) | 2 |
| 9.2 | Server-Regelwerk mit nftables: Tabelle `inet`, Set für Verwaltungsadressen, Rate-Limit für SSH, Aussperrschutz | 2 |
| 9.3 | Frontend `ufw`: Befehle und Trockenlauf (`--dry-run`), Grenzen gegenüber nftables | 1 |
| 9.4 | Praxis: Regelwerk laden und von zwei Quelladressen testen (`firewall_test.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dienste und Quellen festlegen (Einheit 9.1):** Legen Sie für `vm01` fest, welche Dienste (Port, Protokoll) aus welchen Quellnetzen erreichbar sein sollen, und schreiben Sie das als Tabelle. Begründen Sie, welche Verbindungen ausgehend erlaubt bleiben.
2. **Regelwerk anpassen (Einheit 9.2):** Passen Sie `server_firewall.nft` an die Tabelle aus Aufgabe 1 an (Adressen, Ports). Prüfen Sie die Syntax mit `nft -c -f`, laden Sie es und prüfen Sie mit `nft list ruleset`.
3. **ufw im Trockenlauf (Einheit 9.3):** Geben Sie auf `vm01` die ufw-Befehle für dieselben Freigaben ein, zunächst mit `ufw --dry-run`, und vergleichen Sie die erzeugten Regeln mit Ihrer nftables-Datei. Nennen Sie zwei Dinge, die Sie mit ufw nicht so genau ausdrücken können.
4. **Test und Aussperrschutz (Einheit 9.4):** Führen Sie `bash firewall_test.sh` aus und erklären Sie jede Zeile. Beschreiben Sie, wie Sie das Regelwerk auf `vm01` laden, ohne sich auszusperren (zweite Sitzung, zeitgesteuerter Rückfall mit `at`, `nft -c`).

#### Kontrollfragen

1. Warum werden `ct state established,related` und die Loopback-Schnittstelle vor dem Drop-Eintrag erlaubt?
2. Warum gehört `ct state invalid drop` vor die Dienstregeln?
3. Was bewirkt `limit rate 6/minute burst 6 packets` bei SSH, und welche Nebenwirkung hat es?
4. Was ist der Vorteil eines Sets für Verwaltungsadressen gegenüber mehreren Einzelregeln?

### Modul 10: Protokollierung und auditd

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Protokollquellen eines Linux-Servers benennen und Rotation und Aufbewahrung festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende auditd-Regeln für Dateien, Programme und Systemaufrufe schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse mit `ausearch` und `aureport` finden und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Zeitsynchronisation und zentraler Protokollsammlung erklären.
* **Voraussetzungen:** Modul 4; Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Protokollarchitektur: `journald`, `rsyslog`, `/var/log`, Rotation mit `logrotate`; wichtige Protokolle (auth, syslog) | 3 |
| 10.2 | `auditd`: Aufbau, Regeln (Watches und Systemaufrufe), `auditctl`, `audit.rules`, `augenrules` | 3 |
| 10.3 | Praxis: Regeln laden, Ereignisse auslösen, mit `ausearch` und `aureport` auswerten (`audit_test.sh`) | 2 |
| 10.4 | Auswertung und Weiterleitung: Zeitsynchronisation, zentrale Sammlung, Alarmierung (Konzept) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Protokolle erkunden (Einheit 10.1):** Finden Sie auf `vm01` die Protokolle für Anmeldungen, sudo-Aufrufe und Paketänderungen (z. B. `/var/log/auth.log`, `journalctl _COMM=sudo`, `/var/log/dpkg.log`). Lesen Sie die Konfiguration von `logrotate` und halten Sie fest, wie lange Protokolle aufbewahrt werden.
2. **auditd-Regeln schreiben (Einheit 10.2):** Schreiben Sie Regeln, die Änderungen an `/etc/sudoers.d/` und einer Testkonfigurationsdatei sowie die Ausführung von `chage` und das Einhängen von Dateisystemen protokollieren. Laden Sie sie mit `auditctl -R` und zeigen Sie sie mit `auditctl -l`.
3. **Ereignisse auswerten (Einheit 10.3):** Führen Sie `bash audit_test.sh` aus. Lösen Sie die Ereignisse einzeln auf `vm01` aus und finden Sie sie mit `ausearch -k` und `aureport -f -i`. Erklären Sie die Felder `syscall`, `exe`, `auid` und `key`.
4. **Sammlung planen (Einheit 10.4):** Skizzieren Sie, wie Protokolle von drei Servern zentral gesammelt würden (Weiterleitung mit rsyslog, Zeitsynchronisation, Aufbewahrung, Zugriffsschutz) und welche fünf Ereignisse einen Alarm auslösen sollen.

#### Kontrollfragen

1. Wofür steht `-p wa` in einer Watch-Regel?
2. Warum ist `auid=unset` im Testlauf kein Fehler?
3. Warum müssen die Uhren aller Server synchron laufen?
4. Welche Gefahr besteht, wenn auditd viele Ereignisse erzeugt und das Protokoll volläuft?

### Modul 11: Updates und automatische Sicherheitsupdates

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Paketquellen und die Prüfung von Signaturen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende automatische Sicherheitsupdates mit `unattended-upgrades` einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Probelauf auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Neustart-Bedarf und Rückfall planen.
* **Voraussetzungen:** Modul 1; Internetphase für `vm01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Patch-Strategie: Paketquellen, Signaturen, Sicherheitsupdates, Wartungsfenster, Kernel-Updates | 2 |
| 11.2 | `unattended-upgrades`: erlaubte Herkünfte, Ausschlüsse, Neustart, Benachrichtigung | 3 |
| 11.3 | Praxis: Einstellungen prüfen und Probelauf (`updates_test.sh`) | 2 |
| 11.4 | Neustart und Rückfall: `needrestart`, Haltemarkierungen, Prüfpunkte | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Paketquellen prüfen (Einheit 11.1):** Lesen Sie die Paketquellen auf `vm01` (`/etc/apt/sources.list.d/`) und erklären Sie, wie `apt` die Paketlisten auf Echtheit prüft (Signatur der Release-Datei, Schlüsselringe). Notieren Sie, welche Quelle Sicherheitsupdates liefert.
2. **Automatik einrichten (Einheit 11.2):** Aktivieren Sie `unattended-upgrades` mit einer eigenen Zusatzdatei in `/etc/apt/apt.conf.d/` (nur Sicherheitsquellen, ungenutzte Abhängigkeiten entfernen, kein automatischer Neustart, Benachrichtigung an root) und prüfen Sie die wirksamen Einstellungen mit `apt-config dump`.
3. **Probelauf auswerten (Einheit 11.3):** Führen Sie `bash updates_test.sh` aus (oder `unattended-upgrade --dry-run`) und lesen Sie das Protokoll `/var/log/unattended-upgrades/unattended-upgrades.log`. Erklären Sie, welche Pakete aktualisiert würden und warum.
4. **Neustartkonzept (Einheit 11.4):** Legen Sie fest, wann `vm01` neu gestartet wird (Wartungsfenster), wie Sie den Bedarf mit `needrestart` erkennen und wie Sie vor Kernel-Updates einen Prüfpunkt anlegen.

#### Kontrollfragen

1. Warum soll `Automatic-Reboot` bei Servern mit Diensten bewusst entschieden werden?
2. Wie schützt die Signatur der `Release`-Datei vor manipulierten Paketen?
3. Was bewirkt `apt-mark hold`, und wann ist es sinnvoll?
4. Warum ersetzen automatische Sicherheitsupdates kein Patch-Management für Anwendungen außerhalb der Paketquellen?

### Modul 12: Integritätsprüfung (AIDE) und Schutz vor Dauerangriffen (fail2ban)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende AIDE mit eigener Konfiguration einrichten und Änderungen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Datenbank so schützen, dass ein Angreifer sie nicht unbemerkt ändern kann.
  * Nach Abschluss dieses Moduls kann der Lernende einen fail2ban-Filter gegen eine Protokolldatei testen.
  * Nach Abschluss dieses Moduls kann der Lernende Vor- und Nachteile automatischer Sperren benennen.
* **Voraussetzungen:** Modul 5; Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Dateiintegrität mit AIDE: Datenbank, Regeln, Prüfung, Pflege nach Updates, Schutz der Datenbank | 3 |
| 12.2 | Schutz vor wiederholten Anmeldeversuchen mit fail2ban: Filter, Jails, `maxretry`, `findtime`, `bantime` | 2 |
| 12.3 | Praxis: AIDE-Datenbank und Prüfung, fail2ban-Filter testen (`integritaet_test.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **AIDE einrichten (Einheit 12.1):** Legen Sie auf `vm01` eine AIDE-Konfiguration für `/etc` und `/usr/local/bin` an, erzeugen Sie die Datenbank mit `aide --init` und prüfen Sie ohne Änderung (Rückgabewert 0).
2. **Änderungen erkennen (Einheit 12.1):** Ändern Sie eine Konfigurationsdatei, legen Sie eine neue an und ändern Sie Rechte. Prüfen Sie mit `aide --check`, deuten Sie den Bericht und den Rückgabewert und erklären Sie, wo die Datenbank sicher abgelegt werden sollte.
3. **Filter testen (Einheit 12.2):** Führen Sie `bash integritaet_test.sh` aus. Testen Sie den Filter `sshd` mit `fail2ban-regex` gegen `beispiel_ssh.log` und erklären Sie die Zeile „Lines“ der Ausgabe.
4. **Jail planen (Einheit 12.3):** Schreiben Sie eine Jail-Einstellung für sshd (drei Versuche in zehn Minuten, Sperre eine Stunde) und nennen Sie, welche Adressen nie gesperrt werden dürfen (`ignoreip`) und warum.

#### Kontrollfragen

1. Warum ist eine AIDE-Datenbank auf demselben Rechner wertlos, wenn ein Angreifer root erlangt?
2. Was bedeutet der Rückgabewert 5 von `aide --check` im Testlauf?
3. Welche Nebenwirkung hat eine automatische Sperre bei Anmeldeversuchen hinter NAT?
4. Warum ersetzt fail2ban die Schlüsselanmeldung nicht?

### Modul 13: Härtung prüfen, Fehlersuche und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Lynis-Bericht lesen und Vorschläge bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler nach einer Härtung systematisch eingrenzen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende einen eigenen Prüfkatalog schreiben und vorher/nachher messen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Härtungsprotokoll mit Ausnahmen abschließen.
* **Voraussetzungen:** Module 1 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Härtung bewerten: Lynis-Bericht lesen (Index, Warnungen, Vorschläge), Grenzen, Ergänzung durch eigene Prüfungen | 2 |
| 13.2 | Fehlersuche nach Härtung: Aussperren, Dienste, die nicht mehr starten; Diagnosewerkzeuge (`sshd -T`, `visudo -c`, `nft -c`, `pamtester`, `ss`, `ausearch`) | 3 |
| 13.3 | Praxis: Prüfkatalog und Messung vorher/nachher (`pruefkatalog.sh`, `abschluss_messung.sh`) | 3 |
| 13.4 | Abschluss: Härtungsprotokoll fertigstellen, Ausnahmen begründen, Wiederholung und Betrieb | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bericht lesen (Einheit 13.1):** Führen Sie `lynis audit system` auf `vm01` aus und lesen Sie `/var/log/lynis-report.dat`. Wählen Sie fünf Vorschläge, ordnen Sie sie einem Modul dieser Reihe zu und entscheiden Sie, ob Sie die Maßnahme umsetzen oder als Ausnahme begründen.
2. **Fehlersuche (Einheit 13.2):** Bauen Sie nacheinander fünf Fehler ein (Tippfehler in `sshd_config`, Syntaxfehler in `sudoers.d`, Firewall-Regel, die SSH blockiert, falsche Rechte an `authorized_keys`, `noexec` auf einem Skriptverzeichnis) und beheben Sie jeden mit dem passenden Diagnosewerkzeug. Notieren Sie für jeden Fehler Symptom, Werkzeug, Ursache und Lösung.
3. **Messen (Einheit 13.3):** Führen Sie `bash pruefkatalog.sh` und danach `bash abschluss_messung.sh` aus. Vergleichen Sie Prüfkatalog und Lynis-Index vorher und nachher und erklären Sie, warum der Index weniger steigt als die Zahl bestandener Prüfungen.
4. **Abschluss (Einheit 13.4):** Stellen Sie das Härtungsprotokoll fertig (alle Maßnahmen, Messwerte, Ausnahmen, offene Punkte) und legen Sie einen Wiederholungsplan fest (Prüfung nach Updates, Lynis monatlich, Review der Ausnahmen). Löschen Sie die Prüfpunkte.

#### Kontrollfragen

1. Warum kann der Lynis-Index nach einer richtigen Maßnahme unverändert bleiben?
2. Welche Reihenfolge der Eingrenzung empfehlen Sie bei „nach der Härtung kann ich mich nicht mehr anmelden“?
3. Warum gehört eine Ausnahme mit Begründung ins Protokoll, statt die Prüfung zu ändern?
4. Welche Teile der Härtung lassen sich nicht automatisch prüfen?
