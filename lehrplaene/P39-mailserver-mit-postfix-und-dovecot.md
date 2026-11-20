# Lehrplan: Mailserver mit Postfix und Dovecot

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux- und DNS-Grundlagen |
| **Gesamtumfang** | 10 Module, 110 UE (zu 45 Minuten; 82,5 Stunden) |
| **Fokus-Technologien** | Postfix (MTA), Dovecot (IMAP, MDA-Funktion der Zustellung ins Maildir, SASL), Debian/Ubuntu Linux |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: SPF, DKIM und DMARC im Kurs „E-Mail-Authentifizierung: SPF, DKIM und DMARC“, Exchange Online im Kurs „Exchange Online Administration“, DNS-Grundlagen und Linux-Grundlagen in eigenen Kursen. Nicht behandelt: Betrieb von Spam- und Virenfiltern im Detail (nur Überblick), Webmail, Groupware, Mailinglisten, Cluster und Replikation, Betrieb eines öffentlich erreichbaren Mailservers (Reputation, Reverse-DNS, Blocklisten) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Mail-Architektur: MUA, MTA, MDA und der Weg einer Nachricht | 1 | 10 |
| 2 | Postfix-Grundkonfiguration | 1 | 10 |
| 3 | DNS für E-Mail: MX, A und Namen | 1 | 10 |
| 4 | Benutzer, Postfächer und Aliase | 1 | 12 |
| 5 | Dovecot als IMAP-Server | 1 | 12 |
| 6 | TLS für SMTP und IMAP | 1 | 12 |
| 7 | Authentifizierung und Submission | 1 | 12 |
| 8 | Relay-Regeln und Warteschlange | 1 | 12 |
| 9 | Spam- und Missbrauchsschutz im Überblick | 2 | 10 |
| 10 | Protokolle, Fehlersuche und Sicherung | 1 | 10 |
| **Gesamt** | 10 Module | 9 × Priorität 1, 1 × Priorität 2 | **110** |

**Priorität 1** (Pflicht) sind die Module 1 bis 8 und 10; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 9 (Spam- und Missbrauchsschutz im Überblick). Fällt Modul 9 weg, verringert sich der Gesamtumfang auf 100 UE; kein Pflichtmodul setzt Modul 9 voraus.

### 2. Quellen

**Nicht gelesen:** Die offizielle Dokumentation von Postfix (postfix.org) und Dovecot (doc.dovecot.org) sowie die RFCs zu SMTP (5321), Nachrichtenformat (5322) und IMAP (3501/9051) wurden **nicht** gelesen. Alle Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch die Läufe im Labor bestätigt. Parameternamen und Standardwerte zeigt das Skript jeweils selbst (`postconf -d`); verbindlich ist immer die Dokumentation der installierten Version.

**Getestet mit:** Postfix 3.8.6 und Dovecot 2.3.21 (Pakete aus Ubuntu 24.04), dnsmasq, swaks, OpenSSL, Python 3. Die Beispieldaten (Konten, Domains, Passwörter, Nachrichten) sind **frei erfunden**; es wird ausschließlich `example.com` (reservierte Beispiel-Domain) verwendet.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Mail`, `10.39.0.0/24`).

**VMs:** `dns01` (**erforderlich**, `10.39.0.2`): Linux mit einem DNS-Server (z. B. BIND 9 oder dnsmasq) für die Zone `example.com` mit MX-Eintrag auf `mail.example.com`. `mail01` (**erforderlich**, `10.39.0.3`): Ubuntu Server 24.04 oder Debian 12 mit den Paketen `postfix`, `dovecot-imapd`, `swaks`, `openssl`; als DNS-Server `dns01` eintragen. `win11` (**erforderlich ab Modul 5**, `10.39.0.20`): Windows 11 mit einem E-Mail-Programm (z. B. Thunderbird) zum Testen von IMAP und Submission.

**Internetphase:** Für die Paketinstallation braucht `mail01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es wird **kein** öffentlicher Mailserver betrieben; es gibt keine Verbindung zu fremden Mailservern.

**Prüfpunkt (Checkpoint):** Vor Modul 4 und vor Modul 8 von `mail01` je einen Prüfpunkt anlegen.

**Skripte:** Die Beispielskripte liefen **nicht** in Hyper-V und nicht mit `systemd`, sondern in einem Cloud-Container mit einer **privaten Instanz** (`lab.sh`): Postfix auf `127.0.0.1:2525` (Submission `127.0.0.1:5587`), Dovecot auf `127.0.0.1:1143`, dnsmasq als DNS auf `127.0.0.1:5353`, Arbeitsordner `/tmp/p39`, Test-Konten `t39alice` und `t39bob`. Auf `mail01` gelten die Standardports 25, 587 und 143 und die Konfiguration in `/etc/postfix` und `/etc/dovecot`.

## B. Detaillierter Modulaufbau

### Modul 1: Mail-Architektur: MUA, MTA, MDA und der Weg einer Nachricht

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende MUA, MSA, MTA, MDA und Postfach unterscheiden und ihre Protokolle nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Umschlag und Kopfzeilen einer Nachricht unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen SMTP-Dialog von Hand führen und die Antwortcodes deuten.
  * Nach Abschluss dieses Moduls kann der Lernende den Weg einer Nachricht im Protokoll und in den Kopfzeilen nachvollziehen.
* **Voraussetzungen:** IP-Adressen und Ports; Linux-Grundlagen (Terminal).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Rollen: MUA, MSA, MTA, MDA, Postfach; Protokolle SMTP und IMAP | 3 |
| 1.2 | Aufbau einer Nachricht: Umschlag (envelope) und Kopfzeilen, Received-Zeilen | 2 |
| 1.3 | Praxis: SMTP-Dialog von Hand führen und den Weg im Protokoll verfolgen (`smtp_dialog.sh`) | 3 |
| 1.4 | Labor aufbauen und prüfen: `dns01`, `mail01`, `win11` am privaten Switch | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rollen zeichnen (Einheit 1.1):** Zeichnen Sie den Weg einer Nachricht von einem E-Mail-Programm zum Postfach des Empfängers und beschriften Sie MUA, MSA, MTA, MDA, Postfach und die Protokolle SMTP bzw. IMAP an jeder Strecke.
2. **Umschlag und Kopfzeilen (Einheit 1.2):** Erklären Sie anhand des Beispiels in `beispiele/smtp_dialog.ausgabe.txt` den Unterschied zwischen `MAIL FROM`/`RCPT TO` (Umschlag) und den Zeilen `From:`/`To:` (Kopfzeilen) und warum beide verschieden sein dürfen.
3. **SMTP-Dialog ausführen (Einheit 1.3):** Führen Sie `bash smtp_dialog.sh` aus (im Testlabor) oder öffnen Sie auf `mail01` mit `nc localhost 25` einen Dialog und senden Sie eine Nachricht an ein lokales Konto. Notieren Sie die Antwortcodes der Schritte EHLO, MAIL, RCPT, DATA und QUIT.
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie das Labor nach der Laborbeschreibung auf (privater Switch `Lab-Mail`, `dns01`, `mail01`, `win11`) und prüfen Sie mit `ping` die Verbindungen.

#### Kontrollfragen

1. Wozu dient der Umschlag, und was geschieht, wenn Umschlag und Kopfzeilen verschiedene Absender nennen?
2. Welche Aufgabe hat der MDA im Unterschied zum MTA?
3. Warum verwendet man SMTP zum Senden und IMAP zum Lesen?
4. Was verrät die Received-Zeile über den Weg einer Nachricht?

### Modul 2: Postfix-Grundkonfiguration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aufgabe von `main.cf` und `master.cf` unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die wichtigsten Basisparameter erklären und setzen.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationen mit `postconf` lesen, ändern und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Tippfehler und ungültige Parameter finden.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Installation und Dateien: `main.cf`, `master.cf`, Warteschlangenverzeichnis, Dienste | 2 |
| 2.2 | Wichtige Parameter: `myhostname`, `mydomain`, `myorigin`, `mydestination`, `mynetworks`, `inet_interfaces` | 3 |
| 2.3 | Konfiguration lesen und ändern: `postconf -n`, `-d`, `-e`, `postfix check`, `reload` (`postfix_konfig.sh`) | 3 |
| 2.4 | Fehler in der Konfiguration erkennen und beheben | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Parameter erklären (Einheit 2.2):** Erklären Sie in je einem Satz die Parameter `myhostname`, `mydestination`, `myorigin` und `mynetworks` und tragen Sie die Werte des Labors ein.
2. **Konfiguration auslesen (Einheit 2.3):** Führen Sie auf `mail01` `postconf -n` aus und vergleichen Sie die Ausgabe mit `postconf -d myhostname`. Notieren Sie, welche Parameter von der Standardeinstellung abweichen.
3. **Parameter ändern (Einheit 2.3):** Ändern Sie `smtpd_banner` mit `postconf -e`, prüfen Sie mit `postfix check`, laden Sie mit `postfix reload` neu und beobachten Sie die Begrüßung beim Verbinden (`postfix_konfig.sh`).
4. **Tippfehler finden (Einheit 2.4):** Setzen Sie absichtlich einen falsch geschriebenen Parameter und lesen Sie die Warnung. Entfernen Sie ihn mit `postconf -X`.
5. **Dateien zuordnen (Einheit 2.1):** Ordnen Sie `main.cf`, `master.cf` und das Warteschlangenverzeichnis ihrem Zweck zu und nennen Sie, wo sie im Labor liegen.

#### Kontrollfragen

1. Was ist der Unterschied zwischen `main.cf` und `master.cf`?
2. Wozu dient `mydestination`, und was geschieht mit Mails an andere Domains?
3. Warum ist ein zu weit gefasstes `mynetworks` gefährlich?
4. Warum prüft man vor dem Neuladen mit `postfix check`?

### Modul 3: DNS für E-Mail: MX, A und Namen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von MX-Einträgen und Prioritäten erklären.
  * Nach Abschluss dieses Moduls kann der Lernende MX und A mit `dig` abfragen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende die Auswahl des Zielservers nachvollziehen (kleinere Zahl zuerst).
  * Nach Abschluss dieses Moduls kann der Lernende typische DNS-Fehler bei Mailservern erkennen.
* **Voraussetzungen:** Modul 1; DNS-Grundlagen (A-Eintrag, Zone).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | MX-Eintrag, Priorität und A-Eintrag des Mailservers | 3 |
| 3.2 | Die Zone `example.com` auf `dns01` anlegen (BIND oder dnsmasq) | 3 |
| 3.3 | MX-Auswahl in Python nachbilden (`mx_auswahl.py`) und Abfragen mit `dig` (`dns_mx.sh`) | 2 |
| 3.4 | Fehlerbilder: fehlender MX, MX auf CNAME, fehlende Adresse | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eintrag lesen (Einheit 3.1):** Fragen Sie mit `dig MX example.com` den MX-Eintrag ab und lesen Sie Priorität und Name ab. Fragen Sie danach die Adresse des Mailservers ab.
2. **Zone anlegen (Einheit 3.2):** Legen Sie auf `dns01` die Zone `example.com` an mit `mail` (10.39.0.3) und einem MX-Eintrag Priorität 10. Prüfen Sie von `mail01` aus.
3. **Auswahl nachbilden (Einheit 3.3):** Führen Sie `python3 mx_auswahl.py example.com` aus. Fügen Sie einen zweiten MX mit Priorität 20 hinzu und erklären Sie, wann er verwendet wird (`dns_mx.sh`).
4. **Fehler suchen (Einheit 3.4):** Beschreiben Sie, was ein sendender Server tut, wenn für die Domain kein MX-Eintrag, aber ein A-Eintrag existiert, und was bei einem MX ohne Adresse geschieht.

#### Kontrollfragen

1. Warum hat ein MX-Eintrag eine Priorität, und welche Zahl wird zuerst versucht?
2. Was geschieht, wenn eine Domain keinen MX-Eintrag, aber einen A-Eintrag hat?
3. Warum sollte ein MX nicht auf einen CNAME zeigen?
4. Wozu dient ein zweiter MX mit höherer Zahl?

### Modul 4: Benutzer, Postfächer und Aliase

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines Maildir-Postfachs beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Aliase und virtuelle Aliase einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Nachschlagetabellen mit `postmap` und `postalias` erzeugen und abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum unbekannte Empfänger sofort abgelehnt werden sollten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Lokale Konten und das Maildir-Format (`new/`, `cur/`, `tmp/`) | 3 |
| 4.2 | Aliase: `aliases`-Datei, `postalias`, Verteilung an mehrere Empfänger | 3 |
| 4.3 | Virtuelle Aliase (`virtual_alias_maps`, `postmap`) | 3 |
| 4.4 | Unbekannte Empfänger: `local_recipient_maps` und Ablehnung im SMTP-Dialog (`postfaecher.sh`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konto anlegen (Einheit 4.1):** Legen Sie auf `mail01` zwei Konten an (z. B. `alice`, `bob`), senden Sie an `alice` eine Nachricht und prüfen Sie, dass `~/Maildir/new` entsteht.
2. **Alias einrichten (Einheit 4.2):** Richten Sie in `/etc/aliases` den Alias `hilfe` auf beide Konten ein, aktualisieren Sie die Datenbank mit `newaliases` und prüfen Sie mit `postalias -q hilfe /etc/aliases` (`postfaecher.sh`).
3. **Virtuellen Alias einrichten (Einheit 4.3):** Legen Sie `info@example.com` → `bob@example.com` über `virtual_alias_maps` an. Erzeugen Sie die Tabelle mit `postmap`, laden Sie neu und testen Sie mit `postmap -q`.
4. **Unbekannten Empfänger prüfen (Einheit 4.4):** Senden Sie eine Mail an ein nicht vorhandenes Konto und notieren Sie den Antwortcode. Erklären Sie, warum die Ablehnung während des Dialogs besser ist als ein späterer Unzustellbarkeitsbericht.

#### Kontrollfragen

1. Warum legt Maildir jede Nachricht als eigene Datei ab?
2. Worin unterscheiden sich Alias und virtueller Alias?
3. Wofür steht der Antwortcode 550 5.1.1?
4. Warum entsteht bei späterer Ablehnung „Backscatter“?

### Modul 5: Dovecot als IMAP-Server

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle von Dovecot und die Bedeutung von `passdb` und `userdb` erklären.
  * Nach Abschluss dieses Moduls kann der Lernende IMAP-Befehle von Hand ausführen und Antworten deuten.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, wie IMAP-Flags im Maildir gespeichert werden.
  * Nach Abschluss dieses Moduls kann der Lernende ein E-Mail-Programm mit dem Server verbinden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Aufgaben von Dovecot, Konfigurationsdateien, `mail_location`, Authentifizierung (`passdb`, `userdb`) | 3 |
| 5.2 | IMAP-Befehle von Hand: LOGIN, LIST, SELECT, FETCH, STORE, SEARCH | 3 |
| 5.3 | Flags im Dateinamen des Maildirs und Ordner (`dovecot_imap.sh`) | 3 |
| 5.4 | Anbindung eines E-Mail-Programms auf `win11` (Thunderbird) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration lesen (Einheit 5.1):** Lesen Sie auf `mail01` `doveconf -n` und erklären Sie `mail_location`, `passdb` und `userdb`.
2. **IMAP von Hand (Einheit 5.2):** Verbinden Sie sich mit `nc localhost 143`, melden Sie sich mit `a LOGIN alice <Passwort>` an, wählen Sie `SELECT INBOX`, rufen Sie `FETCH 1 (BODY[HEADER])` ab und setzen Sie `STORE 1 +FLAGS (\Seen)` (`dovecot_imap.sh`).
3. **Flags im Dateisystem (Einheit 5.3):** Sehen Sie nach dem Setzen von `\Seen` im Verzeichnis `~/Maildir/cur` nach und erklären Sie das Suffix `:2,S` im Dateinamen.
4. **Programm anbinden (Einheit 5.4):** Richten Sie auf `win11` ein Konto in Thunderbird ein (IMAP, Server `mail.example.com`, Port 143, STARTTLS) und rufen Sie die Testnachricht ab. Halten Sie die Fehlermeldung bei falschen Einstellungen fest.

#### Kontrollfragen

1. Wozu dienen `passdb` und `userdb`?
2. Warum bleibt eine per IMAP gelesene Nachricht auf dem Server?
3. Was bedeutet der Antwortcode `NO [AUTHENTICATIONFAILED]`?
4. Wo wird die Information „gelesen“ gespeichert?

### Modul 6: TLS für SMTP und IMAP

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende STARTTLS und implizites TLS unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Zertifikat für den Mailserver erzeugen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende TLS in Postfix und Dovecot einschalten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Verschlüsselung erzwingen und die Folgen für Clients beschreiben.
* **Voraussetzungen:** Modul 2; Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Warum TLS: Mitlesen und Veränderung auf dem Weg; STARTTLS und implizites TLS | 3 |
| 6.2 | Zertifikat für den Mailserver: selbst signiert im Labor, Namen im Zertifikat, Gültigkeit | 3 |
| 6.3 | Konfiguration in Postfix und Dovecot und Prüfung mit `openssl s_client` (`tls.sh`) | 3 |
| 6.4 | Verschlüsselung erzwingen (`smtpd_tls_security_level`) und Folgen für Clients | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verfahren abgrenzen (Einheit 6.1):** Beschreiben Sie den Unterschied zwischen STARTTLS (Port 25/587/143) und implizitem TLS (Port 465/993) und nennen Sie je einen Vor- und Nachteil.
2. **Zertifikat erzeugen (Einheit 6.2):** Erzeugen Sie mit `openssl req -x509 -newkey rsa:2048 -nodes -days 30 …` ein selbst signiertes Zertifikat für `mail.example.com` und lesen Sie Aussteller und Gültigkeit mit `openssl x509 -noout -subject -issuer -dates`.
3. **TLS prüfen (Einheit 6.3):** Prüfen Sie mit `openssl s_client -starttls smtp -connect …` und `-starttls imap` Protokollversion und Zertifikat (`tls.sh`). Erklären Sie die Meldung „self-signed certificate“.
4. **Erzwingen (Einheit 6.4):** Setzen Sie `smtpd_tls_security_level = encrypt` und senden Sie ohne und mit `swaks --tls`. Notieren Sie die Antwort ohne TLS.

#### Kontrollfragen

1. Warum ist STARTTLS allein kein Schutz vor aktivem Angreifer, wenn es nur „angeboten“ wird?
2. Warum meldet `openssl` „self-signed certificate“, und wann ist das in Ordnung?
3. Welche Folge hat `smtpd_tls_security_level = encrypt` auf Port 25 für fremde Server?
4. Warum muss der Name im Zertifikat zum Servernamen passen?

### Modul 7: Authentifizierung und Submission

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck des Submission-Ports erklären.
  * Nach Abschluss dieses Moduls kann der Lernende SASL-Anmeldung über Dovecot für Postfix konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldeversuche mit `swaks` testen und die Antworten deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldungen im Protokoll nachvollziehen.
* **Voraussetzungen:** Module 5 und 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Submission-Port 587: warum eigener Port, TLS-Pflicht, Anmeldung vor dem Senden | 3 |
| 7.2 | SASL über Dovecot: `smtpd_sasl_type = dovecot`, Auth-Socket, `permit_sasl_authenticated` | 3 |
| 7.3 | Tests mit `swaks`: ohne TLS, ohne Anmeldung, falsches und richtiges Passwort (`sasl_submission.sh`) | 3 |
| 7.4 | Protokollierung: `sasl_username` und Fehlversuche | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zweck beschreiben (Einheit 7.1):** Begründen Sie, warum Benutzer ihre Nachrichten über Port 587 mit Anmeldung einliefern sollen und nicht über Port 25.
2. **SASL einrichten (Einheit 7.2):** Richten Sie in `master.cf` einen Dienst `submission` mit `smtpd_tls_security_level=encrypt` und `smtpd_sasl_auth_enable=yes` ein und aktivieren Sie in Dovecot den Auth-Socket für Postfix (`master.cf`-Auszug in `lab.sh`).
3. **Tests ausführen (Einheit 7.3):** Führen Sie die vier Tests aus (`sasl_submission.sh`): ohne TLS, mit TLS ohne Anmeldung, mit falschem Passwort, mit richtigem Passwort. Notieren Sie je Test den Antwortcode.
4. **Protokoll lesen (Einheit 7.4):** Suchen Sie im Protokoll die Zeilen mit `sasl_username=` und die Warnung bei dem fehlgeschlagenen Versuch.

#### Kontrollfragen

1. Warum soll auf Port 587 die Anmeldung vor dem Senden verlangt werden?
2. Warum darf das Passwort nur über TLS gesendet werden?
3. Welche Rolle spielt der Auth-Socket zwischen Postfix und Dovecot?
4. Warum sind Fehlversuche im Protokoll wichtig?

### Modul 8: Relay-Regeln und Warteschlange

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wer Nachrichten an fremde Ziele weiterleiten darf.
  * Nach Abschluss dieses Moduls kann der Lernende ein offenes Relay im Test erkennen und schließen.
  * Nach Abschluss dieses Moduls kann der Lernende die Warteschlange lesen, einzelne Nachrichten ansehen, löschen und neu versuchen lassen.
  * Nach Abschluss dieses Moduls kann der Lernende zeitweilige und dauerhafte Fehler unterscheiden.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Wer darf weiterleiten: `smtpd_relay_restrictions`, `mynetworks`, Anmeldung | 3 |
| 8.2 | Offenes Relay erkennen und schließen (`relay_queue.sh`) | 3 |
| 8.3 | Warteschlange lesen: `postqueue -p`, `-j`, `postcat`, `postsuper`, `postqueue -f` | 3 |
| 8.4 | Zustellfehler: zeitweilig (4xx), dauerhaft (5xx), Wiederholung und Ablauf | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Relay testen (Einheit 8.1):** Senden Sie von einem fremden Client mit `swaks` eine Nachricht an eine externe Adresse über Port 25 und notieren Sie die Antwort. Erwartet ist die Ablehnung.
2. **Offenes Relay provozieren (Einheit 8.2):** Setzen Sie im Labor `mynetworks = 0.0.0.0/0`, wiederholen Sie den Test, notieren Sie das Ergebnis und stellen Sie danach die enge Einstellung wieder her (`relay_queue.sh`).
3. **Warteschlange untersuchen (Einheit 8.3):** Liefern Sie zwei Nachrichten an ein nicht erreichbares Ziel ein. Lesen Sie die Warteschlange mit `postqueue -p` und `-j`, sehen Sie eine Nachricht mit `postcat -q` an und löschen Sie sie mit `postsuper -d`.
4. **Fehlerarten erklären (Einheit 8.4):** Erklären Sie anhand des Protokolls den Unterschied zwischen `status=deferred` (4.4.1) und `status=bounced` (5.4.4).

#### Kontrollfragen

1. Warum ist ein offenes Relay gefährlich?
2. Was bedeutet `454 4.7.1 Relay access denied` im Unterschied zu 554?
3. Wann wird eine zeitweilig nicht zustellbare Nachricht endgültig abgewiesen?
4. Warum sollte man `postsuper -d ALL` nur mit Bedacht verwenden?

### Modul 9: Spam- und Missbrauchsschutz im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Schutzebenen gegen Spam und Missbrauch nennen.
  * Nach Abschluss dieses Moduls kann der Lernende einfache Regeln in Postfix einrichten und testen.
  * Nach Abschluss dieses Moduls kann der Lernende Rate-Limits einsetzen und ihre Wirkung beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende externe Filter einordnen.
* **Voraussetzungen:** Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Schutzebenen: Verbindung, HELO und Absender, Inhalt, Rate; Rolle von Spam- und Virenfiltern | 3 |
| 9.2 | Postfix-eigene Regeln: HELO-Pflicht, FQDN-Prüfung, `header_checks` (`spam_regeln.sh`) | 3 |
| 9.3 | Begrenzung pro Client: `smtpd_client_message_rate_limit` | 2 |
| 9.4 | Externe Filter im Überblick: SpamAssassin, Rspamd, ClamAV, `postscreen` | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ebenen zuordnen (Einheit 9.1):** Ordnen Sie die Regeln `reject_non_fqdn_helo_hostname`, `reject_non_fqdn_sender`, `header_checks` und `smtpd_client_message_rate_limit` den Schutzebenen zu.
2. **Regeln testen (Einheit 9.2):** Führen Sie `spam_regeln.sh` aus oder richten Sie die Regeln selbst ein. Notieren Sie je Regel den Antwortcode (504, 550, 450).
3. **Rate-Limit (Einheit 9.3):** Senden Sie fünf Nachrichten in kurzer Folge bei einem Limit von 3 und notieren Sie, ab wann die Annahme abgelehnt wird.
4. **Filter einordnen (Einheit 9.4):** Beschreiben Sie in je zwei Sätzen, was ein Spam-Filter (Inhaltsbewertung), ein Virenscanner und `postscreen` leisten und wo sie in den Mailfluss eingehängt werden.

#### Kontrollfragen

1. Warum ist eine einzelne Regel nie ausreichend?
2. Welches Risiko besteht bei `header_checks` mit zu allgemeinen Mustern?
3. Warum lehnt `smtpd_client_message_rate_limit` mit 450 und nicht mit 550 ab?
4. Warum wurde in dieser Übung kein Spamfilter ausgeführt?

### Modul 10: Protokolle, Fehlersuche und Sicherung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Protokollzeilen einer Zustellung über die Queue-ID verfolgen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Protokoll auswerten und Fehlerursachen zählen.
  * Nach Abschluss dieses Moduls kann der Lernende Postfächer und Konfiguration sichern und die Wiederherstellung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehlerbilder eingrenzen.
* **Voraussetzungen:** Module 1 bis 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Protokolle lesen: Postfix-Zeilen, Queue-ID, Status; `journalctl` bzw. `/var/log/mail.log` | 2 |
| 10.2 | Protokoll auswerten mit `log_auswerten.py` und typische Fehlerbilder | 3 |
| 10.3 | Sicherung: Postfächer, Konfiguration; Wiederherstellung und Prüfsummen (`logs_sicherung.sh`) | 3 |
| 10.4 | Abschlussübung: Fehler suchen und Selbstprüfung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zustellung verfolgen (Einheit 10.1):** Verfolgen Sie eine Nachricht im Protokoll über ihre Queue-ID von `smtpd` über `cleanup` und `qmgr` bis `local`/`smtp` und beschreiben Sie die Stationen.
2. **Protokoll auswerten (Einheit 10.2):** Führen Sie `python3 log_auswerten.py <Protokoll>` aus und deuten Sie Zustellstatus, Fehlerursachen und Ablehnungen (`logs_sicherung.sh`).
3. **Sichern und wiederherstellen (Einheit 10.3):** Sichern Sie Postfächer und Konfiguration mit `tar`, stellen Sie in ein anderes Verzeichnis zurück und vergleichen Sie die Prüfsummen. Holen Sie eine einzelne gelöschte Nachricht zurück.
4. **Fehler suchen (Einheit 10.4):** Beschreiben Sie, wie Sie vorgehen, wenn Benutzer melden: (a) „Mails kommen nicht an“, (b) „Senden schlägt mit Anmeldefehler fehl“, (c) „Das Mailprogramm warnt vor dem Zertifikat“.

#### Kontrollfragen

1. Wozu dient die Queue-ID im Protokoll?
2. Warum gehört die Warteschlange nicht in die Sicherung der Postfächer?
3. Wie prüft man, dass eine Sicherung wiederherstellbar ist?
4. Welche Angaben gehören in die Dokumentation einer Mail-Störung?
