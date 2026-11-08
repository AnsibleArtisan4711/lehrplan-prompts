# Lehrplan: Windows-11-Client-Administration

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 12 Module, 108 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows 11 (Enterprise/Pro), Active-Directory-Domäne (Client-Sicht), PowerShell, Hyper-V (nur als Laborumgebung) |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen: Aufbau und Betrieb des Domain Controllers (Windows Server, Active Directory) sowie PC-Hardware sind eigene Kurse, hier nur kurze Verweise. Der Domain Controller ist vorbereitet und wird nur als Gegenstelle benutzt. Keine Cloud-Verwaltung (Microsoft Entra ID, Intune), keine Zertifizierungsvorbereitung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Windows 11: Editionen, Versionen, Lebenszyklus | 1 | 7 |
| 2 | Installation und Ersteinrichtung | 1 | 10 |
| 3 | Bereitstellung: Antwortdatei und Image | 2 | 9 |
| 4 | Konten, Gruppen und Rechte | 1 | 10 |
| 5 | Netzwerk und Domänenbeitritt | 1 | 10 |
| 6 | Gruppenrichtlinien und Windows LAPS | 1 | 9 |
| 7 | BitLocker | 1 | 9 |
| 8 | Microsoft Defender und Firewall | 1 | 9 |
| 9 | Updates | 1 | 8 |
| 10 | Sicherung und Wiederherstellung | 1 | 9 |
| 11 | Fernwartung | 2 | 7 |
| 12 | Fehlersuche und Leistung | 1 | 11 |
| **Gesamt** | **10 Pflichtmodule, 2 Vertiefungsmodule** | | **108** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln die Kernkompetenzen. Module mit Priorität 2 (3 und 11) dienen der Vertiefung und können bei Zeitmangel gekürzt oder als Selbststudium ausgelagert werden. Kein Pflichtmodul setzt ein Modul mit Priorität 2 voraus: Alle Pflichtmodule starten von dem Zustand, den Modul 2 (manuelle Installation) erzeugt, nicht von einem Ergebnis aus Modul 3.*

### 2. Quellen

Alle Microsoft-Learn-Angaben stammen aus Suchtreffer-Auszügen vom 08.11.2026 (Seiten nicht vollständig gelesen). Wo eine Aussage nur aus dem Gedächtnis oder aus Foren stammt, ist sie im Text als „nicht bestätigt“ gekennzeichnet.

* **Windows 11 requirements** (Microsoft Learn): [https://learn.microsoft.com/windows/whats-new/windows-11-requirements](https://learn.microsoft.com/windows/whats-new/windows-11-requirements). Mindestanforderungen (2 Kerne, 4 GB RAM, 64 GB, UEFI mit Secure Boot, TPM 2.0), VM-Anforderungen (Generation 2, Hyper-V: Secure Boot und virtuelles TPM). Stand der Seite nicht angegeben.
* **Windows 11 release information** und **Supported versions of Windows client** (Microsoft Learn): [https://learn.microsoft.com/windows/release-health/windows11-release-information](https://learn.microsoft.com/windows/release-health/windows11-release-information), [https://learn.microsoft.com/windows/release-health/supported-versions-windows-client](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client). Versionen 23H2 bis 26H2, Ende der Updates je Edition; „Last Updated: 2026-09-29“, Tabelle „Latest revision“ 28.10.2026. Dazu **Windows message center** ([https://learn.microsoft.com/windows/release-health/windows-message-center](https://learn.microsoft.com/windows/release-health/windows-message-center)): Eintrag vom 13.10.2026, Windows 11 24H2 (Home und Pro) hat das Ende der Updates erreicht.
* **Windows 11, version 26H1** ([https://learn.microsoft.com/windows/whats-new/windows-11-version-26h1](https://learn.microsoft.com/windows/whats-new/windows-11-version-26h1)): nur vorinstalliert auf bestimmten neuen Geräten, kein Feature-Update für bestehende Geräte.
* **BitLocker overview** ([https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/](https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/)), **manage-bde** ([https://learn.microsoft.com/windows-server/administration/windows-commands/manage-bde](https://learn.microsoft.com/windows-server/administration/windows-commands/manage-bde)), **manage-bde on** ([https://learn.microsoft.com/windows-server/administration/windows-commands/manage-bde-on](https://learn.microsoft.com/windows-server/administration/windows-commands/manage-bde-on)) und **BitLocker recovery: known issues** ([https://learn.microsoft.com/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues](https://learn.microsoft.com/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues)): Geräteverschlüsselung, Sicherung des Wiederherstellungsschlüssels in AD DS, `manage-bde -protectors -adbackup C:`.
* **Join a computer to a domain** ([https://learn.microsoft.com/windows-server/identity/ad-ds/manage/join-computer-to-domain](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/join-computer-to-domain)) und **Add-Computer** ([https://learn.microsoft.com/powershell/module/microsoft.powershell.management/add-computer?view=powershell-5.1](https://learn.microsoft.com/powershell/module/microsoft.powershell.management/add-computer?view=powershell-5.1)): Beitritt über Systemsteuerung, Einstellungen, `netdom`, `Add-Computer`; Reparatur der Vertrauensstellung mit `Test-ComputerSecureChannel`; Hinweis auf KB5020276 (Härtung des Domänenbeitritts).
* **Configure Windows Update client policies** ([https://learn.microsoft.com/windows/deployment/update/waas-configure-wufb](https://learn.microsoft.com/windows/deployment/update/waas-configure-wufb)), **Walkthrough: Group Policy for Windows Update client policies** ([https://learn.microsoft.com/windows/deployment/update/waas-wufb-group-policy](https://learn.microsoft.com/windows/deployment/update/waas-wufb-group-policy)), **Deploy Windows client updates using WSUS** ([https://learn.microsoft.com/windows/deployment/update/waas-manage-updates-wsus](https://learn.microsoft.com/windows/deployment/update/waas-manage-updates-wsus)) und **Use Windows Update client policies and WSUS together** ([https://learn.microsoft.com/windows/deployment/update/wufb-wsus](https://learn.microsoft.com/windows/deployment/update/wufb-wsus)).
* **Windows Recovery Environment (Windows RE)** ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference?view=windows-11](https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference?view=windows-11)) und **REAgentC** ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11](https://learn.microsoft.com/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)): Wiederherstellungsumgebung, Systemwiederherstellung, Reset.
* **Enable Remote Desktop on your PC** ([https://learn.microsoft.com/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access)) und **Enable-PSRemoting** ([https://learn.microsoft.com/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.6](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.6)).
* **What is Windows LAPS?** ([https://learn.microsoft.com/windows-server/identity/laps/laps-overview](https://learn.microsoft.com/windows-server/identity/laps/laps-overview)) und **Key concepts in Windows LAPS** ([https://learn.microsoft.com/windows-server/identity/laps/laps-concepts-overview](https://learn.microsoft.com/windows-server/identity/laps/laps-concepts-overview)): Verwaltung und Sicherung des lokalen Administratorkennworts; Hinweis, dass das Zurücksetzen einer VM auf einen Prüfpunkt Kennwortabweichungen erzeugen kann.
* **Answer files (unattend.xml)** ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11](https://learn.microsoft.com/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11)) und **Automate Windows Setup** ([https://learn.microsoft.com/windows-hardware/manufacture/desktop/automate-windows-setup?view=windows-11](https://learn.microsoft.com/windows-hardware/manufacture/desktop/automate-windows-setup?view=windows-11)): `Autounattend.xml` auf dem USB-Stick, Windows System Image Manager, Konfigurationsphasen.
* **Microsoft Defender Antivirus PowerShell** ([https://learn.microsoft.com/defender-endpoint/use-powershell-cmdlets-microsoft-defender-antivirus](https://learn.microsoft.com/defender-endpoint/use-powershell-cmdlets-microsoft-defender-antivirus)), **Defender-Ausnahmen** ([https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-exclusions-configure](https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-exclusions-configure)) und **Get-NetFirewallProfile** ([https://learn.microsoft.com/powershell/module/netsecurity/get-netfirewallprofile?view=windowsserver2025-ps](https://learn.microsoft.com/powershell/module/netsecurity/get-netfirewallprofile?view=windowsserver2025-ps)).
* **Hyper-V, Generation-2-Sicherheit:** [https://learn.microsoft.com/windows-server/virtualization/hyper-v/learn-more/Generation-2-virtual-machine-security-settings-for-Hyper-V](https://learn.microsoft.com/windows-server/virtualization/hyper-v/learn-more/Generation-2-virtual-machine-security-settings-for-Hyper-V) (nur als Verweis in Learn gesehen, nicht abgerufen).
* **RFC 1918** ([https://datatracker.ietf.org/doc/html/rfc1918](https://datatracker.ietf.org/doc/html/rfc1918)) und **RFC 2606** ([https://www.rfc-editor.org/rfc/rfc2606](https://www.rfc-editor.org/rfc/rfc2606), nur als Suchtreffer gesehen): private Adressen und reservierte Namen. Die Top-Level-Domain `.internal` ist für die private Verwendung reserviert (Quelle hier nicht abgerufen, nicht bestätigt).
* **Windows-Evaluierungsversionen** (Windows 11 Enterprise, Windows Server): Download beim Microsoft Evaluation Center. Aktuelle Version, Laufzeit und Verfügbarkeit nicht geprüft.

### 3. Labor-Setup & Rahmenbedingungen

**Alle Befehle in diesem Lehrplan wurden nicht ausgeführt**, weil keine Windows-Umgebung zur Verfügung stand. Cmdlets, die Microsoft Learn belegt (siehe Quellen), sind nicht besonders markiert; alles andere ist als „nicht bestätigt“ gekennzeichnet und vor dem Kurs im Labor zu prüfen.

* **Hyper-V-Host:** Arbeitsplatzrechner mit Windows 11 Pro oder Enterprise, aktiviertem Hyper-V, mindestens 16 GB Arbeitsspeicher und 150 GB freiem Speicher (Annahme des Lehrplans). Beide VMs laufen gleichzeitig. Der Host braucht einmalig Internet für die ISO-Dateien.
* **Virtueller Switch (ab Modul 2):** Ein privater Switch `vSwitch-Lab` ohne Verbindung zum Heim- oder Produktivnetz. Beide VMs hängen ausschließlich daran. Es gibt kein Internet im Labor (siehe Hinweise zu Modul 2 und 9).
* **VM1 „DC01“ (vom Kursleiter vorbereitet):** Generation-2-VM, 2 vCPUs, 4 GB RAM, 60 GB, Windows Server (Evaluation; Version legt der Kursleiter fest und notiert sie), Domänencontroller mit DNS für die Domäne `lab.example.internal` (NetBIOS-Name `LAB`), Adresse `10.50.0.10/24`. Organisationseinheiten `Clients` und `Benutzer`; Benutzer `anna.muster` (Standardbenutzer), `ben.beispiel` (Standardbenutzer), Domänenadministrator `LAB\labadmin`; Kennwörter vergibt der Kursleiter. Prüfpunkt `DC-Basis`.
* **VM2 „CL01“ (von den Lernenden in Modul 2 gebaut):** Generation-2-VM, 2 vCPUs, 4 GB RAM, 80 GB (dynamisch), aktiviertes virtuelles TPM, Secure Boot aktiviert, Windows 11 Enterprise (Evaluation) aus dem Microsoft Evaluation Center. Adresse `10.50.0.21/24`, lokales Konto `labadmin`. Ab Modul 10 kommt eine zweite virtuelle Festplatte (20 GB) hinzu, die die Lernenden anlegen, initialisieren (GPT) und mit NTFS als `D:` formatieren.
* **Namens- und Adressplan:**

| Bezeichnung | Name / Adresse | Verwendet in |
| :--- | :--- | :--- |
| Lab-Netz | `10.50.0.0/24` (RFC 1918), kein Gateway | Modul 2 bis 12 |
| Domain Controller, DNS | `DC01`, `10.50.0.10` | Modul 5 bis 12 |
| Client | `CL01`, `10.50.0.21` | Modul 2 bis 12 |
| Domäne | `lab.example.internal` | Modul 5 bis 12 |
| Übungsnetz für die Adressplanung (nur Rechnung) | `10.60.0.0/24` | Modul 5 |

* **Prüfpunkte (Hyper-V-Checkpoints):** `CL01-M2-Ende` (nach Installation, vor Domänenbeitritt), `CL01-M5-Join` (nur vorübergehend in Modul 5), `CL01-M5-Ende` und `DC-M5-Ende` (nach Beitritt und Reparatur, nur gemeinsam zurücksetzen), `CL01-M7-Ende`. **Achtung:** Wird CL01 nach dem Domänenbeitritt auf einen älteren Prüfpunkt zurückgesetzt, stimmt das Kennwort des Computerkontos unter Umständen nicht mehr mit der Domäne überein (Learn nennt dies für Windows LAPS; die Vertrauensstellung ist dann zu reparieren, siehe Modul 5 und 12). Ein Prüfpunkt ist keine Datensicherung (siehe Modul 10).
* **Vom Kursleiter bereitzustellen:** DC01 mit Prüfpunkt, ISO-Dateien, Vorlagen (leere Tabellen für Inventar, Prüfprotokolle), Kennwörter, Liste der Fehler für Modul 12 (siehe Kontrollwerte).
* **Nicht möglich im Labor (ohne Internet):** tatsächliches Einspielen von Windows-Updates, Aktualisierung der Defender-Signaturen, Quick Assist, Microsoft-Konto-Anmeldung. Die Module behandeln das nur auf Richtlinien- und Konzeptebene. Wer Internet im Lab zulassen will, trifft die Entscheidung bewusst und dokumentiert, dass der Switch dann nicht mehr privat ist.

## B. Detaillierter Modulaufbau

### Modul 1: Windows 11: Editionen, Versionen, Lebenszyklus
* **Priorität:** 1
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende prüfen, ob ein Gerät die Mindestanforderungen für Windows 11 erfüllt.
  * Nach Abschluss dieses Moduls kann der Lernende Windows-11-Versionen und Editionen unterscheiden und den Stand der Unterstützung für ein Gerät bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende Version, Edition, TPM- und Secure-Boot-Status auf einem Gerät auslesen.
* **Voraussetzungen:** Keine.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Mindestanforderungen: Prozessor, RAM, Speicher, UEFI, Secure Boot, TPM 2.0; Anforderungen an VMs | 2 |
| 1.2 | Editionen (Home, Pro, Enterprise, Education), Versionen und jährliche Feature-Updates | 2 |
| 1.3 | Lebenszyklus: Ende der Updates je Edition, LTSC | 1 |
| 1.4 | Gerätedaten auslesen (Version, Edition, TPM, Secure Boot) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Anforderungen prüfen (Lernziel 1):** Bewerte diese Geräte. Prozessor-Kompatibilität, Grafik und Display gelten als erfüllt (Annahme).

   | Gerät | RAM | Speicher | TPM | Firmware | Secure Boot |
   | :--- | :--- | :--- | :--- | :--- | :--- |
   | A | 8 GB | 256 GB | 2.0 | UEFI | fähig, aktiv |
   | B | 4 GB | 128 GB | 1.2 | UEFI | fähig, aktiv |
   | C | 4 GB | 64 GB | 2.0 | Legacy-BIOS (MBR) | nicht fähig |
   | D | 2 GB | 128 GB | 2.0 | UEFI | fähig, aktiv |
   | E | 16 GB | 512 GB | 2.0 | UEFI | fähig, aber ausgeschaltet |
   | F | 4 GB | 60 GB | 2.0 | UEFI | fähig, aktiv |

   Begründe jede Entscheidung mit der verletzten Anforderung. Erkläre für Gerät E, ob „fähig“ oder „aktiv“ gefordert ist.
2. **Unterstützung bestimmen (Lernziel 2):** Stichtag ist der 30.11.2026. Ordne diesen Geräten anhand der Tabelle „Ende der Updates“ (aus den Quellen, siehe unten) „unterstützt“ oder „Ende der Updates erreicht“ zu und nenne bei unterstützten Geräten die Restlaufzeit in Tagen:

   | Gerät | Version | Edition |
   | :--- | :--- | :--- |
   | PC-01 | 25H2 | Pro |
   | PC-02 | 24H2 | Pro |
   | PC-03 | 24H2 | Enterprise |
   | PC-04 | 23H2 | Enterprise |
   | PC-05 | 26H2 | Pro |
   | PC-06 | 23H2 | Pro |
   | PC-07 | 25H2 | Enterprise |
   | PC-08 | 24H2 | Pro |

   Ende der Updates laut Learn (abgerufen 08.11.2026): 23H2 Pro: beendet, Enterprise 10.11.2026; 24H2 Pro 13.10.2026, Enterprise 12.10.2027; 25H2 Pro 12.10.2027, Enterprise 10.10.2028; 26H2 Pro 10.10.2028, Enterprise 09.10.2029. Beantworte zusätzlich: Welche dieser Geräte sind am 30.06.2027 noch unterstützt?
3. **Gerätedaten auslesen (Lernziel 3):** Notiere auf dem Hyper-V-Host (Windows 11) Version und Build mit `winver`, die Edition mit `systeminfo` oder `Get-ComputerInfo`, den TPM-Status mit `Get-Tpm` und den Secure-Boot-Status mit `Confirm-SecureBootUEFI` (nicht bestätigt: die genauen Ausgabefelder; `Confirm-SecureBootUEFI` meldet auf Geräten ohne UEFI einen Fehler). Ordne die Version der Tabelle aus Aufgabe 2 zu und bestimme das Datum, bis zu dem der Host (je nach Edition) Updates erhält. Wiederhole die Abfrage in Modul 2 auf CL01.

#### Kontrollfragen
1. Welche Mindestanforderungen stellt Windows 11 an Prozessor, Arbeitsspeicher, Speicher, Firmware und TPM?
2. Wie unterscheidet sich die Unterstützungsdauer von Windows 11 Pro und Windows 11 Enterprise?
3. Welche Besonderheit hat Windows 11, Version 26H1?
4. Welche Voraussetzungen muss eine Hyper-V-VM erfüllen, damit Windows 11 darauf läuft (Generation, Sicherheit)?
5. Welche Bedingung nennt Learn für die Ersteinrichtung von Windows 11 Home?

---

### Modul 2: Installation und Ersteinrichtung
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Generation-2-VM mit virtuellem TPM und Secure Boot für Windows 11 anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Windows 11 installieren und die Ersteinrichtung (lokales Administratorkonto, Computername) durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Netzwerkadresse, Computername und Zeitzone per Einstellungen und PowerShell setzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Prüfpunkt anlegen und erklären, wofür er sich eignet und wofür nicht.
* **Voraussetzungen:** Modul 1

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Hyper-V-VM der Generation 2: Secure Boot, virtuelles TPM, Speicher, Switch | 2 |
| 2.2 | Windows-Setup: Datenträger, Edition, Ersteinrichtung (OOBE) | 3 |
| 2.3 | Grundkonfiguration: Computername, Adresse, Zeitzone, Sprache | 3 |
| 2.4 | Prüfpunkte: Nutzen und Grenzen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **VM anlegen (Lernziel 1):** Lege die VM `CL01` mit Generation 2, 2 vCPUs, 4 GB RAM, 80 GB Festplatte an, aktiviere Secure Boot und das virtuelle TPM (Sicherheitseinstellungen der VM) und verbinde den Adapter mit `vSwitch-Lab`. Hänge die Windows-11-ISO als DVD ein. Dokumentiere die Einstellungen mit einem Screenshot.
2. **Windows installieren (Lernziel 2):** Installiere Windows 11 Enterprise. Falls die Ersteinrichtung Internet oder ein Microsoft-Konto verlangt (nicht bestätigt für die verwendete Version), ordne der VM vorübergehend einen externen Switch zu, schließe die Einrichtung mit dem lokalen Konto `labadmin` ab und stelle die VM danach wieder auf `vSwitch-Lab` um. Notiere, an welcher Stelle der Einrichtung die Verbindung nötig war.
3. **Grundkonfiguration (Lernziel 3):** Setze die Adresse `10.50.0.21/24` (ohne Gateway, DNS `10.50.0.10`), den Computernamen `CL01` und die Zeitzone auf die Zeit von Wien. Beispiel (Schnittstellenname mit `Get-NetAdapter` prüfen, Zeitzonenname und Befehlsfolge nicht bestätigt):

   ```powershell
   Get-NetAdapter
   New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.50.0.21 -PrefixLength 24
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 10.50.0.10
   Rename-Computer -NewName CL01 -Restart
   Set-TimeZone -Id "W. Europe Standard Time"
   ```

   Prüfe die Erreichbarkeit von DC01 mit `ping 10.50.0.10` (nicht bestätigt: Die Antwort auf Ping kann durch die Firewall blockiert sein; in diesem Fall ist das Ergebnis zu dokumentieren und nicht zu umgehen, bevor Modul 8 behandelt ist).
4. **Prüfpunkt (Lernziel 4):** Lege den Prüfpunkt `CL01-M2-Ende` an. Beschreibe in drei Sätzen, warum ein Prüfpunkt keine Datensicherung ersetzt.

#### Kontrollfragen
1. Warum braucht Windows 11 in einer Hyper-V-VM Generation 2?
2. Welche Rolle spielt das virtuelle TPM für spätere Kapitel (BitLocker)?
3. Welche Adresse und welche DNS-Einstellung braucht CL01 für den Domänenbeitritt, und warum?
4. Warum darf `vSwitch-Lab` keine Verbindung zum Heimnetz haben?

---

### Modul 3: Bereitstellung: Antwortdatei und Image
* **Priorität:** 2
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Phasen der Windows-Installation und die Rolle einer Antwortdatei erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Antwortdatei mit dem Windows System Image Manager erstellen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Windows-Image mit DISM untersuchen und die Schritte einer image-basierten Bereitstellung beschreiben.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Installationsphasen und Konfigurationsphasen (windowsPE, specialize, oobeSystem) | 2 |
| 3.2 | Antwortdatei mit dem Windows System Image Manager | 3 |
| 3.3 | Image-Werkzeuge: WIM-Datei, DISM, Index und Edition | 2 |
| 3.4 | Bereitstellungswege im Überblick (USB, Netzwerk, Hersteller-Image) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Phasen zuordnen (Lernziel 1):** Ordne diese Einstellungen den Phasen zu: Partitionierung der Festplatte, Computername, Anlage des lokalen Benutzers `labadmin`, Zeitzone. Begründe jede Zuordnung. (Die Zuordnung ist mit der Learn-Seite „Answer files“ abzugleichen; die Phasen `windowsPE`, `specialize`, `oobeSystem` werden dort genannt.)
2. **Antwortdatei erstellen (Lernziel 2):** Installiere das Windows ADK mit dem Windows System Image Manager auf dem Host (Internet am Host nötig; Version des ADK nicht bestätigt), erstelle einen Katalog aus der `install.wim` der ISO und entwirf eine Antwortdatei `Autounattend.xml` mit Computername `CL01`, Zeitzone und lokalem Konto `labadmin` (Kennwort nicht in der Datei dokumentieren, sondern Platzhalter `<vom Kursleiter>`). Validiere sie im Programm. Die Datei wird nicht in der Laborumgebung eingesetzt; der Einsatz (Learn: `Autounattend.xml` im Stammverzeichnis eines USB-Laufwerks) ist in dieser Fassung nicht geprüft.
3. **Image untersuchen (Lernziel 3):** Mounte die ISO in der VM oder auf dem Host und lies mit `DISM /Get-ImageInfo /ImageFile:<Pfad>\sources\install.wim` die enthaltenen Editionen und Indizes aus. Notiere den Index der Edition Enterprise (Pfad und Dateiname der WIM-Datei nicht bestätigt, in manchen ISO-Dateien kann es eine `.esd` sein).
4. **Bereitstellungsweg wählen (Lernziel 3):** Wähle für drei Szenarien (10 Geräte in einem Büro, 300 Geräte an einem Standort, Hersteller-Geräte mit eigenem Image) einen Bereitstellungsweg und begründe.

#### Kontrollfragen
1. Wozu dient eine Antwortdatei, und wo sucht Windows-Setup sie, wenn keine angegeben ist?
2. Welche Phase eignet sich für Einstellungen, die beim ersten Start des installierten Systems gelten sollen?
3. Warum gehören Kennwörter nicht im Klartext in eine Antwortdatei?
4. Was ist der Unterschied zwischen einer manuellen und einer image-basierten Bereitstellung?

---

### Modul 4: Konten, Gruppen und Rechte
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende lokale Benutzer und Gruppen anlegen, ändern und entfernen.
  * Nach Abschluss dieses Moduls kann der Lernende Konten- und Anmeldearten (lokal, Microsoft-Konto, Domäne) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende NTFS-Berechtigungen setzen und die effektiven Rechte eines Benutzers bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende die Benutzerkontensteuerung (UAC) und die Rolle von Administratorrechten erklären.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Lokale Benutzer und Gruppen (Benutzer, Administratoren, Remotedesktopbenutzer) | 3 |
| 4.2 | Kontoarten: lokal, Microsoft-Konto, Domäne; Anmeldung | 2 |
| 4.3 | NTFS-Berechtigungen, Vererbung und effektive Rechte | 3 |
| 4.4 | Benutzerkontensteuerung und Prinzip der geringsten Rechte | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Lokale Konten (Lernziel 1):** Lege auf CL01 die lokalen Benutzer `lokal.eins` und `lokal.zwei` mit Kennwörtern an, die du nicht dokumentierst, sondern in einer Kennwortliste des Kursleiters ablegst. Füge `lokal.zwei` zur Gruppe der Administratoren hinzu und danach wieder ab. Verwende `Get-LocalUser`, `New-LocalUser`, `Add-LocalGroupMember`, `Remove-LocalGroupMember` (Parameter nicht bestätigt). Dokumentiere die Gruppenmitgliedschaften vorher und nachher.
2. **Kontoarten (Lernziel 2):** Erstelle eine Tabelle mit Spalten Anmeldeart, Verwaltung, Wiederherstellung bei Kennwortverlust, Eignung für den Firmen-Client. Markiere, welche Angaben du aus Learn belegen kannst (Home braucht Microsoft-Konto und Internet bei der Einrichtung) und welche nicht.
3. **NTFS-Rechte (Lernziel 3):** Lege `C:\Daten\Projekt` an. Setze mit `icacls` für `lokal.eins` Lesen und Ausführen und für `lokal.zwei` Ändern, ohne die Vererbung auf Ordnerebene zu entfernen (Parameter nicht bestätigt). Prüfe die Rechte mit `icacls C:\Daten\Projekt` und Anmeldung als beide Benutzer. Beantworte: Welche effektiven Rechte hat `lokal.zwei`, wenn er zusätzlich in einer Gruppe mit „Verweigern: Schreiben“ steckt?
4. **Rechte begrenzen (Lernziel 4):** Beschreibe an drei Beispielen, wann Windows die UAC-Abfrage anzeigt und was beim Eingeben von Zugangsdaten passiert. Begründe, warum Mitarbeiter am Alltagsarbeitsplatz keine Administratorrechte haben sollen.

#### Kontrollfragen
1. Welche Gruppen sind für die tägliche Arbeit und für die Fernwartung relevant?
2. Wie wirken Vererbung und ausdrückliche Berechtigungen zusammen?
3. Welche Art von Eintrag gewinnt bei einem Konflikt zwischen „Zulassen“ und „Verweigern“? (Antwort aus dem Material des Kurses belegen.)
4. Warum sollten Administratorrechte im Alltag nicht dauerhaft verwendet werden?

---

### Modul 5: Netzwerk und Domänenbeitritt
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Netzwerkeinstellungen eines Clients (Adresse, Maske, DNS, Profil) auslesen und ändern.
  * Nach Abschluss dieses Moduls kann der Lernende Adressbereiche mit Präfixlängen für gegebene Hostzahlen planen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Windows-11-Client einer Domäne hinzufügen und den Beitritt prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine gestörte Vertrauensstellung zwischen Client und Domäne feststellen und reparieren.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Netzwerkeinstellungen und Diagnosewerkzeuge (`ipconfig`, `nslookup`, `Test-NetConnection`) | 2 |
| 5.2 | Adressplanung mit Präfixlängen | 2 |
| 5.3 | Domänenbeitritt: Voraussetzungen, Wege, Prüfung | 3 |
| 5.4 | Computerkonto, Vertrauensstellung und Reparatur | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Einstellungen auslesen (Lernziel 1):** Lies auf CL01 die Netzwerkkonfiguration aus (`ipconfig /all`, `Get-NetIPConfiguration`, `Get-DnsClientServerAddress`) und weise nach, dass DNS auf `10.50.0.10` zeigt. Prüfe die Namensauflösung mit `nslookup dc01.lab.example.internal` und die Erreichbarkeit des Verzeichnisdienstes mit `Test-NetConnection -ComputerName 10.50.0.10 -Port 389` (Port und Verhalten nicht bestätigt; bei fehlgeschlagenem Test Ursache analysieren, nicht übergehen).
2. **Adressplanung (Lernziel 2):** Im Übungsnetz `10.60.0.0/24` werden drei Netze benötigt: A mit 100 Hosts, B mit 50 Hosts, C mit 25 Hosts. Wähle jeweils die kleinste Präfixlänge, die ausreicht, und lege die Netze lückenlos hintereinander (größtes zuerst) ab `10.60.0.0` fest. Gib für jedes Netz Netzadresse, ersten und letzten Host und Broadcast an.
3. **Beitritt (Lernziel 3):** Trete CL01 der Domäne `lab.example.internal` bei, und zwar über die Einstellungen (Konten, Zugriff auf Arbeits- oder Schulkonto, „Dieses Gerät einer lokalen Active Directory-Domäne hinzufügen“, nach Learn). Stelle zusätzlich die beiden Befehlsvarianten aus Learn gegenüber, ohne sie auszuführen: `netdom join %COMPUTERNAME% /domain:lab.example.internal /userd:<Benutzer> /passwordd:*` und `Add-Computer -DomainName lab.example.internal -Credential (Get-Credential)` mit anschließendem `Restart-Computer`. Prüfe danach in der Active-Directory-Verwaltung auf DC01, in welcher Organisationseinheit das Computerkonto steht, verschiebe es in `Clients` und melde dich als `LAB\anna.muster` an.
4. **Vertrauensstellung (Lernziel 4):** Lege nach dem Beitritt den Prüfpunkt `CL01-M5-Join` an. Ändere dann das Kennwort des Computerkontos (`Reset-ComputerMachinePassword -Credential (Get-Credential)`, danach `Restart-Computer`; Verhalten nicht bestätigt) und setze CL01 auf `CL01-M5-Join` zurück, ohne DC01 zurückzusetzen. Beobachte den Anmeldefehler, melde dich mit dem lokalen Konto an und führe `Test-ComputerSecureChannel` aus. Liefert er `False`, repariere mit `Test-ComputerSecureChannel -Repair -Credential (Get-Credential)` oder, falls nötig, mit `Reset-ComputerMachinePassword` und `Restart-Computer -Force` (Schritte nach Learn). Dokumentiere Ausgangsfehler und Behebung. Lösche den Prüfpunkt `CL01-M5-Join` und lege danach die Prüfpunkte `CL01-M5-Ende` und `DC-M5-Ende` an (beide VMs ausgeschaltet).

#### Kontrollfragen
1. Warum muss der DNS-Server eines Domänenmitglieds auf den Domain Controller zeigen?
2. Welche drei Wege zum Domänenbeitritt nennt Learn?
3. Was ist ein Computerkonto, und was bedeutet „Vertrauensstellung zwischen Arbeitsstation und Domäne fehlgeschlagen“?
4. Wie viele nutzbare Hostadressen hat ein `/25`-, `/26`- und `/27`-Netz?
5. Warum ist ein Zurücksetzen eines Domänenmitglieds auf einen älteren Prüfpunkt riskant?

---

### Modul 6: Gruppenrichtlinien und Windows LAPS
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Gruppenrichtlinien auf Computer und Benutzer wirken (Verknüpfung, Reihenfolge, Aktualisierung).
  * Nach Abschluss dieses Moduls kann der Lernende eine Gruppenrichtlinie für Clients anlegen, verknüpfen und ihre Wirkung auf dem Client nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende Windows LAPS für lokale Administratorkennwörter einrichten und das Kennwort abrufen.
  * Nach Abschluss dieses Moduls kann der Lernende beschreiben, welche Risiken ein gemeinsames lokales Administratorkennwort hat.
* **Voraussetzungen:** Modul 4, Modul 5

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Gruppenrichtlinien: Verknüpfung an Organisationseinheiten, Verarbeitungsreihenfolge, Aktualisierung | 3 |
| 6.2 | Richtlinie anlegen und prüfen (`gpupdate`, `gpresult`) | 3 |
| 6.3 | Windows LAPS: Zweck, Einrichtung, Kennwortabruf | 3 |

#### Praxisaufgaben (Hands-on Lab)
Diese Aufgaben laufen auf DC01 (Gruppenrichtlinienverwaltung) und CL01. Die Menüpfade sind nicht bestätigt.
1. **Reihenfolge (Lernziel 1):** Beschreibe an einem Beispiel mit drei Richtlinien (Domäne, Organisationseinheit `Clients`, lokal), welche Einstellung gewinnt, wenn alle denselben Wert konfigurieren, und wann eine Richtlinie nicht angewendet wird (Computerkonto in der falschen Organisationseinheit).
2. **Richtlinie anlegen (Lernziel 2):** Lege auf DC01 eine Richtlinie `CL-Basis` an, verknüpfe sie mit der Organisationseinheit `Clients` und setze eine harmlose, sichtbare Einstellung (zum Beispiel einen Hintergrund oder eine Sperrbildschirm-Zeitüberschreitung; gewählte Einstellung dokumentieren). Aktualisiere auf CL01 mit `gpupdate /force`, prüfe mit `gpresult /r`, welche Richtlinien angewendet wurden, und weise die Wirkung nach.
3. **Windows LAPS (Lernziel 3):** Erweitere das Schema und die Berechtigungen für die Organisationseinheit `Clients` (nicht bestätigt: `Update-LapsADSchema`, `Set-LapsADComputerSelfPermission`; bei einem Domänencontroller mit Windows Server 2025 ist das Schema nach Learn ggf. schon vorhanden). Lege eine Richtlinie an, die das Kennwort des lokalen Administratorkontos in Active Directory sichert (Pfad der Richtlinie nicht bestätigt, laut Quelle sind „BackupDirectory“ und „Administratorkonto“ Teil der Richtlinie). Rufe nach der Verarbeitung auf CL01 das Kennwort auf DC01 ab (nicht bestätigt: `Get-LapsADPassword`), melde dich damit am lokalen Administratorkonto an und dokumentiere nur, dass der Abruf funktioniert hat, nicht das Kennwort.
4. **Risiko beschreiben (Lernziel 4):** Beschreibe in einem Absatz, welches Risiko ein lokales Administratorkennwort darstellt, das auf allen Clients gleich ist, und wie Windows LAPS es verringert (Quelle: Learn, „What is Windows LAPS?“).

#### Kontrollfragen
1. In welcher Reihenfolge werden Gruppenrichtlinien angewendet, und wie lässt sich das Ergebnis auf dem Client prüfen?
2. Warum gehört ein Computer in die passende Organisationseinheit, damit eine Richtlinie wirkt?
3. Was macht Windows LAPS, und welche Geräte unterstützt es laut Learn?
4. Welches Problem tritt auf, wenn eine VM mit Windows LAPS auf einen älteren Prüfpunkt zurückgesetzt wird?

---

### Modul 7: BitLocker
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie BitLocker mit TPM, Schutzvorrichtungen (Protektoren) und Wiederherstellungskennwort arbeitet.
  * Nach Abschluss dieses Moduls kann der Lernende BitLocker auf dem Systemlaufwerk aktivieren und den Zustand prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Sicherung des Wiederherstellungsschlüssels in Active Directory einrichten und nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende ein gesperrtes Gerät mit dem Wiederherstellungskennwort entsperren.
* **Voraussetzungen:** Modul 2, Modul 6

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Grundlagen: Verschlüsselung, TPM, Protektoren, Geräteverschlüsselung | 2 |
| 7.2 | BitLocker aktivieren und prüfen (`manage-bde`, Einstellungen) | 2 |
| 7.3 | Wiederherstellungsschlüssel in AD DS sichern (Richtlinie, Prüfung) | 3 |
| 7.4 | Wiederherstellung durchführen | 2 |

#### Praxisaufgaben (Hands-on Lab)
**Sicherheitsregel für dieses Modul:** Vor jedem Schritt, der Verschlüsselung oder Wiederherstellung auslöst, ist der Prüfpunkt `CL01-M5-Ende` (beide VMs ausgeschaltet gesichert) vorhanden und das Wiederherstellungskennwort nachweislich in AD gesichert.
1. **Konzept (Lernziel 1):** Erkläre in einer Skizze, wie der Schlüssel des Systemlaufwerks durch TPM-Protektor und Wiederherstellungskennwort geschützt wird. Nenne nach Learn, wann „Geräteverschlüsselung“ automatisch startet (abhängig vom Konto) und was bei lokalem Konto passiert („bleibt ungeschützt, obwohl die Daten verschlüsselt sind“).
2. **Aktivieren (Lernziel 2):** Aktiviere BitLocker für `C:` auf CL01 über die Systemsteuerung oder per Befehl (nach Learn: `manage-bde -on C: -recoverypassword`; ob dabei zusätzlich ein TPM-Protektor entsteht, nicht bestätigt, daher mit `manage-bde -protectors -get C:` prüfen). Starte neu, falls ein Hardwaretest verlangt wird, und beobachte den Fortschritt mit `manage-bde -status`. Dokumentiere Verschlüsselungsmethode und Status.
3. **Sicherung in AD (Lernziel 3):** Aktiviere auf DC01 in der Richtlinie für `Clients` die Richtlinie „Choose how BitLocker-protected operating system drives can be recovered“ mit Speicherung in AD DS (laut Learn Voraussetzung für die Sicherung). Sichere bei bereits verschlüsseltem Laufwerk nach Learn manuell: `manage-bde -protectors -adbackup C: -id <ID des Wiederherstellungskennwort-Protektors>` (ID aus `manage-bde -protectors -get C:`; die genaue Syntax mit `-id` nicht bestätigt). Weise die Sicherung auf DC01 nach (nicht bestätigt: Abfrage des Attributs `msFVE-RecoveryPassword` am Computerobjekt mit PowerShell oder Registerkarte „BitLocker-Wiederherstellung“ im Computerobjekt).
4. **Wiederherstellung (Lernziel 4):** Löse die Wiederherstellung gezielt aus (nach Learn gibt es `manage-bde -forcerecovery`; Verhalten nicht bestätigt) und gib auf der Wiederherstellungsseite das aus AD abgerufene Kennwort ein. Notiere, welche Kennwortlänge und -form angezeigt werden (nicht bestätigt: 48 Ziffern in acht Gruppen).
   *Nur ausführen, wenn Aufgabe 3 erfolgreich nachgewiesen ist und der Prüfpunkt besteht.* Lege `CL01-M7-Ende` an.

#### Kontrollfragen
1. Welche Aufgabe hat das TPM bei BitLocker?
2. Warum ist die Sicherung des Wiederherstellungsschlüssels vor der Verschlüsselung der Flotte eine organisatorische Pflicht?
3. Was passiert laut Learn bei Geräteverschlüsselung auf einem Gerät mit lokalem Konto?
4. Welche Ereignisse können eine BitLocker-Wiederherstellung auslösen? (Antwort aus dem Kurs belegen, Beispiele: Änderung der Startumgebung, erzwungene Wiederherstellung.)

---

### Modul 8: Microsoft Defender und Firewall
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zustand von Microsoft Defender Antivirus auslesen und einen Scan auslösen.
  * Nach Abschluss dieses Moduls kann der Lernende Ausnahmen setzen und die Risiken von Ausnahmen beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende die Firewall-Profile (Domäne, Privat, Öffentlich) unterscheiden und Regeln anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Verbindungsprobleme auf Firewall-Regeln zurückführen.
* **Voraussetzungen:** Modul 2, Modul 4, Modul 5

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Defender Antivirus: Zustand, Scans, Bedrohungsverlauf, Signaturen | 3 |
| 8.2 | Ausnahmen und Manipulationsschutz | 2 |
| 8.3 | Firewall-Profile und Regeln | 2 |
| 8.4 | Fehlersuche an der Firewall | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Zustand und Scan (Lernziel 1):** Lies mit `Get-MpComputerStatus` den Zustand aus, löse mit `Start-MpScan -ScanType QuickScan` einen Schnellscan aus und prüfe Funde mit `Get-MpThreat` (Cmdlets nach Learn). Notiere das Alter der Signaturen und erkläre, warum es im Labor ohne Internet veraltet ist. Eine Testdatei zum Auslösen des Virenschutzes (EICAR-Testdatei, Zeichenfolge von eicar.org) wird nur vom Kursleiter bereitgestellt und nicht in diesem Dokument abgedruckt.
2. **Ausnahmen (Lernziel 2):** Lege mit `Add-MpPreference -ExclusionPath "C:\Daten\Projekt"` eine Ausnahme an (nach Learn), prüfe sie mit `Get-MpPreference` und entferne sie wieder mit `Remove-MpPreference -ExclusionPath`. Beschreibe drei Risiken von zu weit gefassten Ausnahmen und erkläre, was der Manipulationsschutz dagegen tun soll (nach Learn: kann organisationsverwaltete Ausnahmelisten schützen).
3. **Firewall-Regeln (Lernziel 3):** Zeige die Profile mit `Get-NetFirewallProfile` und das aktive Profil von CL01 (nach dem Beitritt sollte es das Domänenprofil sein; nicht bestätigt, mit `Get-NetConnectionProfile` prüfen). Lege eine eingehende Regel an, die TCP-Port 8080 zulässt, und eine, die ihn blockiert, prüfe die Rangfolge und entferne beide wieder (`New-NetFirewallRule`, `Remove-NetFirewallRule`; Parameter nicht bestätigt).
4. **Verbindung analysieren (Lernziel 4):** Der Kursleiter blockiert auf CL01 eingehenden Datenverkehr für Ping (nicht angekündigt). Finde mit `Test-NetConnection`, `Get-NetFirewallRule` und `Get-NetFirewallProfile` die Ursache und beschreibe die Beseitigung.

#### Kontrollfragen
1. Welche Cmdlets liefern Zustand und Verlauf von Defender Antivirus?
2. Warum sind Ausnahmen für ganze Laufwerke gefährlich?
3. Welches Profil gilt in der Domäne, und was unterscheidet es vom öffentlichen Profil?
4. Welche Regel gewinnt: Zulassen oder Blockieren, wenn beide passen? (Antwort aus dem Kurs belegen.)

---

### Modul 9: Updates
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Qualitäts- und Feature-Updates unterscheiden und den Update-Rhythmus von Windows 11 erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Verzögerungen (Deferral) und Pausen für Updates per Gruppenrichtlinie planen und die Freigabetermine berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Update-Richtlinien setzen und auf dem Client nachweisen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wann ein WSUS-Server und wann Windows Update der Quelle ist.
* **Voraussetzungen:** Modul 6

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Update-Arten und Rhythmus (monatliche Qualitätsupdates, jährliche Feature-Updates) | 2 |
| 9.2 | Verzögerung, Pause und Ringe planen | 2 |
| 9.3 | Richtlinien setzen und nachweisen | 2 |
| 9.4 | Updatequellen: Windows Update, WSUS, Suchquelle | 2 |

#### Praxisaufgaben (Hands-on Lab)
Im Labor ohne Internet werden Richtlinien gesetzt und geprüft, aber keine Updates eingespielt.
1. **Rhythmus (Lernziel 1):** Notiere nach Learn: Qualitätsupdates erscheinen am zweiten Dienstag des Monats, Feature-Updates jährlich in der zweiten Jahreshälfte. Nenne zu jeder Art ein Beispiel für ein Risiko beim sofortigen Einspielen.
2. **Termine berechnen (Lernziel 2):** Ein Qualitätsupdate erscheint am Dienstag, 10.11.2026. Drei Ringe haben Verzögerungen von 0 (Pilot), 5 (schnell) und 10 Tagen (langsam). Berechne Datum und Wochentag für die Freigabe an jeden Ring. Ein Feature-Update erscheint am 29.09.2026 (26H2). Berechne das Datum bei 90 Tagen Verzögerung und bei der höchsten Verzögerung (365 Tage). Die Pause eines Qualitätsupdates beginnt am 10.11.2026 und gilt für höchstens 35 Tage; bis zu welchem Datum?
3. **Richtlinien (Lernziel 3):** Setze auf DC01 in einer Richtlinie für `Clients` unter *Computerkonfiguration > Administrative Vorlagen > Windows-Komponenten > Windows Update > Windows Update for Business* die Richtlinie „Select when Preview Builds and feature updates are Received“ mit 90 Tagen (Pfad nach Learn). Prüfe auf CL01 nach `gpupdate /force` die Werte unter `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` (z. B. `DeferFeatureUpdates`, `DeferFeatureUpdatesPeriodinDays`) mit `Get-ItemProperty`. Wenn die Richtlinie in der Verwaltungskonsole fehlt, sind die Vorlagen (ADMX) auf DC01 älter als Windows 11; dann Vorlagen des Windows-11-Clients vom Host bereitstellen (nicht bestätigt, nicht geprüft).
4. **Quellen (Lernziel 4):** Beantworte mit Learn: Woher bezieht ein Windows-11-Client Updates, wenn nur die Richtlinie für den WSUS-Server gesetzt ist, und welche Richtlinie ändert das? Trage dazu die Werte `WUServer` und `UseWUServer` ein, die Learn nennt, und beschreibe, was dadurch im Labor nicht funktioniert (kein WSUS-Server vorhanden).

#### Kontrollfragen
1. Wie lange kann nach Learn ein Feature-Update höchstens verzögert werden?
2. Was gilt für die Verzögerung von Qualitätsupdates? (Learn nennt im Text 30 Tage, in der Registry-Tabelle 0–35: Abweichung ist zu benennen und vor dem Kurs zu klären.)
3. Warum teilt man Geräte in Ringe ein?
4. Ist WSUS laut Learn noch unterstützt, und was heißt „deprecated“ dort?

---

### Modul 10: Sicherung und Wiederherstellung
* **Priorität:** 1
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Sicherungsarten (voll, inkrementell) beschreiben und Speicherbedarf und Dauer berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Daten eines Clients sichern und wiederherstellen und den Erfolg prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Systemwiederherstellungspunkte anlegen und nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Windows-Wiederherstellungsumgebung (WinRE) prüfen und ihre Werkzeuge nennen.
* **Voraussetzungen:** Modul 2, Modul 4, Modul 7

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Sicherungskonzept: Voll, inkrementell, Aufbewahrung, Wiederherstellungstest | 2 |
| 10.2 | Datensicherung mit Bordmitteln und Wiederherstellung | 3 |
| 10.3 | Systemwiederherstellung und Wiederherstellungspunkte | 2 |
| 10.4 | WinRE und Zurücksetzen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Bedarf berechnen (Lernziel 1):** 50 Clients haben je 40 GB Nutzdaten (1 GB = 1000 MB), pro Tag ändern sich 2 %. Berechne bei 14 Tagen Aufbewahrung den Speicherbedarf für (a) tägliche Vollsicherung, (b) Vollsicherung wöchentlich plus tägliche inkrementelle Sicherung (Fulls an Tag 0 und 7), (c) eine Vollsicherung plus 13 inkrementelle Sicherungen. Berechne außerdem die Dauer einer Vollsicherung aller Clients bei 100 MB/s und einer inkrementellen Sicherung sowie die Wiederherstellung eines Clients (40 GB) bei 80 MB/s. Nenne einen Nachteil von Variante (c).
2. **Datensicherung (Lernziel 2):** Sichere `C:\Daten\Projekt` auf CL01 mit `robocopy C:\Daten\Projekt D:\Sicherung /MIR /LOG:C:\sicherung.log` (nach Anlage einer zweiten virtuellen Festplatte als `D:`; Vorsicht: `/MIR` löscht im Ziel; Ziel vorher kontrollieren, Parameter nicht bestätigt). Lösche danach drei Dateien im Quellordner, stelle sie aus der Sicherung wieder her und weise die Gleichheit der Dateien nach (zum Beispiel mit `Get-FileHash`). Dokumentiere, dass der Wiederherstellungstest erfolgreich war. Eine Sicherung mit `wbadmin` oder der Sicherungs-App ist hier nicht Teil der Aufgabe, weil ihre Verfügbarkeit in Windows 11 nicht bestätigt ist.
3. **Wiederherstellungspunkt (Lernziel 3):** Aktiviere den Computerschutz für `C:`, lege mit `Checkpoint-Computer` einen Wiederherstellungspunkt an, ändere bewusst eine Einstellung, liste mit `Get-ComputerRestorePoint` die Punkte und stelle den Zustand wieder her (Cmdlets nicht bestätigt). Beantworte: Welche Daten schützt die Systemwiederherstellung nicht? (nach Learn: persönliche Dateien nicht).
4. **WinRE (Lernziel 4):** Prüfe mit `reagentc /info`, ob WinRE aktiv ist, starte über die erweiterten Startoptionen in WinRE, nenne die dort verfügbaren Werkzeuge (nach Learn: Starthilfe, Systemwiederherstellung, Zurücksetzen) und gib die BitLocker-Wiederherstellung ein, falls die Umgebung danach fragt. Starte ohne Zurücksetzen wieder in Windows.

#### Kontrollfragen
1. Warum ist eine Sicherung ohne Wiederherstellungstest wertlos?
2. Wieso ersetzt ein Hyper-V-Prüfpunkt keine Datensicherung?
3. Was schützt die Systemwiederherstellung, und was nicht?
4. Wann startet WinRE nach Learn automatisch?

---

### Modul 11: Fernwartung
* **Priorität:** 2
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Remotedesktop auf einem Client einrichten und den Zugriff auf berechtigte Benutzer beschränken.
  * Nach Abschluss dieses Moduls kann der Lernende PowerShell-Remoting einrichten und Befehle auf einem Client ausführen.
  * Nach Abschluss dieses Moduls kann der Lernende die Sicherheitsrisiken von Fernwartung benennen und Gegenmaßnahmen festlegen.
* **Voraussetzungen:** Modul 5, Modul 8

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Remotedesktop: Voraussetzungen, Berechtigungen, Netzwerkebenenauthentifizierung | 3 |
| 11.2 | PowerShell-Remoting | 2 |
| 11.3 | Sicherheit der Fernwartung | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Remotedesktop (Lernziel 1):** Aktiviere Remotedesktop auf CL01 (Einstellungen, System, Remotedesktop; nach Learn). Füge `LAB\ben.beispiel` zur Gruppe der Remotedesktopbenutzer hinzu und prüfe die Verbindung von DC01 mit `mstsc /v:10.50.0.21`. Beantworte nach Learn: Welche Editionen können als Host dienen, und welche nicht? Prüfe, dass die Firewall die Verbindung zulässt, ohne die Regel zu weit zu öffnen.
2. **PowerShell-Remoting (Lernziel 2):** Aktiviere auf CL01 `Enable-PSRemoting` (nach Learn) und führe von DC01 `Invoke-Command -ComputerName CL01 -ScriptBlock { Get-ComputerInfo -Property OsName }` aus (Kombination nicht bestätigt). Dokumentiere Ausgabe und Ports (WinRM nutzt standardmäßig TCP 5985; nicht bestätigt).
3. **Risiken (Lernziel 3):** Erstelle eine Tabelle mit mindestens fünf Risiken von Fernwartung (offener Port, schwache Kennwörter, zu viele berechtigte Konten, Ausnutzung von Sitzungen, fehlende Protokollierung) und je einer Gegenmaßnahme. Nenne eine Gegenmaßnahme, die Learn nennt (starke Kennwörter, nur vertrauenswürdige Netze).

#### Kontrollfragen
1. Welche Editionen von Windows 11 können Remotedesktop-Verbindungen annehmen?
2. Wer darf sich nach dem Aktivieren verbinden?
3. Was macht `Enable-PSRemoting`?
4. Warum wird Quick Assist hier nur theoretisch behandelt?

---

### Modul 12: Fehlersuche und Leistung
* **Priorität:** 1
* **Zeitaufwand:** 11 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein strukturiertes Vorgehen zur Fehlersuche anwenden (Symptom, Hypothese, Test, Behebung, Dokumentation).
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisprotokolle auswerten und Systemdateien prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende vier typische Domänen-Client-Fehler eingrenzen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende Leistungsdaten (CPU, Speicher, Datenträger) erfassen, mit Schwellenwerten bewerten und den Engpass benennen.
* **Voraussetzungen:** Modul 5, Modul 6, Modul 7, Modul 8

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Vorgehensmodell der Fehlersuche und Dokumentation | 2 |
| 12.2 | Ereignisanzeige, Systemdateiprüfung, abgesicherter Modus | 3 |
| 12.3 | Fallstudien Domänen-Client (Namensauflösung, Richtlinie, Vertrauensstellung, BitLocker) | 3 |
| 12.4 | Leistung: Zähler, Engpassanalyse | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Vorgehen (Lernziel 1):** Lege eine Vorlage „Fehlerbericht“ (Symptom, Zeitpunkt, letzte Änderung, Hypothesen, Tests, Ergebnis, Behebung) an und verwende sie in den folgenden Aufgaben.
2. **Protokolle und Systemdateien (Lernziel 2):** Lies mit `Get-WinEvent -LogName System -MaxEvents 20` die letzten Ereignisse, filtere Fehler und Warnungen und beschreibe zwei. Prüfe mit `sfc /scannow` (Administrator) die Systemdateien und mit `DISM /Online /Cleanup-Image /CheckHealth` den Komponentenspeicher (Befehle nicht bestätigt; `/RestoreHealth` braucht eine Quelle und scheitert im Labor ohne Internet).
3. **Vier Fälle (Lernziel 3):** Der Kursleiter baut nacheinander vier Fehler ein (CL01 jeweils auf `CL01-M7-Ende` zurücksetzen und den Fehler herbeiführen; Anleitung siehe Kontrollwerte). Bearbeite jeden Fall mit dem Fehlerbericht: (a) Namensauflösung schlägt fehl; (b) Richtlinie `CL-Basis` wird nicht angewendet; (c) Anmeldung scheitert mit Hinweis auf die Vertrauensstellung; (d) BitLocker verlangt beim Start das Wiederherstellungskennwort. Nenne zu jedem Fall die ersten drei Prüfschritte und deren erwartetes Ergebnis.
4. **Leistung (Lernziel 4):** Auf einem Client wurden in acht Messungen im Abstand von fünf Minuten diese Werte erfasst (Gesamtspeicher 4096 MB):

   | Messung | CPU gesamt (%) | Verfügbarer Speicher (MB) | Datenträger-Warteschlange |
   | :--- | :--- | :--- | :--- |
   | 1 | 35 | 1200 | 0,4 |
   | 2 | 42 | 950 | 0,8 |
   | 3 | 38 | 800 | 1,2 |
   | 4 | 55 | 520 | 2,5 |
   | 5 | 48 | 380 | 3,1 |
   | 6 | 40 | 330 | 3,8 |
   | 7 | 44 | 310 | 2,9 |
   | 8 | 39 | 290 | 3,4 |

   Berechne Mittelwert und Höchstwert der drei Zähler und zähle die Messungen, die die Schwellenwerte überschreiten (Annahmen dieses Lehrplans, keine Herstellerangabe: CPU über 85 %, verfügbarer Speicher unter 400 MB, Warteschlange über 2). Benenne den Engpass und begründe. Erfasse danach auf CL01 mit `Get-Counter` selbst zwei Zähler über zehn Messungen (Zählernamen nicht bestätigt, zum Beispiel `\Processor(_Total)\% Processor Time` und `\Memory\Available MBytes`).

#### Kontrollfragen
1. Welche Schritte gehören zu einer strukturierten Fehlersuche?
2. Wann ist ein Neustart eine sinnvolle Maßnahme und wann nicht?
3. Wie unterscheidet man ein Namensauflösungsproblem von einem Verbindungsproblem?
4. Warum ist ein Mittelwert allein für die Leistungsbewertung nicht ausreichend?

---

## C. Hinweise zur Entstehung und Prüfvermerk (08.11.2026)

Dieser Lehrplan wurde ohne Gem-Entwurf direkt aus dem Prompt P45 erstellt. Annahmen: 12 Module mit 108 UE (innerhalb 100 bis 120), Lab mit zwei VMs auf privatem Switch, Domäne `lab.example.internal` mit `.internal` (reserviert für private Nutzung, nicht bestätigt), Enterprise-Evaluation als Client. Rechenwerte per Skript berechnet; Befehle nicht ausgeführt.

**Kontrollwerte (Lösungsschlüssel für Dozenten):**

* **Modul 1, Aufgabe 1:** A erfüllt; B nicht (TPM 1.2); C nicht (Legacy-BIOS statt UEFI, kein Secure Boot); D nicht (2 GB RAM); E erfüllt (Secure Boot „fähig“ genügt nach Learn: „UEFI, Secure Boot capable“); F nicht (60 GB unter 64 GB).
* **Modul 1, Aufgabe 2 (Stichtag 30.11.2026):** unterstützt: PC-01 (Ende 12.10.2027, 316 Tage), PC-03 (12.10.2027, 316), PC-05 (10.10.2028, 680), PC-07 (10.10.2028, 680). Ende erreicht: PC-02 und PC-08 (13.10.2026, seit 48 Tagen), PC-04 (10.11.2026, seit 20 Tagen), PC-06 (23H2 Pro: beendet, Datum hier nicht genannt). Am 30.06.2027 unterstützt: PC-01, PC-03, PC-05, PC-07.
* **Modul 5, Aufgabe 2:** A (100 Hosts) `/25`, 126 nutzbar: `10.60.0.0/25`, Hosts `.1` bis `.126`, Broadcast `10.60.0.127`. B (50) `/26`, 62: `10.60.0.128/26`, Hosts `.129` bis `.190`, Broadcast `.191`. C (25) `/27`, 30: `10.60.0.192/27`, Hosts `.193` bis `.222`, Broadcast `.223`. Frage 4: `/25` 126, `/26` 62, `/27` 30.
* **Modul 9, Aufgabe 2:** Ringe: Pilot Di 10.11.2026, schnell So 15.11.2026, langsam Fr 20.11.2026 (der Sonntag zeigt, dass Kalendertage und nicht Arbeitstage gelten). Feature-Update: 90 Tage nach 29.09.2026 ist Mo 28.12.2026; 365 Tage ist Mi 29.09.2027. Pause: 35 Tage ab 10.11.2026 reicht bis Di 15.12.2026.
* **Modul 10, Aufgabe 1:** Vollsicherung aller Clients 2000 GB; Änderung pro Tag 40 GB. (a) 14 × 2000 = 28 000 GB; (b) 2 × 2000 + 12 × 40 = 4480 GB; (c) 2000 + 13 × 40 = 2520 GB. Dauer Vollsicherung: 2 000 000 MB / 100 MB/s = 20 000 s ≈ 5,56 h; inkrementell 40 000 MB / 100 = 400 s ≈ 6,7 min; Wiederherstellung eines Clients 40 000 MB / 80 = 500 s ≈ 8,3 min. Nachteil von (c): lange Kette bei der Wiederherstellung, ein defektes Glied bricht die Kette ab; nur eine Vollsicherung als Basis.
* **Modul 12, Aufgabe 4:** CPU Mittelwert 42,6 %, Höchstwert 55 %; Speicher Mittelwert 597,5 MB, Minimum 290 MB; Warteschlange Mittelwert 2,26, Höchstwert 3,8. Schwellenwerte überschritten: CPU 0 von 8; Speicher unter 400 MB 4 von 8 (Messungen 5 bis 8); Warteschlange über 2 in 5 von 8 (Messungen 4 bis 8). Engpass: Arbeitsspeicher (verbunden mit hoher Datenträgerauslastung durch Auslagerung), nicht die CPU.
* **Modul 12, Aufgabe 3 (Fehlereinbau, Vorschlag des Kursleiters, nicht getestet):** (a) auf CL01 `Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 10.50.0.99`; (b) Computerkonto von DC01 in eine andere Organisationseinheit verschieben; (c) Vorgehen wie Modul 5, Aufgabe 4 (Kennwort des Computerkontos ändern, CL01 auf einen Prüfpunkt davor zurücksetzen); (d) `manage-bde -forcerecovery C:` mit gesichertem Kennwort in AD, dann Neustart. Für jeden Fall ist der Behebungsweg im Kursleiter-Skript festzuhalten.

**Prüfvermerk (Grundanweisung, neun Punkte):**

1. **Stunden und Prioritäten:** 7+10+9+10+10+9+9+9+8+9+7+11 = 108 UE; 10× Priorität 1, 2× Priorität 2; jede Einheitentabelle summiert auf die Modulstunden und die Master-Tabelle stimmt mit den Modulköpfen überein (per Skript über die Datei geprüft). Keine Fehler gefunden; Stichprobe: Modul 12 mit 2+3+3+3 = 11 UE.
2. **Labor-Setup:** Host, Switch, DC01, CL01 und Prüfpunkte sind aufgeführt. Offen: Version des Windows Servers, ob die Evaluation den Domänenbeitritt unterstützt (ja für Enterprise; nicht bestätigt). Internet-Bedarf in Modul 2 (Ersteinrichtung) und die ADMX-Frage in Modul 9 sind benannt.
3. **Quellen:** Siehe A.2. Learn-Seiten wurden nur als Suchtreffer-Auszüge gesehen; Defender- und Firewall-Cmdlets nach Learn belegt, `.internal`, Evaluation-Laufzeit und Windows-Server-Version nicht.
4. **Widerspruchsfreiheit und Zustände:** Adressplan, Domäne und Prüfpunkte stehen in A.3. Zustandsabhängigkeit: CL01 ist ab Modul 5 Domänenmitglied; Modul 7 braucht Modul 6 (Richtlinie für AD-Sicherung); Modul 10 braucht Modul 4 (`C:\Daten\Projekt`) und Modul 7; Modul 12 braucht Modul 6 und 7 (Richtlinie `CL-Basis`, BitLocker) und baut auf `CL01-M7-Ende`. Hinweis auf das Risiko bei Prüfpunkten (Computerkonto). Korrigiert bei der Prüfung: Die Vertrauensstellung in Modul 5 wurde zuerst über den Prüfpunkt `CL01-M2-Ende` provoziert (das entfernt nur die Mitgliedschaft und erzeugt den Fehler nicht); jetzt über Kennwortänderung des Computerkontos und Prüfpunkt `CL01-M5-Join`. Modul 8, 10 und 12 nannten Voraussetzungen nicht vollständig; ergänzt. Die zweite virtuelle Festplatte für Modul 10 fehlte im Laborsetup; ergänzt. Modul 1, Aufgabe 3 verlangte CL01, das erst in Modul 2 entsteht; nutzt jetzt den Host.
5. **Lernziele, Lerneinheiten, Kontrollfragen:** Jedes Lernziel hat mindestens eine Aufgabe (im Text mit „Lernziel n“ markiert; per Skript geprüft: in allen 12 Modulen sind alle Lernziele durch Aufgaben markiert); jede Lerneinheit hat mindestens eine Aufgabe oder Frage (Stichprobe Einheit 1.3: Aufgabe 2, Frage 2; Einheit 10.4: Aufgabe 4, Frage 4).
6. **Einschränkungen und Rückbau:** Kein Pflichtmodul hängt von Modul 3 oder 11 ab. Rückbau über Prüfpunkte; Verschlüsselung (Modul 7) nur mit gesichertem Schlüssel.
7. **Infrastruktur über eine VM hinaus:** Zwei VMs (DC01, CL01) auf einem privaten Switch; gemeinsames Zurücksetzen nur zusammen (siehe A.3).
8. **Internet, Namen, Dateiwege:** Lab ohne Internet, Domäne `lab.example.internal`, Adressen nach RFC 1918. Nicht möglich: Updates, Signaturen, Quick Assist (benannt).
9. **Befehle und Sicherheit:** Destruktive Befehle (`robocopy /MIR`, `manage-bde -forcerecovery`, Zurücksetzen von Prüfpunkten) stehen mit Vorbedingung (Sicherung, Prüfpunkt, Schlüssel in AD). Kennwörter stehen nicht im Dokument.

**Offene Punkte:**

* Alle Befehle und Menüpfade vor dem Kurs im Labor ausführen (nichts davon wurde in einer Windows-Umgebung getestet); besonders `Get-LapsADPassword`, `manage-bde -protectors -adbackup … -id`, `Checkpoint-Computer`, die ADMX-Frage in Modul 9 und die Ersteinrichtung ohne Internet.
* Learn-Widerspruch zur Verzögerung von Qualitätsupdates (30 Tage im Text, 0 bis 35 in der Tabelle) klären.
* Windows-Server-Version und Evaluationszeitraum festlegen und dokumentieren.
* Zeitaufwand unerprobt (108 UE mit Labor sind eine Schätzung).
