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
Stand der 241 Kurse: 213 offen, 0 Lehrplan erstellt, 0 aufbereitet, 28 gepusht.

Bedeutung der Status:

- **offen**: Der Prompt liegt vor, ein Lehrplan ist noch nicht erstellt.
- **Lehrplan erstellt**: Der Lehrplan ist erstellt und von mir geprüft. Er liegt in `lehrplaene/` und ist in der Spalte „Lehrplan“ verlinkt.
- **aufbereitet**: Aus dem Lehrplan ist Übungsmaterial ausgearbeitet, aber noch nicht veröffentlicht.
- **gepusht**: Das Übungsmaterial liegt als Kursordner in einem Themen-Repository auf GitHub, das in der Spalte „Repository“ verlinkt wird.

Kennung: **P** = ursprüngliche Prompt-Reihe (P01–P72). Die Kennungen **A**, **N** und **F** gehören zu Kursen aus der Sichtung der Excel-Lehrpläne, eingestuft nach dem Berufsbild Systemadministration und IT-Betrieb: **A** = Admin-Kern, **N** = Admin-nah, **F** = profilfern. Bei A, N und F steht die Priorität C, solange sie nicht von Hand gesetzt ist; das Themengebiet ist die Kategorie der Sichtung.

Spalte „Repository“: bei vorhandenem Kursordner (Feld `ordner`) der Link darauf, sonst das geplante Themen-Repository (Feld `repo` in `daten/kurse.json`).

| Nr | Prio | Themengebiet | Kurs | Status | Prompt | Lehrplan | Repository |
|---|---|---|---|---|---|---|---|
| 1 | A | Windows-Server-Rollen | DNS-Grundlagen (Windows-DNS und BIND) | gepusht | [P01](prompts/P01-dns-grundlagen-windows-dns-und-bind.md) | [P01](lehrplaene/P01-dns-grundlagen-windows-dns-und-bind.md) | [netzwerkdienste-uebungen/dns-grundlagen](https://github.com/AnsibleArtisan4711/netzwerkdienste-uebungen/tree/main/dns-grundlagen) |
| 2 | A | Windows-Server-Rollen | Dateidienste, DFS und Druckserver | gepusht | [P02](prompts/P02-dateidienste-dfs-und-druckserver.md) | [P02](lehrplaene/P02-dateidienste-dfs-und-druckserver.md) | [windows-server-uebungen/dateidienste-dfs-druckserver](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/dateidienste-dfs-druckserver) |
| 3 | A | Windows-Server-Rollen | WSUS und Update-Verwaltung | gepusht | [P03](prompts/P03-wsus-und-update-verwaltung.md) | [P03](lehrplaene/P03-wsus-und-update-verwaltung.md) | [windows-server-uebungen/wsus-und-update-verwaltung](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/wsus-und-update-verwaltung) |
| 4 | A | Windows-Server-Rollen | Zertifikatsdienste und PKI (AD CS) | gepusht | [P04](prompts/P04-zertifikatsdienste-und-pki-ad-cs.md) | [P04](lehrplaene/P04-zertifikatsdienste-und-pki-ad-cs.md) | [windows-server-uebungen/zertifikatsdienste-und-pki](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/zertifikatsdienste-und-pki) |
| 5 | A | Virtualisierung | Hyper-V Administration | gepusht | [P05](prompts/P05-hyper-v-administration.md) | [P05](lehrplaene/P05-hyper-v-administration.md) | [virtualisierung-uebungen/hyper-v-administration](https://github.com/AnsibleArtisan4711/virtualisierung-uebungen/tree/main/hyper-v-administration) |
| 6 | A | Virtualisierung | Proxmox VE | offen | [P06](prompts/P06-proxmox-ve.md) | – | `virtualisierung-uebungen` (geplant) |
| 7 | A | Virtualisierung | VMware vSphere und ESXi | offen | [P07](prompts/P07-vmware-vsphere-und-esxi.md) | – | `virtualisierung-uebungen` (geplant) |
| 8 | A | Netzwerkdienste und Firewall | Firewall mit OPNsense | offen | [P08](prompts/P08-firewall-mit-opnsense.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 9 | A | Netzwerkdienste und Firewall | Linux-Firewall mit nftables und iptables | offen | [P09](prompts/P09-linux-firewall-mit-nftables-und-iptables.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 10 | A | Netzwerkdienste und Firewall | VPN mit WireGuard und OpenVPN | gepusht | [P10](prompts/P10-vpn-mit-wireguard-und-openvpn.md) | [P10](lehrplaene/P10-vpn-mit-wireguard-und-openvpn.md) | [netzwerk-und-firewall-uebungen/vpn-mit-wireguard-und-openvpn](https://github.com/AnsibleArtisan4711/netzwerk-und-firewall-uebungen/tree/main/vpn-mit-wireguard-und-openvpn) |
| 11 | A | Netzwerkdienste und Firewall | Reverse Proxy, Lastverteilung und TLS | offen | [P11](prompts/P11-reverse-proxy-lastverteilung-und-tls.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 12 | A | IT-Sicherheit | IT-Sicherheitsgrundlagen | gepusht | [P12](prompts/P12-it-sicherheitsgrundlagen.md) | [P12](lehrplaene/P12-it-sicherheitsgrundlagen.md) | [it-sicherheit-uebungen/it-sicherheitsgrundlagen](https://github.com/AnsibleArtisan4711/it-sicherheit-uebungen/tree/main/it-sicherheitsgrundlagen) |
| 13 | A | IT-Sicherheit | Windows-Server-Härtung | offen | [P13](prompts/P13-windows-server-haertung.md) | – | `it-sicherheit-uebungen` (geplant) |
| 14 | A | IT-Sicherheit | Linux-Server-Härtung | offen | [P14](prompts/P14-linux-server-haertung.md) | – | `it-sicherheit-uebungen` (geplant) |
| 15 | A | IT-Sicherheit | Schwachstellenmanagement | offen | [P15](prompts/P15-schwachstellenmanagement.md) | – | `it-sicherheit-uebungen` (geplant) |
| 16 | A | IT-Sicherheit | Kryptografie, Zertifikate und TLS | gepusht | [P16](prompts/P16-kryptografie-zertifikate-und-tls.md) | [P16](lehrplaene/P16-kryptografie-zertifikate-und-tls.md) | [it-sicherheit-uebungen/kryptografie-zertifikate-und-tls](https://github.com/AnsibleArtisan4711/it-sicherheit-uebungen/tree/main/kryptografie-zertifikate-und-tls) |
| 17 | A | Monitoring und Logging | Monitoring mit Zabbix | offen | [P17](prompts/P17-monitoring-mit-zabbix.md) | – | `monitoring-logging-uebungen` (geplant) |
| 18 | A | Monitoring und Logging | Monitoring mit Prometheus und Grafana | offen | [P18](prompts/P18-monitoring-mit-prometheus-und-grafana.md) | – | `monitoring-logging-uebungen` (geplant) |
| 19 | A | Monitoring und Logging | Zentrales Logging mit Graylog und Elastic Stack | offen | [P19](prompts/P19-zentrales-logging-mit-graylog-und-elastic-stack.md) | – | `monitoring-logging-uebungen` (geplant) |
| 20 | A | Monitoring und Logging | Monitoring mit PRTG | offen | [P20](prompts/P20-monitoring-mit-prtg.md) | – | `monitoring-logging-uebungen` (geplant) |
| 21 | B | Automatisierung | Konfigurationsmanagement mit Ansible | offen | [P21](prompts/P21-konfigurationsmanagement-mit-ansible.md) | – | `automatisierung-uebungen` (geplant) |
| 22 | B | Automatisierung | Infrastructure as Code mit Terraform | offen | [P22](prompts/P22-infrastructure-as-code-mit-terraform.md) | – | `automatisierung-uebungen` (geplant) |
| 23 | B | Automatisierung | cloud-init und VM-Vorlagen | offen | [P23](prompts/P23-cloud-init-und-vm-vorlagen.md) | – | `automatisierung-uebungen` (geplant) |
| 24 | B | Automatisierung | PowerShell Desired State Configuration (DSC) | offen | [P24](prompts/P24-powershell-desired-state-configuration-dsc.md) | – | `automatisierung-uebungen` (geplant) |
| 25 | B | Container | Docker und Docker Compose | offen | [P25](prompts/P25-docker-und-docker-compose.md) | – | `container-uebungen` (geplant) |
| 26 | B | Container | Kubernetes-Grundlagen | offen | [P26](prompts/P26-kubernetes-grundlagen.md) | – | `container-uebungen` (geplant) |
| 27 | B | Azure und Identität | Azure Administration | offen | [P27](prompts/P27-azure-administration.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 28 | B | Azure und Identität | Entra ID und Hybrid-Identität | offen | [P28](prompts/P28-entra-id-und-hybrid-identitaet.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 29 | B | Azure und Identität | Intune und Autopilot | offen | [P29](prompts/P29-intune-und-autopilot.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 30 | B | Datenbanken | SQL-Grundlagen | gepusht | [P30](prompts/P30-sql-grundlagen.md) | [P30](lehrplaene/P30-sql-grundlagen.md) | [datenbanken-uebungen/sql-grundlagen](https://github.com/AnsibleArtisan4711/datenbanken-uebungen/tree/main/sql-grundlagen) |
| 31 | B | Datenbanken | MariaDB und PostgreSQL Administration | offen | [P31](prompts/P31-mariadb-und-postgresql-administration.md) | – | `datenbanken-uebungen` (geplant) |
| 32 | B | Datenbanken | SQL Server Administration | offen | [P32](prompts/P32-sql-server-administration.md) | – | `datenbanken-uebungen` (geplant) |
| 33 | B | Storage | NAS, SAN, iSCSI und RAID | offen | [P33](prompts/P33-nas-san-iscsi-und-raid.md) | – | `storage-backup-uebungen` (geplant) |
| 34 | B | Storage | Btrfs, ZFS und Snapshots | offen | [P34](prompts/P34-btrfs-zfs-und-snapshots.md) | – | `storage-backup-uebungen` (geplant) |
| 35 | B | Backup und Notfall | Backup-Konzept (3-2-1, RPO und RTO) | offen | [P35](prompts/P35-backup-konzept-3-2-1-rpo-und-rto.md) | – | `storage-backup-uebungen` (geplant) |
| 36 | B | Backup und Notfall | Notfallplanung und Disaster Recovery | offen | [P36](prompts/P36-notfallplanung-und-disaster-recovery.md) | – | `storage-backup-uebungen` (geplant) |
| 37 | B | E-Mail | Exchange Online Administration | offen | [P37](prompts/P37-exchange-online-administration.md) | – | `e-mail-uebungen` (geplant) |
| 38 | B | E-Mail | E-Mail-Authentifizierung: SPF, DKIM und DMARC | offen | [P38](prompts/P38-e-mail-authentifizierung-spf-dkim-und-dmarc.md) | – | `e-mail-uebungen` (geplant) |
| 39 | B | E-Mail | Mailserver mit Postfix und Dovecot | offen | [P39](prompts/P39-mailserver-mit-postfix-und-dovecot.md) | – | `e-mail-uebungen` (geplant) |
| 40 | C | IT-Betrieb und Prozesse | ITIL 4 Grundlagen | gepusht | [P40](prompts/P40-itil-4-grundlagen.md) | [P40](lehrplaene/P40-itil-4-grundlagen.md) | [it-betrieb-uebungen/itil-4-grundlagen](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/itil-4-grundlagen) |
| 41 | C | IT-Betrieb und Prozesse | Incident-, Problem- und Change-Management | gepusht | [P41](prompts/P41-incident-problem-und-change-management.md) | [P41](lehrplaene/P41-incident-problem-und-change-management.md) | [it-betrieb-uebungen/incident-problem-und-change-management](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/incident-problem-und-change-management) |
| 42 | C | IT-Betrieb und Prozesse | Ticketsysteme in der Praxis | gepusht | [P42](prompts/P42-ticketsysteme-in-der-praxis.md) | [P42](lehrplaene/P42-ticketsysteme-in-der-praxis.md) | [it-betrieb-uebungen/ticketsysteme-in-der-praxis](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/ticketsysteme-in-der-praxis) |
| 43 | C | IT-Betrieb und Prozesse | SLA und Betriebshandbuch | gepusht | [P43](prompts/P43-sla-und-betriebshandbuch.md) | [P43](lehrplaene/P43-sla-und-betriebshandbuch.md) | [it-betrieb-uebungen/sla-und-betriebshandbuch](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/sla-und-betriebshandbuch) |
| 44 | C | Client und Hardware | PC-Hardware und Fehlersuche | gepusht | [P44](prompts/P44-pc-hardware-und-fehlersuche.md) | [P44](lehrplaene/P44-pc-hardware-und-fehlersuche.md) | [client-hardware-uebungen/pc-hardware-und-fehlersuche](https://github.com/AnsibleArtisan4711/client-hardware-uebungen/tree/main/pc-hardware-und-fehlersuche) |
| 45 | C | Client und Hardware | Windows-11-Client-Administration | gepusht | [P45](prompts/P45-windows-11-client-administration.md) | [P45](lehrplaene/P45-windows-11-client-administration.md) | [client-hardware-uebungen/windows-11-client-administration](https://github.com/AnsibleArtisan4711/client-hardware-uebungen/tree/main/windows-11-client-administration) |
| 46 | C | Client und Hardware | Betriebssystem-Rollout (MDT, MECM und Alternativen) | gepusht | [P46](prompts/P46-betriebssystem-rollout-mdt-mecm-und-alternativen.md) | [P46](lehrplaene/P46-betriebssystem-rollout-mdt-mecm-und-alternativen.md) | [client-hardware-uebungen/betriebssystem-rollout](https://github.com/AnsibleArtisan4711/client-hardware-uebungen/tree/main/betriebssystem-rollout) |
| 47 | C | Recht und Compliance | Datenschutz (DSGVO) in der IT | gepusht | [P47](prompts/P47-datenschutz-dsgvo-in-der-it.md) | [P47](lehrplaene/P47-datenschutz-dsgvo-in-der-it.md) | [it-betrieb-uebungen/datenschutz-dsgvo-in-der-it](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/datenschutz-dsgvo-in-der-it) |
| 48 | C | Recht und Compliance | NIS2 für Administratoren | gepusht | [P48](prompts/P48-nis2-fuer-administratoren.md) | [P48](lehrplaene/P48-nis2-fuer-administratoren.md) | [it-betrieb-uebungen/nis2-fuer-administratoren](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/nis2-fuer-administratoren) |
| 49 | C | Recht und Compliance | ISO 27001 Grundlagen | gepusht | [P49](prompts/P49-iso-27001-grundlagen.md) | [P49](lehrplaene/P49-iso-27001-grundlagen.md) | [it-betrieb-uebungen/iso-27001-grundlagen](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/iso-27001-grundlagen) |
| 50 | C | Zusatz | Troubleshooting-Methodik | gepusht | [P50](prompts/P50-troubleshooting-methodik.md) | [P50](lehrplaene/P50-troubleshooting-methodik.md) | [it-betrieb-uebungen/troubleshooting-methodik](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/troubleshooting-methodik) |
| 51 | C | Zusatz | Projektmanagement für Administratoren | gepusht | [P51](prompts/P51-projektmanagement-fuer-administratoren.md) | [P51](lehrplaene/P51-projektmanagement-fuer-administratoren.md) | [it-betrieb-uebungen/projektmanagement-fuer-administratoren](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/projektmanagement-fuer-administratoren) |
| 52 | C | Zusatz | IT-Englisch für Administratoren | gepusht | [P52](prompts/P52-it-englisch-fuer-administratoren.md) | [P52](lehrplaene/P52-it-englisch-fuer-administratoren.md) | [it-betrieb-uebungen/it-englisch-fuer-administratoren](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/it-englisch-fuer-administratoren) |
| 53 | B | Container | Podman und Container-Sicherheit | offen | [P53](prompts/P53-podman-und-container-sicherheit.md) | – | `container-uebungen` (geplant) |
| 54 | B | Storage | LVM und Dateisysteme unter Linux | offen | [P54](prompts/P54-lvm-und-dateisysteme-unter-linux.md) | – | `storage-backup-uebungen` (geplant) |
| 55 | B | Storage | Dateidienste unter Linux mit Samba und NFS | offen | [P55](prompts/P55-dateidienste-unter-linux-mit-samba-und-nfs.md) | – | `storage-backup-uebungen` (geplant) |
| 56 | B | Cloud-Plattformen | AWS Administration (SysOps) | offen | [P56](prompts/P56-aws-administration-sysops.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 57 | B | Azure und Identität | Azure-Netzwerk und Azure-Sicherheit | offen | [P57](prompts/P57-azure-netzwerk-und-azure-sicherheit.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 58 | C | Cloud-Plattformen | Google Cloud Grundlagen | offen | [P58](prompts/P58-google-cloud-grundlagen.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 59 | B | Windows-Server-Rollen | Remotedesktopdienste (RDS) | gepusht | [P59](prompts/P59-remotedesktopdienste-rds.md) | [P59](lehrplaene/P59-remotedesktopdienste-rds.md) | [windows-server-uebungen/remotedesktopdienste-rds](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/remotedesktopdienste-rds) |
| 60 | B | Virtualisierung | Failover-Clustering und Hochverfügbarkeit | offen | [P60](prompts/P60-failover-clustering-und-hochverfuegbarkeit.md) | – | `virtualisierung-uebungen` (geplant) |
| 61 | C | Windows-Server-Rollen | Windows Admin Center | gepusht | [P61](prompts/P61-windows-admin-center.md) | [P61](lehrplaene/P61-windows-admin-center.md) | [windows-server-uebungen/windows-admin-center](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/windows-admin-center) |
| 62 | B | IT-Sicherheit | IDS und IPS mit Suricata | offen | [P62](prompts/P62-ids-und-ips-mit-suricata.md) | – | `it-sicherheit-uebungen` (geplant) |
| 63 | B | IT-Sicherheit | Passwort- und Secrets-Verwaltung | offen | [P63](prompts/P63-passwort-und-secrets-verwaltung.md) | – | `it-sicherheit-uebungen` (geplant) |
| 64 | B | IT-Sicherheit | Penetrationstest-Grundlagen | offen | [P64](prompts/P64-penetrationstest-grundlagen.md) | – | `it-sicherheit-uebungen` (geplant) |
| 65 | B | Automatisierung | CI/CD mit GitLab und Jenkins | offen | [P65](prompts/P65-ci-cd-mit-gitlab-und-jenkins.md) | – | `automatisierung-uebungen` (geplant) |
| 66 | C | Monitoring und Logging | Windows Event Forwarding und Ereignisprotokolle | offen | [P66](prompts/P66-windows-event-forwarding-und-ereignisprotokolle.md) | – | `monitoring-logging-uebungen` (geplant) |
| 67 | C | Datenbanken | NoSQL-Datenbanken und Redis | offen | [P67](prompts/P67-nosql-datenbanken-und-redis.md) | – | `datenbanken-uebungen` (geplant) |
| 68 | B | Datenbanken | Datenbank-Backup und -Wiederherstellung | offen | [P68](prompts/P68-datenbank-backup-und-wiederherstellung.md) | – | `datenbanken-uebungen` (geplant) |
| 69 | C | IT-Betrieb und Prozesse | Asset-Verwaltung und CMDB | gepusht | [P69](prompts/P69-asset-verwaltung-und-cmdb.md) | [P69](lehrplaene/P69-asset-verwaltung-und-cmdb.md) | [it-betrieb-uebungen/asset-verwaltung-und-cmdb](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/asset-verwaltung-und-cmdb) |
| 70 | C | IT-Betrieb und Prozesse | Lizenzmanagement | gepusht | [P70](prompts/P70-lizenzmanagement.md) | [P70](lehrplaene/P70-lizenzmanagement.md) | [it-betrieb-uebungen/lizenzmanagement](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/lizenzmanagement) |
| 71 | A | Netzwerkdienste und Firewall | DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea) | gepusht | [P71](prompts/P71-dhcp-grundlagen-und-betrieb.md) | [P71](lehrplaene/P71-dhcp-grundlagen-und-betrieb.md) | [netzwerkdienste-uebungen/dhcp-grundlagen-und-betrieb](https://github.com/AnsibleArtisan4711/netzwerkdienste-uebungen/tree/main/dhcp-grundlagen-und-betrieb) |
| 72 | A | IT-Betrieb und Prozesse | Weiterbildung IT-Systemtechnik (Querschnitt nach der Lehre) | gepusht | [P72](prompts/P72-weiterbildung-it-systemtechnik.md) | [P72](lehrplaene/P72-weiterbildung-it-systemtechnik.md) | [it-betrieb-uebungen/weiterbildung-it-systemtechnik](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/weiterbildung-it-systemtechnik) |
| 73 | C | Windows, Client & Betriebssysteme | Betriebssysteme | offen | [A01](prompts/A01-betriebssysteme.md) | – | `client-hardware-uebungen` (geplant) |
| 74 | C | Windows, Client & Betriebssysteme | CompTIA A+ | offen | [A02](prompts/A02-comptia-a-plus.md) | – | `client-hardware-uebungen` (geplant) |
| 75 | C | Windows, Client & Betriebssysteme | Microsoft MD-102 | offen | [A03](prompts/A03-microsoft-md-102.md) | – | `client-hardware-uebungen` (geplant) |
| 76 | C | Windows, Client & Betriebssysteme | Microsoft Windows Server Hybrid Administrator | offen | [A04](prompts/A04-microsoft-windows-server-hybrid-administrator.md) | – | `windows-server-uebungen` (geplant) |
| 77 | C | Windows, Client & Betriebssysteme | Weiterbildung IT Systemtechnik | offen | [A05](prompts/A05-weiterbildung-it-systemtechnik.md) | – | `it-betrieb-uebungen` (geplant) |
| 78 | C | Windows, Client & Betriebssysteme | Windows Autopilot | offen | [A06](prompts/A06-windows-autopilot.md) | – | `client-hardware-uebungen` (geplant) |
| 79 | C | Windows, Client & Betriebssysteme | Windows Server 2025 | offen | [A07](prompts/A07-windows-server-2025.md) | – | `windows-server-uebungen` (geplant) |
| 80 | C | Identität, Zugriff & Microsoft 365 | Conditional Access (CA) | offen | [A08](prompts/A08-conditional-access.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 81 | C | Identität, Zugriff & Microsoft 365 | LDAP | offen | [A09](prompts/A09-ldap.md) | – | `windows-server-uebungen` (geplant) |
| 82 | C | Identität, Zugriff & Microsoft 365 | MFA und Passwordless | offen | [A10](prompts/A10-mfa-und-passwordless.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 83 | C | Identität, Zugriff & Microsoft 365 | Microsoft Defender | offen | [A11](prompts/A11-microsoft-defender.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 84 | C | Identität, Zugriff & Microsoft 365 | Microsoft MS-102 | offen | [A12](prompts/A12-microsoft-ms-102.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 85 | C | Identität, Zugriff & Microsoft 365 | Microsoft SC-300 | offen | [A13](prompts/A13-microsoft-sc-300.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 86 | C | Identität, Zugriff & Microsoft 365 | Privileged Identity Management | offen | [A14](prompts/A14-privileged-identity-management.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 87 | C | Linux & Open Source | LPIC-1 | offen | [A15](prompts/A15-lpic-1.md) | – | `linux-uebungen` (geplant) |
| 88 | C | Linux & Open Source | LPIC-2 | offen | [A16](prompts/A16-lpic-2.md) | – | `linux-uebungen` (geplant) |
| 89 | C | Linux & Open Source | LPIC-3 | offen | [A17](prompts/A17-lpic-3.md) | – | `linux-uebungen` (geplant) |
| 90 | C | Linux & Open Source | RHEL-Familie (Red Hat Enterprise Linux und AlmaLinux) | offen | [A18](prompts/A18-rhel-familie.md) | – | `linux-uebungen` (geplant) |
| 91 | C | Netzwerk & Netzwerkdienste | Cisco CCNA | offen | [A19](prompts/A19-cisco-ccna.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 92 | C | Netzwerk & Netzwerkdienste | DNS Security (DNSSEC) | offen | [A20](prompts/A20-dns-security.md) | – | `netzwerkdienste-uebungen` (geplant) |
| 93 | C | Netzwerk & Netzwerkdienste | E-Mail-Routing, SMTP und Mail Security | offen | [A21](prompts/A21-e-mail-routing-smtp-und-mail-security.md) | – | `e-mail-uebungen` (geplant) |
| 94 | C | Netzwerk & Netzwerkdienste | Firewall, Netzwerkdesign und DMZ | offen | [A22](prompts/A22-firewall-netzwerkdesign-und-dmz.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 95 | C | Netzwerk & Netzwerkdienste | Netzwerktechnik | offen | [A23](prompts/A23-netzwerktechnik.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 96 | C | Netzwerk & Netzwerkdienste | Open-Source-Firewalls (IPFire und OPNsense) | offen | [A24](prompts/A24-open-source-firewalls.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 97 | C | Netzwerk & Netzwerkdienste | Traffic Analysis (NetFlow, Wireshark, tcpdump) | offen | [A25](prompts/A25-traffic-analysis.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 98 | C | IT-Sicherheit & Compliance | CompTIA Security+ | offen | [A26](prompts/A26-comptia-security-plus.md) | – | `it-sicherheit-uebungen` (geplant) |
| 99 | C | IT-Sicherheit & Compliance | Cyber-Angriffe und Verteidigung | offen | [A27](prompts/A27-cyber-angriffe-und-verteidigung.md) | – | `it-sicherheit-uebungen` (geplant) |
| 100 | C | IT-Sicherheit & Compliance | DSGVO | offen | [A28](prompts/A28-dsgvo.md) | – | `it-betrieb-uebungen` (geplant) |
| 101 | C | IT-Sicherheit & Compliance | Incident Response | offen | [A29](prompts/A29-incident-response.md) | – | `it-sicherheit-uebungen` (geplant) |
| 102 | C | IT-Sicherheit & Compliance | SIEM | offen | [A30](prompts/A30-siem.md) | – | `it-sicherheit-uebungen` (geplant) |
| 103 | C | IT-Sicherheit & Compliance | Schwachstellen-, Patch- und Änderungsmanagement | offen | [A31](prompts/A31-schwachstellen-patch-und-aenderungsmanagement.md) | – | `it-sicherheit-uebungen` (geplant) |
| 104 | C | Cloud-Plattformen (AWS, Azure, Google) | AWS Certified CloudOps Engineer Associate | offen | [A32](prompts/A32-aws-certified-cloudops-engineer-associate.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 105 | C | Cloud-Plattformen (AWS, Azure, Google) | AWS Certified Solutions Architect Associate | offen | [A33](prompts/A33-aws-certified-solutions-architect-associate.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 106 | C | Cloud-Plattformen (AWS, Azure, Google) | Azure Virtual Desktop | offen | [A34](prompts/A34-azure-virtual-desktop.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 107 | C | Cloud-Plattformen (AWS, Azure, Google) | Google Associate Cloud Engineer | offen | [A35](prompts/A35-google-associate-cloud-engineer.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 108 | C | Cloud-Plattformen (AWS, Azure, Google) | Microsoft AZ-104 | offen | [A36](prompts/A36-microsoft-az-104.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 109 | C | Cloud-Plattformen (AWS, Azure, Google) | Microsoft AZ-500 | offen | [A37](prompts/A37-microsoft-az-500.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 110 | C | Cloud-Plattformen (AWS, Azure, Google) | Microsoft AZ-900 (Azure Fundamentals) | offen | [A38](prompts/A38-microsoft-az-900.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 111 | C | Virtualisierung, Container & Automatisierung | Ansible | offen | [A39](prompts/A39-ansible.md) | – | `automatisierung-uebungen` (geplant) |
| 112 | C | Virtualisierung, Container & Automatisierung | Docker und Container (inkl. Nano-Images) | offen | [A40](prompts/A40-docker-und-container.md) | – | `container-uebungen` (geplant) |
| 113 | C | Virtualisierung, Container & Automatisierung | Kubernetes (Grundlagen und Betrieb) | offen | [A41](prompts/A41-kubernetes.md) | – | `container-uebungen` (geplant) |
| 114 | C | Virtualisierung, Container & Automatisierung | Virtualisierung (VMware vSphere/ESXi und Microsoft Hyper-V) | offen | [A42](prompts/A42-virtualisierung.md) | – | `virtualisierung-uebungen` (geplant) |
| 115 | C | Speicher, Backup & Hochverfügbarkeit | BCDR | offen | [A43](prompts/A43-bcdr.md) | – | `storage-backup-uebungen` (geplant) |
| 116 | C | Speicher, Backup & Hochverfügbarkeit | Backup, Restore und Ransomware Recovery | offen | [A44](prompts/A44-backup-restore-und-ransomware-recovery.md) | – | `storage-backup-uebungen` (geplant) |
| 117 | C | Speicher, Backup & Hochverfügbarkeit | File-Systeme | offen | [A45](prompts/A45-file-systeme.md) | – | `storage-backup-uebungen` (geplant) |
| 118 | C | Speicher, Backup & Hochverfügbarkeit | High Availability und Load Balancing | offen | [A46](prompts/A46-high-availability-und-load-balancing.md) | – | `virtualisierung-uebungen` (geplant) |
| 119 | C | Speicher, Backup & Hochverfügbarkeit | Storage: SAN, NAS und Storage-Protokolle | offen | [A47](prompts/A47-storage-san-nas-und-storage-protokolle.md) | – | `storage-backup-uebungen` (geplant) |
| 120 | C | Datenbanken | MS SQL | offen | [A48](prompts/A48-ms-sql.md) | – | `datenbanken-uebungen` (geplant) |
| 121 | C | Datenbanken | MySQL (MariaDB) | offen | [A49](prompts/A49-mysql.md) | – | `datenbanken-uebungen` (geplant) |
| 122 | C | Datenbanken | PostgreSQL | offen | [A50](prompts/A50-postgresql.md) | – | `datenbanken-uebungen` (geplant) |
| 123 | C | Monitoring, Logging & Betrieb | Logmanagement | offen | [A51](prompts/A51-logmanagement.md) | – | `monitoring-logging-uebungen` (geplant) |
| 124 | C | Monitoring, Logging & Betrieb | Monitoring, Alerting und SLO/SLA/SLI | offen | [A52](prompts/A52-monitoring-alerting-und-slo-sla-sli.md) | – | `monitoring-logging-uebungen` (geplant) |
| 125 | C | Monitoring, Logging & Betrieb | Troubleshooting | offen | [A53](prompts/A53-troubleshooting.md) | – | `it-betrieb-uebungen` (geplant) |
| 126 | C | ITSM, Assets & Lieferanten | CMDB und Asset Management | offen | [A54](prompts/A54-cmdb-und-asset-management.md) | – | `it-betrieb-uebungen` (geplant) |
| 127 | C | Windows, Client & Betriebssysteme | Registry und Treiber | offen | [N01](prompts/N01-registry-und-treiber.md) | – | `client-hardware-uebungen` (geplant) |
| 128 | C | Identität, Zugriff & Microsoft 365 | Copilot Readiness | offen | [N02](prompts/N02-copilot-readiness.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 129 | C | Identität, Zugriff & Microsoft 365 | MS-900 | offen | [N03](prompts/N03-ms-900.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 130 | C | Identität, Zugriff & Microsoft 365 | Microsoft Purview | offen | [N04](prompts/N04-microsoft-purview.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 131 | C | Identität, Zugriff & Microsoft 365 | Microsoft SC-500 | offen | [N05](prompts/N05-microsoft-sc-500.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 132 | C | Identität, Zugriff & Microsoft 365 | Microsoft SC-900 | offen | [N06](prompts/N06-microsoft-sc-900.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 133 | C | Netzwerk & Netzwerkdienste | BGP | offen | [N07](prompts/N07-bgp.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 134 | C | Netzwerk & Netzwerkdienste | NAC (802.1X) | offen | [N08](prompts/N08-nac.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 135 | C | Netzwerk & Netzwerkdienste | SD-WAN | offen | [N09](prompts/N09-sd-wan.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 136 | C | Netzwerk & Netzwerkdienste | VoIP und QoS | offen | [N10](prompts/N10-voip-und-qos.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 137 | C | Netzwerk & Netzwerkdienste | WLAN-Infrastruktur | offen | [N11](prompts/N11-wlan-infrastruktur.md) | – | `netzwerk-und-firewall-uebungen` (geplant) |
| 138 | C | IT-Sicherheit & Compliance | Compliance in Unternehmen | offen | [N12](prompts/N12-compliance-in-unternehmen.md) | – | `it-betrieb-uebungen` (geplant) |
| 139 | C | IT-Sicherheit & Compliance | IT-Risikomanagement | offen | [N13](prompts/N13-it-risikomanagement.md) | – | `it-betrieb-uebungen` (geplant) |
| 140 | C | IT-Sicherheit & Compliance | Kali Linux | offen | [N14](prompts/N14-kali-linux.md) | – | `it-sicherheit-uebungen` (geplant) |
| 141 | C | IT-Sicherheit & Compliance | Secrets Management und Vault-Konzepte | offen | [N15](prompts/N15-secrets-management-und-vault-konzepte.md) | – | `it-sicherheit-uebungen` (geplant) |
| 142 | C | IT-Sicherheit & Compliance | Security Awareness und Phishing-Simulation | offen | [N16](prompts/N16-security-awareness-und-phishing-simulation.md) | – | `it-sicherheit-uebungen` (geplant) |
| 143 | C | IT-Sicherheit & Compliance | Zero Trust Grundlagen: Identität, Geräte und Daten | offen | [N17](prompts/N17-zero-trust-grundlagen-identitaet-geraete-und-dat.md) | – | `it-sicherheit-uebungen` (geplant) |
| 144 | C | Cloud-Plattformen (AWS, Azure, Google) | AWS Certified Advanced Networking Specialty | offen | [N18](prompts/N18-aws-certified-advanced-networking-specialty.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 145 | C | Cloud-Plattformen (AWS, Azure, Google) | AWS Certified Security Specialty | offen | [N19](prompts/N19-aws-certified-security-specialty.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 146 | C | Cloud-Plattformen (AWS, Azure, Google) | Google Cloud Digital Leader | offen | [N20](prompts/N20-google-cloud-digital-leader.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 147 | C | Cloud-Plattformen (AWS, Azure, Google) | Google Professional Cloud Network Engineer | offen | [N21](prompts/N21-google-professional-cloud-network-engineer.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 148 | C | Cloud-Plattformen (AWS, Azure, Google) | Google Professional Cloud Security Engineer | offen | [N22](prompts/N22-google-professional-cloud-security-engineer.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 149 | C | Cloud-Plattformen (AWS, Azure, Google) | Microsoft AZ-305 | offen | [N23](prompts/N23-microsoft-az-305.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 150 | C | Cloud-Plattformen (AWS, Azure, Google) | Microsoft AZ-700 | offen | [N24](prompts/N24-microsoft-az-700.md) | – | `cloud-identitaet-uebungen` (geplant) |
| 151 | C | Virtualisierung, Container & Automatisierung | AWS Certified DevOps Engineer Professional | offen | [N25](prompts/N25-aws-certified-devops-engineer-professional.md) | – | `automatisierung-uebungen` (geplant) |
| 152 | C | Virtualisierung, Container & Automatisierung | CI/CD-Pipeline | offen | [N26](prompts/N26-ci-cd-pipeline.md) | – | `automatisierung-uebungen` (geplant) |
| 153 | C | Virtualisierung, Container & Automatisierung | Google Professional Cloud DevOps Engineer | offen | [N27](prompts/N27-google-professional-cloud-devops-engineer.md) | – | `automatisierung-uebungen` (geplant) |
| 154 | C | Virtualisierung, Container & Automatisierung | Terraform | offen | [N28](prompts/N28-terraform.md) | – | `automatisierung-uebungen` (geplant) |
| 155 | C | Datenbanken | Google Professional Database Engineer | offen | [N29](prompts/N29-google-professional-database-engineer.md) | – | `datenbanken-uebungen` (geplant) |
| 156 | C | Datenbanken | MongoDB | offen | [N30](prompts/N30-mongodb.md) | – | `datenbanken-uebungen` (geplant) |
| 157 | C | Datenbanken | Redis | offen | [N31](prompts/N31-redis.md) | – | `datenbanken-uebungen` (geplant) |
| 158 | C | ITSM, Assets & Lieferanten | Anwendungssupport | offen | [N32](prompts/N32-anwendungssupport.md) | – | `it-betrieb-uebungen` (geplant) |
| 159 | C | ITSM, Assets & Lieferanten | Jira Service Management | offen | [N33](prompts/N33-jira-service-management.md) | – | `it-betrieb-uebungen` (geplant) |
| 160 | C | ITSM, Assets & Lieferanten | ServiceNow | offen | [N34](prompts/N34-servicenow.md) | – | `it-betrieb-uebungen` (geplant) |
| 161 | C | ITSM, Assets & Lieferanten | Vendor Management und Lizenzmanagement | offen | [N35](prompts/N35-vendor-management-und-lizenzmanagement.md) | – | `it-betrieb-uebungen` (geplant) |
| 162 | C | Hardware, Geräte & Elektro | Arduino | offen | [N36](prompts/N36-arduino.md) | – | `client-hardware-uebungen` (geplant) |
| 163 | C | Hardware, Geräte & Elektro | Elektrotechnik, Strom und Sicherheit | offen | [N37](prompts/N37-elektrotechnik-strom-und-sicherheit.md) | – | `client-hardware-uebungen` (geplant) |
| 164 | C | Hardware, Geräte & Elektro | Gerätetechnik | offen | [N38](prompts/N38-geraetetechnik.md) | – | `client-hardware-uebungen` (geplant) |
| 165 | C | Hardware, Geräte & Elektro | Kabel und Stecker | offen | [N39](prompts/N39-kabel-und-stecker.md) | – | `client-hardware-uebungen` (geplant) |
| 166 | C | Hardware, Geräte & Elektro | Raspberry Pi und Einplatinencomputer | offen | [N40](prompts/N40-raspberry-pi-und-einplatinencomputer.md) | – | `client-hardware-uebungen` (geplant) |
| 167 | C | Office, Dokumentation & Low-Code | Confluence | offen | [N41](prompts/N41-confluence.md) | – | `it-betrieb-uebungen` (geplant) |
| 168 | C | Office, Dokumentation & Low-Code | LaTeX (inkl. MiKTeX, TeXstudio und Overleaf) | offen | [N42](prompts/N42-latex.md) | – | `office-uebungen` (geplant) |
| 169 | C | Office, Dokumentation & Low-Code | Microsoft Access Expert | offen | [N43](prompts/N43-microsoft-access-expert.md) | – | `office-uebungen` (geplant) |
| 170 | C | Office, Dokumentation & Low-Code | Microsoft Outlook Associate | offen | [N44](prompts/N44-microsoft-outlook-associate.md) | – | `office-uebungen` (geplant) |
| 171 | C | Office, Dokumentation & Low-Code | Microsoft PL-900 (Power Platform Fundamentals) | offen | [N45](prompts/N45-microsoft-pl-900.md) | – | `office-uebungen` (geplant) |
| 172 | C | Office, Dokumentation & Low-Code | Microsoft PowerPoint Associate | offen | [N46](prompts/N46-microsoft-powerpoint-associate.md) | – | `office-uebungen` (geplant) |
| 173 | C | Office, Dokumentation & Low-Code | Microsoft Word Expert | offen | [N47](prompts/N47-microsoft-word-expert.md) | – | `office-uebungen` (geplant) |
| 174 | C | Office, Dokumentation & Low-Code | Power Platform Governance | offen | [N48](prompts/N48-power-platform-governance.md) | – | `office-uebungen` (geplant) |
| 175 | C | Projekt- und Methodenwissen | Anforderungsmanagement | offen | [N49](prompts/N49-anforderungsmanagement.md) | – | `it-betrieb-uebungen` (geplant) |
| 176 | C | Projekt- und Methodenwissen | Kanban | offen | [N50](prompts/N50-kanban.md) | – | `it-betrieb-uebungen` (geplant) |
| 177 | C | Projekt- und Methodenwissen | Projekt-Risikoregister und Issue Tracking | offen | [N51](prompts/N51-projekt-risikoregister-und-issue-tracking.md) | – | `it-betrieb-uebungen` (geplant) |
| 178 | C | Projekt- und Methodenwissen | Projektmanagement | offen | [N52](prompts/N52-projektmanagement.md) | – | `it-betrieb-uebungen` (geplant) |
| 179 | C | Projekt- und Methodenwissen | Scrum | offen | [N53](prompts/N53-scrum.md) | – | `it-betrieb-uebungen` (geplant) |
| 180 | C | Programmierung, Web & Design | Apache Tomcat | offen | [N54](prompts/N54-apache-tomcat.md) | – | `web-uebungen` (geplant) |
| 181 | C | Projekt- und Methodenwissen | Open Source | offen | [F01](prompts/F01-open-source.md) | – | `it-betrieb-uebungen` (geplant) |
| 182 | C | Projekt- und Methodenwissen | Stakeholder Management und Moderation | offen | [F02](prompts/F02-stakeholder-management-und-moderation.md) | – | `it-betrieb-uebungen` (geplant) |
| 183 | C | Programmierung, Web & Design | AWS Certified Developer Associate | offen | [F03](prompts/F03-aws-certified-developer-associate.md) | – | `programmierung-uebungen` (geplant) |
| 184 | C | Programmierung, Web & Design | Adobe XD | offen | [F04](prompts/F04-adobe-xd.md) | – | `web-uebungen` (geplant) |
| 185 | C | Programmierung, Web & Design | Algorithmen und Datenstrukturen | offen | [F05](prompts/F05-algorithmen-und-datenstrukturen.md) | – | `programmierung-uebungen` (geplant) |
| 186 | C | Programmierung, Web & Design | Android | offen | [F06](prompts/F06-android.md) | – | `programmierung-uebungen` (geplant) |
| 187 | C | Programmierung, Web & Design | Angular | offen | [F07](prompts/F07-angular.md) | – | `web-uebungen` (geplant) |
| 188 | C | Programmierung, Web & Design | Bootstrap | offen | [F08](prompts/F08-bootstrap.md) | – | `web-uebungen` (geplant) |
| 189 | C | Programmierung, Web & Design | C# und .NET | offen | [F09](prompts/F09-c-sharp-und-net.md) | – | `programmierung-uebungen` (geplant) |
| 190 | C | Programmierung, Web & Design | C++ | offen | [F10](prompts/F10-c-plus-plus.md) | – | `programmierung-uebungen` (geplant) |
| 191 | C | Programmierung, Web & Design | GraphQL | offen | [F11](prompts/F11-graphql.md) | – | `web-uebungen` (geplant) |
| 192 | C | Programmierung, Web & Design | Java | offen | [F12](prompts/F12-java.md) | – | `programmierung-uebungen` (geplant) |
| 193 | C | Programmierung, Web & Design | JavaScript | offen | [F13](prompts/F13-javascript.md) | – | `web-uebungen` (geplant) |
| 194 | C | Programmierung, Web & Design | Logik und diskrete Mathematik | offen | [F14](prompts/F14-logik-und-diskrete-mathematik.md) | – | `programmierung-uebungen` (geplant) |
| 195 | C | Programmierung, Web & Design | Material 3 | offen | [F15](prompts/F15-material-3.md) | – | `web-uebungen` (geplant) |
| 196 | C | Programmierung, Web & Design | Mathematik (Grundlagen und Anwendung) | offen | [F16](prompts/F16-mathematik.md) | – | `programmierung-uebungen` (geplant) |
| 197 | C | Programmierung, Web & Design | PHP | offen | [F17](prompts/F17-php.md) | – | `web-uebungen` (geplant) |
| 198 | C | Programmierung, Web & Design | RESTful API | offen | [F18](prompts/F18-restful-api.md) | – | `web-uebungen` (geplant) |
| 199 | C | Programmierung, Web & Design | React.js | offen | [F19](prompts/F19-react-js.md) | – | `web-uebungen` (geplant) |
| 200 | C | Programmierung, Web & Design | Visual Basic | offen | [F20](prompts/F20-visual-basic.md) | – | `programmierung-uebungen` (geplant) |
| 201 | C | Programmierung, Web & Design | Vue.js | offen | [F21](prompts/F21-vue-js.md) | – | `web-uebungen` (geplant) |
| 202 | C | Programmierung, Web & Design | XML | offen | [F22](prompts/F22-xml.md) | – | `web-uebungen` (geplant) |
| 203 | C | KI, Machine Learning & Daten | AWS Certified AI Practitioner | offen | [F23](prompts/F23-aws-certified-ai-practitioner.md) | – | `ki-und-daten-uebungen` (geplant) |
| 204 | C | KI, Machine Learning & Daten | AWS Certified Data Engineer Associate | offen | [F24](prompts/F24-aws-certified-data-engineer-associate.md) | – | `ki-und-daten-uebungen` (geplant) |
| 205 | C | KI, Machine Learning & Daten | AWS Certified Generative AI Developer Professional | offen | [F25](prompts/F25-aws-certified-generative-ai-developer-profession.md) | – | `ki-und-daten-uebungen` (geplant) |
| 206 | C | KI, Machine Learning & Daten | AWS Certified Machine Learning Engineer Associate | offen | [F26](prompts/F26-aws-certified-machine-learning-engineer-associat.md) | – | `ki-und-daten-uebungen` (geplant) |
| 207 | C | KI, Machine Learning & Daten | CompTIA Data+ | offen | [F27](prompts/F27-comptia-data-plus.md) | – | `ki-und-daten-uebungen` (geplant) |
| 208 | C | KI, Machine Learning & Daten | Google AI Studio | offen | [F28](prompts/F28-google-ai-studio.md) | – | `ki-und-daten-uebungen` (geplant) |
| 209 | C | KI, Machine Learning & Daten | Google Generative AI Leader | offen | [F29](prompts/F29-google-generative-ai-leader.md) | – | `ki-und-daten-uebungen` (geplant) |
| 210 | C | KI, Machine Learning & Daten | Google Professional Data Engineer | offen | [F30](prompts/F30-google-professional-data-engineer.md) | – | `ki-und-daten-uebungen` (geplant) |
| 211 | C | KI, Machine Learning & Daten | Google Professional Machine Learning Engineer | offen | [F31](prompts/F31-google-professional-machine-learning-engineer.md) | – | `ki-und-daten-uebungen` (geplant) |
| 212 | C | KI, Machine Learning & Daten | KI-Ethik & Datenschutz | offen | [F32](prompts/F32-ki-ethik-und-datenschutz.md) | – | `ki-und-daten-uebungen` (geplant) |
| 213 | C | KI, Machine Learning & Daten | Künstliche Intelligenz | offen | [F33](prompts/F33-kuenstliche-intelligenz.md) | – | `ki-und-daten-uebungen` (geplant) |
| 214 | C | KI, Machine Learning & Daten | Large und Small Language Models | offen | [F34](prompts/F34-large-und-small-language-models.md) | – | `ki-und-daten-uebungen` (geplant) |
| 215 | C | KI, Machine Learning & Daten | Machine Learning und Data Science | offen | [F35](prompts/F35-machine-learning-und-data-science.md) | – | `ki-und-daten-uebungen` (geplant) |
| 216 | C | KI, Machine Learning & Daten | Microsoft AI-900 | offen | [F36](prompts/F36-microsoft-ai-900.md) | – | `ki-und-daten-uebungen` (geplant) |
| 217 | C | KI, Machine Learning & Daten | Microsoft DP-900 | offen | [F37](prompts/F37-microsoft-dp-900.md) | – | `ki-und-daten-uebungen` (geplant) |
| 218 | C | KI, Machine Learning & Daten | Pandas | offen | [F38](prompts/F38-pandas.md) | – | `ki-und-daten-uebungen` (geplant) |
| 219 | C | KI, Machine Learning & Daten | Prompt Engineering | offen | [F39](prompts/F39-prompt-engineering.md) | – | `ki-und-daten-uebungen` (geplant) |
| 220 | C | KI, Machine Learning & Daten | TensorFlow | offen | [F40](prompts/F40-tensorflow.md) | – | `ki-und-daten-uebungen` (geplant) |
| 221 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Bankenwesen | offen | [F41](prompts/F41-bankenwesen.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 222 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Bilanzbuchhalterprüfung Österreich | offen | [F42](prompts/F42-bilanzbuchhalterpruefung-oesterreich.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 223 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Buchhalterprüfung Österreich | offen | [F43](prompts/F43-buchhalterpruefung-oesterreich.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 224 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Business Management | offen | [F44](prompts/F44-business-management.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 225 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Controlling und Reporting | offen | [F45](prompts/F45-controlling-und-reporting.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 226 | C | Wirtschaft, Steuer, Marketing & Soft Skills | E-Commerce: Zahlungsabwicklung | offen | [F46](prompts/F46-e-commerce-zahlungsabwicklung.md) | – | `web-uebungen` (geplant) |
| 227 | C | Wirtschaft, Steuer, Marketing & Soft Skills | IT-Controlling | offen | [F47](prompts/F47-it-controlling.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 228 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Kommunikation | offen | [F48](prompts/F48-kommunikation.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 229 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Kundenorientierung | offen | [F49](prompts/F49-kundenorientierung.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 230 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Magento | offen | [F50](prompts/F50-magento.md) | – | `web-uebungen` (geplant) |
| 231 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Marketing | offen | [F51](prompts/F51-marketing.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 232 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Microsoft Dynamics 365 | offen | [F52](prompts/F52-microsoft-dynamics-365.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 233 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Personalverrechnung Österreich | offen | [F53](prompts/F53-personalverrechnung-oesterreich.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 234 | C | Wirtschaft, Steuer, Marketing & Soft Skills | SAP | offen | [F54](prompts/F54-sap.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 235 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Search Engine Optimization | offen | [F55](prompts/F55-search-engine-optimization.md) | – | `web-uebungen` (geplant) |
| 236 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Shopify | offen | [F56](prompts/F56-shopify.md) | – | `web-uebungen` (geplant) |
| 237 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Social Media Marketing (LinkedIn, Meta und YouTube) | offen | [F57](prompts/F57-social-media-marketing.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 238 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Steuerrecht Österreich (inkl. Umsatzsteuer und Internationales) | offen | [F58](prompts/F58-steuerrecht-oesterreich.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 239 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Tax Technology (BMD, Excel, Power Query) | offen | [F59](prompts/F59-tax-technology.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 240 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Weiterbildungsfahrplan Steuerassistenz Österreich | offen | [F60](prompts/F60-weiterbildungsfahrplan-steuerassistenz-oesterrei.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
| 241 | C | Wirtschaft, Steuer, Marketing & Soft Skills | Wirtschaft und kaufmännische Grundlagen | offen | [F61](prompts/F61-wirtschaft-und-kaufmaennische-grundlagen.md) | – | `wirtschaft-und-steuer-uebungen` (geplant) |
<!-- TABELLE-ENDE -->

## Die 16 Fächer (K01–K16)

Neben den Prompts für neue Lehrpläne gibt es 16 Fächer, die schon als Lehrplan mit Skriptkapiteln vorliegen. Sie sind hier mit Typ, Modulen und Stunden erfasst, damit sie wie die Kurse oben geführt werden können. Die Modulübersicht je Fach liegt in `faecher/`; Übungsmaterial und Skripte stehen in eigenen Repositories (Spalte „Repository“, Eintrag in `daten/faecher.json`, Feld `repo`). Die Tabelle wird vom Skript erzeugt; nicht von Hand ändern.

<!-- FAECHER-START -->
16 Fächer: 9 Kern, 7 Erweiterung; zusammen 209 Module, ca. 2124,75 Stunden.

| Nr | Fach | Typ | Bereich | Module | Stunden | Voraussetzung | Repository |
|---|---|---|---|---|---|---|---|
| [K01](faecher/K01-linux-essentials.md) | Linux Essentials | Kern | Fundament | 12 | 96 | – | [linux-uebungen/linux-essentials](https://github.com/AnsibleArtisan4711/linux-uebungen/tree/main/linux-essentials) |
| [K02](faecher/K02-webdesign.md) | Webdesign (HTML, CSS, responsives Design) | Kern | Web | 21 | 294,5 | – | [web-uebungen/webdesign](https://github.com/AnsibleArtisan4711/web-uebungen/tree/main/webdesign) |
| [K03](faecher/K03-microsoft-excel-expert.md) | Microsoft Excel Expert | Kern | Daten & Office | 12 | 105 | Empfehlung: Office-Grundlagen (MOS, Erweiterung) | [office-uebungen/excel-expert](https://github.com/AnsibleArtisan4711/office-uebungen/tree/main/excel-expert) |
| [K04](faecher/K04-bash.md) | Bash | Kern | Scripting & Automatisierung | 12 | 124 | Linux Essentials | [automatisierung-uebungen/bash](https://github.com/AnsibleArtisan4711/automatisierung-uebungen/tree/main/bash) |
| [K05](faecher/K05-technische-dokumentation.md) | Technische Dokumentation & Dokumentations-Governance | Kern | Cloud, Doku & Business | 17 | 191,75 | – | [it-betrieb-uebungen/technische-dokumentation](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/technische-dokumentation) |
| [K06](faecher/K06-active-directory.md) | Active Directory | Kern | Windows & Microsoft | 12 | 134 | – | [windows-server-uebungen/active-directory](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/active-directory) |
| [K07](faecher/K07-python-automatisierung.md) | Python (Automatisierung unter Linux) | Kern | Scripting & Automatisierung | 15 | 150 | Bash | [automatisierung-uebungen/python-automatisierung](https://github.com/AnsibleArtisan4711/automatisierung-uebungen/tree/main/python-automatisierung) |
| [K08](faecher/K08-git-versionskontrolle.md) | Git & Versionskontrolle | Kern | Scripting & Automatisierung | 12 | 126 | Bash | [automatisierung-uebungen/git-versionskontrolle](https://github.com/AnsibleArtisan4711/automatisierung-uebungen/tree/main/git-versionskontrolle) |
| [K09](faecher/K09-powershell.md) | PowerShell | Kern | Windows & Microsoft | 12 | 126 | Bash | [automatisierung-uebungen/powershell](https://github.com/AnsibleArtisan4711/automatisierung-uebungen/tree/main/powershell) |
| [K10](faecher/K10-microsoft-office-specialist-associate.md) | Microsoft Office Specialist Associate | Erweiterung | Fundament | 12 | 100 | – | [office-uebungen/office-specialist-associate](https://github.com/AnsibleArtisan4711/office-uebungen/tree/main/office-specialist-associate) |
| [K11](faecher/K11-comptia-tech-itf.md) | CompTIA Tech+ / ITF+ | Erweiterung | Fundament | 12 | 87 | – | [client-hardware-uebungen/comptia-tech-itf](https://github.com/AnsibleArtisan4711/client-hardware-uebungen/tree/main/comptia-tech-itf) |
| [K12](faecher/K12-aws-cloud-practitioner.md) | AWS Cloud Practitioner | Erweiterung | Cloud, Doku & Business | 12 | 106 | – | [cloud-identitaet-uebungen/aws-cloud-practitioner](https://github.com/AnsibleArtisan4711/cloud-identitaet-uebungen/tree/main/aws-cloud-practitioner) |
| [K13](faecher/K13-webserver-apache-nginx.md) | Webserver (Apache HTTP Server & Nginx) | Erweiterung | Web | 14 | 165,5 | Webdesign, Linux Essentials | [web-uebungen/webserver](https://github.com/AnsibleArtisan4711/web-uebungen/tree/main/webserver) |
| [K14](faecher/K14-100-gruppenrichtlinien.md) | 100 Gruppenrichtlinien | Erweiterung | Windows & Microsoft | 10 | 100 | Active Directory | [windows-server-uebungen/gruppenrichtlinien](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/gruppenrichtlinien) |
| [K15](faecher/K15-m365-governance.md) | M365 Governance | Erweiterung | Windows & Microsoft | 12 | 109 | Active Directory (empfohlen) | [cloud-identitaet-uebungen/m365-governance](https://github.com/AnsibleArtisan4711/cloud-identitaet-uebungen/tree/main/m365-governance) |
| [K16](faecher/K16-unternehmensgruendung.md) | Unternehmensgründung | Erweiterung | Cloud, Doku & Business | 12 | 110 | – | [it-betrieb-uebungen/unternehmensgruendung](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/unternehmensgruendung) |
<!-- FAECHER-ENDE -->

## Die 6 Übungsreihen (E01–E06)

Eigene Übungsreihen, die nicht aus einem Lehrplan-Skript stammen: Homelab, Netzwerk, Active Directory, WLAN, Backup und USV. Aufbau und Umfang stehen in `uebungen/` und werden aus den Dateien der jeweiligen Repositories gelesen (`tools/uebungen_einlesen.py`). Die Tabelle wird vom Skript erzeugt; nicht von Hand ändern.

<!-- UEBUNGEN-START -->
| Nr | Übung | Thema | Module | Einheiten | Repository |
|---|---|---|---|---|---|
| [E01](uebungen/E01-multi-site-hybrid-cloud-ai-sec-lab.md) | Multi-Site Hybrid Cloud & AI-Sec Operations | Homelab und Betrieb | 14 | 92 | [it-betrieb-uebungen/homelab-multi-site](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/homelab-multi-site) |
| [E02](uebungen/E02-netzwerk-packet-tracer.md) | Netzwerktechnik mit Cisco Packet Tracer | Netzwerk | 8 | 37 | [netzwerk-und-firewall-uebungen/packet-tracer](https://github.com/AnsibleArtisan4711/netzwerk-und-firewall-uebungen/tree/main/packet-tracer) |
| [E03](uebungen/E03-benutzerverwaltung-active-directory.md) | Benutzerverwaltung im Active Directory | Windows und Active Directory | 1 | 1 | [windows-server-uebungen/ad-benutzerverwaltung](https://github.com/AnsibleArtisan4711/windows-server-uebungen/tree/main/ad-benutzerverwaltung) |
| [E04](uebungen/E04-wlan-gaestenetz.md) | WLAN und Gästenetz | Netzwerk | 2 | 2 | [netzwerk-und-firewall-uebungen/wlan-gaestenetz](https://github.com/AnsibleArtisan4711/netzwerk-und-firewall-uebungen/tree/main/wlan-gaestenetz) |
| [E05](uebungen/E05-backup-nas-veeam.md) | Backup auf NAS mit Veeam | Homelab und Betrieb | 2 | 2 | [storage-backup-uebungen/veeam-nas](https://github.com/AnsibleArtisan4711/storage-backup-uebungen/tree/main/veeam-nas) |
| [E06](uebungen/E06-geordnetes-herunterfahren-ohne-usv.md) | Geordnetes Herunterfahren ohne USV | Homelab und Betrieb | 1 | 1 | [it-betrieb-uebungen/usv-shutdown](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen/tree/main/usv-shutdown) |
<!-- UEBUNGEN-ENDE -->

## Empfohlene Reihenfolge

1. Priorität A zuerst: DNS, Windows-Server-Rollen, Virtualisierung, Netzwerkdienste, IT-Sicherheit und Monitoring.
2. Danach Priorität B, passend zu den vorhandenen Themen (Automatisierung zu PowerShell, Bash und Python; Azure zu Microsoft 365 Governance).
3. Priorität C nach Bedarf.

Schon vorhanden und deshalb nicht in der Liste: Active Directory, Gruppenrichtlinien, Microsoft 365, PowerShell, Bash, Python, Linux-Grundlagen, LPIC 1 bis 3, DHCP, DNSSEC, Netzwerktechnik, Webserver, Webdesign, Git, technische Dokumentation, Cloud-Grundlagen, IT-Grundlagen, Microsoft Office, Unternehmensgründung.

## Zuordnung zu den Themen-Repositories

Die Ausarbeitungen der Lehrpläne kommen in ein Repository je Themenbereich, je Kurs ein Ordner (Entscheidung vom 2026-11-11). Ein Repository entsteht mit dem ersten fertigen Kurs. Die Tabelle wird aus den Feldern `repo` und `ordner` in `daten/kurse.json` erzeugt; nicht von Hand ändern. Die Fächer K01–K16 und die Übungsreihen E01–E06 liegen in denselben Repositories, ihr Ordner steht in der Spalte „Repository“ der beiden anderen Tabellen.

Die Zuordnung ist ein Vorschlag. Offen sind vor allem Randfälle: Recht und Compliance (P47 bis P49) liegen vorläufig in `it-betrieb-uebungen`, Firewall und VPN (P08 bis P11) in `netzwerk-und-firewall-uebungen`, P54 und P55 (Linux-Dateidienste und LVM) in `storage-backup-uebungen`.

<!-- REPOS-START -->
| Repository | Kurse |
|---|---|
| [netzwerkdienste-uebungen](https://github.com/AnsibleArtisan4711/netzwerkdienste-uebungen) | P01 DNS-Grundlagen (Windows-DNS und BIND) (gepusht); P71 DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea) (gepusht); A20 DNS Security (DNSSEC) |
| [windows-server-uebungen](https://github.com/AnsibleArtisan4711/windows-server-uebungen) | P02 Dateidienste, DFS und Druckserver (gepusht); P03 WSUS und Update-Verwaltung (gepusht); P04 Zertifikatsdienste und PKI (AD CS) (gepusht); P59 Remotedesktopdienste (RDS) (gepusht); P61 Windows Admin Center (gepusht); A04 Microsoft Windows Server Hybrid Administrator; A07 Windows Server 2025; A09 LDAP |
| [virtualisierung-uebungen](https://github.com/AnsibleArtisan4711/virtualisierung-uebungen) | P05 Hyper-V Administration (gepusht); P06 Proxmox VE; P07 VMware vSphere und ESXi; P60 Failover-Clustering und Hochverfügbarkeit; A42 Virtualisierung (VMware vSphere/ESXi und Microsoft Hyper-V); A46 High Availability und Load Balancing |
| [netzwerk-und-firewall-uebungen](https://github.com/AnsibleArtisan4711/netzwerk-und-firewall-uebungen) | P08 Firewall mit OPNsense; P09 Linux-Firewall mit nftables und iptables; P10 VPN mit WireGuard und OpenVPN (gepusht); P11 Reverse Proxy, Lastverteilung und TLS; A19 Cisco CCNA; A22 Firewall, Netzwerkdesign und DMZ; A23 Netzwerktechnik; A24 Open-Source-Firewalls (IPFire und OPNsense); A25 Traffic Analysis (NetFlow, Wireshark, tcpdump); N07 BGP; N08 NAC (802.1X); N09 SD-WAN; N10 VoIP und QoS; N11 WLAN-Infrastruktur |
| [it-sicherheit-uebungen](https://github.com/AnsibleArtisan4711/it-sicherheit-uebungen) | P12 IT-Sicherheitsgrundlagen (gepusht); P13 Windows-Server-Härtung; P14 Linux-Server-Härtung; P15 Schwachstellenmanagement; P16 Kryptografie, Zertifikate und TLS (gepusht); P62 IDS und IPS mit Suricata; P63 Passwort- und Secrets-Verwaltung; P64 Penetrationstest-Grundlagen; A26 CompTIA Security+; A27 Cyber-Angriffe und Verteidigung; A29 Incident Response; A30 SIEM; A31 Schwachstellen-, Patch- und Änderungsmanagement; N14 Kali Linux; N15 Secrets Management und Vault-Konzepte; N16 Security Awareness und Phishing-Simulation; N17 Zero Trust Grundlagen: Identität, Geräte und Daten |
| `monitoring-logging-uebungen` (noch nicht angelegt) | P17 Monitoring mit Zabbix; P18 Monitoring mit Prometheus und Grafana; P19 Zentrales Logging mit Graylog und Elastic Stack; P20 Monitoring mit PRTG; P66 Windows Event Forwarding und Ereignisprotokolle; A51 Logmanagement; A52 Monitoring, Alerting und SLO/SLA/SLI |
| [automatisierung-uebungen](https://github.com/AnsibleArtisan4711/automatisierung-uebungen) | P21 Konfigurationsmanagement mit Ansible; P22 Infrastructure as Code mit Terraform; P23 cloud-init und VM-Vorlagen; P24 PowerShell Desired State Configuration (DSC); P65 CI/CD mit GitLab und Jenkins; A39 Ansible; N25 AWS Certified DevOps Engineer Professional; N26 CI/CD-Pipeline; N27 Google Professional Cloud DevOps Engineer; N28 Terraform |
| `container-uebungen` (noch nicht angelegt) | P25 Docker und Docker Compose; P26 Kubernetes-Grundlagen; P53 Podman und Container-Sicherheit; A40 Docker und Container (inkl. Nano-Images); A41 Kubernetes (Grundlagen und Betrieb) |
| [cloud-identitaet-uebungen](https://github.com/AnsibleArtisan4711/cloud-identitaet-uebungen) | P27 Azure Administration; P28 Entra ID und Hybrid-Identität; P29 Intune und Autopilot; P56 AWS Administration (SysOps); P57 Azure-Netzwerk und Azure-Sicherheit; P58 Google Cloud Grundlagen; A08 Conditional Access (CA); A10 MFA und Passwordless; A11 Microsoft Defender; A12 Microsoft MS-102; A13 Microsoft SC-300; A14 Privileged Identity Management; A32 AWS Certified CloudOps Engineer Associate; A33 AWS Certified Solutions Architect Associate; A34 Azure Virtual Desktop; A35 Google Associate Cloud Engineer; A36 Microsoft AZ-104; A37 Microsoft AZ-500; A38 Microsoft AZ-900 (Azure Fundamentals); N02 Copilot Readiness; N03 MS-900; N04 Microsoft Purview; N05 Microsoft SC-500; N06 Microsoft SC-900; N18 AWS Certified Advanced Networking Specialty; N19 AWS Certified Security Specialty; N20 Google Cloud Digital Leader; N21 Google Professional Cloud Network Engineer; N22 Google Professional Cloud Security Engineer; N23 Microsoft AZ-305; N24 Microsoft AZ-700 |
| [datenbanken-uebungen](https://github.com/AnsibleArtisan4711/datenbanken-uebungen) | P30 SQL-Grundlagen (gepusht); P31 MariaDB und PostgreSQL Administration; P32 SQL Server Administration; P67 NoSQL-Datenbanken und Redis; P68 Datenbank-Backup und -Wiederherstellung; A48 MS SQL; A49 MySQL (MariaDB); A50 PostgreSQL; N29 Google Professional Database Engineer; N30 MongoDB; N31 Redis |
| [storage-backup-uebungen](https://github.com/AnsibleArtisan4711/storage-backup-uebungen) | P33 NAS, SAN, iSCSI und RAID; P34 Btrfs, ZFS und Snapshots; P35 Backup-Konzept (3-2-1, RPO und RTO); P36 Notfallplanung und Disaster Recovery; P54 LVM und Dateisysteme unter Linux; P55 Dateidienste unter Linux mit Samba und NFS; A43 BCDR; A44 Backup, Restore und Ransomware Recovery; A45 File-Systeme; A47 Storage: SAN, NAS und Storage-Protokolle |
| `e-mail-uebungen` (noch nicht angelegt) | P37 Exchange Online Administration; P38 E-Mail-Authentifizierung: SPF, DKIM und DMARC; P39 Mailserver mit Postfix und Dovecot; A21 E-Mail-Routing, SMTP und Mail Security |
| [it-betrieb-uebungen](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen) | P40 ITIL 4 Grundlagen (gepusht); P41 Incident-, Problem- und Change-Management (gepusht); P42 Ticketsysteme in der Praxis (gepusht); P43 SLA und Betriebshandbuch (gepusht); P47 Datenschutz (DSGVO) in der IT (gepusht); P48 NIS2 für Administratoren (gepusht); P49 ISO 27001 Grundlagen (gepusht); P50 Troubleshooting-Methodik (gepusht); P51 Projektmanagement für Administratoren (gepusht); P52 IT-Englisch für Administratoren (gepusht); P69 Asset-Verwaltung und CMDB (gepusht); P70 Lizenzmanagement (gepusht); P72 Weiterbildung IT-Systemtechnik (Querschnitt nach der Lehre) (gepusht); A05 Weiterbildung IT Systemtechnik; A28 DSGVO; A53 Troubleshooting; A54 CMDB und Asset Management; N12 Compliance in Unternehmen; N13 IT-Risikomanagement; N32 Anwendungssupport; N33 Jira Service Management; N34 ServiceNow; N35 Vendor Management und Lizenzmanagement; N41 Confluence; N49 Anforderungsmanagement; N50 Kanban; N51 Projekt-Risikoregister und Issue Tracking; N52 Projektmanagement; N53 Scrum; F01 Open Source; F02 Stakeholder Management und Moderation |
| [client-hardware-uebungen](https://github.com/AnsibleArtisan4711/client-hardware-uebungen) | P44 PC-Hardware und Fehlersuche (gepusht); P45 Windows-11-Client-Administration (gepusht); P46 Betriebssystem-Rollout (MDT, MECM und Alternativen) (gepusht); A01 Betriebssysteme; A02 CompTIA A+; A03 Microsoft MD-102; A06 Windows Autopilot; N01 Registry und Treiber; N36 Arduino; N37 Elektrotechnik, Strom und Sicherheit; N38 Gerätetechnik; N39 Kabel und Stecker; N40 Raspberry Pi und Einplatinencomputer |
| [linux-uebungen](https://github.com/AnsibleArtisan4711/linux-uebungen) | A15 LPIC-1; A16 LPIC-2; A17 LPIC-3; A18 RHEL-Familie (Red Hat Enterprise Linux und AlmaLinux) |
| [office-uebungen](https://github.com/AnsibleArtisan4711/office-uebungen) | N42 LaTeX (inkl. MiKTeX, TeXstudio und Overleaf); N43 Microsoft Access Expert; N44 Microsoft Outlook Associate; N45 Microsoft PL-900 (Power Platform Fundamentals); N46 Microsoft PowerPoint Associate; N47 Microsoft Word Expert; N48 Power Platform Governance |
| [web-uebungen](https://github.com/AnsibleArtisan4711/web-uebungen) | N54 Apache Tomcat; F04 Adobe XD; F07 Angular; F08 Bootstrap; F11 GraphQL; F13 JavaScript; F15 Material 3; F17 PHP; F18 RESTful API; F19 React.js; F21 Vue.js; F22 XML; F46 E-Commerce: Zahlungsabwicklung; F50 Magento; F55 Search Engine Optimization; F56 Shopify |
| `programmierung-uebungen` (noch nicht angelegt) | F03 AWS Certified Developer Associate; F05 Algorithmen und Datenstrukturen; F06 Android; F09 C# und .NET; F10 C++; F12 Java; F14 Logik und diskrete Mathematik; F16 Mathematik (Grundlagen und Anwendung); F20 Visual Basic |
| `ki-und-daten-uebungen` (noch nicht angelegt) | F23 AWS Certified AI Practitioner; F24 AWS Certified Data Engineer Associate; F25 AWS Certified Generative AI Developer Professional; F26 AWS Certified Machine Learning Engineer Associate; F27 CompTIA Data+; F28 Google AI Studio; F29 Google Generative AI Leader; F30 Google Professional Data Engineer; F31 Google Professional Machine Learning Engineer; F32 KI-Ethik & Datenschutz; F33 Künstliche Intelligenz; F34 Large und Small Language Models; F35 Machine Learning und Data Science; F36 Microsoft AI-900; F37 Microsoft DP-900; F38 Pandas; F39 Prompt Engineering; F40 TensorFlow |
| `wirtschaft-und-steuer-uebungen` (noch nicht angelegt) | F41 Bankenwesen; F42 Bilanzbuchhalterprüfung Österreich; F43 Buchhalterprüfung Österreich; F44 Business Management; F45 Controlling und Reporting; F47 IT-Controlling; F48 Kommunikation; F49 Kundenorientierung; F51 Marketing; F52 Microsoft Dynamics 365; F53 Personalverrechnung Österreich; F54 SAP; F57 Social Media Marketing (LinkedIn, Meta und YouTube); F58 Steuerrecht Österreich (inkl. Umsatzsteuer und Internationales); F59 Tax Technology (BMD, Excel, Power Query); F60 Weiterbildungsfahrplan Steuerassistenz Österreich; F61 Wirtschaft und kaufmännische Grundlagen |
<!-- REPOS-ENDE -->

## Entstehung

Die Prompts und das Erzeugungsskript wurden gemeinsam mit Claude (Anthropic) entworfen. Die Kurse, die Reihenfolge und die Entscheidungen, was daraus ein Lehrplan wird, liegen bei mir. Prüfen muss man weiterhin die Ergebnisse der Gem, nicht nur die Prompts.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `prompts/` | ein Prompt pro Kurs (erzeugt, nicht von Hand bearbeiten) |
| `uebungen/` | Aufbau je Übungsreihe E01–E06 (erzeugt, nicht von Hand bearbeiten) |
| `faecher/` | Modulübersicht je Fach K01–K16 (erzeugt, nicht von Hand bearbeiten) |
| `lehrplaene/` | die fertigen, geprüften Lehrpläne (Markdown, mit Prüfvermerk am Ende); Ausarbeitungen zu Übungen liegen in eigenen Repositories |
| `daten/kurse.json` | Quelle der Kurse: Titel, Themen, Abgrenzung, Fokus-Technologien, Vorkenntnisse, Labor-Ressourcen, Hinweis, Status, Themen-Repository (`repo`) und Kursordner (`ordner`, sobald gepusht) |
| `daten/uebungen.json` | Quelle der 6 Übungsreihen E01–E06: Titel, Thema, Repository, lokaler Ordner und der aus den Repositories gelesene Aufbau |
| `daten/faecher.json` | Quelle der 16 Fächer K01–K16: Typ, Bereich, Voraussetzung, Stunden, Module mit Stunden, Repository |
| `daten/rahmen.json` | gemeinsame Angaben: Umfang, Standard-Abgrenzung, erlaubte Status |
| `daten/topics.json` | GitHub-Topics je Themen-Repository (gemeinsame und fachliche Topics) für `tools/topics_setzen.py` |
| `rahmen/prompt-vorlage.txt` | Variablen-Vorlage aller Prompts mit Platzhaltern |
| `gem/grundanweisung.md` | Grundanweisung der Gem (von Hand einzufügen) |
| `gem/vorlage-variablen.md` | leere Vorlage für einen eigenen Kurs-Prompt |
| `tools/build_prompts.py` | erzeugt `prompts/`, `faecher/`, `uebungen/` und die vier Tabellen (Kurse, Fächer, Übungsreihen, Zuordnung zu den Repositories) |
| `tools/uebungen_einlesen.py` | liest den Aufbau der Übungsreihen E01–E06 aus ihren lokalen Repository-Ordnern in `daten/uebungen.json` |
| `tools/umsetzung_anlegen.py` | legt aus einem Lehrplan einen Umsetzungsordner an (Checklisten, Protokolle, Ablage für Screenshots) |
| `tools/bilder_index.py` | erzeugt `bilder-index.md` mit allen Bildern eines Umsetzungsordners; meldet unverlinkte, fehlende und große Bilder |
| `tools/topics_setzen.py` | setzt GitHub-Topics bei Repositories ohne Topics (Trockenlauf, `--anwenden` zum Setzen; braucht die GitHub-CLI `gh`) |
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
- **Kurs ändern oder ergänzen:** Eintrag in `daten/kurse.json` bearbeiten oder am Ende anfügen (nächste freie ID, `slug` in Kleinbuchstaben ohne Umlaute), `repo` ist Pflicht (Themen-Repository, siehe Zuordnung oben). Ist ein Kurs gepusht, `status` auf „gepusht“ setzen und `ordner` (Kursordner im Repository) eintragen, dann Skript laufen lassen.
- **Fach ändern oder ergänzen:** Eintrag in `daten/faecher.json` bearbeiten (Repository-Name in `repo` eintragen, sobald das Repository existiert), Skript laufen lassen.
- **Übungsreihe ändern oder ergänzen:** Eintrag in `daten/uebungen.json` anpassen (Feld `lokal` = Ordner des Repositories), dann `python tools/uebungen_einlesen.py` und `python tools/build_prompts.py`.
- **Umsetzung vorbereiten:** `python tools/umsetzung_anlegen.py P46` (oder `K01`, `E03`) legt neben dem Repository den Ordner `Umsetzung/P46-<slug>/` an, mit einem Unterordner je Modul (`checkliste.md`, `protokoll.md`, `fehlerprotokoll.md`, `screenshots/`, `notizen/`, `ausgaben/`), einer Übersicht, einer Liste der Befehle mit „nicht bestätigt“ und einem Abschlussordner. Ein zweiter Parameter wählt einen anderen Zielordner. Vorhandene Dateien werden nicht überschrieben.
- **Bilder indizieren:** `python tools/bilder_index.py` (Standard: `D:\Umsetzung`) oder mit Ordner als Parameter schreibt `bilder-index.md` in diesen Ordner: Tabelle aller verlinkten Bilder mit Modul, Abschnitt, Beschreibung, Größe und Link, dazu unverlinkte Bilder, Links auf fehlende Bilder und Bilder über 1 MB.
- **GitHub-Topics setzen:** `python tools/topics_setzen.py` zeigt als Trockenlauf, was gesetzt würde; `python tools/topics_setzen.py --anwenden` setzt die Topics aus `daten/topics.json`. Repositories, die schon Topics haben, bleiben unverändert; Repositories ohne Eintrag in `daten/topics.json` werden nur gemeldet. Voraussetzung: GitHub-CLI, angemeldet mit `gh auth login`.
- **Qualität:** Die Prompts verlangen Versions- und Lizenzstände mit Datum. Diese Angaben im fertigen Lehrplan stichprobenartig gegen die Herstellerdokumentation prüfen.

## Lizenz

Texte (Prompts, Vorlage, Daten, Lehrpläne): CC BY 4.0, siehe [LICENSE-DOCS.md](LICENSE-DOCS.md). Skript `tools/build_prompts.py`: MIT, siehe [LICENSE](LICENSE).
