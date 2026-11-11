# Lehrplan: DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea)

| Parameter | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IPv4-Adressen, Subnetze, Standardgateway, grundlegende Bedienung von Windows- und Linux-Kommandozeilen, Umgang mit Hyper-V) |
| **Gesamtumfang** | 12 Module, 116 Unterrichtseinheiten (UE zu je 45 Minuten) |
| **Fokus-Technologien** | Windows Server (DHCP-Server-Rolle, PowerShell-Modul `DhcpServer`), Debian GNU/Linux bzw. Ubuntu Server mit ISC Kea (`kea-dhcp4`, `kea-dhcp6`), DHCP-Relay unter Linux, DHCPv4 und DHCPv6 |
| **Thematische Abgrenzung (Out of Scope)** | DNS-Betrieb (Zonen, Ressourceneinträge) ist ein eigener Lehrplan (DNS-Grundlagen) und wird nur an der Schnittstelle der dynamischen Updates behandelt; DNSSEC, PXE-Netzwerkstart und Betriebssystem-Rollout (WDS, MDT, MECM), IP-Adressverwaltung mit IPAM-Werkzeugen, 802.1X und Netzwerkzugangskontrolle, WLAN-Controller sowie die DHCP-Funktionen von Heimroutern und Cloud-Diensten gehören nicht zum Kurs. Switch-Funktionen wie DHCP Snooping werden nur konzeptionell behandelt. |

---

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| **1** | Grundlagen von DHCP, Lease-Ablauf und Laboraufbau | 1 | 8 |
| **2** | Windows-DHCP-Server: Installation, Scopes und Basisoptionen | 1 | 10 |
| **3** | Leases, Reservierungen und Ausschlüsse | 1 | 8 |
| **4** | Optionen, Klassen, Policies und MAC-Filter | 1 | 10 |
| **5** | Mehrere Subnetze und DHCP-Relay | 1 | 10 |
| **6** | DHCP in Active Directory: Autorisierung und dynamische DNS-Updates | 1 | 10 |
| **7** | Hochverfügbarkeit: DHCP-Failover und Split-Scope | 1 | 10 |
| **8** | DHCP unter Linux mit ISC Kea | 1 | 10 |
| **9** | DHCPv6 und IPv6-Adressvergabe | 2 | 10 |
| **10** | Betrieb: Überwachung, Sicherung, Migration und Dokumentation | 1 | 8 |
| **11** | Sicherheit: Rogue-DHCP, Zugriffsschutz und Härtung | 2 | 10 |
| **12** | Fehlersuche und integriertes Abschlussprojekt | 1 | 12 |
| **Gesamt** | **12 Module (10x Priorität 1, 2x Priorität 2)** | **1: 96 UE / 2: 20 UE** | **116** |

*Hinweis zur Priorisierung:* Module der **Priorität 1 (Pflicht / Kernkompetenz, 96 UE)** vermitteln alles, was für Einrichtung, Betrieb und Fehlersuche von DHCP in einer gemischten Windows-/Linux-Umgebung mit mehreren Subnetzen nötig ist. Module der **Priorität 2 (Vertiefung / Optional, 20 UE)** behandeln DHCPv6 und das Thema Sicherheit. Kein Pflichtmodul setzt ein Modul der Priorität 2 voraus.

### 2. Quellen

Hinweis zur Prüfung: Die RFC-Angaben (Titel, Autoren, Datum) stammen aus dem Wissensstand des Autors; die RFC-Adressen konnten in der Erstellungssitzung nicht abgerufen werden und sind als `nicht geprüft` gekennzeichnet. Die Microsoft-Learn-Seiten wurden am 2026-11-12 über die Microsoft-Learn-Suche aufgefunden (Inhalt gelesen, Versionsstand der Seiten nicht geprüft).

* **RFC 951 – Bootstrap Protocol (BOOTP)**, Herausgeber: IETF (B. Croft, J. Gilmore), Datum: September 1985, URL: https://datatracker.ietf.org/doc/html/rfc951 (nicht geprüft)
* **RFC 1542 – Clarifications and Extensions for the Bootstrap Protocol**, Herausgeber: IETF (W. Wimer), Datum: Oktober 1993, URL: https://datatracker.ietf.org/doc/html/rfc1542 (nicht geprüft)
* **RFC 1918 – Address Allocation for Private Internets**, Herausgeber: IETF (Y. Rekhter et al.), Datum: Februar 1996, URL: https://datatracker.ietf.org/doc/html/rfc1918 (nicht geprüft)
* **RFC 2131 – Dynamic Host Configuration Protocol**, Herausgeber: IETF (R. Droms), Datum: März 1997, URL: https://datatracker.ietf.org/doc/html/rfc2131 (nicht geprüft)
* **RFC 2132 – DHCP Options and BOOTP Vendor Extensions**, Herausgeber: IETF (S. Alexander, R. Droms), Datum: März 1997, URL: https://datatracker.ietf.org/doc/html/rfc2132 (nicht geprüft)
* **RFC 2606 – Reserved Top Level DNS Names**, Herausgeber: IETF (D. Eastlake, A. Panitz), Datum: Juni 1999, URL: https://datatracker.ietf.org/doc/html/rfc2606 (nicht geprüft)
* **RFC 3046 – DHCP Relay Agent Information Option**, Herausgeber: IETF (M. Patrick), Datum: Januar 2001, URL: https://datatracker.ietf.org/doc/html/rfc3046 (Adresse über Suchergebnis bestätigt)
* **RFC 3397 – Dynamic Host Configuration Protocol (DHCP) Domain Search Option**, Herausgeber: IETF (B. Aboba, S. Cheshire), Datum: November 2002, URL: https://datatracker.ietf.org/doc/html/rfc3397 (nicht geprüft)
* **RFC 3442 – The Classless Static Route Option for Dynamic Host Configuration Protocol (DHCP) version 4**, Herausgeber: IETF (T. Lemon et al.), Datum: Dezember 2002, URL: https://datatracker.ietf.org/doc/html/rfc3442 (nicht geprüft)
* **RFC 3646 – DNS Configuration options for Dynamic Host Configuration Protocol for IPv6 (DHCPv6)**, Herausgeber: IETF (R. Droms), Datum: Dezember 2003, URL: https://datatracker.ietf.org/doc/html/rfc3646 (nicht geprüft)
* **RFC 3849 – IPv6 Address Prefix Reserved for Documentation**, Herausgeber: IETF (G. Huston et al.), Datum: Juli 2004, URL: https://datatracker.ietf.org/doc/html/rfc3849 (nicht geprüft)
* **RFC 3927 – Dynamic Configuration of IPv4 Link-Local Addresses**, Herausgeber: IETF (S. Cheshire et al.), Datum: Mai 2005, URL: https://datatracker.ietf.org/doc/html/rfc3927 (nicht geprüft)
* **RFC 4193 – Unique Local IPv6 Unicast Addresses**, Herausgeber: IETF (R. Hinden, B. Haberman), Datum: Oktober 2005, URL: https://datatracker.ietf.org/doc/html/rfc4193 (nicht geprüft)
* **RFC 4702 – The Dynamic Host Configuration Protocol (DHCP) Client Fully Qualified Domain Name (FQDN) Option**, Herausgeber: IETF (M. Stapp et al.), Datum: Oktober 2006, URL: https://datatracker.ietf.org/doc/html/rfc4702 (nicht geprüft)
* **RFC 4703 – Resolution of Fully Qualified Domain Name (FQDN) Conflicts among Dynamic Host Configuration Protocol (DHCP) Clients**, Herausgeber: IETF (M. Stapp, B. Volz), Datum: Oktober 2006, URL: https://datatracker.ietf.org/doc/html/rfc4703 (nicht geprüft)
* **RFC 4861 – Neighbor Discovery for IP version 6 (IPv6)**, Herausgeber: IETF (T. Narten et al.), Datum: September 2007, URL: https://datatracker.ietf.org/doc/html/rfc4861 (nicht geprüft)
* **RFC 4862 – IPv6 Stateless Address Autoconfiguration**, Herausgeber: IETF (S. Thomson et al.), Datum: September 2007, URL: https://datatracker.ietf.org/doc/html/rfc4862 (nicht geprüft)
* **RFC 5227 – IPv4 Address Conflict Detection**, Herausgeber: IETF (S. Cheshire), Datum: Juli 2008, URL: https://datatracker.ietf.org/doc/html/rfc5227 (nicht geprüft)
* **RFC 8415 – Dynamic Host Configuration Protocol for IPv6 (DHCPv6)**, Herausgeber: IETF (T. Mrugalski et al.), Datum: November 2018, URL: https://datatracker.ietf.org/doc/html/rfc8415 (nicht geprüft)
* **DHCP Server (Windows Server) – Quickstart: Install and configure DHCP Server**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server (über Suche aufgefunden)
* **DHCP scopes**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/dhcp-scopes (über Suche aufgefunden)
* **DHCP failover overview**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/dhcp-failover (über Suche aufgefunden)
* **Manage DHCP failover relationships in Windows Server**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/manage-dhcp-failover-relationships (über Suche aufgefunden)
* **Replicate DHCP failover**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/replicate-dhcp-failover (über Suche aufgefunden)
* **Migrate existing DHCP failover deployment**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/migrate-existing-dhcp-failover (über Suche aufgefunden)
* **Deploy DHCP Using Windows PowerShell**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/windows-server/networking/technologies/dhcp/dhcp-deploy-wps (über Suche aufgefunden)
* **DHCP troubleshooting guidance**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/troubleshoot/windows-server/networking/troubleshoot-dhcp-guidance (über Suche aufgefunden)
* **DhcpServer PowerShell Module Reference**, Herausgeber: Microsoft Corporation (Microsoft Learn), Version: Stand nicht geprüft, URL: https://learn.microsoft.com/powershell/module/dhcpserver/ (über Suche aufgefunden)
* **Kea Administrator Reference Manual (ARM)**, Herausgeber: Internet Systems Consortium (ISC), Version: Stand nicht geprüft, URL: https://kea.readthedocs.io/ (nicht geprüft)
* **Kea end of life dates**, Herausgeber: Internet Systems Consortium (ISC), Version: Stand nicht geprüft, URL: https://kb.isc.org/docs/kea-end-of-life-dates (am 2026-11-12 abgerufen; die Seite nennt die Zweige 2.6 und 3.1 mit Ende der Unterstützung im Juni bzw. Juli 2026, daher ist die aktuell unterstützte Kea-Version vor Kursbeginn zu prüfen)
* **ISC DHCP (dhcrelay, isc-dhcp-relay)**: Keine geprüfte Quelle. Dass die Wartung von ISC DHCP eingestellt wurde, ist nicht bestätigt und vor dem Einsatz zu prüfen.

### 3. Labor-Setup & Rahmenbedingungen

Alle Übungen laufen in einer vollständig isolierten Hyper-V-Umgebung. Keine VM darf mit dem Heim- oder Produktivnetz verbunden sein, weil ein DHCP-Server im Labor sonst fremde Geräte mit Adressen versorgen oder stören könnte. Auf dem Hyper-V-Host darf kein Switch des Labors mit einer physischen Netzwerkkarte verbunden werden.

#### Virtuelle Netzwerke (Hyper-V) und Adressplan
* **`vSwitch-Server`** (Typ **Privat**, **erforderlich ab Modul 1**): Netz A `192.168.10.0/24` nach RFC 1918, Server-Segment.
* **`vSwitch-ClientA`** (Typ **Privat**, **erforderlich ab Modul 1**, genutzt ab Modul 5): Netz B `192.168.20.0/24`.
* **`vSwitch-ClientB`** (Typ **Privat**, **erforderlich ab Modul 1**, genutzt ab Modul 8): Netz C `192.168.30.0/24`.
* **IPv6 (erforderlich ab Modul 9, nur Priorität 2):** Unique-Local-Präfixe nach RFC 4193: `fd00:10::/64` (Netz A), `fd00:20::/64` (Netz B), `fd00:30::/64` (Netz C).
* **Reservierte Labor-Domäne:** `corp.example.com` (RFC 2606), Active Directory ab Modul 6.
* **Internetphase (vor Modul 1, danach Rückbau):** Die Pakete und Medien werden vor dem Trennen vom Netz bereitgestellt (siehe VM-Liste). Dazu erhält jede betroffene Linux-VM vorübergehend einen zusätzlichen Netzwerkadapter an einem externen Switch mit Internetzugang; nach der Installation wird dieser Adapter entfernt und ein Checkpoint `BASIS` erstellt. Windows-Rollen (DHCP, AD DS, DNS) kommen aus dem lokalen Komponentenspeicher; ob dafür Internet nötig ist, ist nicht bestätigt.

#### Virtuelle Maschinen (VMs)
1. **`RTR-LIN` (Linux-Router und Relay)**, **erforderlich ab Modul 1**
   * **Betriebssystem:** Debian GNU/Linux 12 oder Ubuntu Server 24.04 LTS, ohne grafische Oberfläche.
   * **Ressourcen:** 1 vCPU, 1 GB RAM, 10 GB VHDX, drei vNICs: an `vSwitch-Server` (`192.168.10.1/24`), `vSwitch-ClientA` (`192.168.20.1/24`), `vSwitch-ClientB` (`192.168.30.1/24`); IPv6-Adressen ab Modul 9 (`fd00:10::1`, `fd00:20::1`, `fd00:30::1`).
   * **Pakete (in der Internetphase installieren):** `tcpdump` (**erforderlich ab Modul 1**); `isc-dhcp-relay` (**erforderlich ab Modul 5**); `radvd` (**erforderlich ab Modul 9**). Paketnamen und Verfügbarkeit je Distribution: nicht bestätigt.
2. **`SRV-WIN-DHCP1` (Windows Server)**, **erforderlich ab Modul 2**
   * **Betriebssystem:** Windows Server 2022 oder 2025 Standard (offizielle Evaluationsversion, 180 Tage; Laufzeit vor Beginn prüfen), mit Desktopdarstellung.
   * **Ressourcen:** 2 vCPUs, 4 GB RAM, 60 GB VHDX, 1 vNIC an `vSwitch-Server`, IPv4 `192.168.10.11/24`, Gateway `192.168.10.1` (IPv6 `fd00:10::11/64` ab Modul 9).
   * **Rolle:** `DHCP` (ab Modul 2). Bis Modul 6 Mitglied einer Arbeitsgruppe, danach Domänenmitglied von `corp.example.com`.
3. **`SRV-WIN-DC1` (Windows Server, Domänencontroller)**, **erforderlich ab Modul 6**
   * **Betriebssystem:** wie `SRV-WIN-DHCP1`; 2 vCPUs, 4 GB RAM, 60 GB VHDX, `vSwitch-Server`, IPv4 `192.168.10.10/24` (IPv6 `fd00:10::10/64` ab Modul 9).
   * **Rollen:** `AD-Domain-Services` und `DNS` (werden in Modul 6 per Aufgabe installiert).
4. **`SRV-WIN-DHCP2` (Windows Server)**, **erforderlich ab Modul 7**: wie `SRV-WIN-DHCP1`, IPv4 `192.168.10.12/24`, Domänenmitglied; Rolle `DHCP` wird in Modul 7 per Aufgabe installiert.
5. **`SRV-LIN-KEA` (Linux-Server)**, **erforderlich ab Modul 8**
   * **Betriebssystem:** Debian GNU/Linux 12 oder Ubuntu Server 24.04 LTS; 1 vCPU, 2 GB RAM, 20 GB VHDX, `vSwitch-Server`, IPv4 `192.168.10.21/24`, Gateway `192.168.10.1` (IPv6 `fd00:10::21/64` ab Modul 9).
   * **Pakete (in der Internetphase installieren):** `kea-dhcp4-server` (**ab Modul 8**), `kea-dhcp6-server` (**ab Modul 9**), `tcpdump` (**ab Modul 11**). Kea-Version: die der Distribution, Versionsstand nicht geprüft.
6. **`CLI-WIN-A` (Windows-Client)**, **erforderlich ab Modul 1**
   * **Betriebssystem:** Windows 11 Enterprise (Evaluationsversion, Laufzeit vor Beginn prüfen); 2 vCPUs, 4 GB RAM, 60 GB VHDX. Modul 1 bis 4: 1 vNIC an `vSwitch-Server`; ab Modul 5: an `vSwitch-ClientA` (dauerhaft). DHCP-Client, keine statische Adresse. Domänenbeitritt in Modul 6.
7. **`CLI-LIN-B` (Linux-Client)**, **erforderlich ab Modul 8**: Ubuntu Server 24.04 LTS (Netzwerkkonfiguration mit netplan und `systemd-networkd`); 1 vCPU, 1 GB RAM, 10 GB VHDX, 1 vNIC an `vSwitch-ClientB` (dauerhaft), DHCP-Client.

*Passwörter:* Alle Passwörter (Administrator, Wiederherstellungsmodus, Testkonten) werden bei der Aufgabe interaktiv gesetzt und weder in Skripten noch in Dokumentation abgelegt. *Checkpoints:* Vor jedem Modul mit zerstörerischen oder rückzubauenden Änderungen wird auf den betroffenen VMs ein Checkpoint `M<Nr>-Anfang` erstellt.

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen von DHCP, Lease-Ablauf und Laboraufbau

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum DHCP gegenüber statischer Adressvergabe eingesetzt wird, und die Entwicklung von BOOTP (RFC 951, RFC 1542) zu DHCP (RFC 2131) skizzieren.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf DISCOVER, OFFER, REQUEST, ACK sowie die Nachrichten NAK, DECLINE, RELEASE und INFORM beschreiben und die UDP-Ports 67 und 68 zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende aus einer Lease-Dauer die Zeitpunkte für Erneuerung (T1) und erneute Bindung (T2) berechnen und das Verhalten bei Fehlen eines DHCP-Servers (Link-Local-Adresse nach RFC 3927) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die virtuellen Switches und den Linux-Router des Labors aufbauen und einen DHCP-Mitschnitt mit `tcpdump` lesen.
* **Voraussetzungen:** Grundkenntnisse in TCP/IP, Subnetzmasken und der Kommandozeile unter Windows und Linux; Hyper-V ist auf dem Host aktiviert.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **1.1** | Warum DHCP: Probleme statischer Adressierung, vergebene Parameter (Adresse, Maske, Gateway, DNS), historische Entwicklung BOOTP (RFC 951, RFC 1542) zu DHCP (RFC 2131). | 2 |
| **1.2** | Der DORA-Ablauf: DISCOVER, OFFER, REQUEST, ACK; weitere Nachrichten NAK, DECLINE, RELEASE, INFORM; Broadcast-Verhalten, Transaktions-ID, Server-Identifier, UDP-Ports 67 (Server) und 68 (Client). | 2 |
| **1.3** | Lease-Lebenszyklus: Lease-Dauer, Erneuerung bei T1 (Standard 50 %) und erneute Bindung bei T2 (Standard 87,5 %), Verhalten bei Ablauf; Adresskonflikterkennung (RFC 5227) und Link-Local-Adresse 169.254.0.0/16 (RFC 3927). | 2 |
| **1.4** | DHCP-Optionen im Überblick (RFC 2132): Aufbau einer Option (Code, Länge, Wert), wichtige Optionen (Subnetzmaske, Router, DNS-Server, Domänenname, Lease-Zeit, Nachrichtentyp, Server-Identifier, Parameter Request List, Client-Identifier). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Laboraufbau:** Erstellen Sie auf dem Hyper-V-Host die drei privaten Switches `vSwitch-Server`, `vSwitch-ClientA` und `vSwitch-ClientB` (z. B. mit `New-VMSwitch -Name vSwitch-Server -SwitchType Private`). Legen Sie `RTR-LIN` mit drei Netzwerkadaptern an, vergeben Sie die statischen Adressen aus dem Adressplan und aktivieren Sie die Weiterleitung (`sysctl net.ipv4.ip_forward=1`, dauerhaft über eine Datei unter `/etc/sysctl.d/`). Stellen Sie sicher, dass der Internet-Adapter aus der Internetphase entfernt ist, und erstellen Sie den Checkpoint `BASIS`. Verbinden Sie `CLI-WIN-A` mit `vSwitch-Server`.
2. **Verhalten ohne DHCP-Server:** Stellen Sie auf `CLI-WIN-A` den Adapter auf automatische Adressvergabe und starten Sie auf `RTR-LIN` einen Mitschnitt (`tcpdump -n -vv -i <Schnittstelle-Netz-A> port 67 or port 68`). Beobachten Sie mit `ipconfig /all`, welche Adresse der Client nach einer Wartezeit erhält, und notieren Sie, wie oft und in welchen Abständen DISCOVER-Pakete erscheinen.
3. **Analyse einer DISCOVER-Nachricht:** Werten Sie ein DISCOVER aus Aufgabe 2 aus: Quell- und Zieladresse, Ports, MAC-Adresse des Clients, Transaktions-ID, Parameter Request List und gesendeter Hostname. Ordnen Sie jede Angabe einer Option aus Einheit 1.4 zu. Die Darstellung des Mitschnitts hängt von der `tcpdump`-Version ab (nicht bestätigt).

#### Kontrollfragen

1. Welche Ports verwenden DHCP-Server und -Client, und warum sendet der Client sein erstes DISCOVER an die Broadcast-Adresse?
2. Eine Lease dauert 8 Stunden. Zu welchen Zeitpunkten versucht der Client unter Standardwerten die Erneuerung (T1) und die erneute Bindung (T2)?
3. Warum erhält ein Client ohne erreichbaren DHCP-Server eine Adresse aus 169.254.0.0/16, und was bedeutet das für die Fehlersuche?
4. Wozu dient die Parameter Request List in DISCOVER und REQUEST?
5. In welchen Situationen sendet ein Server ein NAK und ein Client ein DECLINE?

---

### Modul 2: Windows-DHCP-Server: Installation, Scopes und Basisoptionen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die DHCP-Server-Rolle unter Windows Server per GUI und PowerShell installieren und die Sicherheitsgruppen sowie die Netzwerkbindung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen IPv4-Scope mit Adressbereich, Subnetzmaske, Lease-Dauer und Aktivierung planen und anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Server- und Scope-Optionen (Router, DNS-Server, Domänenname) setzen und deren Vorrang erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen DORA-Austausch im Mitschnitt mit den Einträgen der Lease-Tabelle auf dem Server vergleichen.
* **Voraussetzungen:** Abschluss von Modul 1 (Laboraufbau, `RTR-LIN`, `CLI-WIN-A`); Grundkenntnisse in der Verwaltung von Windows Server und der PowerShell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **2.1** | Architektur des Windows-DHCP-Servers: Dienst `DHCPServer`, Konsole `dhcpmgmt.msc`, PowerShell-Modul `DhcpServer`, Datenbank- und Protokollverzeichnis unter `%SystemRoot%\System32\dhcp` (Pfad nicht bestätigt). | 2 |
| **2.2** | Installation der Rolle per GUI und PowerShell (`Install-WindowsFeature DHCP -IncludeManagementTools`), Sicherheitsgruppen `DHCP Administrators` und `DHCP Users` (`netsh dhcp add securitygroups`), Bindung an Netzwerkschnittstellen. | 2 |
| **2.3** | Scope-Planung und -Anlage: Adressbereich, Subnetzmaske, Ausschlüsse, Lease-Dauer, Aktivierung (`Add-DhcpServerv4Scope`); Unterschied zwischen aktiviertem und inaktivem Scope. | 2 |
| **2.4** | Basisoptionen: Router (Option 3), DNS-Server (Option 6), DNS-Domänenname (Option 15); Optionsebenen Server und Scope, Vorrang (`Set-DhcpServerv4OptionValue`). | 2 |
| **2.5** | Erster Lease und Mitschnitt: DORA im Mitschnitt, Lease-Tabelle (`Get-DhcpServerv4Lease`), Client-Sicht (`ipconfig /all`). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Installation auf `SRV-WIN-DHCP1`:** Erstellen Sie den Checkpoint `M2-Anfang`. Installieren Sie die Rolle `DHCP` per PowerShell, legen Sie die Sicherheitsgruppen an, starten Sie den Dienst `DHCPServer` neu, prüfen Sie ihn mit `Get-Service DHCPServer` und die Bindung an die Netzwerkschnittstelle mit `Get-DhcpServerv4Binding`. Der Server ist in dieser Phase Mitglied einer Arbeitsgruppe; ob er dort ohne Autorisierung Adressen vergibt, ist nicht bestätigt und wird in dieser Aufgabe beobachtet und notiert.
2. **Scope für Netz A:** Legen Sie den Scope `Netz-A` an: Bereich `192.168.10.100` bis `192.168.10.199`, Maske `255.255.255.0`, Lease-Dauer 8 Stunden, Option Router `192.168.10.1`, Option DNS-Server `192.168.10.10` (der Domänencontroller entsteht erst in Modul 6; bis dahin dient die Option nur der Anzeige) und Domänenname `corp.example.com`. Aktivieren Sie den Scope.
3. **Erster Lease mit Mitschnitt:** Starten Sie den Mitschnitt auf `RTR-LIN` (Netz A) und führen Sie auf `CLI-WIN-A` `ipconfig /release` und `ipconfig /renew` aus. Identifizieren Sie die vier DORA-Nachrichten, vergleichen Sie die angebotene Adresse und die Optionen mit `ipconfig /all` und mit `Get-DhcpServerv4Lease -ScopeId 192.168.10.0`.
4. **Vorrang von Optionen:** Setzen Sie auf Serverebene die Option DNS-Server auf `192.168.10.99`, erneuern Sie den Lease auf `CLI-WIN-A` und prüfen Sie, welcher Wert gilt. Entfernen Sie danach den Serverwert (`Remove-DhcpServerv4OptionValue`) und bestätigen Sie, dass wieder der Scope-Wert `192.168.10.10` gilt.

#### Kontrollfragen

1. Welche beiden lokalen Sicherheitsgruppen entstehen durch den Befehl `netsh dhcp add securitygroups`, und wofür werden sie verwendet?
2. Was passiert, wenn ein Scope angelegt, aber nicht aktiviert wird?
3. Welcher Optionswert gilt, wenn Server- und Scope-Ebene dieselbe Option unterschiedlich setzen?
4. Welche Informationen enthält eine Lease-Tabelle, die ein Mitschnitt allein nicht liefert?

---

### Modul 3: Leases, Reservierungen und Ausschlüsse

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Lease-Dauer für unterschiedliche Einsatzfälle (Büro, Gäste, Server-nahe Geräte) begründet wählen und das Erneuerungsverhalten im Mitschnitt nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende Reservierungen und Ausschlussbereiche einrichten und von statischen Adressen abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Konflikterkennung des Servers aktivieren und einen Adresskonflikt im Labor auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende die Auslastung eines Scopes auslesen und berechnen.
* **Voraussetzungen:** Abschluss von Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **3.1** | Wahl der Lease-Dauer: Adressverbrauch, Last auf dem Server, Erreichbarkeit nach Ausfall; Zusammenhang mit T1 und T2. | 2 |
| **3.2** | Reservierungen: MAC-basiert (Client-Identifier), Vergleich mit statischer Adresse am Gerät, Reservierung innerhalb und außerhalb des Bereichs. | 2 |
| **3.3** | Ausschlüsse und Konflikterkennung: Ausschlussbereiche, Konflikterkennung des Servers (`ConflictDetectionAttempts`, Parametername nicht bestätigt), Erkennung durch den Client (RFC 5227). | 2 |
| **3.4** | Lease-Verwaltung und Statistik: Leases anzeigen und entfernen, Scope-Statistik (`Get-DhcpServerv4ScopeStatistics`), Berechnung der Auslastung. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Erneuerung im Mitschnitt:** Erstellen Sie `M3-Anfang` auf `SRV-WIN-DHCP1`. Setzen Sie die Lease-Dauer des Scopes `Netz-A` auf 30 Minuten (`Set-DhcpServerv4Scope`), erneuern Sie den Lease auf `CLI-WIN-A` und beobachten Sie mit dem Mitschnitt auf `RTR-LIN`, wann der Client erneuert (erwartet bei etwa 15 Minuten). **Rückbau:** Setzen Sie die Lease-Dauer wieder auf 8 Stunden.
2. **Reservierung:** Legen Sie für die MAC-Adresse von `CLI-WIN-A` eine Reservierung auf `192.168.10.150` an (`Add-DhcpServerv4Reservation`), erneuern Sie den Lease und prüfen Sie Adresse und Optionen. Lassen Sie die Reservierung für Modul 4 bestehen.
3. **Adresskonflikt:** Aktivieren Sie die Konflikterkennung des Servers mit einem Versuch. Entfernen Sie die Reservierung aus Aufgabe 2 vorübergehend und geben Sie den Lease auf `CLI-WIN-A` frei (`ipconfig /release`). Konfigurieren Sie temporär auf `RTR-LIN` die Adresse `192.168.10.100/24` zusätzlich auf der Netz-A-Schnittstelle (`ip addr add`; `.100` ist die erste Adresse des Pools), fordern Sie mit `ipconfig /renew` einen neuen Lease an und beobachten Sie, ob `.100` übersprungen wird. **Rückbau:** Entfernen Sie die Zusatzadresse von `RTR-LIN`, stellen Sie die Reservierung wieder her und setzen Sie die Konflikterkennung auf den Ausgangswert zurück.
4. **Ausschluss und Auslastung:** Legen Sie den Ausschlussbereich `192.168.10.190` bis `192.168.10.199` an (`Add-DhcpServerv4ExclusionRange`; der Bereich bleibt bestehen) und prüfen Sie, dass die Adressen nicht vergeben werden und die Zahl der verfügbaren Adressen sinkt. Lesen Sie die Statistik des Scopes `Netz-A` aus und berechnen Sie mit einem PowerShell-Einzeiler die Auslastung in Prozent; vergleichen Sie das Ergebnis mit der Anzeige in `dhcpmgmt.msc`.

#### Kontrollfragen

1. Warum sind sehr kurze Lease-Zeiten bei stabilen Büro-Clients unvorteilhaft, und wann sind sie sinnvoll?
2. Worin unterscheidet sich eine Reservierung von einer statischen Adresse am Gerät, und welche Vorteile bietet sie für die Dokumentation?
3. Wie erkennt ein Client nach RFC 5227, dass eine zugewiesene Adresse bereits belegt ist, und welche DHCP-Nachricht sendet er dann?
4. Wie berechnet sich die Auslastung eines Scopes?

---

### Modul 4: Optionen, Klassen, Policies und MAC-Filter

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Optionsebenen Server, Scope, Reservierung und Policy und deren Vorrang erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Vendor- und User-Classes erklären und eine User-Class auf einem Windows-Client setzen und serverseitig auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende eine Policy mit Bedingung und abweichenden Optionen oder Lease-Dauer konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende MAC-Filter (Allow- und Deny-Liste) konfigurieren und die Auswirkung testen.
* **Voraussetzungen:** Abschluss von Modul 2 und 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **4.1** | Optionsebenen und Vorrang (Server, Scope, Reservierung, Policy); weitere Optionen: Domänen-Suchliste (RFC 3397), klassenlose statische Routen (RFC 3442), Zeitserver, Optionen 66 und 67 (Boot-Informationen); Überblick, die Unterstützung je Server und Client ist nicht bestätigt. | 2 |
| **4.2** | Vendor-Classes und User-Classes: Zweck, Funktionsweise, Standard-Classes, benutzerdefinierte Classes (`Add-DhcpServerv4Class`). | 2 |
| **4.3** | Policy-basierte Zuweisung: Bedingungen (z. B. User-Class, MAC-Präfix), Bereiche und Optionen je Policy (`Add-DhcpServerv4Policy`), Verarbeitungsreihenfolge. | 2 |
| **4.4** | MAC-Filter: Allow- und Deny-Liste (`Add-DhcpServerv4Filter`), Zusammenspiel mit Reservierungen, Grenzen des MAC-Filters als Sicherheitsmaßnahme. | 2 |
| **4.5** | Verifikation von Optionen: Server-Sicht (`Get-DhcpServerv4OptionValue`), Client-Sicht (`ipconfig /all`, Mitschnitt). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zusätzliche Optionen:** Erstellen Sie `M4-Anfang`. Setzen Sie im Scope `Netz-A` die Option Zeitserver (Option 42) auf `192.168.10.1`. Prüfen Sie mit `Get-DhcpServerv4OptionValue -ScopeId 192.168.10.0`, welche Optionen gesetzt sind, und im Mitschnitt, ob der Server sie im ACK mitsendet. Ob ein Windows-Client Option 42 verwendet, ist nicht bestätigt; erwartet wird nur der Nachweis im Mitschnitt.
2. **User-Class und Policy:** Legen Sie auf dem Server die User-Class `Labor` an. Setzen Sie auf `CLI-WIN-A` die Class-ID mit `ipconfig /setclassid "<Adaptername>" Labor` und erneuern Sie den Lease. Erstellen Sie eine Policy `Labor-Clients` mit der Bedingung User-Class gleich `Labor`, die eine Lease-Dauer von 1 Stunde und einen abweichenden Wert für Option 15 vergibt. Weisen Sie nach, dass die Policy greift (Lease-Dauer und Option im Lease-Eintrag und Mitschnitt). **Rückbau:** Entfernen Sie am Ende der Aufgabe die Policy und leeren Sie die Class-ID auf dem Client (`ipconfig /setclassid "<Adaptername>"`).
3. **MAC-Filter:** Tragen Sie die MAC-Adresse von `CLI-WIN-A` in die Deny-Liste ein und aktivieren Sie die Deny-Liste (`Set-DhcpServerv4FilterList -Deny $true`). Erneuern Sie den Lease und werten Sie das Ergebnis im Mitschnitt aus. **Rückbau:** Entfernen Sie den Filter und deaktivieren Sie die Deny-Liste wieder, sonst scheitern alle folgenden Module.
4. **Dokumentation:** Erstellen Sie mit `Get-DhcpServerv4OptionValue -All` und `Get-DhcpServerv4Scope` eine Übersicht aller gesetzten Optionen und Scopes als Textdatei für die Betriebsdokumentation.

#### Kontrollfragen

1. In welcher Reihenfolge werden Optionen aus Server, Scope, Reservierung und Policy angewendet, und welcher Wert gewinnt?
2. Was unterscheidet eine Vendor-Class von einer User-Class?
3. Warum ist ein MAC-Filter kein wirksamer Schutz gegen einen böswilligen Teilnehmer im Netz?
4. Welche Bedingungen kann eine Policy auswerten, und was ist ein sinnvoller Einsatzfall?

---

### Modul 5: Mehrere Subnetze und DHCP-Relay

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum DHCP-Broadcasts Router nicht passieren, und die Arbeitsweise eines Relay-Agents (Feld `giaddr`, Option 82 nach RFC 3046) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Relay-Agent unter Linux konfigurieren und die Funktion im Mitschnitt auf beiden Seiten nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende für mehrere Subnetze Scopes planen, anlegen und einem Netz anhand der Relay-Adresse zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Superscopes und Multinetting erklären und vom Normalfall abgrenzen.
* **Voraussetzungen:** Abschluss von Modul 2 bis 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **5.1** | Broadcast-Domänen und Router: warum der Broadcast nicht weitergeleitet wird; Relay-Agent nach RFC 1542; Felder `giaddr` und Hop-Zähler; Unicast zwischen Relay und Server. | 2 |
| **5.2** | Relay Agent Information Option (Option 82, RFC 3046): Zweck und Einsatz in Switch-Umgebungen; Superscopes und mehrere logische Subnetze auf einem Segment (Überblick, `Add-DhcpServerv4Superscope`). | 2 |
| **5.3** | Relay unter Linux (`isc-dhcp-relay`, Konfigurationsdatei `/etc/default/isc-dhcp-relay`, Variablennamen nicht bestätigt) und Scope-Auswahl des Windows-Servers anhand von `giaddr`. | 2 |
| **5.4** | Adressplanung für mehrere Subnetze: Netze A, B, C; Bereiche, Gateways, Reservierungen, Dokumentation des Adressplans. | 2 |
| **5.5** | Fehlersuche am Relay: Mitschnitt an Client- und Serverseite, typische Fehler (falsche Schnittstellen, fehlende Routen, fehlender Scope). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ausgangslage ohne Relay:** Erstellen Sie `M5-Anfang` (`SRV-WIN-DHCP1`, `RTR-LIN`, `CLI-WIN-A`). Verbinden Sie `CLI-WIN-A` dauerhaft mit `vSwitch-ClientA`. Beobachten Sie mit `ipconfig /all` und einem Mitschnitt an der Netz-B-Schnittstelle von `RTR-LIN`, dass der Client keine Adresse erhält, und prüfen Sie, dass der Mitschnitt auf der Netz-A-Seite keine Pakete des Clients zeigt.
2. **Scope für Netz B:** Legen Sie auf `SRV-WIN-DHCP1` den Scope `Netz-B` an: `192.168.20.100` bis `192.168.20.199`, Maske `255.255.255.0`, Router `192.168.20.1`, DNS-Server `192.168.10.10`, Domänenname `corp.example.com`, Lease-Dauer 8 Stunden, aktiviert.
3. **Relay konfigurieren:** Konfigurieren Sie `isc-dhcp-relay` auf `RTR-LIN` mit dem Server `192.168.10.11` und allen drei Schnittstellen (Netz A, B und C), und starten Sie den Dienst neu. Weisen Sie nach, dass `CLI-WIN-A` eine Adresse aus `192.168.20.100–199` erhält, und lesen Sie im Mitschnitt auf beiden Seiten `giaddr` sowie die Unicast-Weiterleitung zwischen `192.168.20.1`/`192.168.10.1` und `192.168.10.11` ab. Die Reservierung aus Modul 3 gilt nur im Netz A und bleibt ohne Wirkung; notieren Sie dies.
4. **Superscope als Gedankenexperiment:** Erklären Sie schriftlich, in welchem Fall ein Superscope nötig wäre, und entwerfen Sie für ein Segment mit 300 Clients die Adressplanung mit zwei /24-Bereichen als Superscope. Es ist keine Umsetzung im Labor nötig.

#### Kontrollfragen

1. Welche Aufgabe hat das Feld `giaddr`, und wie wählt der Windows-Server anhand dessen den Scope?
2. Welche Schnittstellen muss ein Relay-Agent auf einem Router mit drei Netzen berücksichtigen, und warum auch die Serverseite?
3. Was geschieht, wenn der Server für ein Relay-Subnetz keinen passenden Scope hat?
4. Wozu dient Option 82, und wer fügt sie ein?
5. Wann ist ein Superscope sinnvoll, und warum ist der Fall heute selten?

---

### Modul 6: DHCP in Active Directory: Autorisierung und dynamische DNS-Updates

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Active-Directory-Testdomäne mit Domänencontroller und DNS aufbauen und DHCP-Server sowie Client in die Domäne aufnehmen.
  * Nach Abschluss dieses Moduls kann der Lernende einen DHCP-Server in Active Directory autorisieren und den Schutzgedanken gegen nicht autorisierte Server erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die dynamische DNS-Registrierung über den DHCP-Server konfigurieren (Zonen, Anmeldedaten, Client-FQDN-Option nach RFC 4702, Namenskonflikte nach RFC 4703) und im DNS nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle von Scavenging und der Löschung von DNS-Einträgen bei Lease-Ablauf erklären.
* **Voraussetzungen:** Abschluss von Modul 2 bis 5. Kenntnisse der Zonen im DNS aus dem Lehrplan DNS-Grundlagen sind hilfreich, aber nicht Bedingung.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **6.1** | Aufbau der Testdomäne `corp.example.com`: Rollen `AD-Domain-Services` und `DNS`, Gesamtstruktur anlegen, Domänenbeitritt von Server und Client. | 2 |
| **6.2** | Autorisierung von DHCP-Servern in Active Directory (`Add-DhcpServerInDC`, `Get-DhcpServerInDC`), Verhalten nicht autorisierter Server in der Domäne. | 2 |
| **6.3** | Zusammenspiel DHCP und DNS: wer registriert A- und PTR-Einträge (Client oder Server), Client-FQDN-Option (RFC 4702), Konfliktauflösung (RFC 4703), Name Protection, Reverse-Zonen. | 2 |
| **6.4** | Anmeldedaten für DNS-Updates (`Set-DhcpServerDnsCredential`), Einstellungen je Scope (`Set-DhcpServerv4DnsSetting`), Löschung von Einträgen bei Lease-Ablauf, Verhältnis zu Scavenging. | 2 |
| **6.5** | Abnahme: Test der Namensauflösung nach Lease-Vergabe, Prüfung der Einträge im DNS, Dokumentation. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Domäne aufbauen:** Erstellen Sie `M6-Anfang` auf `SRV-WIN-DHCP1` und `CLI-WIN-A`. Installieren Sie auf `SRV-WIN-DC1` (`192.168.10.10`) die Rollen `AD-Domain-Services` und `DNS` und legen Sie die Gesamtstruktur `corp.example.com` an (z. B. `Install-ADDSForest`; das Passwort für den Wiederherstellungsmodus wird interaktiv eingegeben). Legen Sie eine Reverse-Lookupzone für `192.168.20.0/24` mit sicheren dynamischen Updates an. Nehmen Sie `SRV-WIN-DHCP1` und `CLI-WIN-A` in die Domäne auf (`Add-Computer`); als DNS-Server verwenden beide `192.168.10.10`.
2. **Autorisierung:** Prüfen Sie, wie sich der DHCP-Server nach dem Domänenbeitritt in `dhcpmgmt.msc` darstellt, autorisieren Sie ihn mit `Add-DhcpServerInDC -DnsName SRV-WIN-DHCP1.corp.example.com -IPAddress 192.168.10.11` und bestätigen Sie den Eintrag mit `Get-DhcpServerInDC`.
3. **Dynamische DNS-Registrierung:** Legen Sie ein Dienstkonto `svc-dhcp-dns` in der Domäne an (Passwort interaktiv) und hinterlegen Sie es mit `Set-DhcpServerDnsCredential`. Aktivieren Sie für den Scope `Netz-B` die Registrierung durch den Server (immer, auch für ältere Clients, Löschung bei Lease-Ablauf, Name Protection). Parameternamen von `Set-DhcpServerv4DnsSetting`: nicht bestätigt, vorher mit `Get-Help` prüfen.
4. **Nachweis:** Erneuern Sie den Lease auf `CLI-WIN-A` und prüfen Sie mit `Resolve-DnsName cli-win-a.corp.example.com` die A-Registrierung sowie mit `Resolve-DnsName <Client-IP>` die PTR-Registrierung. Beobachten Sie im Mitschnitt, ob der Client die FQDN-Option mitsendet (Option 81, nicht bestätigt für die genutzte Windows-Version).

#### Kontrollfragen

1. Welchen Zweck hat die Autorisierung von DHCP-Servern in Active Directory, und wogegen schützt sie nicht?
2. Wer trägt den PTR-Eintrag ein, wenn der Client die A-Registrierung selbst übernimmt?
3. Wozu dient das Dienstkonto für DNS-Updates, und warum sollte es kein Domänen-Administrator sein?
4. Was bewirkt Name Protection, und welcher Konflikt wird dadurch verhindert?
5. Warum kann ein veralteter DNS-Eintrag trotz abgelaufener Lease weiter existieren?

---

### Modul 7: Hochverfügbarkeit: DHCP-Failover und Split-Scope

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Split-Scope, Cluster und DHCP-Failover vergleichen und die Grenzen von Failover (zwei Server, nur IPv4) benennen.
  * Nach Abschluss dieses Moduls kann der Lernende zwischen Load-Balance- und Hot-Standby-Modus unterscheiden und eine Failover-Beziehung für mehrere Scopes konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten bei Ausfall eines Partners im Labor nachweisen und Konfigurationsänderungen replizieren.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum der Relay-Agent beide Server erreichen muss.
* **Voraussetzungen:** Abschluss von Modul 2 bis 6 (Domäne, Autorisierung, Relay).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **7.1** | Hochverfügbarkeit bei DHCP: Split-Scope (z. B. 80/20), Clustering, Microsoft-DHCP-Failover; Begrenzungen laut Microsoft Learn (maximal zwei Server, nur DHCPv4). | 2 |
| **7.2** | Failover einrichten: Modi Load Balance (Standard 50/50) und Hot Standby, Shared Secret, Beziehung mit mehreren Scopes (`Add-DhcpServerv4Failover`). | 2 |
| **7.3** | Verhalten bei Ausfall: Kommunikationsunterbrechung, Partnerausfall, Maximum Client Lead Time (MCLT) und Zustandswechselintervall (Begriffe, Details nicht bestätigt); Rolle des Relay-Agents. | 2 |
| **7.4** | Betrieb: Replikation von Scope-Änderungen (`Invoke-DhcpServerv4FailoverReplication`), Status prüfen (`Get-DhcpServerv4Failover`), Hinweise zu gemischten Windows-Versionen. | 2 |
| **7.5** | Split-Scope als historische Alternative, Auswahlkriterien, Dokumentation der Entscheidung. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zweiten Server vorbereiten:** Erstellen Sie `M7-Anfang` auf `SRV-WIN-DHCP1`, `RTR-LIN` und `CLI-WIN-A`. Installieren Sie auf `SRV-WIN-DHCP2` (`192.168.10.12`, DNS `192.168.10.10`) die Rolle `DHCP`, nehmen Sie den Server in die Domäne auf und autorisieren Sie ihn in Active Directory. Ergänzen Sie auf `RTR-LIN` den Relay-Server `192.168.10.12` zu `192.168.10.11` und starten Sie den Dienst neu.
2. **Failover einrichten:** Legen Sie auf `SRV-WIN-DHCP1` eine Failover-Beziehung im Modus Load Balance für die Scopes `192.168.10.0` und `192.168.20.0` mit Partner `SRV-WIN-DHCP2` an (`Add-DhcpServerv4Failover`; das Shared Secret wird interaktiv gewählt und nicht dokumentiert). Prüfen Sie mit `Get-DhcpServerv4Scope -ComputerName SRV-WIN-DHCP2`, dass die Scopes repliziert wurden.
3. **Ausfalltest:** Beenden Sie die VM `SRV-WIN-DHCP1` (z. B. `Stop-VM`). Führen Sie auf `CLI-WIN-A` `ipconfig /release` und `ipconfig /renew` aus und weisen Sie nach, dass `SRV-WIN-DHCP2` einen Lease vergibt (Mitschnitt, `Get-DhcpServerv4Lease` auf dem Partner). Starten Sie `SRV-WIN-DHCP1` wieder und prüfen Sie den Zustand der Beziehung. Zustandsnamen in der Ausgabe: nicht bestätigt.
4. **Replikation:** Ändern Sie auf `SRV-WIN-DHCP1` die Lease-Dauer des Scopes `Netz-B` auf 4 Stunden, replizieren Sie mit `Invoke-DhcpServerv4FailoverReplication` und prüfen Sie den Wert auf dem Partner. **Rückbau:** Setzen Sie die Lease-Dauer wieder auf 8 Stunden und replizieren Sie erneut. Die Failover-Beziehung bleibt für die folgenden Module bestehen.

#### Kontrollfragen

1. Welche Einschränkungen von DHCP-Failover nennt Microsoft Learn, und welche Folgen hat das für IPv6?
2. Worin unterscheiden sich Load Balance und Hot Standby, und wann würden Sie welchen Modus wählen?
3. Warum muss ein Relay-Agent im Failover-Betrieb beide Server als Ziel kennen?
4. Was geschieht mit geänderten Scope-Einstellungen, wenn sie nicht repliziert werden?
5. Warum ist Split-Scope heute meist nur noch ein Sonderfall?

---

### Modul 8: DHCP unter Linux mit ISC Kea

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Komponenten von Kea (`kea-dhcp4`, `kea-dhcp6`, Control Agent, DDNS-Daemon) benennen und ihren Zweck erklären.
  * Nach Abschluss dieses Moduls kann der Lernende `kea-dhcp4` mit einem Subnetz, Pool, Optionen und einer Reservierung konfigurieren, die Konfiguration prüfen und den Dienst betreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Linux-Client über das Relay mit Kea versorgen und den Lease in der Lease-Datei nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende die Koexistenz von Windows-DHCP und Kea hinter demselben Relay erklären.
* **Voraussetzungen:** Abschluss von Modul 1, 2 und 5 sowie Grundkenntnisse in der Linux-Kommandozeile (Editor, `systemctl`, `journalctl`).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **8.1** | Kea im Überblick: Daemons (`kea-dhcp4`, `kea-dhcp6`, `kea-ctrl-agent`, `kea-dhcp-ddns`), JSON-Konfiguration, Lease-Speicher (Datei, MySQL, PostgreSQL, Überblick); Einordnung von ISC DHCP (Wartungsstatus: Quelle nicht geprüft). | 2 |
| **8.2** | Installation, Dienst und Konfigurationsprüfung: Paket `kea-dhcp4-server`, Konfigurationsdatei `/etc/kea/kea-dhcp4.conf` und Lease-Datei unter `/var/lib/kea/` (Pfade nicht bestätigt), Syntaxprüfung mit `kea-dhcp4 -t <Datei>`. | 2 |
| **8.3** | Konfiguration im Detail: `interfaces-config`, `lease-database`, `valid-lifetime` sowie `renew-timer` und `rebind-timer`, `subnet4` mit Pools, `option-data`, Reservierungen. | 2 |
| **8.4** | Betrieb: Dienststatus, Protokolle (`journalctl -u kea-dhcp4-server`), Lease-Datei im CSV-Format, Neuladen der Konfiguration. | 2 |
| **8.5** | Windows-DHCP und Kea im Vergleich, gemeinsames Relay für mehrere Server, Hooks (z. B. Hochverfügbarkeit, nur Überblick). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Installation prüfen:** Erstellen Sie `M8-Anfang` auf `SRV-LIN-KEA` und `RTR-LIN`. Prüfen Sie auf `SRV-LIN-KEA` (`192.168.10.21`) mit `dpkg -l | grep kea`, dass `kea-dhcp4-server` installiert ist, und notieren Sie Versionsstand und Pfade der Konfigurations- und Lease-Dateien.
2. **Konfiguration für Netz C:** Erstellen Sie eine Konfiguration für das Subnetz `192.168.30.0/24` mit Pool `192.168.30.100 - 192.168.30.199`, Router `192.168.30.1`, DNS-Server `192.168.10.10`, Domänenname `corp.example.com`, Lease-Dauer 8 Stunden und der Netz-A-Schnittstelle von `SRV-LIN-KEA` in `interfaces-config`. Prüfen Sie die Datei mit `kea-dhcp4 -t`, starten Sie den Dienst und kontrollieren Sie ihn mit `systemctl status`.
3. **Relay erweitern und Linux-Client:** Ergänzen Sie auf `RTR-LIN` den Relay-Server `192.168.10.21` zu den bestehenden Servern und starten Sie das Relay neu. Verbinden Sie `CLI-LIN-B` mit `vSwitch-ClientB`, aktivieren Sie `dhcp4: true` in der netplan-Konfiguration (`netplan apply`) und prüfen Sie mit `ip addr` sowie `networkctl status`, dass der Client eine Adresse aus `192.168.30.100–199` erhält. Weisen Sie die Lease in der CSV-Datei von Kea nach und bestätigen Sie im Mitschnitt auf `RTR-LIN`, dass der Windows-Server für Netz C nicht antwortet, weil dort kein Scope existiert (Verhalten nicht bestätigt, ggf. notieren).
4. **Reservierung:** Fügen Sie in der Kea-Konfiguration eine Reservierung für die MAC-Adresse von `CLI-LIN-B` mit `192.168.30.50` hinzu, prüfen Sie die Konfiguration, laden Sie sie neu (Neustart des Dienstes genügt) und weisen Sie die neue Adresse nach einer erneuten Anforderung nach (`networkctl renew <Schnittstelle>` bzw. Neustart der Schnittstelle).

#### Kontrollfragen

1. Welche Aufgaben haben `kea-dhcp4`, `kea-dhcp6`, `kea-ctrl-agent` und `kea-dhcp-ddns`?
2. Wie unterscheiden sich Windows-DHCP und Kea in Konfiguration (GUI und PowerShell gegen JSON-Datei) und Replikation?
3. Warum antwortet Kea nur für Netz C, obwohl das Relay Anfragen aus allen Netzen weiterleitet?
4. Welche Vorteile hat die Syntaxprüfung vor dem Neustart des Dienstes?
5. Welche Alternativen zur Lease-Datei bietet Kea, und wann sind sie sinnvoll?

---

### Modul 9: DHCPv6 und IPv6-Adressvergabe

* **Priorität:** 2 (Vertiefung / Optional)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SLAAC (RFC 4862), Router Advertisements mit den Flags M und O (RFC 4861) und DHCPv6 (RFC 8415) unterscheiden und den passenden Betriebsmodus (SLAAC, stateless DHCPv6, stateful DHCPv6) auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende die DHCPv6-Nachrichten, Ports (546, 547), die Multicast-Adresse `ff02::1:2`, DUID und IAID erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen DHCPv6-Scope unter Windows und ein Subnetz in `kea-dhcp6` konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Router Advertisements mit `radvd` und ein DHCPv6-Relay einrichten und die Funktion im Mitschnitt nachweisen.
* **Voraussetzungen:** Abschluss von Modul 5, 6 und 8 sowie Grundlagen der IPv6-Adressierung.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **9.1** | IPv6-Adressvergabe im Überblick: SLAAC, Router Advertisement mit Flags M und O, stateless und stateful DHCPv6, Präfixe nach RFC 4193. | 2 |
| **9.2** | DHCPv6-Protokoll (RFC 8415): Nachrichten Solicit, Advertise, Request, Reply, Renew, Rebind, Release, Information-Request; DUID, IAID, IA_NA; DNS-Option nach RFC 3646; Prefix Delegation (Überblick). | 2 |
| **9.3** | Windows-DHCPv6: IPv6-Scope anlegen (`Add-DhcpServerv6Scope`), Optionen, Unterschiede zu DHCPv4, keine Failover-Unterstützung für DHCPv6 laut Microsoft Learn. | 2 |
| **9.4** | Kea DHCPv6: Daemon `kea-dhcp6`, Konfiguration von Subnetz und Pool, Unterschiede zu DHCPv4. | 2 |
| **9.5** | Router Advertisements mit `radvd` (Paket und Konfigurationsdatei, Details nicht bestätigt) und DHCPv6-Relay (`dhcrelay -6`, Optionen nicht bestätigt). | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **IPv6-Grundlage:** Erstellen Sie `M9-Anfang` auf `RTR-LIN`, `SRV-WIN-DHCP1`, `SRV-WIN-DC1`, `SRV-LIN-KEA`, `CLI-WIN-A` und `CLI-LIN-B`. Vergeben Sie die statischen IPv6-Adressen aus dem Adressplan auf Router, Servern und Domänencontroller und aktivieren Sie die IPv6-Weiterleitung auf `RTR-LIN` (`net.ipv6.conf.all.forwarding=1`). Testen Sie die Erreichbarkeit mit `ping -6` bzw. `ping fd00:10::10`.
2. **Router Advertisements:** Konfigurieren Sie `radvd` auf `RTR-LIN` für Netz B und Netz C mit gesetztem M-Flag. Nutzen Sie `AdvAutonomous` so, dass keine SLAAC-Adresse entsteht, damit der Unterschied zwischen SLAAC und DHCPv6 sichtbar wird (Optionsnamen nicht bestätigt, vorher mit der Dokumentation des Pakets prüfen). Prüfen Sie am Client mit `ipconfig /all` bzw. `ip -6 addr`, welche Adressen entstehen.
3. **Windows-DHCPv6 für Netz B:** Legen Sie auf `SRV-WIN-DHCP1` einen IPv6-Scope für `fd00:20::/64` an (`Add-DhcpServerv6Scope`), setzen Sie die Option DNS-Server auf `fd00:10::10` und richten Sie auf `RTR-LIN` ein DHCPv6-Relay von der Netz-B-Schnittstelle zum Server `fd00:10::11` ein. Weisen Sie nach, dass `CLI-WIN-A` per DHCPv6 eine Adresse erhält, und lesen Sie die Nachrichten im Mitschnitt (`tcpdump -n -i <Schnittstelle> ip6 and udp port 547`).
4. **Kea DHCPv6 für Netz C und Rückbau:** Konfigurieren Sie auf `SRV-LIN-KEA` `kea-dhcp6` für `fd00:30::/64` mit einem Pool und der Option DNS-Server, richten Sie das Relay für Netz C ein und weisen Sie nach, dass `CLI-LIN-B` eine DHCPv6-Adresse erhält. **Rückbau:** Stoppen und deaktivieren Sie `radvd` und das IPv6-Relay auf `RTR-LIN`, stoppen Sie `kea-dhcp6` und deaktivieren Sie die IPv6-Scopes auf `SRV-WIN-DHCP1`, damit die Pflichtmodule ohne IPv6-Einfluss arbeiten.

#### Kontrollfragen

1. Welche Rolle spielen die Flags M und O im Router Advertisement?
2. Welche beiden Kennungen (DUID, IAID) identifizieren einen DHCPv6-Client, und warum genügt die MAC-Adresse nicht?
3. Warum steht Failover für DHCPv6 unter Windows laut Microsoft Learn nicht zur Verfügung, und welche Alternativen gibt es?
4. Wie unterscheiden sich stateless und stateful DHCPv6?
5. Welche Ports und welche Multicast-Adresse verwendet DHCPv6, und warum benötigt ein DHCPv6-Relay eine Zieladresse und eine Eingangsschnittstelle?

---

### Modul 10: Betrieb: Überwachung, Sicherung, Migration und Dokumentation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisprotokolle, Audit-Log und Statistiken eines DHCP-Servers auswerten und Auslastungsschwellen überwachen.
  * Nach Abschluss dieses Moduls kann der Lernende die DHCP-Konfiguration sichern, wiederherstellen und exportieren.
  * Nach Abschluss dieses Moduls kann der Lernende den Austausch eines DHCP-Servers über eine Failover-Beziehung (Microsoft-Verfahren) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Betriebsdokumentation für DHCP (Adressplan, Scopes, Optionen, Ansprechpartner) erstellen und Änderungen nachvollziehbar protokollieren.
* **Voraussetzungen:** Abschluss von Modul 2, 3 und 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **10.1** | Überwachung: Ereignisprotokolle des DHCP-Servers, Audit-Log (`Get-DhcpServerAuditLog`), Statistiken und Schwellenwerte für die Scope-Auslastung. | 2 |
| **10.2** | Sicherung und Wiederherstellung: `Backup-DhcpServer`, `Restore-DhcpServer`, `Export-DhcpServer` und `Import-DhcpServer`; Wirkung bei bestehender Failover-Beziehung. | 2 |
| **10.3** | Migration und Austausch eines Servers: Vorgehen nach dem Microsoft-Verfahren (Aufnahme des neuen Servers als Failover-Partner, Replikation, Entfernen des alten Servers). | 2 |
| **10.4** | Betriebsdokumentation und Änderungsverfahren: Adressplan, Scope-Liste, Optionsübersicht, Prüfliste für Änderungen. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Audit-Log auswerten:** Lesen Sie auf `SRV-WIN-DHCP1` das Audit-Log des laufenden Tages (`Get-DhcpServerAuditLog`; Dateiname und Pfad nicht bestätigt) und filtern Sie die Einträge zum Lease von `CLI-WIN-A`. Erklären Sie die Ereignisse und Codes anhand der Kopfzeile der Datei.
2. **Auslastungsbericht:** Schreiben Sie ein PowerShell-Skript, das alle Scopes mit `Get-DhcpServerv4ScopeStatistics` abfragt, die Auslastung berechnet und Scopes ab 80 % in eine CSV-Datei schreibt. Testen Sie es mit den Scopes der Failover-Beziehung und mit einem neuen Testscope.
3. **Sicherung und Wiederherstellung:** Erstellen Sie `M10-Anfang` auf `SRV-WIN-DHCP1` und `SRV-WIN-DHCP2`. Legen Sie auf `SRV-WIN-DHCP1` einen Testscope `Test` (`192.168.40.0/24`, inaktiv, nicht in der Failover-Beziehung) an, sichern Sie den Server mit `Backup-DhcpServer -Path C:\DhcpBackup`, löschen Sie den Testscope und stellen Sie die Konfiguration mit `Restore-DhcpServer -Path C:\DhcpBackup` wieder her. Weisen Sie die Wiederherstellung nach. **Rückbau:** Löschen Sie den Testscope endgültig und prüfen Sie, dass die Scopes `Netz-A` und `Netz-B` sowie die Failover-Beziehung unverändert sind.
4. **Export:** Exportieren Sie die Konfiguration mit `Export-DhcpServer -File C:\DhcpBackup\export.xml -Leases` und untersuchen Sie die Datei im Editor: Welche Informationen sind enthalten? Ob Leases über Failover-Grenzen hinweg sauber importiert werden, ist nicht bestätigt; ein Import wird im Labor nicht ausgeführt.
5. **Dokumentation und Migrationsplan:** Erstellen Sie die Betriebsdokumentation für DHCP (Adressplan der Netze A bis C, Scope-Liste mit Optionen, Failover-Beziehung, Sicherungsverfahren, Änderungsprotokoll mit einem ersten Eintrag). Entwerfen Sie zusätzlich auf Papier einen Migrationsplan für den Ersatz von `SRV-WIN-DHCP1` durch einen neuen Server nach dem Microsoft-Verfahren mit Schritten, Prüfpunkten und Rückfallpunkt; eine Umsetzung im Labor ist nicht vorgesehen.

#### Kontrollfragen

1. Welche Unterschiede bestehen zwischen `Backup-DhcpServer` und `Export-DhcpServer`?
2. Welche Schwellenwerte würden Sie für Scope-Auslastung warnen lassen, und wie begründen Sie sie?
3. Welche Schritte sind laut Microsoft-Verfahren nötig, um einen DHCP-Server in einer Failover-Beziehung durch einen neuen zu ersetzen?
4. Welche Inhalte gehören in eine DHCP-Betriebsdokumentation?

---

### Modul 11: Sicherheit: Rogue-DHCP, Zugriffsschutz und Härtung

* **Priorität:** 2 (Vertiefung / Optional)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Bedrohungen gegen DHCP (Rogue-Server, Adress-Erschöpfung, Spoofing) beschreiben und passende Gegenmaßnahmen auf Server- und Netzebene benennen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie DHCP Snooping, vertrauenswürdige Ports und Port Security auf Switches gegen Rogue-Server wirken.
  * Nach Abschluss dieses Moduls kann der Lernende einen Rogue-DHCP-Server im Labor erzeugen, im Mitschnitt erkennen und die Auswirkung auf den Client nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende die Berechtigungen eines Windows-DHCP-Servers über die lokalen Gruppen steuern und die Kea-Installation grundlegend härten.
* **Voraussetzungen:** Abschluss von Modul 4, 6 und 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **11.1** | Bedrohungsbild: Rogue-DHCP, Adress-Erschöpfung (Starvation), gefälschte Antworten; Wirkung auf Clients. | 2 |
| **11.2** | Schutz auf Netzebene (nur Konzept): DHCP Snooping, vertrauenswürdige Ports, Dynamic ARP Inspection, Port Security; Hinweis auf Modul 5 (Sicherheit) der Packet-Tracer-Reihe. | 2 |
| **11.3** | Schutz auf Serverebene (Windows): Autorisierung, Gruppen `DHCP Administrators` und `DHCP Users`, Audit-Log, Name Protection, MAC-Filter und ihre Grenzen. | 2 |
| **11.4** | Härtung von Kea: Dateirechte der Konfiguration und der Lease-Datei, nur benötigte Schnittstellen, Protokollierung, Absicherung des Control Agents (Konzept). | 2 |
| **11.5** | Maßnahmenkatalog und Prüfliste: Risiken, Gegenmaßnahmen, Nachweise. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rogue-Server im Labor:** Erstellen Sie `M11-Anfang` auf `SRV-LIN-KEA`, `RTR-LIN` und `CLI-WIN-A`. Verbinden Sie `SRV-LIN-KEA` temporär zusätzlich mit `vSwitch-ClientA` (Netz B, Adresse `192.168.20.50/24`) und konfigurieren Sie in Kea ein zweites Subnetz `192.168.20.0/24` mit Pool `192.168.20.200 - 192.168.20.220`, abweichendem Router `192.168.20.99` und der Schnittstelle des Netzes B. Fordern Sie auf `CLI-WIN-A` mehrfach einen Lease an und lesen Sie im Mitschnitt auf `RTR-LIN` die beiden OFFER-Nachrichten. **Rückbau:** Entfernen Sie das zweite Subnetz aus der Kea-Konfiguration, prüfen Sie die Datei, starten Sie den Dienst neu, trennen Sie den Zusatzadapter und bestätigen Sie mit `ip addr`, dass `SRV-LIN-KEA` nur noch an `vSwitch-Server` hängt, und mit einem erneuten Lease auf `CLI-WIN-A`, dass ausschließlich die Windows-Server antworten.
2. **Zugriffsrechte unter Windows:** Legen Sie in der Domäne ein Testkonto `lab.reader` an (Passwort interaktiv). Nehmen Sie es in die lokale Gruppe `DHCP Users` auf `SRV-WIN-DHCP1` auf und prüfen Sie, welche Aktionen im DHCP-Werkzeug erlaubt sind und welche abgelehnt werden. **Rückbau:** Entfernen Sie das Konto aus der Gruppe.
3. **Härtung von Kea:** Prüfen Sie mit `ls -l` die Rechte der Kea-Konfigurationsdatei und der Lease-Datei, mit `ss -lun` die gebundenen Ports und mit `systemctl status` den Dienstbenutzer. Dokumentieren Sie Abweichungen vom Prinzip der geringsten Rechte und passen Sie nur die Rechte an, die Sie begründen können.
4. **Maßnahmenkatalog:** Erstellen Sie eine Tabelle mit mindestens sechs Risiken (Rogue-Server, Starvation, falsche Optionen, offene Konfiguration, fehlende Protokolle, fehlende Sicherung), jeweils mit Gegenmaßnahme, Nachweis im Labor und Restrisiko.

#### Kontrollfragen

1. Warum schützt die Autorisierung in Active Directory nicht vor einem Rogue-Server, der kein Windows ist?
2. Wie unterscheidet DHCP Snooping vertrauenswürdige und nicht vertrauenswürdige Ports, und welchen Beitrag leistet Port Security?
3. Welche Wirkung hat ein erfolgreicher Starvation-Angriff, und welche Maßnahme begrenzt ihn?
4. Welche Rechte bietet die lokale Gruppe `DHCP Users` im Vergleich zu `DHCP Administrators`?

---

### Modul 12: Fehlersuche und integriertes Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende DHCP-Störungen systematisch über Client, Server und Netz eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Windows- und Linux-Clients sowie Windows- und Kea-Server mit den passenden Werkzeugen (`ipconfig`, `networkctl`, Ereignisprotokolle, `journalctl`, `tcpdump`) diagnostizieren.
  * Nach Abschluss dieses Moduls kann der Lernende drei vorgegebene Störungen (Relay, Kea-Schnittstelle, falsche Option) finden, beheben und in einem Fehlerprotokoll dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende die gesamte Laborumgebung gegen eine Anforderungsliste abnehmen und eine Betriebsdokumentation übergeben.
* **Voraussetzungen:** Abschluss von Modul 1 bis 8 und Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **12.1** | Methodik der Fehlersuche: Eingrenzung nach Schicht (Client, Netz, Server), Hypothese, Test, Dokumentation; Fehlerprotokoll. | 2 |
| **12.2** | Client-Diagnose: `ipconfig /all`, `/release`, `/renew`, Link-Local-Adresse, Linux `networkctl`, `journalctl -u systemd-networkd`. | 2 |
| **12.3** | Server-Diagnose: Dienst, Autorisierung, Bindungen, Scope-Status, Auslastung, Filter und Policies, Failover-Status, Kea-Protokolle. | 2 |
| **12.4** | Netz-Diagnose: Relay, Routing, Firewall (UDP 67/68), Mitschnitt mit `tcpdump`; Hinweise aus der Microsoft-Troubleshooting-Checkliste. | 2 |
| **12.5** | Störungsszenarien im Labor und Auswertung. | 2 |
| **12.6** | Abschlussprojekt: Abnahme gegen Anforderungsliste, Betriebsdokumentation, Übergabe. | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorbereitung:** Erstellen Sie Checkpoints `M12-Anfang` auf `SRV-WIN-DHCP1`, `SRV-WIN-DHCP2`, `SRV-LIN-KEA`, `RTR-LIN`, `CLI-WIN-A` und `CLI-LIN-B`. Legen Sie ein Fehlerprotokoll mit den Spalten Nr., Symptom, Hypothese, Test, Ergebnis und Maßnahme an. Die Störungen werden von einer zweiten Person erzeugt; im Selbststudium führen Sie die Änderung aus und beginnen die Fehlersuche erst nach einer Pause, ohne die Änderung nachzulesen.
2. **Störung A (Relay):** Beenden Sie auf `RTR-LIN` den Relay-Dienst. Erwartet wird: Clients in Netz B und Netz C erhalten keine neuen Adressen. Suchen Sie die Ursache nur mit Client-Sicht und Mitschnitt, beheben Sie sie und dokumentieren Sie den Fund.
3. **Störung B (Kea-Schnittstelle):** Tragen Sie in `interfaces-config` von Kea einen nicht existierenden Schnittstellennamen ein und starten Sie den Dienst neu. Erwartet wird: `CLI-LIN-B` erhält keinen Lease. Suchen Sie die Ursache mit den Protokollen, beheben Sie sie und dokumentieren Sie den Fund.
4. **Störung C (falsche Option):** Setzen Sie im Scope `Netz-B` die Router-Option auf `192.168.20.254`, replizieren Sie auf den Partner und erneuern Sie den Lease auf `CLI-WIN-A`. Erwartet wird: Lease vorhanden, aber keine Verbindung zu Netz A. Finden und beheben Sie die Ursache, replizieren Sie die Korrektur und dokumentieren Sie den Fund.
5. **Abnahme und Dokumentation:** Prüfen Sie die Umgebung gegen die Anforderungsliste: Netz A und B über Failover-Paar mit DDNS, Netz C über Kea, Relay mit allen drei Servern, Autorisierung, Backup aus Modul 10, vollständig dokumentierter Adressplan. Erstellen Sie ein Abnahmeprotokoll mit Soll, Ist und Nachweis (Befehlsausgabe oder Mitschnitt) und eine Betriebsdokumentation von maximal vier Seiten.

#### Kontrollfragen

1. In welcher Reihenfolge grenzen Sie eine Störung „Client erhält keine Adresse“ ein?
2. Woran erkennen Sie im Mitschnitt, ob ein DISCOVER den Server erreicht und ob eine Antwort zurückkommt?
3. Welche Ursachen kommen in Frage, wenn ein Client einen Lease hat, aber keine Verbindung zu anderen Netzen?
4. Wie weisen Sie nach, dass eine Korrektur auf beide Failover-Partner repliziert wurde?
5. Welche Punkte der Anforderungsliste würden Sie bei einer realen Übergabe zusätzlich nachweisen?
