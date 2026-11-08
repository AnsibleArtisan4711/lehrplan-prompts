# Lehrplan: Hyper-V Administration

| Kategorie | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Windows-Server-Grundlagen |
| **Gesamtumfang** | 12 Module, 110 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Hyper-V unter Windows Server (Desktop Experience und Server Core), PowerShell (Hyper-V-Modul), Windows Event Viewer, Performance Monitor |
| **Thematische Abgrenzung (Out of Scope)** | Hyper-V dient in anderen Übungen (Veeam, USV, Homelab) nur als Umgebung; hier ist es der Lerngegenstand. Keine Drittanbieter-Backup-Software (z. B. Veeam), keine Storage Area Networks (Fibre Channel/iSCSI-Hardware-Arrays), kein System Center Virtual Machine Manager (SCVMM), keine Azure-Hybrid-Dienste. |

---

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| **1** | Architektur, Voraussetzungen und Installation von Hyper-V | 1 | 8 |
| **2** | Virtuelle Maschinen: Generation 1 vs. Generation 2 und Basisverwaltung | 1 | 10 |
| **3** | Virtuelle Netzwerke und Hyper-V Virtual Switches | 1 | 10 |
| **4** | Speicherverwaltung: VHD/VHDX und Differenzdatenträger | 1 | 10 |
| **5** | Ressourcensteuerung: Virtuelle Prozessoren und Dynamischer Arbeitsspeicher | 1 | 8 |
| **6** | Zustandssicherung mit Checkpoints (Snapshots) | 1 | 8 |
| **7** | Automatisierung und Verwaltung per PowerShell | 1 | 12 |
| **8** | Verschachtelte Virtualisierung (Nested Virtualization) | 1 | 8 |
| **9** | Hochverfügbarkeit I: Live-Migration und Storage Migration | 2 | 10 |
| **10** | Disaster Recovery mit Hyper-V-Replica | 2 | 8 |
| **11** | Hochverfügbarkeit II: Failover-Cluster-Grundlagen für Hyper-V | 2 | 8 |
| **12** | Leistungsüberwachung, Diagnosewerkzeuge und Troubleshooting | 1 | 10 |
| **Gesamt** | **9 Module mit Priorität 1 / 3 Module mit Priorität 2** | **9x P1 / 3x P2** | **110** |

*Hinweis zur Priorisierung:* Module der **Priorität 1 (Pflicht / Kernkompetenz, 84 UE)** vermitteln die unverzichtbaren Grundlagen für den täglichen Betrieb eines einzelnen Hyper-V-Hosts sowie den Aufbau einer verschachtelten Laborumgebung. Module der **Priorität 2 (Vertiefung / Optional, 26 UE)** behandeln hostübergreifende Funktionen (Migration, Replikation, Clustering), die im Labor über die in Modul 8 aufgebaute Nested-Virtualization-Umgebung dargestellt werden.

---

### 2. Quellen

* **Hyper-V on Windows Server Documentation**, Herausgeber: Microsoft Corporation, Stand nicht geprüft, URL: `https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/` (nicht geprüft)
* **Hyper-V PowerShell Module Reference**, Herausgeber: Microsoft Corporation, Stand nicht geprüft, URL: `https://learn.microsoft.com/en-us/powershell/module/hyper-v/` (nicht geprüft)
* **Run Hyper-V in a Virtual Machine with Nested Virtualization**, Herausgeber: Microsoft Corporation, Stand nicht geprüft, URL: `https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/user-guide/nested-virtualization` (nicht geprüft)
* **Hyper-V nested virtualization (aktuelle Seite)**, Herausgeber: Microsoft Corporation, Stand: Inhalt am 08.11.2026 per Suche bestätigt (Seite nicht vollständig gelesen), URL: `https://learn.microsoft.com/windows-server/virtualization/hyper-v/nested-virtualization`
* **Set up hosts for live migration without Failover Clustering**, Herausgeber: Microsoft Corporation, Stand: Inhalt am 08.11.2026 per Suche bestätigt (Seite nicht vollständig gelesen), URL: `https://learn.microsoft.com/windows-server/virtualization/hyper-v/deploy/set-up-hosts-for-live-migration-without-failover-clustering`
* **Add-VMHardDiskDrive (Hyper-V-Modul)**, Herausgeber: Microsoft Corporation, Stand: Parameterliste am 08.11.2026 per Suche bestätigt, URL: `https://learn.microsoft.com/powershell/module/hyper-v/add-vmharddiskdrive`
* **Failover Clustering in Windows Server Documentation**, Herausgeber: Microsoft Corporation, Stand nicht geprüft, URL: `https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview` (nicht geprüft)
* **Study Guide for Exam AZ-800: Administering Windows Server Hybrid Core Infrastructure**, Herausgeber: Microsoft Corporation, Stand nicht geprüft, URL: `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800` (nicht geprüft)
* **Study Guide for Exam AZ-801: Configuring Windows Server Hybrid Advanced Services**, Herausgeber: Microsoft Corporation, Stand nicht geprüft, URL: `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-801` (nicht geprüft)
* **RFC 1918: Address Allocation for Private Internets**, Herausgeber: IETF (Y. Rekhter et al.), Februar 1996, URL: `https://www.rfc-editor.org/rfc/rfc1918` (nicht geprüft)
* **RFC 4193: Unique Local IPv6 Unicast Addresses**, Herausgeber: IETF (R. Hinden, B. Haberman), Oktober 2005, URL: `https://www.rfc-editor.org/rfc/rfc4193` (nicht geprüft)
* **IEEE 802.1Q: IEEE Standard for Local and Metropolitan Area Networks—Bridges and Bridged Networks (VLANs)**, Herausgeber: IEEE, Stand nicht geprüft, Keine geprüfte Quelle (URL)

---

### 3. Labor-Setup & Rahmenbedingungen

Alle praktischen Übungen finden in einer strikt vom Heim- und Produktivnetz getrennten Umgebung statt. Es wird ausschließlich mit privaten IPv4-Adressbereichen nach RFC 1918 (`192.168.100.0/24` und `10.10.20.0/24`), IPv6 Unique Local Addresses nach RFC 4193 (`fd00:10:10::/64`) sowie dem reservierten Namensraum `lab.internal` gearbeitet. **Im Labor wird keine Active-Directory-Domäne betrieben:** Alle Hosts und VMs sind Mitglieder einer Arbeitsgruppe (Workgroup); `lab.internal` dient nur als DNS-Suffix bzw. Namensraum.

#### Hardware- und Host-Anforderungen (Erforderlich ab Modul 1)
* **1x Hyper-V-Basishost (`HV-HOST01`):** Physischer Server/Workstation oder übergeordnete VM mit unterstützter Hardware-Virtualisierung (Intel VT-x / AMD-V mit EPT/RVI) und aktivierter Weitergabe der Virtualisierungserweiterungen für Nested Virtualization.
  * **CPU:** Mindestens 4 physische Kerne (8 logische Prozessoren empfohlen).
  * **RAM:** Mindestens 16 GB RAM (32 GB empfohlen, um in Modul 8 bis 11 verschachtelte Hyper-V-Hosts flüssig zu betreiben).
  * **Speicher:** Mindestens 150 GB freier SSD/NVMe-Speicherplatz für VHDX-Dateien, Differenzdatenträger und Checkpoints.

#### Software-Evaluationsversionen (Erforderlich ab Modul 1)
* **Windows Server 2022 oder Windows Server 2025 Evaluation ISO** (180 Tage kostenlose Evaluierungsversion von Microsoft, Editionen Standard und Datacenter enthalten) – **erforderlich ab Modul 1** für den Basishost und ab **Modul 2** als Installationsmedium für die Gast-VMs.

#### Virtuelle Maschinen (Aufbau im Kursverlauf)
* **`VM-SRV01` (Kleine Gast-VM 1):** Windows Server Evaluation (Server Core oder Desktop Experience, je nach Übung), 2 vCPUs, 2048 MB Start-RAM, 40 GB dynamisch wachsende VHDX. **Erforderlich ab Modul 2** (wird in Modul 8 bis 11 zeitweise mit 4096 MB RAM als verschachtelter Hyper-V-Host genutzt).
* **`VM-SRV02` (Kleine Gast-VM 2):** Windows Server Evaluation (Server Core oder Desktop Experience), 2 vCPUs, 2048 MB Start-RAM, 40 GB dynamisch wachsende VHDX. **Erforderlich ab Modul 2** (wird in Modul 8 bis 11 zeitweise mit 4096 MB RAM als zweiter verschachtelter Hyper-V-Host genutzt).
* **`VM-NESTED01` (Kleinst-VM innerhalb der verschachtelten Umgebung):** Kleine Test-VM ohne vollständiges Gastbetriebssystem oder mit minimalem Server-Core-Image (512 MB RAM, 5 GB VHDX) zur Demonstration von verschachtelten VMs, Live-Migration und Replikation zwischen `VM-SRV01` und `VM-SRV02`. **Erforderlich ab Modul 8**.

#### Virtuelle Switches auf `HV-HOST01`
* **`vSwitch-Privat-Lab` (Typ: Privat):** Isolierter Switch für die Kommunikation ausschließlich zwischen den Gast-VMs (`VM-SRV01` und `VM-SRV02`) ohne Verbindung zum Host oder zum physischen Netzwerk. **Erforderlich ab Modul 3**.
* **`vSwitch-Intern-Mgmt` (Typ: Intern):** Isolierter Switch für die Kommunikation zwischen dem Basishost `HV-HOST01` und den beiden Gast-VMs (Subnetz `192.168.100.0/24`), ohne Verbindung zum physischen Heim- oder Produktivnetz. **Erforderlich ab Modul 3**.
* *Hinweis zum externen Switch:* Die Funktionsweise eines externen Switches wird in Modul 3 ausführlich behandelt; um das Heimnetz nicht zu beeinflussen, wird im Labor jedoch dauerhaft mit dem privaten und internen Switch gearbeitet.

---

## B. Detaillierter Modulaufbau

### Modul 1: Architektur, Voraussetzungen und Installation von Hyper-V

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den architektonischen Unterschied zwischen Typ-1- (Bare-Metal) und Typ-2-Hypervisoren sowie die Rolle der Parent Partition und der Child Partitions in Hyper-V erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Hardware- und Firmware-Voraussetzungen (SLAT, VT-x/AMD-V, DEP/NX-Bit) mittels Diagnosewerkzeugen vor der Installation überprüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Hyper-V-Rolle samt Verwaltungswerkzeugen über den Server Manager und per PowerShell installieren sowie die Grundeinstellungen des Hosts konfigurieren.
* **Voraussetzungen:** Grundkenntnisse in Windows Server und PC-Hardwarearchitektur.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **1.1** | Virtualisierungsarchitektur: Typ-1- vs. Typ-2-Hypervisor, Hyper-V-Architektur (Hypervisor-Layer, Parent Partition, Child Partitions, VMBus, VSP/VSC) | 2 |
| **1.2** | Hardware- und BIOS/UEFI-Voraussetzungen: 64-Bit-Architektur, Hardware-assisted Virtualization (Intel VT-x, AMD-V), Second Level Address Translation (SLAT: EPT/RVI), Data Execution Prevention (DEP/XD/NX), Prüfung mit `systeminfo.exe` | 2 |
| **1.3** | Lizenzierungs- und Editionsunterschiede bei Windows Server (Standard vs. Datacenter bez. OSE-Rechten) sowie Installationsoptionen (Desktop Experience vs. Server Core) | 1 |
| **1.4** | Installation der Hyper-V-Rolle und der Management-Tools (GUI und PowerShell) inkl. Neustartverhalten und Überprüfung der Systemdienste (`vmms`, `vmcompute`) | 2 |
| **1.5** | Hyper-V-Host-Grundeinstellungen (Standardpfade für virtuelle Festplatten und Konfigurationsdateien, NUMA-Spanning, erweiterter Sitzungsmodus) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Überprüfung der Hardware-Voraussetzungen:** Öffnen Sie auf dem Basishost `HV-HOST01` eine administrative Eingabeaufforderung bzw. PowerShell. Prüfen Sie mithilfe von `systeminfo.exe` die Anforderungen unter den Hyper-V-Anforderungen (oder das Vorhandensein eines bereits laufenden Hypervisors). Dokumentieren Sie die Ausgabe.
2. **Installation der Hyper-V-Rolle per PowerShell:** Installieren Sie auf `HV-HOST01` (sofern noch nicht aktiv) die Rolle `Hyper-V` inklusive der Verwaltungswerkzeuge mit dem Cmdlet `Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart` bzw. überprüfen Sie bei vorinstalliertem Host den Status mit `Get-WindowsFeature -Name Hyper-V*`.
3. **Konfiguration der Standardpfade und Host-Optionen:** Legen Sie auf `HV-HOST01` die Ordnerstruktur `C:\HyperV\VMs` (für Konfigurationsdateien) und `C:\HyperV\VHDs` (für virtuelle Festplatten) an. Passen Sie in den Hyper-V-Einstellungen von `HV-HOST01` die Standardpfade auf diese beiden Verzeichnisse an und aktivieren Sie die Richtlinie für den Erweiterten Sitzungsmodus (Enhanced Session Mode). Prüfen Sie anschließend den Dienststatus von `vmms` (Hyper-V-Verwaltung für virtuelle Computer).

#### Kontrollfragen

1. Welche konkrete Aufgabe übernimmt die *Parent Partition* (Root Partition) in der Hyper-V-Architektur, und warum greifen *Child Partitions* nicht direkt auf die physische Hardware des Servers zu?
2. Welche vier Kriterien prüft `systeminfo.exe` auf einem physischen Server vor der Installation von Hyper-V, und welche Funktion erfüllt dabei SLAT (Second Level Address Translation)?
3. Welcher Systemdienst steuert die Verwaltung der virtuellen Maschinen auf einem Hyper-V-Host, und was passiert mit bereits laufenden VMs, wenn dieser Dienst neu gestartet wird?
4. Warum sollten die Standardpfade für virtuelle Festplatten und VM-Konfigurationsdateien vor dem Anlegen der ersten VM angepasst werden?

---

### Modul 2: Virtuelle Maschinen: Generation 1 vs. Generation 2 und Basisverwaltung

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die technischen Unterschiede zwischen virtuellen Maschinen der Generation 1 und Generation 2 gegenüberstellen und eine begründete Entscheidung für den jeweiligen Einsatzzweck treffen.
  * Nach Abschluss dieses Moduls kann der Lernende die Dateistruktur einer virtuellen Maschine auf dem Host-Dateisystem (`.vmcx`, `.vmrs`, `.vhdx`) identifizieren und deren Zweck erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende virtuelle Maschinen anlegen, Gastbetriebssysteme per ISO-Datei installieren, den Erweiterten Sitzungsmodus (Enhanced Session Mode) über VMBus nutzen sowie VMs exportieren und importieren.
* **Voraussetzungen:** Abschluss von Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **2.1** | Vergleich Generation 1 vs. Generation 2: BIOS vs. UEFI, Secure Boot, IDE vs. SCSI-Boot, Legacy-Netzwerkadapter vs. PXE über synthetische Adapter | 2 |
| **2.2** | Dateistruktur und Konfigurationsversionen: `.vmcx` (Binäre Konfiguration), `.vmrs` (Runtime State), GUID-Identifikation, VM-Konfigurationsversionen und deren Upgrade (`Update-VMVersion`) | 2 |
| **2.3** | Erstellen von VMs, Einbinden von ISO-Abbildern, Bootreihenfolge in UEFI (Generation 2) und Installation von Windows Server in den Gast-VMs | 3 |
| **2.4** | Integrationsdienste (Integration Services), VMBus-Treiber und Nutzung der Virtuellen Maschinenverbindung (`vmconnect.exe`) im Basis- und Erweiterten Sitzungsmodus (RDP over VMBus) | 1 |
| **2.5** | Exportieren und Importieren von virtuellen Maschinen (Importtypen: Direkt registrieren, Virtuellen Computer wiederherstellen, Virtuellen Computer kopieren mit neuer ID) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Erstellen und Installieren von `VM-SRV01` (Generation 2):** Erstellen Sie auf `HV-HOST01` die virtuelle Maschine `VM-SRV01` als Generation 2 mit 2048 MB Start-RAM (ohne dynamischen Arbeitsspeicher), zunächst ohne Netzwerkverbindung (`Nicht verbunden`), und einer neuen dynamisch wachsenden VHDX (`VM-SRV01_OS.vhdx`, 40 GB) im Standardpfad `C:\HyperV\VHDs`. Binden Sie die Windows Server Evaluation ISO ein und installieren Sie Windows Server (Desktop Experience).
2. **Erstellen und Installieren von `VM-SRV02` (Generation 2, Server Core):** Erstellen Sie analog die zweite Gast-VM `VM-SRV02` (Generation 2, 2048 MB Start-RAM, 40 GB VHDX `VM-SRV02_OS.vhdx`, `Nicht verbunden`) und installieren Sie darauf Windows Server in der Variante *Server Core*.
3. **Vergleichstest Generation 1 (Temporär):** Legen Sie zu Analysezwecken eine leere VM `VM-GEN1-TEST` der Generation 1 ohne Festplatte an. Vergleichen Sie in den Einstellungen von `VM-GEN1-TEST` und `VM-SRV01` die Abschnitte *Firmware/BIOS*, *Sicherheit* (Secure Boot) und die verfügbaren Controller für das DVD-Laufwerk (IDE vs. SCSI). **Aufräumschritt:** Löschen Sie die VM `VM-GEN1-TEST` nach der Dokumentation wieder vollständig von `HV-HOST01`.
4. **Inspektion der Dateistruktur und Export/Import-Test:** Prüfen Sie im Explorer unter `C:\HyperV\VMs` die erzeugten `.vmcx`- und `.vmrs`-Dateien von `VM-SRV01` und ordnen Sie deren Dateinamen den VM-GUIDs (abrufbar per `Get-VM | Select-Object Name, Id`) zu. Fahren Sie `VM-SRV02` herunter, exportieren Sie die VM nach `C:\HyperV\Export` (`Export-VM -Name VM-SRV02 -Path C:\HyperV\Export`) und prüfen Sie den Inhalt des Exportordners. **Import-Test:** Importieren Sie den Export als Kopie mit neuer ID (Assistent „Virtuellen Computer importieren“ → *Virtuellen Computer kopieren*, oder `Import-VM -Path <Pfad zur .vmcx> -Copy -GenerateNewId -VirtualMachinePath C:\HyperV\ImportTest -VhdDestinationPath C:\HyperV\ImportTest`). Benennen Sie die importierte VM in `VM-SRV02-IMPORT` um (`Rename-VM`), vergleichen Sie ihre ID mit der von `VM-SRV02` und starten Sie sie **nicht** (gleicher Computername und gleiche SID wie das Original). **Aufräumschritt:** Entfernen Sie `VM-SRV02-IMPORT` (`Remove-VM`) und löschen Sie die Ordner `C:\HyperV\ImportTest` und `C:\HyperV\Export`. Starten Sie `VM-SRV02` wieder.

#### Kontrollfragen

1. Warum kann eine virtuelle Maschine der Generation 1 nicht nachträglich in eine VM der Generation 2 umgewandelt werden, und welche Vorteile bietet Generation 2 beim Bootvorgang und der Sicherheit?
2. Worin unterscheiden sich die drei Import-Optionen („Direkt registrieren“, „Virtuellen Computer wiederherstellen“, „Virtuellen Computer kopieren“) im Hyper-V-Manager, und wann muss zwingend „Kopieren“ gewählt werden?
3. Wie funktioniert der *Erweiterte Sitzungsmodus* (Enhanced Session Mode) technisch im Hintergrund, und warum benötigt er keine IP-Netzwerkverbindung zwischen Host und Gast-VM?
4. Welchen Zweck erfüllen die Dateien mit den Endungen `.vmcx` und `.vmrs`, und warum dürfen diese nicht mit einem Texteditor bearbeitet werden?

---

### Modul 3: Virtuelle Netzwerke und Hyper-V Virtual Switches

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsweise und Sicherheitsauswirkungen der drei virtuellen Switch-Typen (Extern, Intern, Privat) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende isolierte virtuelle Switches (Privat und Intern) einrichten und die IP-Kommunikation zwischen Host und Gast-VMs bzw. zwischen den Gast-VMs konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende VLAN-Tagging sowie die erweiterten Sicherheitsfunktionen eines virtuellen Netzwerkadapters (MAC-Adressen-Spoofing, DHCP-Guard, Router-Guard, Portspiegelung) konfigurieren.
* **Voraussetzungen:** Abschluss von Modul 2; Grundkenntnisse in IPv4/IPv6-Subnetting.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **3.1** | Architektur des Hyper-V Virtual Switch: Extensible Switch, Bindung an physische Adapter vs. rein logische Switches | 2 |
| **3.2** | Die drei Switch-Typen im Detail: *Privat* (nur VM zu VM), *Intern* (VM zu VM plus virtueller Adapter in der Parent Partition), *Extern* (Bindung an physische NIC inkl. Option „Gemeinsames Verwenden dieses Netzwerkadapters für das Verwaltungsbetriebssystem zulassen“) | 3 |
| **3.3** | Virtuelle Netzwerkadapter in VMs: Synthetischer Netzwerkadapter vs. Älterer Netzwerkadapter (Legacy Network Adapter), Bandbreitenverwaltung (QoS) | 1 |
| **3.4** | VLAN-Identifikation nach IEEE 802.1Q auf Switch- und VM-Adapter-Ebene | 2 |
| **3.5** | Erweiterte Funktionen und Schutzmechanismen für virtuelle Netzwerkadapter: Dynamische vs. statische MAC-Adressen, MAC Address Spoofing, DHCP Guard, Router Guard, Geschütztes Netzwerk (Protected Network), Portspiegelung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Erstellen des privaten und internen Switches:** Öffnen Sie den Manager für virtuelle Switches auf `HV-HOST01`. Erstellen Sie zwei virtuelle Switches:
   * `vSwitch-Privat-Lab` vom Typ **Privat**
   * `vSwitch-Intern-Mgmt` vom Typ **Intern**
   Prüfen Sie anschließend auf `HV-HOST01` mit `Get-NetAdapter`, welcher der beiden Switches einen virtuellen Netzwerkadapter (`vEthernet (vSwitch-Intern-Mgmt)`) im Host-Betriebssystem erzeugt hat.
2. **IP-Konfiguration über den internen und privaten Switch:** Fügen Sie an `VM-SRV01` und `VM-SRV02` jeweils einen zweiten virtuellen Netzwerkadapter hinzu. Verbinden Sie auf beiden VMs Adapter 1 mit `vSwitch-Intern-Mgmt` und Adapter 2 mit `vSwitch-Privat-Lab`. Konfigurieren Sie folgende statische IPv4-Adressen (ohne Standardgateway, um das Routing auf dem Host nicht zu beeinflussen):
   * **Internes Netz (`vSwitch-Intern-Mgmt`, `192.168.100.0/24`):**
     * `HV-HOST01` (`vEthernet (vSwitch-Intern-Mgmt)`): `192.168.100.1/24`
     * `VM-SRV01` (Adapter 1): `192.168.100.11/24`
     * `VM-SRV02` (Adapter 1): `192.168.100.12/24`
   * **Privates Netz (`vSwitch-Privat-Lab`, `10.10.20.0/24`):**
     * `VM-SRV01` (Adapter 2): `10.10.20.11/24`
     * `VM-SRV02` (Adapter 2): `10.10.20.12/24`
   Aktivieren Sie in den Gast-VMs `VM-SRV01` und `VM-SRV02` die Windows-Firewall-Regel für eingehende ICMPv4-Echoanforderungen (`Enable-NetFirewallRule -Name FPS-ICMP4-ERQ-In`) und testen Sie per `ping` die Erreichbarkeit zwischen Host und VMs auf `192.168.100.x` sowie zwischen den beiden VMs auf `10.10.20.x`.
3. **Isolationstest mittels VLAN-Tagging (mit anschließendem Rückbau):** Aktivieren Sie in den Einstellungen von `VM-SRV01` auf dem mit `vSwitch-Privat-Lab` verbundenen Adapter (Adapter 2) die VLAN-Identifikation und setzen Sie die VLAN-ID auf `10`. Versuchen Sie von `VM-SRV01` aus einen Ping auf `10.10.20.12` (`VM-SRV02`) und beobachten Sie den Verbindungsabbruch. Aktivieren Sie nun auch auf `VM-SRV02` (Adapter 2) die VLAN-ID `10` und verifizieren Sie, dass die Kommunikation wieder funktioniert. **Wichtiger Rückbauschritt:** Deaktivieren Sie die VLAN-Identifikation auf den Adaptern von `VM-SRV01` und `VM-SRV02` wieder vollständig und testen Sie den Ping auf `10.10.20.12`, damit nachfolgende Module ohne VLAN-Filterung arbeiten können.
4. **Schutzfunktionen des virtuellen Netzwerkadapters (mit anschließendem Rückbau):** Aktivieren Sie auf `HV-HOST01` für den mit `vSwitch-Privat-Lab` verbundenen Adapter von `VM-SRV01` die Funktionen *DHCP-Guard*, *Router-Guard* und *MAC-Adressen-Spoofing* sowie die *Portspiegelung* (`VM-SRV01` als Quelle, `VM-SRV02` als Ziel):
   `Get-VMNetworkAdapter -VMName VM-SRV01 | Where-Object SwitchName -eq 'vSwitch-Privat-Lab' | Set-VMNetworkAdapter -DhcpGuard On -RouterGuard On -MacAddressSpoofing On -PortMirroring Source`
   `Get-VMNetworkAdapter -VMName VM-SRV02 | Where-Object SwitchName -eq 'vSwitch-Privat-Lab' | Set-VMNetworkAdapter -PortMirroring Destination`
   Prüfen Sie die Einstellungen mit `Get-VMNetworkAdapter -VMName VM-SRV01, VM-SRV02 | Format-List Name, SwitchName, DhcpGuard, RouterGuard, MacAddressSpoofing, PortMirroringMode` und dokumentieren Sie die Ausgabe. **Wichtiger Rückbauschritt:** Setzen Sie anschließend auf beiden Adaptern `-DhcpGuard Off -RouterGuard Off -MacAddressSpoofing Off -PortMirroring None` zurück und prüfen Sie dies erneut; Modul 8 aktiviert das MAC-Adressen-Spoofing gezielt selbst.

#### Kontrollfragen

1. Worin besteht der genaue Unterschied zwischen einem *Privaten* und einem *Internen* virtuellen Switch in Hyper-V, und warum kann der Host über einen privaten Switch keine Pakete an die Gast-VMs senden?
2. Welche Auswirkung hat das Deaktivieren des Kontrollkästchens „Gemeinsames Verwenden dieses Netzwerkadapters für das Verwaltungsbetriebssystem zulassen“ bei einem *Externen* Switch mit nur einer physischen Netzwerkkarte im Server?
3. Vor welchem konkreten Risiko im virtuellen Netzwerk schützt die Einstellung *DHCP-Guard* in den erweiterten Funktionen eines VM-Netzwerkadapters?
4. In welchem Szenario muss die Option *MAC-Adressen-Spoofing aktivieren* auf dem virtuellen Netzwerkadapter einer Gast-VM zwingend eingeschaltet werden?

---

### Modul 4: Speicherverwaltung: VHD/VHDX und Differenzdatenträger

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das VHD- und VHDX-Dateiformat vergleichen sowie die Vor- und Nachteile von dynamisch erweiterbaren, festen und Differenzdatenträgern beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende virtuelle Festplatten im laufenden Betrieb vergrößern, verkleinern, komprimieren (Compact) und konvertieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine Vorlagen-Festplatte (Parent Disk) mit Differenzdatenträgern (Child Disks) aufbauen und die Risiken für die Datenträgerkette erklären.
* **Voraussetzungen:** Abschluss von Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **4.1** | Vergleich VHD vs. VHDX: Maximale Kapazität (2 TB vs. 64 TB), Schutz vor Datenbeschädigung bei Stromausfall, 4K-Sektorgröße (Logical/Physical Sector Size), Online-Größenänderung | 2 |
| **4.2** | Datenträgertypen im Detail: Feste Größe (Fixed), Dynamisch erweiterbar (Dynamically Expanding), Differenzierung (Differencing) und Pass-Through-Datenträger (Nachteile und Ablösung) | 3 |
| **4.3** | Virtuelle Speichercontroller: IDE vs. Virtueller SCSI-Controller, Hot-Add/Hot-Remove von VHDX-Dateien an SCSI-Controllern, Storage Quality of Service (IOPS-Limits) | 2 |
| **4.4** | Wartungsoperationen an VHDX-Dateien: Erweitern (Expand), Verkleinern (Shrink), Komprimieren (Compact), Konvertieren (Fixed <-> Dynamic) und Zusammenführen (Merge) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Hot-Add und Online-Größenänderung einer Daten-VHDX:** Erstellen Sie auf `HV-HOST01` eine neue dynamisch wachsende VHDX-Datei `C:\HyperV\VHDs\VM-SRV01_Data.vhdx` mit einer Größe von 10 GB. Hängen Sie diese Datei im **laufenden Betrieb** an den SCSI-Controller von `VM-SRV01` an. Initialisieren Sie den Datenträger innerhalb von `VM-SRV01` als GPT, erstellen Sie ein Volume mit dem Laufwerksbuchstaben `D:` (NTFS) und erweitern Sie die VHDX anschließend über den Hyper-V-Manager im laufenden Betrieb von 10 GB auf 15 GB. Erweitern Sie danach das Volume `D:` in der Datenträgerverwaltung von `VM-SRV01` und verkleinern Sie sowohl das Volume als auch die VHDX-Datei testweise wieder auf 12 GB.
2. **Komprimieren (Compact) einer dynamisch wachsenden VHDX:** Erzeugen Sie auf dem Laufwerk `D:` in `VM-SRV01` eine 2 GB große Testdatei (z. B. mittels `fsutil file createnew D:\test.bin 2147483648`). Beobachten Sie auf `HV-HOST01` das Anwachsen der Datei `VM-SRV01_Data.vhdx`. Löschen Sie `D:\test.bin` in der Gast-VM (Papierkorb leeren). Fahren Sie `VM-SRV01` herunter (oder trennen Sie die Daten-VHDX kurzzeitig) und führen Sie auf `HV-HOST01` über den Assistenten zum Bearbeiten von Datenträgern (oder `Optimize-VHD`) die Aktion **Komprimieren** auf `VM-SRV01_Data.vhdx` aus. Dokumentieren Sie die Dateigröße vor und nach dem Vorgang.
3. **Einsatz von Differenzdatenträgern:** Erstellen Sie auf `HV-HOST01` eine dynamisch wachsende Basis-VHDX `C:\HyperV\VHDs\Parent_Data.vhdx` (5 GB), binden Sie diese kurz auf dem Host ein (`Mount-VHD`), formatieren Sie sie mit NTFS, legen Sie darauf eine Textdatei `Basis.txt` ab und trennen Sie sie wieder (`Dismount-VHD`). Setzen Sie auf `Parent_Data.vhdx` im Dateisystem das Attribut **Schreibgeschützt** (Read-Only). Erstellen Sie nun zwei Differenzdatenträger `Child_SRV01.vhdx` und `Child_SRV02.vhdx`, die beide `Parent_Data.vhdx` als übergeordneten Datenträger nutzen, und hängen Sie je einen an `VM-SRV01` und `VM-SRV02` an. Prüfen Sie, dass Änderungen in `VM-SRV01` nicht auf `VM-SRV02` sichtbar sind. **Aufräumschritt:** Trennen Sie `Child_SRV01.vhdx` und `Child_SRV02.vhdx` nach der Übung wieder von den SCSI-Controllern von `VM-SRV01` und `VM-SRV02` und löschen Sie die drei Test-VHDX-Dateien (`Child_SRV01.vhdx`, `Child_SRV02.vhdx`, `Parent_Data.vhdx`), während `VM-SRV01_Data.vhdx` für spätere Übungen an `VM-SRV01` verbleibt.

#### Kontrollfragen

1. Warum schrumpft eine dynamisch erweiterbare VHDX-Datei auf dem Host-Dateisystem nicht automatisch wieder, wenn innerhalb des Gastbetriebssystems große Dateien gelöscht werden?
2. Warum sollte die übergeordnete VHDX-Datei (Parent Disk) einer Differenzdatenträger-Hierarchie im NTFS-Dateisystem des Hosts immer mit dem Attribut „Schreibgeschützt“ versehen werden?
3. Was ist der Unterschied zwischen den Aktionen *Verkleinern (Shrink)* und *Komprimieren (Compact)* beim Bearbeiten einer virtuellen Festplatte?
4. Welche Voraussetzung muss erfüllt sein, damit eine virtuelle Festplatte im laufenden Betrieb der VM hinzugefügt, entfernt oder vergrößert werden kann?

---

### Modul 5: Ressourcensteuerung: Virtuelle Prozessoren und Dynamischer Arbeitsspeicher

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Zuteilung und Gewichtung virtueller Prozessoren (Reserve, Limit, Relative Gewichtung) sowie das Konzept von NUMA (Non-Uniform Memory Access) erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende Dynamischen Arbeitsspeicher (Dynamic Memory) mit Start-RAM, Minimalem/Maximalem RAM, Speicherpuffer und Gewichtung bedarfsgerecht konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsweise von Memory Ballooning und Smart Paging erklären und beurteilen, wann Smart Paging ausgelöst wird.
* **Voraussetzungen:** Abschluss von Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **5.1** | Virtuelle Prozessoren (vCPUs): Verhältnis von physischen Kernen/logischen Prozessoren zu vCPUs, CPU-Ressourcensteuerung (Reserve in %, Grenze/Limit in %, Relative Gewichtung) | 2 |
| **5.2** | NUMA-Architektur (Non-Uniform Memory Access): Physisches NUMA vs. Virtual NUMA, Auswirkungen von NUMA-Spanning auf die Leistung | 2 |
| **5.3** | Statischer vs. Dynamischer Arbeitsspeicher (Dynamic Memory): Arbeitsspeicher beim Start, Minimaler und Maximaler RAM, Arbeitsspeicherpuffer (in %), Arbeitsspeichergewichtung | 2 |
| **5.4** | Speicher-Rückgewinnung und Engpass-Mechanismen: Der Dynamic Memory VSC/Balloon-Treiber (`dmvsc`) und die Funktionsweise von *Smart Paging* beim Neustart von VMs | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration von Dynamischem Arbeitsspeicher:** Fahren Sie `VM-SRV01` und `VM-SRV02` herunter. Aktivieren Sie für beide VMs den **Dynamischen Arbeitsspeicher** mit folgenden Parametern:
   * **Arbeitsspeicher beim Start (Startup RAM):** 1024 MB
   * **Minimaler RAM:** 512 MB
   * **Maximaler RAM:** 2048 MB
   * **Arbeitsspeicherpuffer:** 20 %
   Starten Sie beide VMs und beobachten Sie im Hyper-V-Manager nach einigen Minuten Leerlauf die Spalten *Zugewiesener Arbeitsspeicher*, *Speicherbedarf* und *Arbeitsspeicherstatus*. Dokumentieren Sie, wie der zugewiesene Arbeitsspeicher von `VM-SRV02` (Server Core) im Leerlauf unter den Start-RAM-Wert von 1024 MB absinkt.
2. **CPU-Ressourcensteuerung und Gewichtung:** Konfigurieren Sie auf `VM-SRV01` für die virtuellen Prozessoren eine **Virtuelle Maschinenreserve** von `10 %`, ein **Limit** von `80 %` und eine **Relative Gewichtung** von `200` (Standard ist `100`). Prüfen Sie die Einstellungen per PowerShell mit `Get-VMProcessor -VMName VM-SRV01`. **Rückbauschritt:** Setzen Sie Reserve (`0 %`), Limit (`100 %`) und Relative Gewichtung (`100`) auf `VM-SRV01` sowie den Arbeitsspeicher beider VMs wieder auf **statisch 2048 MB** zurück, damit Modul 8 mit statischem Arbeitsspeicher beginnt (für Level-1-Hosts wird statischer RAM empfohlen, siehe Modul 8).

#### Kontrollfragen

1. Worin besteht der Unterschied zwischen dem *Arbeitsspeicher beim Start (Startup RAM)* und dem *Minimalen RAM* bei aktiviertem Dynamischen Arbeitsspeicher?
2. Warum tritt *Smart Paging* ausschließlich beim **Neustart** einer virtuellen Maschine auf und nicht während des regulären laufenden Betriebs?
3. Wie gewinnt der Hyper-V-Host über den Mechanismus *Memory Ballooning* Arbeitsspeicher von einer laufenden VM zurück, wenn auf dem Host Speicherknappheit herrscht?
4. Welche Bedeutung hat der Wert *Relative Gewichtung* (z. B. 200 vs. 100) bei der CPU- oder Arbeitsspeicherzuteilung, solange auf dem Hyper-V-Host genügend freie Ressourcen vorhanden sind?

---

### Modul 6: Zustandssicherung mit Checkpoints (Snapshots)

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den technischen Unterschied zwischen Produktions-Checkpoints (Production Checkpoints) und Standard-Checkpoints (Standard Checkpoints) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die beim Erstellen und Löschen eines Checkpoints ablaufenden Dateisystemprozesse (`.avhdx`, `.vmcx`, `.vmrs`) analysieren.
  * Nach Abschluss dieses Moduls kann der Lernende Checkpoints vor kritischen Konfigurationsänderungen erstellen, einen Rollback durchführen und Checkpoint-Bäume sauber zusammenführen (Merge).
* **Voraussetzungen:** Abschluss von Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **6.1** | Konzept und Einsatzzwecke von Checkpoints: Warum Checkpoints kein Backup ersetzen; Risiken langfristig bestehender Checkpoints | 2 |
| **6.2** | Produktions-Checkpoints vs. Standard-Checkpoints: Einsatz des Volume Shadow Copy Service (VSS) im Gastsystem vs. Speichern des flüchtigen RAM- und CPU-Status | 2 |
| **6.3** | Technische Funktionsweise im Dateisystem: Entstehung von `.avhdx`-Dateien (automatische Differenzdatenträger), Schreibumleitung und der Hintergrund-Merge-Prozess beim Löschen eines Checkpoints | 2 |
| **6.4** | Verwaltung von Checkpoint-Bäumen: Anwenden (Apply), Umbenennen, Löschen einzelner Checkpoints vs. Löschen von Checkpoint-Teilbäumen, Exportieren einer VM aus einem Checkpoint | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vergleich von Produktions- und Standard-Checkpoints:** Prüfen Sie in den Einstellungen von `VM-SRV01` unter *Checkpoints*, dass *Produktions-Checkpoints* aktiviert sind. Erstellen Sie im laufenden Betrieb von `VM-SRV01` einen Checkpoint und benennen Sie ihn in `CP1-Prod` um. Beobachten Sie im Ereignisprotokoll innerhalb von `VM-SRV01`, dass der Volume Shadow Copy Service (VSS) ausgelöst wurde. Stellen Sie die Einstellung für `VM-SRV01` anschließend testweise auf *Standard-Checkpoints* um, öffnen Sie in `VM-SRV01` ein Programmfenster (z. B. `notepad.exe`) und erstellen Sie einen zweiten Checkpoint `CP2-Standard`.
2. **Analyse der `.avhdx`-Dateien und Rollback-Test:** Prüfen Sie auf `HV-HOST01` im Verzeichnis `C:\HyperV\VHDs` die neu entstandenen `.avhdx`-Dateien für `VM-SRV01`. Legen Sie innerhalb von `VM-SRV01` auf dem Desktop eine Datei `Fehlerhafte_Aenderung.txt` an. Wenden Sie im Hyper-V-Manager zunächst den Checkpoint `CP2-Standard` an (*Anwenden*) und beobachten Sie, dass die VM sofort im laufenden Zustand mit geöffnetem Notepad-Fenster, aber ohne die Datei `Fehlerhafte_Aenderung.txt` wiederhergestellt wird. Wenden Sie anschließend `CP1-Prod` an und beobachten Sie, dass die VM hierbei wie nach einem Kaltstart neu bootet.
3. **Löschen von Checkpoints und Überwachung des Merge-Vorgangs (Rückbau):** Stellen Sie die Checkpoint-Konfiguration von `VM-SRV01` wieder auf *Produktions-Checkpoints* zurück. Löschen Sie im Hyper-V-Manager den gesamten Checkpoint-Teilbaum (`CP1-Prod` und `CP2-Standard`). Überprüfen Sie im Ordner `C:\HyperV\VHDs`, dass die `.avhdx`-Dateien im Hintergrund in die Basis-`.vhdx`-Dateien zusammengeführt (gemerged) wurden und anschließend verschwunden sind.

#### Kontrollfragen

1. Worin unterscheiden sich *Produktions-Checkpoints* und *Standard-Checkpoints* hinsichtlich der Datenkonsistenz von Applikationen (z. B. Datenbanken) und des Zustands der VM nach dem Anwenden des Checkpoints?
2. Was passiert auf dem Dateisystem des Hyper-V-Hosts technisch gesehen in dem Moment, in dem Sie einen Checkpoint erstellen, und was passiert, wenn Sie diesen Checkpoint später wieder löschen?
3. Warum dürfen `.avhdx`-Dateien niemals manuell im Windows Explorer gelöscht werden, um Speicherplatz auf dem Host freizugeben?
4. Aus welchen Gründen sind Checkpoints kein Ersatz für eine reguläre Datensicherung (Backup)?

---

### Modul 7: Automatisierung und Verwaltung per PowerShell

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den gesamten Lebenszyklus von virtuellen Maschinen, virtuellen Switches und VHDX-Dateien mithilfe des PowerShell-Moduls `Hyper-V` verwalten.
  * Nach Abschluss dieses Moduls kann der Lernende PowerShell Direct (`Invoke-Command -VMName`, `Enter-PSSession -VMName`) nutzen, um Gast-VMs über den VMBus ohne Netzwerkverbindung zu administrieren.
  * Nach Abschluss dieses Moduls kann der Lernende wiederverwendbare PowerShell-Skripte zur automatisierten Bereitstellung und Inventarisierung von Hyper-V-Umgebungen entwickeln.
* **Voraussetzungen:** Abschluss der Module 1 bis 6; Grundkenntnisse in Windows PowerShell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **7.1** | Überblick über das PowerShell-Modul `Hyper-V`: Cmdlet-Struktur (`Get-Command -Module Hyper-V`), Abfragen von Host- und VM-Eigenschaften (`Get-VMHost`, `Get-VM`) | 2 |
| **7.2** | Automatisierte Bereitstellung von VMs, Speichern und Netzwerken (`New-VM`, `Set-VM`, `New-VHD`, `Add-VMHardDiskDrive`, `New-VMSwitch`, `Connect-VMNetworkAdapter`) | 3 |
| **7.3** | Steuerung des Betriebszustands und der Checkpoints per PowerShell (`Start-VM`, `Stop-VM`, `Suspend-VM`, `Checkpoint-VM`, `Restore-VMCheckpoint`, `Remove-VMCheckpoint`) | 2 |
| **7.4** | Verwaltung von Gast-VMs über den VMBus mit *PowerShell Direct* (`Enter-PSSession -VMName`, `Invoke-Command -VMName`, `Copy-Item -ToSession`) | 2 |
| **7.5** | Entwicklung von Bereitstellungs- und Reporting-Skripten (Inventarisierung aller VMs, vCPUs, RAM-Zuweisungen, VHDX-Größen und Checkpoint-Alter als CSV/HTML-Report) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verwaltung über PowerShell Direct (ohne Netzwerk):** Stellen Sie über `HV-HOST01` eine interaktive Sitzung zu `VM-SRV02` mittels `Enter-PSSession -VMName VM-SRV02` her (Authentifizierung mit dem lokalen Administratorkonto von `VM-SRV02`). Fragen Sie innerhalb der Sitzung den Hostnamen, die IP-Konfiguration und die laufenden Dienste ab und verlassen Sie die Sitzung wieder (`Exit-PSSession`). Kopieren Sie anschließend mit `Copy-Item -ToSession` eine auf dem Host erstellte Textdatei direkt über den VMBus nach `C:\Temp` auf `VM-SRV02`.
2. **Skriptgesteuerte Bereitstellung einer VM (mit anschließendem Rückbau):** Schreiben Sie auf `HV-HOST01` ein PowerShell-Skript `Deploy-TestVM.ps1`, das vollautomatisch:
   * eine neue Generation-2-VM namens `VM-AUTO01` mit 1024 MB RAM erstellt,
   * eine 20 GB große dynamische VHDX anlegt und an den SCSI-Controller bindet,
   * die VM mit dem Switch `vSwitch-Privat-Lab` verbindet,
   * die automatische Startaktion auf `Nothing` und die Stoppaktion auf `ShutDown` setzt.
   Führen Sie das Skript aus, überprüfen Sie die Konfiguration mit `Get-VM -Name VM-AUTO01 | Format-List *` und bauen Sie die Test-VM samt ihrer VHDX-Datei anschließend per PowerShell (`Remove-VM -Name VM-AUTO01 -Force` und `Remove-Item`) wieder sauber zurück.
3. **Erstellen eines Hyper-V-Health- und Inventar-Reports:** Entwickeln Sie ein PowerShell-Skript `Get-HyperVReport.ps1`, das für alle VMs auf `HV-HOST01` den Namen, den Status (`State`), die Konfigurationsversion (`Version`), die Anzahl der vCPUs (`ProcessorCount`), den zugewiesenen RAM (`MemoryAssigned`) sowie die Anzahl vorhandener Checkpoints (`Get-VMCheckpoint`) ermittelt und als übersichtliche Tabelle sowie als CSV-Datei `C:\HyperV\VM_Inventory.csv` ausgibt.

#### Kontrollfragen

1. Welche Voraussetzungen müssen auf Host und Gast-VM erfüllt sein, damit *PowerShell Direct* (`-VMName`) funktioniert, und warum gelingt der Zugriff selbst dann, wenn die Gast-VM über keinerlei virtuelle Netzwerkkarte verfügt?
2. Mit welcher Cmdlet-Kombination finden Sie auf einem Hyper-V-Host alle virtuellen Maschinen, auf denen aktuell noch Checkpoints vorhanden sind, die älter als 7 Tage sind?
3. Worin besteht der Unterschied zwischen `Stop-VM -Name VM-SRV01` und `Stop-VM -Name VM-SRV01 -TurnOff`?
4. Warum legt das Cmdlet `New-VM` standardmäßig eine VM der Generation 1 an, wenn der Parameter `-Generation 2` nicht explizit angegeben wird?

---

### Modul 8: Verschachtelte Virtualisierung (Nested Virtualization)

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Konzept und die Einsatzszenarien der verschachtelten Virtualisierung (Nested Virtualization) in Trainings-, Test- und Container-Umgebungen erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende alle technischen Voraussetzungen für Nested Virtualization (Durchreichen der CPU-Virtualisierungserweiterungen, statische Arbeitsspeicherzuweisung, Netzwerkanforderungen) auf einer Gast-VM konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende innerhalb einer Gast-VM die Hyper-V-Rolle installieren und darin eine verschachtelte virtuelle Maschine der nächsten Ebene (Level 2) betreiben.
* **Voraussetzungen:** Abschluss der Module 1 bis 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **8.1** | Grundlagen der Nested Virtualization: Virtualisierungsebenen (Level 0 = Physischer Host, Level 1 = Gast-VM mit Hyper-V, Level 2 = Verschachtelte VM), Einsatzzwecke | 2 |
| **8.2** | Technische Voraussetzungen und Einschränkungen: CPU-Anforderungen; Arbeitsspeicher von Level-1-VMs (solange Hyper-V in der VM läuft, ist eine Änderung des Arbeitsspeichers nur bei ausgeschalteter VM möglich, Dynamic Memory schwankt dann nicht); weitere Einschränkungen laut aktueller Microsoft-Dokumentation der eingesetzten Windows-Server-Version | 2 |
| **8.3** | Aktivierung der Virtualisierungserweiterungen per PowerShell (`Set-VMProcessor -ExposeVirtualizationExtensions $true`) und Installation der Hyper-V-Rolle in den Gast-VMs | 2 |
| **8.4** | Netzwerkoptionen für verschachtelte VMs: MAC-Adressen-Spoofing vs. interner Switch mit NAT innerhalb des Level-1-Hosts | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorbereitung von `VM-SRV01` und `VM-SRV02` als verschachtelte Hyper-V-Hosts:** Fahren Sie `VM-SRV01` und `VM-SRV02` auf dem Basishost `HV-HOST01` herunter. Weisen Sie beiden VMs jeweils **4096 MB statischen Arbeitsspeicher** und **2 virtuelle Prozessoren** zu (`Set-VMMemory -VMName VM-SRV01, VM-SRV02 -DynamicMemoryEnabled $false -StartupBytes 4096MB` und `Set-VMProcessor -VMName VM-SRV01, VM-SRV02 -Count 2`). Statischer RAM wird empfohlen, weil sich der Arbeitsspeicher einer VM, in der Hyper-V läuft, nur bei ausgeschalteter VM ändern lässt. Aktivieren Sie auf `HV-HOST01` für beide VMs die Weitergabe der Hardware-Virtualisierungserweiterungen per PowerShell:
   `Set-VMProcessor -VMName VM-SRV01, VM-SRV02 -ExposeVirtualizationExtensions $true`
   Aktivieren Sie zudem auf den mit `vSwitch-Privat-Lab` verbundenen Netzwerkadaptern beider VMs das MAC-Adressen-Spoofing:
   `Get-VMNetworkAdapter -VMName VM-SRV01, VM-SRV02 | Where-Object SwitchName -eq 'vSwitch-Privat-Lab' | Set-VMNetworkAdapter -MacAddressSpoofing On`
2. **Installation der Hyper-V-Rolle in `VM-SRV01` und `VM-SRV02`:** Starten Sie `VM-SRV01` und `VM-SRV02`. Installieren Sie innerhalb beider Gast-VMs die Rolle `Hyper-V` inklusive der Verwaltungswerkzeuge per PowerShell (`Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart`). Richten Sie nach dem Neustart in beiden Gast-VMs jeweils einen privaten virtuellen Switch namens `Nested-Privat` ein.
3. **Erstellen der verschachtelten Test-VM `VM-NESTED01`:** Erstellen Sie innerhalb des verschachtelten Hyper-V-Hosts `VM-SRV01` eine kleine Generation-2-VM namens `VM-NESTED01` mit 512 MB statischem RAM, einer 5 GB großen dynamischen VHDX (`C:\NestedVMs\VM-NESTED01.vhdx`) und Verbindung zum Switch `Nested-Privat`. Starten Sie `VM-NESTED01` (ein vollständiges Gastbetriebssystem ist für den Nachweis des laufenden Hypervisors der Ebene 2 nicht zwingend erforderlich; die VM läuft bis zum UEFI/PXE-Screen bzw. kann mit einem minimalen Bootmedium gestartet werden) und überprüfen Sie den Status `Running` per `Get-VM` innerhalb von `VM-SRV01`. *(Hinweis: Die aufgebaute Nested-Umgebung auf `VM-SRV01` und `VM-SRV02` sowie `VM-NESTED01` bleiben für die Module 9, 10 und 11 bestehen. Der Rückbau erfolgt in Modul 12, Aufgabe 1, unabhängig davon, ob die Module 9 bis 11 bearbeitet wurden.)*

#### Kontrollfragen

1. Warum lässt sich der Arbeitsspeicher einer Gast-VM (Level 1), in der die Hyper-V-Rolle läuft, nur bei ausgeschalteter VM ändern, und weshalb wird für solche VMs statischer Arbeitsspeicher empfohlen?
2. Mit welchem PowerShell-Cmdlet und Parameter werden die Hardware-Virtualisierungsfunktionen der CPU (Intel VT-x / AMD-V) an eine Gast-VM durchgereicht, und in welchem Betriebszustand muss sich die VM dabei befinden?
3. Welche zwei Möglichkeiten gibt es, damit eine verschachtelte VM (Level 2) über das Netzwerk mit anderen Systemen außerhalb ihres direkten Level-1-Hosts kommunizieren kann?
4. Welche Auswirkung hat die Aktivierung der Nested Virtualization auf Dynamic Memory und auf die Änderung des Arbeitsspeichers im laufenden Betrieb, und wo finden Sie die aktuellen Einschränkungen für die eingesetzte Windows-Server-Version?

---

### Modul 9: Hochverfügbarkeit I: Live-Migration und Storage Migration

* **Priorität:** 2 (Vertiefung / Optional)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsweise und Voraussetzungen von Storage Migration, Shared-Nothing Live-Migration und klassischer Live-Migration erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den mehrstufigen Ablauf einer Live-Migration (Speicher-Pre-Copy, Delta-Übertragung, Blackout-Phase, ARP/RARP-Aktualisierung) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Verschiebe-Assistenten bzw. `Move-VMStorage` nutzen, um Festplatten einer laufenden VM zu verschieben, und die Konfiguration einer Live-Migration (`Enable-VMMigration`, Migrationsnetzwerk, Authentifizierung) beschreiben. *(Die Ausführung einer Live-Migration mit `Move-VM` ist im Labor ohne Active-Directory-Domäne nicht möglich und wird als Syntax behandelt.)*
* **Voraussetzungen:** Abschluss von Modul 8 (aktive Nested-Virtualization-Umgebung auf `VM-SRV01` und `VM-SRV02`).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **9.1** | Überblick über Migrationsarten in Hyper-V: Storage Migration (Verschieben des Speichers einer laufenden VM), Live-Migration (mit gemeinsamem Speicher) und Shared-Nothing Live-Migration | 2 |
| **9.2** | Interner Ablauf einer Live-Migration: TCP-Verbindungsaufbau, Pre-Copy der RAM-Seiten, Tracking geänderter Speicherseiten (Dirty Pages), kurze Pause- und Übergabephase | 2 |
| **9.3** | Voraussetzungen für Live-Migration zwischen zwei Hosts: Domänenmitgliedschaft vs. Workgroup-Einschränkungen, Authentifizierungsprotokolle (CredSSP vs. Kerberos mit Constrained Delegation; ab Windows Server 2025 ist CredSSP-basierte Live-Migration auf domänengebundenen Servern wegen standardmäßig aktivem Credential Guard nicht nutzbar), CPU-Kompatibilitätsmodus | 3 |
| **9.4** | Konfiguration der Live-Migration (`Enable-VMMigration`, Migrationsnetzwerk, Authentifizierung), Durchführung von Storage Migration per GUI und PowerShell (`Move-VMStorage`) sowie Syntax von `Move-VM` für die Shared-Nothing Live-Migration | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Durchführung einer Storage Migration im laufenden Betrieb:** Erstellen Sie auf `HV-HOST01` einen Zielordner `C:\HyperV\StorageMigration_Target`. Verschieben Sie im laufenden Betrieb von `VM-SRV01` ausschließlich die in Modul 4 erstellte Zusatzfestplatte `VM-SRV01_Data.vhdx` per `Move-VMStorage` (oder über den Assistenten „Verschieben“ im Hyper-V-Manager) in den neuen Ordner und anschließend wieder zurück nach `C:\HyperV\VHDs`. Löschen Sie den leeren Ordner `C:\HyperV\StorageMigration_Target` danach wieder. Lehnt Hyper-V die Verschiebung wegen der aktivierten Nested Virtualization ab, dokumentieren Sie die Meldung und führen Sie die Übung nach dem Rückbau (Modul 12, Aufgabe 1) aus.
2. **Live-Migration vorbereiten und Voraussetzungen bewerten (ohne Domäne):** Führen Sie in `VM-SRV01` und `VM-SRV02` jeweils aus: `Get-VMHost | Format-List VirtualMachineMigrationEnabled, VirtualMachineMigrationAuthenticationType, VirtualMachineMigrationPerformanceOption` und notieren Sie den Ausgangszustand. Aktivieren Sie danach `Enable-VMMigration`, legen Sie das Migrationsnetzwerk fest (`Add-VMMigrationNetwork 10.10.20.11` auf `VM-SRV01`, `Add-VMMigrationNetwork 10.10.20.12` auf `VM-SRV02`) und setzen Sie die Authentifizierung auf Kerberos (`Set-VMHost -VirtualMachineMigrationAuthenticationType Kerberos`). Erstellen Sie eine Tabelle *Voraussetzung / Ist-Zustand im Labor* (Domänenmitgliedschaft, Kerberos mit Constrained Delegation, gleiche virtuelle Switches auf beiden Hosts, Migrationsnetzwerk, CPU-Kompatibilität, Firewall) und begründen Sie, warum eine Live-Migration von `VM-NESTED01` zwischen `VM-SRV01` und `VM-SRV02` im Labor nicht ausführbar ist. **Rückbauschritt:** `Remove-VMMigrationNetwork` für die eingetragenen Adressen, `Disable-VMMigration` und `Set-VMHost -VirtualMachineMigrationAuthenticationType` auf den notierten Ausgangswert.
3. **Konfiguration des CPU-Kompatibilitätsmodus:** Fahren Sie `VM-NESTED01` innerhalb von `VM-SRV01` herunter, aktivieren Sie in den Prozessoreinstellungen die Option **Zu einem physischen Computer mit einer anderen Prozessorversion migrieren** (`Set-VMProcessor -VMName VM-NESTED01 -CompatibilityForMigrationEnabled $true`), überprüfen Sie die Einstellung per `Get-VMProcessor`, setzen Sie sie anschließend wieder auf `$false` zurück und starten Sie die VM.

#### Kontrollfragen

1. Welche einzelnen Phasen durchläuft eine *Shared-Nothing Live-Migration* vom Start des Verschiebevorgangs bis zu dem Moment, in dem die VM auf dem Zielhost weiterläuft?
2. Worin besteht der Unterschied zwischen den Authentifizierungsoptionen *CredSSP* und *Kerberos* bei der Live-Migration hinsichtlich der Notwendigkeit, direkt am Quellserver angemeldet zu sein?
3. Welchen Zweck erfüllt die Einstellung „Zu einem physischen Computer mit einer anderen Prozessorversion migrieren“ (CPU-Kompatibilitätsmodus), und welchen Nachteil bringt ihre Aktivierung mit sich?
4. Was passiert bei einer *Storage Migration* im Hintergrund, während die virtuelle Maschine während des Kopiervorgangs der VHDX-Datei weiterhin Schreibzugriffe auf ihre Festplatte ausführt?
5. Welche Voraussetzung fehlt im Labor, um `Move-VM` für `VM-NESTED01` zwischen `VM-SRV01` und `VM-SRV02` tatsächlich als Live-Migration auszuführen, und welche Authentifizierungsart würden Sie ab Windows Server 2025 konfigurieren?

---

### Modul 10: Disaster Recovery mit Hyper-V-Replica

* **Priorität:** 2 (Vertiefung / Optional)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Architektur und Einsatzszenarien von Hyper-V-Replica für die asynchrone Disaster-Recovery-Replikation erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Hyper-V-Replica zwischen zwei Hosts konfigurieren (Kerberos/HTTP in Domänenumgebungen erläutern, zertifikatsbasiertes HTTPS im Workgroup-Labor praktisch einrichten) und die Replikationsintervalle festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen Test-Failover, Geplantem Failover und Ungeplantem Failover erläutern und ein Test-Failover praktisch durchführen.
* **Voraussetzungen:** Abschluss von Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **10.1** | Funktionsweise von Hyper-V-Replica: Asynchrone Replikation auf VHDX-Ebene, Änderungsprotokollierung (`.hrl`-Dateien), Replikationsintervalle (30 Sekunden, 5 Minuten, 15 Minuten) | 2 |
| **10.2** | Authentifizierungs- und Sicherheitsoptionen: Kerberos über HTTP (Port 80, erfordert AD-Domäne) vs. Zertifikatsbasierte Authentifizierung über HTTPS (Port 443, auch für Workgroup-Hosts möglich) | 2 |
| **10.3** | Einrichtung eines Replikatservers, Firewallregeln (`Hyper-V-Replikat-HTTP-Listener` / `HTTPS-Listener`), Initialreplikation und Wiederherstellungspunkte | 2 |
| **10.4** | Failover-Arten im Vergleich: *Test-Failover* (isoliert ohne Unterbrechung), *Geplantes Failover* (ohne Datenverlust bei Wartung) und *Ungeplantes Failover* (im Katastrophenfall inkl. Replikationsumkehr) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration von `VM-SRV01` und `VM-SRV02` für zertifikatsbasierte Hyper-V-Replikation (Workgroup):** Tragen Sie in der `hosts`-Datei beider VMs `10.10.20.11 VM-SRV01` und `10.10.20.12 VM-SRV02` ein. Erzeugen Sie auf jeder VM ein selbstsigniertes Testzertifikat (`New-SelfSignedCertificate -DnsName <Hostname> -CertStoreLocation Cert:\LocalMachine\My`; der Antragstellername muss dem Hostnamen entsprechen, die Schlüsselverwendung muss Server- und Clientauthentifizierung umfassen – im Zertifikat prüfen). Exportieren Sie die öffentlichen Zertifikate (`Export-Certificate`), übertragen Sie die `.cer`-Dateien über die Administrationsfreigabe der Gegenstelle (`\\10.10.20.12\C$` bzw. `\\10.10.20.11\C$`, lokale Administrator-Anmeldung, Firewallregel `FPS-SMB-In-TCP` aktivieren) und importieren Sie das jeweilige Gegenstellen-Zertifikat in die vertrauenswürdigen Stammzertifizierungsstellen (`Import-Certificate -CertStoreLocation Cert:\LocalMachine\Root`). Aktivieren Sie auf beiden VMs die Rolle als Replikatserver über HTTPS (Port 443) mit dem Speicherpfad `C:\ReplicaStorage` (Hyper-V-Einstellungen oder `Set-VMReplicationServer -ReplicationEnabled $true -AllowedAuthenticationType Certificate -CertificateThumbprint <Fingerabdruck> -CertificateAuthenticationPort 443 -ReplicationAllowedFromAnyServer $true -DefaultStorageLocation C:\ReplicaStorage`) und schalten Sie die integrierte Windows-Firewall-Regel für den Hyper-V-Replikat-HTTPS-Listener (TCP-Port 443) frei (Regelname mit `Get-NetFirewallRule | Where-Object DisplayName -match 'Replica|Replikat'` ermitteln). Dieses Verfahren dient nur dem Test; produktiv werden Zertifikate einer internen Zertifizierungsstelle verwendet.
2. **Aktivieren der Replikation für `VM-NESTED01`:** Aktivieren Sie auf `VM-SRV01` die Replikation für die VM `VM-NESTED01` zum Zielserver `VM-SRV02` über Port 443 mit einem Replikationsintervall von 5 Minuten. Führen Sie die Initialreplikation über das Netzwerk (`10.10.20.0/24`) durch und überprüfen Sie den Replikationszustand (`Normal`) mit `Measure-VMReplication` bzw. im Hyper-V-Manager.
3. **Durchführen eines Test-Failovers und anschließender Rückbau:** Führen Sie auf dem Zielserver `VM-SRV02` ein **Test-Failover** für `VM-NESTED01` durch. Beobachten Sie, dass eine temporäre VM `VM-NESTED01 - Test` angelegt wird, ohne die laufende Replikation der Produktiv-VM auf `VM-SRV01` zu unterbrechen. Beenden Sie das Test-Failover wieder über die Aktion *Test-Failover beenden*. **Rückbauschritt:** Entfernen Sie die Replikation auf `VM-SRV01` und `VM-SRV02` (`Remove-VMReplication`), löschen Sie die Replikat-VM auf `VM-SRV02`, deaktivieren Sie die Replikatserver-Funktion (`Set-VMReplicationServer -ReplicationEnabled $false`) und die Firewallregeln für HTTPS-Listener und `FPS-SMB-In-TCP`, entfernen Sie die Testzertifikate aus `Cert:\LocalMachine\My` und `Cert:\LocalMachine\Root` beider VMs, löschen Sie die `.cer`-Dateien und den Ordner `C:\ReplicaStorage` und entfernen Sie die beiden Einträge aus der `hosts`-Datei.

#### Kontrollfragen

1. Worin unterscheiden sich *Test-Failover*, *Geplantes Failover* und *Ungeplantes Failover* bei Hyper-V-Replica hinsichtlich der Voraussetzungen am Quellhost und eines möglichen Datenverlusts (RPO)?
2. Welche Aufgabe übernehmen die `.hrl`-Dateien (Hyper-V Replica Log) auf dem Quellhost, und was passiert mit ihnen, wenn die Netzwerkverbindung zum Zielserver vorübergehend unterbrochen ist?
3. Warum ist Hyper-V-Replica auch in Umgebungen ohne Active-Directory-Domäne (Workgroup) einsetzbar, und welche Authentifizierungsmethode muss dafür zwingend konfiguriert werden?
4. Warum ersetzt auch Hyper-V-Replica kein vollwertiges Backup (z. B. bei logischer Datenbeschädigung, versehentlichem Löschen oder einem Ransomware-Befall in der Quell-VM)?

---

### Modul 11: Hochverfügbarkeit II: Failover-Cluster-Grundlagen für Hyper-V

* **Priorität:** 2 (Vertiefung / Optional)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen asynchroner Replikation (Hyper-V-Replica) und echter Hochverfügbarkeit in einem Windows Server Failover Cluster erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Kernkomponenten eines Hyper-V-Failover-Clusters (Clusterknoten, Cluster-Netzwerke, Quorum und Zeugen/Witness, Cluster Shared Volumes / CSV) erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende das Feature `Failover-Clustering` installieren, einen Cluster-Validierungstest (`Test-Cluster`) durchführen und die Ergebnisse auswerten.
* **Voraussetzungen:** Abschluss von Modul 8 (Modul 9 und 10 werden empfohlen, sind aber nicht zwingend).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **11.1** | Grundlagen der Hochverfügbarkeit: Geplante vs. ungeplante Ausfallzeiten, Abgrenzung Live-Migration (geplant) vs. Failover-Clustering (automatischer Neustart bei Host-Ausfall) | 2 |
| **11.2** | Architektur eines Hyper-V-Failover-Clusters: Knoten (Nodes), Anforderungen an gemeinsamen Speicher (iSCSI, Fibre Channel, Storage Spaces Direct) und Funktionsweise von Cluster Shared Volumes (CSV) unter `C:\ClusterStorage\` | 2 |
| **11.3** | Quorum-Modelle und Split-Brain-Vermeidung: Node Majority, Disk Witness, File Share Witness und Cloud Witness | 2 |
| **11.4** | Installation des Features `Failover-Clustering`, Durchführung und Interpretation der Cluster-Validierung (`Test-Cluster`) sowie hochverfügbare VM-Rollen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Installation des Features Failover-Clustering auf den verschachtelten Hosts:** Installieren Sie innerhalb der beiden Gast-VMs `VM-SRV01` und `VM-SRV02` das Windows-Feature `Failover-Clustering` inklusive der Verwaltungswerkzeuge per PowerShell:
   `Install-WindowsFeature -Name Failover-Clustering -IncludeManagementTools`
2. **Konfiguration einer gemeinsamen VHDX-Set-Datei (`.vhds`) als simulierter Shared Storage:** Erstellen Sie auf dem Basishost `HV-HOST01` eine gemeinsame virtuelle Festplatte im VHD-Set-Format (`New-VHD -Path C:\HyperV\VHDs\ClusterSharedDisk.vhds -SizeBytes 10GB -Dynamic`). Hängen Sie diese `.vhds`-Datei an die SCSI-Controller von **beiden** Gast-VMs (`VM-SRV01` und `VM-SRV02`) mit aktivierter Option für gemeinsame Datenträgernutzung (`Add-VMHardDiskDrive -ShareVirtualDisk`) an.
3. **Cluster-Validierung eines Einzelknotens:** Führen Sie auf `VM-SRV01` `Test-Cluster -Node VM-SRV01` aus und öffnen Sie den HTML-Bericht unter `C:\Windows\Cluster\Reports`. Erwartung: Im Workgroup-Labor mit nur einem Knoten enthält der Bericht Warnungen oder Fehler (z. B. nur ein Knoten, keine Domänenmitgliedschaft, kein bestätigter gemeinsamer Speicher). Ordnen Sie jede Meldung einer Anforderung aus 11.2 bis 11.4 zu und notieren Sie, welche Anforderung das Labor nicht erfüllt. Eine Clusterbildung (`New-Cluster`) ist nicht Ziel der Übung. Bricht `Test-Cluster` schon vor der Berichtserstellung mit einer Fehlermeldung ab, dokumentieren Sie die Meldung und ihre Ursache.
4. **Rückbau der Änderungen aus Modul 11:** Fahren Sie `VM-SRV01` und `VM-SRV02` herunter, trennen Sie `ClusterSharedDisk.vhds` von beiden VMs (`Remove-VMHardDiskDrive`) und löschen Sie die `.vhds`-Datei samt Begleitdateien im selben Ordner auf `HV-HOST01`. Starten Sie beide VMs und deinstallieren Sie darin das Feature (`Uninstall-WindowsFeature -Name Failover-Clustering -IncludeManagementTools -Restart`). Der übrige Rückbau der Nested-Umgebung erfolgt in Modul 12, Aufgabe 1.

#### Kontrollfragen

1. Welches Problem löst ein *Cluster Shared Volume (CSV)* in einem Hyper-V-Cluster im Vergleich zu einer klassischen NTFS-formatierten LUN, auf die immer nur ein Server gleichzeitig zugreifen darf?
2. Was versteht man in einem Cluster unter einem *Split-Brain-Szenario*, und wie verhindert das Quorum (z. B. mithilfe eines File Share Witness oder Disk Witness) diesen Zustand?
3. Was geschieht mit einer hochverfügbaren virtuellen Maschine in einem Hyper-V-Failover-Cluster, wenn der physische Host, auf dem sie gerade läuft, durch einen plötzlichen Stromausfall hart ausfällt?
4. Warum sollte vor der produktiven Inbetriebnahme eines Hyper-V-Clusters immer der Cluster-Validierungsassistent (`Test-Cluster`) vollständig und ohne Fehler durchlaufen werden?

---

### Modul 12: Leistungsüberwachung, Diagnosewerkzeuge und Troubleshooting

* **Priorität:** 1 (Pflicht / Kernkompetenz)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die spezifischen Leistungsindikatoren (Performance Counters) für Hyper-V im Windows Performance Monitor (`perfmon.exe`) auswerten, um CPU-, RAM-, Speicher- und Netzwerkengpässe zu identifizieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Hyper-V-spezifischen Ereignisprotokolle im Windows Event Viewer (`Hyper-V-VMMS`, `Hyper-V-Worker`, `Hyper-V-Hypervisor`, `Hyper-V-VmSwitch`) zur strukturierten Fehlersuche nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende das integrierte Ressourcenmessungssystem (`Enable-VMResourceMetering`, `Measure-VM`) anwenden und typische Störungsszenarien im Hyper-V-Betrieb selbstständig diagnostizieren und beheben.
* **Voraussetzungen:** Abschluss der Module 1 bis 8. Die Module 9 bis 11 sind nicht erforderlich; Aufgabe 1 stellt die Ausgangslage in jedem Fall her.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| **12.1** | Leistungsüberwachung von Hyper-V: Warum der Task-Manager in der Parent Partition nicht die gesamte CPU-Last aller VMs anzeigt; Einsatz von `perfmon.exe` | 2 |
| **12.2** | Zentrale Hyper-V-Performance-Counter: `Hyper-V Hypervisor Logical Processor(% Total Run Time)`, `Hyper-V Hypervisor Virtual Processor`, `Hyper-V Dynamic Memory VM`, `Hyper-V Virtual Storage Device` und `Hyper-V Virtual Network Adapter` | 3 |
| **12.3** | Ressourcenmessung (Resource Metering) per PowerShell (`Enable-VMResourceMetering`, `Measure-VM`, `Reset-VMResourceMetering`) | 1 |
| **12.4** | Analyse der Hyper-V-Ereignisprotokolle unter `Anwendungs- und Dienstprotokolle -> Microsoft -> Windows -> Hyper-V-*` sowie Umgang mit verwaisten VMs, defekten VHDX-Pfaden und Switch-Bindungsfehlern | 2 |
| **12.5** | Praxis-Troubleshooting: Systematische Diagnose und Behebung von Konfigurations-, Speicher-, Netzwerk- und Startproblemen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Herstellen der Ausgangslage (unabhängig vom Bearbeitungsstand der Module 9 bis 11):** Führen Sie die folgenden Schritte aus; bereits hergestellte Zustände werden übersprungen:
   * Löschen Sie `VM-NESTED01` innerhalb von `VM-SRV01` samt `C:\NestedVMs\VM-NESTED01.vhdx`, falls vorhanden, und entfernen Sie auf beiden VMs den privaten Switch `Nested-Privat` (`Remove-VMSwitch`).
   * Deinstallieren Sie in `VM-SRV01` und `VM-SRV02` die Hyper-V-Rolle (`Uninstall-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart`) und fahren Sie beide VMs danach herunter.
   * Setzen Sie auf `HV-HOST01` zurück: `Set-VMProcessor -VMName VM-SRV01, VM-SRV02 -ExposeVirtualizationExtensions $false`, `Get-VMNetworkAdapter -VMName VM-SRV01, VM-SRV02 | Set-VMNetworkAdapter -MacAddressSpoofing Off` und `Set-VMMemory -VMName VM-SRV01, VM-SRV02 -StartupBytes 2048MB`.
   * Starten Sie beide VMs und prüfen Sie Arbeitsspeicher (`Get-VM`), Prozessoreinstellung (`Get-VMProcessor`) und die gegenseitige Erreichbarkeit per Ping auf `192.168.100.x` und `10.10.20.x`.
2. **Einrichten von Performance-Countern und Ressourcenmessung:** Öffnen Sie auf `HV-HOST01` den Leistungsüberwachungs-Monitor (`perfmon.exe`). Fügen Sie folgende Leistungsindikatoren hinzu und beobachten Sie diese beim gleichzeitigen Betrieb von `VM-SRV01` und `VM-SRV02`:
   * `Hyper-V Hypervisor Logical Processor -> % Total Run Time` (_Total)
   * `Hyper-V Hypervisor Virtual Processor -> % Guest Run Time` (für `VM-SRV01` und `VM-SRV02`)
   * `Hyper-V Virtual Storage Device -> Write Bytes/sec` und `Read Bytes/sec`
   Aktivieren Sie parallel per PowerShell die Ressourcenmessung für beide VMs (`Get-VM | Enable-VMResourceMetering`), erzeugen Sie in `VM-SRV01` kurzzeitig Festplatten- und Netzwerklast (z. B. `fsutil file createnew C:\lasttest.bin 2147483648`, Datei danach löschen, und `ping -n 200 -l 65500 10.10.20.12`) und werten Sie die Messdaten anschließend mit `Measure-VM -VMName VM-SRV01, VM-SRV02` aus. Deaktivieren Sie die Ressourcenmessung nach der Auswertung wieder (`Get-VM | Disable-VMResourceMetering`).
3. **Troubleshooting-Labor mit drei praxisnahen Störungsszenarien:** Simulieren, diagnostizieren (mithilfe der Ereignisanzeige und PowerShell) und beheben Sie auf `HV-HOST01` nacheinander die folgenden **drei Störungen**:
   * **Störung 1 (Fehlende/verschobene VHDX-Datei beim VM-Start):** Fahren Sie `VM-SRV02` herunter. Benennen Sie im Windows Explorer die Datei `C:\HyperV\VHDs\VM-SRV02_OS.vhdx` in `VM-SRV02_OS_verschoben.vhdx` um. Versuchen Sie `VM-SRV02` zu starten, lokalisieren Sie die genaue Fehlermeldung samt Ereignis-ID im Protokoll `Microsoft-Windows-Hyper-V-Worker/Admin` (bzw. `Hyper-V-VMMS/Admin`) und beheben Sie das Problem durch Zurückbenennen der Datei und Prüfung mit `Test-VHD`.
   * **Störung 2 (Überbuchter Arbeitsspeicher verhindert VM-Start):** Konfigurieren Sie auf der ausgeschalteten VM `VM-SRV02` testweise einen statischen Start-Arbeitsspeicher von `65536 MB` (64 GB – bzw. einen Wert, der den physisch auf `HV-HOST01` verfügbaren freien RAM deutlich übersteigt). Versuchen Sie die VM zu starten, analysieren Sie den Startfehler im Ereignisprotokoll `Hyper-V-VMMS/Admin` und setzen Sie den Arbeitsspeicher per `Set-VMMemory` wieder auf `2048 MB` zurück.
   * **Störung 3 (Unterbrochene Netzwerkkommunikation durch falsche Switch-Zuordnung):** Ändern Sie per PowerShell auf `VM-SRV02` die Zuordnung des ersten Netzwerkadapters oder trennen Sie ihn (`Disconnect-VMNetworkAdapter`). Diagnostizieren Sie von `VM-SRV01` aus den Ausfall der Verbindung zu `192.168.100.12`, prüfen Sie auf `HV-HOST01` mit `Get-VMNetworkAdapter` den Verbindungsstatus aller VMs, sichten Sie die Protokolle `Hyper-V-VmSwitch` und `Hyper-V-Hypervisor` (Anwendungs- und Dienstprotokolle → Microsoft → Windows) auf zugehörige Einträge und stellen Sie die korrekte Verbindung zu `vSwitch-Intern-Mgmt` (`Connect-VMNetworkAdapter`) wieder her. Prüfen Sie abschließend, dass beide VMs sauber laufen und sich sowohl auf `192.168.100.x` als auch auf `10.10.20.x` gegenseitig per Ping erreichen.

#### Kontrollfragen

1. Warum zeigt der klassische Windows Task-Manager im Host-Betriebssystem (Parent Partition) unter dem Reiter „Prozesse“ oder „Leistung“ oft eine deutlich zu niedrige CPU-Auslastung an, obwohl mehrere Gast-VMs unter Volllast arbeiten?
2. Welcher Leistungsindikator (Performance Counter) in `perfmon.exe` muss herangezogen werden, um die tatsächliche Gesamtauslastung der physischen logischen Prozessoren durch den Hypervisor und alle laufenden VMs zu messen?
3. In welchen Ereignisprotokollen unter `Anwendungs- und Dienstprotokolle -> Microsoft -> Windows` suchen Sie zuerst, wenn sich eine virtuelle Maschine nicht starten lässt (zwei Protokolle), und in welchem, wenn ein virtueller Switch einen Fehler meldet?
4. Welche Kennzahlen liefert das PowerShell-Cmdlet `Measure-VM` nach Aktivierung des Resource Metering, und warum ist diese Funktion standardmäßig deaktiviert?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Die erste Fassung des Gem wurde geprüft und an den folgenden Stellen geändert. Stundensummen, Prioritäten und Modulreihenfolge blieben unverändert (12 Module, 110 UE).

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| A.2 | Drei geprüfte Quellen ergänzt (Nested Virtualization, Live-Migration ohne Failover Clustering, Add-VMHardDiskDrive) | Aussagen zu Nested Virtualization, Live-Migration und `-ShareVirtualDisk` abgesichert |
| A.3 | Klarstellung: keine Active-Directory-Domäne im Labor, `lab.internal` nur Namensraum | `lab.internal` wurde als Domäne genannt, aber nie aufgebaut |
| Modul 2, Aufgabe 4 | Import als Kopie mit neuer ID, Umbenennung, Aufräumen ergänzt | Lernziel „exportieren und importieren“ wurde nur zur Hälfte geübt |
| Modul 3, Aufgabe 4 (neu) | DHCP-Guard, Router-Guard, MAC-Spoofing, Portspiegelung konfigurieren und zurücksetzen | Lernziel 3 hatte keine Praxisaufgabe |
| Modul 5, Aufgabe 2 | Begründung des Rückbaus auf statischen RAM geändert | Dynamic Memory ist mit Nested Virtualization laut aktueller Doku nicht verboten |
| Modul 8 (Lernziel 2, 8.2, Aufgabe 1, Kontrollfragen 1 und 4) | „Dynamic Memory muss deaktiviert werden“ ersetzt durch „statischer RAM empfohlen, da Änderung nur bei ausgeschalteter VM möglich“; vCPU-Angabe „2 (oder 4)“ auf 2 festgelegt; Aussage zu Live-Migration und Save State entfernt | veraltete bzw. nicht bestätigte Aussage; mehrdeutige Angabe |
| Modul 9 (Lernziel 3, 9.3, 9.4, Aufgaben 1 bis 3, Kontrollfrage 5 neu) | Live-Migration wird konfiguriert und bewertet, aber nicht ausgeführt; `Move-VM` nur als Syntax; Rückbau der Migrationseinstellungen ergänzt; Hinweis zu CredSSP unter Server 2025 | Live-Migration erfordert eine Domäne, die im Labor nicht existiert; Lernziel entsprechend angepasst |
| Modul 10 (Lernziel 2, Aufgaben 1 und 3) | Zertifikatsablauf konkretisiert (Export, Übertragung, Import, Replikatserver-Einstellung), Rückbau um Zertifikate, Firewallregeln, hosts-Einträge, Ordner erweitert | Ablauf war nicht ausführbar beschrieben; Rückstände blieben bestehen |
| Modul 11 (Voraussetzungen, Aufgaben 3 und 4) | Voraussetzung nur Modul 8; `Test-Cluster` als Einzelknoten-Validierung mit erwarteten Meldungen; Rückbau auf die Änderungen des Moduls beschränkt, Feature-Deinstallation ergänzt | Nested-Rückbau hing am optionalen Modul 11 |
| Modul 12 (Voraussetzungen, Aufgabe 1 neu, Kontrollfrage 3, Aufgabe 3) | Idempotente Ausgangslage-Aufgabe (inklusive Deinstallation der Hyper-V-Rolle in den Gast-VMs); Lastbefehle konkretisiert; Protokolle `Hyper-V-VmSwitch` und `Hyper-V-Hypervisor` in die Diagnose einbezogen; Kontrollfrage 3 präzisiert | Rückbau darf nicht von optionalen Modulen abhängen; Lernziel 2 war nur teilweise abgedeckt |

**Hinweise und offene Punkte:**

* Alle neu ergänzten Befehle und Parameter wurden nur gegen die Dokumentation bzw. den Wissensstand geprüft, **nicht im Labor ausgeführt**. Vor Kursstart im Labor zu prüfen: `Import-VM -Copy -GenerateNewId` mit Pfadparametern (Modul 2), die Portspiegelung und `PortMirroringMode` (Modul 3), `Add-VMMigrationNetwork` und `Remove-VMMigrationNetwork` (Modul 9), Zertifikatseigenschaften und `Set-VMReplicationServer`-Parameter (Modul 10), Regelnamen der Firewall (Replikat-HTTPS-Listener, `FPS-SMB-In-TCP`), `New-VHD ... .vhds -Dynamic` (Modul 11), Verhalten von `Test-Cluster` ohne Domäne (Modul 11).
* Aktuelle Einschränkungen der Nested Virtualization (Live-Migration, Save State, Checkpoints) für die eingesetzte Windows-Server-Version vor Kursstart in der Microsoft-Dokumentation prüfen.
* Modul 8 ist als Priorität 1 geführt, dient praktisch aber nur den optionalen Modulen 9 bis 11. Die Einstufung wurde nicht geändert; sie ist eine inhaltliche Entscheidung.
* Erweiterungsmöglichkeit: Mit einer zusätzlichen Domänencontroller-VM (Active Directory) könnten Live-Migration (Kerberos) und Replica mit Kerberos praktisch ausgeführt werden. Das würde Labor-Setup, Modul 9 und die Stundenverteilung verändern und wurde nicht umgesetzt.