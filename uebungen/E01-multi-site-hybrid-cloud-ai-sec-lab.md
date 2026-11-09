# E01 – Multi-Site Hybrid Cloud & AI-Sec Operations

- Thema: Homelab und Betrieb
- Repository: [multi-site-hybrid-cloud-ai-sec-lab](https://github.com/AnsibleArtisan4711/multi-site-hybrid-cloud-ai-sec-lab)
- Umfang: 14 Module, davon 14 mit Material; 92 Einheiten

## Modul 0: Mission Control (Strategie & Architektur)

| Step | Thema |
|---|---|
| 0.1 | Topologie-Design |
| 0.2 | Namenskonvention |
| 0.3 | Ressourcen-Planung (RAM Allocation) |
| 0.4 | Domain-Strategie |
| 0.5 | Lizenz-Management |
| 0.6 | Phasen-Definition (Meilensteine) |
| 0.7 | Sicherheitskonzept (AD Tier-Modell) |

## Modul 1: Virtualisierung & Storage-Meisterschaft

| Step | Thema |
|---|---|
| 1.1 | Hyper-V Setup & vSwitch Konfiguration |
| 1.2 | NAS Storage Architektur (UGreen DXP4800) |
| 1.3 | Storage Tiering & NVMe-Caching (UGreen DXP4800) |
| 1.4 | Netzwerk-Speicher (iSCSI & SMB) Bereitstellung |
| 1.5 | SD-Card Nutzung & NAS Virtualisierung |
| 1.6 | VM-Provisioning (Gen2 & Secure Boot) |
| 1.7 | Dynamischer RAM (Dynamic Memory Tuning) |

## Modul 2: Standortvernetzung & Routing (OPNsense)

| Step | Thema |
|---|---|
| 2.1 | Firewall Installation (OPNsense) |
| 2.2 | Interface-Konfiguration (WAN, LAN, DMZ) |
| 2.3 | Site-to-Site VPN (WireGuard) |
| 2.4 | Routing-Test & Tunnel-Verifizierung |
| 2.5 | DMZ-Konfiguration & Isolation |
| 2.6 | Firewall-Regelwerk & Basisschutz |
| 2.7 | NAT/Port-Forwarding & Webserver-Zugriff |

## Modul 3: Multi-Site Active Directory

| Step | Thema |
|---|---|
| 3.1 | PDC Promotion (Forest Setup) |
| 3.2 | SDC Promotion (Site Replication) |
| 3.3 | Active Directory Sites & Services |
| 3.4 | Replikations-Tuning & Site-Link Konfiguration |
| 3.5 | DNS Split-Brain Konfiguration |
| 3.6 | FSMO-Rollen & Verifizierung |
| 3.7 | Global Catalog (GC) Konfiguration |

## Modul 4: Die virtuelle DMZ & Web-Hosting

| Step | Thema |
|---|---|
| 4.1 | Ubuntu Server Setup (DMZ) |
| 4.2 | Apache Webserver & Test-Website |
| 4.3 | DMZ Hardening & Netzwerk-Isolation |
| 4.4 | Zertifikate (Let’s Encrypt) & SSL-Verschlüsselung |
| 4.5 | Management-Zugriff, Whitelisting & Reverse Proxy |
| 4.6 | Deployment-Prozess (Updates & Web-Content) |
| 4.7 | Live-Test & Split-Brain DNS Verifizierung |

## Modul 5: Windows & Linux Client Integration

| Step | Thema |
|---|---|
| 5.1 | Windows 11 AD-Join (HQ Client) |
| 5.2 | Edubuntu (Linux) AD-Join |
| 5.3 | GPO: Basis-Security (Kennwort & Bildschirmsperre) |
| 5.4 | GPO: File Shares (Automatische Netzlaufwerke) |
| 5.5 | LAPS Implementierung (Local Administrator Password Solution) |
| 5.6 | Linux AD-Logins (Test & Verifizierung) |
| 5.7 | Sudo-Rechte via AD (Gruppenbasierte Vergabe) |

## Modul 6: Hybrid Identity & Microsoft 365

| Step | Thema |
|---|---|
| 6.1 | UPN-Suffix Config & Tenant-Schutzkonzept |
| 6.2 | Entra Connect Setup (Dedizierter Sync-Server) |
| 6.3 | Password Hash Sync (PHS) & Seamless SSO |
| 6.4 | Selektiver Sync (Organisationseinheiten-Filterung) |
| 6.5 | Microsoft 365 Lizenz-Zuweisung |
| 6.6 | Exchange Online Postfach-Test (End-to-End) |
| 6.7 | SharePoint Online & Team-Site Zugriff |

## Modul 7: Log-Aggregation & Event Management

| Step | Thema |
|---|---|
| 7.1 | Windows Event Forwarding (Staging auf DC-01) |
| 7.2 | Syslog auf OPNsense (Export zum Kali-Hub) |
| 7.3 | Linux Log Export (rsyslog zum Kali-Hub) |
| 7.4 | Zentraler Speicherort (Kali-SIEM & Share-Setup) |
| 7.5 | Log-Formatierung (KI-Readiness & Strukturierung) |
| 7.6 | Erweiterte Überwachungsrichtlinien (Audit Policies) |
| 7.7 | Datenbereinigung (Noise-Filtering & AI-Ready Data) |

## Modul 8: AI Ops – Log-Analyse mit Ollama (Highlight)

| Step | Thema |
|---|---|
| 8.1 | Kali Linux Setup (KI-Plattform & SIEM-Hub) |
| 8.2 | Ollama Installation & Modell-Management |
| 8.3 | Python API-Anbindung (Automatisierte Analyse) |
| 8.4 | Prompt Engineering (Bedrohungserkennung mit LLMs) |
| 8.5 | Automatisierter Feed (Echtzeit-KI-Analyse) |
| 8.6 | Alarmierung & Benachrichtigung (Incident Response) |
| 8.7 | Simulation & Verifizierung (KI-Attack-Test) |

## Modul 9: Security Audits & Penetration Testing

| Step | Thema |
|---|---|
| 9.1 | Vulnerability Scanning (OpenVAS / GVM) |
| 9.2 | Vulnerability Audits: Nmap Sweeps & Port-Scans |
| 9.3 | AD Enumeration & Rechte-Analyse (BloodHound) |
| 9.4 | Passwort-Tests (Brute-Force & Offline Cracking) |
| 9.5 | Web-App Security (Apache & DMZ Audit) |
| 9.6 | Intrusion Detection & Prevention (Suricata) |
| 9.7 | Blue Team vs. Red Team (Purple Teaming & KI-Audit) |

## Modul 10: Backup & Disaster Recovery (3-2-1-0)

| Step | Thema |
|---|---|
| 10.1 | Veeam Backup & Replication (Installation & Setup) |
| 10.2 | NAS als Primary Repository & Erster Backup-Job |
| 10.3 | Backup-Jobs (Tägliche inkrementelle Sicherung) |
| 10.4 | Sekundär-Speicher (A:) & Cloud-Gateway (Google Drive) |
| 10.5 | Backup Copy Job & Cloud-Verschlüsselung |
| 10.6 | Disaster Recovery Test (Instant VM Recovery) |
| 10.7 | Active Directory Item-Level Recovery (Veeam Explorer) |

## Modul 11: M365 Business Basic Deep Dive

| Step | Thema |
|---|---|
| 11.1 | Exchange Online Admin (Shared Mailboxes) |
| 11.2 | Microsoft Teams Governance (Erstellung & Gäste) |
| 11.3 | SharePoint Berechtigungen (Abgleich mit lokalen Shares) |
| 11.4 | Basic Mobility & Security (Mobile Device Management) |
| 11.5 | Security Defaults & MFA (Überprüfung der Anmeldesicherheit) |
| 11.6 | PowerShell für M365 (MS Graph Automatisierung) |
| 11.7 | Spam- & Phishing-Filter (Defender Basiseinstellungen) |

## Modul 12: Dokumentation, Lifecycle & Übergabe

| Step | Thema |
|---|---|
| 12.1 | Executive Summary & Projekt-Tabellen |
| 12.2 | Systemhandbuch: AD, GPOs & Backup-Dokumentation |
| 12.3 | AI-Projektbericht (Ollama SIEM & Analyse-Ergebnisse) |
| 12.4 | Notfall-Plan (Disaster Recovery Runbook) |
| 12.5 | Lizenz-Übersicht & IT-Kostenrechnung (TCO) |
| 12.6 | Übergabe-Protokoll (Cleanup & Dauer-Admins) |
| 12.7 | Lessons Learned & Kritische Selbstreflexion |

## Anhang: Anhang: Exkurs – Windows Server Remote Management & Admin-Tools

| Step | Thema |
|---|---|
| A | Anhang: Exkurs – Windows Server Remote Management & Admin-Tools |

Aufbau gelesen aus den Dateien des Repositories (`python tools/uebungen_einlesen.py`).
Umsetzungsordner anlegen: `python tools/umsetzung_anlegen.py E01`
