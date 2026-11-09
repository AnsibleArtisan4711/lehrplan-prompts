# Lehrplan-Prompts

Fertige Prompts für den Lehrplan-Architekten (benutzerdefinierte Gem), ein Prompt pro Kurs. Sie decken die Themen ab, die zu den vorhandenen Lehrplänen für Systemadministration und Systemtechnik noch fehlen. Öffentlich einsehbar, damit die Arbeitsweise nachvollziehbar ist.

## So benutzt du die Prompts

1. Einmalig: den Text aus `gem/grundanweisung.md` (Abschnitt „Anweisung“) in das Feld „Anweisungen“ der Gem einfügen. Dort stehen die festen Regeln, der Aufbau des Lehrplans und die Selbstprüfung.
2. In der Tabelle den Kurs suchen und die Datei unter `prompts/` öffnen.
3. Den Text im Codeblock kopieren und in die Gem einfügen.
4. Wenn der Lehrplan fertig und geprüft ist, die Datei als `lehrplaene/PNN-<slug>.md` ablegen (Name wie die Prompt-Datei), in `daten/kurse.json` den Status des Kurses ändern (`offen`, `Lehrplan erstellt`, `aufbereitet`, `gepusht`) und das Skript laufen lassen (siehe Pflege).

Jeder Prompt füllt nur die Variablen des Kurses aus: Fokus-Technologien, Vorkenntnisse, Umfang, Kernthemen, Abgrenzung, Labor-Ressourcen und bei Bedarf Zusätzliche Hinweise. Alles andere (Zielgruppe, Priorisierung, Aufbau, Quellenregeln, Ausgabeformat) steht in der Grundanweisung. Die leere Vorlage für eigene Kurse liegt in `gem/vorlage-variablen.md`.

## Kurse

Priorität A: zuerst, größte Lücke. Priorität B: wichtig. Priorität C: Vertiefung, optional. Die Tabelle wird vom Skript erzeugt; nicht von Hand ändern.

<!-- TABELLE-START -->
Stand der 52 Kurse: 36 offen, 16 Lehrplan erstellt, 0 aufbereitet, 0 gepusht.

Bedeutung der Status:

- **offen**: Der Prompt liegt vor, ein Lehrplan ist noch nicht erstellt.
- **Lehrplan erstellt**: Der Lehrplan ist erstellt und von mir geprüft. Er liegt in `lehrplaene/` und ist in der Spalte „Lehrplan“ verlinkt.
- **aufbereitet**: Aus dem Lehrplan ist Übungsmaterial ausgearbeitet, aber noch nicht veröffentlicht.
- **gepusht**: Das Übungsmaterial liegt in einem eigenen GitHub-Repository, das in der Spalte „Lehrplan“ verlinkt wird.

| Nr | Prio | Themengebiet | Kurs | Status | Prompt | Lehrplan |
|---|---|---|---|---|---|---|
| 1 | A | Windows-Server-Rollen | DNS-Grundlagen (Windows-DNS und BIND) | Lehrplan erstellt | [P01](prompts/P01-dns-grundlagen-windows-dns-und-bind.md) | [P01](lehrplaene/P01-dns-grundlagen-windows-dns-und-bind.md) |
| 2 | A | Windows-Server-Rollen | Dateidienste, DFS und Druckserver | Lehrplan erstellt | [P02](prompts/P02-dateidienste-dfs-und-druckserver.md) | [P02](lehrplaene/P02-dateidienste-dfs-und-druckserver.md) |
| 3 | A | Windows-Server-Rollen | WSUS und Update-Verwaltung | Lehrplan erstellt | [P03](prompts/P03-wsus-und-update-verwaltung.md) | [P03](lehrplaene/P03-wsus-und-update-verwaltung.md) |
| 4 | A | Windows-Server-Rollen | Zertifikatsdienste und PKI (AD CS) | Lehrplan erstellt | [P04](prompts/P04-zertifikatsdienste-und-pki-ad-cs.md) | [P04](lehrplaene/P04-zertifikatsdienste-und-pki-ad-cs.md) |
| 5 | A | Virtualisierung | Hyper-V Administration | Lehrplan erstellt | [P05](prompts/P05-hyper-v-administration.md) | [P05](lehrplaene/P05-hyper-v-administration.md) |
| 6 | A | Virtualisierung | Proxmox VE | offen | [P06](prompts/P06-proxmox-ve.md) | – |
| 7 | A | Virtualisierung | VMware vSphere und ESXi | offen | [P07](prompts/P07-vmware-vsphere-und-esxi.md) | – |
| 8 | A | Netzwerkdienste und Firewall | Firewall mit OPNsense | offen | [P08](prompts/P08-firewall-mit-opnsense.md) | – |
| 9 | A | Netzwerkdienste und Firewall | Linux-Firewall mit nftables und iptables | offen | [P09](prompts/P09-linux-firewall-mit-nftables-und-iptables.md) | – |
| 10 | A | Netzwerkdienste und Firewall | VPN mit WireGuard und OpenVPN | Lehrplan erstellt | [P10](prompts/P10-vpn-mit-wireguard-und-openvpn.md) | [P10](lehrplaene/P10-vpn-mit-wireguard-und-openvpn.md) |
| 11 | A | Netzwerkdienste und Firewall | Reverse Proxy, Lastverteilung und TLS | offen | [P11](prompts/P11-reverse-proxy-lastverteilung-und-tls.md) | – |
| 12 | A | IT-Sicherheit | IT-Sicherheitsgrundlagen | Lehrplan erstellt | [P12](prompts/P12-it-sicherheitsgrundlagen.md) | [P12](lehrplaene/P12-it-sicherheitsgrundlagen.md) |
| 13 | A | IT-Sicherheit | Windows-Server-Härtung | offen | [P13](prompts/P13-windows-server-haertung.md) | – |
| 14 | A | IT-Sicherheit | Linux-Server-Härtung | offen | [P14](prompts/P14-linux-server-haertung.md) | – |
| 15 | A | IT-Sicherheit | Schwachstellenmanagement | offen | [P15](prompts/P15-schwachstellenmanagement.md) | – |
| 16 | A | IT-Sicherheit | Kryptografie, Zertifikate und TLS | Lehrplan erstellt | [P16](prompts/P16-kryptografie-zertifikate-und-tls.md) | [P16](lehrplaene/P16-kryptografie-zertifikate-und-tls.md) |
| 17 | A | Monitoring und Logging | Monitoring mit Zabbix | offen | [P17](prompts/P17-monitoring-mit-zabbix.md) | – |
| 18 | A | Monitoring und Logging | Monitoring mit Prometheus und Grafana | offen | [P18](prompts/P18-monitoring-mit-prometheus-und-grafana.md) | – |
| 19 | A | Monitoring und Logging | Zentrales Logging mit Graylog und Elastic Stack | offen | [P19](prompts/P19-zentrales-logging-mit-graylog-und-elastic-stack.md) | – |
| 20 | A | Monitoring und Logging | Monitoring mit PRTG | offen | [P20](prompts/P20-monitoring-mit-prtg.md) | – |
| 21 | B | Automatisierung | Konfigurationsmanagement mit Ansible | offen | [P21](prompts/P21-konfigurationsmanagement-mit-ansible.md) | – |
| 22 | B | Automatisierung | Infrastructure as Code mit Terraform | offen | [P22](prompts/P22-infrastructure-as-code-mit-terraform.md) | – |
| 23 | B | Automatisierung | cloud-init und VM-Vorlagen | offen | [P23](prompts/P23-cloud-init-und-vm-vorlagen.md) | – |
| 24 | B | Automatisierung | PowerShell Desired State Configuration (DSC) | offen | [P24](prompts/P24-powershell-desired-state-configuration-dsc.md) | – |
| 25 | B | Container | Docker und Docker Compose | offen | [P25](prompts/P25-docker-und-docker-compose.md) | – |
| 26 | B | Container | Kubernetes-Grundlagen | offen | [P26](prompts/P26-kubernetes-grundlagen.md) | – |
| 27 | B | Azure und Identität | Azure Administration | offen | [P27](prompts/P27-azure-administration.md) | – |
| 28 | B | Azure und Identität | Entra ID und Hybrid-Identität | offen | [P28](prompts/P28-entra-id-und-hybrid-identitaet.md) | – |
| 29 | B | Azure und Identität | Intune und Autopilot | offen | [P29](prompts/P29-intune-und-autopilot.md) | – |
| 30 | B | Datenbanken | SQL-Grundlagen | Lehrplan erstellt | [P30](prompts/P30-sql-grundlagen.md) | [P30](lehrplaene/P30-sql-grundlagen.md) |
| 31 | B | Datenbanken | MariaDB und PostgreSQL Administration | offen | [P31](prompts/P31-mariadb-und-postgresql-administration.md) | – |
| 32 | B | Datenbanken | SQL Server Administration | offen | [P32](prompts/P32-sql-server-administration.md) | – |
| 33 | B | Storage | NAS, SAN, iSCSI und RAID | offen | [P33](prompts/P33-nas-san-iscsi-und-raid.md) | – |
| 34 | B | Storage | Btrfs, ZFS und Snapshots | offen | [P34](prompts/P34-btrfs-zfs-und-snapshots.md) | – |
| 35 | B | Backup und Notfall | Backup-Konzept (3-2-1, RPO und RTO) | offen | [P35](prompts/P35-backup-konzept-3-2-1-rpo-und-rto.md) | – |
| 36 | B | Backup und Notfall | Notfallplanung und Disaster Recovery | offen | [P36](prompts/P36-notfallplanung-und-disaster-recovery.md) | – |
| 37 | B | E-Mail | Exchange Online Administration | offen | [P37](prompts/P37-exchange-online-administration.md) | – |
| 38 | B | E-Mail | E-Mail-Authentifizierung: SPF, DKIM und DMARC | offen | [P38](prompts/P38-e-mail-authentifizierung-spf-dkim-und-dmarc.md) | – |
| 39 | B | E-Mail | Mailserver mit Postfix und Dovecot | offen | [P39](prompts/P39-mailserver-mit-postfix-und-dovecot.md) | – |
| 40 | C | IT-Betrieb und Prozesse | ITIL 4 Grundlagen | Lehrplan erstellt | [P40](prompts/P40-itil-4-grundlagen.md) | [P40](lehrplaene/P40-itil-4-grundlagen.md) |
| 41 | C | IT-Betrieb und Prozesse | Incident-, Problem- und Change-Management | Lehrplan erstellt | [P41](prompts/P41-incident-problem-und-change-management.md) | [P41](lehrplaene/P41-incident-problem-und-change-management.md) |
| 42 | C | IT-Betrieb und Prozesse | Ticketsysteme in der Praxis | Lehrplan erstellt | [P42](prompts/P42-ticketsysteme-in-der-praxis.md) | [P42](lehrplaene/P42-ticketsysteme-in-der-praxis.md) |
| 43 | C | IT-Betrieb und Prozesse | SLA und Betriebshandbuch | Lehrplan erstellt | [P43](prompts/P43-sla-und-betriebshandbuch.md) | [P43](lehrplaene/P43-sla-und-betriebshandbuch.md) |
| 44 | C | Client und Hardware | PC-Hardware und Fehlersuche | Lehrplan erstellt | [P44](prompts/P44-pc-hardware-und-fehlersuche.md) | [P44](lehrplaene/P44-pc-hardware-und-fehlersuche.md) |
| 45 | C | Client und Hardware | Windows-11-Client-Administration | Lehrplan erstellt | [P45](prompts/P45-windows-11-client-administration.md) | [P45](lehrplaene/P45-windows-11-client-administration.md) |
| 46 | C | Client und Hardware | Betriebssystem-Rollout (MDT, MECM und Alternativen) | Lehrplan erstellt | [P46](prompts/P46-betriebssystem-rollout-mdt-mecm-und-alternativen.md) | [P46](lehrplaene/P46-betriebssystem-rollout-mdt-mecm-und-alternativen.md) |
| 47 | C | Recht und Compliance | Datenschutz (DSGVO) in der IT | offen | [P47](prompts/P47-datenschutz-dsgvo-in-der-it.md) | – |
| 48 | C | Recht und Compliance | NIS2 für Administratoren | offen | [P48](prompts/P48-nis2-fuer-administratoren.md) | – |
| 49 | C | Recht und Compliance | ISO 27001 Grundlagen | offen | [P49](prompts/P49-iso-27001-grundlagen.md) | – |
| 50 | C | Zusatz | Troubleshooting-Methodik | offen | [P50](prompts/P50-troubleshooting-methodik.md) | – |
| 51 | C | Zusatz | Projektmanagement für Administratoren | offen | [P51](prompts/P51-projektmanagement-fuer-administratoren.md) | – |
| 52 | C | Zusatz | IT-Englisch für Administratoren | offen | [P52](prompts/P52-it-englisch-fuer-administratoren.md) | – |
<!-- TABELLE-ENDE -->

## Die 16 Fächer (K01–K16)

Neben den Prompts für neue Lehrpläne gibt es 16 Fächer, die schon als Lehrplan mit Skriptkapiteln vorliegen. Sie sind hier mit Typ, Modulen und Stunden erfasst, damit sie wie die Kurse oben geführt werden können. Die Modulübersicht je Fach liegt in `faecher/`; Übungsmaterial und Skripte stehen in eigenen Repositories (Spalte „Repository“, Eintrag in `daten/faecher.json`, Feld `repo`). Die Tabelle wird vom Skript erzeugt; nicht von Hand ändern.

<!-- FAECHER-START -->
16 Fächer: 9 Kern, 7 Erweiterung; zusammen 209 Module, ca. 2124,75 Stunden.

| Nr | Fach | Typ | Bereich | Module | Stunden | Voraussetzung | Repository |
|---|---|---|---|---|---|---|---|
| [K01](faecher/K01-linux-essentials.md) | Linux Essentials | Kern | Fundament | 12 | 96 | – | [linux-essentials-uebungen](https://github.com/AnsibleArtisan4711/linux-essentials-uebungen) |
| [K02](faecher/K02-webdesign.md) | Webdesign (HTML, CSS, responsives Design) | Kern | Web | 21 | 294,5 | – | [webdesign-uebungen](https://github.com/AnsibleArtisan4711/webdesign-uebungen) |
| [K03](faecher/K03-microsoft-excel-expert.md) | Microsoft Excel Expert | Kern | Daten & Office | 12 | 105 | Empfehlung: Office-Grundlagen (MOS, Erweiterung) | [microsoft-excel-expert-uebungen](https://github.com/AnsibleArtisan4711/microsoft-excel-expert-uebungen) |
| [K04](faecher/K04-bash.md) | Bash | Kern | Scripting & Automatisierung | 12 | 124 | Linux Essentials | [bash-uebungen](https://github.com/AnsibleArtisan4711/bash-uebungen) |
| [K05](faecher/K05-technische-dokumentation.md) | Technische Dokumentation & Dokumentations-Governance | Kern | Cloud, Doku & Business | 17 | 191,75 | – | [technische-dokumentation-uebungen](https://github.com/AnsibleArtisan4711/technische-dokumentation-uebungen) |
| [K06](faecher/K06-active-directory.md) | Active Directory | Kern | Windows & Microsoft | 12 | 134 | – | [active-directory-uebungen](https://github.com/AnsibleArtisan4711/active-directory-uebungen) |
| [K07](faecher/K07-python-automatisierung.md) | Python (Automatisierung unter Linux) | Kern | Scripting & Automatisierung | 15 | 150 | Bash | [python-automatisierung-uebungen](https://github.com/AnsibleArtisan4711/python-automatisierung-uebungen) |
| [K08](faecher/K08-git-versionskontrolle.md) | Git & Versionskontrolle | Kern | Scripting & Automatisierung | 12 | 126 | Bash | [git-versionskontrolle-uebungen](https://github.com/AnsibleArtisan4711/git-versionskontrolle-uebungen) |
| [K09](faecher/K09-powershell.md) | PowerShell | Kern | Windows & Microsoft | 12 | 126 | Bash | [powershell-uebungen](https://github.com/AnsibleArtisan4711/powershell-uebungen) |
| [K10](faecher/K10-microsoft-office-specialist-associate.md) | Microsoft Office Specialist Associate | Erweiterung | Fundament | 12 | 100 | – | [microsoft-office-specialist-associate-uebungen](https://github.com/AnsibleArtisan4711/microsoft-office-specialist-associate-uebungen) |
| [K11](faecher/K11-comptia-tech-itf.md) | CompTIA Tech+ / ITF+ | Erweiterung | Fundament | 12 | 87 | – | [comptia-tech-itf-uebungen](https://github.com/AnsibleArtisan4711/comptia-tech-itf-uebungen) |
| [K12](faecher/K12-aws-cloud-practitioner.md) | AWS Cloud Practitioner | Erweiterung | Cloud, Doku & Business | 12 | 106 | – | [aws-cloud-practitioner-uebungen](https://github.com/AnsibleArtisan4711/aws-cloud-practitioner-uebungen) |
| [K13](faecher/K13-webserver-apache-nginx.md) | Webserver (Apache HTTP Server & Nginx) | Erweiterung | Web | 14 | 165,5 | Webdesign, Linux Essentials | [webserver-uebungen](https://github.com/AnsibleArtisan4711/webserver-uebungen) |
| [K14](faecher/K14-100-gruppenrichtlinien.md) | 100 Gruppenrichtlinien | Erweiterung | Windows & Microsoft | 10 | 100 | Active Directory | [100-gruppenrichtlinien-uebungen](https://github.com/AnsibleArtisan4711/100-gruppenrichtlinien-uebungen) |
| [K15](faecher/K15-m365-governance.md) | M365 Governance | Erweiterung | Windows & Microsoft | 12 | 109 | Active Directory (empfohlen) | [m365-governance-uebungen](https://github.com/AnsibleArtisan4711/m365-governance-uebungen) |
| [K16](faecher/K16-unternehmensgruendung.md) | Unternehmensgründung | Erweiterung | Cloud, Doku & Business | 12 | 110 | – | [unternehmensgruendung-uebungen](https://github.com/AnsibleArtisan4711/unternehmensgruendung-uebungen) |
<!-- FAECHER-ENDE -->

## Die 6 Übungsreihen (E01–E06)

Eigene Übungsreihen, die nicht aus einem Lehrplan-Skript stammen: Homelab, Netzwerk, Active Directory, WLAN, Backup und USV. Aufbau und Umfang stehen in `uebungen/` und werden aus den Dateien der jeweiligen Repositories gelesen (`tools/uebungen_einlesen.py`). Die Tabelle wird vom Skript erzeugt; nicht von Hand ändern.

<!-- UEBUNGEN-START -->
| Nr | Übung | Thema | Module | Einheiten | Repository |
|---|---|---|---|---|---|
| [E01](uebungen/E01-multi-site-hybrid-cloud-ai-sec-lab.md) | Multi-Site Hybrid Cloud & AI-Sec Operations | Homelab und Betrieb | 14 | 92 | [multi-site-hybrid-cloud-ai-sec-lab](https://github.com/AnsibleArtisan4711/multi-site-hybrid-cloud-ai-sec-lab) |
| [E02](uebungen/E02-netzwerk-packet-tracer.md) | Netzwerktechnik mit Cisco Packet Tracer | Netzwerk | 8 | 1 | [netzwerk-uebungen-packet-tracer](https://github.com/AnsibleArtisan4711/netzwerk-uebungen-packet-tracer) |
| [E03](uebungen/E03-benutzerverwaltung-active-directory.md) | Benutzerverwaltung im Active Directory | Windows und Active Directory | 1 | 1 | [ad-uebungen-benutzerverwaltung](https://github.com/AnsibleArtisan4711/ad-uebungen-benutzerverwaltung) |
| [E04](uebungen/E04-wlan-gaestenetz.md) | WLAN und Gästenetz | Netzwerk | 2 | 2 | [wlan-gaeste-netz-uebung](https://github.com/AnsibleArtisan4711/wlan-gaeste-netz-uebung) |
| [E05](uebungen/E05-backup-nas-veeam.md) | Backup auf NAS mit Veeam | Homelab und Betrieb | 1 | 1 | [veeam-backup-uebung](https://github.com/AnsibleArtisan4711/veeam-backup-uebung) |
| [E06](uebungen/E06-geordnetes-herunterfahren-ohne-usv.md) | Geordnetes Herunterfahren ohne USV | Homelab und Betrieb | 1 | 1 | [usv-shutdown-uebung](https://github.com/AnsibleArtisan4711/usv-shutdown-uebung) |
<!-- UEBUNGEN-ENDE -->

## Empfohlene Reihenfolge

1. Priorität A zuerst: DNS, Windows-Server-Rollen, Virtualisierung, Netzwerkdienste, IT-Sicherheit und Monitoring.
2. Danach Priorität B, passend zu den vorhandenen Themen (Automatisierung zu PowerShell, Bash und Python; Azure zu Microsoft 365 Governance).
3. Priorität C nach Bedarf.

Schon vorhanden und deshalb nicht in der Liste: Active Directory, Gruppenrichtlinien, Microsoft 365, PowerShell, Bash, Python, Linux-Grundlagen, LPIC 1 bis 3, DHCP, DNSSEC, Netzwerktechnik, Webserver, Webdesign, Git, technische Dokumentation, Cloud-Grundlagen, IT-Grundlagen, Microsoft Office, Unternehmensgründung.

## Entstehung

Die Prompts und das Erzeugungsskript wurden gemeinsam mit Claude (Anthropic) entworfen. Die Kurse, die Reihenfolge und die Entscheidungen, was daraus ein Lehrplan wird, liegen bei mir. Prüfen muss man weiterhin die Ergebnisse der Gem, nicht nur die Prompts.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `prompts/` | ein Prompt pro Kurs (erzeugt, nicht von Hand bearbeiten) |
| `uebungen/` | Aufbau je Übungsreihe E01–E06 (erzeugt, nicht von Hand bearbeiten) |
| `faecher/` | Modulübersicht je Fach K01–K16 (erzeugt, nicht von Hand bearbeiten) |
| `lehrplaene/` | die fertigen, geprüften Lehrpläne (Markdown, mit Prüfvermerk am Ende); Ausarbeitungen zu Übungen liegen in eigenen Repositories |
| `daten/kurse.json` | Quelle der Kurse: Titel, Themen, Abgrenzung, Fokus-Technologien, Vorkenntnisse, Labor-Ressourcen, Hinweis, Status |
| `daten/uebungen.json` | Quelle der 6 Übungsreihen E01–E06: Titel, Thema, Repository, lokaler Ordner und der aus den Repositories gelesene Aufbau |
| `daten/faecher.json` | Quelle der 16 Fächer K01–K16: Typ, Bereich, Voraussetzung, Stunden, Module mit Stunden, Repository |
| `daten/rahmen.json` | gemeinsame Angaben: Umfang, Standard-Abgrenzung, erlaubte Status |
| `rahmen/prompt-vorlage.txt` | Variablen-Vorlage aller Prompts mit Platzhaltern |
| `gem/grundanweisung.md` | Grundanweisung der Gem (von Hand einzufügen) |
| `gem/vorlage-variablen.md` | leere Vorlage für einen eigenen Kurs-Prompt |
| `tools/build_prompts.py` | erzeugt `prompts/`, `faecher/`, `uebungen/` und die drei Tabellen |
| `tools/uebungen_einlesen.py` | liest den Aufbau der Übungsreihen E01–E06 aus ihren lokalen Repository-Ordnern in `daten/uebungen.json` |
| `tools/umsetzung_anlegen.py` | legt aus einem Lehrplan einen Umsetzungsordner an (Checklisten, Protokolle, Ablage für Screenshots) |
| `tools/bilder_index.py` | erzeugt `bilder-index.md` mit allen Bildern eines Umsetzungsordners; meldet unverlinkte, fehlende und große Bilder |
| `CHANGELOG.md` | Änderungen am gemeinsamen Rahmen |
| `LICENSE`, `LICENSE-DOCS.md` | MIT für das Skript, CC BY 4.0 für die Texte (Prompts, Vorlage, Daten, Lehrpläne) |

## Pflege

Im Repository-Ordner:

```powershell
python tools/build_prompts.py
git status --short
git add .
git commit -m "Prompts aktualisiert"
git push
```

- **Gemeinsamen Rahmen ändern** (Umfang, Standard-Abgrenzung): `daten/rahmen.json` oder `rahmen/prompt-vorlage.txt` bearbeiten, Skript laufen lassen. Zielgruppe und Regeln stehen in `gem/grundanweisung.md` und müssen dort und in der Gem angepasst werden. Alles im `CHANGELOG.md` eintragen.
- **Kurs ändern oder ergänzen:** Eintrag in `daten/kurse.json` bearbeiten oder am Ende anfügen (nächste freie ID, `slug` in Kleinbuchstaben ohne Umlaute), Skript laufen lassen.
- **Fach ändern oder ergänzen:** Eintrag in `daten/faecher.json` bearbeiten (Repository-Name in `repo` eintragen, sobald das Repository existiert), Skript laufen lassen.
- **Übungsreihe ändern oder ergänzen:** Eintrag in `daten/uebungen.json` anpassen (Feld `lokal` = Ordner des Repositories), dann `python tools/uebungen_einlesen.py` und `python tools/build_prompts.py`.
- **Umsetzung vorbereiten:** `python tools/umsetzung_anlegen.py P46` (oder `K01`, `E03`) legt neben dem Repository den Ordner `Umsetzung/P46-<slug>/` an, mit einem Unterordner je Modul (`checkliste.md`, `protokoll.md`, `fehlerprotokoll.md`, `screenshots/`, `notizen/`, `ausgaben/`), einer Übersicht, einer Liste der Befehle mit „nicht bestätigt“ und einem Abschlussordner. Ein zweiter Parameter wählt einen anderen Zielordner. Vorhandene Dateien werden nicht überschrieben.
- **Bilder indizieren:** `python tools/bilder_index.py` (Standard: `D:\Umsetzung`) oder mit Ordner als Parameter schreibt `bilder-index.md` in diesen Ordner: Tabelle aller verlinkten Bilder mit Modul, Abschnitt, Beschreibung, Größe und Link, dazu unverlinkte Bilder, Links auf fehlende Bilder und Bilder über 1 MB.
- **Qualität:** Die Prompts verlangen Versions- und Lizenzstände mit Datum. Diese Angaben im fertigen Lehrplan stichprobenartig gegen die Herstellerdokumentation prüfen.

## Lizenz

Texte (Prompts, Vorlage, Daten, Lehrpläne): CC BY 4.0, siehe [LICENSE-DOCS.md](LICENSE-DOCS.md). Skript `tools/build_prompts.py`: MIT, siehe [LICENSE](LICENSE).
