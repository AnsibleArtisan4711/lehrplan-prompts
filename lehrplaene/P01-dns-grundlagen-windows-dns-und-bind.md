# Lehrplan: DNS-Grundlagen (Windows-DNS und BIND)

| Parameter | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze, OSI-Schichtenmodell, grundlegende Bedienung von Windows- und Linux-Kommandozeilen) |
| **Gesamtumfang** | 12 Module, 112 Unterrichtseinheiten (UE zu je 45 Minuten) |
| **Fokus-Technologien** | Windows Server (DNS-Server-Rolle, PowerShell-Modul `DnsServer`), Debian GNU/Linux bzw. Ubuntu Server mit ISC BIND 9 (`named`) |
| **Thematische Abgrenzung (Out of Scope)** | DNSSEC und DHCP sind eigene vorhandene Lehrpläne und werden nur konzeptionell bzw. an den direkten Schnittstellen kurz verwiesen; Active-Directory-Integration wird ausschließlich insoweit behandelt, wie sie für das Verständnis und den Betrieb von DNS-Zonen nötig ist. |

---

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| **1** | Grundlagen der Namensauflösung und DNS-Architektur | 1 | 8 |
| **2** | Installation und Grundkonfiguration des Windows-DNS-Servers | 1 | 8 |
| **3** | Installation und Grundkonfiguration von ISC BIND 9 unter Linux | 1 | 10 |
| **4** | Zonentypen im Detail: Primäre, Sekundäre und Stub-Zonen | 1 | 10 |
| **5** | Ressourceneinträge (Resource Records) in Forward- und Reverse-Zonen | 1 | 12 |
| **6** | Zonenübertragung (AXFR/IXFR) und plattformübergreifende Replikation | 1 | 10 |
| **7** | Weiterleitungen, bedingte Weiterleitungen, Caching und TTL-Steuerung | 1 | 8 |
| **8** | Dynamische DNS-Updates (DDNS) und Active-Directory-integrierte Zonen | 1 | 10 |
| **9** | Split-Brain-DNS (Split-Horizon), BIND Views und Windows DNS Policies | 2 | 10 |
| **10** | DNS-Sicherheit im Grundbetrieb, Härtung und Abgrenzung zu DNSSEC | 2 | 8 |
| **11** | Systematische Fehlersuche, Diagnose und Monitoring (Windows & Linux) | 1 | 10 |
| **12** | Integriertes Abschlussprojekt: Hybride DNS-Infrastruktur (Windows & BIND 9) | 2 | 8 |
| **Gesamt** | **12 Module (9x Priorität 1, 3x Priorität 2)** | **1: 86 UE / 2: 26 UE** | **112** |

*Hinweis zur Priorisierung:* Module der **Priorität 1 (Pflicht / Kernkompetenz, 86 UE)** vermitteln die unverzichtbaren Grundlagen für den täglichen Betrieb, die Einrichtung und die Entstörung von DNS-Diensten in gemischten Windows- und Linux-Umgebungen. Module der **Priorität 2 (Vertiefung / Optional, 26 UE)** behandeln erweiterte Architekturen (Split-Brain-DNS), spezifische Härtungsmaßnahmen wie Response Rate Limiting sowie ein umfassendes Abschlussprojekt zur Vorbereitung auf komplexe Unternehmensszenarien.

### 2. Quellen

* **RFC 1034 – Domain Names - Concepts and Facilities**, Herausgeber: IETF (P. Mockapetris), Datum: November 1987, URL: https://datatracker.ietf.org/doc/html/rfc1034 (Stand: geprüft)
* **RFC 1035 – Domain Names - Implementation and Specification**, Herausgeber: IETF (P. Mockapetris), Datum: November 1987, URL: https://datatracker.ietf.org/doc/html/rfc1035 (Stand: geprüft)
* **RFC 1918 – Address Allocation for Private Internets**, Herausgeber: IETF (Y. Rekhter et al.), Datum: Februar 1996, URL: https://datatracker.ietf.org/doc/html/rfc1918 (Stand: geprüft)
* **RFC 1995 – Incremental Zone Transfer in DNS**, Herausgeber: IETF (M. Ohta), Datum: August 1996, URL: https://datatracker.ietf.org/doc/html/rfc1995 (Stand: geprüft)
* **RFC 1996 – A Mechanism for Prompt Notification of Zone Changes (DNS NOTIFY)**, Herausgeber: IETF (P. Vixie), Datum: August 1996, URL: https://datatracker.ietf.org/doc/html/rfc1996 (Stand: geprüft)
* **RFC 2136 – Dynamic Updates in the Domain Name System (DNS UPDATE)**, Herausgeber: IETF (P. Vixie et al.), Datum: April 1997, URL: https://datatracker.ietf.org/doc/html/rfc2136 (Stand: geprüft)
* **RFC 2181 – Clarifications to the DNS Specification**, Herausgeber: IETF (R. Elz, R. Bush), Datum: Juli 1997, URL: https://datatracker.ietf.org/doc/html/rfc2181 (Stand: geprüft)
* **RFC 2308 – Negative Caching of DNS Queries (DNS NCACHE)**, Herausgeber: IETF (M. Andrews), Datum: März 1998, URL: https://datatracker.ietf.org/doc/html/rfc2308 (Stand: geprüft)
* **RFC 2606 – Reserved Top Level DNS Names**, Herausgeber: IETF (D. Eastlake, A. Panitz), Datum: Juni 1999, URL: https://datatracker.ietf.org/doc/html/rfc2606 (Stand: geprüft)
* **RFC 2782 – A DNS RR for specifying the location of services (DNS SRV)**, Herausgeber: IETF (A. Gulbrandsen et al.), Datum: Februar 2000, URL: https://datatracker.ietf.org/doc/html/rfc2782 (Stand: geprüft)
* **RFC 3596 – DNS Extensions to Support IP Version 6**, Herausgeber: IETF (S. Thomson et al.), Datum: Oktober 2003, URL: https://datatracker.ietf.org/doc/html/rfc3596 (Stand: geprüft)
* **RFC 3849 – IPv6 Address Prefix Reserved for Documentation**, Herausgeber: IETF (G. Huston et al.), Datum: Juli 2004, URL: https://datatracker.ietf.org/doc/html/rfc3849 (Stand: geprüft)
* **RFC 4193 – Unique Local IPv6 Unicast Addresses**, Herausgeber: IETF (R. Hinden, B. Haberman), Datum: Oktober 2005, URL: https://datatracker.ietf.org/doc/html/rfc4193 (Stand: geprüft)
* **RFC 5936 – DNS Zone Transfer Protocol (AXFR)**, Herausgeber: IETF (E. Lewis, A. Hoenes), Datum: Juni 2010, URL: https://datatracker.ietf.org/doc/html/rfc5936 (Stand: geprüft)
* **RFC 6891 – Extension Mechanisms for DNS (EDNS(0))**, Herausgeber: IETF (J. Damas et al.), Datum: April 2013, URL: https://datatracker.ietf.org/doc/html/rfc6891 (Stand: geprüft)
* **RFC 8499 – DNS Terminology**, Herausgeber: IETF (P. Hoffman et al.), Datum: Januar 2019, URL: https://datatracker.ietf.org/doc/html/rfc8499 (Stand: geprüft)
* **RFC 8945 – Secret Key Transaction Authentication for DNS (TSIG)**, Herausgeber: IETF (F. Dupont et al.), Datum: November 2020, URL: https://datatracker.ietf.org/doc/html/rfc8945 (Stand: geprüft)
* **BIND 9 Administrator Reference Manual (ARM)**, Herausgeber: Internet Systems Consortium (ISC), Version: BIND 9.18 / 9.20 (Stand nicht geprüft), URL: https://bind9.readthedocs.io/ (nicht geprüft)
* **Domain Name System (DNS) Documentation**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Windows Server 2022 / 2025 (Stand nicht geprüft), URL: https://learn.microsoft.com/en-us/windows-server/networking/dns/ (nicht geprüft)
* **DnsServer PowerShell Module Reference**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/en-us/powershell/module/dnsserver/ (nicht geprüft)

### 3. Labor-Setup & Rahmenbedingungen

Alle praktischen Übungen dieses Lehrplans finden in einer vollständig isolierten Virtualisierungsumgebung statt. Es darf zu keinem Zeitpunkt eine Verbindung zwischen den DNS-Diensten des Labors und einem produktiven Unternehmens- oder Heimnetzwerk bestehen, um Fehlkonfigurationen oder Störungen produktiver Namensauflösungen auszuschließen.

#### Virtuelles Netzwerk (Hyper-V)
* **Virtueller Switch (`vSwitch-DNS-Lab`):** Typ **Privat (Private Network)** (**erforderlich ab Modul 1**). Dieser Switch erlaubt ausschließlich die Kommunikation zwischen den virtuellen Maschinen auf dem Host, hat jedoch keine Bindung an das Host-Betriebssystem oder physische Netzwerkkarten.
* **IPv4-Subnetz A (Hauptnetz):** `192.168.50.0/24` nach RFC 1918 (**erforderlich ab Modul 1**).
* **IPv4-Subnetz B (Simuliertes Zweigstellen-/DMZ-Netz für Split-Brain-Tests):** `192.168.60.0/24` nach RFC 1918, realisiert über sekundäre IP-Adressen (IP-Aliasing) auf denselben virtuellen Netzwerkkarten (**erforderlich ab Modul 9**).
* **IPv6-Präfix:** Unique Local Unicast `fd00:50::/64` nach RFC 4193 bzw. Dokumentationspräfix `2001:db8:50::/64` nach RFC 3849 (**erforderlich ab Modul 5**).
* **Reservierte Labor-Domänen:** `corp.example.com`, `branch.example.org` und `lab.internal` (gemäß RFC 2606 und reservierten Namensräumen).

#### Virtuelle Maschinen (VMs)
1. **VM 1: `SRV-WIN-DNS` (Windows Server)** – **erforderlich ab Modul 1**
   * **Betriebssystem:** Windows Server 2022 oder Windows Server 2025 Standard/Datacenter (offizielle 180-Tage-Evaluationsversion von Microsoft, Installation mit Desktopdarstellung).
   * **Hardware-Ressourcen:** 2 vCPUs, 4 GB RAM, 60 GB dynamische VHDX, 1x vNIC an `vSwitch-DNS-Lab`.
   * **Statische IP-Konfiguration:** IPv4 `192.168.50.10/24`, IPv6 `fd00:50::10/64` (zusätzlich `192.168.60.10/24` **erforderlich ab Modul 9**).
   * **Erforderliche Rollen & Features:**
     * Rolle `DNS` (DNS-Server) inkl. Verwaltungstools und PowerShell-Modul `DnsServer` (**erforderlich ab Modul 2**).
     * Rolle `AD-Domain-Services` (Active Directory-Domänendienste) (**erforderlich ab Modul 8** für die Demonstration AD-integrierter Zonen und sicherer dynamischer Updates).
2. **VM 2: `SRV-LIN-BIND` (Linux Server)** – **erforderlich ab Modul 1**
   * **Betriebssystem:** Debian GNU/Linux 12 (Bookworm) oder Ubuntu Server 24.04 LTS (kostenlose Open-Source-Software, Installation ohne grafische Oberfläche).
   * **Hardware-Ressourcen:** 1–2 vCPUs, 2 GB RAM, 20 GB dynamische VHDX, 1x vNIC an `vSwitch-DNS-Lab`.
   * **Statische IP-Konfiguration:** IPv4 `192.168.50.11/24`, IPv6 `fd00:50::11/64` (zusätzlich `192.168.60.11/24` **erforderlich ab Modul 9**).
   * **Erforderliche Softwarepakete:**
     * `bind9`, `bind9utils`, `bind9-doc` (**erforderlich ab Modul 3**).
     * `dnsutils` bzw. `bind9-dnsutils` (enthält `dig`, `nslookup`, `nsupdate`, `delv`) (**erforderlich ab Modul 1**).
     * `tcpdump` (zur Paketanalyse auf der Kommandozeile) (**erforderlich ab Modul 11**).
   * *Hinweis zur Paketinstallation im isolierten Netz:* Die Pakete werden entweder während der Grundinstallation von einem vollständigen DVD-ISO-Image installiert oder einmalig vor dem Trennen der Netzwerkverbindung (vor Modul 1) heruntergeladen und anschließend per Snapshot gesichert.
3. **VM 3: `CLI-TEST-01` (Client-VM)** – **erforderlich ab Modul 1**
   * **Betriebssystem:** Windows 10/11 Enterprise (Evaluationsversion, Laufzeit vor Beginn prüfen) – **erforderlich ab Modul 1**, weil die Aufgaben von Beginn an `ipconfig`, `Resolve-DnsName` und die Windows-`hosts`-Datei verwenden und der Client in Modul 8 der Domäne beitritt. Eine zusätzliche Desktop-Linux-VM ist optional und wird von keiner Aufgabe vorausgesetzt.
   * **Hardware-Ressourcen:** 2 vCPUs, 4 GB RAM, 50 GB VHDX, 1x vNIC an `vSwitch-DNS-Lab`.
   * **Statische IP-Konfiguration:** IPv4 `192.168.50.100/24` (zusätzlich `192.168.60.100/24` **erforderlich ab Modul 9**), IPv6 `fd00:50::100/64`.
   * **Erforderliche Software:** Vorinstallierte Bordmittel (`nslookup`, PowerShell `Resolve-DnsName`, `ipconfig`). Optional (von keiner Aufgabe zwingend vorausgesetzt): Wireshark zur grafischen Betrachtung von PCAP-Dateien, die mit `tcpdump` oder `pktmon` aufgezeichnet wurden.

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen der Namensauflösung und DNS-Architektur

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die historische Entwicklung von lokalen `hosts`-Dateien hin zum hierarchischen Domain Name System nach RFC 1034 und RFC 1035 erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau des DNS-Namensraums (Root, Top-Level-Domains, Second-Level-Domains, Subdomains, FQDN) skizzieren und die Funktion der Root-Server erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen rekursiven und iterativen DNS-Abfragen sowie zwischen einem Stub-Resolver, einem Recursor (Caching-Resolver) und einem autoritativen Nameserver nach RFC 8499 präzise benennen.
  * Nach Abschluss dieses Moduls kann der Lernende lokale Namensauflösungsmechanismen (`hosts`-Datei, lokaler Resolver-Cache) konfigurieren und auf Netzwerkebene (UDP/TCP Port 53, EDNS(0) nach RFC 6891) analysieren.
* **Voraussetzungen:** Grundkenntnisse in TCP/IP, IPv4/IPv6-Adressierung und Umgang mit der Kommandozeile unter Windows und Linux.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **1.1** | Historie der Namensauflösung (`HOSTS.TXT`), Aufbau und Funktionsweise der lokalen `hosts`-Datei unter Windows und Linux, Reihenfolge der Namensauflösung (`nsswitch.conf` unter Linux, Resolver-Reihenfolge unter Windows). | 2 |
| **1.2** | Der DNS-Namensraum (RFC 1034, RFC 1035, RFC 8499): Baumstruktur, Root-Zone (`.`), Top-Level-Domains (gTLD, ccTLD, reservierte Namen nach RFC 2606), Fully Qualified Domain Name (FQDN) und Längengrenzen (Labels bis 63 Zeichen, Gesamtname bis 255 Byte). | 2 |
| **1.3** | Rollen im DNS: Stub-Resolver, rekursiver Resolver (Caching-Server) und autoritativer Nameserver; Detailablauf einer rekursiven vs. iterativen Abfrage; Delegationsprinzip. | 2 |
| **1.4** | Transportprotokolle und Paketstruktur: UDP Port 53 vs. TCP Port 53, klassische 512-Byte-Grenze, Erweiterung durch EDNS(0) nach RFC 6891, DNS-Header-Flags (`QR`, `AA`, `TC`, `RD`, `RA`) und Antwortcodes (`NOERROR`, `NXDOMAIN`, `SERVFAIL`, `REFUSED`). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Grundkonfiguration des isolierten Labor-Netzwerks:** Konfigurieren Sie auf den drei VMs (`SRV-WIN-DNS`, `SRV-LIN-BIND`, `CLI-TEST-01`), die an den privaten Switch `vSwitch-DNS-Lab` angebunden sind, die statischen IPv4-Adressen aus dem Netz `192.168.50.0/24` (`.10`, `.11`, `.100`). Prüfen Sie die gegenseitige Erreichbarkeit per `ping`.
2. **Manuelle Namensauflösung über die `hosts`-Datei:** Tragen Sie auf der Client-VM `CLI-TEST-01` in die lokale `hosts`-Datei (`C:\Windows\System32\drivers\etc\hosts`) den Namen `winserver.corp.example.com` mit der IP `192.168.50.10` und `linserver.corp.example.com` mit der IP `192.168.50.11` ein. Prüfen Sie die Auflösung mit `ping` und lassen Sie sich den lokalen DNS-Client-Cache mit `ipconfig /displaydns` anzeigen.
3. **Beobachtung der Namensauflösungsreihenfolge und Bereinigung:** Testen Sie auf `CLI-TEST-01` das Verhalten von `Resolve-DnsName winserver.corp.example.com` im Vergleich zu `nslookup winserver.corp.example.com` (Hinweis: `nslookup` ignoriert die lokale `hosts`-Datei und fragt direkt einen konfigurierten DNS-Server ab). **Wichtige Bereinigung für nachfolgende Module:** Entfernen Sie am Ende dieser Aufgabe die beiden Einträge für `winserver.corp.example.com` und `linserver.corp.example.com` wieder vollständig aus der `hosts`-Datei auf `CLI-TEST-01` und leeren Sie den Cache mit `ipconfig /flushdns`, damit in den folgenden Modulen die echte DNS-Server-Auflösung nicht durch lokale Einträge überdeckt wird.

#### Kontrollfragen

1. Warum verwendet das DNS-Protokoll im Regelfall UDP auf Port 53 für Standardabfragen, und in welchen konkreten Fällen weicht ein DNS-Client oder -Server zwingend auf TCP Port 53 aus?
2. Welche Bedeutung haben die DNS-Header-Flags `RD` (Recursion Desired), `RA` (Recursion Available) und `AA` (Authoritative Answer) in einer DNS-Nachricht?
3. Worin unterscheidet sich das Verhalten von `nslookup` gegenüber `ping` oder `Resolve-DnsName`, wenn ein gesuchter Hostname ausschließlich in der lokalen `hosts`-Datei des Betriebssystems eingetragen ist?
4. Was besagt der Antwortcode `NXDOMAIN` im Vergleich zu `NODATA` (Antwort mit `NOERROR`, aber 0 Einträgen im Answer-Abschnitt)?

---

### Modul 2: Installation und Grundkonfiguration des Windows-DNS-Servers

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die DNS-Server-Rolle unter Windows Server sowohl über die grafische Oberfläche als auch automatisiert über die Windows PowerShell installieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Dienststeuerung, die Lauschschnittstellen (Listening Interfaces) und die Stammhinweise (Root Hints) eines Windows-DNS-Servers konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Speicherung von DNS-Konfigurationsdaten in der Windows-Registry und in Textdateien unter `%SystemRoot%\System32\dns` erläutern.
* **Voraussetzungen:** Abschluss von Modul 1; Grundkenntnisse in der Verwaltung von Windows Server und der Windows PowerShell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **2.1** | Architektur des Windows-DNS-Dienstes (`dns.exe`): Systemdienst, Integration in den Server-Manager, Überblick über die Konsole `dnsmgmt.msc` und das PowerShell-Modul `DnsServer`. | 2 |
| **2.2** | Installation der DNS-Server-Rolle per GUI und PowerShell (`Install-WindowsFeature -Name DNS -IncludeManagementTools`); Verzeichnisstruktur unter `C:\Windows\System32\dns` und Registry-Pfade (`HKLM\SYSTEM\CurrentControlSet\Services\DNS`). | 2 |
| **2.3** | Grundkonfiguration: Binden des DNS-Dienstes an ausgewählte IP-Adressen (Listening Interfaces), Funktionsweise und Verwaltung der Root Hints (`cache.dns`), Verhalten im isolierten Labornetz ohne Internetzugang. | 2 |
| **2.4** | Erste Verwaltung mit der PowerShell: Abfragen und Anpassen von Servereinstellungen mit `Get-DnsServer`, `Get-DnsServerSetting` und `Set-DnsServerSetting`; Dienststeuerung und Ereignisanzeige (`DNS Server`-Protokoll). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Installation der DNS-Rolle auf `SRV-WIN-DNS`:** Installieren Sie auf der VM `SRV-WIN-DNS` (IP `192.168.50.10`) mithilfe der PowerShell die Rolle `DNS` inklusive der Verwaltungswerkzeuge. Überprüfen Sie anschließend mit `Get-Service DNS`, ob der Dienst läuft, und öffnen Sie die Konsole `dnsmgmt.msc`.
2. **Konfiguration der Lauschschnittstellen und Analyse der Root Hints:** Konfigurieren Sie den DNS-Server auf `SRV-WIN-DNS` so, dass er ausschließlich auf den statischen Labor-Adressen `192.168.50.10` und `fd00:50::10` (sowie Loopback) auf DNS-Anfragen lauscht. Untersuchen Sie die Datei `C:\Windows\System32\dns\cache.dns` im Texteditor und lassen Sie sich die Root Hints per PowerShell (`Get-DnsServerRootHint`) ausgeben.
3. **Deaktivierung der Rekursion für den isolierten Laborbetrieb (temporärer Test):** Da im isolierten Labornetz keine Verbindung zu den öffentlichen Root-Servern besteht, testen Sie auf `CLI-TEST-01` eine Anfrage nach einer externen Domain gegen `192.168.50.10` (`Resolve-DnsName example.net -Server 192.168.50.10`) und beobachten Sie den Timeout. Deaktivieren Sie testweise die Rekursion auf `SRV-WIN-DNS` (`Set-DnsServerRecursion -Enable $false`), wiederholen Sie die Abfrage und beobachten Sie die sofortige Antwort. **Wichtige Wiederherstellung für nachfolgende Module:** Aktivieren Sie die Rekursion auf `SRV-WIN-DNS` am Ende der Übung wieder (`Set-DnsServerRecursion -Enable $true`), da diese in Modul 7 für Weiterleitungen zwingend benötigt wird.

#### Kontrollfragen

1. In welchem Verzeichnis legt ein Windows-DNS-Server standardmäßig seine dateibasierten Zonendaten und die Datei `cache.dns` ab?
2. Warum kommt es in einem vom Internet getrennten Labornetzwerk bei aktivierter Rekursion und vorhandenen Root Hints zu Zeitüberschreitungen (Timeouts), wenn ein Client einen unbekannten Domänennamen abfragt?
3. Mit welchem PowerShell-Cmdlet lassen sich sämtliche aktuellen Konfigurationseinstellungen eines Windows-DNS-Servers strukturiert auslesen, um sie beispielsweise für ein Backup oder eine Dokumentation zu exportieren?

---

### Modul 3: Installation und Grundkonfiguration von ISC BIND 9 unter Linux

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den DNS-Server ISC BIND 9 unter Debian/Ubuntu installieren und den Systemdienst (`named`) über `systemd` verwalten.
  * Nach Abschluss dieses Moduls kann der Lernende die modulare Konfigurationsstruktur von BIND 9 (`named.conf`, `named.conf.options`, `named.conf.local`, `named.conf.default-zones`) fehlerfrei bearbeiten.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffskontrolllisten (`acl`), Lauschschnittstellen (`listen-on`, `listen-on-v6`) und das Steuerungswerkzeug `rndc` konfigurieren sowie Konfigurationsdateien vor dem Laden mit `named-checkconf` validieren.
* **Voraussetzungen:** Abschluss von Modul 1; Grundkenntnisse der Linux-Kommandozeile, Texteditoren (`nano` oder `vim`), Dateiberechtigungen und `systemd`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **3.1** | Einführung in ISC BIND 9: Architektur des Daemons `named`, Paketstruktur unter Debian/Ubuntu (`bind9`, `bind9utils`, `bind9-dnsutils`), Systembenutzer `bind` und Sicherheitskontext (AppArmor-Profil `/etc/apparmor.d/usr.sbin.named`). | 2 |
| **3.2** | Die Konfigurationsarchitektur unter `/etc/bind/`: Zusammenspiel von `named.conf`, `named.conf.options`, `named.conf.local` und `named.conf.default-zones` über `include`-Anweisungen; Syntaxregeln (Semikolons, geschweifte Klammern, Kommentarstile). | 3 |
| **3.3** | Globale Optionen und Zugriffsschutz: `directory`, `listen-on`, `listen-on-v6`, Definition von Access Control Lists (`acl`) und Einsatz von `allow-query` sowie `allow-recursion`. | 3 |
| **3.4** | Dienstverwaltung und Syntaxprüfung: Einsatz von `named-checkconf`, Steuerung im laufenden Betrieb über `rndc` (`rndc status`, `rndc reload`, `rndc reconfig`) und Auswertung des Systemprotokolls mit `journalctl -u named` (bzw. `bind9`). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Installation und Überprüfung von BIND 9 auf `SRV-LIN-BIND`:** Prüfen Sie auf `SRV-LIN-BIND` (IP `192.168.50.11`) die Installation der Pakete `bind9`, `bind9utils` und `bind9-dnsutils`. Kontrollieren Sie den Dienststatus mit `systemctl status named` (bzw. `bind9`) und prüfen Sie mit `ss -tulnp | grep named`, auf welchen IP-Adressen und Ports (53 und 953 für `rndc`) der Dienst lauscht.
2. **Einrichten einer ACL und Anpassen der `named.conf.options`:** Öffnen Sie `/etc/bind/named.conf.options` auf `SRV-LIN-BIND`. Definieren Sie oberhalb des `options`-Blocks eine ACL namens `lab-nets` für die Netze `127.0.0.0/8`, `192.168.50.0/24`, `::1/128` und `fd00:50::/64`. Konfigurieren Sie innerhalb von `options` die Direktiven `listen-on { 127.0.0.1; 192.168.50.11; };`, `listen-on-v6 { ::1; fd00:50::11; };` sowie `allow-query { lab-nets; };`.
3. **Syntaxprüfung und Dienststeuerung mit `rndc`:** Bauen Sie absichtlich einen Syntaxfehler (z. B. ein fehlendes Semikolon) in `/etc/bind/named.conf.options` ein und führen Sie `named-checkconf` aus. Interpretieren Sie die Zeilenangabe der Fehlermeldung, beheben Sie den Fehler, prüfen Sie erneut mit `named-checkconf` und laden Sie die Konfiguration anschließend unterbrechungsfrei mit `rndc reload` neu. Prüfen Sie das Ergebnis mit `rndc status` und `journalctl -u named -n 20`.

#### Kontrollfragen

1. Warum teilt Debian/Ubuntu die BIND-9-Konfiguration in mehrere Dateien wie `named.conf.options` und `named.conf.local` auf, anstatt alle Direktiven direkt in `/etc/bind/named.conf` zu schreiben?
2. Welche Aufgabe erfüllt das Werkzeug `rndc`, über welchen TCP-Port kommuniziert es standardmäßig lokal mit dem `named`-Prozess und wie wird diese Kommunikation authentifiziert?
3. Welches Risiko besteht, wenn ein neu erstelltes Verzeichnis für Zonendateien unter Ubuntu/Debian nicht dem Benutzer/Gruppe `bind` gehört oder nicht im AppArmor-Profil von `named` freigegeben ist?
4. Worin besteht der Unterschied zwischen einem Neustart des Dienstes via `systemctl restart named` und dem Neuladen der Konfiguration über `rndc reload` im Hinblick auf den laufenden Betrieb?

---

### Modul 4: Zonentypen im Detail: Primäre, Sekundäre und Stub-Zonen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen einer Domain und einer DNS-Zone sowie die Funktionsweise von Zonendelegationen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende primäre (Primary/Master), sekundäre (Secondary/Slave) und Stub-Zonen hinsichtlich ihrer Einsatzzwecke, Datenhaltung und Ausfallsicherheit vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines SOA-Eintrags (Start of Authority) nach RFC 1035 und RFC 2308 in allen Bestandteilen erläutern und primäre Forward-Lookupzonen sowohl unter Windows Server als auch in BIND 9 fehlerfrei anlegen.
* **Voraussetzungen:** Abschluss der Module 1 bis 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **4.1** | Zone vs. Domain: Wann wird eine Subdomain zu einer eigenen Zone? Prinzip der Zonendelegation über NS-Records und die Notwendigkeit von Glue-Records. | 2 |
| **4.2** | Vergleich der Zonentypen: Primäre Zone (Schreib-/Lesezugriff), Sekundäre Zone (schreibgeschützte Kopie zur Lastverteilung und Redundanz), Stub-Zone (enthält nur SOA-, NS- und Glue-A/AAAA-Records zur aktuellen Namensserver-Auflösung). | 2 |
| **4.3** | Der SOA-Record (Start of Authority) im Detail: Primärer Nameserver (MNAME), Verantwortlicher Kontakt (RNAME), Seriennummer (Serial, Format `YYYYMMDDnn`), Refresh, Retry, Expire und Minimum-TTL (Negative Caching TTL nach RFC 2308). | 3 |
| **4.4** | Anlegen primärer Zonen in der Praxis: Einrichtung unter Windows Server (`Add-DnsServerPrimaryZone`) und in BIND 9 (`type master;` bzw. `type primary;` in `named.conf.local`), Validierung von Zonendateien mit `named-checkzone`. | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einrichten einer primären Zone auf `SRV-WIN-DNS`:** Erstellen Sie auf dem Windows-DNS-Server `SRV-WIN-DNS` eine dateibasierte primäre Forward-Lookupzone für den Namen `corp.example.com` mit der Zonendatei `corp.example.com.dns` (`Add-DnsServerPrimaryZone -Name "corp.example.com" -ZoneFile "corp.example.com.dns"`). Passen Sie in den Zoneneigenschaften (Reiter Ursprung / SOA) das Refresh-Intervall auf 15 Minuten und das Retry-Intervall auf 5 Minuten an. Öffnen Sie anschließend die Datei `C:\Windows\System32\dns\corp.example.com.dns` zur Kontrolle im Texteditor.
2. **Einrichten einer primären Zone auf `SRV-LIN-BIND`:** Deklarieren Sie auf `SRV-LIN-BIND` in der Datei `/etc/bind/named.conf.local` eine primäre Zone für `branch.example.org` (`type primary; file "/etc/bind/db.branch.example.org";`). Erstellen Sie die Zonendatei `/etc/bind/db.branch.example.org` auf Basis von `/etc/bind/db.empty`, tragen Sie einen korrekten SOA-Record (`linserver.branch.example.org. hostmaster.branch.example.org.`), die Seriennummer im Format `2026110801`, einen NS-Record sowie den A-Record für `linserver` (`192.168.50.11`) ein.
3. **Validierung und Abfragetest:** Prüfen Sie die neue Zonendatei auf `SRV-LIN-BIND` mit `named-checkzone branch.example.org /etc/bind/db.branch.example.org`. Laden Sie BIND mit `rndc reload` neu und fragen Sie von `CLI-TEST-01` aus den SOA-Eintrag beider Server gezielt ab (`Resolve-DnsName -Name corp.example.com -Type SOA -Server 192.168.50.10` und `Resolve-DnsName -Name branch.example.org -Type SOA -Server 192.168.50.11`).

#### Kontrollfragen

1. Worin besteht der zentrale technische Unterschied zwischen einer sekundären Zone und einer Stub-Zone, und in welchem Szenario ist eine Stub-Zone einer sekundären Zone vorzuziehen?
2. Welche Funktion hat der letzte numerische Wert (Minimum-TTL) im SOA-Record seit der Spezifikation von RFC 2308?
3. Was sind sogenannte Glue-Records, und unter welcher Bedingung sind sie bei einer Zonendelegation zwingend erforderlich?
4. Welche Auswirkung hat es im laufenden Betrieb, wenn ein Administrator in einer BIND-9-Zonendatei Einträge ändert, die Datei speichert und `rndc reload` ausführt, dabei aber vergisst, die Seriennummer (Serial) im SOA-Record zu erhöhen?

---

### Modul 5: Ressourceneinträge (Resource Records) in Forward- und Reverse-Zonen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Syntax, Felder und Einsatzzwecke der Resource Records `A`, `AAAA`, `CNAME`, `MX`, `TXT`, `SRV` und `PTR` nach RFC 1035, RFC 2181, RFC 2782 und RFC 3596 erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Reverse-Lookupzonen für IPv4 (`in-addr.arpa`) und IPv6 (`ip6.arpa`) berechnen, anlegen und mit `PTR`-Einträgen pflegen.
  * Nach Abschluss dieses Moduls kann der Lernende sämtliche genannten Resource Records sowohl in Windows-DNS als auch in BIND-9-Zonendateien fehlerfrei anlegen und verifizieren.
* **Voraussetzungen:** Abschluss von Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **5.1** | Struktur von Resource Records (`Name`, `TTL`, `Class IN`, `Type`, `RDATA`); Adress- und Alias-Einträge: `A` (IPv4 nach RFC 1035), `AAAA` (IPv6 nach RFC 3596) und `CNAME` (Canonical Name). Restriktionen beim Einsatz von `CNAME` (kein `CNAME` am Zone Apex `@`, keine Kombination mit anderen Record-Typen am selben Knoten gemäß RFC 2181). | 3 |
| **5.2** | Dienst- und Text-Einträge: `MX` (Mail Exchanger inkl. Präferenzwert/Priorität), `TXT` (freie Textdaten, Überblick zur Nutzung für SPF/DKIM/DMARC-Verifikation) und `SRV` (Service Location nach RFC 2782: `_service._proto.Name TTL IN SRV Priority Weight Port Target`). | 3 |
| **5.3** | Reverse-Lookupzonen und `PTR`-Records: Aufbau des `in-addr.arpa`-Baums für IPv4 und des `ip6.arpa`-Baums (Nibble-Format in umgekehrter Reihenfolge nach RFC 3596) für IPv6; Bedeutung konsistenter Forward- und Reverse-Auflösung. | 3 |
| **5.4** | Zonendatei-Syntax im Detail (BIND 9 vs. Windows): Die Direktiven `$TTL` und `$ORIGIN`, das Symbol `@`, Bedeutung des abschließenden Punktes (Trailing Dot) bei FQDNs in Zonendateien zur Vermeidung ungewollter Namensanhänge. | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Pflege von Forward-Records auf `SRV-WIN-DNS` (`corp.example.com`):** Legen Sie auf `SRV-WIN-DNS` in der Zone `corp.example.com` per PowerShell oder GUI folgende Einträge an:
   * `A` und `AAAA` für `winserver` (`192.168.50.10` und `fd00:50::10`) sowie für `files` (`192.168.50.20` und `fd00:50::20`).
   * `CNAME` für `intranet.corp.example.com` mit Ziel `files.corp.example.com`.
   * `MX` für die Domäne `corp.example.com` mit Priorität `10` auf `mail.corp.example.com` sowie den zugehörigen `A`-Record `mail` (`192.168.50.25`).
   * `TXT` am Zone Apex (`@`) mit dem Wert `"v=spf1 mx -all"`.
   * `SRV` für `_sip._tcp.corp.example.com` (Priorität `10`, Gewichtung `100`, Port `5060`, Ziel `voip.corp.example.com`) inkl. `A`-Record für `voip` (`192.168.50.30`).
2. **Einrichten von IPv4- und IPv6-Reverse-Zonen auf `SRV-WIN-DNS`:** Erstellen Sie auf `SRV-WIN-DNS` je eine primäre dateibasierte Reverse-Lookupzone für das IPv4-Netz `192.168.50.0/24` (`50.168.192.in-addr.arpa`) und für das IPv6-Präfix `fd00:50::/64` (`0.0.0.0.0.0.0.0.0.5.0.0.0.0.d.f.ip6.arpa`). Erstellen Sie darin passende `PTR`-Einträge für `winserver.corp.example.com` (`192.168.50.10` und `fd00:50::10`) sowie für `linserver.branch.example.org` (`192.168.50.11` und `fd00:50::11`).
3. **Pflege von Resource Records in BIND 9 auf `SRV-LIN-BIND` (`branch.example.org`):** Erweitern Sie die Zonendatei `/etc/bind/db.branch.example.org` um `A`- und `AAAA`-Records für `linserver` (`192.168.50.11`, `fd00:50::11`) und `web` (`192.168.50.40`, `fd00:50::40`), einen `CNAME` `www` auf `web`, einen `MX`-Record (Priorität `10` auf `linserver.branch.example.org.`), einen `TXT`-Record und einen `SRV`-Record (`_ldap._tcp.branch.example.org.`). Erhöhen Sie die Seriennummer im SOA-Record, prüfen Sie die Datei mit `named-checkzone` und laden Sie den Dienst per `rndc reload` neu. Testen Sie alle angelegten Record-Typen von `CLI-TEST-01` aus.

#### Kontrollfragen

1. Warum darf am Zone Apex (also für den Domänennamen selbst, z. B. `corp.example.com`) laut DNS-Spezifikation (RFC 1034 / RFC 2181) kein `CNAME`-Record angelegt werden?
2. Ein Unternehmen betreibt zwei Mailserver mit `MX`-Einträgen der Präferenzwerte `10` (`mail1`) und `20` (`mail2`). In welcher Reihenfolge versucht ein externer Mailserver die Zustellung, und wie verhält es sich, wenn beide `MX`-Einträge denselben Präferenzwert `10` besitzen?
3. Wie lautet der exakte Name des `PTR`-Eintrags (inklusive Zonensuffix) für die IPv4-Adresse `192.168.50.25` und wie wird das Nibble-Format für IPv6-Reverse-Zonen gebildet?
4. Was passiert in einer BIND-9-Zonendatei für die Zone `branch.example.org`, wenn Sie als Ziel eines `CNAME`-Eintrags `web.branch.example.org` (ohne abschließenden Punkt am Ende) eintragen?

---

### Modul 6: Zonenübertragung (AXFR/IXFR) und plattformübergreifende Replikation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer vollständigen (AXFR nach RFC 5936) und einer inkrementellen Zonenübertragung (IXFR nach RFC 1995) sowie den DNS-NOTIFY-Mechanismus nach RFC 1996 erklären.
  * Nach Abschluss dieses Moduls kann der Lernende sekundäre Zonen plattformübergreifend zwischen Windows Server und BIND 9 in beide Richtungen einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Zonenübertragungen durch IP-Restriktionen absichern und die Absicherung mit kryptografischen Transaktionssignaturen (TSIG nach RFC 8945) in BIND 9 einrichten sowie begründen, warum TSIG zwischen Windows-DNS und BIND nicht einsetzbar ist.
* **Voraussetzungen:** Abschluss der Module 4 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **6.1** | Mechanismen der Zonenübertragung: Vollständiger Transfer (AXFR nach RFC 5936) vs. inkrementeller Transfer (IXFR nach RFC 1995) über TCP Port 53; Rolle der SOA-Seriennummer; Push-Benachrichtigung bei Änderungen mittels DNS NOTIFY (RFC 1996). | 2 |
| **6.2** | Plattformübergreifende Replikation: Windows als Primary und BIND 9 als Secondary sowie umgekehrt; Verzeichnisberechtigungen für sekundäre Zonendateien unter Linux (`/var/cache/bind/`). | 3 |
| **6.3** | Absicherung von Zonenübertragungen: Gefahr offener Zonentransfers (Information Disclosure); Einschränkung per IP-Liste unter Windows und per `allow-transfer` in BIND 9; TSIG (Transaction Signatures nach RFC 8945) zur Authentifizierung von Transfers; praktisch an einer separaten Testzone auf BIND, da Windows-DNS TSIG für Zonenübertragungen nach bisherigem Kenntnisstand nicht unterstützt (nicht bestätigt). | 3 |
| **6.4** | Diagnose und manuelles Auslösen von Zonenübertragungen: Einsatz von `rndc retransfer`, `rndc refresh`, `Sync-DnsServerZone` sowie Testabfragen mit `dig @server domain AXFR`. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zonenübertragung von Windows (Primary) zu BIND 9 (Secondary):**
   * Fügen Sie auf `SRV-WIN-DNS` in der Zone `corp.example.com` den Server `linserver.branch.example.org` (`192.168.50.11`) als weiteren autoritativen Nameserver (NS-Record) hinzu. Aktivieren Sie in den Zoneneigenschaften von `corp.example.com` ( sowie den beiden Reverse-Zonen aus Modul 5) die Zonenübertragung ausschließlich an die IP-Adresse `192.168.50.11` inklusive DNS-Benachrichtigung (Notify).
   * Richten Sie auf `SRV-LIN-BIND` in `/etc/bind/named.conf.local` eine sekundäre Zone für `corp.example.com` sowie für `50.168.192.in-addr.arpa` ein (`type secondary; masters { 192.168.50.10; }; file "/var/cache/bind/db.corp.example.com";`). Laden Sie BIND neu und prüfen Sie im Log (`journalctl -u named`), ob der AXFR-Transfer erfolgreich war.
2. **Zonenübertragung von BIND 9 (Primary) zu Windows (Secondary):**
   * Ergänzen Sie auf `SRV-LIN-BIND` in der Zone `branch.example.org` den NS-Record für `winserver.corp.example.com.` und beschränken Sie den Transfer in `/etc/bind/named.conf.local` innerhalb der Zonendefinition mit `allow-transfer { 192.168.50.10; };` und `also-notify { 192.168.50.10; };`. Erhöhen Sie die SOA-Seriennummer und führen Sie `rndc reload` aus.
   * Legen Sie auf `SRV-WIN-DNS` eine sekundäre Zone für `branch.example.org` mit dem Master-Server `192.168.50.11` an (`Add-DnsServerSecondaryZone -Name "branch.example.org" -ZoneFile "branch.example.org.dns" -MasterServers 192.168.50.11`).
3. **Testen von IXFR/NOTIFY und Verhinderung unbefugter Transfers:** Fügen Sie auf `SRV-WIN-DNS` einen neuen `A`-Record `test-notify.corp.example.com` (`192.168.50.99`) hinzu und prüfen Sie auf `SRV-LIN-BIND`, ob die Änderung sofort per NOTIFY und IXFR/AXFR übernommen wurde. Versuchen Sie anschließend von `CLI-TEST-01` (`192.168.50.100`) aus einen unbefugten Zonenabzug beider Server (`nslookup` mit `ls -d corp.example.com` bzw. `dig @192.168.50.11 branch.example.org AXFR`) und verifizieren Sie, dass beide Server den Transfer ablehnen.
4. **TSIG-gesicherte Zonenübertragung an einer separaten Testzone (nur BIND):** Legen Sie auf `SRV-LIN-BIND` eine zusätzliche kleine primäre Zone `tsig-test.example.org` an (Zonendatei `/etc/bind/db.tsig-test.example.org`, ein `A`-Record `host1` mit `192.168.50.55`). Erzeugen Sie mit `tsig-keygen -a hmac-sha256 xfer-key > /etc/bind/xfer.key` einen Schlüssel (Berechtigungen `640`, Gruppe `bind`), binden Sie ihn per `include` in `/etc/bind/named.conf.local` ein und setzen Sie in der Zone `allow-transfer { key "xfer-key"; };`. Prüfen Sie auf `SRV-LIN-BIND`, dass `dig @192.168.50.11 tsig-test.example.org AXFR` ohne Schlüssel abgelehnt wird und mit `dig @192.168.50.11 tsig-test.example.org AXFR -k /etc/bind/xfer.key` gelingt. **Wichtige Bereinigung für nachfolgende Module:** Entfernen Sie am Ende die Zone `tsig-test.example.org`, die `include`-Zeile sowie die Dateien `xfer.key` und `db.tsig-test.example.org` und laden Sie BIND mit `rndc reload` neu; die Zonen `corp.example.com` und `branch.example.org` behalten ihre IP-basierte Transferbeschränkung unverändert.

#### Kontrollfragen

1. Wie erkennt ein sekundärer DNS-Server beim regulären Refresh-Ablauf oder nach dem Empfang eines DNS-NOTIFY-Pakets, ob er überhaupt eine Zonenübertragung vom primären Server anfordern muss?
2. Warum sollten sekundäre Zonendateien unter Debian/Ubuntu im Verzeichnis `/var/cache/bind/` und nicht in `/etc/bind/` gespeichert werden?
3. Welche Sicherheitsrisiken entstehen, wenn ein öffentlich erreichbarer autoritativer DNS-Server Zonenübertragungen (`AXFR`) für beliebige IP-Adressen zulässt?
4. Welchen zusätzlichen Schutz bietet TSIG (RFC 8945) gegenüber einer reinen IP-Adress-Freigabe in `allow-transfer`?

---

### Modul 7: Weiterleitungen, bedingte Weiterleitungen, Caching und TTL-Steuerung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen globalen Weiterleitungen (Forwarders) und bedingten Weiterleitungen (Conditional Forwarders / Forward Zones) erläutern und beide Varianten in Windows-DNS und BIND 9 einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten des DNS-Caches (positives und negatives Caching nach RFC 2308) sowie die Auswirkungen unterschiedlicher TTL-Werte bei geplanten Migrationen beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende den DNS-Cache auf Servern und Clients gezielt inspizieren und leeren.
* **Voraussetzungen:** Abschluss der Module 1 bis 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **7.1** | Weiterleitungsarchitekturen: Globale Weiterleitungen (Forwarders) vs. Root Hints; Option „Nur Weiterleitungen verwenden“ (`forward only;` vs. `forward first;` in BIND 9). | 2 |
| **7.2** | Bedingte Weiterleitungen (Conditional Forwarders unter Windows, `type forward;` in BIND 9): Gezielte Namensauflösung für Partnernetzwerke, interne Subdomänen oder nach Unternehmensfusionen; Vergleich Conditional Forwarder vs. Stub-Zone. | 2 |
| **7.3** | Caching-Mechanismen und TTL-Steuerung: Positives Caching (Record-TTL) und Negatives Caching (SOA Minimum-TTL nach RFC 2308); Best Practices zur rechtzeitigen Absenkung der TTL vor IP-Umstellungen oder Servermigrationen. | 2 |
| **7.4** | Cache-Verwaltung in der Praxis: Anzeigen und Löschen des Caches unter Windows Server (`Show-DnsServerCache`, `Clear-DnsServerCache`), unter BIND 9 (`rndc dumpdb -cache`, `rndc flush`, `rndc flushname`) und auf dem Client (`ipconfig /flushdns`, `Clear-DnsClientCache`). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Testen von bedingten Weiterleitungen (Conditional Forwarding) anstelle einer sekundären Zone:**
   * Legen Sie auf `SRV-LIN-BIND` eine weitere kleine primäre Zone für eine Partnerfirma `partner.example.net` (Zonendatei `/etc/bind/db.partner.example.net`) mit einem `A`-Record `portal.partner.example.net` (`192.168.50.88`) an und laden Sie BIND neu.
   * Richten Sie auf `SRV-WIN-DNS` eine bedingte Weiterleitung (Conditional Forwarder) für die Domäne `partner.example.net` auf die IP-Adresse `192.168.50.11` ein (`Add-DnsServerConditionalForwarderZone -Name "partner.example.net" -MasterServers 192.168.50.11`).
2. **Analyse des Caching-Verhaltens und der herabzählenden TTL:** Fragen Sie von `CLI-TEST-01` aus den Namen `portal.partner.example.net` über den Windows-Server `192.168.50.10` ab (`Resolve-DnsName portal.partner.example.net -Server 192.168.50.10`). Wiederholen Sie die Abfrage nach 15 Sekunden und beobachten Sie, wie der zurückgelieferte TTL-Wert sinkt und die Antwort ohne `AA`-Flag (nicht-autoritativ, aus dem Cache von `SRV-WIN-DNS`) geliefert wird.
3. **Inspektion und gezieltes Leeren des Server-Caches:** Lassen Sie sich auf `SRV-WIN-DNS` den aktuellen Cache-Inhalt ausgeben (`Show-DnsServerCache`) und leeren Sie ihn anschließend mit `Clear-DnsServerCache`. Führen Sie analog auf `SRV-LIN-BIND` nach einer Abfrage von `winserver.corp.example.com` den Befehl `rndc dumpdb -cache` aus, betrachten Sie die erzeugte Datei `/var/cache/bind/named_dump.db` und leeren Sie den Cache mit `rndc flush`.

#### Kontrollfragen

1. Worin unterscheiden sich die BIND-9-Optionen `forward first;` und `forward only;`, wenn der eingetragene Weiterleitungsserver (Forwarder) nicht erreichbar ist?
2. Wann sollten Sie in einem Unternehmensnetzwerk eine bedingte Weiterleitung (Conditional Forwarder) einsetzen und wann ist stattdessen eine Stub-Zone vorteilhafter?
3. Sie planen für kommenden Freitag die Umstellung der IP-Adresse eines geschäftskritischen Webservers, dessen `A`-Record aktuell eine TTL von 86.400 Sekunden (24 Stunden) aufweist. Welche Schritte müssen Sie im Vorfeld der Umstellung durchführen, um Ausfallzeiten durch veraltete Caches zu minimieren?
4. Warum speichert ein rekursiver DNS-Server auch negative Antworten (`NXDOMAIN`) für eine gewisse Zeit im Cache, und welcher Wert in der abgefragten Zone bestimmt diese Speicherdauer?

---

### Modul 8: Dynamische DNS-Updates (DDNS) und Active-Directory-integrierte Zonen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsweise dynamischer DNS-Updates nach RFC 2136 sowie das Zusammenspiel mit Clients und DHCP-Servern (als Schnittstellenüberblick) erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende die zwingende Abhängigkeit von Active Directory Domain Services (AD DS) von DNS (insbesondere `SRV`-Records) sowie die Vorteile AD-integrierter Zonen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende sichere dynamische Updates unter Windows Server sowie TSIG-authentifizierte dynamische Updates in BIND 9 mittels `nsupdate` konfigurieren, inklusive Alterung und Aufräumvorgang (Aging & Scavenging).
* **Voraussetzungen:** Abschluss der Module 1 bis 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **8.1** | Dynamische DNS-Updates (RFC 2136): Funktionsweise des `UPDATE`-Opcodes; Registrierungsverhalten von Windows-Clients (A-, AAAA- und PTR-Registrierung); konzeptioneller Überblick über die Schnittstelle zum DHCP-Server (ohne tiefe DHCP-Konfiguration, da eigener Lehrplan). | 2 |
| **8.2** | DNS und Active Directory (soweit für DNS nötig): Warum AD DS ohne DNS nicht funktioniert; Rolle der `_msdcs`-Zone und der Domänen-Controller-Locator-Records (`_ldap._tcp.dc._msdcs.<Domain>`); Umwandlung dateibasierter Zonen in AD-integrierte Zonen; Replikationsbereiche (ForestDnsZones, DomainDnsZones). | 3 |
| **8.3** | Sicherheit bei dynamischen Updates: Nicht sichere vs. sichere dynamische Updates (Kerberos/GSS-TSIG im AD); Alterung und Aufräumvorgang (Aging and Scavenging: No-Refresh-Interval und Refresh-Interval) unter Windows Server gegen verwaiste Einträge. | 2 |
| **8.4** | Dynamische Updates unter BIND 9: Absicherung über TSIG-Schlüssel (`tsig-keygen`), Konfiguration von `allow-update` bzw. `update-policy`, Verwaltung der `.jnl`-Journaldateien, Einfrieren und Auftauen dynamischer Zonen (`rndc freeze` / `rndc thaw`) für manuelle Bearbeitungen sowie Einsatz von `nsupdate`. | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einrichten von AD DS und Umwandlung in eine AD-integrierte Zone auf `SRV-WIN-DNS`:**
   * Installieren Sie auf `SRV-WIN-DNS` die Rolle `AD-Domain-Services` und stufen Sie den Server zum Domänencontroller einer neuen Gesamtstruktur `corp.example.com` hoch (`Install-ADDSForest -DomainName "corp.example.com" -InstallDns:$false`).
   * Konvertieren Sie anschließend die bestehende primäre Zone `corp.example.com` sowie die Reverse-Zone `50.168.192.in-addr.arpa` in AD-integrierte Zonen und stellen Sie die dynamischen Updates auf „Nur sichere“ (`SecureOnly`). Prüfen Sie das Vorhandensein der neu angelegten `_msdcs.corp.example.com`-Einträge und nehmen Sie die Client-VM `CLI-TEST-01` (primärer DNS-Server: `192.168.50.10`) in die Domäne `corp.example.com` auf. Beobachten Sie die automatische dynamische Registrierung des Client-Eintrags via `ipconfig /registerdns`.
   * *Hinweis für den hybriden Betrieb mit `SRV-LIN-BIND`:* Überprüfen Sie nach der Konvertierung in den Zoneneigenschaften von `corp.example.com` auf `SRV-WIN-DNS`, dass die Zonenübertragung an `192.168.50.11` weiterhin aktiviert ist, damit `SRV-LIN-BIND` sekundärer Server bleibt.
2. **Konfiguration von Aging und Scavenging unter Windows Server:** Aktivieren Sie auf `SRV-WIN-DNS` die Alterung (Aging) für die Zone `corp.example.com` (Nichtaktualisierungsintervall: 7 Tage, Aktualisierungsintervall: 7 Tage) sowie auf Serverebene den automatischen Aufräumvorgang. Unterscheiden Sie in der Konsole statische Einträge (Zeitstempel „Statisch“) von dynamisch registrierten Einträgen (mit Datum/Uhrzeit-Zeitstempel).
3. **Dynamische Updates mit TSIG und `nsupdate` auf `SRV-LIN-BIND`:**
   * Erzeugen Sie auf `SRV-LIN-BIND` mit `tsig-keygen -a hmac-sha256 ddns-key > /etc/bind/ddns.key` einen TSIG-Schlüssel (Berechtigungen `640`, Gruppe `bind`). Binden Sie `/etc/bind/ddns.key` per `include` in `/etc/bind/named.conf.local` ein.
   * Kopieren Sie die Zonendatei `/etc/bind/db.branch.example.org` nach `/var/lib/bind/db.branch.example.org` (damit `named` Schreibrechte für die `.jnl`-Journaldatei hat), passen Sie den Pfad in `named.conf.local` an und fügen Sie in der Zone `branch.example.org` die Direktive `allow-update { key "ddns-key"; };` hinzu. Laden Sie BIND neu.
   * Führen Sie mit `nsupdate -k /etc/bind/ddns.key` ein dynamisches Update durch, das den Eintrag `dynhost.branch.example.org` (`A 192.168.50.77`, TTL `300`) anlegt. Prüfen Sie die angelegte Datei `db.branch.example.org.jnl` und üben Sie den Ablauf `rndc freeze branch.example.org` gefolgt von `rndc thaw branch.example.org`.

#### Kontrollfragen

1. Welche konkrete Aufgabe haben das „Nichtaktualisierungsintervall“ (No-Refresh Interval) und das „Aktualisierungsintervall“ (Refresh Interval) beim DNS-Scavenging unter Windows Server?
2. Warum schlägt die Anmeldung eines Windows-Clients an einer Active-Directory-Domäne fehl, wenn in dessen Netzwerkkonfiguration ein DNS-Server eingetragen ist, der die `_msdcs`- bzw. `SRV`-Einträge der AD-Domäne nicht auflösen kann?
3. Warum darf eine in BIND 9 für dynamische Updates freigegebene Zonendatei niemals direkt im Texteditor bearbeitet werden, ohne zuvor `rndc freeze <zone>` auszuführen?
4. Welchen Vorteil bietet die Speicherung von DNS-Zonen im Active Directory (AD-integriert) gegenüber klassischen Textdateien im Verzeichnis `C:\Windows\System32\dns`?

---

### Modul 9: Split-Brain-DNS (Split-Horizon), BIND Views und Windows DNS Policies

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Architekturkonzept von Split-Brain-DNS (Split-Horizon-DNS) erläutern und dessen Vor- und Nachteile abwägen.
  * Nach Abschluss dieses Moduls kann der Lernende in BIND 9 mithilfe von `view`-Direktiven und `match-clients`-Regeln unterschiedliche Zonenansichten für verschiedene Quell-Subnetze implementieren.
  * Nach Abschluss dieses Moduls kann der Lernende unter Windows Server mithilfe von DNS-Richtlinien (DNS Policies, Zonenscopes und Client-Subnetzen) eine Split-Brain-Namensauflösung über die PowerShell konfigurieren.
* **Voraussetzungen:** Abschluss der Module 1 bis 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **9.1** | Konzept Split-Brain-DNS (Split-Horizon): Warum derselbe FQDN (z. B. `mail.corp.example.com` oder `www.branch.example.org`) für interne Clients auf eine private IP (RFC 1918) und für externe bzw. DMZ-Clients auf eine andere IP aufgelöst werden soll; Architekturalternativen (getrennte Server vs. Views/Policies auf einem Server). | 2 |
| **9.2** | Implementierung in BIND 9 mit `view`-Klauseln: Funktionsweise von `match-clients`, Reihenfolge der Auswertung (First Match), zwingende Regel „Sobald ein View existiert, müssen alle Zonen innerhalb von Views liegen“. | 4 |
| **9.3** | Implementierung unter Windows Server mit DNS Policies (ab Windows Server 2016): Anlegen von `DnsServerClientSubnet`, `DnsServerZoneScope`, Zuweisung abweichender Resource Records in Zonenscopes und Verknüpfung über `Add-DnsServerQueryResolutionPolicy`. | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorbereitung des zweiten Test-Subnetzes auf `CLI-TEST-01`:** Fügen Sie auf der Netzwerkkarte der Client-VM `CLI-TEST-01` zusätzlich zur bestehenden IP `192.168.50.100/24` die sekundäre IP-Adresse `192.168.60.100/24` hinzu und auf `SRV-WIN-DNS` (`192.168.60.10/24`) sowie `SRV-LIN-BIND` (`192.168.60.11/24`) ebenfalls je eine Adresse im Netz `192.168.60.0/24`, um Anfragen aus einem zweiten Subnetz (z. B. Gast-/DMZ-Netz) ohne zusätzlichen Router zu simulieren. **Erweitern Sie dabei die Dienstkonfiguration, sonst werden Abfragen aus dem zweiten Subnetz nicht beantwortet:** (a) Ergänzen Sie auf `SRV-WIN-DNS` die Lauschadresse `192.168.60.10` zu den Adressen aus Modul 2 (Eigenschaften des DNS-Servers, Reiter „Schnittstellen“, oder PowerShell `Set-DnsServerSetting -ListenAddresses`; Parametername nicht bestätigt). (b) Ergänzen Sie auf `SRV-LIN-BIND` in `/etc/bind/named.conf.options` die Adresse `192.168.60.11;` in `listen-on`, definieren Sie eine ACL `dmz-net { 192.168.60.0/24; };` und erweitern Sie `allow-query` auf `{ lab-nets; dmz-net; }`; prüfen Sie mit `named-checkconf` und laden Sie mit `rndc reload` neu. Diese Erweiterungen bleiben auch nach den Bereinigungen dieses Moduls bestehen; `allow-recursion` wird erst in Modul 10 auf `lab-nets` beschränkt, die DMZ erhält dann keine Rekursion.
2. **Einrichten von Split-Horizon mit BIND Views auf `SRV-LIN-BIND`:**
   * Sichern Sie Ihre bisherige `/etc/bind/named.conf.local` und `/etc/bind/named.conf.default-zones` als Backup-Kopien.
   * Konfigurieren Sie zwei Views: `view "internal"` (`match-clients { 192.168.50.0/24; 127.0.0.0/8; fd00:50::/64; ::1/128; };`) und `view "dmz"` (`match-clients { 192.168.60.0/24; };`). Binden Sie die Standardzonen in den internen View ein (ebenso die sekundären Zonen aus Modul 6 und die dynamisch aktualisierte Zone `branch.example.org` aus Modul 8 samt `include` des Schlüssels, denn BIND verlangt, dass alle Zonen in Views liegen) und hinterlegen Sie für `branch.example.org` im View `dmz` eine eigene Zonendatei `/etc/bind/db.branch.example.org.dmz`, in der `www.branch.example.org` auf `192.168.60.40` (statt `192.168.50.40`) zeigt.
   * Testen Sie von `CLI-TEST-01` aus die Auflösung von `www.branch.example.org` einmal gegen `192.168.50.11` (Quell-IP aus `.50.0/24`) und einmal gegen `192.168.60.11` (Quell-IP aus `.60.0/24`).
   * **Wichtige Bereinigung für nachfolgende Module:** Stellen Sie am Ende dieser Teilaufgabe auf `SRV-LIN-BIND` die gesicherte Konfiguration ohne Views wieder her (Dateien `named.conf.local` und `named.conf.default-zones`; die Änderungen in `named.conf.options` aus Aufgabe 1 bleiben bestehen) und führen Sie `rndc reload` aus, damit die Standard-Zonenstruktur für die Module 10 bis 12 einheitlich bleibt (oder behalten Sie den `internal`-View als primären Arbeits-View bei, sofern alle Zonen aus Modul 6 darin sauber geführt werden).
3. **Einrichten von DNS Query Resolution Policies auf `SRV-WIN-DNS`:**
   * Erstellen Sie auf `SRV-WIN-DNS` per PowerShell ein Client-Subnetz für das DMZ-Netz (`Add-DnsServerClientSubnet -Name "DMZ-Subnet" -IPv4Subnet "192.168.60.0/24"`).
   * Erstellen Sie in der Zone `corp.example.com` einen zusätzlichen Zonenscope (`Add-DnsServerZoneScope -ZoneName "corp.example.com" -Name "DMZ-Scope"`), fügen Sie darin für `files` die IP `192.168.60.20` ein (`Add-DnsServerResourceRecord -ZoneName "corp.example.com" -ZoneScope "DMZ-Scope" -A -Name "files" -IPv4Address "192.168.60.20"`) und aktivieren Sie die Richtlinie (`Add-DnsServerQueryResolutionPolicy -Name "DMZ-Policy" -Action ALLOW -ClientSubnet "eq,DMZ-Subnet" -ZoneScope "DMZ-Scope,1" -ZoneName "corp.example.com"`).
   * Prüfen Sie das Ergebnis durch Abfragen von `files.corp.example.com` über `192.168.50.10` vs. `192.168.60.10`. **Wichtige Bereinigung:** Entfernen Sie am Ende der Übung die Richtlinie `DMZ-Policy` (`Remove-DnsServerQueryResolutionPolicy`) und den Scope `DMZ-Scope`, damit in Modul 11 und 12 eine eindeutige Standardauflösung vorliegt.

#### Kontrollfragen

1. Welche zwingende Konfigurationsregel gilt in BIND 9, sobald Sie in der `named.conf` auch nur einen einzigen `view`-Block definieren?
2. Wie entscheidet BIND 9, welcher `view` für eine eingehende Client-Anfrage herangezogen wird, wenn die Quell-IP-Adresse des Clients theoretisch auf die `match-clients`-Liste von zwei verschiedenen Views passt?
3. Aus welchen drei logischen Bausteinen setzt sich eine Split-Brain-Konfiguration auf Basis von Windows Server DNS Policies zusammen?

---

### Modul 10: DNS-Sicherheit im Grundbetrieb, Härtung und Abgrenzung zu DNSSEC

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische Angriffsvektoren auf DNS-Infrastrukturen (Cache Poisoning/Spoofing, DNS Amplification/Reflection DDoS, Offene Rekursion, unautorisierte Zonentransfers) analysieren.
  * Nach Abschluss dieses Moduls kann der Lernende Härtungsmaßnahmen für den Grundbetrieb in Windows-DNS (Cache Locking, Socket Pool, Response Rate Limiting) und BIND 9 (Versionsverschleierung, Rate Limiting, Trennung von Rekursion und Autorität) umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende das Schutzziel von DNSSEC (Authentizität und Integrität von DNS-Antworten) im Überblick beschreiben und gegen verschlüsselte Transportprotokolle (DoT/DoH) abgrenzen (Hinweis: Die detaillierte Einrichtung von DNSSEC ist Bestandteil eines eigenen weiterführenden Lehrplans).
* **Voraussetzungen:** Abschluss der Module 1 bis 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **10.1** | Bedrohungslandschaft im DNS: Funktionsweise von DNS Cache Poisoning (Kaminsky-Angriff), DNS Amplification / Reflection DDoS über offene rekursive Resolver und DNS-Tunneling. | 2 |
| **10.2** | Härtung von Windows-DNS-Servern: Source Port Randomization (Socket Pool Size), DNS Cache Locking (Prozentsatz der TTL, während derer zwischengespeicherte Einträge nicht überschrieben werden können) und Aktivierung von Response Rate Limiting (RRL). | 2 |
| **10.3** | Härtung von BIND 9: Strikte Begrenzung von `allow-recursion` und `allow-query-cache`, Ausblenden der Versionsnummer (`version "unavailable";`), Konfiguration von `rate-limit` (Response Rate Limiting) und Betrieb im eingeschränkten Sicherheitskontext. | 2 |
| **10.4** | Konzeptüberblick und Abgrenzung (Out-of-Scope-Brücke): Was leistet DNSSEC (kryptografische Signatur von Resource Records über `RRSIG`, `DNSKEY`, `DS`) und was leistet es nicht (keine Verschlüsselung des Datenverkehrs)? Kurzer Ausblick auf DNS over TLS (DoT) und DNS over HTTPS (DoH). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Überprüfung und Härtung von `SRV-WIN-DNS`:**
   * Fragen Sie auf `SRV-WIN-DNS` per PowerShell die aktuellen Sicherheitsparameter ab (`Get-DnsServerSetting -All | Select-Object SocketPoolSize`, `Get-DnsServerCache | Select-Object LockingPercent` sowie `Get-DnsServerResponseRateLimiting`; Eigenschaftsnamen nicht bestätigt, bei Abweichung mit `Get-Member` prüfen).
   * Setzen Sie den Cache-Locking-Wert auf 100 % (`Set-DnsServerCache -LockingPercent 100`) und prüfen Sie die Konfiguration des Response Rate Limiting (RRL), indem Sie RRL im Modus `LogOnly` oder `Enable` konfigurieren (`Set-DnsServerResponseRateLimiting`).
2. **Versionsabfrage und Härtung von `SRV-LIN-BIND`:**
   * Fragen Sie von `CLI-TEST-01` aus die aktuelle BIND-Versionsnummer über die Chaos-Klasse ab (`dig @192.168.50.11 version.bind CHAOS TXT` bzw. `nslookup -q=txt -class=CHAOS version.bind 192.168.50.11`).
   * Fügen Sie auf `SRV-LIN-BIND` in `/etc/bind/named.conf.options` im `options`-Block die Direktiven `version "unavailable";`, `allow-recursion { lab-nets; };` sowie einen `rate-limit { responses-per-second 10; };`-Block ein. Prüfen Sie die Konfiguration mit `named-checkconf`, laden Sie BIND mit `rndc reload` neu und verifizieren Sie erneut von `CLI-TEST-01` aus, dass die echte Versionsnummer nicht mehr ausgegeben wird.

#### Kontrollfragen

1. Wie schützen die beiden Mechanismen „Source Port Randomization“ (zufällige Quellports bei ausgehenden Serverabfragen) und „DNS Cache Locking“ vor DNS-Cache-Poisoning-Angriffen?
2. Warum stellt ein aus dem Internet erreichbarer DNS-Server mit unbeschränkt aktivierter Rekursion (Open Resolver) eine erhebliche Gefahr für Dritte im Rahmen von DNS-Amplification-Angriffen dar?
3. Welches konkrete Sicherheitsproblem löst DNSSEC, und warum schützt DNSSEC allein nicht davor, dass ein Beobachter im lokalen Netzwerk mitlesen kann, welche Domänennamen ein Client auflöst?

---

### Modul 11: Systematische Fehlersuche, Diagnose und Monitoring (Windows & Linux)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Diagnosewerkzeuge `nslookup`, `Resolve-DnsName` und `dig` zielgerichtet mit erweiterten Parametern zur Eingrenzung von Auflösungsfehlern einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Serverprotokolle, Debug-Logs und Query-Logs sowohl unter Windows Server als auch unter BIND 9 aktivieren und auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende DNS-Datenverkehr auf Paketebene mitschneiden und typische Fehlerbilder (Replikationsstörungen, `REFUSED` durch fehlende Zugriffsregeln, Firewall-Blockaden, veraltete Seriennummern) systematisch beheben.
* **Voraussetzungen:** Abschluss der Module 1 bis 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **11.1** | Vergleich und Einsatz der Abfrage-Tools: `nslookup` (interaktiver Modus, `set type=...`, `set debug`), Windows PowerShell `Resolve-DnsName` (`-Type`, `-Server`, `-DnsOnly`, `-NoHostsFile`, `-NoRecursion`) und Linux `dig` (`@server`, `+short`, `+norecurse`, `+trace`, `-x` für Reverse-Lookups). | 3 |
| **11.2** | Server-Logging und Diagnose unter Windows Server: Ereignisanzeige (`Applications and Services Logs -> DNS Server`), analytisches DNS-Protokoll, Debug-Protokollierung (`Set-DnsServerDiagnostics`) und Auswertung von Leistungsindikatoren. | 2 |
| **11.3** | Server-Logging und Diagnose unter BIND 9: Konfiguration des `logging`-Blocks in `named.conf` (`channel` und `category`, z. B. `queries`, `xfer-in`, `xfer-out`, `security`), Aktivierung des Query-Loggings zur Laufzeit mit `rndc querylog` und Analyse mit `journalctl`. | 2 |
| **11.4** | Paketanalyse und strukturiertes Troubleshooting-Vorgehen: Mitschnitt von Port-53-Verkehr mit `tcpdump -i any port 53 -nn -vv`; typische Fehlerszenarien (Seriennummer nicht inkrementiert, Firewall blockiert TCP 53 bei AXFR, `REFUSED` wegen fehlender ACL, Endlosschleifen bei Weiterleitungen). | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tiefenanalyse von DNS-Antworten mit `dig` und `Resolve-DnsName`:** Führen Sie von `SRV-LIN-BIND` und `CLI-TEST-01` gezielte Abfragen ohne Rekursion (`dig @192.168.50.10 files.corp.example.com A +norecurse` bzw. `Resolve-DnsName files.corp.example.com -Server 192.168.50.10 -NoRecursion -DnsOnly`) sowie Reverse-Abfragen (`dig @192.168.50.10 -x 192.168.50.10`) durch. Analysieren Sie die Abschnitte `HEADER`, `QUESTION`, `ANSWER`, `AUTHORITY` und `ADDITIONAL` im Detail.
2. **Aktivieren des Query-Loggings und Paketmitschnitt auf `SRV-LIN-BIND`:** Schalten Sie auf `SRV-LIN-BIND` mit `rndc querylog on` die Protokollierung aller eingehenden Abfragen ein. Starten Sie parallel in einer zweiten SSH-/Terminal-Sitzung `tcpdump -i any port 53 -nn` und lösen Sie von `CLI-TEST-01` mehrere Abfragen aus. Deaktivieren Sie das Query-Log am Ende wieder mit `rndc querylog off`. Aktivieren Sie außerdem auf `SRV-WIN-DNS` die Debug-Protokollierung mit Protokolldatei (`Set-DnsServerDiagnostics`, Parameter siehe `Get-Help Set-DnsServerDiagnostics`, oder GUI: Eigenschaften des DNS-Servers, Reiter „Debugprotokollierung“; Parameternamen nicht bestätigt), lösen Sie von `CLI-TEST-01` einige Abfragen aus, werten Sie die Protokolldatei und das Ereignisprotokoll `DNS Server` aus und schalten Sie die Debug-Protokollierung danach wieder aus.
3. **Troubleshooting-Labor (Fehlersuche an drei simulierten Störungen):**
   * *Szenario A:* Blockieren Sie auf `SRV-WIN-DNS` temporär in der Windows Defender Firewall eingehend den **TCP**-Port 53 (während UDP 53 offen bleibt). Lösen Sie auf `SRV-LIN-BIND` mit `rndc retransfer corp.example.com` einen Zonentransfer aus, diagnostizieren Sie das Scheitern des Transfers im BIND-Log und per `dig @192.168.50.10 corp.example.com AXFR` und nehmen Sie die Firewall-Blockade danach wieder zurück.
   * *Szenario B:* Ändern Sie in `/var/lib/bind/db.branch.example.org` (nach `rndc freeze`) einen `A`-Record, ohne die Seriennummer im SOA-Record zu erhöhen, und führen Sie `rndc thaw` sowie `rndc reload` aus. Überprüfen Sie auf `SRV-WIN-DNS`, warum die sekundäre Zone den neuen Wert nicht übernimmt, und korrigieren Sie den Fehler durch Inkrementieren der Seriennummer.
   * *Szenario C:* Entfernen Sie auf `SRV-LIN-BIND` in `/etc/bind/named.conf.options` temporär das Netz `192.168.50.0/24` aus der ACL `lab-nets` (Sicherungskopie der Datei vorher anlegen) und laden Sie mit `rndc reload` neu. Fragen Sie von `CLI-TEST-01` aus `Resolve-DnsName www.branch.example.org -Server 192.168.50.11` ab, diagnostizieren Sie den Antwortcode `REFUSED` mit Query-Log und `journalctl -u named` und stellen Sie danach die gesicherte Datei wieder her (`rndc reload`, Kontrollabfrage).

#### Kontrollfragen

1. Ein DNS-Server beantwortet normale `A`- und `AAAA`-Anfragen von einem sekundären Server problemlos, aber die Zonenübertragung (`AXFR`) zwischen denselben beiden Servern schlägt mit einem Verbindungsfehler (Connection Reset / Timeout) fehl. Welche Netzwerkursache liegt hier am wahrscheinlichsten vor?
2. Welcher Parameter von `Resolve-DnsName` stellt sicher, dass bei der Fehlersuche weder die lokale `hosts`-Datei noch LLMNR oder NetBIOS verwendet werden, sondern ausschließlich eine reine DNS-Abfrage erfolgt?
3. Worin liegt der Unterschied im Antwortverhalten eines DNS-Servers, wenn Sie ihn mit `dig @server name +norecurse` abfragen, im Vergleich zu einer Standardabfrage mit `dig @server name`?
4. Wie können Sie in BIND 9 im laufenden Betrieb ohne Bearbeitung von Konfigurationsdateien die Protokollierung sämtlicher eingehender DNS-Abfragen vorübergehend ein- und wieder ausschalten?

---

### Modul 12: Integriertes Abschlussprojekt: Hybride DNS-Infrastruktur (Windows & BIND 9)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine redundante, plattformübergreifende DNS-Architektur aus Windows Server und Linux BIND 9 nach einer schriftlichen Anforderungsspezifikation selbstständig planen, implementieren und absichern.
  * Nach Abschluss dieses Moduls kann der Lernende die gesamte Konfiguration anhand eines strukturierten Abnahmeprotokolls testen und für den Betrieb dokumentieren.
* **Voraussetzungen:** Abschluss der Module 1 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **12.1** | Projektbriefing und Architekturentwurf: Analyse der Anforderungen der fiktiven „AlpenTech GmbH“ (Hauptsitz mit Windows AD/DNS `hq.alpentech.internal`, Linux-Entwicklungsstandort mit BIND 9 `dev.alpentech.internal`). | 2 |
| **12.2** | Praktische Implementierung der Gesamtarchitektur: Einrichtung der Forward- und Reverse-Zonen (IPv4 & IPv6), gegenseitige sekundäre Zonen zur Ausfallsicherheit, Härtung und Zugriffskontrolle. | 4 |
| **12.3** | Abnahmetest (Peer-Review / Selbsttest), Ausfallsimulation (Abschalten jeweils eines DNS-Servers) und Erstellung einer kompakten Betriebsdokumentation. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbau der hybriden Projektumgebung „AlpenTech GmbH“:** Formulieren Sie zunächst aus den folgenden Vorgaben eine kurze schriftliche Anforderungsspezifikation (Zonen, Zonentypen, Transferbeschränkungen, Testfälle), die als Grundlage für den Abnahmetest dient.
   * Richten Sie auf `SRV-WIN-DNS` (`192.168.50.10` / `fd00:50::10`) die primäre Zone `hq.alpentech.internal` und auf `SRV-LIN-BIND` (`192.168.50.11` / `fd00:50::11`) die primäre Zone `dev.alpentech.internal` ein.
   * Konfigurieren Sie gegenseitige sekundäre Zonen: `SRV-LIN-BIND` hält eine sekundäre Kopie von `hq.alpentech.internal`, während `SRV-WIN-DNS` eine sekundäre Kopie von `dev.alpentech.internal` hält. Sichern Sie die Zonenübertragungen strikt auf die jeweilige Partner-IP ab.
   * Legen Sie in beiden Zonen jeweils mindestens drei `A`- und `AAAA`-Records, einen `CNAME`, einen `MX`-Record, einen `TXT`-Record, einen `SRV`-Record sowie die korrespondierenden `PTR`-Records in den Reverse-Zonen (`50.168.192.in-addr.arpa` und `0.0.0.0.0.0.0.0.0.5.0.0.0.0.d.f.ip6.arpa`) an.
2. **Hochverfügbarkeitstest und Abnahme von `CLI-TEST-01`:**
   * Tragen Sie auf `CLI-TEST-01` als primären DNS-Server `192.168.50.10` und als sekundären DNS-Server `192.168.50.11` ein (nur für diesen Test: `CLI-TEST-01` ist seit Modul 8 Domänenmitglied und `SRV-LIN-BIND` kennt die AD-`SRV`-Einträge nicht, siehe Modul 8, Kontrollfrage 2).
   * Überprüfen Sie die vollständige Vorwärts- und Rückwärtsauflösung aller angelegten Einträge beider Zonen.
   * Beenden Sie testweise den DNS-Dienst auf `SRV-WIN-DNS` (`Stop-Service DNS`), leeren Sie den Client-Cache auf `CLI-TEST-01` (`ipconfig /flushdns`) und weisen Sie nach, dass sämtliche Einträge aus `hq.alpentech.internal` und `dev.alpentech.internal` weiterhin unterbrechungsfrei über `SRV-LIN-BIND` aufgelöst werden. Starten Sie anschließend den Dienst auf `SRV-WIN-DNS` wieder (`Start-Service DNS`). **Bereinigung:** Entfernen Sie den sekundären DNS-Eintrag `192.168.50.11` auf `CLI-TEST-01` wieder, damit die Domänenanmeldung nicht durch einen DNS-Server ohne AD-Einträge gestört wird.
3. **Erstellung der Betriebsdokumentation:** Dokumentieren Sie in einer strukturierten Übersicht alle eingerichteten Zonen, Zonentypen, Master-/Slave-Beziehungen, SOA-Parameter sowie die durchgeführten Härtungsmaßnahmen.

#### Kontrollfragen

1. Warum ist es für die Ausfallsicherheit eines Standorts entscheidend, dass Clients beide DNS-Server (`SRV-WIN-DNS` und `SRV-LIN-BIND`) in ihrer Netzwerkkonfiguration eingetragen haben (bei domänenverbundenen Clients nur, wenn beide Server auch die AD-Einträge auflösen können), und beide Server sämtliche internen Zonen (entweder primär, sekundär oder über redundante Weiterleitungen) auflösen können?
2. Welche Prüfschritte führen Sie vor der Übergabe einer neu eingerichteten DNS-Infrastruktur in den Produktivbetrieb durch, um sicherzustellen, dass sowohl die Zonensyntax als auch die Replikation und die Zugriffskontrolle fehlerfrei arbeiten?
3. Wie verhalten sich sekundäre Zonen auf `SRV-LIN-BIND`, wenn der primäre Server `SRV-WIN-DNS` länger ausfällt als die im SOA-Record definierte `Expire`-Zeitspanne?

---

## C. Änderungsvermerk (Korrektur nach Prüfung)

Dieses Dokument wurde nach einer fachlichen Prüfung der ersten Fassung korrigiert. Stunden, Prioritäten, Modulreihenfolge und Quellenliste blieben unverändert (112 UE; 9 Module Priorität 1 mit 86 UE, 3 Module Priorität 2 mit 26 UE).

| Stelle | Änderung |
| :--- | :--- |
| A.3 Labor-Setup | Client-VM: Windows ab Modul 1 erforderlich (statt „oder Linux“); Server-Zusatzadressen `192.168.60.10` und `192.168.60.11` ab Modul 9 ergänzt; `tcpdump` erst ab Modul 11 erforderlich. |
| Modul 6 | Lernziel zu TSIG auf BIND beschränkt und um die Begründung ergänzt, warum TSIG zwischen Windows-DNS und BIND nicht einsetzbar ist (nicht bestätigt); Einheit 6.3 angepasst; neue Praxisaufgabe 4 (TSIG an separater Testzone, mit Bereinigung). |
| Modul 9 | Aufgabe 1: Lauschadressen (Windows und BIND) und `allow-query` für das zweite Subnetz ergänzt, sonst wären die Abfragen an `192.168.60.10` und `192.168.60.11` nicht beantwortet worden; Aufgabe 2: Hinweis auf alle Zonen in Views und genauere Bereinigung. |
| Modul 10 | Einheit 10.3 und Aufgabe 2 nutzen jetzt dieselbe Direktive `version "unavailable";`; Cmdlet für Cache Locking korrigiert (Eigenschaftsnamen nicht bestätigt). |
| Modul 11 | Lernziel an die Aufgaben angepasst; Windows-Debug-Protokollierung als Aufgabe ergänzt; dritte Störung (Szenario C, `REFUSED`) ergänzt. |
| Modul 12 | Einheiten 12.1 und 12.2 an die Aufgaben angepasst (DMZ-Zone und bedingte Weiterleitungen entfallen); schriftliche Anforderungsspezifikation als Teil von Aufgabe 1; sekundärer DNS-Eintrag am Domänenclient nur als Test mit Bereinigung; Kontrollfrage 1 ergänzt. |

**Nicht bestätigt und vor dem Einsatz im Lab zu prüfen:** Parameternamen von `Set-DnsServerSetting -ListenAddresses` und `Set-DnsServerDiagnostics`, Eigenschaftsnamen von `Get-DnsServerCache`, `Get-DnsServerSetting` und `Get-DnsServerResponseRateLimiting`, die Aussage zu TSIG und Windows-DNS sowie die Laufzeiten der Evaluationsversionen. Die Quellen von Microsoft und ISC sind weiterhin als „nicht geprüft“ markiert.
