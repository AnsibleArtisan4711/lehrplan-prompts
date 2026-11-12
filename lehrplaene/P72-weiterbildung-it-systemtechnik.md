# Lehrplan: Weiterbildung IT-Systemtechnik

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Absolventen einer IT-Lehre und Berufseinsteiger in der Systemtechnik (Raum Österreich/EU), die sich auf eine Spezialisierung (Netzwerk, Windows/Workplace, Linux, Cloud, Security) vorbereiten |
| **Vorkenntnisse** | IT-Grundlagen aus der Lehre: Bedienung von Windows und einer Linux-Shell, Grundbegriffe der Netzwerktechnik (IP-Adresse, Subnetzmaske, Gateway), Umgang mit virtuellen Maschinen |
| **Gesamtumfang** | 12 Module, 110 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows Server 2025 (Evaluation), Active Directory, Windows 11 Enterprise (Evaluation), Microsoft Intune und Microsoft Entra ID (Testzugang), Ubuntu Server 24.04 LTS, Hyper-V (als Laborumgebung), Microsoft Azure (Testzugang), Windows PowerShell 5.1, Bash |
| **Thematische Abgrenzung (Out of Scope)** | Keine Praxis zu Exchange Online, Teams und SharePoint (kein Lizenz-Testzugang vorgesehen; nur Einordnung in Modul 4). Kein praktischer Aufbau von Entra Connect, Clustern, SAN/NAS, VMware oder Proxmox (nur Konzept). Keine Zertifizierungsprüfung, keine Prüfungsvorbereitung mit Fragenkatalogen. Keine Verwendung produktiver Mandanten, Konten oder Netze. Kein Aufbau von Ticketsystemen oder Monitoring-Produkten (nur Konzept und eigene Skripte). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Berufsbild IT-Systemtechnik und Spezialisierungslandkarte | 1 | 8 |
| 2 | Netzwerk, Protokolle und Infrastruktur als Grundspezialisierung | 1 | 9 |
| 3 | Windows Server, Active Directory und Hybrid Identity | 1 | 10 |
| 4 | Modern Workplace, Microsoft 365 und Endpoint Management | 1 | 10 |
| 5 | Linux-Server, Open-Source-Dienste und Plattformbetrieb | 1 | 9 |
| 6 | Virtualisierung, Storage und Plattformen für Rechenzentrum und Edge | 2 | 9 |
| 7 | Cloud Administration und Hybrid Platforms | 1 | 10 |
| 8 | Monitoring, Logging, Backup und Business Continuity | 1 | 9 |
| 9 | Security, Hardening und Identity & Access Management | 1 | 10 |
| 10 | Automation, Scripting und Infrastructure as Code Grundlagen | 1 | 10 |
| 11 | Troubleshooting, ITSM, Dokumentation und Governance im Betrieb | 2 | 8 |
| 12 | Karrierepfade, Zertifikate und Spezialisierungen nach der Lehre | 1 | 8 |
| **Gesamt** | **10 Pflichtmodule, 2 Vertiefungsmodule** | | **110** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln die Kernkompetenzen (93 UE). Module mit Priorität 2 (Modul 6 und 11, zusammen 17 UE) dienen der Vertiefung und können bei Zeitmangel gekürzt oder ins Selbststudium verlegt werden. Kein Pflichtmodul setzt ein Modul mit Priorität 2 voraus: Die Sicherungsaufgaben in Modul 8 bauen ihre Datenträger selbst auf, und Modul 12 braucht kein Ergebnis aus Modul 6 oder 11. Abweichung von der Vorlage: Modul 5 hat in der Excel-Vorlage Priorität 2, wird hier aber auf Priorität 1 gesetzt, weil die Module 8, 9 und 10 Aufgaben mit dem Linux-Server (LX-UBU01) enthalten und deshalb Modul 5 voraussetzen. Die in der Vorlage angegebenen „Dauer (h)“ werden als Unterrichtseinheiten zu 45 Minuten gelesen (Annahme). Die UE enthalten Theorie und angeleitete Praxis; die Laboraufgaben können je nach Vorkenntnissen zusätzliche Übungszeit erfordern, die nicht in den UE enthalten ist.*

### 2. Quellen

Alle Microsoft-Learn-Angaben stammen aus Suchtreffer-Auszügen vom 12.11.2026 (Seiten nicht vollständig gelesen). Wo eine Aussage nur aus dem Gedächtnis stammt oder eine Seite nicht abgerufen wurde, ist das im Text als „nicht bestätigt“ oder „nicht geprüft“ gekennzeichnet. Eine Veröffentlichungsangabe („Stand“) liefern die Suchtreffer in der Regel nicht.

* **Excel-Vorlage** „Lehrplan - Weiterbildung IT Systemtechnik.xlsx“ (Blätter „Lehrplan in Modulen“ und „Lehrplan in Details“): Modultitel, Einheiten, Stunden und Prioritäten stammen von dort. Die „Lernziele & Inhalte“ der Modulübersicht sind in der Vorlage für alle zwölf Module wortgleich (allgemeiner Platzhaltertext); Lernziele, Praxisaufgaben und Kontrollfragen in diesem Lehrplan sind neu geschrieben.
* **Hyper-V Checkpoints** (Microsoft Learn): [https://learn.microsoft.com/windows-server/virtualization/hyper-v/checkpoints](https://learn.microsoft.com/windows-server/virtualization/hyper-v/checkpoints). Standard- und Produktions-Checkpoints, `Set-VM -CheckpointType`, `Get-VMSnapshot`/`Remove-VMCheckpoint`; Hinweis, dass ein Standard-Checkpoint kein Backup ist und bei Systemen mit Datenreplikation wie Active Directory Konsistenzprobleme verursachen kann.
* **Hyper-V Dynamic Memory** ([https://learn.microsoft.com/windows-server/virtualization/hyper-v/dynamic-memory](https://learn.microsoft.com/windows-server/virtualization/hyper-v/dynamic-memory)), **Export und Import von VMs** ([https://learn.microsoft.com/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines](https://learn.microsoft.com/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines)) und **Import-VM** ([https://learn.microsoft.com/powershell/module/hyper-v/import-vm](https://learn.microsoft.com/powershell/module/hyper-v/import-vm)): Startup/Minimum/Maximum RAM, `Export-VM`, `Import-VM -Copy -GenerateNewId`.
* **Hyper-V NAT-Netzwerk** ([https://learn.microsoft.com/windows-server/virtualization/hyper-v/setup-nat-network](https://learn.microsoft.com/windows-server/virtualization/hyper-v/setup-nat-network)): `New-VMSwitch`, `New-NetNat`. Ob der „Default Switch“ auf einem Windows-Server-Host verfügbar ist, ist nicht bestätigt.
* **Set-VMNetworkAdapterVlan** ([https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadaptervlan](https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadaptervlan)), **Hyper-V Generation-2-Sicherheit** ([https://learn.microsoft.com/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features](https://learn.microsoft.com/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features)), **Enable-VMTPM** ([https://learn.microsoft.com/powershell/module/hyper-v/enable-vmtpm](https://learn.microsoft.com/powershell/module/hyper-v/enable-vmtpm)) und **Set-VMKeyProtector** ([https://learn.microsoft.com/powershell/module/hyper-v/set-vmkeyprotector](https://learn.microsoft.com/powershell/module/hyper-v/set-vmkeyprotector)): VLAN auf VM-Adaptern, Secure-Boot-Vorlage `MicrosoftUEFICertificateAuthority` für Linux, virtuelles TPM.
* **Ubuntu auf Hyper-V** ([https://learn.microsoft.com/windows-server/virtualization/hyper-v/supported-ubuntu-virtual-machines-on-hyper-v](https://learn.microsoft.com/windows-server/virtualization/hyper-v/supported-ubuntu-virtual-machines-on-hyper-v)); **Ubuntu Server Download** ([https://ubuntu.com/download/server](https://ubuntu.com/download/server)) und **Ubuntu 24.04 Images** ([https://releases.ubuntu.com/releases/24.04/](https://releases.ubuntu.com/releases/24.04/)), nur als Suchtreffer gesehen; **Netplan-Referenz** ([https://netplan.io/reference](https://netplan.io/reference)), nur als Suchtreffer gesehen (Syntax der Beispiel-Konfiguration nicht bestätigt, vor dem Kurs im Labor prüfen). `systemd`, `ufw`, `journalctl`, `unattended-upgrades` und OpenSSH: Keine geprüfte Quelle, Befehle aus dem Gedächtnis.
* **Windows Server 2025, Evaluierung** ([https://www.microsoft.com/evalcenter/evaluate-windows-server-2025](https://www.microsoft.com/evalcenter/evaluate-windows-server-2025)): 180 Tage. **Windows 11 Enterprise, Evaluierung** (Microsoft Evaluation Center, Seite nicht abgerufen): 90 Tage laut früherem Lehrplan, nicht geprüft.
* **Install-ADDSForest** ([https://learn.microsoft.com/powershell/module/addsdeployment/install-addsforest](https://learn.microsoft.com/powershell/module/addsdeployment/install-addsforest)); **Group Policy overview** ([https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)) und **Group Policy processing** ([https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing)): GPO-Verknüpfung auf Standort, Domäne, OU; Reihenfolge lokal, Standort, Domäne, OU.
* **Set-NetIPInterface** ([https://learn.microsoft.com/powershell/module/nettcpip/set-netipinterface](https://learn.microsoft.com/powershell/module/nettcpip/set-netipinterface)): `-Forwarding Enabled`. `New-NetFirewallRule`, `Test-NetConnection`, `New-NetRoute`, `Rename-NetAdapter`, `Set-DnsClientServerAddress`, `Add-Computer`, `Get-NetTCPConnection`, `Get-WinEvent`, `Register-ScheduledTask`, `Invoke-Command`, `auditpol`, `sc.exe failure`: Cmdlets bzw. Programme aus dem Gedächtnis, im Text als „nicht bestätigt“ markiert, soweit nicht oben belegt.
* **Windows Server Backup / wbadmin:** Installation und Sicherung ([https://learn.microsoft.com/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-a-full-server](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-a-full-server)), `wbadmin start backup` ([https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-backup](https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-backup)), `wbadmin get versions` ([https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-get-versions](https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-get-versions)), `wbadmin start recovery` ([https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-recovery](https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-recovery)), `wbadmin start systemstaterecovery` ([https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-systemstaterecovery](https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-systemstaterecovery)). **Volume Shadow Copy Service** ([https://learn.microsoft.com/windows-server/storage/file-server/volume-shadow-copy-service](https://learn.microsoft.com/windows-server/storage/file-server/volume-shadow-copy-service)).
* **New-EventLog / Write-EventLog** (Windows PowerShell 5.1): [https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-eventlog?view=powershell-5.1](https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-eventlog?view=powershell-5.1).
* **PowerShell Desired State Configuration** (DSC 1.1, Windows PowerShell 5.1): [https://learn.microsoft.com/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1](https://learn.microsoft.com/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1).
* **Microsoft Intune, kostenlose Testversion** ([https://learn.microsoft.com/intune/fundamentals/free-trial-sign-up](https://learn.microsoft.com/intune/fundamentals/free-trial-sign-up)): 30 Tage, Anmeldung mit Zahlungskarte zur Überprüfung, Domäne `<name>.onmicrosoft.com`. **Compliance-Richtlinie in Intune** ([https://learn.microsoft.com/intune/device-security/compliance/create-policy](https://learn.microsoft.com/intune/device-security/compliance/create-policy)). **BitLocker mit Intune** ([https://learn.microsoft.com/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows](https://learn.microsoft.com/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows)): Wiederherstellungsschlüssel in Entra ID, Löschen des Intune-Objekts eines BitLocker-Geräts lässt BitLocker auf dem Systemvolume im Zustand „suspendiert“. **dsregcmd** ([https://learn.microsoft.com/entra/identity/devices/troubleshoot-device-dsregcmd](https://learn.microsoft.com/entra/identity/devices/troubleshoot-device-dsregcmd)).
* **Azure Free Account** ([https://learn.microsoft.com/azure/cost-management-billing/manage/create-free-services](https://learn.microsoft.com/azure/cost-management-billing/manage/create-free-services)) und **Kosten vermeiden** ([https://learn.microsoft.com/azure/cost-management-billing/manage/avoid-charges-free-account](https://learn.microsoft.com/azure/cost-management-billing/manage/avoid-charges-free-account)): Guthaben (laut Learn 200 USD für 30 Tage; Betrag kann sich ändern und ist vor der Anmeldung auf der Anmeldeseite zu prüfen), Telefonnummer, Zahlungskarte und Microsoft-/GitHub-Konto erforderlich. **Azure-Budgets** ([https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-acm-create-budgets](https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-acm-create-budgets)). **Azure RBAC** ([https://learn.microsoft.com/azure/role-based-access-control/overview](https://learn.microsoft.com/azure/role-based-access-control/overview), [https://learn.microsoft.com/azure/role-based-access-control/scope-overview](https://learn.microsoft.com/azure/role-based-access-control/scope-overview)). **Azure Policy, integrierte Definitionen** ([https://learn.microsoft.com/azure/governance/policy/samples/built-in-policies](https://learn.microsoft.com/azure/governance/policy/samples/built-in-policies)): „Allowed locations“.
* **Entra-Sicherheitsstandards** ([https://learn.microsoft.com/entra/fundamentals/security-defaults](https://learn.microsoft.com/entra/fundamentals/security-defaults)), **MFA-Lizenzierung** ([https://learn.microsoft.com/entra/identity/authentication/concept-mfa-licensing](https://learn.microsoft.com/entra/identity/authentication/concept-mfa-licensing)), **Conditional Access im Nur-Bericht-Modus** ([https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-report-only](https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-report-only)), **Notfallzugriffskonten** ([https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access](https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access)), **Kennwort-Hashsynchronisierung** ([https://learn.microsoft.com/entra/identity/hybrid/connect/whatis-phs](https://learn.microsoft.com/entra/identity/hybrid/connect/whatis-phs)).
* **Zertifizierungen:** AZ-104 ([https://learn.microsoft.com/credentials/certifications/resources/study-guides/az-104](https://learn.microsoft.com/credentials/certifications/resources/study-guides/az-104)); MS-102 ([https://learn.microsoft.com/credentials/certifications/exams/ms-102/](https://learn.microsoft.com/credentials/certifications/exams/ms-102/); der Studienleitfaden nennt als Auslaufdatum den 30.11.2026, der aktuelle Status ist auf der Seite zu prüfen); CCNA ([https://www.cisco.com/go/ccna](https://www.cisco.com/go/ccna), nur als Suchtreffer gesehen); RHCSA (EX200, [https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam), nur als Suchtreffer gesehen); LPIC-1 (Linux Professional Institute, [https://www.lpi.org/](https://www.lpi.org/), Prüfungsstruktur nicht geprüft). Prüfungsinhalte, Preise und Auslaufdaten ändern sich und sind vor jeder Planung auf den Herstellerseiten zu prüfen.
* **Hypervisoren:** Proxmox VE Administration Guide ([https://pve.proxmox.com/pve-docs](https://pve.proxmox.com/pve-docs), nur als Suchtreffer gesehen); VMware: Keine geprüfte Quelle.
* **RFC 1918** (Address Allocation for Private Internets, [https://datatracker.ietf.org/doc/html/rfc1918](https://datatracker.ietf.org/doc/html/rfc1918), nur als Suchtreffer gesehen): private Adressbereiche. Die Top-Level-Domain `.internal` ist für die private Verwendung reserviert (Quelle nicht abgerufen, nicht bestätigt).
* **Technikbegriffe ohne eigene Quelle** (DNS, DHCP, NTLM, WinRM, TOTP, SSH): Allgemeinwissen, Keine geprüfte Quelle; Windows-Computernamen im Gast entsprechen den VM-Namen (höchstens 15 Zeichen), die DNS-Namen lauten daher z. B. `srv-dc01.lab.example.internal`.
* **Bicep und Terraform** (Modul 10, nur Theorie) und **3-2-1-Regel** für Backups (Modul 8): Keine geprüfte Quelle, Allgemeinwissen.
* **ITIL** (Begriffe Incident, Problem, Change in Modul 11): Keine geprüfte Quelle, Begriffe sind als Allgemeinwissen verwendet; offizielle Definitionen nicht geprüft.
* **Arbeitsmarkt Österreich** (Modul 1 und 12): AMS-Berufsinformation und Stelleninserate wurden nicht geprüft; die Lernenden recherchieren selbst, und Aussagen zum Markt gelten nur für die von ihnen gesammelten Inserate.

### 3. Labor-Setup & Rahmenbedingungen

**Alle Befehle in diesem Lehrplan wurden nicht ausgeführt**, weil keine Hyper-V-Umgebung zur Verfügung stand. Cmdlets und Befehle, die Microsoft Learn belegt (siehe Quellen), sind nicht besonders markiert; alles andere ist als „nicht bestätigt“ gekennzeichnet und vor dem Kurs im Labor zu prüfen. Alle Kennwörter vergibt der Kursleiter bzw. die Lernenden selbst; sie stehen in keinem Dokument.

* **Hyper-V-Host (erforderlich ab Modul 2):** Windows 11 Pro/Enterprise oder Windows Server mit aktiviertem Hyper-V, mindestens 16 GB Arbeitsspeicher (dann nur die jeweils benötigten VMs starten), empfohlen 24 GB, und etwa 250 GB freier Speicher (Annahmen des Lehrplans, nicht gemessen). Der Host braucht einmalig Internet für die ISO-Dateien (Internetphase I-1). Es müssen nicht alle VMs gleichzeitig laufen. Laufwerksbuchstaben und Pfade auf dem Host (z. B. `D:`) sind Beispiele und anzupassen.
* **Virtuelle Switches (erforderlich ab Modul 2):** `sw-lab-srv` (privat, Servernetz `192.168.50.0/24`), `sw-lab-cli` (privat, Clientnetz `192.168.60.0/24`), ab Modul 6 zusätzlich `sw-lab-test` (privat, nur für Klon-Tests). Für die Internetphasen dient der `Default Switch` (NAT, auf Windows-Client-Hyper-V vorhanden). Fehlt er (z. B. auf einem Server-Host, nicht bestätigt), wird ein eigener NAT-Switch nach Learn „Set up a NAT network“ mit `192.168.100.0/24` angelegt; der DNS-Server muss dort manuell gesetzt werden. Das Labornetz hat sonst keine Verbindung zum Heim- oder Firmennetz.
* **Virtuelle Maschinen:**

| VM | Betriebssystem / Ausstattung | Adresse(n) | Erforderlich ab |
| :--- | :--- | :--- | :--- |
| `SRV-DC01` | Windows Server 2025 Standard Evaluation (Desktop-Darstellung), Generation 2, 2 vCPU, 4 GB RAM, 60 GB; später Domänencontroller | `192.168.50.10/24`, **kein** Standardgateway, statische Route zu `192.168.60.0/24` über `192.168.50.20`; **kein** Internetadapter | Modul 2 (Heraufstufung in Modul 3) |
| `SRV-FS01` | Windows Server 2025 Standard Evaluation, Generation 2, 2 vCPU, 4 GB RAM, 60 GB; Dateiserver und Router | `NIC-LAB` `192.168.50.20/24` (`sw-lab-srv`), `NIC-CLI` `192.168.60.1/24` (`sw-lab-cli`), `NIC-INET` (Default Switch, normalerweise getrennt) | Modul 2 |
| `CL-W11-01` | Windows 11 Enterprise Evaluation, Generation 2, vTPM, 2 vCPU, 4 GB RAM, 80 GB; ab Modul 3 Domänenmitglied | `192.168.60.101/24`, Gateway `192.168.60.1`, DNS `192.168.50.10`; `NIC-INET` normalerweise getrennt | Modul 2 |
| `LX-UBU01` | Ubuntu Server 24.04 LTS, Generation 2, Secure-Boot-Vorlage `MicrosoftUEFICertificateAuthority` (`Set-VMFirmware -VMName LX-UBU01 -SecureBootTemplate MicrosoftUEFICertificateAuthority`), 1 vCPU, 2 GB RAM, 30 GB | `192.168.50.30/24` (netplan), Route zu `192.168.60.0/24` über `192.168.50.20`, DNS `192.168.50.10`; `NIC-INET` mit DHCP und `optional: true` | Modul 5 |
| `CL-W11-02` | Windows 11 Enterprise Evaluation, Generation 2, vTPM (`Set-VMKeyProtector -NewLocalKeyProtector`, dann `Enable-VMTPM`), 2 vCPU, 4 GB RAM, 80 GB; **nur Cloud-Mandant**, nie Domänenmitglied | nur `Default Switch`, **nie** mit dem Labornetz verbunden | Modul 4 |

* **Domäne:** `lab.example.internal`, NetBIOS-Name `LAB` (entsteht in Modul 3). Vor Modul 3 gibt es keinen DNS-Server; Modul 2 arbeitet nur mit IP-Adressen.
* **Routing im Labor:** `SRV-FS01` leitet zwischen `192.168.50.0/24` und `192.168.60.0/24` (`Set-NetIPInterface -InterfaceAlias <Name> -Forwarding Enabled` auf beiden Labor-Adaptern). Da `SRV-DC01` und `LX-UBU01` kein Standardgateway haben, brauchen sie die statische Route zurück ins Clientnetz.
* **Internetphasen (Regel):** Internet gibt es nur in benannten Phasen: **I-1** (Host-Downloads der ISO-Dateien), **I-2** (`SRV-FS01` zieht Windows-Updates, Modul 3.6), **I-3** (`LX-UBU01`: Installation, `apt`; `CL-W11-01`: OpenSSH-Client falls fehlend, Modul 5), dazu dauerhaft `CL-W11-02` (Cloud-Mandant, Modul 4 ff.). Während einer Phase werden die Labor-Adapter der betroffenen VM getrennt (`Disconnect-VMNetworkAdapter -VMName <VM> -Name NIC-LAB`) und `NIC-INET` verbunden (`Connect-VMNetworkAdapter -VMName <VM> -Name NIC-INET -SwitchName "Default Switch"`); danach wird alles umgekehrt. Ob die Ubuntu-Installation ohne Internet vollständig durchläuft, ist nicht bestätigt; deshalb liegt sie in Phase I-3.
* **Prüfpunkte (Checkpoints):** Prüfpunkte von `SRV-DC01` und `SRV-FS01` nur bei ausgeschalteter VM (Learn: Standard-Checkpoints können bei Active Directory Konsistenzprobleme verursachen) und für das gesamte Labor nur gemeinsam zurücksetzen. Ein Prüfpunkt ist keine Datensicherung (siehe Modul 8). Die Prüfpunkte heißen `<VM>-M<Nr>-Start`.
* **Cloud-Testzugänge (Ausnahme vom isolierten Labor, nur nach ausdrücklicher Zustimmung der Lernenden):**
  * **Intune-Testmandant (erforderlich ab Modul 4):** kostenlose 30-Tage-Testversion (Learn); Zahlungskarte nur zur Überprüfung, kein Kauf; Domäne `<name>.onmicrosoft.com`. Beginn erst bei Start von Modul 4, damit die 30 Tage reichen; nach Ablauf prüfen, ob sich die Testversion automatisch verlängert (nicht bestätigt). Kosten: 0 EUR, solange nichts dazugebucht wird.
  * **Azure Free Account (erforderlich ab Modul 7):** Guthaben für 30 Tage (laut Learn 200 USD, vor Anmeldung prüfen), Telefonnummer, Zahlungskarte, Microsoft- oder GitHub-Konto. Kosten: 0 EUR innerhalb des Guthabens; ein Budget mit Warnung (Modul 7.7) und das Löschen der Ressourcengruppe am Ende sind Pflicht. Der zugehörige Entra-Mandant (Entra ID Free) wird in Modul 9 für die Sicherheitsstandards (MFA) weiterverwendet; ob er nach Ablauf des Guthabens bestehen bleibt, ist nicht bestätigt (Ersatz: Fallstudie).
  * **Nicht vorgesehen:** das Microsoft-365-Entwicklerprogramm (Zugang an Bedingungen geknüpft, nicht bestätigt) und jeder produktive Mandant. Exchange, Teams und SharePoint werden nur theoretisch behandelt.
* **Evaluierungs-Laufzeit:** Windows Server 180 Tage, Windows 11 Enterprise 90 Tage (nicht geprüft): Startdatum notieren; nach Ablauf ist der Kurs neu aufzusetzen oder die Evaluierung zu erneuern.
* **Vom Kursleiter bereitzustellen:** ISO-Dateien, Adress- und Namensplan als Vorlage, Kennwörter, Liste der eingebauten Fehler (Modul 2, 5, 9, 11).
* **Nicht möglich im Labor:** Exchange/Teams/SharePoint-Praxis, Entra-Connect-Synchronisation, Cluster, Hardware-RAID/SAN. Diese Themen sind in den Modulen ausdrücklich als Theorie oder Fallstudie gekennzeichnet.

## B. Detaillierter Modulaufbau

Konvention: Befehle für Windows laufen in Windows PowerShell 5.1 (als Administrator), sofern nichts anderes steht. Befehle mit dem Zusatz „nicht bestätigt“ sind weder in einer Umgebung ausgeführt noch durch Learn belegt. Alle Kennwörter werden interaktiv eingegeben (`Read-Host -AsSecureString` bzw. Eingabeaufforderung) und nicht in Dokumenten oder Skripten gespeichert.

### Modul 1: Berufsbild IT-Systemtechnik und Spezialisierungslandkarte
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zielrollen der Systemtechnik (Systemadministration, Netzwerk, Modern Workplace, Cloud, Security Operations) und die Betriebsmodelle On-Prem, Hybrid und Cloud anhand von Stelleninseraten unterscheiden und einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende seine eigenen Kompetenzen in einer Matrix mit Nachweisen bewerten und die Lücken zu einer gewählten Zielrolle benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikate anhand von Herstellerseiten recherchieren, eine Reihenfolge begründen und einen Entwicklungsplan für 12 bis 24 Monate mit Meilensteinen erstellen.
* **Voraussetzungen:** Keine. Kein technisches Labor; dieses Modul arbeitet mit Recherche und Fallstudien.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Marktüberblick Systemtechnik: Zielrollen in Unternehmen, IT-Dienstleistern und MSPs, Nachfrage nach Cloud-, Workplace- und Security-Rollen | 1 |
| 1.2 | On-Prem, Hybrid und Cloud: Betriebsmodelle unterscheiden, Auswirkungen auf Karrierepfad und Skill-Aufbau | 1 |
| 1.3 | Kernkompetenzen nach der Lehre: Netzwerk, Betriebssysteme, Scripting, Security priorisieren, Lücken sichtbar machen | 1 |
| 1.4 | Typische Zielrollen: Systemadministration, Netzwerk, Modern Workplace, Cloud und Security Operations vergleichen, Passung nach Interessen | 1 |
| 1.5 | Zertifizierungslogik: Herstellerzertifikate und praxisnahe Nachweise einordnen, Reihenfolge planen | 1 |
| 1.6 | Arbeitsumfelder in Österreich: KMU, Enterprise, öffentliche Verwaltung, Dienstleister; typische Systemlandschaften | 1 |
| 1.7 | Praxis versus Theorie: Bedeutung von Lab, Troubleshooting und Projektarbeit für Bewerbungen, Lerntransfer | 1 |
| 1.8 | Persönlicher Entwicklungsplan: Stärken, Zielrolle und Lernprioritäten für 12 bis 24 Monate | 1 |

#### Praxisaufgaben (Hands-on Lab)
Dieses Modul hat kein technisches Labor. Die Aufgaben sind Recherche- und Fallstudienaufgaben; Ergebnisse werden als Dokument im Markdown-Format abgelegt.

1. **Stelleninserate auswerten (Lernziel 1; Einheiten 1.1, 1.4, 1.6):** Sammle 10 aktuell veröffentlichte Stelleninserate aus Österreich (bevorzugt Raum Wien) für Rollen wie Systemadministrator, Systemtechniker, Netzwerktechniker, Modern-Workplace-Administrator, Cloud-Administrator oder Security-Analyst. Lege eine Tabelle an mit den Spalten: Quelle (URL, Abrufdatum), Rolle, Arbeitgebertyp (KMU, Konzern, öffentliche Verwaltung, IT-Dienstleister/MSP), genannte Technologien, genannte Zertifikate, Betriebsmodell (On-Prem, Hybrid, Cloud). Werte die Tabelle mit einer Strichliste aus und formuliere drei Aussagen. **Wichtig:** Die Aussagen gelten nur für diese 10 Inserate und sind nicht als Marktstatistik zu formulieren.
2. **Betriebsmodelle zuordnen (Lernziel 1; Einheit 1.2):** Fallstudie: Ein Betrieb mit 40 Mitarbeitenden betreibt Dateiablage, E-Mail, Benutzeranmeldung, Drucker, Datensicherung und einen Webshop. Ordne jeden der sechs Dienste einem Betriebsmodell zu (On-Prem, Hybrid, Cloud) und begründe die Zuordnung in je einem Satz. Nenne für jedes Modell zwei Fähigkeiten, die ein Administrator dafür braucht.
3. **Zielrollen vergleichen (Lernziel 1; Einheit 1.4):** Erstelle eine Vergleichstabelle der fünf Zielrollen mit den Spalten: typische Aufgaben (aus deinen Inseraten), häufigste Werkzeuge, Interessenprofil („Wer passt dazu?“), Einstiegshürde. Kennzeichne, welche Aussagen aus Aufgabe 1 stammen und welche deine Einschätzung sind.
4. **Kompetenzmatrix (Lernziel 2; Einheit 1.3):** Bewerte dich in den Feldern Netzwerk, Windows, Linux, Scripting, Security und Cloud mit 0 (keine Erfahrung) bis 3 (selbstständig im Betrieb). Jede Bewertung ab 1 braucht einen Nachweis (Projekt, Aufgabe, Lab). Vergleiche mit der Zielrolle aus Aufgabe 3 und nenne die drei größten Lücken.
5. **Zertifikatsreihenfolge (Lernziel 3; Einheit 1.5):** Wähle für zwei Zielrollen je zwei Zertifikate. Lies auf der Herstellerseite nach (Quelle mit URL und Abrufdatum angeben): Prüfungscode, Voraussetzungen, Gültigkeit bzw. Auslaufdatum und Preis. Begründe die Reihenfolge nach Vorkenntnis, Kosten und Praxisnähe. **Wichtig:** Keine Angaben aus dem Gedächtnis; sind Daten nicht auffindbar, schreibe „nicht geprüft“.
6. **Nachweise aus Praxis (Lernziel 3; Einheit 1.7):** Plane drei Nachweise, die du in den nächsten drei Monaten erzeugst (z. B. dokumentiertes Labor, ein Skript in einem Git-Repository, ein Troubleshooting-Protokoll). Lege fest, wie jeder Nachweis ohne Kennwörter, echte Firmennamen oder Kundendaten veröffentlicht werden kann.
7. **Entwicklungsplan (Lernziel 3; Einheit 1.8):** Schreibe einen Plan für 12 bis 24 Monate: Zielrolle, drei Meilensteine mit Datum, Lernzeit pro Woche, Kontrollpunkt alle drei Monate, Kriterium „Ziel erreicht“. Der Plan muss zu den Lücken aus Aufgabe 4 passen.

#### Kontrollfragen
1. Worin unterscheiden sich die Betriebsmodelle On-Prem, Hybrid und Cloud, und was ändert sich dadurch für die Aufgaben eines Administrators?
2. Warum dürfen Aussagen aus zehn gesammelten Inseraten nicht als Marktstatistik verwendet werden?
3. Welche vier Kernkompetenzen gelten laut Einheit 1.3 als Basis, und woran erkennt man eine Lücke im Nachweis?
4. Nach welchen drei Kriterien lässt sich eine Reihenfolge von Zertifikaten begründen, und woher stammen die Fakten dazu?
5. Warum sind dokumentierte Lab-Projekte in einer Bewerbung wertvoll, und was darf darin nicht stehen?

---

### Modul 2: Netzwerk, Protokolle und Infrastruktur als Grundspezialisierung
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Fehlersymptome den Schichten des OSI- und TCP/IP-Modells zuordnen, Subnetze berechnen und die Konzepte VLAN, WLAN und NAT erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Labornetz mit zwei Subnetzen aufbauen (statische Adressen, Routing über einen Windows-Server, Firewallregeln) und mit Netzplan und Portplan dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende Konnektivitätsfehler (Gateway, Weiterleitung, Firewall) mit einer festen Prüfreihenfolge eingrenzen und beheben.
* **Voraussetzungen:** Hyper-V-Host und ISO-Dateien aus Internetphase I-1 (siehe A.3). Modul 1 ist nicht erforderlich.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | OSI und TCP/IP praxisnah: Protokollebenen mit typischen Störungen verknüpfen, Netzwerkfehler lokalisieren | 1,2 |
| 2.2 | IP-Adressierung und Subnetting: Adresspläne für kleine und mittlere Umgebungen, Bezug zu VLANs und Diensten | 1,2 |
| 2.3 | Switching und VLANs: Broadcast-Domänen, Trunks, Segmentierung von Clients, Servern und VoIP | 1,1 |
| 2.4 | Routing und Default Gateway: Wege zwischen Netzen, Standardfehler | 1,1 |
| 2.5 | WLAN-Grundlagen: SSID, Sicherheit und Roaming, typische Störfelder in Büros | 1,1 |
| 2.6 | Firewall-Basis und NAT: Regelwerke, Ports und NAT, kontrollierte Freigaben | 1,1 |
| 2.7 | Netzwerkdokumentation: IP-Plan, Portplan und Systemübersichten | 1,1 |
| 2.8 | Basis-Monitoring und Fehlerbilder: Latenz, Paketverlust, Gateway-Fehler systematisch prüfen, Frühwarnsignale | 1,1 |

#### Praxisaufgaben (Hands-on Lab)
Vor Beginn: Das Labor besteht noch nicht. Der Aufbau (Aufgabe 3) ist die Grundlage für alle weiteren Module. Die Installation der Betriebssysteme folgt den Standardassistenten und ist nicht Lernstoff dieses Moduls (Vorbereitungszeit außerhalb der UE, Annahme).

1. **Subnetze berechnen (Lernziel 1; Einheit 2.2):** Teile `192.168.50.0/24` in vier gleich große Subnetze. Gib für jedes Netz Netz-ID, Präfixlänge, Hostbereich, Broadcast-Adresse und Anzahl nutzbarer Hosts an. Bestimme außerdem Netz-ID und Broadcast-Adresse von `192.168.60.101/24` und begründe, ob `192.168.50.20` und `192.168.60.101` im selben Netz liegen. Nenne die Berechnungsformel für die Hostanzahl.
2. **Symptome den Schichten zuordnen (Lernziel 1; Einheit 2.1):** Ordne diese Symptome der wahrscheinlichsten Schicht des TCP/IP-Modells zu und nenne je ein Prüfwerkzeug: (a) Netzwerkkabel getrennt, (b) falsche Subnetzmaske, (c) Name wird nicht aufgelöst, (d) TCP-Port ist gesperrt, (e) Gateway falsch, (f) Anwendung meldet einen Anmeldefehler.
3. **Labornetz aufbauen und dokumentieren (Lernziel 2; Einheiten 2.4, 2.7):**
   1. Switches anlegen (`New-VMSwitch`, nicht bestätigt):
      ```powershell
      New-VMSwitch -Name sw-lab-srv -SwitchType Private
      New-VMSwitch -Name sw-lab-cli -SwitchType Private
      ```
   2. VMs `SRV-DC01`, `SRV-FS01`, `CL-W11-01` nach A.3 anlegen und Betriebssysteme installieren. Für `SRV-FS01` weitere Adapter hinzufügen (`Add-VMNetworkAdapter -VMName SRV-FS01 -Name NIC-CLI -SwitchName sw-lab-cli`, nicht bestätigt) und `NIC-INET` ohne Switch-Verbindung anlegen; `CL-W11-01` bekommt ebenfalls einen nicht verbundenen `NIC-INET`.
   3. Adapter im Gast eindeutig benennen (Namen: `NIC-LAB` auf `SRV-DC01`, `NIC-LAB`/`NIC-CLI`/`NIC-INET` auf `SRV-FS01`, `NIC-CLI` auf `CL-W11-01`): MAC-Adressen auf dem Host (`Get-VMNetworkAdapter -VMName SRV-FS01 | Select-Object Name, MacAddress`) mit `Get-NetAdapter | Select-Object Name, MacAddress` im Gast abgleichen und mit `Rename-NetAdapter` umbenennen (nicht bestätigt).
   4. Adressen setzen (`New-NetIPAddress`, nicht bestätigt) nach dem Plan in A.3. Auf `SRV-DC01` keine Gateway-Adresse, sondern die Route: `New-NetRoute -DestinationPrefix 192.168.60.0/24 -InterfaceAlias NIC-LAB -NextHop 192.168.50.20` (nicht bestätigt).
   5. Auf `SRV-FS01` Weiterleitung auf beiden Labor-Adaptern aktivieren: `Set-NetIPInterface -InterfaceAlias NIC-LAB -Forwarding Enabled`, ebenso `NIC-CLI`.
   6. Auf allen drei VMs eine eigene Regel anlegen, die Ping erlaubt (`New-NetFirewallRule -DisplayName "LAB-ICMPv4-In" -Direction Inbound -Protocol ICMPv4 -IcmpType 8 -Action Allow`, nicht bestätigt). Prüfe, ob bereits vorhandene Echo-Regeln aktiv sind (Namen nicht bestätigt) und notiere es.
   7. Teste von `CL-W11-01` aus nacheinander `Test-NetConnection 192.168.60.1`, `Test-NetConnection 192.168.50.20` und `Test-NetConnection 192.168.50.10` (alle drei sollen erreichbar sein).
   8. Lege eine Datei `netzplan.md` an mit IP-Plan (Gerät, Adapter, Adresse, Netz, Gateway/Route, Rolle), Portplan (die in Aufgabe 6 geöffneten Ports) und einer Textskizze der Topologie. Nimm je VM den Prüfpunkt `<VM>-M2-Ende` bei ausgeschalteter VM.
4. **Fehler eingrenzen (Lernziel 3; Einheiten 2.4, 2.8):** Der Kursleiter baut drei Fehler ein (Vorschlag in C, nicht getestet): falsches Standardgateway auf `CL-W11-01`, deaktivierte Weiterleitung auf `SRV-FS01`, deaktivierte Ping-Regel auf `SRV-DC01`. Gehe in dieser festen Reihenfolge vor: (1) eigene Adresse und Maske (`Get-NetIPAddress`), (2) Gateway erreichbar, (3) nächstes Netz erreichbar, (4) Ziel erreichbar, (5) Zielport. Nutze `Test-NetConnection`, `Get-NetRoute` und `Get-NetIPInterface`. Notiere pro Fehler: Symptom, Hypothese, Test, Ursache, Behebung. Messe danach die Latenz zu `SRV-DC01` mit `Test-Connection -ComputerName 192.168.50.10 -Count 20` (Mittelwert, Höchstwert, Verlust) und halte die Werte als Baseline fest.
5. **VLAN-Demonstration (Lernziel 1; Einheit 2.3):** Setze die Adapter `NIC-LAB` von `SRV-DC01` und `SRV-FS01` auf unterschiedliche VLANs (`Set-VMNetworkAdapterVlan -VMName SRV-DC01 -VMNetworkAdapterName NIC-LAB -Access -VlanId 10`; `-VlanId 20` für `SRV-FS01`; der Parameter `-VMNetworkAdapterName` ist nicht bestätigt). Teste Ping zwischen beiden, setze danach beide auf `-VlanId 10` und teste erneut. **Rückbau:** `Set-VMNetworkAdapterVlan -VMName <VM> -VMNetworkAdapterName NIC-LAB -Untagged` für beide VMs. Ob ein privater Switch die VLAN-Trennung wie erwartet zeigt, ist nicht bestätigt; weicht das Ergebnis ab, dokumentiere es und erkläre mögliche Ursachen.
6. **Port freigeben und prüfen (Lernziel 2; Einheit 2.6):** Starte auf `SRV-DC01` in einem PowerShell-Fenster einen Listener:
   ```powershell
   $l = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, 8080)
   $l.Start()
   ```
   Teste von `CL-W11-01`: `Test-NetConnection 192.168.50.10 -Port 8080` (soll scheitern). Lege auf `SRV-DC01` eine Regel an (`New-NetFirewallRule -DisplayName "LAB-TCP8080-In" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow`, nicht bestätigt), teste erneut (soll gelingen). **Rückbau:** `$l.Stop()` und `Remove-NetFirewallRule -DisplayName "LAB-TCP8080-In"`. Zeichne danach, was NAT macht: ein Client im privaten Netz, ein Router mit einer öffentlichen Adresse (Platzhalter ÖFF) und ein Server im Internet; beschrifte, welche Quelladresse der Server sieht.
7. **WLAN-Fallstudie (Lernziel 1; Einheit 2.5):** In einem Büro mit 30 Personen melden Nutzer Verbindungsabbrüche beim Gehen durch das Gebäude, langsames WLAN in Besprechungsräumen und ein gemeinsames Kennwort für alle. Nenne mindestens drei Ursachenhypothesen mit je einer Prüfmethode, drei Maßnahmen und ein Risiko des gemeinsamen Kennworts. Technische Detailwerte (Kanalbreiten, Sendeleistung) sind nicht gefordert.

#### Kontrollfragen
1. Auf welcher Schicht arbeitet ein Switch, auf welcher ein Router, und woran erkennst du das an einer Fehlermeldung?
2. Wie viele nutzbare Hosts hat ein `/26`-Netz, und wie lautet die Formel?
3. Warum braucht `SRV-DC01` eine statische Route in das Clientnetz, obwohl es kein Standardgateway hat?
4. Was trennt ein VLAN, und was bleibt ohne Router getrennt?
5. Was leistet NAT, und warum ist NAT kein Ersatz für eine Firewall?

---

### Modul 3: Windows Server, Active Directory und Hybrid Identity
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rollen DNS, AD DS und Dateidienst einordnen und eine AD-Domäne mit OU-Struktur, Konten und Gruppen aufbauen.
  * Nach Abschluss dieses Moduls kann der Lernende Gruppenrichtlinien erstellen und verknüpfen sowie Dateifreigaben mit NTFS- und Freigaberechten nach AGDLP einrichten und testen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Patch-Vorgang mit Wartungsfenster und Rückfallplan planen, Hybrid Identity (Kennwort-Hashsynchronisierung) einordnen und typische Domänenfehler (DNS, Gruppenrichtlinie, Berechtigung) systematisch eingrenzen.
* **Voraussetzungen:** Modul 2 (Labor im Zustand `<VM>-M2-Ende`).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Windows-Server-Rollen: DNS, DHCP, File und Print einordnen, Abhängigkeiten im Betrieb | 1,3 |
| 3.2 | Active Directory Domain Services: Objektlogik, OU-Struktur, Verwaltungsmodell, Standardfehler bei Organisation und Delegation | 1,3 |
| 3.3 | DNS und Namensauflösung: AD-nahe DNS-Funktion und Störbilder | 1,3 |
| 3.4 | Gruppenrichtlinien: GPO-Struktur, Scope und Wirklogik | 1,3 |
| 3.5 | Dateidienste und Berechtigungen: NTFS- und Freigaberechte, Least Privilege | 1,2 |
| 3.6 | Patch- und Serverbetrieb: Wartungsfenster, Rollback, Basis-Hardening | 1,2 |
| 3.7 | Hybrid Identity mit Entra ID: Synchronisation, Anmeldemodelle, Rollenlogik im Grundsatz | 1,2 |
| 3.8 | Troubleshooting in Windows-Umgebungen: Login-, DNS-, Replikations- und Richtlinienfehler | 1,2 |

#### Praxisaufgaben (Hands-on Lab)
Vor Beginn: `SRV-DC01` ausschalten und Prüfpunkt `SRV-DC01-M3-Start` erzeugen (Standard-Checkpoints bei Active Directory nur bei ausgeschalteter VM, siehe A.3). Ein Zurücksetzen von `SRV-DC01` nach der Heraufstufung gilt nur gemeinsam für das ganze Labor. Folgende AD-Cmdlets sind nicht bestätigt: `New-ADOrganizationalUnit`, `New-ADUser`, `New-ADGroup`, `Add-ADGroupMember`, `New-GPO`, `New-GPLink`.

1. **Rollen einordnen (Lernziel 1; Einheit 3.1):** Liste auf `SRV-DC01` und `SRV-FS01` die installierten Rollen und Features (`Get-WindowsFeature | Where-Object Installed`). Erstelle eine Tabelle: Rolle, Zweck, Abhängigkeit (z. B. „AD DS benötigt DNS“), Auswirkung eines Ausfalls. DHCP ist in diesem Lehrplan nur Theorie; beantworte schriftlich, was bei Ausfall eines DHCP-Servers mit bereits verbundenen Clients passiert (Begründung, ohne Praxistest).
2. **Domäne aufbauen (Lernziel 1; Einheit 3.2):**
   1. Auf `SRV-DC01`: `Install-WindowsFeature AD-Domain-Services -IncludeManagementTools`, danach `Install-ADDSForest -DomainName lab.example.internal -DomainNetbiosName LAB -InstallDns`. Das Wiederherstellungskennwort (DSRM) wird interaktiv abgefragt und nicht notiert.
   2. Nach dem Neustart den DNS-Client von `SRV-DC01` auf sich selbst stellen: `Set-DnsClientServerAddress -InterfaceAlias NIC-LAB -ServerAddresses 192.168.50.10` (nicht bestätigt).
   3. OU-Struktur `LAB` mit den Unter-OUs `Benutzer`, `Gruppen`, `Computer` und `Admin` anlegen.
   4. Konten anlegen, Kennwörter interaktiv (`-AccountPassword (Read-Host -AsSecureString "Kennwort")`): `lab-user01` (Standardbenutzer, OU `Benutzer`), `lab-adm01` (Mitglied von `Domain Admins`, OU `Admin`), `lab-hd01` (Helpdesk, OU `Benutzer`), Gruppe `grp-helpdesk` (OU `Gruppen`).
   5. Notiere, warum `lab-adm01` nur für Verwaltungsaufgaben verwendet wird und nicht für die tägliche Arbeit.
3. **Mitglieder aufnehmen (Lernziel 1; Einheit 3.3):** Stelle DNS auf `SRV-FS01` und `CL-W11-01` auf `192.168.50.10` (`Set-DnsClientServerAddress`). Prüfe die Auflösung mit `nslookup srv-dc01.lab.example.internal` und der SRV-Abfrage `nslookup -type=SRV _ldap._tcp.dc._msdcs.lab.example.internal 192.168.50.10`. Nimm beide Computer in die Domäne auf: `Add-Computer -DomainName lab.example.internal -Credential LAB\lab-adm01 -Restart` (Kennwort wird abgefragt). Verschiebe die Computerkonten in die OU `Computer`. Erkläre, warum der Beitritt von `CL-W11-01` über das geroutete Netz funktioniert.
4. **Gruppenrichtlinie (Lernziel 2; Einheit 3.4):** Lege `GPO-Lab-Client` an, verknüpft mit der OU `Computer`, mit der Einstellung „Interaktive Anmeldung: Nachrichtentext für Benutzer, die sich anmelden“ (Computerkonfiguration, Windows-Einstellungen, Sicherheitseinstellungen, Lokale Richtlinien, Sicherheitsoptionen). Aktualisiere auf dem Client (`gpupdate /force`), melde dich ab und prüfe die Anzeige. Lege eine Unter-OU `Computer\Test` an, verschiebe `CL-W11-01` dorthin, verknüpfe `GPO-Lab-Client-2` mit einem anderen Text und bestimme mit `gpresult /r`, welcher Text gewinnt (Learn: Reihenfolge lokal, Standort, Domäne, OU; die näher am Objekt liegende OU überschreibt). **Rückbau:** Verknüpfungen entfernen und Computer in die OU `Computer` zurückschieben.
5. **Dateiserver mit AGDLP (Lernziel 2; Einheit 3.5):**
   1. **Vorbedingung für Datenträgerbefehle:** `SRV-FS01` ist gesichert (Prüfpunkt bei ausgeschalteter VM). Eine neue leere virtuelle Festplatte (20 GB) anhängen. Führe zuerst `Get-Disk` aus und fahre nur fort, wenn der neue Datenträger `PartitionStyle` = `RAW` hat und die Größe 20 GB beträgt.
   2. Initialisieren, partitionieren, formatieren als `E:` (`Initialize-Disk`, `New-Partition -DriveLetter E -UseMaximumSize`, `Format-Volume`, nicht bestätigt).
   3. Ordner `E:\Daten\Projekt` und Freigabe `Daten`. Gruppen: `grp-projekt` (global, Mitglied `lab-user01`), `dl-projekt-rw` (domänenlokal, Mitglied `grp-projekt`). NTFS: `dl-projekt-rw` Ändern; Freigabeberechtigung: `dl-projekt-rw` Ändern; keine Berechtigung für `Jeder`.
   4. Teste von `CL-W11-01` mit `lab-user01` (Zugriff) und `lab-hd01` (Zugriff verweigert) mit `net use`; füge `lab-hd01` testweise zu `grp-projekt` hinzu und melde dich neu an (Zugriffstoken wird bei der Anmeldung erstellt). Notiere, welche Berechtigung (Freigabe oder NTFS) im Ergebnis gilt.
6. **Patch-Vorgang planen und durchführen (Lernziel 3; Einheit 3.6):** Schreibe einen Wartungsplan (eine Seite): Zeitfenster, betroffene Systeme, Vorab-Sicherung, Prüfschritte nach dem Update, Rückfallplan. Führe den Plan auf `SRV-FS01` in Internetphase I-2 aus: `SRV-FS01` ausschalten, Prüfpunkt `SRV-FS01-M3-Pre-Update`, Labor-Adapter trennen, `NIC-INET` mit dem `Default Switch` verbinden (der DNS-Server kommt aus der DHCP-Zuweisung des Switches), Updates über die Einstellungen installieren, Neustart, KB-Nummern notieren, Phase beenden (Adapter zurücktauschen). `SRV-DC01` bekommt kein Internet und wird nicht gepatcht; dokumentiere diese Entscheidung als Risiko. **Hinweis:** Ein Zurücksetzen eines Domänenmitglieds auf einen älteren Prüfpunkt kann zu abweichendem Kennwort des Computerkontos führen (nicht bestätigt); das Zurücksetzen ist deshalb nur sofort nach dem Update sinnvoll, später gilt die Deinstallation des Updates (`wusa /uninstall /kb:<Nummer>`, nicht bestätigt).
7. **Hybrid Identity bewerten (Lernziel 3; Einheit 3.7):** Papierübung. Ein Betrieb mit 80 Mitarbeitenden hat ein lokales AD und möchte Microsoft-Cloud-Dienste nutzen. Beschreibe, was die Kennwort-Hashsynchronisierung (Learn: Entra Connect) leistet, nenne zwei Voraussetzungen und ein Risiko. Prüfe außerdem, warum der Domänenname `lab.example.internal` des Labors nicht als eigene Domäne in einem Entra-Mandanten verifiziert werden kann (nicht bestätigt: nicht routbare Domänen werden nicht akzeptiert). Weitere Anmeldemodelle sind nicht geprüft und nur in einem Satz zu benennen.
8. **Fehlerbilder eingrenzen (Lernziel 3; Einheit 3.8):** Der Kursleiter baut drei Fehler ein (Vorschlag in C): (a) `CL-W11-01` hat einen falschen DNS-Server, (b) `GPO-Lab-Client` ist mit der falschen OU verknüpft, (c) `lab-user01` fehlt in `grp-projekt`. Analysiere mit `nslookup`, `gpresult /r`, `Get-ADPrincipalGroupMembership` (nicht bestätigt) und dem Ereignisprotokoll. Dokumentiere pro Fehler den Fehlerpfad: Symptom, Hypothese, Prüfschritt, Ursache, Behebung.

#### Kontrollfragen
1. Warum benötigt Active Directory einen funktionierenden DNS-Server, und woran erkennst du einen DNS-Fehler beim Domänenbeitritt?
2. In welcher Reihenfolge werden Gruppenrichtlinien verarbeitet, und welche gewinnt bei Konflikt?
3. Was bedeutet AGDLP, und warum werden Rechte nicht direkt Benutzern zugewiesen?
4. Welche Berechtigung gilt, wenn Freigabe „Lesen“ und NTFS „Ändern“ vergeben sind?
5. Welche Risiken entstehen, wenn ein Domänencontroller ohne Updates dauerhaft läuft?

---

### Modul 4: Modern Workplace, Microsoft 365 und Endpoint Management
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Dienste Entra ID, Intune, Exchange Online, Teams und SharePoint einordnen und klassische Verwaltung (Gruppenrichtlinie) von cloudbasierter Verwaltung (Intune) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende in einem Testmandanten ein Gerät per Entra Join registrieren, ein Konfigurationsprofil, eine App und eine Compliance-Richtlinie zuweisen und den Status prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Conditional Access sicher planen (Nur-Bericht-Modus, Notfallkonto), BitLocker per Richtlinie aktivieren und typische Enrollment-, Richtlinien- und Lizenzfehler eingrenzen.
* **Voraussetzungen:** Modul 2 (Windows-11-Image, Hyper-V-Grundlagen) und Modul 3 (Begriff Gruppenrichtlinie). Ab hier wird ein Cloud-Testzugang benötigt (A.3).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Microsoft-365-Dienste im Überblick: Exchange Online, Teams, SharePoint, Entra ID, Zusammenspiel im Arbeitsplatz | 1,3 |
| 4.2 | Windows-Clientbetrieb modern: Client-Lifecycle, Standardisierung, Deployment-Grundlogik | 1,3 |
| 4.3 | Microsoft-Intune-Grundlagen: Geräteregistrierung, Richtlinien und App-Rollout | 1,3 |
| 4.4 | Entra Join und Identität am Arbeitsplatz: Geräte- und Benutzeridentität in Cloud-first-Szenarien | 1,3 |
| 4.5 | Compliance und Conditional Access Basis: Gerätezustand und Zugriffsregeln | 1,2 |
| 4.6 | App-Bereitstellung und Konfiguration: Standardsoftware, Richtlinien und Profile reproduzierbar verteilen | 1,2 |
| 4.7 | Endpoint-Security-Grundlagen: BitLocker, Defender, Basishardening am Client | 1,2 |
| 4.8 | Troubleshooting im Workplace: Enrollment-, Policy-, Sync- und Lizenzprobleme | 1,2 |

#### Praxisaufgaben (Hands-on Lab)
**Kostenhinweis:** Der Intune-Testmandant ist eine Ausnahme vom isolierten Labor (Dauer 30 Tage, Kosten 0 EUR, solange nichts dazugebucht wird). Die Lernenden stimmen der Registrierung mit eigener Zahlungskarte (nur zur Überprüfung) ausdrücklich zu; ein produktiver Mandant wird nie verwendet. Starte den Testzugang erst zu Beginn dieses Moduls. Benennungen im Portal können sich ändern; Menüpfade sind nicht bestätigt.

1. **Dienste einordnen (Lernziel 1; Einheit 4.1):** Erstelle eine Tabelle mit Exchange Online, Teams, SharePoint, Entra ID und Intune: Aufgabe, benötigt Identität aus, typische Verwaltungsaufgaben. Ordne in der Fallstudie „Neue Mitarbeiterin“ (Konto, Postfach, Teamzugang, Laptop, Datenablage) jeden Schritt einem Dienst zu. Der Lizenzbedarf je Dienst ist auf der Microsoft-Lizenzseite nachzulesen (nicht geprüft). Exchange, Teams und SharePoint haben in diesem Lehrplan keine Praxisübung.
2. **Verwaltungsmodelle vergleichen (Lernziel 1; Einheit 4.2):** Vergleiche Gruppenrichtlinie (Modul 3) und Intune in einer Tabelle: Voraussetzung, Zielobjekt, Verteilweg, Verhalten ohne Verbindung (nicht bestätigt), Prüfwerkzeug. Beschreibe den Lebenszyklus von `CL-W11-02` von der Bereitstellung bis zur Außerbetriebnahme in vier Schritten.
3. **Testmandant und Gerät einrichten (Lernziel 2; Einheiten 4.3, 4.4):**
   1. Mandant nach Learn „Intune free trial“ einrichten; Administratorkonto `adm-lab01`, Notfallkonto `bg-lab01` (Kennwörter in einem Kennwortmanager, nicht im Dokument), Testbenutzer `user.cloud01`, `user.cloud02`, Gruppe `grp-cloud-test` (beide Benutzer).
   2. Einem weiteren Konto eine Intune-Rolle mit eingeschränkten Rechten zuweisen (eingebaute Rolle; Name im Portal prüfen, nicht bestätigt) und begründen, warum nicht Globaler Administrator.
   3. VM `CL-W11-02` mit vTPM anlegen (`Set-VMKeyProtector -VMName CL-W11-02 -NewLocalKeyProtector`, dann `Enable-VMTPM -VMName CL-W11-02`), nur mit `Default Switch` verbinden und Windows 11 installieren; bei der Ersteinrichtung mit `user.cloud01` anmelden (Entra Join; Menüführung nicht bestätigt).
   4. Auf `CL-W11-02`: `dsregcmd /status` ausführen und Werte `AzureAdJoined` (soll `YES`) und `DomainJoined` (soll `NO`) notieren (Learn). Prüfe, ob das Gerät in Entra und in Intune erscheint. Wird es nicht automatisch in Intune aufgenommen, melde es manuell an (Einstellungen, Konten, Zugriff auf Arbeits- oder Schulkonto; nicht bestätigt).
4. **Profil und App verteilen (Lernziel 2; Einheit 4.6):** Erstelle ein Konfigurationsprofil mit einer eindeutig prüfbaren Einstellung (im Einstellungskatalog suchen; konkrete Einstellung nicht bestätigt) und weise es `grp-cloud-test` zu. Verteile eine freie App aus dem Store-Katalog (z. B. 7-Zip, Verfügbarkeit nicht bestätigt) als „erforderlich“. Löse auf dem Gerät eine Synchronisierung aus, prüfe Installation und Einstellung und halte die Zeitspanne bis zur Wirkung fest.
5. **Compliance und Conditional Access (Lernziel 3; Einheit 4.5):** Erstelle eine Compliance-Richtlinie für Windows (z. B. BitLocker erforderlich, Echtzeitschutz erforderlich; Auswahl der Einstellungen im Portal) für `grp-cloud-test` (Learn: Bewertung beim Check-in des Geräts). Lege dann eine Conditional-Access-Richtlinie „kompatibles Gerät erforderlich“ **im Nur-Bericht-Modus** an (Learn), nur für `grp-cloud-test`, **ohne** das Notfallkonto `bg-lab01` (ausgeschlossen, Learn: Notfallzugriffskonten). Lies im Anmeldeprotokoll, was die Richtlinie ergeben hätte. **Vor jeder Umstellung auf „Ein“:** Melde dich mit `bg-lab01` an und dokumentiere, dass das Konto funktioniert. Die Umstellung auf „Ein“ ist optional und nur für `grp-cloud-test` erlaubt.
6. **BitLocker per Richtlinie (Lernziel 3; Einheit 4.7):** Erzeuge einen Prüfpunkt `CL-W11-02-M4-Pre-BitLocker`. Lege eine Endpoint-Security-Richtlinie für Datenträgerverschlüsselung an, mit der Einstellung, dass die Wiederherstellungsinformation in Entra gesichert sein muss, bevor BitLocker aktiviert wird (Learn). Prüfe auf dem Gerät `manage-bde -status C:` (Ausgabefelder nicht bestätigt) und rufe den Wiederherstellungsschlüssel in Entra oder Intune ab (Learn: dazu ist eine Rolle wie Cloud Device Administrator oder Helpdesk Administrator nötig). Prüfe den Defender-Status mit `Get-MpComputerStatus` (nicht bestätigt) auf `RealTimeProtectionEnabled`.
7. **Fehlerbilder eingrenzen (Lernziel 3; Einheit 4.8):** Der Kursleiter bzw. ein Partner baut drei Fehler ein: (a) `user.cloud02` hat keine passende Lizenz, (b) `user.cloud02` ist nicht in `grp-cloud-test`, (c) ein Profil wurde geändert, ist aber auf dem Gerät nicht sichtbar. Analysiere im Portal (Gerätestatus, Zuweisungen, Anmeldeprotokoll) und löse die Synchronisierung manuell aus. Dokumentiere Symptom, Hypothese, Prüfpfad, Ursache und Behebung je Fehler.
8. **Rückbau (alle Lernziele):** Conditional-Access-Richtlinie löschen, Compliance- und Konfigurationsrichtlinien löschen, Testbenutzer und Gruppe löschen, Gerät aus Intune/Entra entfernen. **Hinweis (Learn):** Das Löschen des Intune-Objekts eines Entra-gejointen Geräts mit BitLocker lässt BitLocker auf dem Systemvolume im Zustand „suspendiert“; sichere deshalb den Wiederherstellungsschlüssel vorher oder verwirf die VM danach. Prüfe unter Abrechnung/Abonnements, ob eine automatische Verlängerung oder ein bezahltes Abonnement aktiv ist (Menüpfad nicht bestätigt) und kündige, falls nötig.

#### Kontrollfragen
1. Wofür ist Entra ID zuständig, und wofür Intune?
2. Was zeigt `dsregcmd /status` bei einem rein cloudverbundenen Gerät in den Feldern `AzureAdJoined` und `DomainJoined`?
3. Warum wird eine neue Conditional-Access-Richtlinie zuerst im Nur-Bericht-Modus betrieben, und wozu dient das Notfallkonto?
4. Was passiert mit der BitLocker-Verschlüsselung, wenn das Intune-Objekt eines Geräts gelöscht wird, und wie schützt man sich?
5. Nenne drei Ursachen, warum eine zugewiesene Richtlinie auf einem Gerät nicht ankommt, und den jeweiligen Prüfschritt.

---

### Modul 5: Linux-Server, Open-Source-Dienste und Plattformbetrieb
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Linux-Server-Distributionen und Paketverwaltung funktional unterscheiden und einen Ubuntu-Server mit statischer Adresse, Route und DNS (netplan) in das Labornetz einbinden.
  * Nach Abschluss dieses Moduls kann der Lernende Benutzer, Gruppen, Rechte und sudo einrichten sowie Systemdienste mit systemd anlegen, starten und bei Fehlern analysieren.
  * Nach Abschluss dieses Moduls kann der Lernende den SSH-Zugang auf Schlüssel umstellen, eine Firewall (ufw) sicher aktivieren und Protokolle (journalctl) zur Diagnose nutzen.
* **Voraussetzungen:** Modul 2 (Labor, Routing über `SRV-FS01`) und Modul 3 (DNS-Server `SRV-DC01`, Domäne). Dieses Modul nutzt Internetphase I-3.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Linux-Distributionen und Rollen: Server-Distributionen unterscheiden, Einsatzfelder in Unternehmen und Cloud | 1,2 |
| 5.2 | Shell und Grundbefehle: Dateisystem, Prozesse, Basisadministration | 1,2 |
| 5.3 | Benutzer, Gruppen und Rechte: Rechtekonzept, sudo-Logik | 1,1 |
| 5.4 | Paketmanagement und Repositorys: reproduzierbare Softwarepflege, Versions- und Abhängigkeitsprobleme | 1,1 |
| 5.5 | Systemdienste und Daemons: Service-Management mit systemd, Start-, Stop- und Fehlerlogik | 1,1 |
| 5.6 | Netzwerk und SSH: Adressierung, DNS, SSH-Zugriff, Basissicherheit, Remote-Betrieb | 1,1 |
| 5.7 | Logging und Diagnose: Journal, Logdateien, Prozessbeobachtung | 1,1 |
| 5.8 | Linux-Hardening Basis: Updates, sichere Defaults, minimale Angriffsoberfläche | 1,1 |

#### Praxisaufgaben (Hands-on Lab)
Alle Linux-Befehle in diesem Modul stammen aus dem Gedächtnis und sind nicht bestätigt; die Netplan-Syntax ist gegen die Netplan-Referenz zu prüfen (A.2). Sichere Zustände: Prüfpunkt `LX-UBU01-M5-Start` direkt nach der Installation (VM ausgeschaltet).

1. **Distributionen vergleichen (Lernziel 1; Einheit 5.1):** Vergleiche Ubuntu Server (LTS), eine Debian-basierte und eine Red-Hat-basierte Distribution in einer Tabelle: Paketformat/-werkzeug, Veröffentlichungsrhythmus, Supportzeitraum, typischer Einsatz. Entnimm die Angaben den offiziellen Seiten der Hersteller (URL und Abrufdatum angeben); nicht auffindbare Angaben markierst du mit „nicht geprüft“.
2. **Server installieren und einbinden (Lernziel 1; Einheiten 5.4, 5.6):**
   1. VM `LX-UBU01` mit Secure-Boot-Vorlage anlegen: `Set-VMFirmware -VMName LX-UBU01 -SecureBootTemplate MicrosoftUEFICertificateAuthority` (Learn). Zwei Adapter: `NIC-LAB` (`sw-lab-srv`) und `NIC-INET`.
   2. **Internetphase I-3:** `NIC-LAB` trennen, `NIC-INET` mit `Default Switch` verbinden, Ubuntu Server 24.04 LTS installieren (Benutzer `labadmin`, Kennwort wird beim Installieren eingegeben), danach `sudo apt update` und `sudo apt upgrade`. Prüfe, ob `ufw`, `unattended-upgrades` und `openssh-server` installiert sind (`dpkg -l | grep -E "ufw|unattended-upgrades|openssh-server"`; Vorinstallation nicht bestätigt). Phase beenden: `NIC-INET` trennen, `NIC-LAB` verbinden.
   3. Adressen per netplan setzen. Sichere die vom Installer erzeugte Datei (`sudo cp /etc/netplan/<Datei>.yaml ~/netplan-backup.yaml`) und ersetze deren Inhalt (Schnittstellen über ihre MAC-Adresse zuordnen, `ip -br link` zeigt die Adressen; MAC-Werte sind Platzhalter):
      ```yaml
      network:
        version: 2
        ethernets:
          lab0:
            match:
              macaddress: "00:15:5d:00:00:01"
            set-name: lab0
            addresses: [192.168.50.30/24]
            routes:
              - to: 192.168.60.0/24
                via: 192.168.50.20
            nameservers:
              addresses: [192.168.50.10]
          inet0:
            match:
              macaddress: "00:15:5d:00:00:02"
            set-name: inet0
            dhcp4: true
            optional: true
      ```
      Anwenden mit `sudo netplan try` (nicht bestätigt: automatische Rücknahme nach Zeitablauf). **Rückbau:** Sicherungsdatei zurückkopieren und `sudo netplan apply`.
   4. Teste: Ping zu `192.168.50.10` und `192.168.60.101`, Namensauflösung `getent hosts srv-dc01.lab.example.internal`, und von `CL-W11-01` aus Ping zu `192.168.50.30` (die Ping-Regel von Modul 2 gilt nur für Windows; Linux antwortet standardmäßig, nicht bestätigt).
3. **Shell, Benutzer und Rechte (Lernziel 2; Einheiten 5.2, 5.3):** Lege `/srv/lab/shared` an, erstelle Gruppe `labgrp` und Benutzer `labuser01` (`sudo adduser labuser01`, Kennwort interaktiv), füge `labuser01` zu `labgrp` hinzu, setze `sudo chgrp labgrp /srv/lab/shared` und `sudo chmod 2770 /srv/lab/shared`. Lege als `labuser01` eine Datei an und prüfe mit `ls -l`, dass die Gruppe `labgrp` übernommen wird. Prüfe mit einem Benutzer ohne Gruppenmitgliedschaft, dass der Zugriff verweigert wird. Nutze `ps aux`, `top` und `find` und erkläre drei Spalten der Ausgabe. Zeige mit `sudo -l -U labuser01`, dass `labuser01` kein sudo-Recht hat.
4. **Pakete (Lernziel 1; Einheit 5.4):** Installiere ein kleines Paket (z. B. `tree`) mit `sudo apt install tree`, simuliere vorher mit `apt install -s tree`, zeige Version und Quelle (`apt policy tree`), fixiere es mit `sudo apt-mark hold tree` und hebe die Fixierung wieder auf (`sudo apt-mark unhold tree`). Entferne das Paket (`sudo apt remove tree`). Beschreibe, wofür die Fixierung nützlich ist und welches Risiko sie hat.
5. **Eigener Dienst (Lernziel 2; Einheit 5.5):** Lege ein Skript `/usr/local/bin/lab-hello.sh` an (`#!/bin/bash`, Schleife mit `echo "lab-hello $(date)"` und `sleep 30`, ausführbar) und eine Unit `/etc/systemd/system/lab-hello.service` mit `[Service]`, `ExecStart=/usr/local/bin/lab-hello.sh`, `Restart=on-failure`, `[Install]`, `WantedBy=multi-user.target`. Danach `sudo systemctl daemon-reload`, `sudo systemctl start lab-hello`, `systemctl status lab-hello`, Ausgabe im Journal prüfen. Ändere dann absichtlich den Pfad in `ExecStart` auf `/usr/local/bin/lab-hallo.sh`, lade neu, starte den Dienst und analysiere den Fehler mit `systemctl status` und `journalctl -u lab-hello -e`. Korrigiere. **Rückbau:** `sudo systemctl disable --now lab-hello`, Unit und Skript löschen (nur die beiden genannten Dateien), `sudo systemctl daemon-reload`.
6. **SSH mit Schlüssel (Lernziel 3; Einheit 5.6):**
   1. Auf `CL-W11-01`: `ssh -V` prüfen. Fehlt der OpenSSH-Client (Standardlieferung nicht bestätigt), in Phase I-3 über „Optionale Features“ nachinstallieren.
   2. Schlüsselpaar erzeugen: `ssh-keygen -t ed25519` (Passphrase interaktiv). Öffentlichen Schlüssel übertragen: `scp $env:USERPROFILE\.ssh\id_ed25519.pub labadmin@192.168.50.30:/home/labadmin/`.
   3. Auf `LX-UBU01`: Schlüssel in `~/.ssh/authorized_keys` eintragen, Rechte `chmod 700 ~/.ssh` und `chmod 600 ~/.ssh/authorized_keys`.
   4. **Vor dem Abschalten der Kennwortanmeldung:** Schlüsselanmeldung in einer zweiten Sitzung erfolgreich testen und die erste Sitzung offen lassen. Dann `PasswordAuthentication no` setzen (Datei `/etc/ssh/sshd_config` oder ein Eintrag unter `/etc/ssh/sshd_config.d/`; Vorrangregel nicht bestätigt), prüfen mit `sudo sshd -t` und die wirksame Einstellung mit `sudo sshd -T | grep -i passwordauthentication`, dann `sudo systemctl reload ssh` (Dienstname nicht bestätigt). Teste eine neue Verbindung. **Rückbau:** Über die Hyper-V-Konsole (nicht über SSH) die Einstellung auf `yes` zurücksetzen, falls der Zugang verloren geht.
7. **Protokolle auswerten (Lernziel 3; Einheit 5.7):** Löse von `CL-W11-01` einen fehlgeschlagenen Anmeldeversuch aus (falscher Benutzername) und finde ihn mit `journalctl -u ssh --since "10 min ago"` (Unit-Name nicht bestätigt). Zeige mit `journalctl -p err -b` die Fehler seit dem Start. Prüfe, ob `/var/log/auth.log` existiert (nicht bestätigt) und vergleiche. Notiere Zeit, Quelladresse und Benutzername des fehlgeschlagenen Versuchs.
8. **Härten (Lernziel 3; Einheit 5.8):** Zeige offene Ports mit `ss -tulpn` und dokumentiere jeden Eintrag (Dienst, Zweck, nötig ja/nein). Firewall **nur mit zweiter offener SSH-Sitzung** aktivieren:
   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   sudo ufw allow from 192.168.50.0/24 to any port 22 proto tcp
   sudo ufw allow from 192.168.60.0/24 to any port 22 proto tcp
   sudo ufw enable
   ```
   Beide Netze sind nötig: `SRV-FS01` routet ohne NAT, daher bleibt die Quelladresse von `CL-W11-01` `192.168.60.x`. Teste die Verbindung von `CL-W11-01`. Prüfe `sudo sshd -T | grep -iE "permitrootlogin|passwordauthentication"`. **Rückbau:** `sudo ufw disable` (über die Hyper-V-Konsole, falls der Zugang verloren geht). Erzeuge am Ende den Prüfpunkt `LX-UBU01-M5-Ende` bei ausgeschalteter VM.

#### Kontrollfragen
1. Wodurch unterscheiden sich Ubuntu LTS und eine Red-Hat-basierte Distribution in Paketverwaltung und Supportmodell?
2. Was bewirkt das Setgid-Bit (`2770`) auf einem gemeinsamen Verzeichnis?
3. Warum muss nach Änderung einer systemd-Unit `daemon-reload` ausgeführt werden?
4. Warum wird die Kennwortanmeldung per SSH erst nach einem erfolgreichen Schlüsseltest deaktiviert?
5. Warum braucht die ufw-Regel für SSH beide Quellnetze `192.168.50.0/24` und `192.168.60.0/24`?

---

### Modul 6: Virtualisierung, Storage und Plattformen für Rechenzentrum und Edge
* **Priorität:** 2
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Hypervisoren (Hyper-V, VMware, Proxmox) funktional vergleichen, Speicherarten (DAS, NAS, SAN) einordnen und Single Points of Failure einer Umgebung benennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine VM exportieren und als Klon in einem isolierten Netz importieren, Dynamic Memory konfigurieren und feste und dynamische virtuelle Festplatten vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Checkpoints (Produktion und Standard) richtig einsetzen, virtuelle Switch-Typen unterscheiden und typische Fehlerbilder (Speicherbedarf, Checkpoint-Wachstum) analysieren.
* **Voraussetzungen:** Modul 2 (Hyper-V-Grundlagen). Für die Aufgaben 2, 3 und 5 wird eine fertige Linux-VM benötigt: Ist Modul 5 nicht absolviert, stellt der Kursleiter eine beliebige kleine VM als `LX-UBU01` zur Verfügung. **Kein Pflichtmodul hängt von diesem Modul ab.**

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Hypervisor-Konzepte: VMware, Hyper-V oder Proxmox funktional vergleichen | 1,2 |
| 6.2 | VM-Lifecycle und Templates: Provisionierung, Standardisierung, Klonlogik | 1,2 |
| 6.3 | Ressourcenplanung: CPU, RAM, Storage und Overcommitment | 1,1 |
| 6.4 | Storage-Grundlagen: SAN, NAS und lokale Storage-Konzepte | 1,1 |
| 6.5 | Cluster und Hochverfügbarkeit: HA- und Failover-Logik im Grundsatz | 1,1 |
| 6.6 | Backup-Schnittstellen für VMs: Snapshots, Konsistenz, Integrationslogik mit Backup | 1,1 |
| 6.7 | Netzwerk in virtuellen Plattformen: vSwitch, Uplinks, Managementnetz | 1,1 |
| 6.8 | Troubleshooting in der Virtualisierung: Storage-Latenz, Snapshot-Wuchs, Ressourcenkonflikte | 1,1 |

#### Praxisaufgaben (Hands-on Lab)
Dieses Modul nutzt den privaten Switch `sw-lab-test` (anlegen mit `New-VMSwitch -Name sw-lab-test -SwitchType Private`, nicht bestätigt). Hyper-V-Cmdlets, die nicht durch Learn belegt sind (A.2), sind markiert. Das Hostlaufwerk `D:` und die Ordner darauf sind Beispiele und anzupassen.

1. **Hypervisoren vergleichen (Lernziel 1; Einheit 6.1):** Vergleiche Hyper-V, VMware und Proxmox VE: Lizenzmodell, Verwaltung, Backup-Anbindung, typische Einsatzgebiete (Rechenzentrum, Edge, Labor). Nutze die Herstellerseiten (URL und Abrufdatum); für VMware gibt es hier keine geprüfte Quelle, Lizenzangaben musst du selbst nachlesen und mit „nicht geprüft“ kennzeichnen, falls keine Quelle gefunden wird.
2. **Klon in isoliertem Netz (Lernziel 2; Einheit 6.2):**
   1. Exportiere `LX-UBU01`: `Export-VM -Name LX-UBU01 -Path D:\Export` (Learn; Pfad anpassen).
   2. Importiere als Kopie mit neuer ID: `Import-VM -Path '<Pfad>\LX-UBU01\Virtual Machines\<ID>.vmcx' -Copy -GenerateNewId -VhdDestinationPath D:\VMs\Klon -VirtualMachinePath D:\VMs\Klon` (Learn: `-Copy -GenerateNewId`).
   3. Benenne die VM um (`Rename-VM`, nicht bestätigt) in `LX-UBU01-Klon`, hänge **vor dem ersten Start** beide Adapter ab bzw. auf `sw-lab-test` (`Connect-VMNetworkAdapter -VMName LX-UBU01-Klon -SwitchName sw-lab-test` für `NIC-LAB`, `NIC-INET` bleibt getrennt; nicht bestätigt).
   4. Starte den Klon und beobachte: Hostname, IP-Adresse und SSH-Hostschlüssel sind identisch mit dem Original. Beschreibe, welche Konflikte entstünden, wenn beide im selben Netz liefen. Beschreibe in Worten (nicht ausführen), wie ein Linux-Template vorbereitet wird (Hostname, Maschinen-ID, SSH-Hostschlüssel zurücksetzen; Details nicht bestätigt).
   5. **Rückbau am Ende des Moduls:** `Stop-VM`, `Remove-VM -Name LX-UBU01-Klon -Force`, danach den Ordner `D:\VMs\Klon` löschen. **Vorbedingung:** Prüfe vorher mit `Get-VM -Name LX-UBU01-Klon | Get-VMHardDiskDrive`, dass die Datenträgerpfade im Klonordner liegen, und nicht im Ordner des Originals.
3. **Dynamic Memory (Lernziel 2; Einheit 6.3):** VM `LX-UBU01-Klon` ausschalten, `Set-VMMemory -VMName LX-UBU01-Klon -DynamicMemoryEnabled $true -StartupBytes 1GB -MinimumBytes 512MB -MaximumBytes 2GB` (nicht bestätigt; Learn: Startup RAM, Minimum RAM, Maximum RAM). Starte, notiere `Get-VM -Name LX-UBU01-Klon | Select-Object Name, MemoryAssigned, MemoryDemand`, belege im Gast ca. 600 MB (`python3 -c "x = bytearray(600*1024*1024); input()"`, Python-Vorinstallation nicht bestätigt, Abbruch mit Enter) und miss erneut. Rechne außerdem: Host mit 24 GB RAM, vier VMs mit je 8 GB Maximum: Überbuchungsfaktor und Folge, wenn alle Maximalwerte gleichzeitig benötigt werden.
4. **Storage (Lernziel 2; Einheiten 6.4, 6.5):**
   1. Lege auf dem Host eine feste und eine dynamische virtuelle Festplatte an (`New-VHD -Path D:\Test\fix.vhdx -SizeBytes 5GB -Fixed`; `New-VHD -Path D:\Test\dyn.vhdx -SizeBytes 5GB -Dynamic`) und vergleiche die Dateigrößen (`Get-Item`). **Rückbau:** nur diese beiden Dateien löschen, nachdem der Pfad `D:\Test` geprüft wurde.
   2. Erstelle eine Tabelle DAS, NAS, SAN: Zugriffsart, typische Protokolle, Ausfallfolgen.
   3. Papierübung Hochverfügbarkeit: Liste alle Single Points of Failure des Labors (Host, Datenträger, Netzteil, Switch, Strom) und ordne je eine Maßnahme zu. Beschreibe in vier Sätzen, was ein Failover-Cluster für zwei Hosts leistet und was nicht (zum Beispiel Datenverlust durch Fehlbedienung).
5. **Checkpoints (Lernziel 3; Einheit 6.6):** Setze `Set-VM -Name LX-UBU01-Klon -CheckpointType Production` (Learn). Lege eine Datei an, erzeuge einen Checkpoint, ändere die Datei, wende den Checkpoint an und notiere, dass die VM danach ausgeschaltet ist (Learn). Wiederhole mit `-CheckpointType Standard` bei laufender VM und vergleiche (Speicherzustand). Prüfe `Get-VMSnapshot -VMName LX-UBU01-Klon` und die `.avhdx`-Dateien im VM-Ordner. Entferne Checkpoints mit `Remove-VMCheckpoint` (Learn); **niemals** `.avhdx`-Dateien direkt löschen (Learn). Beschreibe, warum ein Checkpoint kein Backup ist (Learn).
6. **Switch-Typen (Lernziel 3; Einheit 6.7):** Lege einen internen Switch an (`New-VMSwitch -Name sw-lab-int -SwitchType Internal`), beobachte den neuen Netzwerkadapter auf dem Host (`Get-NetAdapter`), erkläre die Unterschiede zwischen privatem, internem und externem Switch und entferne ihn wieder (`Remove-VMSwitch -Name sw-lab-int -Force`). Einen externen Switch legst du **nicht** an, weil er das Labornetz mit dem Heimnetz verbinden würde.
7. **Fehlerbilder (Lernziel 3; Einheit 6.8):** Fallstudie mit drei Symptomen: (a) eine VM startet mit der Meldung „Not enough memory in the system to start the virtual machine“, (b) die Festplatte des Hosts ist voll, die VM-Ordner enthalten viele `.avhdx`-Dateien, (c) alle VMs sind langsam, die Datenträgerwarteschlange ist hoch. Nenne je Symptom zwei Hypothesen und den Prüfschritt. Nutze die Hinweise aus Learn: Zähler „Hyper-V Dynamic Memory Balancer, Available Memory“ und Prüfliste mit freiem Speicherplatz für das Zusammenführen (ideal in Größe der Festplatte).

#### Kontrollfragen
1. Welche Unterschiede bestehen zwischen Standard- und Produktions-Checkpoints, und warum ist keiner davon ein Backup?
2. Was bedeuten Startup RAM, Minimum RAM und Maximum RAM bei Dynamic Memory?
3. Warum muss ein importierter Klon `-GenerateNewId` bekommen, und warum läuft er in einem isolierten Switch?
4. Welche Unterschiede bestehen zwischen DAS, NAS und SAN bei Zugriff und Ausfallfolgen?
5. Wie entsteht ein Snapshot-Wachstum, und wie wird es beseitigt?

---

### Modul 7: Cloud Administration und Hybrid Platforms
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende IaaS, PaaS und SaaS anhand der Verantwortungsverteilung unterscheiden und die Azure-Grundbegriffe Subscription, Ressourcengruppe, Region, VNet und NSG einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende in einem Azure-Testkonto eine Ressourcengruppe, ein VNet mit überschneidungsfreiem Adressraum und eine Linux-VM mit eingeschränktem SSH-Zugang einrichten und die Kosten mit einem Budget begrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffe mit Azure RBAC und Azure Policy steuern, typische Verbindungs- und Rollenfehler eingrenzen und alle Ressourcen vollständig zurückbauen.
* **Voraussetzungen:** Modul 2 (Subnetting, Adressüberschneidung), Modul 3 (Identitätsbegriffe) und Modul 5 (SSH-Schlüssel). Für dieses Modul wird der Azure-Testzugang benötigt (A.3).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Cloud-Modelle und Servicearten: IaaS, PaaS, SaaS, Aufgabenverschiebung im Betrieb | 1,3 |
| 7.2 | Azure-Struktur und Basisobjekte: Subscriptions, Ressourcengruppen, Regionen | 1,3 |
| 7.3 | Virtuelle Netze und Konnektivität: VNet, Subnetze, Hybridanbindung | 1,3 |
| 7.4 | Compute und Standardservices: VMs, Storage, zentrale Plattformdienste | 1,3 |
| 7.5 | Identität und Rollen in der Cloud: RBAC, Entra, Zugriff | 1,2 |
| 7.6 | Governance und Policy Basis: Namensstandards, Tags, Richtlinien | 1,2 |
| 7.7 | Kosten- und Nutzungsgrundlagen: Verbrauchsmodell, Budgetkontrolle, Fehlkonfigurationen mit Kostenwirkung | 1,2 |
| 7.8 | Monitoring und Troubleshooting im Hybridbetrieb: Verbindungs-, Rollen- und Ressourcenthemen | 1,2 |

#### Praxisaufgaben (Hands-on Lab)
**Kostenhinweis:** Der Azure Free Account ist eine Ausnahme vom isolierten Labor: Dauer des Guthabens 30 Tage (laut Learn 200 USD; Betrag vor der Anmeldung auf der Anmeldeseite prüfen), Kosten 0 EUR innerhalb des Guthabens, Anmeldung mit Telefonnummer, Zahlungskarte (zur Überprüfung) und Microsoft- oder GitHub-Konto. Die Lernenden stimmen der Registrierung ausdrücklich zu; ein produktives Abonnement wird nie verwendet. **Voraussichtliche Kostentreiber, die nicht angelegt werden (nicht bestätigt):** VPN-Gateway, Bastion, Load Balancer, Datenbankdienste. Cloud-Zugriffe laufen vom Host (Browser, PowerShell, OpenSSH-Client; Verfügbarkeit nicht bestätigt), nicht von den Labor-VMs. Portalbezeichnungen und Menüpfade sind nicht bestätigt.

1. **Verantwortung zuordnen (Lernziel 1; Einheit 7.1):** Erstelle eine Matrix mit den Zeilen Hardware, Netzwerk, Betriebssystem, Laufzeit, Anwendung, Daten und den Spalten Lokal (`LX-UBU01`), IaaS, PaaS, SaaS: Wer ist verantwortlich (Anbieter oder Kunde)? Begründe zwei Zellen, in denen die Antwort überrascht.
2. **Konto, Budget und Struktur (Lernziel 2; Einheiten 7.2, 7.7):** Registriere das Free Account. **Zuerst** das Budget: lege ein Kostenbudget in kleiner Höhe an (Vorschlag 5 EUR, Annahme) mit Warnungen bei 50 % und 80 % an die eigene Adresse (Learn: Budgets). Danach Ressourcengruppe `rg-lab-sysadmin` in einer EU-Region deiner Wahl, Tags `Zweck=Kurs` und `Ablauf=<Datum>`. Notiere Subscription-ID **nicht** in Dokumenten.
3. **Netz planen und anlegen (Lernziel 2; Einheit 7.3):**
   1. Prüfe auf Papier, welche dieser Adressräume mit dem Labornetz (`192.168.50.0/24`, `192.168.60.0/24`, `192.168.100.0/24`) überlappen: `10.100.0.0/16`, `192.168.0.0/16`, `192.168.50.0/24`, `172.16.0.0/12`. Wähle einen überschneidungsfreien Raum.
   2. Lege ein VNet `vnet-lab` mit Adressraum `10.100.0.0/16` und Subnetz `snet-srv` (`10.100.1.0/24`) an sowie eine Netzwerksicherheitsgruppe `nsg-srv`, die SSH (TCP 22) nur von **deiner eigenen öffentlichen Adresse** erlaubt (Adresse nur im Portal eintragen, nicht im Dokument). Weise sie dem Subnetz zu.
   3. Beschreibe in vier Sätzen, wie eine echte Hybridanbindung (Site-to-Site-VPN) aussähe und warum sie hier wegen der Kosten nicht gebaut wird (Theorie).
4. **Linux-VM (Lernziel 2; Einheit 7.4):** Lege `vm-lab01` (Ubuntu Server, kleine Größe, z. B. `B1s`, Verfügbarkeit und Gratis-Kontingent laut Learn auf der Anmeldeseite prüfen) in `snet-srv` an, Authentifizierung nur mit SSH-Schlüssel (Schlüsselpaar mit `ssh-keygen -t ed25519` auf dem Host erzeugen, Passphrase interaktiv). Teste vom Host `Test-NetConnection <öffentliche Adresse der VM> -Port 22` und die Anmeldung mit `ssh`. Notiere den Speicher (Datenträger) der VM und nenne zwei Standarddienste der Plattform, die du nicht benutzt hast.
5. **Rollen (Lernziel 3; Einheit 7.5):** Lege im Verzeichnis des Testkontos einen Benutzer `user.az01` an (Kennwort interaktiv), weise die Rolle „Reader“ auf dem Scope `rg-lab-sysadmin` zu (Learn: RBAC-Scope), melde dich in einem privaten Browserfenster an, prüfe: sichtbar ja, `vm-lab01` stoppen nein. **Rückbau:** Rollenzuweisung und Benutzer entfernen.
6. **Governance (Lernziel 3; Einheit 7.6):** Weise auf `rg-lab-sysadmin` die integrierte Richtlinie „Allowed locations“ (Learn) mit deiner Region zu, versuche eine Ressource in einer anderen Region anzulegen und dokumentiere die Ablehnung (die Wirkungsverzögerung ist nicht bestätigt). Lege einen Namensstandard fest: `rg-`, `vnet-`, `snet-`, `nsg-`, `vm-` plus Zweck. **Rückbau:** Richtlinienzuweisung entfernen.
7. **Kosten verstehen (Lernziel 2; Einheit 7.7):** Rufe die Kostenanalyse auf und halte den aktuellen Stand fest. Berechne mit dem Preisrechner des Anbieters (Seite nicht geprüft; Datum angeben) die Monatskosten der VM bei Dauerbetrieb und bei 2 Stunden pro Tag. Nenne drei Fehlkonfigurationen mit Kostenwirkung (zum Beispiel vergessene Datenträger oder öffentliche Adressen, Aufzählung aus eigener Recherche, nicht bestätigt) und je eine Gegenmaßnahme.
8. **Fehler eingrenzen (Lernziel 3; Einheit 7.8):** Ein Partner baut drei Fehler ein: (a) die NSG-Regel erlaubt SSH nur von einer falschen Adresse, (b) `user.az01` darf als „Reader“ die VM nicht starten (Reader-Konto wird zum Test wieder zugewiesen), (c) die VM ist freigegeben/gestoppt (deallocated). Analysiere mit `Test-NetConnection`, den NSG-Regeln und dem VM-Status. Dokumentiere Symptom, Hypothese, Prüfschritt, Ursache, Behebung. Die Fehlersuche im Hybridbetrieb ist hier auf die Strecke Host zu Azure-VM beschränkt.
9. **Rückbau (alle Lernziele):** Prüfe zuerst in der Ressourcenliste, dass `rg-lab-sysadmin` nur deine Testressourcen enthält. Lösche dann die Ressourcengruppe im Portal (Learn: Löschen der Ressourcengruppe entfernt alle Ressourcen darin; alternativ `az group delete --name rg-lab-sysadmin`, die Azure CLI ist nicht Teil des Labors). Prüfe in der Ressourcenliste, dass nichts mehr existiert, lösche das Budget, und notiere das Ablaufdatum des Guthabens.

#### Kontrollfragen
1. Wer ist bei IaaS für das Betriebssystem verantwortlich, und wer bei PaaS?
2. Warum dürfen sich der Adressraum eines VNet und das lokale Netz nicht überschneiden?
3. Was bedeutet „Scope“ bei Azure RBAC, und wie wirkt eine Rolle auf Ressourcengruppen-Ebene?
4. Wozu dient die Richtlinie „Allowed locations“, und welche Wirkung hat sie auf bestehende Ressourcen?
5. Welche Schritte garantieren, dass nach dem Kurs keine Kosten mehr entstehen?

---

### Modul 8: Monitoring, Logging, Backup und Business Continuity
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Schwellwerte, Warnstufen und Logquellen festlegen, ein Prüfskript als geplante Aufgabe betreiben und Protokolle zentral auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien, den AD-Systemstatus und eine Linux-Konfiguration sichern und Wiederherstellungen mit Hash-Vergleich nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende RTO und RPO aus Messwerten ableiten, ein Runbook schreiben und typische Fehlerbilder (ungetestetes Backup, Alarmmüdigkeit, veraltete Dokumentation) bewerten.
* **Voraussetzungen:** Modul 3 (Domäne, Freigabe `Daten` auf `SRV-FS01`) und Modul 5 (`LX-UBU01`, SSH-Zugang von `CL-W11-01`). **Unabhängig von Modul 6:** Alle benötigten Datenträger werden in diesem Modul angelegt.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Monitoring-Grundlagen: Metriken, Schwellwerte, Alarmierung | 1,2 |
| 8.2 | Logging und zentrale Auswertung: Logs für Diagnose und Security-Fälle, Logquellen | 1,2 |
| 8.3 | Kapazität und Trendbeobachtung: Ressourcenentwicklung, Engpässe früh erkennen | 1,1 |
| 8.4 | Backup-Strategien: Voll, inkrementell, Wiederherstellungsziele | 1,1 |
| 8.5 | Restore und Testpflicht: Wiederherstellbarkeit als Kernkriterium, Restore-Prüfungen planen | 1,1 |
| 8.6 | BCDR Grundlagen: Business Continuity und Disaster Recovery, RTO und RPO | 1,1 |
| 8.7 | Dokumentation und Runbooks: Störfall- und Restoreabläufe standardisieren | 1,1 |
| 8.8 | Typische Fehlerbilder in Betrieb und Recovery: Alarmmüdigkeit, nie getestete Backups, unvollständige Doku | 1,1 |

#### Praxisaufgaben (Hands-on Lab)
Prüfpunkte `SRV-DC01-M8-Start`, `SRV-FS01-M8-Start`, `LX-UBU01-M8-Start` bei ausgeschalteten VMs. Zusätzliche Datenträger werden am Ende entfernt (Aufgabe 8). Cmdlets, die Learn nicht belegt, sind nicht bestätigt.

1. **Prüfskript und geplante Aufgabe (Lernziel 1; Einheit 8.1):** Lege auf `SRV-FS01` die Ordner `C:\Skripte` und `C:\Temp` an (`New-Item -ItemType Directory`) und darin `Check-Lab.ps1`:
   ```powershell
   $source = "LabMonitor"
   if (-not [System.Diagnostics.EventLog]::SourceExists($source)) {
       New-EventLog -LogName Application -Source $source
   }
   $freeGB = [math]::Round((Get-PSDrive -Name C).Free / 1GB, 1)
   $limit = 20   # Schwellwert in GB; zum Test auf 1000 setzen
   if ($freeGB -lt $limit) {
       Write-EventLog -LogName Application -Source $source -EventId 4001 -EntryType Warning -Message "C: nur $freeGB GB frei (Limit $limit GB)"
   }
   ```
   (`New-EventLog`/`Write-EventLog` gelten in Windows PowerShell 5.1, Learn.) Setze das Limit testweise auf 1000, führe das Skript aus und finde die Meldung im Ereignisprotokoll. Stelle es dann auf 20 zurück und plane die Ausführung alle 5 Minuten als SYSTEM (`Register-ScheduledTask` mit `New-ScheduledTaskAction`, `New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(2) -RepetitionInterval (New-TimeSpan -Minutes 5)`; ob zusätzlich eine Wiederholungsdauer nötig ist, ist nicht bestätigt). **Rückbau:** `Unregister-ScheduledTask -TaskName LabMonitor -Confirm:$false`. Lege dazu eine Tabelle der Warnstufen an (Information, Warnung, Kritisch): Bedingung, Empfänger, Reaktionszeit.
2. **Zentrale Auswertung (Lernziel 1; Einheit 8.2):** Lege auf `CL-W11-01` die Ordner `C:\Temp` und `C:\Backup` an. Von `CL-W11-01` aus (angemeldet als `LAB\lab-adm01`) Ereignisse beider Server abrufen: `Invoke-Command -ComputerName SRV-FS01,SRV-DC01 -ScriptBlock { Get-WinEvent -FilterHashtable @{LogName='Application'; ProviderName='LabMonitor'} -MaxEvents 10 }` (WinRM-Voraussetzungen, Firewallregeln und die automatische DNS-Registrierung der Servernamen nicht bestätigt; `Enable-PSRemoting` auf Servern nur falls nötig). Exportiere das Ergebnis mit `Export-Csv`. Hole das Linux-Journal per SSH: `ssh labadmin@192.168.50.30 "journalctl -p warning --since '1 hour ago' --no-pager" > C:\Temp\lx-journal.txt`. Erstelle eine Tabelle der Logquellen (Quelle, Inhalt, Wert für Diagnose, Wert für Security).
3. **Kapazitätstrend (Lernziel 1; Einheit 8.3):** Sammle auf `SRV-FS01` zehn Messwerte im Abstand von 30 Sekunden (freier Speicher auf `C:`, `Get-Counter '\Memory\Available MBytes'`) in eine CSV und berechne Mittelwert und Spanne mit `Import-Csv | Measure-Object`. Papierübung: Frei 40 GB, Wachstum 0,5 GB pro Tag, Alarmgrenze 10 GB; nach wie vielen Tagen wird die Grenze erreicht?
4. **Dateisicherung und Wiederherstellung (Lernziel 2; Einheiten 8.4, 8.5):**
   1. Auf `SRV-FS01`: `Install-WindowsFeature -Name Windows-Server-Backup` (Learn). Hänge eine neue leere Festplatte (40 GB) an; **Vorbedingung:** `Get-Disk` zeigt den neuen Datenträger als `RAW`; erst dann initialisieren und als `F:` formatieren.
   2. Lege in `E:\Daten\Projekt` 20 Testdateien an und speichere ihre Hashwerte (`Get-ChildItem E:\Daten\Projekt | Get-FileHash | Export-Csv C:\Temp\hash-vorher.csv`).
   3. Sicherung: `wbadmin start backup -backupTarget:F: -include:E: -quiet` (Learn). Versionen anzeigen: `wbadmin get versions -backupTarget:F:` (Learn).
   4. Lösche drei Testdateien (nur in `E:\Daten\Projekt`). Stelle sie wieder her: `wbadmin start recovery -version:<Version> -itemType:File -items:E:\Daten\Projekt\<Datei> -backupTarget:F: -recoveryTarget:E:\Wiederhergestellt` (Learn; Reihenfolge der Parameter und Option `-recursive` nicht bestätigt). Vergleiche die Hashwerte nach der Wiederherstellung mit der gespeicherten CSV.
   5. Messe die Dauer von Sicherung und Wiederherstellung (`Measure-Command { ... }`).
   6. Erstelle eine Tabelle Voll/Inkrementell/Differenziell: Sicherungsumfang, Wiederherstellungsaufwand, Speicherbedarf. Nenne die „3-2-1-Regel“ (Allgemeinwissen, nicht geprüft) und beurteile, welche ihrer Teile das Labor nicht erfüllt.
5. **AD-Systemstatus (Lernziel 2; Einheit 8.4):** Hänge an `SRV-DC01` eine neue leere Festplatte (30 GB) an (`Get-Disk` prüfen), formatiere sie als `G:` und sichere den Systemstatus: `wbadmin start systemstatebackup -backupTarget:G:` (Learn: Befehl `systemstatebackup`; Ausgabe nicht bestätigt). Die Wiederherstellung (`wbadmin start systemstaterecovery`, Learn) wird **nicht ausgeführt**, nur anhand der Learn-Seite beschrieben: Welche Voraussetzungen (u. a. besonderer Startmodus des DC) nennt die Seite, und warum ist eine Wiederherstellung eines DC kein Routineschritt (nicht bestätigt)?
6. **Linux-Sicherung (Lernziel 2; Einheiten 8.4, 8.5):** Auf `LX-UBU01`: `sudo tar -czf ~/etc-backup.tar.gz /etc`, Hash `sha256sum ~/etc-backup.tar.gz`. Übertrage mit `scp labadmin@192.168.50.30:etc-backup.tar.gz C:\Backup\` (auf `CL-W11-01`) und vergleiche mit `Get-FileHash -Algorithm SHA256`. Stelle eine Datei zurück: `tar -xzf etc-backup.tar.gz -C /tmp etc/hostname` und vergleiche mit `diff /etc/hostname /tmp/etc/hostname`.
7. **RTO, RPO und Runbook (Lernziel 3; Einheiten 8.6, 8.7):** Leite aus den Messungen der Aufgaben 4 bis 6 für `SRV-FS01` ein RPO (tägliche Sicherung bedeutet höchstens 24 Stunden Datenverlust) und ein RTO (gemessene Dauer plus Vorbereitungs- und Prüfzeit) ab und begründe, ob sie zu einem Betrieb passen, der 4 Stunden Ausfall verträgt. Schreibe ein Runbook „Einzelne Datei auf `SRV-FS01` wiederherstellen“ (Zweck, Voraussetzungen, Schritte, Prüfung, Eskalation, Version und Datum, Kontakt als Platzhalter). Ein Mitlernender führt das Runbook ohne Rückfragen aus; notiere jede Abweichung und verbessere das Runbook.
8. **Fehlerbilder bewerten und aufräumen (Lernziel 3; Einheit 8.8):** Bewerte drei Fallstudien: (a) Ein Backup läuft seit sechs Monaten, die erste Wiederherstellung scheitert. (b) Ein Team erhält 200 Alarmmeldungen am Tag und ignoriert sie. (c) Ein Runbook nennt eine alte IP-Adresse. Nenne je Ursache, Gegenmaßnahme und Prüfintervall. **Rückbau:** Zusatzdatenträger `F:` und `G:` von den VMs trennen (Hyper-V-Einstellungen) und die zugehörigen VHDX-Dateien löschen, nachdem Pfad und Dateiname mit `Get-VMHardDiskDrive` bestätigt wurden. `C:\Temp\hash-vorher.csv` kann bleiben.

#### Kontrollfragen
1. Warum wird eine Warnung erst bei einem Schwellwert und nicht bei jeder Abweichung ausgelöst?
2. Warum gilt ein Backup erst nach einem erfolgreichen Restore-Test als sicher?
3. Was unterscheidet RTO und RPO, und wie ergeben sie sich aus den Messwerten dieses Moduls?
4. Welche Vorteile bietet das Sichern des AD-Systemstatus, und warum wird die Wiederherstellung nicht im Kurs ausgeführt?
5. Welche Eigenschaften hat ein gutes Runbook, und wie wird es getestet?

---

### Modul 9: Security, Hardening und Identity & Access Management
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Schutzbedarf und Angriffsfläche von Systemen bewerten (offene Ports, Patchstand) und Schwachstellen nach Risiko priorisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Mehrfaktor-Authentifizierung mit den Sicherheitsstandards einrichten, privilegierte Konten trennen und absichern, Aufgaben delegieren und Systeme nach einer Checkliste härten.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffsmodelle prüfen, fehlgeschlagene Anmeldungen auditieren und typische Fehlerbilder (offene Freigabe, geteilte Administratorkonten, fehlende MFA) erkennen und beheben.
* **Voraussetzungen:** Modul 3 (Domäne, Gruppen, Freigaben), Modul 5 (`LX-UBU01`), Modul 7 (Azure-Testkonto und dessen Verzeichnis für Aufgabe 3) und Modul 8 (Logquellen).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Security-Grundprinzipien im Betrieb: Schutzbedarf, Angriffsoberfläche, Minimalprinzip | 1,3 |
| 9.2 | Patch- und Vulnerability-Grundlagen: Aktualität als Sicherheitselement, Priorisierung nach Risiko | 1,3 |
| 9.3 | MFA und starke Authentifizierung: Standard für Admin- und Cloud-Zugriffe | 1,3 |
| 9.4 | Privilegierte Konten und Rollen: Admin-Konten, Delegation, Least Privilege | 1,3 |
| 9.5 | Hardening von Servern und Clients: sichere Defaults, Baselines, reduzierte Dienste | 1,2 |
| 9.6 | Identity & Access Management: Zugriffsmodelle für Benutzer, Gruppen, Rollen; Nachvollziehbarkeit | 1,2 |
| 9.7 | Security Logging und Basiserkennung: Sicherheitsereignisse von Betriebslogs unterscheiden | 1,2 |
| 9.8 | Typische Security-Fehlerbilder: geteilte Admin-Konten, fehlende MFA, offene Freigaben, Sofortmaßnahmen | 1,2 |

#### Praxisaufgaben (Hands-on Lab)
Prüfpunkte der Domänen-VMs nur bei ausgeschalteter VM. Befehle ohne Learn-Beleg (A.2) sind nicht bestätigt. Kein Kennwort wird in Skripten oder Dokumenten festgehalten.

1. **Angriffsfläche und Schutzbedarf (Lernziel 1; Einheit 9.1):** Liste auf Windows-VMs die lauschenden Ports (`Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess`) und ordne den Prozess zu (`Get-Process -Id <ID>`), auf `LX-UBU01` mit `sudo ss -tulpn`. Erstelle eine Tabelle je VM: Port, Dienst, nötig ja/nein, Maßnahme. Bewerte den Schutzbedarf (hoch, mittel, niedrig) von `SRV-DC01`, `SRV-FS01`, `LX-UBU01`, `CL-W11-01` nach Vertraulichkeit, Integrität, Verfügbarkeit mit je einem Satz Begründung.
2. **Patchstand und Priorisierung (Lernziel 1; Einheit 9.2):** Erhebe den Patchstand (`Get-HotFix` auf den Windows-VMs, zeigt nicht alle Updates, nicht bestätigt; `apt list --upgradable` auf `LX-UBU01`) und halte fest, dass `SRV-DC01` und `CL-W11-01` im Labor keine Updates beziehen (Risiko dokumentieren, Maßnahmenplan formulieren). Priorisiere anschließend diese drei erfundenen Schwachstellen und begründe die Reihenfolge nach Schwere laut Hersteller, Erreichbarkeit und bekannter Ausnutzung:

   | Meldung | Schwere laut Hersteller | Erreichbarkeit | Ausnutzung bekannt |
   | :--- | :--- | :--- | :--- |
   | A | kritisch | aus dem Internet | ja |
   | B | hoch | nur intern | nein |
   | C | mittel | aus dem Internet | nein |
3. **MFA einrichten (Lernziel 2; Einheit 9.3):** Im Verzeichnis des Azure-Testkontos (Entra ID Free; Verfügbarkeit nach Ablauf des Guthabens nicht bestätigt, andernfalls Fallstudie mit den Learn-Seiten zu Sicherheitsstandards und MFA-Lizenzierung) lege `user.mfa01` an (Kennwort interaktiv). Aktiviere die Sicherheitsstandards (Learn; Menüpfad nicht bestätigt) **erst, nachdem** du dein Administratorkonto in einem zweiten Fenster mit einer Authentifizierungs-App (TOTP) registriert hast, damit du dich nicht aussperrst. Melde `user.mfa01` an, registriere eine Authentifizierungs-App, melde dich ab und erneut an und dokumentiere die Abfrage. **Rückbau:** Sicherheitsstandards deaktivieren (falls nicht mehr benötigt) und Testbenutzer löschen. Beantworte: Warum können Sicherheitsstandards nicht zusammen mit einer eigenen Conditional-Access-Richtlinie desselben Verzeichnisses betrieben werden (nicht bestätigt, Begründung aus Learn herleiten)?
4. **Privilegierte Konten und Delegation (Lernziel 2; Einheit 9.4):**
   1. Auf `SRV-FS01` das AD-Modul installieren: `Install-WindowsFeature RSAT-AD-PowerShell` (nicht bestätigt).
   2. Delegiere auf der OU `Benutzer` mit dem Assistenten „Objektverwaltung zuweisen“ (Active Directory-Benutzer und -Computer) an `grp-helpdesk` nur das Recht „Benutzerkennwörter zurücksetzen und Kennwortänderung bei der nächsten Anmeldung erzwingen“ (Name im Assistenten nicht bestätigt).
   3. Test als `lab-hd01` (Mitglied von `grp-helpdesk`): `Set-ADAccountPassword -Identity lab-user01 -Reset -NewPassword (Read-Host -AsSecureString "Neues Kennwort") -Credential LAB\lab-hd01` (soll gelingen, Kennwort wird abgefragt). Wiederhole für `lab-adm01` in der OU `Admin` (soll mit „Zugriff verweigert“ scheitern). Erkläre, warum.
   4. Lege ein Zweitkonto `lab-adm02` an, füge es der Gruppe `Protected Users` hinzu und beobachte, dass die Anmeldung mit Namen funktioniert, mit IP-Adresse (NTLM) nicht (nicht bestätigt). Das bestehende Konto `lab-adm01` wird **nicht** in diese Gruppe aufgenommen, um Verwaltungszugriffe nicht zu verlieren. **Rückbau:** `lab-adm02` löschen.
5. **Härtung nach Checkliste (Lernziel 2; Einheit 9.5):** Beschränke die Ping-Regel aller Windows-VMs auf die Labornetze: `Set-NetFirewallRule -DisplayName "LAB-ICMPv4-In" -RemoteAddress 192.168.50.0/24,192.168.60.0/24` (nicht bestätigt); Wirkung testen. Erstelle eine Checkliste mit mindestens 10 Punkten (Updates, Firewall an, nicht benötigte Rollen entfernt, getrennte Admin-Konten, SSH nur mit Schlüssel, Root-Login aus, Gastkonto deaktiviert, Freigaben geprüft, Protokollierung aktiv, Notfallzugang dokumentiert) und bewerte jede VM mit erfüllt, teilweise, nicht erfüllt, mit Nachweis (Befehl oder Screenshot-Beschreibung).
6. **Zugriffsmodell prüfen (Lernziel 3; Einheit 9.6):** Zeichne die Zugriffsmatrix des Labors (Rolle, Gruppe, Ressource, Recht, Verantwortlicher als Platzhalter). Prüfe die Ist-Mitgliedschaften: `Get-ADGroupMember "Domain Admins"` und `Get-ADGroupMember grp-helpdesk` (nicht bestätigt) und vergleiche Soll und Ist. Benenne jede Abweichung.
7. **Auditing (Lernziel 3; Einheit 9.7):** Merke dir vorher die Einstellung (`auditpol /get /subcategory:"Logon"`). Aktiviere auf `SRV-FS01` die Fehlerprotokollierung der Anmeldung (`auditpol /set /subcategory:"Logon" /failure:enable`; Unterkategoriename nicht bestätigt). Löse von `CL-W11-01` einen Fehlversuch aus: `net use \\192.168.50.20\Daten /user:LAB\lab-user01 *` und gib ein **falsches** Kennwort ein. Suche das Ereignis auf `SRV-FS01` (`Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5`; die Ereignis-ID 4625 für fehlgeschlagene Anmeldungen ist nicht bestätigt) und notiere Zeit, Konto, Quelladresse und Fehlerursache. Prüfe zusätzlich `SRV-DC01`. **Rückbau:** den ursprünglichen Wert wiederherstellen (`auditpol /set /subcategory:"Logon" /failure:disable`, falls er vorher deaktiviert war). Erkläre, was ein Sicherheitsereignis von einem Betriebsereignis unterscheidet.
8. **Fehlerbilder finden und beheben (Lernziel 3; Einheit 9.8):** Ein Partner legt auf `SRV-FS01` eine Freigabe `Tausch` für `Jeder` mit Vollzugriff an (z. B. `New-SmbShare -Name Tausch -Path E:\Tausch -FullAccess Everyone`, nicht bestätigt). Finde sie mit `Get-SmbShare` und `Get-SmbShareAccess -Name Tausch`, bewerte das Risiko und behebe (Zugriff auf `dl-projekt-rw` beschränken oder die Freigabe entfernen, nachdem du den Pfad geprüft hast). Bearbeite außerdem zwei Fallstudien mit Sofortmaßnahmen: (a) Ein Administratorkonto wird von drei Personen gemeinsam genutzt. (b) Ein Cloud-Administrator hat keine MFA.

#### Kontrollfragen
1. Was bedeutet „Angriffsfläche reduzieren“, und welche zwei Maßnahmen dazu hast du im Labor umgesetzt?
2. Nach welchen drei Kriterien priorisierst du Patches, wenn nicht alle gleichzeitig eingespielt werden können?
3. Warum wird beim Einrichten von MFA zuerst das eigene Administratorkonto geprüft?
4. Warum erhält ein Helpdesk-Konto nur delegierte Rechte statt Mitgliedschaft in `Domain Admins`?
5. Welche Information liefert ein fehlgeschlagenes Anmeldeereignis, und wo findest du es?

---

### Modul 10: Automation, Scripting und Infrastructure as Code Grundlagen
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende wiederkehrende Aufgaben nach Nutzen und Risiko als Skriptkandidaten bewerten sowie einfache PowerShell- und Bash-Skripte schreiben, ausführen und planen.
  * Nach Abschluss dieses Moduls kann der Lernende Betriebsdaten als CSV und JSON ausgeben, Skripte mit Parametern, Validierung, try/catch und `-WhatIf` absichern und Benutzer aus einer CSV-Datei in Active Directory anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende deklarative Konfiguration (DSC) von imperativen Skripten unterscheiden, Infrastructure as Code einordnen und Skripte mit Ablage, Freigabe und Hashprüfung regeln.
* **Voraussetzungen:** Modul 3 (Domäne, `SRV-FS01`) und Modul 5 (`LX-UBU01`, Bash-Umgebung).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Automatisierungsdenken im Betrieb: Skriptkandidaten erkennen, Nutzen gegen Risiko abwägen | 1,3 |
| 10.2 | PowerShell Grundlagen: Befehlsaufbau, Objekte, einfache Automation im Windows-Umfeld | 1,3 |
| 10.3 | Bash Grundlagen: Shell-Logik, Variablen, einfache Linux-Automation | 1,3 |
| 10.4 | Dateien, Logs und Reports automatisieren: Ausgaben, Selektion, Export von Betriebsdaten | 1,3 |
| 10.5 | Fehlerbehandlung und saubere Skripte: Try/Catch, Validierung, gefährliche Skripte vermeiden | 1,2 |
| 10.6 | Skripte für AD, Clients und Server: typische Admin-Use-Cases mit vertretbarem Risiko | 1,2 |
| 10.7 | IaC Grundideen: deklarative Infrastruktur, Wiederholbarkeit, Brücke zu Cloud und DevOps | 1,2 |
| 10.8 | Governance für Automation: Skriptablage, Freigabe, Dokumentation | 1,2 |

#### Praxisaufgaben (Hands-on Lab)
Alle Windows-Skripte laufen in Windows PowerShell 5.1 auf `SRV-FS01` (Ordner `C:\Skripte`, ab Modul 8 vorhanden oder neu anlegen). Alle Skripte werden zuerst mit `-WhatIf` oder in einem Testordner geprüft. Befehle ohne Learn-Beleg sind nicht bestätigt.

1. **Skriptkandidaten bewerten (Lernziel 1; Einheit 10.1):** Bewerte diese sechs Aufgaben nach Häufigkeit, Dauer pro Durchführung, Fehlerrisiko und Umkehrbarkeit und entscheide „Skript ja/nein“ mit Begründung: Kennwort zurücksetzen, 20 neue Benutzer anlegen, inaktive Konten löschen, wöchentlicher Bericht über freien Speicher, einmalige Migration von 5 TB Daten, Neustart eines hängenden Dienstes.
2. **PowerShell-Grundlagen (Lernziel 1; Einheit 10.2):** Gib `$PSVersionTable` aus. Nutze `Get-Command`, `Get-Help Get-Service -Examples`, `Get-Member` und die Pipeline: `Get-Service | Where-Object Status -eq Running | Sort-Object Name | Select-Object -First 5` sowie `Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name, WS`. Erkläre den Unterschied zwischen Text und Objekt an dieser Ausgabe.
3. **Bash-Skript und Zeitplan (Lernziel 1; Einheit 10.3):** Auf `LX-UBU01` das Skript `~/diskcheck.sh`:
   ```bash
   #!/bin/bash
   set -euo pipefail
   LIMIT=80
   USED=$(df --output=pcent / | tail -n 1 | tr -dc '0-9')
   if [ "$USED" -ge "$LIMIT" ]; then
       echo "WARNUNG: / zu ${USED}% belegt"
       exit 1
   fi
   echo "OK: / zu ${USED}% belegt"
   ```
   Ausführbar machen (`chmod +x`), ausführen, Rückgabewert mit `echo $?` zeigen, Limit testweise auf 1 setzen und Fehlerfall zeigen. Plane es alle 5 Minuten mit `crontab -e` (`*/5 * * * * /home/labadmin/diskcheck.sh >> /home/labadmin/diskcheck.log 2>&1`). **Rückbau:** den Eintrag in `crontab -e` löschen (nicht `crontab -r`, das entfernt alle Einträge).
4. **Berichte (Lernziel 2; Einheit 10.4):** Erzeuge auf `SRV-FS01` einen Bericht der Laufwerke mit freiem Speicher in Gigabyte (berechnete Eigenschaft): `Get-Volume | Where-Object DriveLetter | Select-Object DriveLetter, @{n='FreiGB';e={[math]::Round($_.SizeRemaining/1GB,1)}}` und exportiere als `Export-Csv` und `ConvertTo-Json` in `C:\Skripte\bericht-<Datum>.csv/json` (Datum aus `Get-Date -Format yyyy-MM-dd`). Öffne die CSV in einem Editor und die JSON-Datei und erkläre die Unterschiede.
5. **Sicheres Löschskript (Lernziel 2; Einheit 10.5):** Schreibe `Remove-OldFiles.ps1` mit `[CmdletBinding(SupportsShouldProcess)]`, den Parametern `Path` und `Days` (Validierung: `Path` muss unterhalb `C:\Skripte\Test` liegen, `Days` zwischen 1 und 365), `try/catch` und `-ErrorAction Stop`. Das Skript muss jeden Pfad außerhalb des Testordners ablehnen. Teste: erst mit `-WhatIf`, dann real in einem Ordner mit angelegten Beispieldateien (`(Get-Item $f).LastWriteTime = (Get-Date).AddDays(-40)`), dann mit einem verbotenen Pfad (z. B. `C:\Windows`; es darf nichts gelöscht werden).
6. **Benutzer aus CSV (Lernziel 2; Einheit 10.6):** **Vorbedingung:** Auf `SRV-FS01` ist das AD-Modul vorhanden (Modul 9, sonst `Install-WindowsFeature RSAT-AD-PowerShell`). Lege die OU `Skript-Test` an. Erstelle `users.csv` (Spalten `Name`, `Vorname`, `Anmeldename`) mit fünf Konten `skript-user01` bis `skript-user05`. Schreibe ein Skript, das (a) nach `Get-ADUser -Filter` prüft, ob das Konto schon existiert (wiederholbar), (b) einmal ein Anfangskennwort mit `Read-Host -AsSecureString` abfragt, (c) die Konten in der OU anlegt und `-ChangePasswordAtLogon $true` setzt, (d) `-WhatIf` unterstützt. Lauf zweimal und prüfe, dass der zweite Lauf nichts doppelt anlegt. **Rückbau:** Prüfe mit `Get-ADUser -SearchBase "OU=Skript-Test,DC=lab,DC=example,DC=internal" -Filter *`, dass nur die fünf Testkonten existieren; erst dann Schutz vor versehentlichem Löschen entfernen (`Set-ADOrganizationalUnit … -ProtectedFromAccidentalDeletion $false`) und OU samt Inhalt entfernen (`Remove-ADOrganizationalUnit … -Recursive`; Cmdlets nicht bestätigt).
7. **Deklarativ statt imperativ (Lernziel 3; Einheit 10.7):** Auf `SRV-FS01` (Windows PowerShell 5.1, Learn: DSC 1.1) die Konfiguration anlegen:
   ```powershell
   Configuration LabBasis {
       Import-DscResource -ModuleName PSDesiredStateConfiguration
       Node "localhost" {
           File Ordner { DestinationPath = "C:\Skripte\dsc-test"; Type = "Directory"; Ensure = "Present" }
           File Datei  { DestinationPath = "C:\Skripte\dsc-test\hallo.txt"; Contents = "Lab"; Ensure = "Present"; DependsOn = "[File]Ordner" }
       }
   }
   LabBasis -OutputPath C:\Skripte\LabBasis
   Start-DscConfiguration -Path C:\Skripte\LabBasis -Wait -Verbose
   ```
   Wende sie zweimal an (zweiter Lauf ändert nichts), lösche die Datei per Hand, wende erneut an (wird neu erstellt) und zeige den Zustand mit `Get-DscConfiguration`. Schreibe danach das Ergebnis als Skript mit `if (-not (Test-Path ...))` und vergleiche beide Ansätze in einer Tabelle (Wiederholbarkeit, Lesbarkeit, Drift). **Rückbau:** den Ordner `C:\Skripte\dsc-test` löschen, nachdem der Pfad geprüft wurde. Bicep und Terraform sind in diesem Lehrplan nur Theorie: Beschreibe in einem Absatz, wie eine deklarative Cloud-Vorlage (Modul 7) die Ressourcengruppe `rg-lab-sysadmin` wiederholbar erzeugen würde (Quellen dazu nicht geprüft).
8. **Skript-Governance (Lernziel 3; Einheit 10.8):** Lege auf `SRV-FS01` die Freigabe `Skripte$` (versteckt) auf `C:\Skripte\Freigegeben` an, NTFS-Änderungsrecht nur für `LAB\lab-adm01`, Lesen für `Authentifizierte Benutzer`. Lege einen Kopfblock für jedes Skript fest (Zweck, Verantwortlicher als Rolle, Version, Änderungsdatum, Aufrufbeispiel). Erzeuge eine Freigabeliste `freigabe.csv` mit Skriptname, Version, SHA-256-Hash (`Get-FileHash`), Datum, Freigeber. Schreibe ein Startskript, das vor der Ausführung den Hash prüft und bei Abweichung abbricht. Notiere `Get-ExecutionPolicy -List` und erkläre, warum die Ausführungsrichtlinie keine Sicherheitsgrenze ist (nicht bestätigt). Ändere sie nur, wenn nötig, und stelle den Ausgangswert danach wieder her.

#### Kontrollfragen
1. Nach welchen Kriterien entscheidest du, ob sich eine Aufgabe für ein Skript eignet?
2. Wodurch unterscheiden sich Objekte in PowerShell von Text in Bash, und was folgt für die Weiterverarbeitung?
3. Welche drei Schutzmaßnahmen verhindern, dass ein Löschskript Unbeabsichtigtes löscht?
4. Was bedeutet „idempotent“ am Beispiel des Benutzerskripts und der DSC-Konfiguration?
5. Welche Elemente gehören zu einer nachvollziehbaren Skriptablage (Ablage, Freigabe, Prüfung)?

---

### Modul 11: Troubleshooting, ITSM, Dokumentation und Governance im Betrieb
* **Priorität:** 2
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Störungen mit einer festen Methode (Symptom, Hypothese, Prüfpfad, Zeitbox, Eskalation) analysieren und Incident, Problem und Change unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine Störung dokumentieren, eine Änderung mit Risiko, Test und Rollback beantragen und kontrolliert durchführen sowie Statusmeldungen sachlich formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine Asset- und Abhängigkeitsübersicht erstellen, Betriebsstandards und Zuständigkeiten festlegen und typische Fehlerbilder (Ad-hoc-Fixes, fehlende Assets, unklare Zuständigkeit) bewerten.
* **Voraussetzungen:** Modul 3 (Domäne, DNS). Dieses Modul ist überwiegend Dokumentation; die Begriffe Incident, Problem und Change werden als Allgemeinwissen verwendet (A.2: Keine geprüfte Quelle). **Kein Pflichtmodul hängt von diesem Modul ab.**

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Systematisches Troubleshooting: Symptome, Hypothesen, Prüfpfade, Zeit und Eskalation | 1 |
| 11.2 | Incident, Problem und Change unterscheiden: Bearbeitungslogik je Falltyp | 1 |
| 11.3 | Dokumentation als Betriebswerkzeug: Systemdokumentation, Runbooks, Vertretung und Recovery | 1 |
| 11.4 | Change- und Release-Disziplin: Risiko, Test, Kommunikationsbedarf, kontrollierte Änderungen | 1 |
| 11.5 | Asset- und Konfigurationsübersicht: Systeme, Abhängigkeiten, Betriebsverantwortung | 1 |
| 11.6 | Basis-Governance im Systembetrieb: Standards, Rollen, Freigaben | 1 |
| 11.7 | Kommunikation in Störfällen: Statusmeldungen, Eskalationen, Rückfragen | 1 |
| 11.8 | Typische Fehlerbilder im Betrieb: Ad-hoc-Fixes ohne Doku, fehlende Assets, unklare Zuständigkeiten | 1 |

#### Praxisaufgaben (Hands-on Lab)
Die Aufgaben 2 bis 4 verwenden das Labor; die übrigen sind Dokumentations- und Fallstudienaufgaben. Prüfpunkt `SRV-DC01-M11-Start` bei ausgeschalteter VM.

1. **Methode anwenden (Lernziel 1; Einheit 11.1):** Fallstudie: „Der Dateiserver ist seit 08:10 nicht erreichbar.“ Erstelle eine Vorlage mit den Spalten Zeit, Symptom, Hypothese, Prüfschritt, Ergebnis, nächste Aktion, Zeitbox (15 Minuten je Hypothese) und Eskalationskriterium. Fülle sie für drei Hypothesen (Netz, Namensauflösung, Dienst) aus.
2. **Störungssimulation (Lernziele 1 und 2; Einheiten 11.2, 11.7, 11.8):** Ein Partner stoppt auf `SRV-DC01` den DNS-Dienst (`Stop-Service -Name DNS`, Dienstname nicht bestätigt). Analysiere von `CL-W11-01` aus (`nslookup`, Zugriff per Name und per IP, Anmeldung), eskaliere nach der Zeitbox, stelle den Dienst wieder her (`Start-Service -Name DNS`). Lege einen Incident-Eintrag an: Nummer, Zeit, Symptom, Auswirkung, Maßnahmen mit Uhrzeit, Ursache, Lösung, Dauer. Schreibe drei Statusmeldungen (Beginn, Zwischenstand, Ende) mit Wer ist betroffen, Was geht nicht, Seit wann, Workaround, nächste Information um. Formuliere sachlich, ohne Schuldzuweisung.
3. **Problem-Eintrag (Lernziel 1; Einheit 11.2):** Lege zum Vorfall einen Problem-Eintrag an: Ursachenanalyse (warum stoppte der Dienst, warum wurde es nicht automatisch erkannt oder neu gestartet?), Gegenmaßnahme, Verantwortlicher als Rolle. Erkläre den Unterschied zwischen Incident (Wiederherstellung) und Problem (Ursache beseitigen) an diesem Beispiel.
4. **Change beantragen und durchführen (Lernziel 2; Einheiten 11.4, 11.3):** Schreibe eine Änderungsanforderung für „Wiederherstellungsaktionen für den DNS-Dienst“ mit Beschreibung, Grund, Risiko, Test, Rollback, Zeitfenster, Kommunikation, Freigeber (als Rolle). **Vorbedingung:** Sichere den Ist-Zustand (`sc.exe qfailure DNS`) im Antrag. Führe die Änderung im Wartungsfenster aus (`sc.exe failure DNS reset= 86400 actions= restart/60000/restart/60000//0`; Syntax nicht bestätigt), teste durch erneutes Stoppen des Dienstes (soll nach der eingestellten Wartezeit wieder starten, nicht bestätigt), und führe den Rollback anhand der gesicherten Werte aus. Dokumentiere Ergebnis und Abweichungen.
5. **Asset-Übersicht (Lernziel 3; Einheit 11.5):** Erzeuge die Computerliste aus AD (`Get-ADComputer -Filter * -Properties OperatingSystem, IPv4Address | Select-Object Name, OperatingSystem, IPv4Address | Export-Csv`, nicht bestätigt) und ergänze `LX-UBU01` (und, falls noch vorhanden, `CL-W11-02`) von Hand. Erweitere die Tabelle um Rolle, Verantwortlicher (Rolle), Kritikalität, Abhängigkeiten, Dokumentationsverweis. Zeichne die Abhängigkeitskette (z. B. Clients hängen an Namensauflösung auf `SRV-DC01`) als Textskizze.
6. **Betriebsdokumentation und Standards (Lernziel 3; Einheiten 11.3, 11.6):** Erstelle das Gerüst eines Betriebshandbuchs (Inhaltsverzeichnis) und fülle die Systemdokumentation für `SRV-FS01` (Zweck, Rollen, Adressen, Freigaben, Sicherungen, Verantwortlicher als Rolle, Wiederanlaufhinweise). Schreibe einen Betriebsstandard auf einer Seite: Namenskonventionen (aus Modul 3 und 7), Rollen (wer darf was ändern, wer genehmigt), Freigabeverfahren für Änderungen.
7. **Fehlerbilder bewerten (Lernziel 3; Einheit 11.8):** Bewerte drei Fälle: (a) Jemand lockert eine Firewallregel, um ein Problem zu beheben, und vergisst es; zwei Wochen später tritt dasselbe Problem wieder auf. (b) In einem Netzwerksegment wird ein unbekannter Server gefunden. (c) Ein Alarm geht ein, aber niemand fühlt sich zuständig. Nenne je Ursache, Gegenmaßnahme und welches Dokument (Change, Asset-Liste, Zuständigkeitsregel) das Problem verhindert hätte.

#### Kontrollfragen
1. Worin unterscheiden sich Incident, Problem und Change?
2. Wozu dient die Zeitbox bei der Fehlersuche, und wann eskaliert man?
3. Welche Bestandteile braucht ein Änderungsantrag, damit der Rollback möglich ist?
4. Welche Angaben gehören in eine Statusmeldung während einer Störung?
5. Warum ist eine Asset-Übersicht mit Abhängigkeiten für die Störungsanalyse nützlich?

---

### Modul 12: Karrierepfade, Zertifikate und Spezialisierungen nach der Lehre
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Spezialisierungen und Zertifikate (Microsoft, Netzwerk, Linux, Virtualisierung/Backup) anhand von Herstellerseiten und der eigenen Kompetenzmatrix vergleichen und den Modulen dieses Lehrplans zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Praxisprojekte ohne Kennwörter und Echtdaten dokumentieren und Arbeitsumfelder (Dienstleister, Unternehmen, öffentliche Verwaltung) nach Kriterien vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Plan für 12 bis 36 Monate mit Praxis, Zertifikaten und Meilensteinen erstellen und ihn mit dem Plan und der Matrix aus Modul 1 abgleichen.
* **Voraussetzungen:** Modul 1 (Matrix und Entwicklungsplan, ab Modul 12 überarbeitet). Die Module 2 bis 10 liefern die Nachweise für Aufgabe 3; Ergebnisse aus den Vertiefungsmodulen 6 und 11 sind nicht erforderlich. Kein technisches Labor; Recherche und Fallstudien.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Top-Spezialisierungen nach Marktwert: Modern Workplace, Cloud, Netzwerk/Security, Linux/Automation, Virtualisierung qualitativ vergleichen | 1 |
| 12.2 | Sinnvolle Zertifikate für Microsoft-Pfade: AZ-104, MS-102 oder Fundamentals-Levels, Einstiegshürden | 1 |
| 12.3 | Netzwerk- und Security-Nachweise: CCNA, Basis-Firewall- oder Security-Zertifikate | 1 |
| 12.4 | Linux- und Plattformzertifikate: LPIC-1, RHCSA oder distributionsnahe Wege | 1 |
| 12.5 | Virtualisierung und Backup-Pfade: VM- und BCDR-nahe Nachweise als Nischenhebel | 1 |
| 12.6 | Praxisprojekte und Homelab: Lab, Doku und Git-basierte Nachweise für das Bewerbungsprofil | 1 |
| 12.7 | Kanzlei/Dienstleister versus Unternehmen: Arbeitsumfelder nach Lernchance, Breite und Spezialisierungspotenzial | 1 |
| 12.8 | Individueller 12- bis 36-Monats-Plan: Praxis, Zertifikate, Projektarbeit, Spezialisierung | 1 |

#### Praxisaufgaben (Hands-on Lab)
Dieses Modul hat kein technisches Labor. Alle Fakten zu Zertifikaten stammen von den Herstellerseiten (URL und Abrufdatum angeben); Prüfungsinhalte, Preise und Auslaufdaten sind flüchtig. Der Studienleitfaden zu MS-102 nennt als Auslaufdatum den 30.11.2026: Prüfe den aktuellen Status der Prüfung auf der offiziellen Seite, bevor du sie planst.

1. **Spezialisierungen vergleichen (Lernziel 1; Einheit 12.1):** Bewerte Modern Workplace, Cloud, Netzwerk/Security, Linux/Automation und Virtualisierung nach selbst gewählten Kriterien (Lernaufwand, Nähe zu den Lehrinhalten, Aufgabenvielfalt, Passung zu dir, Zahl passender Inserate aus Modul 1) mit Gewichtung. Die Tabelle zeigt deine Einschätzung, keine Marktdaten; kennzeichne das.
2. **Zertifikate recherchieren und zuordnen (Lernziel 1; Einheiten 12.2 bis 12.5):** Wähle vier Nachweise, je einen aus Microsoft (z. B. AZ-104 oder MS-102), Netzwerk (z. B. CCNA), Linux (z. B. LPIC-1 oder RHCSA) und Virtualisierung/Backup (Hersteller und Nachweis nach Wahl). Erfasse je Nachweis: Prüfungscode, Voraussetzungen, Gültigkeit/Auslaufdatum, Kosten, Prüfungsbereiche, Quelle mit Datum. Ordne die Prüfungsbereiche den Modulen dieses Lehrplans zu (zum Beispiel Cloud-Administration zu Modul 7, Netzwerkgrundlagen zu Modul 2, Linux zu Modul 5) und benenne verbleibende Lücken. **Wichtig:** Die Zuordnung ist deine Einschätzung und keine Zusage, dass dieser Lehrplan für die Prüfung genügt.
3. **Projekt dokumentieren (Lernziel 2; Einheit 12.6):** Wähle zwei deiner Laborergebnisse (z. B. Domänenaufbau aus Modul 3, Wiederherstellungstest aus Modul 8) und schreibe je eine Projektseite: Ziel, Aufbau (Diagrammskizze), Schritte, Ergebnis, Probleme und Lösungen, Erkenntnisse. Struktur: `README.md`, `docs/`, `scripts/`. Prüfe vor jeder Veröffentlichung diese Liste: keine Kennwörter, keine echten Firmen- oder Domänennamen (nur Beispieldomänen wie `lab.example.internal`), keine Mandanten-, Subscription- oder Geräte-IDs, keine privaten oder betrieblichen Adressen.
4. **Arbeitsumfelder vergleichen (Lernziel 2; Einheit 12.7):** Vergleiche IT-Dienstleister/MSP, Unternehmen (Konzern oder KMU) und öffentliche Verwaltung in einer Entscheidungsmatrix: Breite der Technik, Tiefe, Kundenkontakt, Bereitschaftsdienst, Lernchance, Spezialisierungspotenzial. „Kanzlei“ aus der Excel-Vorlage wird als kleiner Betrieb mit einer Ein-Personen-IT gelesen (Annahme). Belege die Einträge mit mindestens vier deiner Inserate aus Modul 1 oder kennzeichne sie als Vermutung.
5. **12- bis 36-Monats-Plan (Lernziel 3; Einheit 12.8):** Erstelle einen Plan nach Quartalen mit Praxis (Lab, Betrieb), Zertifikaten, Projekten und Spezialisierungsentscheidung, Zeitbudget pro Woche, Kosten, Risiken (Prüfung ausgelaufen, Termin verschoben) und einem Review alle drei Monate.
6. **Abgleich mit Modul 1 (Lernziel 3; Einheiten 12.6, 12.8):** Vergleiche die Kompetenzmatrix und den Plan aus Modul 1 mit dem heutigen Stand: Welche Bewertungen haben sich geändert, durch welche Module belegt? Welche Ziele sind neu, welche gestrichen, und warum?

#### Kontrollfragen
1. Warum sind Preise, Prüfungscodes und Auslaufdaten von Zertifikaten immer auf der Herstellerseite zu prüfen?
2. Wodurch erhöhen dokumentierte Homelab-Projekte die Glaubwürdigkeit gegenüber einem Zertifikat allein?
3. Was darf in einer veröffentlichten Projektdokumentation nicht stehen?
4. Welche Kriterien sprechen für einen IT-Dienstleister, welche für ein Unternehmen oder die öffentliche Verwaltung?
5. Wie oft und woran überprüfst du deinen 12- bis 36-Monats-Plan?

---

## C. Hinweise zur Entstehung und Prüfvermerk (12.11.2026)

Dieser Lehrplan wurde aus der Excel-Vorlage „Lehrplan - Weiterbildung IT Systemtechnik.xlsx“ (12 Module, 110 „h“) nach den Kriterien der Grundanweisung (Stand 08.11.2026) umgeschrieben. **Übernommen** aus der Vorlage: Modultitel, Einheiten (8 je Modul) mit Stunden, Prioritäten (außer Modul 5). **Neu geschrieben:** Lernziele, Praxisaufgaben, Kontrollfragen, Laborentwurf, Quellen. **Annahmen:** Stunden der Vorlage sind Unterrichtseinheiten zu 45 Minuten; Laborressourcen (24 GB RAM, 250 GB Speicher); „Kanzlei“ in Einheit 12.7 steht für einen kleinen Betrieb mit Ein-Personen-IT.

**Befunde im Rohmaterial (Fachlektorat, nicht stillschweigend geglättet):**

* Die „Detaillierten Lernziele & Inhalte“ im Blatt „Lehrplan in Modulen“ sind für alle zwölf Module wortgleich und beschreiben keines der Module; sie wurden nicht übernommen.
* Modul 5 hat Priorität 2, obwohl die Module 8, 9 und 10 Linux-Aufgaben enthalten; hier Priorität 1 (Abweichung).
* Die Vorlage verwendet Priorität 1 bis 3; tatsächlich kommen nur 1 und 2 vor.
* Texte der Vorlage ohne Umlaute und mit Tippfehlern („Gerate“ in 4.4); Einheit 11.3 enthält die unklare Formulierung „Passus fuer Vertretung und Recovery“, hier als „Vertretung und Recovery“ gelesen; Einheit 3.1 nennt DHCP, das hier nur Theorie ist.
* Die Vorlage enthält Aussagen zum Marktwert (Einheit 12.1) ohne Quelle; der Lehrplan behandelt sie als Recherche- und Bewertungsaufgabe, nicht als Tatsache.

**Kontrollwerte (Lösungsschlüssel für Dozenten):**

* **Modul 2, Aufgabe 1:** Vier `/26`-Netze mit je 62 Hosts (2⁶ − 2): `192.168.50.0/26` (Hosts `.1` bis `.62`, Broadcast `.63`), `192.168.50.64/26` (`.65` bis `.126`, Broadcast `.127`), `192.168.50.128/26` (`.129` bis `.190`, Broadcast `.191`), `192.168.50.192/26` (`.193` bis `.254`, Broadcast `.255`). `192.168.60.101/24`: Netz `192.168.60.0`, Broadcast `192.168.60.255`; `192.168.50.20` liegt nicht im selben Netz.
* **Modul 2, Aufgabe 2:** (a) Netzzugang (physisch), (b) Internetschicht, (c) Anwendungsschicht (DNS), (d) Transportschicht, (e) Internetschicht, (f) Anwendungsschicht.
* **Modul 2, Aufgabe 4 (Fehlereinbau, Vorschlag, nicht getestet):** (a) auf `CL-W11-01` Standardroute entfernen und mit falschem Gateway neu anlegen (`Remove-NetRoute -DestinationPrefix 0.0.0.0/0`, `New-NetRoute -DestinationPrefix 0.0.0.0/0 -InterfaceAlias NIC-CLI -NextHop 192.168.60.254`); (b) auf `SRV-FS01` `Set-NetIPInterface -InterfaceAlias NIC-CLI -Forwarding Disabled`; (c) auf `SRV-DC01` `Disable-NetFirewallRule -DisplayName "LAB-ICMPv4-In"`. Beobachtung: Mit Fehler (b) ist `192.168.50.20` (die Adresse von `SRV-FS01` selbst) möglicherweise trotzdem erreichbar, `192.168.50.10` nicht; das ist ein Lehrpunkt (nicht bestätigt).
* **Modul 3, Aufgabe 4:** Es gilt der Text von `GPO-Lab-Client-2`, weil die OU `Computer\Test` näher am Computerobjekt liegt als `Computer`. **Aufgabe 5:** Bei Freigabe „Lesen“ und NTFS „Ändern“ gilt effektiv „Lesen“. **Aufgabe 8 (Fehlereinbau):** (a) `Set-DnsClientServerAddress -InterfaceAlias NIC-CLI -ServerAddresses 192.168.50.99` auf `CL-W11-01`; (b) GPO-Verknüpfung von `OU=Computer` auf eine andere OU verlegen; (c) `lab-user01` aus `grp-projekt` entfernen.
* **Modul 6, Aufgabe 3:** 4 × 8 GB = 32 GB Maximum auf 24 GB physisch, Faktor etwa 1,33 (die Reserve des Hosts ist nicht abgezogen, der Faktor ist real höher); wenn alle Maximalwerte gleichzeitig gebraucht werden, kommt es zu Speicherdruck und Auslagerung.
* **Modul 7, Aufgabe 3:** Überlappung mit dem Labornetz: `192.168.0.0/16` überlappt alle drei Labornetze, `192.168.50.0/24` überlappt `192.168.50.0/24`; `10.100.0.0/16` und `172.16.0.0/12` überlappen nicht.
* **Modul 8, Aufgabe 3:** (40 − 10) / 0,5 = 60 Tage.
* **Modul 9, Aufgabe 2:** Meldung A zuerst (kritisch, aus dem Internet, bekannte Ausnutzung); Reihenfolge von B und C wird nach Begründung bewertet (B: höhere Schwere, nur intern; C: geringere Schwere, aus dem Internet). **Aufgabe 4:** `lab-hd01` darf `lab-user01` zurücksetzen, `lab-adm01` nicht (Konto liegt außerhalb der delegierten OU).
* **Modul 10, Aufgabe 1 (Vorschlag):** Kennwort zurücksetzen: eher delegieren, kein Skript; 20 neue Benutzer: ja; inaktive Konten löschen: erst Bericht, Löschen nur manuell; Wochenbericht Speicher: ja; einmalige Migration: nein oder nur mit Test; Neustart eines hängenden Dienstes: ja mit Protokoll. Die Begründung zählt.

**Prüfvermerk (Grundanweisung, neun Punkte):**

1. **Stunden und Prioritäten – erfüllt.** 8+9+10+10+9+9+10+9+10+10+8+8 = 110 UE; 10 Module Priorität 1 (93 UE), 2 Module Priorität 2 (17 UE); je Modul stimmen Master-Tabelle, Modulkopf und Summe der acht Einheiten überein (per Skript; Stichprobe Modul 3: 4 × 1,3 + 4 × 1,2 = 10,0).
2. **Labor-Setup – teilweise erfüllt.** Host, Switches, fünf VMs, Adressplan, Internetphasen, Prüfpunkte und Cloud-Zugänge stehen in A.3 mit „erforderlich ab Modul“. Offen: Verfügbarkeit des `Default Switch` auf einem Server-Host, Vorinstallation von OpenSSH-Client und ufw, alle Menüpfade der Cloud-Portale (nicht bestätigt, benannt).
3. **Quellen – teilweise erfüllt.** Alle genannten Verfahren sind in A.2 gelistet (Hyper-V, AD, wbadmin, Intune, Azure, Entra, Zertifikate, RFC 1918); 39 Learn-URLs aus Suchtreffern, Seiten nicht vollständig gelesen. Ohne geprüfte Quelle: VMware, ITIL, Bicep/Terraform, 3-2-1-Regel, Linux-Werkzeuge, Evaluierungslaufzeit von Windows 11, Netplan-Syntax (jeweils so gekennzeichnet).
4. **Widerspruchsfreiheit und Zustände – erfüllt.** Korrigiert bei der Prüfung: Gast-Computernamen waren nicht festgelegt (DNS-Name `dc01` statt `srv-dc01`); jetzt in A.2/A.3 und Modul 3/5 vereinheitlicht. `NIC-INET` für `CL-W11-01` fehlte in Modul 2 (nötig für Phase I-3); ergänzt. Ordner `C:\Temp`/`C:\Backup` fehlten in Modul 8; ergänzt. Zustandskette: Modul 3 braucht `*-M2-Ende`, Modul 5 braucht Modul 3 (DNS), Modul 8 und 9 brauchen Modul 5, Modul 10 braucht Modul 3 und 5, Modul 9 braucht Modul 7 (Cloud-Verzeichnis). Priorität-2-Module (6, 11) werden von keinem Pflichtmodul vorausgesetzt.
5. **Lernziele, Lerneinheiten, Kontrollfragen – erfüllt.** Alle 12 Module haben 3 Lernziele, 8 Einheiten, 5 Kontrollfragen; jedes Lernziel hat mindestens eine Aufgabe, jede Einheit mindestens eine Aufgabe (per Skript über die Markierungen „Lernziel n / Einheit x.y“ geprüft, keine Lücken). Korrigiert: Modul 6 nannte die Linux-VM auch für Aufgabe 6, die sie nicht braucht.
6. **Einschränkungen und Rückbau – erfüllt.** Jede Aufgabe mit Änderung hat Rückbau; Datenträger- und Löschbefehle haben Vorbedingungen (Modul 3.5: `Get-Disk` mit `RAW`; Modul 6/8: Pfadprüfung vor dem Löschen; Modul 10.6: Kontenprüfung vor `Remove-ADOrganizationalUnit`; Modul 7.9: Inhaltsprüfung der Ressourcengruppe). Conditional Access nur im Nur-Bericht-Modus mit getestetem Notfallkonto.
7. **Infrastruktur über eine VM hinaus – erfüllt.** Domänencontroller, Dateiserver als Router, Windows-Client, Linux-Server, Cloud-Client; Routen, Weiterleitung und Rückrouten beschrieben (Modul 2), ufw mit beiden Quellnetzen (Modul 5), Prüfpunkte nur bei ausgeschalteten Domänen-VMs.
8. **Internet, Namen, Dateiwege – erfüllt.** Internet nur in benannten Phasen (I-1, I-2, I-3) und für `CL-W11-02`; Cloud-Ausnahmen mit Dauer und Kosten (A.3, Module 4 und 7); Adressen nach RFC 1918, Domäne `lab.example.internal`; Hostpfade (`D:`) als Beispiele gekennzeichnet; keine Subscription-ID und keine öffentliche Adresse im Dokument.
9. **Befehle und Sicherheit – teilweise erfüllt.** Keine Kennwörter im Dokument, interaktive Eingabe; riskante Schritte (SSH-Kennwort aus, ufw, MFA, Datenträger) mit Vorbedingung und Rückweg. **Kein Befehl wurde ausgeführt**; viele Befehle sind als „nicht bestätigt“ gekennzeichnet.

**Offene Punkte:**

* Alle Befehle, Menüpfade und Ausgabefelder vor dem Kurs im Labor ausführen (nichts davon wurde getestet), besonders die Netplan-Datei, `wbadmin start recovery`, `Set-VMNetworkAdapterVlan` auf privatem Switch, `sc.exe failure`, `auditpol` und die Portal-Schritte in Intune und Azure.
* Ein Kursleiter muss Zeitaufwand der Laboraufgaben erproben; 110 UE einschließlich Labor sind eine Schätzung. Die Installation der Betriebssysteme und die Cloud-Registrierung liegen außerhalb der UE.
* Evaluierungslaufzeiten (Windows Server 180 Tage, Windows 11 Enterprise 90 Tage nicht geprüft) und Zertifikatsstände (MS-102 läuft laut Studienleitfaden am 30.11.2026 aus) vor Kursbeginn prüfen.
* Ob das Cloud-Verzeichnis des Azure-Kontos nach Ablauf des Guthabens für Modul 9, Aufgabe 3 bestehen bleibt, ist nicht bestätigt.
* Zeitpunkt der Module 4, 7 und 9 so planen, dass Intune-Test (30 Tage) und Azure-Guthaben (30 Tage) reichen.

**Paketliste:** Keine LaTeX-Pakete (Markdown-Dokument). Benötigte Software siehe A.3: Hyper-V, Windows Server 2025 Evaluation, Windows 11 Enterprise Evaluation, Ubuntu Server 24.04 LTS, OpenSSH-Client, Windows PowerShell 5.1.
