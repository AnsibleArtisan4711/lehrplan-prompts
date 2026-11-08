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
| `lehrplaene/` | die fertigen, geprüften Lehrpläne (Markdown, mit Prüfvermerk am Ende); Ausarbeitungen zu Übungen liegen in eigenen Repositories |
| `daten/kurse.json` | Quelle der Kurse: Titel, Themen, Abgrenzung, Fokus-Technologien, Vorkenntnisse, Labor-Ressourcen, Hinweis, Status |
| `daten/rahmen.json` | gemeinsame Angaben: Umfang, Standard-Abgrenzung, erlaubte Status |
| `rahmen/prompt-vorlage.txt` | Variablen-Vorlage aller Prompts mit Platzhaltern |
| `gem/grundanweisung.md` | Grundanweisung der Gem (von Hand einzufügen) |
| `gem/vorlage-variablen.md` | leere Vorlage für einen eigenen Kurs-Prompt |
| `tools/build_prompts.py` | erzeugt `prompts/` und die Tabelle oben (Link auf `lehrplaene/`) |
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
- **Qualität:** Die Prompts verlangen Versions- und Lizenzstände mit Datum. Diese Angaben im fertigen Lehrplan stichprobenartig gegen die Herstellerdokumentation prüfen.

## Lizenz

Texte (Prompts, Vorlage, Daten, Lehrpläne): CC BY 4.0, siehe [LICENSE-DOCS.md](LICENSE-DOCS.md). Skript `tools/build_prompts.py`: MIT, siehe [LICENSE](LICENSE).
