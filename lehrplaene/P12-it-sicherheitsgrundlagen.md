# Lehrplan: IT-Sicherheitsgrundlagen

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger, angehende Systemtechniker/Systemadministratoren (AT/EU) |
| **Vorkenntnisse** | IT-Grundlagen, Netzwerk-Grundlagen (IP-Adressen, Subnetze nach RFC 1918 / RFC 4193) |
| **Gesamtumfang** | 12 Module, 116 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | OS-unabhängige Security-Basics, Windows (Server/11), Linux (Ubuntu/Debian) |
| **Thematische Abgrenzung (Out of Scope)** | Keine Tiefenkonfiguration von Active Directory oder komplexem Routing (Verweis auf dedizierte Lehrpläne für M365/AD und Advanced Networking). Keine Penetration-Testing-Zertifizierung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Einführung in die IT-Sicherheit & Schutzziele | 1 | 6 |
| 2 | Bedrohungslandschaft & Angriffsarten | 1 | 10 |
| 3 | Grundlagen der Kryptografie | 1 | 10 |
| 4 | Identitäts- und Zugriffsverwaltung (IAM) | 1 | 10 |
| 5 | Netzwerksicherheit & Segmentierung | 1 | 12 |
| 6 | Endgerätesicherheit & Härtung | 1 | 12 |
| 7 | Sichere Anwendungs- und Dienstkonfiguration | 1 | 10 |
| 8 | Risikomanagement & Schwachstellenbewertung | 2 | 8 |
| 9 | Sicherheitsrichtlinien, Compliance & Awareness | 2 | 8 |
| 10 | Überwachung, Logging & Diagnosewerkzeuge | 1 | 12 |
| 11 | Vorfallbehandlung (Incident Response) & Notfallplanung | 1 | 8 |
| 12 | Praktische Sicherheitsprüfung & Troubleshooting | 2 | 10 |
| **Gesamt** | **12 Module (9x Pflicht, 3x Vertiefung)** | | **116** |

*Hinweis zur Priorisierung: Module der Priorität 1 (Pflicht) vermitteln unverzichtbare Kernkompetenzen. Module der Priorität 2 (Vertiefung) ergänzen diese um fortgeschrittene oder prozessorientierte Konzepte und können bei Zeitmangel gekürzt werden.*

### 2. Quellen
* **CompTIA Security+ (SY0-701) Certification Exam Objectives**, CompTIA, Stand nicht geprüft, `https://www.comptia.org/certifications/security` *(URL nicht geprüft)*
* **ISO/IEC 27001:2022**, International Organization for Standardization (ISO), Stand 2022, `https://www.iso.org/standard/27001` *(URL nicht geprüft)*
* **BSI IT-Grundschutz-Kompendium**, Bundesamt für Sicherheit in der Informationstechnik (BSI), Edition 2023, `https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html` *(URL nicht geprüft)*
* **RFC 1918 - Address Allocation for Private Internets**, IETF, 1996, `https://datatracker.ietf.org/doc/html/rfc1918` *(URL nicht geprüft)*
* **RFC 4193 - Unique Local IPv6 Unicast Addresses**, IETF, 2005, `https://datatracker.ietf.org/doc/html/rfc4193` *(URL nicht geprüft)*
* **Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung, DSGVO)**, Europäische Union, 2016, `https://eur-lex.europa.eu/eli/reg/2016/679/oj` *(URL nicht geprüft)*
* **Common Vulnerability Scoring System (CVSS)**, FIRST.Org, Version nicht bestätigt, `https://www.first.org/cvss/` *(URL nicht geprüft)*
* **CIS Benchmarks**, Center for Internet Security, Stand nicht geprüft, `https://www.cisecurity.org/cis-benchmarks` *(URL nicht geprüft)*

### 3. Labor-Setup & Rahmenbedingungen
Folgende Testumgebung ist für die Durchführung der Praxisaufgaben zwingend **erforderlich** (ab Modul 3):
* **Virtualisierung:** Hyper-V (lokal).
* **Netzwerk:** Ein isolierter virtueller Hyper-V-Switch (Typ „Privat“, Name `vSwitch-Sec-Privat`). Keine Verbindung zum Heimnetz, Router oder produktiven DHCP/DNS. Alle IP-Adressen (RFC 1918, Netz `192.168.50.0/24`, ohne Standardgateway) werden statisch vergeben: `VM-WIN-SRV` `192.168.50.10`, `VM-LINUX` `192.168.50.20`, `VM-WIN-CLIENT` `192.168.50.30`.
* **VM 1 (`VM-WIN-SRV`, Windows Server):** Windows Server 2022 (Evaluationsversion, kostenlos). Einsatz als lokaler Dateiserver (Ordnerfreigabe) und Ziel der Firewall-, Rechte- und Logging-Übungen.
* **VM 2 (`VM-LINUX`, Linux Server):** Ubuntu Server 24.04 LTS (oder aktuelles Debian, Open Source). Einsatz als SSH-Server, Webserver (Apache) und für Netzwerkdiagnosen (Nmap).
* **VM 3 (`VM-WIN-CLIENT`, Windows Client):** Windows 11 Enterprise (Evaluationsversion). Einsatz als simulierter Arbeitsplatz (Gruppenrichtlinien, RDP- und SSH-Client, Wireshark).
* **Zusatzsoftware:** Wireshark (Open Source, inklusive Npcap, auf `VM-WIN-CLIENT`), Nmap (Open Source, auf `VM-LINUX`), OpenSSL (in Linux integriert), OpenSSH-Server und Apache HTTP Server (`apache2`) auf `VM-LINUX`, OpenSSH-Client (in Windows 11 enthalten).
* **Vorbereitung vor Modul 3 (erforderlich, einmalig mit Internetzugang):** Das Labor selbst hat kein Internet, die Software muss deshalb vorher installiert werden. (a) Laden Sie auf dem Hyper-V-Host den Wireshark-Installer (enthält Npcap) herunter, aktivieren Sie in `VM-WIN-CLIENT` den Gastdienst (`Enable-VMIntegrationService -Name 'Guest Service Interface' -VMName VM-WIN-CLIENT`), kopieren Sie den Installer per `Copy-VMFile` in die VM und installieren Sie ihn dort. (b) Verbinden Sie `VM-LINUX` kurzzeitig mit einem Switch, der Internetzugang bietet, aber keine Dienste des Heimnetzes erreicht (z. B. der Hyper-V-„Default Switch“ unter Windows 10/11; Verfügbarkeit nicht bestätigt), und installieren Sie `sudo apt update && sudo apt install openssh-server apache2 nmap`. Stellen Sie danach den Adapter auf `vSwitch-Sec-Privat` um und setzen Sie die statische Adresse. Erst dann beginnt die isolierte Laborarbeit.
* **Einschränkung:** Es wird ausdrücklich **keine Active-Directory-Domäne** bereitgestellt. Alle Konfigurationen (Berechtigungen, Richtlinien) erfolgen als lokale Workgroup-Setups (Lokale Benutzer, Local Group Policy), um die Komplexität auf reine Security-Grundlagen zu fokussieren.
* **Kurse ohne technisches Labor:** Module 1, 2, 8, 9 und 11 sind stark konzeptionell ausgeprägt. Praxisaufgaben in diesen Modulen bestehen aus Dokumentations-, Analyse- oder Fallstudien-Aufgaben; die VMs sind dafür nicht zwingend eingeschaltet.

---

## B. Detaillierter Modulaufbau

### Modul 1: Einführung in die IT-Sicherheit & Schutzziele
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die primären Schutzziele (Vertraulichkeit, Integrität, Verfügbarkeit) definieren und anhand von Beispielen aus der Praxis erklären.
  * Der Lernende kann die grundlegenden Konzepte von Authentifizierung, Autorisierung und Accounting (AAA) unterscheiden.
* **Voraussetzungen:** Keine.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Das CIA-Triad (Confidentiality, Integrity, Availability) | 2 |
| 1.2 | Erweitertes Schutzziel-Modell (Zurechenbarkeit, Authentizität) | 2 |
| 1.3 | Einführung in das AAA-Konzept | 2 |
#### Praxisaufgaben (Hands-on Lab)
*(Kein technisches Labor nötig)*
1. **Fallstudie CIA-Analyse:** Gegeben ist ein Szenario eines fiktiven Krankenhauses (`med.example.com`). Identifiziere für drei gegebene IT-Systeme (Patientenakte, öffentlicher Webserver, Backup-Archiv) die Gewichtung von Vertraulichkeit, Integrität und Verfügbarkeit und dokumentiere diese in einer Matrix.
#### Kontrollfragen
1. Welches der CIA-Schutzziele wird verletzt, wenn ein Angreifer eine Webseite defaced (den sichtbaren Text manipuliert)?
2. Worin besteht der Unterschied zwischen Authentifizierung und Autorisierung im AAA-Modell?
3. Warum ist das Schutzziel "Verfügbarkeit" für einen industriellen Steuerungs-PC (ICS) oft wichtiger als "Vertraulichkeit"?
4. Was wird beim Accounting im AAA-Modell protokolliert, und warum setzt Nachvollziehbarkeit eindeutige Benutzerkonten voraus?

### Modul 2: Bedrohungslandschaft & Angriffsarten
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann gängige Malware-Arten klassifizieren (Ransomware, Trojaner, Rootkits).
  * Der Lernende kann Netzwerk- und Social-Engineering-Angriffe erkennen und deren Vektor beschreiben.
* **Voraussetzungen:** Modul 1.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Malware-Typologien (Viren, Würmer, Ransomware, Spyware) | 3 |
| 2.2 | Social Engineering & Phishing (Tailgating, Vishing, Spear-Phishing) | 3 |
| 2.3 | Netzwerk- und Applikationsangriffe (DoS/DDoS, MITM, SQLi, XSS im Überblick) | 4 |
#### Praxisaufgaben (Hands-on Lab)
*(Kein technisches Labor nötig)*
1. **Phishing-Analyse:** Analysiere drei bereitgestellte (ausgedruckte oder als PDF simulierte) E-Mail-Kopfzeilen und Nachrichtentexte auf typische Indikatoren für Phishing (Dringlichkeit, falsche Absender-Domänen, verdächtige Links).
2. **Bedrohungs-Mapping:** Ordne 10 beschriebene Angriffs-Szenarien den Kategorien Social Engineering, Malware oder Netzwerkangriff zu und benenne die spezifische Angriffsart.
#### Kontrollfragen
1. Was unterscheidet einen Wurm in seiner Verbreitungsweise von einem klassischen Computervirus?
2. Wie funktioniert ein Man-in-the-Middle (MITM) Angriff auf konzeptioneller Ebene?
3. Welches psychologische Druckmittel wird beim Social Engineering am häufigsten eingesetzt, um eine schnelle Reaktion des Opfers zu erzwingen?

### Modul 3: Grundlagen der Kryptografie
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann die Unterschiede zwischen symmetrischer und asymmetrischer Verschlüsselung sowie Hashing erklären.
  * Der Lernende kann Prüfsummen generieren, um die Integrität einer Datei zu verifizieren.
* **Voraussetzungen:** Modul 1; Labor-VMs müssen installiert und über Hyper-V erreichbar sein.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Konzepte: Hashing, Salting und digitale Signaturen | 3 |
| 3.2 | Symmetrische vs. asymmetrische Verschlüsselungsverfahren (AES, RSA) | 3 |
| 3.3 | Public Key Infrastructure (PKI) und Zertifikate im Überblick | 4 |
#### Praxisaufgaben (Hands-on Lab)
1. **Hashing (Linux):** Erstelle auf der Linux-VM eine Textdatei. Generiere mit `sha256sum` einen Hash. Ändere ein Zeichen in der Datei und generiere den Hash erneut, um den Avalanche-Effekt zu dokumentieren.
2. **Hashing (Windows):** Führe den gleichen Integritätstest auf der Windows-11-VM mit dem PowerShell-Cmdlet `Get-FileHash` durch.
3. **Schlüsselgenerierung (Linux):** Generiere mit `openssl` ein asymmetrisches RSA-Schlüsselpaar (`openssl genrsa -out private.pem 3072`, `openssl rsa -in private.pem -pubout -out public.pem`, `chmod 600 private.pem`) und prüfe die Dateien mit `openssl rsa -in private.pem -noout -check`. Dieses Paar dient nur der Demonstration; für den SSH-Zugang erzeugst du in Modul 7 ein eigenes SSH-Schlüsselpaar.
#### Kontrollfragen
1. Warum eignet sich Hashing nicht, um geheime Nachrichten sicher zu übertragen und später wieder im Klartext zu lesen?
2. Welcher Schlüssel (Public oder Private) wird bei asymmetrischer Kryptografie verwendet, um eine digitale Signatur zu erstellen?
3. Welche Aufgabe erfüllt eine Certification Authority (CA) in einer PKI?

### Modul 4: Identitäts- und Zugriffsverwaltung (IAM)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann das Principle of Least Privilege (PoLP) anwenden.
  * Der Lernende kann lokale Dateisystemberechtigungen in Windows und Linux vergeben und Audits durchführen.
* **Voraussetzungen:** Modul 1.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | IAM-Konzepte: MFA, Single Sign-On (SSO), Passwortrichtlinien | 3 |
| 4.2 | Zugriffsmodelle: Discretionary (DAC), Mandatory (MAC) und Role-Based (RBAC) | 3 |
| 4.3 | Datei- und Freigabeberechtigungen (NTFS vs. ext4/POSIX) | 4 |
#### Praxisaufgaben (Hands-on Lab)
1. **Windows NTFS RBAC:** Erstelle auf `VM-WIN-SRV` drei lokale Benutzer (MitarbeiterA, MitarbeiterB, AdminX) und zwei lokale Gruppen (HR, IT); MitarbeiterA gehört zu HR, MitarbeiterB und AdminX gehören zu IT. Lege die Ordner `C:\Daten\HR-Dokumente` und `C:\Daten\IT-Intern` an, deaktiviere die Vererbung auf `C:\Daten` und konfiguriere die NTFS-Berechtigungen so, dass „HR“ auf `HR-Dokumente` nur Leserechte hat, „IT“ auf beide Ordner Vollzugriff besitzt und „HR“ auf `IT-Intern` keinen Zugriff hat. Prüfe die effektiven Rechte mit `icacls` und mit der Registerkarte „Effektiver Zugriff“.
2. **Linux POSIX Permissions:** Lege auf `VM-LINUX` zwei Benutzer (`anna`, `ben`) und eine Gruppe `projekt` an (nur `anna` ist Mitglied). Erstelle das Verzeichnis `/srv/projekt`, weise den Besitz (`chown`) der Gruppe `projekt` zu und setze `chmod 750`, um Zugriffe für „Others“ strikt zu unterbinden. Teste den Zugriff beider Benutzer (`sudo -u ben ls /srv/projekt` muss mit „Permission denied“ scheitern).
3. **Freigabe und effektive Berechtigung:** Gib `C:\Daten\HR-Dokumente` auf `VM-WIN-SRV` als SMB-Freigabe `Dokumente` aus (Freigabeberechtigung „Ändern“ für alle, Konto „Jeder“ bzw. „Everyone“). Verbinde dich von `VM-WIN-CLIENT` aus (`net use \\192.168.50.10\Dokumente /user:VM-WIN-SRV\MitarbeiterA`) und weise nach, dass MitarbeiterA lesen, aber nicht schreiben kann, weil die restriktivere NTFS-Berechtigung gilt.
4. **Soll-Zustand dokumentieren (Audit-Grundlage):** Speichere den Soll-Zustand in Dateien: `icacls C:\Daten /T > Soll-NTFS.txt` auf `VM-WIN-SRV` und `ls -lR /srv/projekt > soll-posix.txt` auf `VM-LINUX`. Diese Dateien sind die Vergleichsbasis für das Audit in Modul 12.
#### Kontrollfragen
1. Welchen Sicherheitsvorteil bietet Multi-Faktor-Authentifizierung (MFA) gegenüber komplexen Kennwörtern?
2. Warum sollten Berechtigungen in Windows bevorzugt an Gruppen statt an einzelne Benutzerkonten vergeben werden?
3. Was bedeutet der Linux-Rechtewert `chmod 644` für Besitzer, Gruppe und den Rest der Welt?

### Modul 5: Netzwerksicherheit & Segmentierung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann eine Host-basierte Firewall einrichten und spezifische Ports blockieren oder freigeben.
  * Der Lernende versteht das Konzept von Netzwerkzonen (DMZ, Intranet) und VPNs.
* **Voraussetzungen:** Grundlagen in IPv4 (Subnetting, RFC 1918). VMs müssen über den privaten Switch kommunizieren können.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Firewalls: Stateless, Stateful, NGFW und Host-basierte Firewalls | 4 |
| 5.2 | Netzwerksegmentierung, VLANs, DMZ und Zero Trust-Konzepte | 4 |
| 5.3 | VPN, IPSec und Intrusion Detection/Prevention (IDS/IPS) | 4 |
#### Praxisaufgaben (Hands-on Lab)
1. **Windows Defender Firewall (Erweitert):** Aktiviere auf `VM-WIN-SRV` zuerst den Remotedesktop (Einstellungen oder `Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 0`). Deaktiviere die vordefinierten Regeln „Remotedesktop“, damit nur deine eigene Regel gilt. Konfiguriere danach eine eingehende Regel, die RDP (TCP-Port 3389) nur von der IP-Adresse `192.168.50.30` (`VM-WIN-CLIENT`) zulässt (z. B. `New-NetFirewallRule -DisplayName 'RDP nur von Client' -Direction Inbound -Protocol TCP -LocalPort 3389 -RemoteAddress 192.168.50.30 -Action Allow`), und eine Regel, die ICMPv4-Echoanforderungen blockiert (`New-NetFirewallRule -DisplayName 'ICMPv4 blockieren' -Direction Inbound -Protocol ICMPv4 -IcmpType 8 -Action Block`). Teste von `VM-WIN-CLIENT` aus: `ping 192.168.50.10` schlägt fehl, `Test-NetConnection 192.168.50.10 -Port 3389` ist erfolgreich. *Hinweis: Dokumentiere diese Regeln genau, sie bleiben für spätere Diagnosen (Modul 12) aktiv.*
2. **Linux UFW (Uncomplicated Firewall):** Erlaube auf `VM-LINUX` zuerst SSH (Port 22) und HTTP (Port 80) (`sudo ufw allow 22/tcp`, `sudo ufw allow 80/tcp`), setze die Standardrichtlinie auf „Deny Incoming“ (`sudo ufw default deny incoming`) und aktiviere erst danach die UFW (`sudo ufw enable`), damit eine bestehende SSH-Sitzung nicht abbricht. Prüfe mit `sudo ufw status verbose`.
3. **Soll-Zustand sichern:** Speichere `Get-NetFirewallRule -Direction Inbound -Enabled True | Format-Table DisplayName, Action > Soll-Firewall.txt` auf `VM-WIN-SRV` und `sudo ufw status verbose > soll-ufw.txt` auf `VM-LINUX` als Vergleichsbasis für Modul 12.
#### Kontrollfragen
1. Was ist der Hauptunterschied zwischen einer zustandslosen (Stateless) und einer zustandsbehafteten (Stateful) Firewall?
2. Welchen Zweck erfüllt eine Demilitarisierte Zone (DMZ) in der Netzwerkarchitektur?
3. Warum ist die Filterung von Outbound-Traffic (Egress-Filtering) wichtig im Kampf gegen Malware?
4. Worin unterscheiden sich ein Site-to-Site-VPN und ein Remote-Access-VPN, und welche Aufgabe übernimmt IPsec dabei?

### Modul 6: Endgerätesicherheit & Härtung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann ein Betriebssystem durch Deaktivierung nicht benötigter Dienste härten (Attack Surface Reduction).
  * Der Lernende versteht Patch-Management-Konzepte.
* **Voraussetzungen:** Modul 4 (Benutzer und Berechtigungen).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Konzepte der Systemhärtung (OS-Hardening, Baselining, CIS Benchmarks) | 4 |
| 6.2 | Patch- und Schwachstellenmanagement | 4 |
| 6.3 | Mobile Device Management (MDM) & Endpoint Detection (EDR) im Überblick | 4 |
#### Praxisaufgaben (Hands-on Lab)
1. **Windows Local Group Policy:** Nutze `gpedit.msc` auf dem Windows-11-Client. Erzwinge eine Passwortrichtlinie (min. 12 Zeichen) und deaktiviere die automatische Wiedergabe (AutoPlay) für Wechselmedien.
2. **Dienste-Härtung (Windows):** Identifiziere auf `VM-WIN-CLIENT` in der `services.msc` zwei laufende, nicht essenzielle Windows-Dienste (z. B. Xbox-Zubehörverwaltung, Print Spooler bei Systemen ohne Drucker), notiere ihren Ausgangszustand und setze sie auf „Deaktiviert“. Mache die Änderung am Ende der Übung für den Print Spooler wieder rückgängig, falls du später drucken möchtest.
3. **Linux Härtung:** Überprüfe auf `VM-LINUX` in `/etc/fstab` die Mount-Optionen, deaktiviere einen nicht benötigten Dienst mittels `systemctl disable` (z. B. `cups`, falls installiert; `ssh` und `apache2` bleiben aktiv) und prüfe mit `sudo passwd -S root`, dass das root-Konto gesperrt ist (Status `L`).
4. **Patch-Plan erstellen:** Dokumentiere den Patch-Stand der drei VMs (`Get-HotFix` auf den Windows-VMs, `uname -r` und `lsb_release -a` auf `VM-LINUX`) und erstelle einen einseitigen Patch-Plan mit Testgruppe, Wartungsfenster, Reihenfolge und Rückfallplan.
#### Kontrollfragen
1. Was ist das Ziel des "Baselining" in der Endgerätesicherheit?
2. Warum ist die Deaktivierung von AutoPlay/AutoRun eine effektive Härtungsmaßnahme?
3. Welche Rolle spielt ein MDM bei der Absicherung mobiler Endgeräte (Smartphones)?
4. Worin unterscheiden sich Patch-Management und Schwachstellenmanagement, und warum werden Patches vor dem Roll-out an einer Testgruppe geprüft?

### Modul 7: Sichere Anwendungs- und Dienstkonfiguration
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann Administrationsdienste (wie SSH) sicher konfigurieren (Key-based Auth).
  * Der Lernende kennt die Bedeutung von TLS für sichere Datenübertragung.
* **Voraussetzungen:** Modul 3 (Konzept asymmetrischer Schlüssel), Modul 5 (Firewall-Freigaben).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Sichere vs. unsichere Protokolle (HTTP vs. HTTPS, Telnet vs. SSH) | 3 |
| 7.2 | Absicherung von Remotedesktop und SSH | 4 |
| 7.3 | Web-Sicherheit: TLS, Zertifikatsverwaltung und sichere Header (Theorie) | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Key-based Authentication einrichten (Passwort-Login noch aktiv):** Prüfe auf `VM-LINUX`, dass der SSH-Dienst läuft (`systemctl status ssh`). Erzeuge auf `VM-WIN-CLIENT` ein SSH-Schlüsselpaar (`ssh-keygen -t ed25519`), übertrage den öffentlichen Schlüssel nach `~/.ssh/authorized_keys` des Benutzers `anna` (z. B. `type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh anna@192.168.50.20 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"`), setze auf `VM-LINUX` die Rechte (`chmod 700 ~/.ssh`, `chmod 600 ~/.ssh/authorized_keys`) und teste den Login mit Schlüssel in einer zweiten Sitzung.
2. **SSH-Härtung (Linux):** Erst nachdem der Schlüssel-Login funktioniert und eine Sitzung offen ist: Konfiguriere den SSH-Daemon (`/etc/ssh/sshd_config`) auf `VM-LINUX`: `PermitRootLogin no` und `PasswordAuthentication no`. Prüfe die Syntax mit `sudo sshd -t`, lade den Dienst neu (`sudo systemctl reload ssh`) und weise nach, dass der Schlüssel-Login weiter funktioniert und der Passwort-Login scheitert (`ssh -o PubkeyAuthentication=no anna@192.168.50.20` → „Permission denied“). Diese Härtung bleibt für die Module 10 und 12 bestehen.
3. **Absicherung von Remotedesktop (Windows):** Prüfe auf `VM-WIN-SRV`, dass die Netzwerkebenen-Authentifizierung (NLA) für RDP aktiv ist (`(Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp').UserAuthentication` ergibt `1`). Nimm nur `MitarbeiterA` in die Gruppe „Remotedesktopbenutzer“ auf und weise von `VM-WIN-CLIENT` aus nach, dass `MitarbeiterA` sich verbinden kann, `MitarbeiterB` jedoch abgewiesen wird.
#### Kontrollfragen
1. Warum sollte Telnet in modernen Netzwerken niemals für die Administration eingesetzt werden?
2. Welche Parameter in der `sshd_config` müssen gesetzt werden, um Brute-Force-Angriffe auf Passwörter effektiv auszuschließen?
3. Wie schützt TLS vor Man-in-the-Middle (MITM) Angriffen?

### Modul 8: Risikomanagement & Schwachstellenbewertung
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann Risiken quantitativ und qualitativ bewerten.
  * Der Lernende versteht das Common Vulnerability Scoring System (CVSS) zur Einstufung von Schwachstellen.
* **Voraussetzungen:** Modul 1 und 2.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Risikobegriffe: Assets, Bedrohungen, Schwachstellen, Eintrittswahrscheinlichkeit | 3 |
| 8.2 | Risikobehandlung: Akzeptieren, Vermeiden, Übertragen, Vermindern | 2 |
| 8.3 | Schwachstellen-Scans, Penetration Testing und CVSS-Scoring | 3 |
#### Praxisaufgaben (Hands-on Lab)
*(Kein technisches Labor nötig)*
1. **CVSS-Analyse:** Gegeben ist ein fiktiver Schwachstellenbericht mit drei CVEs (inklusive Basis-Vektoren). Bewerte, welche Schwachstelle zuerst gepatcht werden muss, basierend auf dem CVSS-Score und dem System-Kontext (z. B. extern erreichbarer Webserver vs. interner Printserver).
2. **Risikobewertung (qualitativ und quantitativ):** Bewerte für die drei Systeme aus Modul 1 je ein Risiko in einer Risikomatrix (Eintrittswahrscheinlichkeit 1 bis 5 mal Auswirkung 1 bis 5). Berechne für ein Risiko quantitativ: Assetwert 50.000 €, Expositionsfaktor 40 %, jährliche Eintrittsrate 0,5; bestimme SLE und ALE (Kontrollwert: ALE = 10.000 €) und ordne eine Behandlungsstrategie zu.
#### Kontrollfragen
1. Wie unterscheidet sich eine "Schwachstelle" (Vulnerability) von einer "Bedrohung" (Threat)?
2. Welche vier Möglichkeiten hat ein Unternehmen im Umgang mit einem identifizierten Risiko (Risikobehandlung)?
3. Was sagt der CVSS-Score einer Schwachstelle über deren Schweregrad aus?
4. Wie berechnet sich die Annualized Loss Expectancy (ALE) aus SLE und jährlicher Eintrittsrate, und wofür ist sie nützlich?

### Modul 9: Sicherheitsrichtlinien, Compliance & Awareness
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kennt Rahmenwerke wie ISO/IEC 27001 und BSI IT-Grundschutz im Überblick.
  * Der Lernende versteht die Relevanz der DSGVO für IT-Prozesse und die Wichtigkeit von Mitarbeiter-Awareness.
* **Voraussetzungen:** Modul 8.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | IT-Sicherheitsrichtlinien (AUP, Passwort Policy, Clean Desk Policy) | 3 |
| 9.2 | Compliance & Rahmenwerke (ISO 27001, BSI IT-Grundschutz, DSGVO) | 3 |
| 9.3 | Security Awareness Programme und Schulungskonzepte | 2 |
#### Praxisaufgaben (Hands-on Lab)
*(Kein technisches Labor nötig)*
1. **Richtlinien-Entwurf:** Skizziere eine kurze, prägnante Acceptable Use Policy (AUP) (max. 1 Seite) für die Nutzung privater USB-Sticks im fiktiven Unternehmen `example.org`, inklusive der Folgen bei Zuwiderhandlung.
#### Kontrollfragen
1. Was ist der Hauptzweck eines Information Security Management Systems (ISMS) gemäß ISO 27001?
2. Warum sind rein technische Schutzmaßnahmen ohne regelmäßige Awareness-Schulungen der Mitarbeiter unzureichend?
3. Welche Grundprinzipien schreibt die DSGVO (z.B. Datensparsamkeit, Zweckbindung) bei der Verarbeitung personenbezogener Daten vor?
4. Welche Rolle spielen die Bausteine und Anforderungen des BSI IT-Grundschutz-Kompendiums bei der Umsetzung von Sicherheitsmaßnahmen?

### Modul 10: Überwachung, Logging & Diagnosewerkzeuge
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann Systemlogs auf Anomalien analysieren.
  * Der Lernende kann mit Wireshark Netzwerktraffic mitschneiden und grundlegend interpretieren.
* **Voraussetzungen:** Windows und Linux VMs lauffähig, Basis-Konfigurationen aus M4-M7 vorhanden.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Logging-Konzepte: Syslog, Windows Event Logs, Log-Aggregation (SIEM) | 4 |
| 10.2 | Event Viewer und `/var/log` Analyse in der Praxis | 4 |
| 10.3 | Netzwerk-Sniffing und Paketanalyse mit Wireshark | 4 |
#### Praxisaufgaben (Hands-on Lab)
1. **Windows Event Logs:** Stelle sicher, dass die Überwachung fehlgeschlagener Anmeldungen aktiv ist (lokale Sicherheitsrichtlinie, Überwachung „Anmelden“: Fehler; Menünamen nicht bestätigt). Simuliere 5 fehlgeschlagene Anmeldeversuche für `MitarbeiterA` am Anmeldebildschirm von `VM-WIN-SRV` (Konsole der VM) mit falschem Kennwort. Suche anschließend im Event Viewer (Security Log) nach der Event ID 4625. Extrahiere den Benutzernamen und den Zeitpunkt der Versuche.
2. **Linux Syslog:** Erzeuge auf der Linux-VM bewusste Fehler (z. B. Aufruf eines nicht existierenden Dienstes, fehlgeschlagener `su`-Versuch) und analysiere `auth.log` und `syslog` mittels `grep` und `tail`, um die Vorfälle zu rekonstruieren.
3. **Wireshark PCAP:** Starte Wireshark auf `VM-WIN-CLIENT` (Capture-Filter `host 192.168.50.20`). Führe einen Ping sowie einen unverschlüsselten HTTP-Aufruf auf den Apache-Webserver von `VM-LINUX` durch (`curl http://192.168.50.20`). Stoppe den Mitschnitt, analysiere die Pakete und weise die Klartextdaten (HTTP, „Follow TCP Stream“) nach. Vergleiche mit einer SSH-Verbindung zu `VM-LINUX`, deren Inhalt nicht lesbar ist.
#### Kontrollfragen
1. Warum ist es kritisch, dass Log-Dateien auf einem zentralen, gehärteten Server (Log-Aggregator) gesammelt werden, statt nur lokal auf den Endgeräten zu verbleiben?
2. Welche Windows Event ID signalisiert einen erfolgreichen Login (Logon)?
3. Auf welchem OSI-Layer operiert Wireshark primär, wenn es IP-Pakete auswertet?

### Modul 11: Vorfallbehandlung (Incident Response) & Notfallplanung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kennt die Phasen des Incident Response Life Cycles.
  * Der Lernende versteht den Unterschied zwischen Business Continuity Planning (BCP) und Disaster Recovery (DRP).
* **Voraussetzungen:** Modul 10 (Modul 8 und 9 werden empfohlen, sind aber nicht zwingend).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Der Incident Response Prozess (Vorbereitung, Erkennung, Eindämmung, Beseitigung, Wiederherstellung, Lessons Learned) | 4 |
| 11.2 | Business Continuity (BCP) und Disaster Recovery (DRP) | 2 |
| 11.3 | Backup-Strategien (3-2-1-Regel, RTO vs. RPO) | 2 |
#### Praxisaufgaben (Hands-on Lab)
*(Kein technisches Labor nötig)*
1. **Tabletop-Übung (Ransomware):** Entwirf für ein Szenario, in dem der Windows-File-Server aus Modul 4 verschlüsselt wurde, einen Schritt-für-Schritt-Reaktionsplan. Benenne explizit Maßnahmen zur sofortigen Eindämmung (Containment) auf Netzwerkebene (Trennen vom vSwitch) und ordne jede Maßnahme in einer Tabelle einer der sechs Phasen des Incident-Response-Prozesses zu.
#### Kontrollfragen
1. Was ist der wichtigste erste Schritt in der "Eindämmungs-Phase" (Containment) bei einem aktiven Wurm-Befall im Netzwerk?
2. Definiere Recovery Time Objective (RTO) und Recovery Point Objective (RPO).
3. Wie funktioniert die 3-2-1-Backup-Regel?
4. Worin unterscheiden sich Business Continuity Planning (BCP) und Disaster Recovery Planning (DRP), und welches umfasst das andere?

### Modul 12: Praktische Sicherheitsprüfung & Troubleshooting
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Der Lernende kann einen simplen Port-Scan durchführen und die Ergebnisse gegen bestehende Firewall-Regeln evaluieren.
  * Der Lernende kann Fehlkonfigurationen in lokalen Berechtigungen identifizieren und beheben.
* **Voraussetzungen:** Abschluss der Module 3 bis 7 und 10 (Modul 8 und 9 sind nicht nötig). Alle drei VMs laufen im Netz `vSwitch-Sec-Privat`.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Grundlagen der Aufklärung (Reconnaissance) und Scanning (Nmap) | 4 |
| 12.2 | Troubleshooting: Identifikation von Firewall- und Zugriffsproblemen | 3 |
| 12.3 | Lab-Challenge: Auffinden und Schließen vorbereiteter Lücken | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Port-Scanning (Nmap):** Führe von `VM-LINUX` aus (nur gegen die eigene Lab-VM) einen Scan gegen den Windows-Server durch: `nmap -Pn -p 22,80,445,3389 192.168.50.10` (`-Pn`, weil der Ping blockiert ist). Überprüfe das Ergebnis im Kontext der in Modul 5 gesetzten Regeln. *Nachweis: Ping schlägt fehl und alle gescannten Ports erscheinen als „filtered“, auch 3389, da RDP nur von `192.168.50.30` erlaubt ist. Von `VM-WIN-CLIENT` aus ist `Test-NetConnection 192.168.50.10 -Port 3389` dagegen erfolgreich.* Erkläre den Unterschied.
2. **Berechtigungs-Audit und Lab-Challenge:** Nimm (oder ein Kollege nimmt) auf den Systemen folgende vorbereitete Änderungen vor: (a) `VM-WIN-SRV`: Gruppe HR erhält Vollzugriff auf `C:\Daten\HR-Dokumente`; (b) `VM-WIN-SRV`: die RDP-Regel erlaubt `RemoteAddress Any`; (c) `VM-LINUX`: `chmod 777 /srv/projekt`; (d) `VM-LINUX`: `sudo ufw allow 23/tcp`. Identifiziere die Abweichungen ohne Blick auf die Änderungen, indem du die Ausgaben mit den Soll-Dateien aus Modul 4 und 5 vergleichst (`Compare-Object (Get-Content Soll-NTFS.txt) (icacls C:\Daten /T)`, `diff` bei `ls -lR` und `ufw status verbose`), setze den Soll-Zustand wieder her und dokumentiere jede Abweichung mit Befund, Risiko und Korrektur.
#### Kontrollfragen
1. Welche Information liefert der Nmap-Status "Filtered" für einen bestimmten Port?
2. Warum schlägt ein Ping-Befehl bei einer Standard-Installation von Windows Server oft fehl, selbst wenn der Server online ist?
3. Wie unterscheidet sich Troubleshooting im Security-Kontext von klassischem Netzwerk-Troubleshooting?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Die erste Fassung wurde geprüft und an den folgenden Stellen geändert. Stundensummen, Prioritäten und Modulreihenfolge blieben unverändert (12 Module, 116 UE).

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| A.2 | DSGVO, CVSS und CIS Benchmarks ergänzt; Prüfstatus bei RFCs; Stand der Security+-Ziele auf „nicht geprüft“ | Im Text genannt, aber nicht in der Quellenliste; Datum ungeprüft |
| A.3 | IP-Plan, VM-Namen, Switch-Name; Software (Wireshark, Nmap, SSH-Server, Apache) und Vorbereitungsschritt mit Internetzugang | Adressen und Software fehlten, das isolierte Labor hat kein Internet |
| Modul 1 | Kontrollfrage 4 (Accounting) | AAA-Lernziel war nur teilweise geprüft |
| Modul 3, Aufgabe 3 | Befehle und Hinweis, dass das SSH-Schlüsselpaar erst in Modul 7 entsteht | Der OpenSSL-Schlüssel war für SSH nicht verwendbar |
| Modul 4 | Gruppenzuordnung, Ordner, Test der Rechte; neue Aufgaben 3 (Freigabe) und 4 (Soll-Zustand) | Lerneinheit 4.3 und Lernziel „Audits“ hatten keine Praxis |
| Modul 5 | RDP aktivieren, genaue Regeln, Test; UFW in sicherer Reihenfolge; Aufgabe 3 (Soll-Zustand); Kontrollfrage 4 (VPN) | RDP lief nie, VPN-Lernziel war ungeprüft |
| Modul 6 | Voraussetzung korrigiert; Aufgabe 2 und 3 präzisiert; Aufgabe 4 (Patch-Plan); Kontrollfrage 4 | Patch-Management-Lernziel war ungeprüft |
| Modul 7 | Reihenfolge der Aufgaben vertauscht (erst Schlüssel-Login, dann Passwort aus), SSH-Schlüssel auf dem Client erzeugt; neue Aufgabe 3 (RDP/NLA) | Aussperr-Risiko, Schlüssel lag auf dem falschen System, Lerneinheit 7.2 ohne RDP-Übung |
| Modul 8 | Aufgabe 2 (Risikomatrix, SLE und ALE), Kontrollfrage 4 | Lernziel „quantitativ und qualitativ“ war ungeprüft |
| Modul 9 | Kontrollfrage 4 (BSI) | BSI-Teil des Lernziels war ungeprüft |
| Modul 10 | Audit-Richtlinie, Konsolenanmeldung, Webserver und Capture-Filter, Vergleich mit SSH | Webserver wurde nie installiert, Ablauf unklar |
| Modul 11 | Pflichtmodul hängt nur noch von Modul 10 ab; Phasenzuordnung; Kontrollfrage 4 (BCP und DRP) | Pflichtmodul setzte optionale Module voraus; Lernziele nur teilweise geprüft |
| Modul 12 | Voraussetzungen ohne Modul 8 und 9; Nmap-Nachweis korrigiert; Audit mit festgelegten Änderungen und Soll-Dateien | Der Nachweis widersprach den Firewall-Regeln aus Modul 5, die „vorbereiteten Lücken“ waren nicht festgelegt |

**Hinweise und offene Punkte:**

* Alle neu ergänzten Befehle wurden nur gegen den Wissensstand geprüft, **nicht im Labor ausgeführt**. Vor Kursstart zu prüfen: `Copy-VMFile` und Gastdienst, Verfügbarkeit des Hyper-V-„Default Switch“, RDP-Registrierungswert und Regel-Namen der Firewall, Gruppenname „Remotedesktopbenutzer“, Befehl zur Übertragung des SSH-Schlüssels in PowerShell, Menünamen der Überwachungsrichtlinie, `nmap`-Ergebnis „filtered“.
* Das Material für die Aufgaben „Phishing-Analyse“ (Modul 2), „Bedrohungs-Mapping“ (Modul 2) und „CVSS-Analyse“ (Modul 8) – drei E-Mails, zehn Szenarien, ein Schwachstellenbericht – ist nicht Teil dieses Lehrplans und muss beim Erstellen des Skripts entstehen.
* Modul 12 ist als Priorität 2 geführt, enthält aber die Audit- und Scanübungen; die Einstufung wurde nicht geändert.