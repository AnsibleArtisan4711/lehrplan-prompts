# Änderungen

## 2026-11-13 (Status von P71 nachgetragen)

- `status` von P71 (DHCP-Grundlagen und -Betrieb) auf „gepusht“ gesetzt. Die Übungsreihe liegt seit 2026-11-12 in `netzwerkdienste-uebungen/dhcp-grundlagen-und-betrieb` (Commit bc423fc, 12 Module); der Status war beim Eintrag der Ordner am 2026-11-12 auf „Lehrplan erstellt“ geblieben und nicht nachgezogen worden. Damit haben alle 28 Lehrpläne in `lehrplaene/` den Status „gepusht“.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Übungsreihe P30: SQL-Grundlagen)

- `status` von P30 auf „gepusht“, Feld `ordner` ergänzt (Repository `datenbanken-uebungen`: `sql-grundlagen`, neues Repository).
- Die Übungsreihe (12 Module, 120 UE, 90 Stunden, davon 2 Module mit Priorität 2) ist ein Entwurf. **Nicht unter Hyper-V, nicht auf Debian 12 mit PostgreSQL 15 und nicht mit DBeaver erprobt.** Die SQL-Skripte und psql-Befehle wurden in einem Cloud-Container (Ubuntu 24.04.5, PostgreSQL 16.15, Cluster `main` mit `de_AT.UTF-8`, zwei Netzwerk-Namespaces für `db-server` 192.168.100.10 und `db-client` 192.168.100.20) ausgeführt; `psql` ersetzt DBeaver, `pg_ctlcluster` ersetzt `systemctl`. Nicht ausgeführt: `apt install`, `systemctl`, `/etc/network/interfaces`, Windows und DBeaver (siehe `befehle-nicht-bestaetigt.md`).
- Der Lehrplan P30 wurde nicht verändert; Befunde stehen in `lehrplan-korrekturen.md` der Übungsreihe (u. a. verbrauchen fehlgeschlagene `INSERT`-Befehle Identity-Werte; `UNIQUE` erlaubt mehrere `NULL`; `NOT IN` mit `NULL` liefert 0 Zeilen; Restore in die bestehende Datenbank `firma` ergibt 17 statt 18 Fehler; Logdatei heißt unter PostgreSQL 16 `postgresql-16-main.log`).
- Lerneinheiten ohne Praxisaufgabe im Lehrplan (1.1, 5.1, 9.1, 10.1, 11.1) wurden durch gekennzeichnete „Ergänzungen der Ausarbeitung“ abgedeckt. Material, das im Rohmaterial fehlte (Rechnung, Flat-File), ist erfunden und als solches gekennzeichnet.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Übungsreihe P16: Kryptografie, Zertifikate und TLS)

- `status` von P16 auf „gepusht“, Feld `ordner` ergänzt (Repository `it-sicherheit-uebungen`: `kryptografie-zertifikate-und-tls`).
- Die Übungsreihe (12 Module, 110 UE, 82,5 Stunden) ist ein Entwurf. **Nicht unter Hyper-V und nicht auf Windows erprobt.** Die OpenSSL-Befehle der Module 2 bis 7, 9 und 12, die TLS-Mitschnitte mit `tshark` (Modul 8) und die LUKS-Verwaltungsbefehle (Modul 10, an einem Loop-Gerät) wurden in einem Cloud-Container (Ubuntu 24.04.5, OpenSSL 3.0.13, curl 8.5.0, TShark 4.2.2, cryptsetup 2.7.0, zwei Netzwerk-Namespaces) ausgeführt; Windows 11 wurde durch einen Linux-Namespace mit `curl` ersetzt. Nicht ausgeführt: alle Windows-Teile (`certlm.msc`, `certutil`, `Import-Certificate`, Browser, `curl.exe`), BitLocker (Modul 11, Befehlssyntax von `manage-bde -lock`, `-unlock` und `-protectors` auf Microsoft Learn gelesen), `scp` zwischen den VMs und `luksOpen`/`mount` (kein Device-Mapper im Container). Die BSI TR-02102-1 wurde nicht inhaltlich gelesen.
- Der Lehrplan P16 wurde nicht verändert; Befunde stehen in `lehrplan-korrekturen.md` der Übungsreihe (u. a. zeigt das Server Hello bei TLS 1.3 `TLS 1.2` als `Version`, die echte Version steht in `supported_versions`; `openssl ciphers -v` akzeptiert TLS-1.3-Suitenamen nur über `-ciphersuites`; `openssl verify` meldet für ein Zertifikat ohne SAN `OK`; unter Ubuntu 24.04 entsteht für neue Konten `$y$` statt `$6$`). Die Ausgaben des Lehrplans zu den Modulen 2 bis 7, 9 und 12 ließen sich bestätigen.
- Lerneinheiten ohne Praxisaufgabe im Lehrplan (1.2, 1.3, 2.1, 2.2, 3.2, 3.3, 4.2, 6.3, 6.4, 10.1, 10.2, 11.1, 12.1) wurden durch gekennzeichnete „Ergänzungen der Ausarbeitung“ an vorhandenen Aufgaben abgedeckt.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Übungsreihe P12: IT-Sicherheitsgrundlagen)

- `status` von P12 auf „gepusht“, Feld `ordner` ergänzt (Repository `it-sicherheit-uebungen`, neu angelegt: `it-sicherheitsgrundlagen`).
- Die Übungsreihe (12 Module, 116 UE, 87 Stunden) ist ein Entwurf. **Nicht unter Hyper-V und nicht auf Windows erprobt.** Die Linux-Befehle der Module 3, 4, 5, 7, 10 und 12 und die Python-Hilfsskripte (Phishing-Prüfung, CVSS-3.1-Rechner mit Selbsttest, ALE-Rechner, Logzähler) wurden in Netzwerk-Namespaces eines Cloud-Containers (Ubuntu 24.04.5) ausgeführt; der Windows-Server in Modul 12 wurde mit nftables nachgebildet. Windows-Befehle wurden nicht ausgeführt; Parameter von `Get-FileHash`, `New-NetFirewallRule`, `icacls` und die Ereignis-IDs 4624/4625 wurden auf Microsoft Learn gelesen (13.11.2026). Die Formeln im CVSS-Rechner stammen aus dem Gedächtnis des Verfassers, nicht aus der Spezifikation.
- Material, das im Lehrplan fehlte (drei E-Mails, zehn Szenarien, Schwachstellenbericht mit erfundenen Kennungen `FIKTIV-2026-000N`, Krankenhaus-Szenario, Logauszug), wurde für die Übungen erfunden und ist gekennzeichnet.
- Der Lehrplan P12 wurde nicht verändert; Befunde stehen in `lehrplan-korrekturen.md` der Übungsreihe (u. a. zeigt `ls -lR` die Rechte des Wurzelordners nicht, sodass die Abweichung `chmod 777` im Audit unentdeckt bleibt; `PasswordAuthentication no` allein lässt `keyboard-interactive` zu; `icacls`-Schalter für die Vererbung in Microsoft Learn anders benannt).
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Übungsreihe P10: VPN mit WireGuard und OpenVPN)

- `status` von P10 auf „gepusht“, Feld `ordner` ergänzt (Repository `netzwerk-und-firewall-uebungen`: `vpn-mit-wireguard-und-openvpn`).
- Die Übungsreihe (12 Module, 110 UE, 82,5 Stunden) ist ein Entwurf. **Nicht auf Debian 12 und nicht unter Hyper-V erprobt.** Die Linux-Befehle der Module 2 bis 12 wurden in zwei Netzwerk-Namespaces eines Cloud-Containers nachgestellt (Ubuntu 24.04, wireguard-go statt Kernelmodul, OpenVPN 2.6.19, EasyRSA 3.1.7, nftables 1.0.9); die Ausgaben liegen als `beispiele/` in den Modulen. Nicht geprüft: Debian 12, Hyper-V, systemd-Dienste, SSH/`scp`, Kernelmodule `dummy` und WireGuard, `dynamic_debug`. Modul 1 ist eine reine Fallstudie.
- Der Lehrplan P10 wurde nicht verändert; Befunde stehen in `lehrplan-korrekturen.md` der Übungsreihe (u. a. `wg syncconf` ändert Routen nicht, erster Ping muss vom Client kommen, `bad source address` erst ab `verb 6`).
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Übungsreihe P05: Hyper-V Administration)

- `status` von P05 auf „gepusht“, Feld `ordner` ergänzt (Repository `virtualisierung-uebungen`: `hyper-v-administration`).
- Die Übungsreihe (12 Module, 110 UE, 82,5 Stunden) ist ein Entwurf. **Es wurde kein Windows-Befehl ausgeführt**; Cmdlets und Parameter wurden, soweit in den Quellen der Übungen vermerkt, auf Microsoft Learn gelesen. Sechs PowerShell-Hilfsskripte sind ungeprüft (nicht ausgeführt, nicht mit PowerShell syntaxgeprüft).
- Der Lehrplan P05 wurde nicht verändert; Anmerkungen stehen in `lehrplan-korrekturen.md` der Übungsreihe.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Lehrpläne und Übungsreihen P50, P51, P52: Zusatz)

- Neu: Lehrpläne `lehrplaene/P50-troubleshooting-methodik.md` (8 Module, 47 UE; Prio 1: 43 UE, Prio 2: 4 UE), `lehrplaene/P51-projektmanagement-fuer-administratoren.md` (8 Module, 46 UE; Prio 1: 41 UE, Prio 2: 5 UE) und `lehrplaene/P52-it-englisch-fuer-administratoren.md` (8 Module, 46 UE; Prio 1: 42 UE, Prio 2: 4 UE). Modul 8 hat jeweils Priorität 2.
- `status` von P50, P51 und P52 auf „gepusht“, Feld `ordner` ergänzt (Repository `it-betrieb-uebungen`: `troubleshooting-methodik`, `projektmanagement-fuer-administratoren`, `it-englisch-fuer-administratoren`).
- Die Übungsreihen (35,25, 34,5 und 34,5 Stunden) sind Entwürfe. Real gelaufen sind nur die Python-Hilfsskripte (Zeitleiste, Eingrenzen, Routenverfolgung, Protokollprüfung, kritischer Pfad, Dreipunktschätzung, Fehlermeldungen, Glossar). Bei P50 wurde das Labor nicht aufgebaut und kein Befehl wie `ping` oder `journalctl` ausgeführt; von `Get-WinEvent` und `Test-NetConnection` sind nur Schlüssel bzw. Parameter auf Microsoft Learn gelesen (13.11.2026). Scrum Guide, RFC 2119 und `journalctl`-Handbuchseite wurden nicht abgerufen (Zugriff gesperrt bzw. nur Suchtreffer); alle englischen Texte in P52 sind erfunden und nicht von einer Lehrkraft geprüft.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Gruppe Recht und Compliance komplett: P47, P48, P49)

- `status` von P47, P48 und P49 auf „gepusht“, Feld `ordner` ergänzt (Repository `it-betrieb-uebungen`: `datenschutz-dsgvo-in-der-it`, `nis2-fuer-administratoren`, `iso-27001-grundlagen`). Die Gruppe „Recht und Compliance“ ist damit komplett.
- Die Übungsreihen (9, 8 und 9 Module; 36,75, 34,5 und 36,75 Stunden) sind Entwürfe ohne technisches Labor. Real gelaufen sind nur die Python-Rechenhilfen (Fristen, Einstufung nach Kursregel, Risikomatrix, Risikoregister, Kennzahlen, Protokollprüfung). Der Wortlaut von DSGVO, NIS-2-Richtlinie und NISG 2026 sowie die Norm ISO/IEC 27001 wurden nicht gelesen; Rechtsaussagen sind Kursannahmen, kein Rechtsrat.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Lehrpläne P47, P48, P49: Recht und Compliance)

- Neu: Lehrpläne `lehrplaene/P47-datenschutz-dsgvo-in-der-it.md` (9 Module, 49 UE; Prio 1: 45 UE, Prio 2: 4 UE), `lehrplaene/P48-nis2-fuer-administratoren.md` (8 Module, 46 UE; Prio 1: 40 UE, Prio 2: 6 UE) und `lehrplaene/P49-iso-27001-grundlagen.md` (9 Module, 49 UE; Prio 1: 45 UE, Prio 2: 4 UE). Alle drei wurden direkt nach der Grundanweisung geschrieben und von Matija noch nicht geprüft.
- `status` von P47, P48 und P49 auf „Lehrplan erstellt“.
- Quellenstand (13.11.2026): P47 stützt sich bei den Meldepflichten auf eine WKO-Seite (Stand 23.10.2026); P48 auf Austrian Standards (NISG 2026, Inkrafttreten laut Quelle 01.10.2026, Seite ohne Datum, mit Widersprüchen bei Registrierungs- und Selbstdeklarationsfrist) sowie Wiedergaben von Art. 21 und 23 der NIS-2-Richtlinie; P49 auf die Produktseite von ISO/IEC 27001:2022 mit Amendment 1:2024. Gesetzestexte (EUR-Lex, RIS) und die Norm selbst wurden nicht gelesen; Rechtsaussagen sind Kursannahmen, kein Rechtsrat.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-13 (Gruppe IT-Betrieb und Prozesse komplett: P40, P41, P42, P43, P69, P70, P72)

- Neu: Lehrpläne `lehrplaene/P69-asset-verwaltung-und-cmdb.md` (8 Module, 45 UE; Prio 1: 39 UE, Prio 2: 6 UE) und `lehrplaene/P70-lizenzmanagement.md` (8 Module, 40 UE; Prio 1: 31 UE, Prio 2: 9 UE). Beide wurden direkt nach der Grundanweisung geschrieben und von Matija noch nicht geprüft. Quellen: GLPI-Dokumentation (Voraussetzungen, Inventory-Seite) und ein archivierter Microsoft-Blog zu Windows Server 2016, jeweils mit Abrufdatum 13.11.2026; Lizenzregeln für aktuelle Produkte und rechtliche Aussagen sind nicht geprüft.
- `status` von P40, P41, P42, P43, P69, P70 und P72 auf „gepusht“, Feld `ordner` ergänzt (Repository `it-betrieb-uebungen`: `itil-4-grundlagen`, `incident-problem-und-change-management`, `ticketsysteme-in-der-praxis`, `sla-und-betriebshandbuch`, `asset-verwaltung-und-cmdb`, `lizenzmanagement`; P72 hatte `ordner` bereits). Die Gruppe „IT-Betrieb und Prozesse“ ist damit komplett.
- Die Übungsreihen sind Entwürfe. In GLPI, Zammad, Ubuntu, Hyper-V und Windows wurde nichts ausgeführt; real gelaufen sind nur die Python-Rechenhilfen.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-12 (Gruppe Client und Hardware komplett: P44, P45, P46)

- `status` von P44, P45 und P46 auf „gepusht“, Feld `ordner` ergänzt (`pc-hardware-und-fehlersuche`, `windows-11-client-administration`, `betriebssystem-rollout` im Repository `client-hardware-uebungen`). Die Gruppe „Client und Hardware“ ist damit komplett. Commits im Repository `client-hardware-uebungen`: 639f82b (P45), 8a341ee (P46), ad7df40 (P44).
- Die Übungsreihen sind Entwürfe und wurden nicht auf Windows oder Hyper-V ausgeführt.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-12 (Gruppe Windows-Server-Rollen komplett: P03, P04, P59, P61)

- Neu: Lehrplan `lehrplaene/P59-remotedesktopdienste-rds.md` (13 Module, 104 UE; Prio 1: 90 UE, Prio 2: 14 UE) und Lehrplan `lehrplaene/P61-windows-admin-center.md` (9 Module, 52 UE; Prio 1: 42 UE, Prio 2: 10 UE). Beide wurden direkt nach der Grundanweisung geschrieben und von Matija noch nicht geprüft. Microsoft-Learn-Angaben stammen aus Suchtreffer-Auszügen vom 12.11.2026.
- `status` von P03, P04, P59 und P61 auf „gepusht“, Feld `ordner` ergänzt (`wsus-und-update-verwaltung`, `zertifikatsdienste-und-pki`, `remotedesktopdienste-rds`, `windows-admin-center` im Repository `windows-server-uebungen`). Die Gruppe „Windows-Server-Rollen“ (P01 bis P04, P59, P61) ist damit komplett. Die Übungsreihen sind Entwürfe und nicht auf Windows ausgeführt.
- Hinweis: Die Übungsreihen P59 und P61 und die beiden Lehrpläne liegen im selben Commit wie diese Änderung.
- README-Tabellen mit `python tools/build_prompts.py` erzeugt.

## 2026-11-12 (Links auf die Kursordner für P71, P72 und P45)

- Fehlerbehebung: In der README-Tabelle waren P71 und P72 in der Spalte „Repository“ nur als `geplant` ohne Link eingetragen, obwohl die Übungsreihen in `netzwerkdienste-uebungen/dhcp-grundlagen-und-betrieb` und `it-betrieb-uebungen/weiterbildung-it-systemtechnik` liegen.
- `daten/kurse.json`: Feld `ordner` bei P71, P72 und P45 (`client-hardware-uebungen/windows-11-client-administration`) ergänzt. Der Status bleibt „Lehrplan erstellt“, weil die Gruppen noch nicht vollständig sind.
- `tools/build_prompts.py`: Die Spalte „Repository“ und die Tabelle der Themen-Repositories verlinken jetzt, sobald `ordner` gesetzt ist (bisher nur bei Status „gepusht“). Die Legende im README wurde angepasst.
- README mit `python tools/build_prompts.py` neu erzeugt; alle anderen Zeilen sind unverändert.

## 2026-11-12 (Kurs P72 Weiterbildung IT-Systemtechnik)

- Neu: Kurs P72 „Weiterbildung IT-Systemtechnik (Querschnitt nach der Lehre)“ in `daten/kurse.json` (Priorität A, Gruppe IT-Betrieb und Prozesse, Repository `it-betrieb-uebungen`, Status Lehrplan erstellt) mit Prompt `prompts/P72-weiterbildung-it-systemtechnik.md` und Lehrplan `lehrplaene/P72-weiterbildung-it-systemtechnik.md` (12 Module, 110 UE; 10 Module Priorität 1 mit 93 UE, 2 Module Priorität 2 mit 17 UE).
- Kennzeichnung der Herkunft: Der Lehrplan wurde aus der Excel-Vorlage „Lehrplan - Weiterbildung IT Systemtechnik“ umgewandelt. Modultitel, Einheiten und Prioritäten stammen aus der Vorlage; Lernziele, Praxisaufgaben und Kontrollfragen sind neu geschrieben, weil die Vorlage dort nur gleichlautende Platzhaltertexte enthält. Abweichungen: Modul 5 (Linux-Server) wurde von Priorität 2 auf 1 angehoben; die Einheiten (UE) werden als 45-Minuten-Einheiten gelesen. Der Prompt wurde nachträglich der Vollständigkeit halber erzeugt.
- Hinweis: P72 ist ein Querschnittskurs mit Einstieg in jedes Gebiet. Überschneidungen mit den Spezialkursen (zum Beispiel DNS, DHCP, Backup, Monitoring, Windows-Client) wurden nicht im Einzelnen analysiert.
- Offen: Befehlsparameter und Pfade sind an den betroffenen Stellen als „nicht bestätigt“ gekennzeichnet; Microsoft-Learn-Angaben stammen aus Suchtreffer-Auszügen vom 12.11.2026. Nichts davon wurde im Labor ausgeführt.
- README-Tabelle und Zähler (72 Kurse) wurden mit `python tools/build_prompts.py` erzeugt. Die übrigen Kurse P01 bis P71 sind unverändert.

## 2026-11-12 (Kurs P71 DHCP)

- Neu: Kurs P71 „DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea)“ in `daten/kurse.json` (Priorität A, Gruppe Netzwerkdienste und Firewall, Repository `netzwerkdienste-uebungen`, Status Lehrplan erstellt) mit Prompt `prompts/P71-dhcp-grundlagen-und-betrieb.md` und Lehrplan `lehrplaene/P71-dhcp-grundlagen-und-betrieb.md` (12 Module, 116 UE; 10 Module Priorität 1 mit 96 UE, 2 Module Priorität 2 mit 20 UE).
- Kennzeichnung der Herkunft: Der Lehrplan ist **nicht** aus dem Prompt über die Gem entstanden, sondern direkt von Claude nach dem Aufbau der Grundanweisung geschrieben. Der Prompt wurde nachträglich der Vollständigkeit halber erzeugt. Die DHCP-Lücke ergab sich aus der Auswertung der Excel-Lehrpläne (2026-11-12): Ein eigener DHCP-Lehrplan lag nicht vor.
- Offen: Der Lehrplan ist von mir noch nicht geprüft. Die RFC-Adressen wurden nicht abgerufen (als „nicht geprüft“ markiert); Befehlsparameter, Paketnamen und Pfade sind an den betroffenen Stellen als „nicht bestätigt“ gekennzeichnet; die aktuell unterstützte Kea-Version ist vor dem Einsatz zu prüfen. Nichts davon wurde im Labor ausgeführt.
- README-Tabelle und Zähler (71 Kurse) wurden mit `python tools/build_prompts.py` erzeugt. Die übrigen Kurse P01 bis P70 sind unverändert.

## 2026-11-11 (Themen-Repositories für die Kurse)

- Neu: Felder `repo` (Themen-Repository, bei allen 70 Kursen) und `ordner` (Kursordner, nur bei gepushten Kursen) in `daten/kurse.json`. Die Zuordnung folgt dem Plan mit 14 Themen-Repositories; offen sind P47 bis P49 (vorläufig `it-betrieb-uebungen`) und die Trennung von Firewall und VPN.
- `status` von P01 (`netzwerkdienste-uebungen/dns-grundlagen`) und P02 (`windows-server-uebungen/dateidienste-dfs-druckserver`) auf „gepusht“. Beide sind ausgearbeitet und liegen auf GitHub; Windows-Befehle sind nicht im Labor ausgeführt (siehe Prüfvermerke in den Repositories).
- `tools/build_prompts.py`: neue Spalte „Repository“ in der Kurstabelle (gepusht = Link auf den Kursordner, sonst das geplante Repository), neue Tabelle „Zuordnung zu den Themen-Repositories“ (Markierungen `REPOS-START`/`REPOS-ENDE`), Prüfung, dass `repo` gesetzt ist und bei „gepusht“ auch `ordner`.
- README: Der von Hand gepflegte Abschnitt „Einordnung in die Profil-README“ (Gruppen 9 bis 13) ist ersetzt durch den erzeugten Abschnitt „Zuordnung zu den Themen-Repositories“. Die Gruppen 9 bis 13 sind damit hinfällig.
- `daten/rahmen.json`: Legende des Status „gepusht“ angepasst. `tools/umsetzung_anlegen.py`: Docstring P01-P52 auf P01-P70.

## 2026-11-09 (Kurse P53–P70, Einordnung in die Profil-README)

- Neu: 18 Kurse in `daten/kurse.json` (P53 bis P70) mit Prompts in `prompts/`: Container (P53), Storage unter Linux (P54, P55), Cloud-Plattformen und Azure (P56 bis P58), Windows-Server und Virtualisierung (P59 bis P61), IT-Sicherheit (P62 bis P64), Automatisierung und Logging (P65, P66), Datenbanken (P67, P68), IT-Betrieb (P69, P70). Status aller neuen Kurse: offen. Die Kurse sind ein Vorschlag des Autors zusammen mit Claude, die Inhalte der Prompts sind nicht aus einer Quelle belegt.
- Neu: Abschnitt „Einordnung in die Profil-README“ in der README (von Hand gepflegt): Zuordnung der Kurse zu den Gruppen 2, 5, 7 und den neuen Gruppen 9 bis 13.
- Die Kurse P01 bis P52 sind unverändert.

## 2026-11-09 (Übungsreihen E01–E06)

- Neu: `daten/uebungen.json` mit den sechs eigenen Übungsreihen E01–E06, in der Reihenfolge der Fächerübersicht: E01 `multi-site-hybrid-cloud-ai-sec-lab`, E02 `netzwerk-uebungen-packet-tracer`, E03 `ad-uebungen-benutzerverwaltung`, E04 `wlan-gaeste-netz-uebung`, E05 `veeam-backup-uebung`, E06 `usv-shutdown-uebung`. Handgepflegt sind Titel, Thema, Repository und der lokale Ordner; der Aufbau (Module, Einheiten, Teile, Schritte, Lernziele, Kontrollfragen, Skripte, Stellen mit „nicht bestätigt“ oder „sinngemäß“) wird aus den Dateien der Repositories gelesen.
- Neu: `tools/uebungen_einlesen.py` liest diesen Aufbau aus den lokalen Repository-Ordnern (Feld `lokal`, überschreibbar mit `--pfad E03=Ordner`) und schreibt ihn in `daten/uebungen.json`. Nach neuen Übungen in einem der Repositories: einlesen, dann `build_prompts.py`.
- Neu: Ordner `uebungen/` mit einer Seite je Reihe (erzeugt) und die dritte Tabelle „Die 6 Übungsreihen“ in der README.
- `tools/umsetzung_anlegen.py`: akzeptiert `E01`–`E06`. Die Modulordner heißen wie im Repository. Bei E02–E06 enthält die Checkliste Voraussetzungen, Teile mit Schritten, Skripte, Prüfbefehle, Lernziele, Kontrollfragen und Erweiterungen; das Protokoll hat einen Block je Teil; `befehle-nicht-bestaetigt.md` listet die Stellen mit „nicht bestätigt“ oder „sinngemäß“. Bei E01 (Steps statt Übungen) gibt es je Step einen Protokollblock mit dem Feld „Tatsächlich umgesetzt: ja / teilweise / nur dokumentiert“, damit im Lebenslauf nur Realisiertes als umgesetzt erscheint.
- Stand der Quellen beim Einlesen (2026-11-09): E01 14 Module mit 92 Einheiten (13 Module mit je 7 Steps und der Anhang); E02 nur Modul 1 mit Übung 01.1, die Module 2 bis 8 sind in den Modul-READMEs als geplant geführt; E03, E05, E06 je eine Übung, E04 zwei Übungen. Die Übungen E03–E06 stehen in ihren READMEs als „Entwurf“, ihre Befehle sind teils „nicht bestätigt“.

## 2026-11-09 (Fächer K01–K16)

- Neu: `daten/faecher.json` mit den 16 Fächern K01–K16 (Linux Essentials bis Unternehmensgründung) aus der Fächerübersicht (Excel) des Autors: Typ (Kern/Erweiterung), Bereich, Voraussetzung, Gesamtstunden, Module mit ca. Stunden und Feld `repository` (`repo`). Die Nummerierung folgt der Reihenfolge in der Excel-Datei. Die 16 Repository-Namen stammen aus der Fächerübersicht (alle auf GitHub gepusht) und sind als Links in der README-Tabelle und auf den Fach-Seiten eingetragen; `ad-uebungen-benutzerverwaltung` ist eine eigene Übungsreihe und nicht das Repository von K06.
- Neu: Ordner `faecher/` mit einer Modulübersicht je Fach (erzeugt). Die README zeigt eine zweite Tabelle „Die 16 Fächer“ (Zähler, Module, Stunden, Voraussetzung, Repository).
- `tools/build_prompts.py`: erzeugt `faecher/` und die zweite Tabelle (Markierungen `FAECHER-START`/`FAECHER-ENDE`); bricht ab bei doppelten IDs oder Modulnummern mit Lücken.
- `tools/umsetzung_anlegen.py`: akzeptiert jetzt auch `K01`–`K16`. Da für diese Fächer nur Modultitel und Stunden vorliegen, sind Checklisten und Protokolle schlanker (Skriptkapitel, Übungen, Lernziele, Kontrollfragen als Abhakpunkte ohne Einzelaufgaben); `befehle-nicht-bestaetigt.md` entfällt.
- Kennzeichnung der Änderung am Rohmaterial: In der Excel-Datei stehen die Modultitel ohne Umlaute („Pruefung“, „Qualitaet“). Sie wurden über eine feste Wortliste ergänzt (24 Wörter, z. B. Prüfung, Qualität, Gründung, Geräte, für, Verträge); „Vertrage“ in K16 Modul 11 wurde als „Verträge“ gelesen. Fachnamen und Stunden sind unverändert. Die Modulstunden sind in der Quelle gleichmäßig verteilt und gerundet; ihre Summe weicht bei einigen Fächern um unter eine Stunde von der Gesamtdauer ab (K02: 294 statt 294,5).
- Die Fächer K01–K16 haben keinen Status wie die Kurse P01–P52; ihr Fortschritt steht weiter im Excel-Stundenplan.

## 2026-11-08 (Bilder-Index)

- Neu: `tools/bilder_index.py`. Es liest alle Markdown-Dateien eines Ordners (Standard: `Umsetzung` neben dem Repository) und schreibt `bilder-index.md` mit allen verlinkten Bildern (Ordner, Datei, Abschnitt, Beschreibung, Größe, Link). Es meldet Bilder ohne Verlinkung, Links auf fehlende Bilder und Bilder über 1 MB. Bilder werden nicht verändert.

## 2026-11-08 (Umsetzungsordner)

- Neu: `tools/umsetzung_anlegen.py`. Es liest einen Lehrplan aus `lehrplaene/` und legt je Modul einen Ordner mit Checkliste (Voraussetzungen, Lerneinheiten, Praxisaufgaben, Lernziele, Kontrollfragen, Prüfpunkte), Protokollvorlage je Praxisaufgabe, Fehlerprotokoll und den Ablageordnern `screenshots/`, `notizen/`, `ausgaben/` an. Dazu eine Übersicht mit Fortschrittstabelle, `befehle-nicht-bestaetigt.md` (Stellen mit „nicht bestätigt“ in den Praxisaufgaben) und `99-abschluss/` mit Checkliste und Sammlung der Lehrplan-Korrekturen. Das Skript überschreibt nichts.
- Die Umsetzungsordner liegen bewusst außerhalb des Repositories (Standard: Ordner neben dem Repository), weil dort Screenshots und Notizen entstehen. Fertiges Material kommt später in ein eigenes Repository je Fach.

## 2026-11-08 (erste Lehrpläne im Repository)

- Neu: Ordner `lehrplaene/` mit den 16 geprüften Lehrplänen (P01–P05, P10, P12, P16, P30, P40–P46), unverändert aus der jeweiligen „Finalen Version“ übernommen, einschließlich Prüfvermerk und offener Punkte. Dateiname wie die Prompt-Datei (`PNN-<slug>.md`).
- Status von P41, P42, P43, P45 und P46 auf „Lehrplan erstellt“ gesetzt; damit stehen 16 von 52 Kursen auf „Lehrplan erstellt“.
- `tools/build_prompts.py`: Neue Spalte „Lehrplan“ in der Tabelle (Link, wenn die Datei in `lehrplaene/` liegt); das Skript bricht ab, wenn ein Kurs auf „Lehrplan erstellt“ steht, aber die Datei fehlt.
- `daten/rahmen.json`: Legende der Statuswerte angepasst. Ausarbeitungen zu Übungen kommen in eigene Repositories („aufbereitet“, „gepusht“).
- Lizenz: Die Lehrpläne stehen wie die Prompts unter CC BY 4.0 (`LICENSE-DOCS.md`, README). Die Frage zur Schutzfähigkeit der KI-erzeugten Tabellen „Lerneinheiten laut Lehrplan“ ist damit nicht rechtlich geklärt, nur die Lizenz des Repositories festgelegt.
- Hinweis: Befehle in den Lehrplänen, die als „nicht bestätigt“ markiert sind, wurden nicht ausgeführt. Das steht in den Prüfvermerken.

## 2026-11-08 (Status in der README erklärt)

- `tools/build_prompts.py` und `daten/rahmen.json`: Vor der Tabelle in der README stehen jetzt ein Zähler (Kurse je Status) und eine Legende zu den vier Statuswerten. Neu in `rahmen.json`: `status_legende`, das Skript bricht ab, wenn ein Statuswert keine Legende hat. Anlass: Aus der Tabelle ging nicht hervor, was „Lehrplan erstellt“ bedeutet und dass die fertigen Lehrpläne nicht im Repository liegen.

## 2026-11-08 (nach der Prüfung von P40 und P44)

- Prüfvermerk der Grundanweisung: Zu jedem der neun Punkte sind die gefundenen und korrigierten Fehler (Modul und Art) zu nennen, oder „keine gefunden“ mit einer konkreten Stichprobe. Ein Punkt ohne beides gilt als nicht geprüft. Anlass: Auch mit Denkaufwand „Hoch“ bewertete die Gem P16, P40 und P44 mit „erfüllt“, obwohl unter anderem Quellen fehlten, Lernziele keine Aufgabe hatten und die Windows-Installation im Labor nirgends geplant war.
- `tools/build_prompts.py`: Das Thema „Troubleshooting und Diagnosewerkzeuge“ wird nur noch bei Kursen mit technischem Labor an die Kernthemen angehängt. Betroffen und neu erzeugt: P40, P41, P43, P47, P48, P49, P51, P52 (Kurse mit „kein technisches Labor nötig“).
- ITIL bleibt bei Version 4 (P40).

## 2026-11-08 (nach den Prüfungen von P02, P03, P04 und P16)

- Selbstprüfung der Grundanweisung von sieben auf neun Punkte erweitert und als nummerierte Liste gesetzt. Der Prüfvermerk verlangt zu jedem Punkt die konkret geprüften Module; Fehler sind vor der Ausgabe zu korrigieren und nicht nur im Prüfvermerk zu nennen.
- Neu: Punkt 2 (jede genutzte Rolle, Software oder jedes Feature hat eine Installationsaufgabe); Punkt 3 (auch Algorithmen, Protokolle und Dateiformate stehen in den Quellen); Punkt 4 (Auswahlen aus frühen Modulen decken spätere Verwendungen ab, Voraussetzungen stehen vor der Aufgabe, die sie braucht); Punkt 5 (Lerneinheiten mit Praxistitel haben eine Aufgabe, Zahlen in Kontrollfragen passen zu den Einheiten); Punkt 6 (Pflichtmodule nennen kein optionales Modul als Voraussetzung); Punkt 8 (Internetphasen, Namen und Adressen im Labor-Setup, Übertragungsweg für Dateien); Punkt 9 (Befehle liefern das Ziel der Aufgabe, zerstörende Befehle stehen nach Zielprüfung und Prüfpunkt). Regel 1 verlangt, erwartete Ausgaben und Fehlercodes nur zu nennen, wenn sie sicher sind.
- Anlass: P02 bis P04 und P16 hatten alle Punkte mit „erfüllt“ bewertet. Gefunden wurden unter anderem ein Pflichtmodul, das von einem optionalen abhing, Software und Inhalte ohne Internet, undefinierte Hostnamen in URLs, ein Webserver, der erst nach seiner Verwendung entstand, eine Auswahl in Modul 3, die spätere Verwendungen nicht abdeckte, ein Zertifikat ohne SAN trotz SAN im CSR, ein falscher Fehlercode, Lerneinheiten ohne Aufgabe und eine Kontrollfrage mit drei statt vier Schutzzielen. P16 wurde mit Denkaufwand „Hoch“ erzeugt; das Fehlermuster blieb ähnlich.

## 2026-11-08 (nach dem Test mit P12)

- Selbstprüfung der Grundanweisung geschärft: Punkt 3 nennt auch Standards, Gesetze und Verordnungen (DSGVO, CVSS, CIS Benchmarks); Punkt 4 verlangt, dass erwartete Ergebnisse zu früheren Modulen passen und Zugangssperren vorher einen Ersatzzugang testen; Punkt 5 unterscheidet Praxisaufgabe (anwenden, konfigurieren) und Kontrollfrage (kennen, verstehen), verlangt Abdeckung jedes genannten Begriffs und verbietet, ein Pflichtlernziel nur in einem optionalen Modul zu prüfen; Punkt 7 nennt Software, die ohne Internet im isolierten Labor installiert werden muss. Anlass: Der Lehrplan P12 (IT-Sicherheit) hatte alle sieben Punkte mit „erfüllt“ bewertet, obwohl mehrere Lernziele ungeprüft waren (VPN, Patch-Management, Risikobewertung), DSGVO und CVSS in den Quellen fehlten, ein Webserver und die Software ohne Internet nie installiert wurden, SSH-Passwort-Login vor dem Schlüsseltest abgeschaltet wurde und der Nmap-Nachweis den Firewall-Regeln widersprach.

## 2026-11-08 (nach dem Test mit P05)

- Selbstprüfung der Grundanweisung: Punkt 6 um die Regel ergänzt, dass der Rückbau von Änderungen nie von einem optionalen Modul abhängt; neuer Punkt 7 (Voraussetzungen wie Domäne, Zertifikate, gemeinsamer Speicher oder zusätzliche Hosts müssen im Labor-Setup aufgebaut oder ausgeschlossen sein). Anlass: Der Hyper-V-Lehrplan (P05) nannte eine Domäne `lab.internal`, baute sie aber nie auf, verlangte aber eine Live-Migration, die ohne Domäne nicht möglich ist, und legte den Rückbau der Nested-Umgebung in ein optionales Modul. Der Prüfvermerk hatte dennoch alle Punkte mit „erfüllt“ bewertet.

## 2026-11-08 (nach dem Test mit P01)

- Selbstprüfung der Grundanweisung um Punkt 6 erweitert (einschränkende Einstellungen in späteren Modulen, angekündigte Szenarien vollständig, Lernziele im Labor machbar) und die Bewertung „teilweise erfüllt“ eingeführt. Anlass: Der zweite Test (P01) hatte alle Punkte mit „erfüllt“ bewertet, obwohl Modul 9 an früheren Lauschadressen und ACLs scheiterte und ein TSIG-Lernziel im Lab nicht machbar war.

## 2026-11-08 (Umbau auf Variablen-Form)

- Gem-Grundanweisung überarbeitet und als `gem/grundanweisung.md` ins Repository aufgenommen. Neu: Dokumentstruktur mit festen Überschriftsebenen, Zeile „Gesamt“ in der Master-Tabelle, Quellenregeln (Format, Verifikation, jede Norm und jeder RFC in der Liste), Labor-Setup mit „erforderlich“ und „optional“, Ausnahme für Cloud-Kurse (Test-Tenant) und für Kurse ohne technisches Labor, Hinweis, dass Scans nur gegen eigene Lab-VMs laufen, UE = 45 Minuten, Dateiname `lehrplan_<kursname>.md`, Selbstprüfung mit Prüfvermerk im Chat.
- Neue Vorlage `gem/vorlage-variablen.md`.
- Alle 52 Prompts auf die Variablen-Form umgebaut (Fokus-Technologien, Vorkenntnisse, Umfang, Kernthemen, Abgrenzung, Labor-Ressourcen, Zusätzliche Hinweise). Neue Felder `fokus` und `labor` in `daten/kurse.json`, das Feld `praxis` entfällt, `zielgruppe` steht nur noch in der Grundanweisung.

## 2026-11-08 (später am Tag)

- Repository öffentlich gestellt und im Profil verlinkt. `LICENSE` (MIT, Skript) und `LICENSE-DOCS.md` (CC BY 4.0, Texte) ergänzt, README um Abschnitte „Entstehung“ und „Lizenz“ erweitert.

## 2026-11-08

- Erste Fassung: 52 Prompts in 16 Themengebieten (Priorität A, B, C), erzeugt aus `daten/kurse.json`.
- Gemeinsamer Rahmen: Zielgruppe Auszubildende, Quereinsteiger und angehende Systemadministratoren/Systemtechniker (Österreich/EU); große Kurse etwa 12 Module und 100 bis 120 Stunden, kleine Kurse (Recht, IT-Betrieb, Zusatz, PC-Hardware) etwa 8 Module und 40 bis 60 Stunden.
- Gemeinsame Regeln in allen Prompts: keine erfundenen Fakten, Versionen oder Befehle; Unsicheres als „nicht bestätigt“; keine geschützten Texte oder Prüfungsfragen; eigene Szenarien mit `example.com`; Übungen nur in isolierten Umgebungen; Ausgabeformat gemäß Grundanweisung der Gem.
