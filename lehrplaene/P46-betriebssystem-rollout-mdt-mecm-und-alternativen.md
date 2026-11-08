# Lehrplan: Betriebssystem-Rollout (MDT, MECM und Alternativen)

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Windows-Server- und Active-Directory-Grundlagen |
| **Gesamtumfang** | 14 Module, 108 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows ADK mit Windows PE und DISM; PXE-Netzwerkboot mit Windows Deployment Services (WDS); Microsoft Configuration Manager (Betriebssystembereitstellung und Softwareverteilung); Microsoft Deployment Toolkit (MDT, nur als Altumgebung); FOG als Alternative im Überblick; Hyper-V (nur als Laborumgebung) |
| **Thematische Abgrenzung (Out of Scope)** | Intune und Autopilot sind ein eigener Kurs und kommen hier nur als Abgrenzung und Entscheidungshilfe vor (Modul 1 und 13), ohne Übungen. Aufbau und Betrieb von Domain Controller, DNS und DHCP sind Vorkenntnis: Der Domain Controller wird vom Kursleiter vorbereitet, der DHCP-Bereich in Modul 2 nur kurz angelegt. Die Client-Verwaltung nach dem Rollout (Gruppenrichtlinien, BitLocker, Updates) ist ein eigener Kurs (Windows-11-Client-Administration). Keine PKI und kein HTTPS-Betrieb von Configuration Manager, keine hierarchischen Standorte, keine Zertifizierungsvorbereitung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Rollout-Konzepte und Produktlandschaft (Stand 08.11.2026) | 1 | 7 |
| 2 | Laborumgebung und Offline-Beschaffung | 1 | 7 |
| 3 | Windows ADK, Windows PE und DISM | 1 | 9 |
| 4 | Abbild anwenden: Partitionierung, Antwortdatei, Skript | 1 | 8 |
| 5 | Referenzabbild erstellen und pflegen | 1 | 8 |
| 6 | Treiberverwaltung | 1 | 7 |
| 7 | Netzwerkboot mit PXE und WDS | 1 | 9 |
| 8 | Configuration Manager: Aufbau | 1 | 8 |
| 9 | Betriebssystembereitstellung mit Configuration Manager | 1 | 10 |
| 10 | Aufgabensequenzen in der Tiefe | 1 | 9 |
| 11 | Softwareverteilung | 1 | 7 |
| 12 | MDT: Altumgebung lesen und ablösen | 2 | 5 |
| 13 | Alternativen: FOG, Autopilot und Intune im Überblick | 2 | 5 |
| 14 | Fehlersuche | 1 | 9 |
| **Gesamt** | **12 Pflichtmodule, 2 Vertiefungsmodule** | | **108** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (98 UE) vermitteln die Kernkompetenzen. Module mit Priorität 2 (12 und 13, zusammen 10 UE) dienen der Vertiefung und können bei Zeitmangel gekürzt oder als Selbststudium ausgelagert werden. Kein Pflichtmodul setzt ein Modul mit Priorität 2 voraus: Modul 12 liest nur Beispieldateien und verändert das Labor nicht dauerhaft, Modul 13 ist eine Demonstration ohne Zustandsänderung am Labor. Die Zahl von 14 Modulen liegt am oberen Rand der Vorgabe (10 bis 14), weil MDT und Alternativen als eigene kurze Module behandelt werden.*

### 2. Quellen

Alle Angaben zu Microsoft-Produkten stammen aus Suchtreffer-Auszügen von Microsoft Learn vom 08.11.2026 (Seiten nicht vollständig gelesen). Die Produktseite von FOG wurde am 08.11.2026 abgerufen. Aussagen ohne Quelle sind im Text als „nicht bestätigt“ gekennzeichnet.

* **MDT eingestellt:** *Microsoft Deployment Toolkit (MDT) - immediate retirement notice* ([https://learn.microsoft.com/troubleshoot/mem/configmgr/mdt/mdt-retirement](https://learn.microsoft.com/troubleshoot/mem/configmgr/mdt/mdt-retirement), Seite „zuletzt aktualisiert 6. Januar 2026“): MDT erhält keine Updates, Korrekturen und keinen Support mehr; bestehende Installationen laufen weiter; Download-Pakete können entfernt werden. Dazu *Microsoft Deployment Toolkit support lifecycle* ([https://learn.microsoft.com/troubleshoot/windows-server/setup-upgrade-and-drivers/deployment-toolkit-support](https://learn.microsoft.com/troubleshoot/windows-server/setup-upgrade-and-drivers/deployment-toolkit-support)), *MDT release notes* ([https://learn.microsoft.com/intune/configmgr/mdt/release-notes](https://learn.microsoft.com/intune/configmgr/mdt/release-notes): „MDT build 8456“ ist die letzte Version im Download Center) und *MDT known issues* ([https://learn.microsoft.com/intune/configmgr/mdt/known-issues](https://learn.microsoft.com/intune/configmgr/mdt/known-issues)).
* **MDT in Configuration Manager:** *Removed and deprecated features for Configuration Manager* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/changes/deprecated/removed-and-deprecated-cmfeatures](https://learn.microsoft.com/intune/configmgr/core/plan-design/changes/deprecated/removed-and-deprecated-cmfeatures)): Die MDT-Integration ist nicht mehr unterstützt; zuerst angekündigt Dezember 2024, Support entfernt „im ersten Release nach dem 10. Oktober 2025“.
* **WDS veraltet:** *Windows Deployment Services (WDS) boot.wim support* ([https://learn.microsoft.com/windows/deployment/wds-boot-support](https://learn.microsoft.com/windows/deployment/wds-boot-support)) und *Windows message center* ([https://learn.microsoft.com/windows/release-health/windows-message-center](https://learn.microsoft.com/windows/release-health/windows-message-center), Eintrag vom 24.09.2026): WDS wird ab der Betriebssystemversion nach Windows Server 2025 abgekündigt (Rolle, Dienste, Verwaltungswerkzeuge, WDS-PXE). Die verlinkte Ankündigung auf support.microsoft.com (`…/windows-deployment-services-deprecation-in-the-next-windows-server-release`) wurde **nicht gelesen**. Ebenso nicht gelesen: die Härtungsanleitung zu CVE-2026-0386 („hands-free deployment“ ab dem Release April 2026 standardmäßig nicht mehr unterstützt). Dazu *Features removed or no longer developed in Windows Server* ([https://learn.microsoft.com/windows-server/get-started/removed-deprecated-features-windows-server](https://learn.microsoft.com/windows-server/get-started/removed-deprecated-features-windows-server)).
* **Configuration Manager, Versionen und Support:** *Updates and servicing for Configuration Manager* ([https://learn.microsoft.com/intune/configmgr/core/servers/manage/updates](https://learn.microsoft.com/intune/configmgr/core/servers/manage/updates)): Versionen 2609, 2603, 2509 mit Verfügbarkeits- und Supportende-Datum. *What's new in version 2609* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/changes/whats-new-version-2609](https://learn.microsoft.com/intune/configmgr/core/plan-design/changes/whats-new-version-2609)) und *Summary of changes in version 2609* ([https://learn.microsoft.com/intune/configmgr/hotfix/2609/2377842](https://learn.microsoft.com/intune/configmgr/hotfix/2609/2377842)).
* **Kompatibilität:** *Support for Windows 11 in Configuration Manager* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/support-for-windows-11](https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/support-for-windows-11)), *Support for the Windows ADK in Configuration Manager* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/support-for-windows-adk](https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/support-for-windows-adk)), *Supported operating systems for site system servers* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/supported-operating-systems-for-site-system-servers](https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/supported-operating-systems-for-site-system-servers)), *Supported SQL Server versions* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/support-for-sql-server-versions](https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/support-for-sql-server-versions)), *Recommended hardware* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/recommended-hardware](https://learn.microsoft.com/intune/configmgr/core/plan-design/configs/recommended-hardware)).
* **Windows ADK und WinPE:** *Download and install the Windows ADK* ([https://learn.microsoft.com/windows-hardware/get-started/adk-install](https://learn.microsoft.com/windows-hardware/get-started/adk-install)): ADK 10.1.26100.9457 (September 2026) und ADK 10.1.28000.3481 (Oktober 2026); *Windows PE (WinPE)* ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/winpe-intro](https://learn.microsoft.com/windows-hardware/manufacture/desktop/winpe-intro)).
* **DISM und Abbildformate:** *DISM Image Management Command-Line Options* ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14](https://learn.microsoft.com/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14)), *Capture and apply a Windows image using a single .WIM file* ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim](https://learn.microsoft.com/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim)), *Append, apply, and export volume images* ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/append-a-volume-image-to-an-existing-image-using-dism--s14](https://learn.microsoft.com/windows-hardware/manufacture/desktop/append-a-volume-image-to-an-existing-image-using-dism--s14)), *WIM vs. VHD vs. FFU* ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/wim-vs-ffu-image-file-formats](https://learn.microsoft.com/windows-hardware/manufacture/desktop/wim-vs-ffu-image-file-formats)).
* **PXE und Betriebssystembereitstellung mit Configuration Manager:** *Install and configure distribution points* ([https://learn.microsoft.com/intune/configmgr/core/servers/deploy/configure/install-and-configure-distribution-points](https://learn.microsoft.com/intune/configmgr/core/servers/deploy/configure/install-and-configure-distribution-points)), *Infrastructure requirements for OS deployment* ([https://learn.microsoft.com/intune/configmgr/osd/plan-design/infrastructure-requirements-for-operating-system-deployment](https://learn.microsoft.com/intune/configmgr/osd/plan-design/infrastructure-requirements-for-operating-system-deployment)), *Use PXE to deploy Windows over the network* ([https://learn.microsoft.com/intune/configmgr/osd/deploy-use/use-pxe-to-deploy-windows-over-the-network](https://learn.microsoft.com/intune/configmgr/osd/deploy-use/use-pxe-to-deploy-windows-over-the-network)), *Troubleshooting PXE boot issues* ([https://learn.microsoft.com/troubleshoot/mem/configmgr/os-deployment/troubleshoot-pxe-boot](https://learn.microsoft.com/troubleshoot/mem/configmgr/os-deployment/troubleshoot-pxe-boot)), *Advanced troubleshooting for PXE boot issues* ([https://learn.microsoft.com/troubleshoot/mem/configmgr/os-deployment/advanced-troubleshooting-pxe-boot](https://learn.microsoft.com/troubleshoot/mem/configmgr/os-deployment/advanced-troubleshooting-pxe-boot)), *Understand PXE boot* ([https://learn.microsoft.com/troubleshoot/mem/configmgr/os-deployment/understand-pxe-boot](https://learn.microsoft.com/troubleshoot/mem/configmgr/os-deployment/understand-pxe-boot)), *Customize boot images* ([https://learn.microsoft.com/intune/configmgr/osd/get-started/customize-boot-images](https://learn.microsoft.com/intune/configmgr/osd/get-started/customize-boot-images)), *Task sequence steps* ([https://learn.microsoft.com/intune/configmgr/osd/understand/task-sequence-steps](https://learn.microsoft.com/intune/configmgr/osd/understand/task-sequence-steps)), *Task sequence variables* ([https://learn.microsoft.com/intune/configmgr/osd/understand/task-sequence-variables](https://learn.microsoft.com/intune/configmgr/osd/understand/task-sequence-variables)), *About log files* ([https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files](https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files)).
* **Configuration-Manager-Labor:** *Set up a Configuration Manager lab* ([https://learn.microsoft.com/intune/configmgr/core/get-started/set-up-your-lab](https://learn.microsoft.com/intune/configmgr/core/get-started/set-up-your-lab)). Die Seite nennt noch Windows Server 2012 R2 und SQL Server 2012 und ist **veraltet**; nur die Abfolge der Installationsschritte (Standortcode `LAB`, eigenständiger Primärstandort, SQL-Anforderungen wie Sortierung `SQL_Latin1_General_CP1_CI_AS`, Port 4022 und 1433) wird übernommen.
* **FOG:** Herstellerseite ([https://fogproject.org/download.php](https://fogproject.org/download.php), abgerufen 08.11.2026): aktuelle Version 1.6.0.14, „released November 02, 2026“; Serverinstallation nur unter Linux; Internetverbindung während der Installation nötig.
* **Eigene Prüfungen (Sandbox, nicht Windows):** Siehe A.3 und Abschnitt C.

**Zum Namen „MECM“ und zum Produktstand (Stand 08.11.2026, Unsicherheit gekennzeichnet):** Die aktuelle Learn-Dokumentation spricht von *Configuration Manager* bzw. *Microsoft Configuration Manager (current branch)* und liegt unter dem Pfad `intune/configmgr`. Die Abkürzung MECM stammt vom früheren Namen *Microsoft Endpoint Configuration Manager*, der in einzelnen Seiten (z. B. der ADK-Seite) noch vorkommt; davor hieß das Produkt SCCM / System Center Configuration Manager. **Datum der Umbenennungen nicht geprüft.** Der Lehrplan verwendet „Configuration Manager“ und nennt MECM nur als Suchbegriff.

### 3. Labor-Setup & Rahmenbedingungen

**Was geprüft wurde und was nicht:** Es stand keine Windows-Umgebung zur Verfügung. **Alle Windows-Befehle (DISM, diskpart, PowerShell, wdsutil, sysprep) in diesem Lehrplan wurden nicht ausgeführt.** Befehle und Optionen, die Microsoft Learn belegt (siehe Quellen), sind nicht besonders markiert; alles andere ist als „nicht bestätigt“ gekennzeichnet und vor dem Kurs im Labor zu prüfen. In einer Linux-Sandbox wurden getestet: das Verhalten von WIM-Abbildern mit dem Linux-Werkzeug `wimlib-imagex` (Capture, Append, Apply, Export, Einfachspeicherung gleicher Dateien; das ist **kein** DISM, die Ergebnisse gelten als Größenordnung), das TFTP-Verhalten (Blockgröße, Paketzahl) gegen `dnsmasq` 2.91, die Syntax einer Proxy-DHCP-Konfiguration (`dnsmasq --test`), die Wohlgeformtheit der Beispiel-XML-Dateien (`xmllint`, **keine** Prüfung gegen das Windows-Schema) und alle Rechenwerte per Python-Skript.

* **Hyper-V-Host:** Arbeitsplatzrechner oder Server mit Windows und aktiviertem Hyper-V, mindestens 32 GB Arbeitsspeicher (VM-Summe 24 GB plus 8 GB Reserve für den Host, Annahme des Lehrplans) und 400 GB freiem Speicher (Summe der maximalen Größen aller virtuellen Festplatten 388 GB, dynamisch angelegt). Alle vier VMs laufen in den Modulen 9 bis 11 gleichzeitig. Der Host braucht **einmalig** Internet für die Beschaffung (siehe unten).
* **Virtueller Switch:** Ein **privater** Switch `vSwitch-Lab` ohne Verbindung zum Heim- oder Produktivnetz. Alle VMs hängen ausschließlich daran. Es gibt im Labor **kein Internet**. Wichtig für PXE: Auf dem Switch läuft nur der DHCP-Server auf `DC01`, damit keine fremden DHCP-Antworten auftreten.
* **VM „DC01“ (vom Kursleiter vorbereitet):** Generation 2, 2 vCPUs, 4 GB RAM, 60 GB, Windows Server (Evaluation; Version legt der Kursleiter fest und notiert sie), Domänencontroller mit DNS für `lab.example.internal` (NetBIOS `LAB`), Adresse `10.70.0.10/24`. Organisationseinheiten `OU=Rollout` mit den Unter-OUs `Clients` und `Dienstkonten`; Konten `LAB\labadmin` (Domänenadministrator), `LAB\svc-osd-read` (nur Leserechte auf die Freigabe `Images`) und `LAB\svc-osd-join` (darf in `OU=Clients,OU=Rollout` Computerkonten anlegen, delegiert); Kennwörter vergibt der Kursleiter. Prüfpunkt `DC01-Basis`.
* **VM „DEPLOY01“ (von den Lernenden in Modul 2 gebaut):** Generation 2, 4 vCPUs, 12 GB RAM (obere Grenze der von Learn genannten Laborempfehlung für Standort- und Datenbankserver: 2 bis 4 Kerne, 8 bis 12 GB, 100 GB), Systemplatte 100 GB, zweite virtuelle Festplatte 100 GB (Laufwerk `E:`, enthält Abbilder, Treiber, `RemoteInstall`, Inhaltsbibliothek). Windows Server 2025 (Evaluation, mit Desktopdarstellung; als Standortserver laut Learn unterstützt), Mitglied der Domäne, Adresse `10.70.0.20/24`.
* **VMs „CL01“ und „CL02“ (leer, von den Lernenden in Modul 2 angelegt):** Generation 2, 2 vCPUs, 4 GB RAM, 64 GB (dynamisch), Secure Boot aktiv, virtuelles TPM aktiv, **ohne Betriebssystem**, Adressen per DHCP. Als Windows 11 wird eine Enterprise-Evaluation benutzt (Version legt der Kursleiter fest; passend zu ADK 10.1.26100.9457 sind 26H2, 25H2 und 24H2).
* **Beschaffung (Host mit Internet, vor dem Kurs):** ISO von Windows Server 2025 und Windows 11 Enterprise (Evaluation); Windows ADK 10.1.26100.9457 und das zugehörige Windows-PE-Add-on (September 2026; Abschnitt „Download the Windows ADK for installation on a separate computer“ im ADK-Setup, nicht bestätigt); SQL Server 2022 (Evaluation) und Microsoft ODBC Driver for SQL Server; Installationsmedium von Configuration Manager (Evaluation oder Testversion, **Verfügbarkeit der aktuellen Version 2609 als Evaluation nicht bestätigt**) samt den „Prerequisite Downloads“ (der Setup-Assistent bietet „Download required files“ an, nach der Learn-Laborseite); für Modul 5 ein monatliches kumulatives Windows-Update als `.msu` aus dem Microsoft Update Catalog (genaue Bezeichnung nicht bestätigt). Der Transport in die VMs läuft über virtuelle DVD-Laufwerke (ISO-Dateien liegen auf dem Host in `D:\ISO`) und über PowerShell Direct (`New-PSSession -VMName …` und `Copy-Item -ToSession` bzw. `-FromSession`, für beide Richtungen, ohne Netzwerk zwischen Host und VM, nicht bestätigt); `Copy-VMFile` überträgt nur vom Host zum Gast (nicht bestätigt).
* **Namens- und Adressplan:**

| Bezeichnung | Name / Adresse | Verwendet in |
| :--- | :--- | :--- |
| Lab-Netz | `10.70.0.0/24` (RFC 1918), kein Gateway | Modul 2 bis 14 |
| Domain Controller, DNS, DHCP | `DC01`, `10.70.0.10` | Modul 2 bis 14 |
| Deployment-Server | `DEPLOY01`, `10.70.0.20` | Modul 2 bis 14 |
| DHCP-Bereich | `10.70.0.100` bis `10.70.0.199` (100 Adressen) | Modul 2 bis 14 |
| Clients | `CL01`, `CL02` (DHCP) | Modul 2 bis 14 |
| Domäne | `lab.example.internal` | Modul 2 bis 14 |
| Freigabe für Abbilder | `\\DEPLOY01\Images` (Ordner `E:\Images`) | Modul 3 bis 7 |
| Standortcode Configuration Manager | `LAB` | Modul 8 bis 14 |

* **Prüfpunkte (Hyper-V-Checkpoints):** `DC01-Basis` (Kursleiter), `DEPLOY01-M2-Ende`, `CL01-leer` und `CL02-leer` (Modul 2), `CL02-M5-vor-Sysprep` (Modul 5), `DEPLOY01-M6-Ende` (Modul 6, danach Basis für Modul 7 **und** 8), `DC01-M8-Ende` und `DEPLOY01-M8-Ende` (Modul 8, nur gemeinsam zurücksetzen), `DEPLOY01-M11-Ende` (Modul 11). **Wichtig:** Modul 7 (WDS) wird nach der Übung durch Zurücksetzen auf `DEPLOY01-M6-Ende` zurückgebaut, damit Modul 8 mit dem Configuration-Manager-PXE-Responder startet; Learn rät, WDS bei einem PXE-fähigen Verteilungspunkt nicht vorher zu konfigurieren. Die in den Modulen 3 bis 6 erzeugten Dateien auf `E:` bleiben dabei erhalten, weil `E:` im Prüfpunkt enthalten ist. Wird ein Domänenmitglied (`DEPLOY01`) auf einen älteren Prüfpunkt zurückgesetzt, kann das Kennwort des Computerkontos von dem der Domäne abweichen (Computerkonten wechseln standardmäßig alle 30 Tage das Kennwort, nicht bestätigt); innerhalb weniger Tage ist das unkritisch, sonst `Test-ComputerSecureChannel -Repair`. `DC01` wird nach Modul 8 nicht allein zurückgesetzt. Ein Prüfpunkt ist keine Datensicherung.
* **Vom Kursleiter bereitzustellen:** `DC01` mit Prüfpunkt, Konten und Delegation (siehe oben), ISO-Dateien und Offline-Medien, Kennwörter, Kursleiter-Skript mit Fehlereinbau für Modul 14, und eine **Ausweich-VM**: `DEPLOY01-CM-fertig` (exportierte VM mit installiertem Standort nach Modul 8), damit die Module 9 bis 11 und 14 stattfinden können, falls die Installation in Modul 8 scheitert oder zu lange dauert.
* **Nicht möglich im Labor (ohne Internet):** Windows Update und WSUS-Synchronisation, Aktivierung, Bezug von Treibern der Hersteller, Download von Software, der Cloud-Teil von Configuration Manager (Cloud Management Gateway, Intune-Anbindung). Die Module behandeln das nur auf Konzeptebene. **Ausnahme FOG (Modul 13):** Der Installer von FOG braucht laut Herstellerseite Internet; deshalb ist FOG hier eine Demonstration des Kursleiters mit einer eigenen, getrennten VM, nicht Teil des privaten Labors.
* **Grundsatz Sicherheit:** Kennwörter stehen nie in Dokumenten dieses Kurses; Beispieldateien enthalten Platzhalter wie `PLATZHALTER-vom-Kursleiter`. Alle Konten im Labor existieren nur im Labor.

## B. Detaillierter Modulaufbau

### Modul 1: Rollout-Konzepte und Produktlandschaft (Stand 08.11.2026)
* **Priorität:** 1
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rollout-Szenarien (Neuinstallation, Refresh, Replace, In-place-Upgrade) und Abbildarten (schlank, voll, hybrid) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende den Status von MDT, WDS, Configuration Manager, Windows ADK und FOG mit Datum und Quelle wiedergeben und Unsicherheit kennzeichnen.
  * Nach Abschluss dieses Moduls kann der Lernende Supportzeiträume berechnen und eine passende Kombination aus ADK-, Configuration-Manager- und Windows-11-Version wählen.
  * Nach Abschluss dieses Moduls kann der Lernende für ein Szenario einen Rolloutweg begründet wählen und einen Rückfallplan nennen.
* **Voraussetzungen:** Windows-Server- und Active-Directory-Grundlagen; keine Laborumgebung nötig (Rechercheaufgaben am Host mit Internet).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Rollout-Szenarien und Abbildarten (schlank, voll, hybrid; manuell, Light-Touch, Zero-Touch) | 2 |
| 1.2 | Produktlandschaft mit Stand: MDT, WDS, Configuration Manager, ADK, FOG; Abgrenzung Autopilot und Intune | 2 |
| 1.3 | Supportzeiträume und Versionsmatrix (Configuration Manager, ADK, Windows 11) | 2 |
| 1.4 | Rollout planen: Bestand, Standardisierung, Pilotgruppe, Rückfallplan | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Begriffe zuordnen (Lernziel 1, Einheit 1.1):** Ordne diese Situationen einem Szenario zu und begründe: (a) neues Gerät ohne Betriebssystem; (b) das Gerät bleibt beim Benutzer, Windows wird neu installiert, Daten werden gesichert und zurückgespielt; (c) ein altes Gerät wird durch ein neues ersetzt, die Daten wandern mit; (d) Windows 10 wird auf Windows 11 angehoben, ohne die Platte zu löschen; (e) ein Abbild enthält nur Windows, die Programme kommen nach der Installation; (f) ein Abbild enthält Windows und alle Programme. Die Begriffe „New computer“, „Refresh“ und „Replace“ sind aus der Configuration-Manager-Welt bekannt (Schreibweise in der Konsole nicht bestätigt).
2. **Produktstatus mit Stand (Lernziel 2, Einheit 1.2):** Fülle diese Tabelle für MDT, WDS, Configuration Manager (aktuelle Version), Windows ADK (aktuelle Version) und FOG aus: Status, Datum, Quelle (URL), Sicherheit der Aussage („belegt“ oder „nicht bestätigt“). Nutze nur die Quellen aus A.2 und prüfe am Host mit Internet, ob sich seit 08.11.2026 etwas geändert hat. Wenn ja, gilt das neue Datum, und der Lehrplan ist an der Stelle zu korrigieren (Meldung an den Kursleiter).
3. **Supportrechnung (Lernziel 3, Einheit 1.3):** (a) Berechne für Configuration Manager 2509, 2603 und 2609 die Supportdauer in Monaten und die Resttage ab dem 08.11.2026 (Daten aus A.2). (b) Ein Rollout beginnt am 01.03.2027 und soll 12 Monate laufen. Welche Versionen sind am Ende noch unterstützt? (c) Wähle für diese Version das Windows ADK und sage, ob Windows 11 26H2 als Client unterstützt wird. (d) Warum ist das ADK vom Oktober 2026 (10.1.28000.3481) hier keine Wahl?
4. **Rolloutweg wählen (Lernziel 4, Einheit 1.4):** Wähle für drei Szenarien einen Weg (manuell mit WinPE und Skript, Configuration-Manager-Betriebssystembereitstellung, Autopilot/Intune als eigener Kurs): (A) Praxis mit 8 Geräten und einem kleinen Server; (B) Standort mit 300 Geräten, Windows Server und Active Directory vorhanden, keine Cloud-Verwaltung; (C) Unternehmen mit Cloud-Konten und Heimarbeitsplätzen ohne Standort-Server. Nenne je Szenario einen Rückfallplan und eine Pilotgruppe.

#### Kontrollfragen
1. (1.1) Was unterscheidet ein schlankes von einem vollen Abbild? Nenne je einen Vorteil und einen Nachteil.
2. (1.2) Was bedeutet „MDT ist eingestellt“ für bestehende Installationen, und was ist laut Learn in Configuration-Manager-Aufgabensequenzen zu tun?
3. (1.2) Was ist an WDS „abgekündigt“, was funktioniert laut Learn weiterhin, und was ist bei Windows 11 blockiert?
4. (1.3) Wofür steht „10.1.26100.9457“, und warum nimmt man nicht automatisch das neueste ADK?
5. (1.4) Warum braucht jeder Rollout einen Rückfallplan und eine Pilotgruppe?

---

### Modul 2: Laborumgebung und Offline-Beschaffung
* **Priorität:** 1
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Laborarchitektur erklären und den Beschaffungsbedarf für ein Labor ohne Internet planen und berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende einen privaten Switch, Generation-2-VMs mit Secure Boot und virtuellem TPM sowie Prüfpunkte in Hyper-V anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende `DEPLOY01` installieren, in die Domäne aufnehmen und eine Datenplatte samt Freigabe einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende einen DHCP-Bereich auf `DC01` anlegen und prüfen.
* **Voraussetzungen:** Modul 1; Hyper-V-Host mit Beschaffungsmedien (siehe A.3); `DC01` vom Kursleiter vorbereitet.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Laborarchitektur, Ressourcenplanung, Beschaffung ohne Internet | 2 |
| 2.2 | Hyper-V: privater Switch, Generation-2-VMs, Firmware, Prüfpunkte | 2 |
| 2.3 | `DEPLOY01`: Installation, Domänenbeitritt, Datenplatte, Freigabe `Images` | 2 |
| 2.4 | DHCP-Bereich auf `DC01` und Namensplan | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Beschaffungsliste und Ressourcen (Lernziel 1, Einheit 2.1):** Erstelle aus A.3 eine Liste aller Dateien (Name, Version, Quelle, Medium für den Transport in die VM). Berechne die Summe des VM-Arbeitsspeichers, den Mindestbedarf des Hosts (mit 8 GB Reserve) und die Summe der maximalen Plattengrößen. Gib an, welche Aussage der Learn-Laborempfehlung (2 bis 4 Kerne, 8 bis 12 GB, 100 GB) zu `DEPLOY01` führt.
2. **Switch und leere VMs (Lernziel 2, Einheit 2.2):** Lege den privaten Switch und die VMs `CL01` und `CL02` an. Vorschlag (Cmdlets aus Erfahrung, **nicht bestätigt**, vor dem Kurs im Labor prüfen):
   ```powershell
   New-VMSwitch -Name "vSwitch-Lab" -SwitchType Private
   New-VM -Name "CL01" -Generation 2 -MemoryStartupBytes 4GB -NewVHDPath "D:\VMs\CL01\CL01.vhdx" -NewVHDSizeBytes 64GB -SwitchName "vSwitch-Lab"
   Set-VMProcessor -VMName "CL01" -Count 2
   Set-VMKeyProtector -VMName "CL01" -NewLocalKeyProtector
   Enable-VMTPM -VMName "CL01"
   Set-VMFirmware -VMName "CL01" -FirstBootDevice (Get-VMNetworkAdapter -VMName "CL01")
   Checkpoint-VM -Name "CL01" -SnapshotName "CL01-leer"
   ```
   Wiederhole für `CL02`. Prüfe mit `Get-VMFirmware`, ob Secure Boot aktiv ist, und notiere die Startreihenfolge. Die Platten sind „dynamisch“ (Standard bei `New-VM -NewVHDPath`, nicht bestätigt).
3. **DEPLOY01 bauen (Lernziel 3, Einheit 2.3):** Installiere Windows Server 2025 (Evaluation) in einer Generation-2-VM (4 vCPUs, 12 GB, 100 GB), vergib `10.70.0.20/24` mit DNS `10.70.0.10`, nenne den Server `DEPLOY01` und nimm ihn in `lab.example.internal` auf. Hänge eine zweite virtuelle Festplatte (100 GB) an, initialisiere sie als GPT, formatiere sie mit NTFS als `E:` und lege `E:\Images` an. Gib den Ordner als `Images` frei (Lesen für `LAB\svc-osd-read`, Vollzugriff für `LAB\labadmin`), zum Beispiel mit `New-SmbShare -Name Images -Path E:\Images -ReadAccess "LAB\svc-osd-read" -FullAccess "LAB\labadmin"` (nicht bestätigt) und prüfe zusätzlich die NTFS-Rechte. Prüfe zuletzt den Transportweg Host und VM mit PowerShell Direct in beiden Richtungen (`$s = New-PSSession -VMName DEPLOY01 -Credential LAB\labadmin`, `Copy-Item -ToSession $s -Path D:\ISO\test.txt -Destination E:\Images\`, `Copy-Item -FromSession $s -Path E:\Images\test.txt -Destination D:\ISO\test-zurueck.txt`; nicht bestätigt). Lege den Prüfpunkt `DEPLOY01-M2-Ende` an.
4. **DHCP (Lernziel 4, Einheit 2.4):** Richte auf `DC01` die DHCP-Rolle ein und lege einen aktiven Bereich `10.70.0.100` bis `10.70.0.199`, Maske `255.255.255.0`, DNS-Server `10.70.0.10`, DNS-Domäne `lab.example.internal` an; kein Standardgateway (privates Netz). Mögliche Cmdlets (nicht bestätigt): `Install-WindowsFeature DHCP -IncludeManagementTools`, `Add-DhcpServerInDC`, `Add-DhcpServerv4Scope`, `Set-DhcpServerv4OptionValue`. Prüfe mit `Get-DhcpServerv4Scope`; die Vergabe an einen Client wird in Modul 3 geprüft. Berechne, wie viele nutzbare Adressen des /24-Netzes außerhalb des Bereichs bleiben.

#### Kontrollfragen
1. (2.1) Warum bleibt das Labor ohne Internet, und welche Folge hat das für die Beschaffung?
2. (2.2) Warum sind die Clients Generation-2-VMs, und was bedeutet das für Startart und Firmware?
3. (2.2) Was unterscheidet einen Prüfpunkt von einer Datensicherung?
4. (2.3) Warum liegen die Abbilder auf einer eigenen Platte `E:`?
5. (2.4) Wie viele Adressen haben der Bereich und der Rest des /24-Netzes, und warum liegt `DEPLOY01` außerhalb des Bereichs?

---

### Modul 3: Windows ADK, Windows PE und DISM
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aufgabe von ADK, Windows PE und Windows-PE-Add-on erklären und die passende ADK-Version begründen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Windows-PE-Medium bauen, um optionale Komponenten erweitern und in einer VM starten.
  * Nach Abschluss dieses Moduls kann der Lernende mit DISM ein Abbild untersuchen, mounten und exportieren.
  * Nach Abschluss dieses Moduls kann der Lernende WIM, VHDX und FFU unterscheiden und die Einfachspeicherung gleicher Dateien in einer WIM erklären.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | ADK und Windows-PE-Add-on: Aufbau, Versionswahl, Installation | 2 |
| 3.2 | Windows-PE-Medium bauen, optionale Komponenten, Start in der VM | 3 |
| 3.3 | DISM: Abbildinformationen, Mounten, Exportieren | 2 |
| 3.4 | Abbildformate WIM, VHDX, FFU; Einfachspeicherung | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **ADK installieren und Version begründen (Lernziel 1, Einheit 3.1):** Übertrage die Offline-Medien mit PowerShell Direct nach `DEPLOY01` und installiere das ADK 10.1.26100.9457 mit der Funktion „Deployment Tools“ (laut Learn das Minimum für WinPE-Medien) und danach das Windows-PE-Add-on. Notiere die Versionen. Fülle diese Tabelle aus und begründe: Ziel Windows 11 26H2, Ziel Windows 11 25H2, Gerät mit Windows 11 26H1 (nur vorinstalliert auf neuen Geräten): welches ADK, und ist es mit Configuration Manager 2609 laut Matrix unterstützt?
2. **WinPE bauen und starten (Lernziel 2, Einheit 3.2):** Öffne die „Deployment and Imaging Tools Environment“ (Name nicht bestätigt) und erzeuge ein Arbeitsverzeichnis, mounte das Boot-Abbild, füge optionale Komponenten hinzu (mindestens `WinPE-WMI`, `WinPE-NetFx` und `WinPE-PowerShell`; Dateinamen nicht bestätigt, die Reihenfolge der Abhängigkeiten ist der Referenzseite „WinPE optional components“ zu entnehmen), speichere und erzeuge ein ISO:
   ```cmd
   copype amd64 E:\WinPE\amd64
   Dism /Mount-Image /ImageFile:"E:\WinPE\amd64\media\sources\boot.wim" /Index:1 /MountDir:"E:\WinPE\amd64\mount"
   Dism /Image:"E:\WinPE\amd64\mount" /Add-Package /PackagePath:"<ADK-Pfad>\Windows Preinstallation Environment\amd64\WinPE_OCs\WinPE-WMI.cab"
   Dism /Unmount-Image /MountDir:"E:\WinPE\amd64\mount" /Commit
   MakeWinPEMedia /ISO E:\WinPE\amd64 E:\Images\WinPE-Basis.iso
   ```
   (`copype`, `MakeWinPEMedia` und die Pfade aus Erfahrung, **nicht bestätigt**; die Platzhalter in `<…>` sind zu ersetzen.) Übertrage das ISO mit `Copy-Item -FromSession` auf den Host (`D:\ISO\WinPE-Basis.iso`), füge `CL01` ein virtuelles DVD-Laufwerk hinzu (`Add-VMDvdDrive -VMName CL01 -Path D:\ISO\WinPE-Basis.iso`), setze das DVD-Laufwerk als erstes Startgerät (`Set-VMFirmware -VMName CL01 -FirstBootDevice (Get-VMDvdDrive -VMName CL01)`; beides nicht bestätigt), starte und prüfe in WinPE mit `ipconfig`, ob `CL01` eine Adresse aus `10.70.0.100` bis `199` hat. Prüfe auf `DC01` mit `Get-DhcpServerv4Lease -ScopeId 10.70.0.0`, ob die Vergabe erscheint. Startet das ISO bei aktivem Secure Boot nicht, prüfe die Secure-Boot-Vorlage der VM (Ursache nicht bestätigt) und dokumentiere die Beobachtung.
3. **Abbild untersuchen und exportieren (Lernziel 3, Einheit 3.3):** Hänge die ISO von Windows 11 Enterprise (Evaluation) an `DEPLOY01`. Lies mit `Dism /Get-ImageInfo /ImageFile:<Laufwerk>:\sources\install.wim` die Editionen und Indizes aus (liegt statt `install.wim` eine `install.esd` vor, gilt der Befehl entsprechend, nicht bestätigt). Exportiere die Enterprise-Edition mit `Dism /Export-Image /SourceImageFile:<…> /SourceIndex:<n> /DestinationImageFile:E:\Images\W11-ENT-Basis.wim` und vergleiche die Größen.
4. **Einfachspeicherung testen (Lernziel 4, Einheit 3.4):** Lege die Ordner `E:\Test\s1` und `E:\Test\s2` an und erzeuge **Zufallsdateien** (nicht mit `fsutil file createnew`, das nur Nullbytes schreibt; gleich große Nulldateien wären untereinander Duplikate und verfälschen den Test):
   ```powershell
   $b = New-Object byte[] 20000000; (New-Object System.Random).NextBytes($b); [IO.File]::WriteAllBytes("E:\Test\s1\common.bin", $b)
   Copy-Item "E:\Test\s1\common.bin" "E:\Test\s2\common.bin"
   $b = New-Object byte[] 5000000; (New-Object System.Random).NextBytes($b); [IO.File]::WriteAllBytes("E:\Test\s1\u1.bin", $b)
   $b = New-Object byte[] 5000000; (New-Object System.Random).NextBytes($b); [IO.File]::WriteAllBytes("E:\Test\s2\u2.bin", $b)
   ```
   Erfasse `s1` und `s2` je in eine eigene WIM-Datei und danach beide als Index 1 und 2 in **eine** WIM-Datei (`Dism /Capture-Image … /Compress:none`, dann `Dism /Append-Image …`). Vergleiche die Dateigrößen und erkläre den Unterschied.

#### Kontrollfragen
1. (3.1) Warum ist Windows PE seit Windows 10, Version 1809, ein Add-on zum ADK?
2. (3.2) Was geschieht beim Start von Windows PE mit `startnet.cmd` und `wpeinit` (Ablauf nicht bestätigt), und warum bekommt `CL01` danach eine Adresse?
3. (3.3) Was unterscheidet Index und Name in der Ausgabe von `/Get-ImageInfo`, und warum exportiert man eine Edition, statt die ganze Datei zu kopieren?
4. (3.4) Welche der Formate WIM, VHDX und FFU sind dateibasiert, welche sektorbasiert, und welche lassen sich laut Learn auf kleinere Datenträger anwenden?
5. (3.4) Warum würde der Test mit Nullbytes ein falsches Ergebnis liefern?

---

### Modul 4: Abbild anwenden: Partitionierung, Antwortdatei, Skript
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine UEFI/GPT-Partitionierung mit `diskpart` erstellen und jede Zeile erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein WIM-Abbild aus Windows PE anwenden und mit `bcdboot` startfähig machen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Antwortdatei den Konfigurationsphasen zuordnen und auf Wohlgeformtheit und Schema prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine skriptgesteuerte Bereitstellung aus Windows PE aufbauen und deren Sicherheitsrisiken benennen.
* **Voraussetzungen:** Modul 3 (Abbild `W11-ENT-Basis.wim`, WinPE-ISO). Hinweis: Die Antwortdatei wurde im Kurs Windows-11-Client-Administration schon einführend behandelt; die Wiederholung ist gewollt, hier mit dem Schwerpunkt Rollout.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Partitionierung mit `diskpart` (UEFI/GPT: EFI, MSR, Windows) | 2 |
| 4.2 | `DISM /Apply-Image`, `bcdboot`, erster Start | 2 |
| 4.3 | Antwortdateien: `Autounattend.xml` (Setup) gegenüber `unattend.xml` (Abbild), Konfigurationsphasen | 2 |
| 4.4 | Skriptgesteuerte Bereitstellung aus WinPE: Freigabe, Anmeldedaten, Sicherheit | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Partitionierung (Lernziel 1, Einheit 4.1):** Vervollständige dieses Skript `CreatePartitions-UEFI.txt` (Zeilen mit `???` ergänzen) und erkläre jede Zeile. Das Skript ist an die Learn-Beispielskripte angelehnt, die Learn für GPT nennt; es wurde nicht ausgeführt.
   ```text
   select disk 0
   clean
   convert gpt
   create partition efi size=300
   format quick fs=fat32 label="System"
   assign letter=S
   create partition msr size=???
   create partition primary
   format quick fs=ntfs label="Windows"
   assign letter=W
   ```
   Prüfe nach dem Lauf mit `list partition` und `list volume`, dass drei Partitionen vorhanden sind. Die Wiederherstellungspartition (WinRE) entfällt in diesem Lab-Layout; die Folgen für Windows RE sind nicht geprüft.
2. **Antwortdatei (Lernziel 3, Einheit 4.3):** Prüfe diese Datei `unattend.xml` (Phasen `specialize` und `oobeSystem`, für den Einsatz nach `Apply-Image`) und ordne jede Einstellung einer Phase zu. Die Datei ist wohlgeformt (mit `xmllint` geprüft); gegen das Windows-Schema wurde sie **nicht** geprüft: Öffne sie im Windows System Image Manager mit einem Katalog der Enterprise-Edition und validiere sie.
   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <unattend xmlns="urn:schemas-microsoft-com:unattend">
     <settings pass="specialize">
       <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
         <ComputerName>CL01</ComputerName>
         <TimeZone>W. Europe Standard Time</TimeZone>
       </component>
     </settings>
     <settings pass="oobeSystem">
       <component name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
         <InputLocale>de-AT</InputLocale>
         <SystemLocale>de-AT</SystemLocale>
         <UILanguage>de-DE</UILanguage>
         <UserLocale>de-AT</UserLocale>
       </component>
       <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
         <OOBE>
           <HideEULAPage>true</HideEULAPage>
           <HideLocalAccountScreen>true</HideLocalAccountScreen>
           <HideOnlineAccountScreens>true</HideOnlineAccountScreens>
           <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
           <ProtectYourPC>3</ProtectYourPC>
         </OOBE>
         <UserAccounts>
           <LocalAccounts>
             <LocalAccount wcm:action="add">
               <Name>labadmin</Name>
               <Group>Administrators</Group>
               <Password><Value>PLATZHALTER-vom-Kursleiter</Value><PlainText>true</PlainText></Password>
             </LocalAccount>
           </LocalAccounts>
         </UserAccounts>
       </component>
     </settings>
   </unattend>
   ```
   Beschreibe zusätzlich in zwei Sätzen, was eine `Autounattend.xml` mit der Phase `windowsPE` (Partitionierung, Abbildauswahl) leistet und warum sie bei `Apply-Image` keine Rolle spielt (Setup läuft dort nicht). Ob die Optionen unter `OOBE` bei Windows 11 in der gewählten Version alle Bildschirme überspringen, ist nicht bestätigt; das Ergebnis ist Teil der Beobachtung.
3. **Abbild anwenden (Lernziel 2, Einheit 4.2):** Lege die Antwortdatei als `E:\Images\scripts\unattend-CL01.xml` ab. Starte `CL01` mit dem WinPE-ISO, führe das `diskpart`-Skript aus, verbinde die Freigabe und wende das Abbild an:
   ```cmd
   net use Z: \\DEPLOY01\Images /user:LAB\svc-osd-read
   diskpart /s Z:\scripts\CreatePartitions-UEFI.txt
   dism /Apply-Image /ImageFile:Z:\W11-ENT-Basis.wim /Index:1 /ApplyDir:W:\
   mkdir W:\Windows\Panther
   copy Z:\scripts\unattend-CL01.xml W:\Windows\Panther\unattend.xml
   bcdboot W:\Windows /s S: /f UEFI
   wpeutil reboot
   ```
   (Der Ort `W:\Windows\Panther\unattend.xml` ist nach Erfahrung eine implizite Suchstelle der Antwortdatei, **nicht bestätigt**. Das Skript `CreatePartitions-UEFI.txt` liegt dazu ebenfalls in `E:\Images\scripts`.) Entferne das ISO, damit die VM von der Platte startet, und beobachte den ersten Start: Wird die Antwortdatei gelesen (kein Konto-Dialog, Computername `CL01`)? Dokumentiere Abweichungen.
4. **Skript und Sicherheit (Lernziel 4, Einheit 4.4):** Schreibe aus den Schritten von Aufgabe 3 ein Skript `E:\Images\scripts\Deploy.cmd` (Anmeldedaten werden **abgefragt**, nicht im Skript gespeichert, zum Beispiel mit `net use Z: \\DEPLOY01\Images /user:LAB\svc-osd-read *`; das Sternchen fragt das Kennwort ab, nicht bestätigt) und rufe es in WinPE per Hand auf. Beantworte schriftlich: Welche drei Risiken entstehen, wenn Kennwort und Skript im Boot-Abbild stehen? Nenne zwei Gegenmaßnahmen.

#### Kontrollfragen
1. (4.1) Wozu dient die MSR-Partition, und warum braucht eine UEFI-Installation eine EFI-Systempartition im Format FAT32?
2. (4.2) Warum reicht `Apply-Image` allein nicht, und was erledigt `bcdboot`?
3. (4.3) In welcher Phase stehen Partitionierung, Computername und Benutzerkonto (windowsPE, specialize, oobeSystem)?
4. (4.3) Warum führt `Apply-Image` die Phase `windowsPE` einer `Autounattend.xml` nicht aus?
5. (4.4) Warum ist ein Kennwort im Boot-Abbild von jedem Gerät im Netz auslesbar, das per PXE starten darf?

---

### Modul 5: Referenzabbild erstellen und pflegen
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Anforderungen an ein schlankes, wiederholbares Referenzabbild nennen und einen Referenzrechner vorbereiten.
  * Nach Abschluss dieses Moduls kann der Lernende ein Referenzabbild mit Sysprep verallgemeinern und mit DISM erfassen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abbild offline mit einem Update versehen, bereinigen und exportieren.
  * Nach Abschluss dieses Moduls kann der Lernende ein Namensschema und einen Wartungsplan für Abbilder festlegen und den Speicherbedarf berechnen.
* **Voraussetzungen:** Modul 4

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Referenzrechner: schlank halten, Änderungen dokumentieren, Prüfpunkt | 2 |
| 5.2 | Sysprep (verallgemeinern) und Erfassen mit DISM | 2 |
| 5.3 | Abbildpflege offline: Update, Bereinigung, Export | 3 |
| 5.4 | Abbild-Lebenszyklus: Namensschema, Aufbewahrung, Test vor Freigabe | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Referenzrechner (Lernziel 1, Einheit 5.1):** Wende `W11-ENT-Basis.wim` mit dem Verfahren aus Modul 4 auf `CL02` an (Computername `REF01` in einer angepassten Antwortdatei, **kein** Domänenbeitritt). Melde dich an, ändere nichts außer einer dokumentierten Einstellung (zum Beispiel Zeitzone), und führe eine Checkliste: keine Updates (kein Internet), keine persönlichen Daten, kein Domänenbeitritt, keine Treiber von Dritten. Lege den Prüfpunkt `CL02-M5-vor-Sysprep` an.
2. **Sysprep und Erfassen (Lernziel 2, Einheit 5.2):** Führe `C:\Windows\System32\Sysprep\sysprep.exe /generalize /oobe /shutdown` aus (Verallgemeinerung nach Learn „Sysprep (Generalize)“; Pfad nicht bestätigt). Starte `CL02` mit dem WinPE-ISO (DVD-Laufwerk und Startreihenfolge wie in Modul 3), ermittle mit `diskpart` und `list volume` den Buchstaben der Windows-Partition (nicht festgelegt, in WinPE oft abweichend von `C:`) und erfasse:
   ```cmd
   net use Z: \\DEPLOY01\Images /user:LAB\labadmin
   Dism /Capture-Image /ImageFile:"Z:\W11-ENT-REF-2026-11-v1.wim" /CaptureDir:<Laufwerk>:\ /Name:"W11-ENT-Referenz"
   Dism /Get-ImageInfo /ImageFile:"Z:\W11-ENT-REF-2026-11-v1.wim"
   ```
   Wende das erfasste Abbild danach mit dem Verfahren aus Modul 4 auf `CL01` an und prüfe, dass `CL01` startet und die Antwortdatei greift. Scheitert Sysprep, setze `CL02` auf `CL02-M5-vor-Sysprep` zurück, lies die Sysprep-Protokolle (Ort nicht bestätigt, nach Erfahrung unter `C:\Windows\System32\Sysprep\Panther`) und notiere die Ursache. Das Zurücksetzen ist nötig, weil die Verallgemeinerung nach Erfahrung nicht rückgängig zu machen ist (nicht bestätigt).
3. **Offline pflegen (Lernziel 3, Einheit 5.3):** Kopiere das Abbild nach `W11-ENT-REF-2026-11-v2.wim`. Mounte es, liste die Pakete, füge das vom Kursleiter gelieferte Update (`.msu`) hinzu, bereinige und speichere:
   ```cmd
   Dism /Mount-Image /ImageFile:"E:\Images\W11-ENT-REF-2026-11-v2.wim" /Index:1 /MountDir:"E:\Mount"
   Dism /Image:"E:\Mount" /Get-Packages
   Dism /Image:"E:\Mount" /Add-Package /PackagePath:"E:\Updates\<Update>.msu"
   Dism /Image:"E:\Mount" /Cleanup-Image /StartComponentCleanup
   Dism /Unmount-Image /MountDir:"E:\Mount" /Commit
   Dism /Export-Image /SourceImageFile:"E:\Images\W11-ENT-REF-2026-11-v2.wim" /SourceIndex:1 /DestinationImageFile:"E:\Images\W11-ENT-REF-2026-11-v2-export.wim"
   ```
   Mount, Unmount und Export sind in Learn belegt; `/Get-Packages`, `/Add-Package` und `/Cleanup-Image` sind es in diesem Auszug nicht (nicht bestätigt; ob das Update zusätzlich einen Wartungsstack braucht, ist nicht bestätigt). Liegt kein Update vor, führe den Zyklus Mount, `/Get-Packages`, Unmount mit `/Discard` aus und beschreibe, was der Unterschied zwischen `/Commit` und `/Discard` ist. Vergleiche die Größen vor und nach dem Export.
4. **Schema und Speicherbedarf (Lernziel 4, Einheit 5.4):** Entwirf ein Namensschema (zum Beispiel `W11-<Edition>-<Version>-<JJJJ-MM>-v<n>.wim`) und einen Wartungsplan (monatlich oder vierteljährlich, Test auf `CL01`, Freigabe, Archivierung). Berechne bei 6 GB je Abbild (Annahme): (a) Speicherbedarf bei monatlicher Pflege ohne Aufräumen nach 12 Monaten; (b) Bedarf, wenn nur die letzten 3 Abbilder behalten werden; (c) ob 3 Abbilder samt `W11-ENT-Basis.wim` auf `E:` (100 GB) passen, wenn ISO-Dateien und Treiber 40 GB belegen.

#### Kontrollfragen
1. (5.1) Welche Dinge gehören in ein schlankes Abbild, und welche werden besser später verteilt?
2. (5.2) Was bewirkt `/generalize`, und warum legt man vorher einen Prüfpunkt an?
3. (5.2) Warum startet man zum Erfassen Windows PE und nicht das laufende Windows?
4. (5.3) Warum exportiert man ein Abbild nach dem Pflegen in eine neue Datei (Erwartung: kleinere, bereinigte Datei; nicht bestätigt)?
5. (5.4) Warum wird jedes neue Abbild vor der Freigabe auf einem Testgerät geprüft?

---

### Modul 6: Treiberverwaltung
* **Priorität:** 1
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Treiberarten (Inbox, Hersteller, Windows PE) unterscheiden und eine Treiberstrategie wählen.
  * Nach Abschluss dieses Moduls kann der Lernende Treiber auf einem laufenden System auflisten und exportieren.
  * Nach Abschluss dieses Moduls kann der Lernende Treiber offline in ein Windows-Abbild und ein Boot-Abbild einfügen.
  * Nach Abschluss dieses Moduls kann der Lernende das Gerätemodell per Abfrage ermitteln und einen passenden Treiberordner auswählen.
* **Voraussetzungen:** Modul 5 (laufendes `CL01` mit Abbild aus Aufgabe 2, Boot-Abbild aus Modul 3)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Treiberarten und Treiberstrategie (Inbox-Treiber, Treiberpakete je Modell, Treiber in Windows PE) | 2 |
| 6.2 | Treiber auflisten und exportieren | 2 |
| 6.3 | Treiber offline einfügen (Windows-Abbild, Boot-Abbild) | 2 |
| 6.4 | Modellerkennung und Treiberauswahl | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Strategie (Lernziel 1, Einheit 6.1):** Entscheide und begründe für drei Fälle, ob der Treiber (a) im Windows-Abbild, (b) im Boot-Abbild, (c) in einem Treiberpaket je Modell oder (d) gar nicht nötig ist: Netzwerkkarte, die Windows PE nicht erkennt; Massenspeicher-Controller, der in Windows PE und im Betriebssystem fehlt; Grafikkarte eines Modells.
2. **Treiber erfassen (Lernziel 2, Einheit 6.2):** Liste auf `CL01` die installierten Treiber (`pnputil /enum-drivers`; `Get-WindowsDriver -Online`) und exportiere die Treiber der Hyper-V-Geräte nach `C:\Export\Virtual-Machine` (`Export-WindowsDriver -Online -Destination …`). Kopiere den Ordner über die Freigabe (`net use Z: \\DEPLOY01\Images /user:LAB\labadmin`) nach `Z:\Drivers\Virtual-Machine`, das ist auf `DEPLOY01` der Ordner `E:\Images\Drivers\Virtual-Machine`. Cmdlets nicht bestätigt. Notiere, wie viele Treiberpakete exportiert wurden.
3. **Treiber einfügen (Lernziel 3, Einheit 6.3):** Mounte `boot.wim` aus Modul 3 und füge **nur** den Treiber der Netzwerkkarte aus dem Export hinzu (Learn rät für Boot-Abbilder zu Netzwerk- und Massenspeichertreibern); prüfe das Ergebnis, speichere und baue das ISO neu:
   ```cmd
   Dism /Mount-Image /ImageFile:"E:\WinPE\amd64\media\sources\boot.wim" /Index:1 /MountDir:"E:\WinPE\amd64\mount"
   Dism /Image:"E:\WinPE\amd64\mount" /Add-Driver /Driver:"E:\Images\Drivers\Virtual-Machine\<NIC-Ordner>" /Recurse
   Dism /Image:"E:\WinPE\amd64\mount" /Get-Drivers
   Dism /Unmount-Image /MountDir:"E:\WinPE\amd64\mount" /Commit
   ```
   (`/Add-Driver` und `/Get-Drivers` nicht bestätigt.) Füge denselben Ordner auch in eine Kopie eines Windows-Abbilds ein. In der VM sind die Treiber bereits im Lieferumfang von Windows; die Übung zeigt das **Verfahren**, ein sichtbarer Funktionsgewinn ist nicht zu erwarten. Lege danach den Prüfpunkt `DEPLOY01-M6-Ende` an.
4. **Modell erkennen (Lernziel 4, Einheit 6.4):** Schreibe eine PowerShell-Funktion, die mit `(Get-CimInstance Win32_ComputerSystem).Model` das Modell liest, daraus den Ordner `E:\Images\Drivers\<Hersteller>\<Modell>` bildet, bei fehlendem Ordner einen Eintrag ins Protokoll schreibt und auf einen Ordner `Allgemein` zurückfällt. Teste sie mit zwei erfundenen Modellnamen (`Modell-X100`, `Modell-Y200`) und auf `CL01` (zu erwartender Wert „Virtual Machine“ bei Hyper-V, nicht bestätigt).

#### Kontrollfragen
1. (6.1) Warum prüft man zuerst, ob der Inbox-Treiber genügt?
2. (6.1) Welche zwei Treiberarten gehören in ein Boot-Abbild, und warum nicht mehr?
3. (6.2) Was unterscheidet `/Online` von `/Image:` bei DISM?
4. (6.3) Warum hilft ein neuer Treiber im Boot-Abbild nicht, wenn das Abbild nicht neu bereitgestellt wird?
5. (6.4) Warum kodiert man den Treiberordner nicht fest ins Skript?

---

### Modul 7: Netzwerkboot mit PXE und WDS
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den PXE-Ablauf (DHCP, Option 60, Proxy-DHCP, Ports 67, 69 und 4011, TFTP) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende TFTP-Transferzeiten aus Blockgröße und Antwortzeit berechnen und Maßnahmen zur Beschleunigung nennen.
  * Nach Abschluss dieses Moduls kann der Lernende WDS mit einem eigenen Windows-PE-Boot-Abbild einrichten, einen Client per PXE starten und den Status von WDS (abgekündigt) einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende das Multicast-Prinzip erklären, Verteilzeiten berechnen und Sicherheitsrisiken des Boot-Abbilds nennen.
* **Voraussetzungen:** Modul 6 (`DEPLOY01` im Zustand `DEPLOY01-M6-Ende`)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | PXE-Ablauf: DHCP, Option 60, Proxy-DHCP, Ports, Boot-Dateien | 2 |
| 7.2 | TFTP: Blockgröße, Antwortzeit, Fenster, Fragmentierung | 2 |
| 7.3 | WDS einrichten (eigenes Boot-Abbild), Status und Zukunft von WDS | 3 |
| 7.4 | Multicast-Prinzip, Verteilzeiten, Sicherheit des Boot-Abbilds | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Ablauf zeichnen (Lernziel 1, Einheit 7.1):** Zeichne den Ablauf von „Client startet per PXE“ bis „Windows PE läuft“ mit den Teilnehmern `CL01`, `DC01` (DHCP) und `DEPLOY01` (PXE/TFTP). Beschrifte Ports (67, 69, 4011), die DHCP-Option 60 (`PXEClient`) und die Dateien (Startdatei, `boot.sdi`, Boot-Abbild; die Datei `boot.sdi` im Ordner `RemoteInstall\SMSBoot` nennt Learn). Lies diese Proxy-DHCP-Konfiguration (Syntax mit `dnsmasq --test` geprüft, als Beispiel aus der Linux-Welt) und erkläre jede Zeile; erkläre, was sich ändert, wenn DHCP und PXE auf demselben Server laufen (Learn: Option 60 setzen, den Dienst nicht auf Port 67 lauschen lassen):
   ```text
   port=0
   dhcp-range=10.70.0.0,proxy
   pxe-service=X86-64_EFI,"Netzwerkboot UEFI x64",bootx64.efi
   enable-tftp
   tftp-root=/srv/tftp
   log-dhcp
   ```
   (Die Zeile `port=0` schaltet in diesem Beispiel nur den DNS-Teil ab. Hinweis aus dem Test: Für reines TFTP gegen `dnsmasq` 2.91 auf Loopback musste der DNS-Port **aktiv** bleiben; das ist ein Detail dieses Werkzeugs und kein Windows-Thema.)
2. **TFTP rechnen (Lernziel 2, Einheit 7.2):** Berechne die Übertragungszeit einer `boot.wim` von 400 MB (400 000 000 Byte) im einfachsten Verfahren (jeder Block wird einzeln bestätigt, Antwortzeit 0,3 ms) für Blockgrößen 512, 1456 und 8192 Byte. Bestimme die größte Nutzlast ohne IP-Fragmentierung bei MTU 1500 (IP 20, UDP 8, TFTP 4 Byte) und die Zahl der IP-Fragmente bei 8192 Byte. Erkläre, warum echte Übertragungen schneller sind (Fenstergröße; Learn nennt für Configuration Manager einstellbare Block- und Fenstergrößen).
3. **WDS einrichten (Lernziel 3, Einheit 7.3):** Installiere die Rolle und richte WDS mit dem Boot-Abbild aus Modul 6 ein (Befehle nicht bestätigt):
   ```powershell
   Install-WindowsFeature -Name WDS -IncludeManagementTools
   wdsutil /Initialize-Server /RemInst:E:\RemoteInstall
   Import-WdsBootImage -Path "E:\WinPE\amd64\media\sources\boot.wim" -NewImageName "WinPE-Rollout"
   ```
   Setze `CL02` auf den Prüfpunkt `CL02-leer` zurück (die VM enthält nach Modul 5 ein verallgemeinertes Windows), stelle das Netzwerk als erstes Startgerät ein, starte und beobachte die Firmware-Meldungen. Lade in WinPE `Deploy.cmd` aus Modul 4 und stelle das Abbild bereit. Prüfe auf `DEPLOY01`, welche UDP-Ports lauschen (`Get-NetUDPEndpoint`, nicht bestätigt). **Vorhersage und Beobachtung:** Laut Learn ist ein Windows-11-`boot.wim` von Installationsmedium bei WDS blockiert und eine End-to-End-Bereitstellung von Windows 11 nur mit WDS nicht möglich; PXE mit eigenem Boot-Abbild ist nicht betroffen. Notiere deine Vorhersage und nach Anweisung des Kursleiters das Ergebnis eines Versuchs mit dem `boot.wim` der Windows-11-ISO (nicht ausprobiert; widerspricht die Beobachtung Learn, gilt die Beobachtung mit Versionsangabe). Fasse die Ankündigung vom 24.09.2026 in drei Sätzen zusammen und nenne, was **nicht** gelesen wurde (A.2). Setze danach `DEPLOY01` auf `DEPLOY01-M6-Ende` zurück (WDS wird für Modul 8 nicht benötigt) und prüfe in `DC01` (Active Directory), ob WDS Objekte hinterlassen hat (nicht bestätigt).
4. **Multicast und Sicherheit (Lernziel 4, Einheit 7.4):** Berechne für ein Abbild von 6 GB bei 100 MB/s (1 Gbit/s mal 0,8, 1 GB gleich 1000 MB) die Zeit für 2, 30 und 200 Clients per Unicast und per Multicast sowie die vom Server gesendete Datenmenge. Nenne drei Risiken eines PXE-Boot-Abbilds (Kennwort im Abbild, Abbild für jeden ladbar, fremder DHCP/PXE-Server) und je eine Gegenmaßnahme (Learn nennt die Option „Require a password when computers use PXE“ für Configuration Manager).

#### Kontrollfragen
1. (7.1) Welche Rolle haben die Ports 67, 69 und 4011 beim PXE-Start?
2. (7.1) Warum unterstützt Microsoft DHCP-Optionen für PXE über Subnetzgrenzen bei Configuration Manager nicht, und was gilt stattdessen?
3. (7.2) Wie viele Datenpakete braucht TFTP für eine Datei von 5120 Byte bei Blockgröße 512, und warum?
4. (7.3) Was ist an WDS laut Learn abgekündigt, wann beginnt das, und was funktioniert weiter?
5. (7.4) Was verliert man laut Learn mit dem PXE-Responder ohne WDS?

---

### Modul 8: Configuration Manager: Aufbau
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Architektur eines Standorts (Standortserver, Datenbank, Verwaltungspunkt, Verteilungspunkt, SMS Provider) erklären und Bezeichnungen und Versionsstand mit Datum wiedergeben.
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzungen (SQL-Server-Version und Sortierung, ADK, Konten, Ports) prüfen und herstellen.
  * Nach Abschluss dieses Moduls kann der Lernende einen eigenständigen Primärstandort `LAB` installieren und die Konsole öffnen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen, Erkennung und die Client-Installation einrichten und prüfen.
* **Voraussetzungen:** Modul 6 (`DEPLOY01` im Zustand `DEPLOY01-M6-Ende`, also ohne WDS). Fällt die Installation aus, startet der Kursleiter mit der Ausweich-VM `DEPLOY01-CM-fertig` bei Einheit 8.4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Architektur, Rollen, Bezeichnungen und Versionsstand | 2 |
| 8.2 | Vorbereitung: Windows-Funktionen, SQL Server, ADK, Konten, Ports | 2 |
| 8.3 | Installation des Standorts `LAB`, Konsole | 2 |
| 8.4 | Grenzen, Erkennung, Client-Installation, Prüfpunkte | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Architektur und Versionswahl (Lernziel 1, Einheit 8.1):** Ordne in einer Tabelle jeder Rolle (Standortserver, Standortdatenbank, SMS Provider, Verwaltungspunkt, Verteilungspunkt) den Server im Labor zu (alle auf `DEPLOY01`) und begründe, warum Learn die Trennung als bewährte Praxis nennt. Wähle die Version (Vorschlag: 2609, Build 5.00.9152.1000, Verfügbarkeit 28.09.2026, Supportende 28.03.2028, Baseline „ja“) und prüfe: Windows Server 2025 als Standortserver (laut Learn unterstützt), SQL Server 2022 (laut Learn unterstützt), ADK 10.1.26100.9457 (laut Matrix unterstützt). Nenne die Bezeichnung des Produkts mit Stand und kennzeichne, was nicht geprüft ist (Umbenennungsdaten).
2. **Voraussetzungen herstellen (Lernziel 2, Einheit 8.2):** Installiere auf `DEPLOY01` die Windows-Funktionen .NET Framework 3.5 und Remote Differential Compression (beide laut Learn Voraussetzung des Standortservers), das ADK samt Windows-PE-Add-on (bereits in Modul 3 installiert und im Prüfpunkt `DEPLOY01-M6-Ende` enthalten; Version prüfen), den Microsoft ODBC Driver for SQL Server und SQL Server 2022 (eigene Instanz, Windows-Authentifizierung, Sortierung `SQL_Latin1_General_CP1_CI_AS`, Dienstkonto mit niedrigen Rechten, keine Begrenzung des SQL-Arbeitsspeichers laut Learn-Laborseite; die Praxisfolgen sind nicht bestätigt). Öffne die Ports 1433 (Datenbank) und 4022 (Service Broker, laut Learn-Laborseite). Aktiviere für die Installation den Dienst „Remote Registry“ (laut Learn). Führe den Prerequisite Checker aus und dokumentiere Warnungen und Fehler. Die Erweiterung des Active-Directory-Schemas wird im Labor **nicht** durchgeführt (optional; Folgen für die Standortveröffentlichung nicht bestätigt).
3. **Standort installieren (Lernziel 3, Einheit 8.3):** Führe den Setup-Assistenten aus (Schritte nach der Learn-Laborseite): Produktschlüssel „Evaluation“ (wenn verfügbar, sonst nach Anweisung des Kursleiters), „Download required files“ mit dem Pfad der Offline-Medien, Standortcode `LAB`, Standortname frei, eigenständiger Primärstandort, Datenbank auf `DEPLOY01` (Standardinstanz, Port 4022), SMS Provider und Verwaltungspunkt auf `DEPLOY01`, und die Kommunikation der Clients **nicht** auf HTTPS beschränkt (nur im isolierten Labor; HTTPS/PKI ist hier Out of Scope). Prüfe nach der Installation Dienste und Protokolle (Serverprotokolle laut Learn unter `C:\Program Files\Microsoft Configuration Manager\Logs`; das Setup-Protokoll `ConfigMgrSetup.log` liegt nach Erfahrung im Stamm von `C:\`, nicht bestätigt) und öffne die Konsole. Die Dauer der Installation ist nicht abgeschätzt.
4. **Grenzen, Erkennung, Client (Lernziel 4, Einheit 8.4):** Lege eine Grenze (IP-Adressbereich `10.70.0.1` bis `10.70.0.254`) und eine Grenzgruppe `BG-Lab` mit Standortzuweisung und Inhaltsstandort `DEPLOY01` an. Aktiviere die Active-Directory-Systemerkennung für `OU=Rollout,DC=lab,DC=example,DC=internal`. Installiere den Client auf `DEPLOY01` (zum Beispiel über die Konsole oder mit `ccmsetup.exe /mp:DEPLOY01.lab.example.internal SMSSITECODE=LAB`, Parameter nicht bestätigt) und prüfe, dass er als „Client: Ja“ und „Aktiv“ erscheint (Bezeichnungen nicht bestätigt) und seine Protokolle unter `C:\Windows\CCM\Logs` liegen. Beschreibe, warum Grenzgruppen wichtig sind; Hinweis: Eine Korrektur in Version 2609 behebt, dass ein Gerät in Windows PE zu einem Verwaltungspunkt außerhalb seiner Grenzgruppe wechseln konnte. Lege die Prüfpunkte `DC01-M8-Ende` und `DEPLOY01-M8-Ende` an (beide VMs ausgeschaltet, gemeinsam).

#### Kontrollfragen
1. (8.1) Welche Rollen vereint `DEPLOY01` im Labor, und warum ist das für den Betrieb nicht empfohlen?
2. (8.1) Wie heißt das Produkt in der aktuellen Dokumentation, wie hieß es früher, und was ist über die Umbenennungsdaten bekannt?
3. (8.2) Welche SQL-Server-Versionen unterstützt Version 2609, und welche nicht mehr?
4. (8.3) Was ist laut Learn nach der Installation eines Standortsystems nicht mehr unterstützt zu ändern?
5. (8.4) Wozu dienen Grenzen und Grenzgruppen?

---

### Modul 9: Betriebssystembereitstellung mit Configuration Manager
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Komponenten der Betriebssystembereitstellung (Boot-Abbild, Betriebssystem-Abbild, Aufgabensequenz, Verteilungspunkt, Bereitstellung) beschreiben und ihren Zusammenhang erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Boot-Abbild bereitstellen und einen Verteilungspunkt mit PXE-Responder (ohne WDS) einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende ein Betriebssystem-Abbild importieren, verteilen und eine Aufgabensequenz erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Bereitstellung für unbekannte Computer einrichten, `CL01` per PXE bereitstellen und das Ergebnis prüfen.
* **Voraussetzungen:** Modul 8, Modul 5 (Abbild `W11-ENT-REF-2026-11-v2-export.wim`)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Komponenten und Ablauf der Betriebssystembereitstellung | 2 |
| 9.2 | Boot-Abbild und PXE-fähiger Verteilungspunkt (PXE-Responder ohne WDS) | 3 |
| 9.3 | Betriebssystem-Abbild importieren und verteilen, Aufgabensequenz erstellen | 3 |
| 9.4 | Sammlung und Bereitstellung, unbekannte Computer, erste Bereitstellung per PXE | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Komponentenplan (Lernziel 1, Einheit 9.1):** Zeichne, welche Objekte für eine Bereitstellung nötig sind (Boot-Abbild, Betriebssystem-Abbild, Aufgabensequenz, Verteilungspunkt, Bereitstellung, Sammlung) und in welcher Reihenfolge sie zusammenspielen. Ordne zu, was in Windows PE und was im installierten Windows abläuft (Learn: Task-Sequence-Variable `_SMSTSInWinPE`).
2. **Boot-Abbild und PXE (Lernziel 2, Einheit 9.2):** Öffne in der Konsole „Software Library“, „Operating Systems“, „Boot Images“. Notiere Paket-ID und Windows-PE-Version des x64-Boot-Abbilds, das der Standort bei der Installation anlegt (ob und wie, nicht bestätigt). Aktiviere in den Eigenschaften (Reiter Datenquelle) „Deploy this boot image from the PXE-enabled distribution point“ und (nur im Labor) im Reiter „Customization“ die Option „Enable command support (testing only)“ (beides laut Learn). Verteile das Abbild mit „Update Distribution Points“. Aktiviere am Verteilungspunkt `DEPLOY01` „Enable PXE support for clients“, „Allow this distribution point to respond to incoming PXE requests“, „Enable unknown computer support“ und „Enable a PXE responder without Windows Deployment Service“ (laut Learn; der Verteilungspunkt muss lokal sein, damit er PXE-Anfragen beantwortet), und setze „Require a password when computers use PXE“ mit einem Kennwort vom Kursleiter. Lass die Firewall-Regeln von Configuration Manager anlegen (Learn: Dialog „Review Required Ports for PXE“). Prüfe, dass der Dienst „ConfigMgr PXE Responder Service“ (`SccmPxe`) läuft. **Befund festhalten:** Learn verlangt für PXE x86- und x64-Boot-Abbilder auf dem Verteilungspunkt, die ADK-Seite stellt 32-Bit-Windows-PE für Windows 11 als nicht unterstützt dar; prüfe im Labor, ob für UEFI-x64-Clients ein x64-Abbild genügt.
3. **Abbild und Aufgabensequenz (Lernziel 3, Einheit 9.3):** Lege das Abbild `\\DEPLOY01\Images\W11-ENT-REF-2026-11-v2-export.wim` unter „Operating System Images“ an (der Quellpfad ist als UNC-Pfad anzugeben, und das Computerkonto des Standortservers braucht Leserechte, nicht bestätigt) und verteile es an den Verteilungspunkt. Prüfe in der Überwachung den Inhaltsstatus. Erstelle eine Aufgabensequenz „TS-Win11-Standard“ aus einem vorhandenen Abbild (Assistent „Install an existing image package“, Name nicht bestätigt) mit den Schritten: Format and Partition Disk (UEFI), Apply Operating System, Apply Windows Settings, Apply Network Settings (zunächst Arbeitsgruppe), Setup Windows and Configuration Manager. Wähle das Boot-Abbild aus Aufgabe 2.
4. **Bereitstellung und erster Lauf (Lernziel 4, Einheit 9.4):** Stelle die Aufgabensequenz für die Sammlung der unbekannten Computer bereit („All Unknown Computers“, Name nicht bestätigt), Verfügbarkeit „Only media and PXE“ (eine der drei Optionen laut Learn). Starte `CL01` per PXE (Netzwerk als erstes Startgerät), gib das PXE-Kennwort ein, wähle die Aufgabensequenz und beobachte den Ablauf; drücke in Windows PE bei Bedarf **F8** (Befehlszeile) und lies `X:\Windows\Temp\SMSTSLog\smsts.log`. Erfasse die Dauer je Phase in einer Tabelle (Start PXE bis Windows PE, Anwenden des Abbilds, erster Start, Client-Installation). Prüfe in der Konsole, ob `CL01` als Gerät mit Client erscheint.

#### Kontrollfragen
1. (9.1) Was unterscheidet ein Boot-Abbild von einem Betriebssystem-Abbild?
2. (9.2) Warum braucht PXE einen lokalen Verteilungspunkt, und was bedeutet „PXE-Responder ohne WDS“?
3. (9.2) Warum ist „Enable command support“ nicht für den Produktivbetrieb gedacht?
4. (9.3) Warum muss der Inhalt auf dem Verteilungspunkt liegen, bevor die Aufgabensequenz läuft?
5. (9.4) Welche drei Verfügbarkeitsoptionen nennt Learn für PXE-Bereitstellungen, und was unterscheidet „Only media and PXE“ von „Configuration Manager clients, media, and PXE“?

---

### Modul 10: Aufgabensequenzen in der Tiefe
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Aufgabensequenz (Gruppen, Schritte, Bedingungen, Variablen) erklären und eine Aufgabensequenz umbauen.
  * Nach Abschluss dieses Moduls kann der Lernende Bedingungen und Variablen einsetzen und Computernamen steuern.
  * Nach Abschluss dieses Moduls kann der Lernende Treiberpaket, Domänenbeitritt mit minimal berechtigtem Konto und einen Befehlszeilenschritt einbauen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerbehandlung konfigurieren und Neu-Bereitstellung und Refresh-Szenarien beschreiben.
* **Voraussetzungen:** Modul 9

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Aufbau: Gruppen, Schritte, Reihenfolge, Phasen | 2 |
| 10.2 | Bedingungen, Variablen (Aufgabensequenz-, Sammlungs- und Gerätevariablen), Computername | 2 |
| 10.3 | Treiberpaket, Domänenbeitritt, Konto mit minimalen Rechten, Befehlszeilenschritt | 3 |
| 10.4 | Fehlerbehandlung, Erfolgscodes, Neu-Bereitstellung, Refresh mit Benutzerdaten | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Struktur (Lernziel 1, Einheit 10.1):** Dupliziere „TS-Win11-Standard“ zu „TS-Win11-Domäne“ und gliedere sie in vier Gruppen: „Vorbereitung (Windows PE)“, „Installation“, „Konfiguration“, „Abschluss“. Erstelle eine Tabelle: Schritt, Gruppe, läuft in Windows PE oder im Windows, Bedingung, Fehlerverhalten.
2. **Bedingungen und Namen (Lernziel 2, Einheit 10.2):** Lege an die Gruppe „Vorbereitung“ eine Bedingung auf die Variable `_SMSTSBootUEFI` (laut Learn wird sie bei UEFI-Systemen gesetzt; erwarteter Vergleichswert nicht bestätigt, im Labor testen). Gib `CL01` und `CL02` feste Namen: Trage die MAC-Adressen ein (Hyper-V: `Get-VMNetworkAdapter -VMName CL01 | Select-Object MacAddress`; setze zuvor statische MAC-Adressen, nicht bestätigt), importiere die Geräte in die Konsole (Funktion „Import Computer Information“, Name nicht bestätigt) und setze die Gerätevariable `OSDComputerName` (Name der Variable nicht aus den Auszügen belegt, in der Variablenreferenz zu prüfen). Lege die Gerätesammlung `Rollout-Clients` an, nimm die importierten Geräte per direkter Mitgliedschaft auf und stelle die Aufgabensequenz zusätzlich für diese Sammlung bereit (die Geräte sind nun bekannt, die Sammlung der unbekannten Computer gilt für sie nicht mehr). Stelle `CL02` bereit und prüfe den Namen.
3. **Treiber, Domänenbeitritt, Befehlszeile (Lernziel 3, Einheit 10.3):** Importiere die Treiber aus `\\DEPLOY01\Images\Drivers\Virtual-Machine` (UNC-Pfad, Quelle nicht bestätigt) in ein Treiberpaket (Funktion und Schritt „Apply Driver Package“ bzw. „Auto Apply Drivers“, Namen nicht bestätigt) und füge den Schritt ein. Ersetze „Apply Network Settings“ durch Domänenbeitritt `lab.example.internal` in `OU=Clients,OU=Rollout,DC=lab,DC=example,DC=internal` mit dem Konto `LAB\svc-osd-join`, dessen Kennwort der Kursleiter einträgt. Füge einen Schritt „Run Command Line“ hinzu, der `C:\Rollout\fertig.txt` anlegt (`cmd /c "mkdir C:\Rollout & echo ok > C:\Rollout\fertig.txt"`, nicht bestätigt). Beachte laut Learn: Gibt der Schritt „Run Command Line“ ein Benutzerkonto an und läuft in Windows PE, schlägt er fehl, weil sich Windows PE nicht in eine Domäne aufnehmen lässt. Begründe schriftlich, warum `svc-osd-join` nicht Domänenadministrator ist und welche Rechte es hat (Computerkonten in einer OU anlegen).
4. **Fehler und Wiederholung (Lernziel 4, Einheit 10.4):** Baue einen absichtlich fehlschlagenden Schritt `cmd /c exit 5` ein; lasse ihn zuerst ohne Option „Continue on error“ laufen (die Aufgabensequenz bricht ab), dann mit „Continue on error“ und dann mit Erfolgscode 5 (Reiter „Options“ des Schritts, laut Learn „Success codes“). Lies im `smsts.log` den Rückgabecode (die Variable `_SMSTSLastActionRetCode` enthält laut Learn den Rückgabecode des letzten Schritts). Stelle `CL01` erneut bereit (eine Wiederholung braucht je nach Einstellung das Zurücksetzen der PXE-Bereitstellung; Funktionsname nicht bestätigt). Beschreibe ohne Umsetzung, wie ein Refresh mit Benutzerdaten arbeitet (Schritte „Capture User State“ und „Restore User State“ laut Learn).

#### Kontrollfragen
1. (10.1) Warum gliedert man eine Aufgabensequenz in Gruppen?
2. (10.2) Mit welcher Variablen erkennt man UEFI, und wozu braucht der Schritt „Format and Partition Disk“ eine passende Bedingung?
3. (10.3) Warum kann „Run Command Line“ mit einem Benutzerkonto in Windows PE nicht laufen?
4. (10.3) Welche Rechte braucht das Beitrittskonto, und warum ist ein Domänenadministrator dafür ungeeignet?
5. (10.4) Was enthält `_SMSTSLastActionRetCode`, und wie nutzt man es zur Fehlersuche?

---

### Modul 11: Softwareverteilung
* **Priorität:** 1
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Anwendungsmodell (Anwendung, Bereitstellungstyp, Erkennungsmethode, Anforderungen, Inhalt) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Anwendung mit Skript-Bereitstellungstyp erstellen, verteilen und die Installation über die Erkennungsmethode prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Anwendung in der Aufgabensequenz und nachträglich über das Software Center bereitstellen und beide Wege vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Anwendung aktualisieren, deinstallieren und die Bereitstellung zurückbauen.
* **Voraussetzungen:** Modul 10 (`CL01` mit Client, Domänenmitglied)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Anwendungsmodell: Anwendung, Bereitstellungstyp, Erkennung, Anforderungen | 2 |
| 11.2 | Anwendung erstellen, verteilen, bereitstellen (Skript-Bereitstellungstyp) | 2 |
| 11.3 | Installation in der Aufgabensequenz gegenüber Software Center | 2 |
| 11.4 | Aktualisieren, Deinstallieren, Rückbau | 1 |

#### Praxisaufgaben (Hands-on Lab)
Als Prüfobjekt dient eine eigene, harmlose „Anwendung“ ohne Fremdsoftware: ein Skript, das eine Markierungsdatei anlegt (keine Lizenzfragen, kein Internet nötig). Die Skripte sind nicht ausgeführt.
```cmd
@echo off
rem install.cmd
mkdir C:\Rollout 2>nul
echo Version 1 installiert %DATE% %TIME% > C:\Rollout\app1.txt
exit /b 0
```
```cmd
@echo off
rem uninstall.cmd
del C:\Rollout\app1.txt
exit /b 0
```
1. **Modell erklären (Lernziel 1, Einheit 11.1):** Beschreibe an diesem Beispiel, welche Rolle Anwendung, Bereitstellungstyp, Erkennungsmethode (Datei `C:\Rollout\app1.txt` existiert), Anforderungen und Inhalt (Quelle, Verteilungspunkt) haben, und was die Erkennungsmethode bei einer zweiten Bereitstellung bewirkt.
2. **Erstellen und bereitstellen (Lernziel 2, Einheit 11.2):** Lege `E:\Apps\Marker` an (Freigabe `\\DEPLOY01\Apps`, Leserechte für das Computerkonto des Standortservers, nicht bestätigt), kopiere die Skripte, lege in der Konsole die Anwendung mit Bereitstellungstyp „Script Installer“ (Name nicht bestätigt), Installationsbefehl `install.cmd`, Deinstallationsbefehl `uninstall.cmd` und der Erkennungsmethode „Datei existiert“ an, verteile den Inhalt, verwende die Gerätesammlung `Rollout-Clients` aus Modul 10 (`CL01` und `CL02`) und stelle die Anwendung als „Required“ bereit. Prüfe auf `CL01`, ob die Datei entsteht, und lies die Client-Protokolle in `C:\Windows\CCM\Logs` (Dateinamen `AppDiscovery.log` und `AppEnforce.log` nach Erfahrung, nicht bestätigt).
3. **Zwei Wege (Lernziel 3, Einheit 11.3):** (a) Füge in „TS-Win11-Domäne“ den Schritt „Install Application“ ein (Schrittname laut Learn) und stelle `CL02` bereit. (b) Stelle dieselbe Anwendung für `CL01` als „Available“ bereit und installiere sie im Software Center (Bezeichnungen nicht bestätigt). Vergleiche Dauer, Zustand beim ersten Anmelden und Fehlerbild in einer Tabelle.
4. **Aktualisieren und zurückbauen (Lernziel 4, Einheit 11.4):** Lege Version 2 an (`install.cmd` schreibt „Version 2“), stelle sie bereit und prüfe den Inhalt der Datei. Deinstalliere die Anwendung über die Bereitstellung mit der Aktion „Uninstall“ (nicht bestätigt) und prüfe, dass die Datei verschwindet. Entferne dann Bereitstellung und Anwendung. Lege den Prüfpunkt `DEPLOY01-M11-Ende` an.

#### Kontrollfragen
1. (11.1) Warum ist die Erkennungsmethode für die Zuverlässigkeit der Verteilung so wichtig?
2. (11.2) Woher laden Clients den Inhalt, und warum muss er vorher verteilt sein?
3. (11.3) Nenne je einen Vorteil und einen Nachteil der Installation innerhalb der Aufgabensequenz.
4. (11.3) Was unterscheidet „Available“ von „Required“ (nach Konsole, nicht bestätigt)?
5. (11.4) Warum prüft man die Deinstallation, bevor man eine Anwendung in Produktion bringt?

---

### Modul 12: MDT: Altumgebung lesen und ablösen
* **Priorität:** 2
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau von MDT (Deployment Share, Boot-Abbilder, Aufgabensequenzen, Regeldateien) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende `Bootstrap.ini` und `CustomSettings.ini` lesen, das Verhalten ableiten und Sicherheitsprobleme erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Ablösung von MDT planen und die Stilllegung in Configuration Manager in der richtigen Reihenfolge beschreiben.
* **Voraussetzungen:** Modul 9. MDT wird im Labor **nicht installiert**; die Übungen lesen vorbereitete Beispieldateien und ändern das Labor nicht.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | MDT: Zweck, Aufbau, Status (eingestellt) | 2 |
| 12.2 | Regeldateien `Bootstrap.ini` und `CustomSettings.ini` lesen | 1 |
| 12.3 | Stilllegung und Migration | 2 |

#### Praxisaufgaben (Hands-on Lab)
**Stand MDT (08.11.2026):** MDT ist eingestellt (Learn, Hinweis vom 06.01.2026): keine Updates, Korrekturen oder Support, Download-Pakete können entfernt werden, bestehende Installationen laufen weiter. Letzte Version: Build 8456. Dass MDT mit Windows 11 nicht unterstützt ist, stammt aus einer Zitierung in einer Q&A-Frage, die Aussage in den *Known issues* war im Auszug nicht enthalten; **nicht bestätigt**. Ob der Download noch verfügbar ist und ob Build 8456 mit ADK 10.1.26100.x läuft, ist **nicht bestätigt**. Eine Installation im Labor erfolgt nur, wenn der Kursleiter einen lokalen Installer hat, auf einer Kopie des Labors; das Ergebnis ist eine Beobachtung, kein Lernziel.
1. **Aufbau zeichnen (Lernziel 1, Einheit 12.1):** Zeichne den Ablauf: Deployment Share (`\\DEPLOY01\DeploymentShare$`, Beispielname), Boot-Abbild, Regeldateien, Aufgabensequenz, Anwendungen, Treiber („Out-of-Box Drivers“, Name nicht bestätigt). Beschreibe in einem Absatz, wofür MDT gebaut wurde und was seine Einstellung für Windows-11-Rollouts bedeutet.
2. **Dateien lesen (Lernziel 2, Einheit 12.2):** Die folgenden Beispieldateien sind erfunden; Schlüsselnamen stammen aus Erfahrung, die MDT-Dokumentation wurde nicht abgerufen (**nicht bestätigt**). Erkläre, was `CustomSettings.ini` bei der Bereitstellung erzwingt und was `Bootstrap.ini` leistet; nenne die zwei Sicherheitsprobleme.
   ```ini
   [Settings]
   Priority=Default

   [Default]
   OSInstall=Y
   SkipBDDWelcome=YES
   JoinDomain=lab.example.internal
   DomainAdmin=svc-osd-join
   DomainAdminDomain=LAB
   DomainAdminPassword=PLATZHALTER-vom-Kursleiter
   MachineObjectOU=OU=Clients,OU=Rollout,DC=lab,DC=example,DC=internal
   ```
   ```ini
   [Settings]
   Priority=Default

   [Default]
   DeployRoot=\\DEPLOY01\DeploymentShare$
   UserID=svc-osd-read
   UserDomain=LAB
   UserPassword=PLATZHALTER-vom-Kursleiter
   ```
3. **Ablösung planen (Lernziel 3, Einheit 12.3):** Erstelle eine Tabelle MDT-Element, Entsprechung in Configuration Manager (Anwendungen, Treiberpakete, Aufgabensequenz, Variablen und dynamische Variablen, Boot-Abbild) und Aufwand. Beschreibe die Stilllegung in Configuration Manager in der Reihenfolge, die Learn nennt (zuerst die MDT-Schritte aus den Aufgabensequenzen entfernen, danach die MDT-Integration), und prüfe „TS-Win11-Domäne“ aus Modul 10 auf MDT-Schritte (erwartet: keine). Nenne drei Risiken des Weiterbetriebs von MDT.

#### Kontrollfragen
1. (12.1) Was ist ein Deployment Share, und was enthält er?
2. (12.2) Welche beiden Dateien enthalten im Beispiel Kennwörter, und warum ist das bei `Bootstrap.ini` besonders kritisch?
3. (12.3) In welcher Reihenfolge entfernt man laut Learn MDT aus Configuration Manager, und warum?

---

### Modul 13: Alternativen: FOG, Autopilot und Intune im Überblick
* **Priorität:** 2
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aufbau und Voraussetzungen von FOG im Überblick beschreiben und Grenzen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende WDS, Configuration Manager, FOG und MDT nach Kriterien vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Autopilot und Intune als Alternative abgrenzen, ohne sie zu konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine Entscheidungsmatrix für ein Szenario ausfüllen und die Wahl begründen.
* **Voraussetzungen:** Modul 9. FOG wird vom Kursleiter in einer **eigenen, getrennten** VM vorgeführt (Installer braucht Internet laut Herstellerseite); das private Labor bleibt unverändert.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 13.1 | FOG im Überblick: Server, Abbilder, PXE, Betrieb (Vorführung) | 2 |
| 13.2 | Vergleich WDS, Configuration Manager, FOG, MDT | 1 |
| 13.3 | Autopilot und Intune: Abgrenzung (eigener Kurs) | 1 |
| 13.4 | Entscheidungsmatrix | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **FOG kennenlernen (Lernziel 1, Einheit 13.1):** Notiere zur Vorführung: aktuelle Version (Herstellerseite am 08.11.2026: 1.6.0.14, 02.11.2026), Betriebssystem des Servers (laut Hersteller nur Linux), Netzwerkbedarf bei der Installation (Internet), wie PXE bereitgestellt wird und wie ein Abbild erfasst und angewendet wird. Aussagen zu Technik im Detail (zum Beispiel iPXE, ein Linux-basierter Client für die Abbildarbeit, Partclone) stammen aus Erfahrung, die FOG-Dokumentation wurde nicht abgerufen (**nicht bestätigt**). Lizenz und Support von FOG sind nicht geprüft.
2. **Vergleich (Lernziel 2, Einheit 13.2):** Fülle eine Tabelle mit den Kriterien Status mit Datum, Windows-11-Eignung, PXE, Multicast, Aufgabensequenzen, Softwareverteilung, Betriebsaufwand, Kosten. Jede Zelle bekommt die Quelle aus A.2 oder „nicht bestätigt“.
3. **Abgrenzung (Lernziel 3, Einheit 13.3):** Schreibe eine halbe Seite: Was sind Autopilot und Intune (laut Learn „cloud-driven, zero-touch provisioning“, von Microsoft als moderner Weg empfohlen), was ersetzen sie, was bleibt lokal, und welche drei Voraussetzungen fehlen im Labor (Internet, Cloud-Mandant, Lizenzen). Keine Konfiguration; die Themen sind ein eigener Kurs.
4. **Entscheidungsmatrix (Lernziel 4, Einheit 13.4):** Bewerte die drei Szenarien aus Modul 1, Aufgabe 4 mit der Matrix (Gewichtung 1 bis 3, Bewertung 1 bis 5) und vergleiche mit deiner damaligen Wahl. Begründe Änderungen.

#### Kontrollfragen
1. (13.1) Welche Voraussetzungen nennt der Hersteller für die Installation eines FOG-Servers?
2. (13.2) Warum ist WDS für neue Aufbauten keine langfristige Wahl?
3. (13.3) Warum ist Autopilot nicht Teil dieses Labors?
4. (13.4) Welche Kriterien würdest du bei 300 Geräten in einem Standort ohne Cloud-Verwaltung am höchsten gewichten, und warum?

---

### Modul 14: Fehlersuche
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Fehlersuche in Stufen (Netzwerk, PXE, Windows PE, Aufgabensequenz, Windows) durchführen und den Stufen Protokolle zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende PXE- und Startfehler (DHCP, Startreihenfolge, Dienste, Bereitstellung) eingrenzen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler einer Aufgabensequenz im `smsts.log` finden und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende Abbild-, Namensauflösungs- und Domänenbeitrittsfehler erkennen und ein Fehlerprotokoll schreiben.
* **Voraussetzungen:** Module 9, 10 und 11 (Zustand `DEPLOY01-M11-Ende`; `DC01-M8-Ende` darf nur gemeinsam mit `DEPLOY01-M8-Ende` zurückgesetzt werden). Der Kursleiter baut die Fehler vor jeder Übung ein (Vorschläge in Abschnitt C, nicht getestet).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 14.1 | Methodik, Stufen, Protokolle und Fundorte | 2 |
| 14.2 | PXE- und Startfehler | 3 |
| 14.3 | Fehler der Aufgabensequenz | 2 |
| 14.4 | Abbild-, DNS- und Domänenbeitrittsfehler, Fehlerprotokoll | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Protokolle und Fundorte (Lernziel 1, Einheit 14.1):** Fülle eine Tabelle: Phase, Pfad von `smsts.log` (Windows PE vor dem Schritt „Format and Partition Disk“, nach diesem Schritt, im neuen Windows vor der Client-Installation, nach der Client-Installation, nach Abschluss), und vergleiche mit Learn („About log files“). Starte `CL01` per PXE, öffne mit F8 die Befehlszeile und finde in `smsts.log` fünf Zeilen, die den Fortschritt belegen (Zeitstempel notieren). Nenne die Variable `_SMSTSLogPath`, die laut Learn den aktuellen Pfad enthält.
2. **PXE- und Startfehler (Lernziel 2, Einheit 14.2):** Der Kursleiter baut nacheinander vier Fehler ein: deaktivierter DHCP-Bereich, gestoppter PXE-Responder-Dienst, Netzwerk nicht als erstes Startgerät, Bereitstellung nicht für unbekannte Computer verfügbar. Fülle je Fehler ein Formular: Symptom, Hypothese, Prüfung, Ursache, Lösung. Die Firmware-Meldungen sind nicht vorab bekannt; notiere sie wörtlich. Prüfe bei fehlender Adresse in Windows PE mit F8 und `ipconfig`, ob die Netzwerkkarte erkannt ist (Learn: fehlt in `smsts.log` die Zeile „Found network adapter … with IP Address …“, liegt meist ein Treiberproblem vor).
3. **Fehler der Aufgabensequenz (Lernziel 3, Einheit 14.3):** Drei Fehler: Inhalt des Betriebssystem-Abbilds nicht an den Verteilungspunkt verteilt; Beitrittskonto mit falschem Kennwort; Bedingung auf `_SMSTSBootUEFI` falsch gesetzt, sodass das Partitionieren übersprungen wird. Finde je Fehler Schritt, Rückgabecode und Meldung im `smsts.log` und behebe ihn. Beachte, dass der Fundort des Protokolls wechselt (siehe Aufgabe 1).
4. **Abbild, DNS, Domäne (Lernziel 4, Einheit 14.4):** Drei Fehler: Antwort-DNS des Clients zeigt nicht auf `DC01`; falscher Index des Abbilds in der Aufgabensequenz (nicht die Enterprise-Edition); ein Computerkonto gleichen Namens liegt in einer anderen OU. Schreibe für jeden Fall ein kurzes Fehlerprotokoll (Zeit, Symptom, Ursache, Beleg im Protokoll, Lösung, Vorbeugung).

#### Kontrollfragen
1. (14.1) Wo liegt `smsts.log` in Windows PE vor und nach dem Schritt „Format and Partition Disk“?
2. (14.1) Wie öffnet man eine Befehlszeile in Windows PE, und warum ist das nicht für die Produktion gedacht?
3. (14.2) Woran erkennt man im `smsts.log` ein Treiberproblem der Netzwerkkarte?
4. (14.2) Der Client meldet, dass keine Aufgabensequenz verfügbar ist. Nenne zwei Ursachen (Learn nennt für Version 2609 einen Fall mit versteckter Bereitstellung und der Variablen `SMSTSPreferredAdvertID`).
5. (14.3) Welche Variable enthält den Rückgabecode des letzten Schritts?
6. (14.4) Warum scheitert der Domänenbeitritt bei falschem DNS-Server, obwohl die Netzwerkverbindung steht?

---

## C. Hinweise zur Entstehung und Prüfvermerk (08.11.2026)

Dieser Lehrplan wurde ohne Gem-Entwurf direkt aus dem Prompt P46 erstellt. Annahmen: 14 Module mit 108 UE (innerhalb der Vorgabe 10 bis 14 Module und 100 bis 120 UE); Labor mit vier VMs (`DC01`, `DEPLOY01`, `CL01`, `CL02`) auf einem privaten Switch mit dem Netz `10.70.0.0/24` und der Domäne `lab.example.internal` (`.internal` ist für private Nutzung vorgesehen, nicht bestätigt); `DEPLOY01` ist zuerst WDS-Server (Modul 7) und danach Configuration-Manager-Standort (ab Modul 8); MDT wird nur als Altumgebung behandelt, weil es eingestellt ist; Intune und Autopilot nur als Abgrenzung. Der Produktstand stammt von Microsoft Learn und der FOG-Herstellerseite vom 08.11.2026 (A.2). Rechenwerte wurden per Skript berechnet; WIM-, TFTP- und XML-Verhalten wurde in einer Linux-Sandbox mit Ersatzwerkzeugen getestet (A.3); **kein Windows-Befehl wurde ausgeführt**.

**Kontrollwerte (Lösungsschlüssel für Dozenten):**

* **Modul 1, Aufgabe 1:** (a) Neuinstallation („New computer“); (b) Refresh; (c) Replace; (d) In-place-Upgrade; (e) schlankes Abbild; (f) volles Abbild.
* **Modul 1, Aufgabe 3:** (a) Supportdauer bei 2509, 2603 und 2609 je 18 Monate (12.11.2025 bis 12.05.2027, 05.05.2026 bis 05.11.2027, 28.09.2026 bis 28.03.2028); Resttage ab 08.11.2026: 2509 185, 2603 362, 2609 506. (b) Das Rollout-Ende ist der 01.03.2028. Nur 2609 ist dann noch unterstützt (Ende 28.03.2028, 27 Tage danach); 2603 endete 117 Tage zuvor, 2509 294 Tage zuvor. (c) ADK 10.1.26100.9457 (September 2026); Windows 11 26H2 als Client wird laut Matrix von 2603 und 2609 unterstützt, von 2509 nicht. (d) Das ADK 10.1.28000.3481 (Oktober 2026) unterstützt laut ADK-Seite nur Windows 11 26H1; in der Configuration-Manager-Matrix ist nur 10.1.28000.1 aufgeführt und für 2509, 2603 und 2609 nicht unterstützt; Version .3481 steht im Auszug nicht in der Matrix (also nicht als unterstützt belegt).
* **Modul 1, Aufgabe 4:** (A) manuell mit Windows-PE-Medium, Abbild und Skript (8 Geräte); (B) Configuration-Manager-Betriebssystembereitstellung (laut Learn „remains a fully supported option“ für lokale Umgebungen); (C) Autopilot/Intune (eigener Kurs). Rückfall zum Beispiel: letztes freigegebenes Abbild bleibt archiviert, Zurückspielen möglich; Pilotgruppe zum Beispiel 1 Gerät, 5 Geräte, 10 % (Vorschlag des Lehrplans, nicht belegt).
* **Modul 2, Aufgabe 1:** VM-Arbeitsspeicher 4 + 12 + 4 + 4 = 24 GB; Host mit 8 GB Reserve 32 GB; maximale Plattengrößen 60 + 100 + 100 + 64 + 64 = 388 GB. Learn-Laborempfehlung für den Standort- und Datenbankserver: 2 bis 4 Kerne, 8 bis 12 GB, 100 GB; gewählt 4 vCPUs, 12 GB, 100 GB plus 100 GB Daten.
* **Modul 2, Aufgabe 4 und Frage 5:** /24 hat 254 nutzbare Adressen; Bereich `.100` bis `.199` hat 100; außerhalb bleiben 154. `DEPLOY01` (`.20`) und `DC01` (`.10`) liegen außerhalb, damit keine Adresse doppelt vergeben wird.
* **Modul 3, Aufgabe 1:** Ziel 26H2 und 25H2: ADK 10.1.26100.9457 (laut ADK-Seite unterstützt es 26H2, 25H2, 24H2 und Windows Server 2025/2022). Gerät mit 26H1: ADK 10.1.28000.3481, mit Configuration Manager 2609 nicht als unterstützt belegt (siehe Modul 1).
* **Modul 3, Aufgabe 4 (Referenzwerte aus `wimlib-imagex`, keine DISM-Werte):** Datei `s1` (20 000 000 + 5 000 000 Byte Zufallsdaten): 25 001 520 Byte; `s2`: 25 001 522 Byte; Summe zweier getrennter Dateien 50 003 042 Byte; eine Datei mit beiden Abbildern (Index 1 und 2): 30 003 630 Byte; Ersparnis 19 999 412 Byte (40,0 %), das ist die einmal gespeicherte gemeinsame Datei. Mit Nullbytes (gleich große Dateien sind untereinander gleich): 25 003 554 Byte. Anwenden von Index 2 und Vergleich mit dem Quellordner: identisch; Export von Index 2 ergibt eine Datei mit einem Abbild (25 001 522 Byte). Mit DISM weichen die Zahlen durch Metadaten ab; die Größenordnung (etwa 30 MB statt 50 MB) muss stimmen.
* **Modul 4, Aufgabe 1:** MSR 16 MB; erwartet: drei Partitionen (EFI/System 300 MB FAT32, MSR 16 MB, Windows NTFS mit dem Rest). Aufgabe 2: Partitionierung gehört in `windowsPE` (nur in einer `Autounattend.xml`); Computername in `specialize`; Zeitzone in `specialize` (ein Einsatz in `oobeSystem` ist ebenfalls möglich, nicht bestätigt); Sprachen, OOBE-Einstellungen und das lokale Konto in `oobeSystem`. Frage 4: Bei `Apply-Image` läuft Windows Setup nicht, die Phase `windowsPE` gehört zu Setup.
* **Modul 5, Aufgabe 4:** (a) 12 × 6 = 72 GB; (b) 3 × 6 = 18 GB; (c) 3 Abbilder plus `W11-ENT-Basis.wim` = 4 × 6 = 24 GB, mit 40 GB für ISO-Dateien und Treiber 64 GB; es bleiben 36 GB auf `E:`, also passt es.
* **Modul 6, Aufgabe 1:** Netzwerkkarte, die Windows PE nicht erkennt: (b) Boot-Abbild; Massenspeicher-Controller, der in Windows PE und im Betriebssystem fehlt: (b) und zusätzlich (a) bzw. (c); Grafikkarte: (c), oder (d), wenn der Inbox-Treiber genügt.
* **Modul 7, Aufgabe 2 (Modell: jeder Block einzeln bestätigt, Antwortzeit 0,3 ms):** 400 000 000 Byte: Blockgröße 512: 781 251 Blöcke, 234,4 s; 1456: 274 726 Blöcke, 82,4 s; 8192: 48 829 Blöcke, 14,6 s. Größte Nutzlast ohne Fragmentierung bei MTU 1500: 1500 − 20 − 8 − 4 = 1468 Byte; bei 8192 Byte: UDP-Nutzlast 8192 + 4 + 8 = 8204 Byte, also 6 IP-Fragmente (je höchstens 1480 Byte Nutzdaten).
* **Modul 7, Frage 3 (gegen `dnsmasq` 2.91 gemessen):** Datei 5120 Byte: bei Blockgröße 512 sind es 11 Datenpakete (10 volle und ein leeres Abschlusspaket), bei 1456 sind es 4. Datei 10 000 000 Byte: 19 532 Pakete (512) und 6 869 Pakete (1456). Formel: Dateigröße ganzzahlig geteilt durch Blockgröße, plus 1. WDS selbst wurde nicht gemessen und kann durch Fenstergrößen abweichen.
* **Modul 7, Aufgabe 4:** 6 GB bei 100 MB/s: 2 Clients: Unicast 120 s (2,0 min), Multicast 60 s; 30 Clients: 1800 s (30 min) gegen 60 s; 200 Clients: 12 000 s (200 min, 3 h 20 min) gegen 60 s. Vom Server gesendet: 12, 180 und 1200 GB gegen 6 GB. Das Modell setzt voraus, dass Multicast mit der vollen Rate läuft; in der Praxis bestimmt der langsamste Empfänger die Rate (nicht bestätigt). Frage 5: Multicast; laut Learn lässt sich der PXE-Responder ohne WDS nicht mit Multicast kombinieren.
* **Modul 8, Fragen:** Frage 3: SQL Server 2017 (ab CU2), 2019 (ab CU5), 2022 und 2025 (Unterstützung ab 2603); SQL Server 2016 wird ab Version 2609 nicht mehr unterstützt. Frage 4: Domänenname, Domänenmitgliedschaft und Computername eines Standortsystems dürfen nach der Installation nicht geändert werden (zuvor Rolle entfernen).
* **Modul 9, Frage 5:** Die drei Optionen laut Learn sind „Configuration Manager clients, media, and PXE“, „Only media and PXE“ und „Only media and PXE (hidden)“. Bei „Only media and PXE“ sehen Clients mit Configuration-Manager-Client die Bereitstellung nicht im Software Center.
* **Modul 10, Aufgabe 4:** `cmd /c exit 5` liefert Rückgabecode 5. Ohne Option bricht die Aufgabensequenz ab; mit „Continue on error“ läuft sie weiter; mit Erfolgscode 5 gilt der Schritt als erfolgreich.
* **Modul 12, Fragen:** Frage 3: erst die MDT-Schritte aus den Aufgabensequenzen entfernen, dann die MDT-Integration (Learn: sonst Beschädigung der Aufgabensequenz und Fehler beim Ändern). Frage 2: Beide Dateien enthalten Kennwörter im Klartext; `Bootstrap.ini` steckt im Boot-Abbild und ist damit von jedem auslesbar, der es per PXE laden darf.
* **Modul 14, Fehlereinbau (Vorschlag des Kursleiters, nicht getestet; für jeden Fall den Behebungsweg im Kursleiter-Skript festhalten):** (1) DHCP-Bereich deaktivieren (`Set-DhcpServerv4Scope -ScopeId 10.70.0.0 -State InActive`): Client erhält keine Adresse; Lösung: aktivieren. (2) Dienst `SccmPxe` anhalten: Client findet keinen PXE-Server; Lösung: Dienst starten. (3) Platte statt Netzwerk als erstes Startgerät: kein PXE-Start; Lösung: `Set-VMFirmware`. (4) Bereitstellung nur für eine andere Sammlung: Meldung, dass keine Aufgabensequenz verfügbar ist; Lösung: Bereitstellung der richtigen Sammlung zuweisen. (5) Abbild-Inhalt nicht verteilt: Schritt „Apply Operating System“ findet den Inhalt nicht (Wortlaut im Protokoll nicht bestätigt); Lösung: Inhalt verteilen, Inhaltsstatus prüfen. (6) Falsches Kennwort des Beitrittskontos: Schritt „Apply Network Settings“ scheitert (Windows-Fehler 1326 „Benutzername oder Kennwort falsch“ ist üblich, nicht bestätigt). (7) Falsche UEFI-Bedingung: Partitionsschritt wird übersprungen, danach scheitert das Anwenden des Abbilds. (8) DNS des Clients zeigt nicht auf `DC01`: Domänenbeitritt findet keinen Domänencontroller. (9) Falscher Index des Abbilds: falsche Edition installiert; Prüfung mit `Dism /Get-ImageInfo`. (10) Computerkonto gleichen Namens in anderer OU: Beitritt scheitert oder übernimmt das Konto je nach Rechten (nicht bestätigt).

**Prüfvermerk (Grundanweisung, neun Punkte):**

1. **Stunden und Prioritäten:** 7+7+9+8+8+7+9+8+10+9+7+5+5+9 = 108 UE; 12× Priorität 1 (98 UE), 2× Priorität 2 (10 UE). Per Skript über die Datei geprüft: Modulkopf, Master-Tabelle und Summe der Einheitentabelle stimmen in allen 14 Modulen überein. Keine Fehler gefunden; Stichprobe: Modul 9 mit 2+3+3+2 = 10 UE.
2. **Labor-Setup und Installation:** Host, Switch, vier VMs, Adressplan, Beschaffung und Prüfpunkte stehen in A.3. Bei der Prüfung gefunden und korrigiert: `CL02` war in Modul 7 nicht mehr leer (jetzt Rücksetzen auf `CL02-leer`); der Transport von Dateien zwischen Host und VM fehlte (jetzt PowerShell Direct mit Prüfaufgabe, Ausweichen nicht bestätigt); Generation-2-VMs haben kein DVD-Laufwerk (jetzt `Add-VMDvdDrive` in Modul 3); der Treiberordner lag außerhalb der Freigabe (jetzt `E:\Images\Drivers`); die Sammlung `Rollout-Clients` wurde erst nach ihrer Verwendung angelegt (jetzt in Modul 10); die ADK-Bemerkung in Modul 8 war missverständlich. Offen: Eignung der Windows-Server-2025-Evaluation, Verfügbarkeit einer Evaluation von Configuration Manager 2609.
3. **Quellen:** Siehe A.2. Learn-Seiten wurden nur als Suchtreffer-Auszüge gelesen; die Ankündigung zur WDS-Abkündigung auf support.microsoft.com und die Härtungsanleitung zu CVE-2026-0386 wurden nicht gelesen; die Aussage „MDT unter Windows 11 nicht unterstützt“ ist nicht bestätigt; Umbenennungsdaten von Configuration Manager nicht geprüft; die Learn-Laborseite ist veraltet und nur für die Abfolge benutzt; die FOG-Dokumentation wurde nicht abgerufen.
4. **Widerspruchsfreiheit und Zustände:** Zustandskette: M2 Basis → M3 bis M6 (Dateien auf `E:`, Prüfpunkt `DEPLOY01-M6-Ende`) → M7 WDS (danach Rücksetzen auf `DEPLOY01-M6-Ende`) → M8 Standort (Prüfpunkte `DC01-M8-Ende`/`DEPLOY01-M8-Ende`) → M9 bis M11 (`DEPLOY01-M11-Ende`) → M14. `CL01` und `CL02` werden vor jeder Bereitstellung überschrieben; `CL02` wird in Modul 5 verallgemeinert und in Modul 7 zurückgesetzt. Namen (`DEPLOY01`, `10.70.0.20`, `LAB`, `E:\Images`) sind in allen Modulen gleich verwendet (per Suche geprüft). Hinweis auf das Risiko beim Zurücksetzen eines Domänenmitglieds steht in A.3.
5. **Lernziele, Lerneinheiten, Kontrollfragen:** Per Skript geprüft: Alle 55 Lernziele sind in einer Praxisaufgabe mit „Lernziel n“ markiert; alle 55 Lerneinheiten sind in mindestens einer Aufgabe („Einheit x.y“) und einer Kontrollfrage („(x.y)“) belegt. Stichprobe: Einheit 7.2 mit Aufgabe 2 und Frage 3; Einheit 12.3 mit Aufgabe 3 und Frage 3.
6. **Einschränkungen und Rückbau:** Kein Pflichtmodul hängt von Modul 12 oder 13 ab (Modul 12 liest Beispieldateien, Modul 13 ist eine Vorführung in getrennter VM). Rückbau: Prüfpunkte; WDS wird durch Zurücksetzen entfernt; Ausweich-VM `DEPLOY01-CM-fertig` sichert die Module 9 bis 11 und 14, falls Modul 8 scheitert. Die Pflichtmodule 8 bis 11 und 14 hängen aber von einer lauffähigen Configuration-Manager-Installation ab; das ist ein bewusst benanntes Risiko (siehe offene Punkte).
7. **Infrastruktur über eine VM hinaus:** Vier VMs auf einem privaten Switch (24 GB VM-Arbeitsspeicher, Host 32 GB); Abhängigkeiten der VMs: `DEPLOY01` braucht `DC01` (Domäne, DHCP); `CL01` und `CL02` brauchen beide. Gemeinsames Zurücksetzen von `DC01` und `DEPLOY01` nach Modul 8 ist festgelegt.
8. **Internet, Namen, Dateiwege:** Labor ohne Internet, Beschaffung am Host; Domäne `lab.example.internal`, Adressen aus RFC 1918; ISO-Dateien in `D:\ISO`, Abbilder in `E:\Images`. Ausnahme FOG (Internet für den Installer) als getrennte Vorführung. Keine erfundenen URLs; alle Links stammen aus Suchtreffern oder Abruf vom 08.11.2026.
9. **Befehle und Sicherheit:** Destruktive Befehle (`diskpart … clean`, `Dism /Apply-Image`, Sysprep, Zurücksetzen von Prüfpunkten) laufen nur in den leeren Labor-VMs und mit Vorbedingung (Prüfpunkt). Kennwörter stehen nicht im Dokument (Platzhalter); Konten sind nach dem Prinzip der minimalen Rechte beschrieben (`svc-osd-read`, `svc-osd-join`); die Gefahr von Kennwörtern in Boot-Abbild und Regeldateien ist Lerninhalt. Das Labor setzt Configuration Manager ohne HTTPS ein; das gilt nur im isolierten Labor. Windows-Befehle wurden nicht ausgeführt (A.3).

**Offene Punkte:**

* Alle Windows-Befehle und Menüpfade vor dem Kurs im Labor ausführen, besonders `copype`/`MakeWinPEMedia`, `wdsutil`, `Import-WdsBootImage`, `Export-WindowsDriver`, PowerShell Direct (`Copy-Item -ToSession/-FromSession`), die Speicherorte der Antwortdatei (`W:\Windows\Panther\unattend.xml`) und die Bezeichnungen in der Configuration-Manager-Konsole.
* Verfügbarkeit und Laufzeit einer Evaluation von Configuration Manager 2609, SQL Server 2022 und Windows Server 2025 klären; ohne Evaluation fallen die Module 8 bis 11 und 14 auf die Ausweich-VM zurück oder entfallen. Entscheidung des Kursleiters nötig.
* Die nicht gelesenen Seiten (WDS-Abkündigung auf support.microsoft.com, Härtung zu CVE-2026-0386) lesen und in Modul 7 und 1 einarbeiten; prüfen, ob das Verhalten von WDS ohne „hands-free“ die Übung in Modul 7 beeinflusst.
* Ob MDT 8456 noch zum Download steht und mit ADK 10.1.26100.x und Windows 11 läuft, ist nicht bestätigt (Modul 12 kommt ohne aus).
* Zeitaufwand unerprobt: 108 UE mit Labor sind eine Schätzung; besonders Modul 8 (Installation von SQL Server und Configuration Manager in einer VM) hängt von der Hardware ab.
* Bezeichnungen und Daten der Umbenennung von SCCM zu MECM zu Configuration Manager sind nicht geprüft.
