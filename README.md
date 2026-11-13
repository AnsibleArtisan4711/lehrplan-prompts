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
Stand der 72 Kurse: 44 offen, 0 Lehrplan erstellt, 0 aufbereitet, 28 gepusht.

Bedeutung der Status:

- **offen**: Der Prompt liegt vor, ein Lehrplan ist noch nicht erstellt.
- **Lehrplan erstellt**: Der Lehrplan ist erstellt und von mir geprüft. Er liegt in `lehrplaene/` und ist in der Spalte „Lehrplan“ verlinkt.
- **aufbereitet**: Aus dem Lehrplan ist Übungsmaterial ausgearbeitet, aber noch nicht veröffentlicht.
- **gepusht**: Das Übungsmaterial liegt als Kursordner in einem Themen-Repository auf GitHub, das in der Spalte „Repository“ verlinkt wird.

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
| [netzwerkdienste-uebungen](https://github.com/AnsibleArtisan4711/netzwerkdienste-uebungen) | P01 DNS-Grundlagen (Windows-DNS und BIND) (gepusht); P71 DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea) (gepusht) |
| [windows-server-uebungen](https://github.com/AnsibleArtisan4711/windows-server-uebungen) | P02 Dateidienste, DFS und Druckserver (gepusht); P03 WSUS und Update-Verwaltung (gepusht); P04 Zertifikatsdienste und PKI (AD CS) (gepusht); P59 Remotedesktopdienste (RDS) (gepusht); P61 Windows Admin Center (gepusht) |
| [virtualisierung-uebungen](https://github.com/AnsibleArtisan4711/virtualisierung-uebungen) | P05 Hyper-V Administration (gepusht); P06 Proxmox VE; P07 VMware vSphere und ESXi; P60 Failover-Clustering und Hochverfügbarkeit |
| [netzwerk-und-firewall-uebungen](https://github.com/AnsibleArtisan4711/netzwerk-und-firewall-uebungen) | P08 Firewall mit OPNsense; P09 Linux-Firewall mit nftables und iptables; P10 VPN mit WireGuard und OpenVPN (gepusht); P11 Reverse Proxy, Lastverteilung und TLS |
| [it-sicherheit-uebungen](https://github.com/AnsibleArtisan4711/it-sicherheit-uebungen) | P12 IT-Sicherheitsgrundlagen (gepusht); P13 Windows-Server-Härtung; P14 Linux-Server-Härtung; P15 Schwachstellenmanagement; P16 Kryptografie, Zertifikate und TLS (gepusht); P62 IDS und IPS mit Suricata; P63 Passwort- und Secrets-Verwaltung; P64 Penetrationstest-Grundlagen |
| `monitoring-logging-uebungen` (noch nicht angelegt) | P17 Monitoring mit Zabbix; P18 Monitoring mit Prometheus und Grafana; P19 Zentrales Logging mit Graylog und Elastic Stack; P20 Monitoring mit PRTG; P66 Windows Event Forwarding und Ereignisprotokolle |
| [automatisierung-uebungen](https://github.com/AnsibleArtisan4711/automatisierung-uebungen) | P21 Konfigurationsmanagement mit Ansible; P22 Infrastructure as Code mit Terraform; P23 cloud-init und VM-Vorlagen; P24 PowerShell Desired State Configuration (DSC); P65 CI/CD mit GitLab und Jenkins |
| `container-uebungen` (noch nicht angelegt) | P25 Docker und Docker Compose; P26 Kubernetes-Grundlagen; P53 Podman und Container-Sicherheit |
| [cloud-identitaet-uebungen](https://github.com/AnsibleArtisan4711/cloud-identitaet-uebungen) | P27 Azure Administration; P28 Entra ID und Hybrid-Identität; P29 Intune und Autopilot; P56 AWS Administration (SysOps); P57 Azure-Netzwerk und Azure-Sicherheit; P58 Google Cloud Grundlagen |
| [datenbanken-uebungen](https://github.com/AnsibleArtisan4711/datenbanken-uebungen) | P30 SQL-Grundlagen (gepusht); P31 MariaDB und PostgreSQL Administration; P32 SQL Server Administration; P67 NoSQL-Datenbanken und Redis; P68 Datenbank-Backup und -Wiederherstellung |
| [storage-backup-uebungen](https://github.com/AnsibleArtisan4711/storage-backup-uebungen) | P33 NAS, SAN, iSCSI und RAID; P34 Btrfs, ZFS und Snapshots; P35 Backup-Konzept (3-2-1, RPO und RTO); P36 Notfallplanung und Disaster Recovery; P54 LVM und Dateisysteme unter Linux; P55 Dateidienste unter Linux mit Samba und NFS |
| `e-mail-uebungen` (noch nicht angelegt) | P37 Exchange Online Administration; P38 E-Mail-Authentifizierung: SPF, DKIM und DMARC; P39 Mailserver mit Postfix und Dovecot |
| [it-betrieb-uebungen](https://github.com/AnsibleArtisan4711/it-betrieb-uebungen) | P40 ITIL 4 Grundlagen (gepusht); P41 Incident-, Problem- und Change-Management (gepusht); P42 Ticketsysteme in der Praxis (gepusht); P43 SLA und Betriebshandbuch (gepusht); P47 Datenschutz (DSGVO) in der IT (gepusht); P48 NIS2 für Administratoren (gepusht); P49 ISO 27001 Grundlagen (gepusht); P50 Troubleshooting-Methodik (gepusht); P51 Projektmanagement für Administratoren (gepusht); P52 IT-Englisch für Administratoren (gepusht); P69 Asset-Verwaltung und CMDB (gepusht); P70 Lizenzmanagement (gepusht); P72 Weiterbildung IT-Systemtechnik (Querschnitt nach der Lehre) (gepusht) |
| [client-hardware-uebungen](https://github.com/AnsibleArtisan4711/client-hardware-uebungen) | P44 PC-Hardware und Fehlersuche (gepusht); P45 Windows-11-Client-Administration (gepusht); P46 Betriebssystem-Rollout (MDT, MECM und Alternativen) (gepusht) |
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
| `rahmen/prompt-vorlage.txt` | Variablen-Vorlage aller Prompts mit Platzhaltern |
| `gem/grundanweisung.md` | Grundanweisung der Gem (von Hand einzufügen) |
| `gem/vorlage-variablen.md` | leere Vorlage für einen eigenen Kurs-Prompt |
| `tools/build_prompts.py` | erzeugt `prompts/`, `faecher/`, `uebungen/` und die vier Tabellen (Kurse, Fächer, Übungsreihen, Zuordnung zu den Repositories) |
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
- **Kurs ändern oder ergänzen:** Eintrag in `daten/kurse.json` bearbeiten oder am Ende anfügen (nächste freie ID, `slug` in Kleinbuchstaben ohne Umlaute), `repo` ist Pflicht (Themen-Repository, siehe Zuordnung oben). Ist ein Kurs gepusht, `status` auf „gepusht“ setzen und `ordner` (Kursordner im Repository) eintragen, dann Skript laufen lassen.
- **Fach ändern oder ergänzen:** Eintrag in `daten/faecher.json` bearbeiten (Repository-Name in `repo` eintragen, sobald das Repository existiert), Skript laufen lassen.
- **Übungsreihe ändern oder ergänzen:** Eintrag in `daten/uebungen.json` anpassen (Feld `lokal` = Ordner des Repositories), dann `python tools/uebungen_einlesen.py` und `python tools/build_prompts.py`.
- **Umsetzung vorbereiten:** `python tools/umsetzung_anlegen.py P46` (oder `K01`, `E03`) legt neben dem Repository den Ordner `Umsetzung/P46-<slug>/` an, mit einem Unterordner je Modul (`checkliste.md`, `protokoll.md`, `fehlerprotokoll.md`, `screenshots/`, `notizen/`, `ausgaben/`), einer Übersicht, einer Liste der Befehle mit „nicht bestätigt“ und einem Abschlussordner. Ein zweiter Parameter wählt einen anderen Zielordner. Vorhandene Dateien werden nicht überschrieben.
- **Bilder indizieren:** `python tools/bilder_index.py` (Standard: `D:\Umsetzung`) oder mit Ordner als Parameter schreibt `bilder-index.md` in diesen Ordner: Tabelle aller verlinkten Bilder mit Modul, Abschnitt, Beschreibung, Größe und Link, dazu unverlinkte Bilder, Links auf fehlende Bilder und Bilder über 1 MB.
- **Qualität:** Die Prompts verlangen Versions- und Lizenzstände mit Datum. Diese Angaben im fertigen Lehrplan stichprobenartig gegen die Herstellerdokumentation prüfen.

## Lizenz

Texte (Prompts, Vorlage, Daten, Lehrpläne): CC BY 4.0, siehe [LICENSE-DOCS.md](LICENSE-DOCS.md). Skript `tools/build_prompts.py`: MIT, siehe [LICENSE](LICENSE).
