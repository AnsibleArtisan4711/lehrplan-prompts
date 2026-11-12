# Lehrplan: Remotedesktopdienste (RDS)

| Kategorie | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen, Grundkenntnisse Netzwerke (IP-Adressen, Subnetze), Windows-Server-Grundlagen, Active-Directory-Grundlagen (Benutzer, Gruppen, OUs), Grundkenntnisse zu Gruppenrichtlinien (GPO anlegen und mit einer OU verknüpfen), erste Erfahrung mit PowerShell |
| **Gesamtumfang** | 13 Module, 104 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows Server 2022 (Remotedesktopdienste, Rollendienste RD Session Host, RD Connection Broker, RD Web Access, RD Gateway, RD Licensing), Windows 11 Enterprise als Client |
| **Thematische Abgrenzung (Out of Scope)** | Gruppenrichtlinien-Grundlagen und Active Directory (eigene Lehrpläne; der Domänencontroller wird vor Kursbeginn aufgebaut); Dateidienste (Kurs „Dateidienste, DFS und Druckserver“; hier nur eine einfache Freigabe für Benutzerprofil-Datenträger); VDI mit Hyper-V-Hosts, Hochverfügbarkeit (Broker-Cluster, mehrere Server), Azure Virtual Desktop und Windows 365 (nur als Vergleich in Modul 1); Zertifizierungsstelle (Kurs „Zertifikatsdienste und PKI (AD CS)“) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | RDS-Grundlagen, Architektur und Lizenzüberblick | 1 | 8 |
| 2 | Vorbereitung der Laborumgebung | 1 | 6 |
| 3 | Bereitstellung der sitzungsbasierten Umgebung | 1 | 10 |
| 4 | Sitzungssammlungen und Desktopzugriff | 1 | 8 |
| 5 | RemoteApps und Web Access | 1 | 8 |
| 6 | Zertifikate für Remotedesktopdienste | 1 | 8 |
| 7 | Remotedesktopgateway | 2 | 8 |
| 8 | Lizenzierung (RDS-CALs) | 1 | 8 |
| 9 | Profilverwaltung mit Benutzerprofil-Datenträgern | 1 | 8 |
| 10 | Gruppenrichtlinien für RDS | 1 | 8 |
| 11 | Druck- und Laufwerksumleitung | 2 | 6 |
| 12 | Sicherheit und Netzwerkebenenauthentifizierung | 1 | 8 |
| 13 | Überwachung und Fehlersuche | 1 | 10 |
| **Gesamt** | **11x Prio 1, 2x Prio 2** | | **104** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (Pflicht, zusammen 90 UE) bilden die Kernkompetenz. Module mit Priorität 2 (Vertiefung, zusammen 14 UE) können bei Zeitmangel entfallen; kein Pflichtmodul setzt sie voraus und kein Rückbau hängt von ihnen ab.*

### 2. Quellen

Die Seiten wurden am 12.11.2026 über die Suche von Microsoft Learn in Auszügen gelesen, nicht vollständig. Was nur aus dem Gedächtnis stammt, ist im Text als `nicht bestätigt` gekennzeichnet. Alle Inhalte sind eigenständig formuliert.

*   **Remote Desktop Services overview in Windows Server**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug; URL nicht erneut aufgerufen), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/overview](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/overview)
*   **Remote Desktop Services architecture**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/desktop-hosting-logical-architecture](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/desktop-hosting-logical-architecture)
*   **Deploy your Remote Desktop environment**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-deploy-infrastructure](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-deploy-infrastructure)
*   **License Remote Desktop Services with Client Access Licenses (CALs)**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-client-access-license](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-client-access-license)
*   **License Remote Desktop session hosts**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-license-session-hosts](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-license-session-hosts)
*   **Activate the Remote Desktop Services license server**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-activate-license-server](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-activate-license-server)
*   **RDS Licensing troubleshooting guidance**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/troubleshoot/windows-server/remote/troubleshoot-rds-licensing-guidance](https://learn.microsoft.com/troubleshoot/windows-server/remote/troubleshoot-rds-licensing-guidance)
*   **Use certificates in Remote Desktop Services**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/remote-desktop-services-certificates](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/remote-desktop-services-certificates)
*   **Deploy the Remote Desktop Gateway role**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/remote-desktop-gateway-role](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/remote-desktop-gateway-role)
*   **Remote Desktop Services - Secure data storage with UPDs**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-plan-secure-data-storage](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-plan-secure-data-storage)
*   **RemoteDesktop PowerShell-Modul** (u. a. `New-RDSessionDeployment`, `Set-RDSessionCollectionConfiguration`, `Set-RDCertificate`, `Get-RDCertificate`), Microsoft Corporation, gelesen am 12.11.2026 (Auszüge zu den genannten Cmdlets), [https://learn.microsoft.com/powershell/module/remotedesktop/](https://learn.microsoft.com/powershell/module/remotedesktop/)
*   **„The system administrator has restricted the types of logon“ error when connecting to a computer**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/troubleshoot/windows-server/remote/system-admin-restrict-types-logon](https://learn.microsoft.com/troubleshoot/windows-server/remote/system-admin-restrict-types-logon)
*   **Windows security baseline** (Richtlinie „Require user authentication for remote connections by using Network Level Authentication“), Microsoft Corporation, gelesen am 12.11.2026 (Auszug; URL nicht erneut aufgerufen), [https://learn.microsoft.com/azure/governance/policy/samples/guest-configuration-baseline-windows](https://learn.microsoft.com/azure/governance/policy/samples/guest-configuration-baseline-windows)
*   **Windows Server 2022: known issues and notifications** (Support-Stand und bekannte Probleme), Microsoft Corporation, Stand der Seite 13.10.2026, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows/release-health/status-windows-server-2022](https://learn.microsoft.com/windows/release-health/status-windows-server-2022)
*   Für die Lizenzbedingungen im Einzelfall (Lizenzprogramme, Preise, Software Assurance) gilt: **Keine geprüfte Quelle** in diesem Lehrplan; sie hängen vom Vertrag ab und werden nicht genannt.

### 3. Labor-Setup & Rahmenbedingungen

Alle Praxisaufgaben finden in einer isolierten Hyper-V-Umgebung statt, ohne unkontrollierte Verbindung zum Heim- oder Produktivnetz.

*   **Privater virtueller Switch `vSwitch-RDS-Privat`:** Netz `192.168.70.0/24`, ohne Gateway, ohne DHCP, alle Adressen statisch. Erforderlich ab Modul 2.
*   **VM 1: Domänencontroller (DC01):** Windows Server 2022 (Evaluation), `192.168.70.10`, DNS-Rolle, AD DS installiert, Domäne `rdslab.internal`. Der Aufbau von AD DS gehört nicht zum Kurs und wird **vor Kursbeginn** vorbereitet (Voraussetzung). Erforderlich ab Modul 2. Hält in Modul 9 eine einfache SMB-Freigabe (Laborvereinfachung; in der Praxis liegt sie auf einem Dateiserver).
*   **VM 2: RDS-Server (RDS01):** Windows Server 2022 (Evaluation, Desktopdarstellung), `192.168.70.20`, DNS `192.168.70.10`, Domänenbeitritt in Modul 2. Trägt in Modul 3 die Rollendienste **RD Connection Broker, RD Web Access und RD Session Host**, in Modul 7 RD Gateway, in Modul 8 RD Licensing. **Alle Rollen auf einem Server sind eine Laborvereinfachung** und kein Produktivdesign. Erforderlich ab Modul 2.
*   **VM 3: Client (CL01):** Windows 11 Enterprise (Evaluation), `192.168.70.50`, DNS `192.168.70.10`, Domänenbeitritt in Modul 2. Generation 2 mit virtuellem TPM (Hyper-V-Einstellung; Einstellungsweg nicht bestätigt). Erforderlich ab Modul 2.
*   **Namen:** Domäne `rdslab.internal`; OUs `RDS-Server` und `Clients`; Benutzer `user1`, `user2`; Gruppen `SG-RDS-Users` (user1) und `SG-RDS-Verwaltung`; DNS-Alias `rds.rdslab.internal` (CNAME auf `rds01.rdslab.internal`) für Web Access und Gateway.
*   **Internet:** Die Evaluationsmedien für Windows Server und Windows 11 werden **vor Modul 2** außerhalb des Labors geladen und in die VMs eingebunden. Danach hat das Lab **kein Internet**. Deshalb kann der Lizenzserver in Modul 8 **nicht aktiviert** werden und es lassen sich **keine CALs installieren** (dafür ist eine Verbindung zum Lizenz-Clearinghouse per Internet, Web oder Telefon und ein gültiger Lizenzschlüssel nötig, siehe Quellen). Modul 8 behandelt die Aktivierung deshalb als reine Theorie; praktisch gearbeitet wird mit dem **Grace-Zeitraum von 120 Tagen**. Es gibt keine Internetphase in diesem Kurs.
*   **Zertifikate:** Es gibt keine Zertifizierungsstelle im Labor. In Modul 6 werden die Zertifikate der Rollen über Server Manager selbst signiert erzeugt. Selbstsignierte Zertifikate sind ein Laborbehelf. Der Kurs „Zertifikatsdienste und PKI (AD CS)“ zeigt den Weg über eine eigene CA, setzt hier aber nichts voraus.
*   **Prüfpunkte (Hyper-V-Checkpoints), immer für alle drei VMs gemeinsam erstellen und gemeinsam zurücksetzen** (ein einzelner Rücksetzer des Domänencontrollers kann das Verzeichnis gegen die anderen VMs verschieben): `M2-Basis` (Ende Modul 2), `M3-RDS` (Ende Modul 3), `M6-Zert` (Ende Modul 6), `vor-M10` (vor den Richtlinien), `vor-M12` (vor den Sicherheitstests), `vor-M13` (vor den Fehlerszenarien).
*   **Versions- und Supportstand (12.11.2026):** Laut Microsoft Learn (Seite vom 13.10.2026) ist Windows Server 2022 seit dem 13.10.2026 im erweiterten Support, mit monatlichen Sicherheitsupdates bis 14.10.2031. Windows Server 2025 ist die aktuelle LTSC-Version. Der Evaluationszeitraum von Windows Server 2022 und Windows 11 Enterprise ist **nicht geprüft** (für Windows Server 2025 nennt Learn 180 Tage). Vor Kursstart die Evaluationsseiten prüfen. Die Menünamen der Server-Manager-Oberfläche sind im Text auf Englisch angegeben, wo Microsoft Learn sie so führt; deutsche Bezeichnungen sind `nicht bestätigt`.

---

## B. Detaillierter Modulaufbau

### Modul 1: RDS-Grundlagen, Architektur und Lizenzüberblick
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rollendienste von Remotedesktopdiensten (Session Host, Connection Broker, Web Access, Gateway, Licensing) benennen und ihre Aufgaben erklären.
  * Nach Abschluss dieses Moduls kann der Lernende sitzungsbasierte Desktops, RemoteApp und virtuelle Desktops voneinander abgrenzen und Azure Virtual Desktop als Alternative einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grundzüge der Lizenzierung (CAL pro Benutzer oder Gerät, Grace-Zeitraum) erklären und den Versions- und Supportstand seines Labors benennen.
* **Voraussetzungen:** Keine; kein Labor nötig.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Rollendienste und logische Architektur einer RDS-Bereitstellung | 3 |
| 1.2 | Bereitstellungsarten: sitzungsbasierter Desktop, RemoteApp, virtuelle Desktops; Alternativen (Azure Virtual Desktop) | 2 |
| 1.3 | Lizenzierung im Überblick und Versions-/Supportstand | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Architekturzeichnung:** Zeichne für das fiktive Unternehmen „Alpenwerk“ (30 Mitarbeitende, eine Branchenanwendung, ein Standort) eine RDS-Bereitstellung mit je einem Server pro Rolle und beschrifte, welche Verbindung über welchen Port läuft (Port-Angaben mit `nicht bestätigt` kennzeichnen, soweit nicht aus den Quellen gelesen).
2. **Variantenvergleich:** Erstelle eine Tabelle mit je drei Merkmalen für sitzungsbasierten Desktop, RemoteApp und Azure Virtual Desktop (zum Beispiel Ressourcenbedarf, Verwaltungsaufwand, Lizenzbedarf).
3. **Lizenz- und Supportstand:** Lies auf den Quellseiten den Supportstand von Windows Server 2022 und die Grace-Dauer ab und notiere beides mit Datum. Notiere, was du nicht geprüft hast (zum Beispiel Preise).

#### Kontrollfragen
1. Welche Aufgabe hat der RD Connection Broker, und warum steht er in jeder Bereitstellung?
2. Worin unterscheiden sich ein sitzungsbasierter Desktop und ein RemoteApp aus Sicht des Benutzers?
3. Wie lange läuft der Grace-Zeitraum ohne Lizenzserver, und was gilt danach?
4. Warum ist ein Server mit allen Rollen nur für ein Labor geeignet?

### Modul 2: Vorbereitung der Laborumgebung
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen privaten Hyper-V-Switch, statische Adressen und DNS-Einträge für die Bereitstellung einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Server und Client in die Domäne aufnehmen und OUs, Benutzer und Gruppen für RDS anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Prüfpunkte für alle VMs erstellen.
* **Voraussetzungen:** Modul 1; VM `DC01` ist vor Kursbeginn betriebsbereit (Voraussetzung).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Netzwerk, Adressplan und Namenskonzept | 2 |
| 2.2 | Domänenbeitritt, OUs, Benutzer und Gruppen | 2 |
| 2.3 | Basisprüfung und Prüfpunkte | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Netzwerk:** Lege `vSwitch-RDS-Privat` an und verbinde `DC01`, `RDS01` und `CL01`. Vergib die Adressen aus dem Labor-Setup statisch (`New-NetIPAddress`, `Set-DnsClientServerAddress`) und prüfe mit `Test-NetConnection 192.168.70.10`.
2. **DNS und Domäne:** Lege auf `DC01` den CNAME `rds` auf `rds01.rdslab.internal` an (`Add-DnsServerResourceRecordCName`). Nimm `RDS01` und `CL01` in die Domäne auf (`Add-Computer`), verschiebe `RDS01` in die OU `RDS-Server` und `CL01` in die OU `Clients`.
3. **Benutzer und Gruppen:** Lege die Benutzer `user1` und `user2`, die Gruppen `SG-RDS-Users` und `SG-RDS-Verwaltung` an und nimm `user1` in `SG-RDS-Users` auf. Vergib die Kennwörter interaktiv (nicht im Skript).
4. **Basisprüfung und Prüfpunkt:** Prüfe `Resolve-DnsName rds.rdslab.internal` von `CL01` und `Test-NetConnection rds01.rdslab.internal -Port 3389`. Erstelle auf allen drei VMs den Prüfpunkt `M2-Basis`.

#### Kontrollfragen
1. Warum erhält das Labor keine Verbindung zum Heimnetz?
2. Wozu dient der CNAME `rds`, und welche Rolle spielt er später bei Zertifikaten?
3. Warum müssen Prüfpunkte der drei VMs gemeinsam zurückgesetzt werden?

### Modul 3: Bereitstellung der sitzungsbasierten Umgebung
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine sitzungsbasierte Standardbereitstellung mit Broker, Web Access und Session Host auf einem Server installieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Rollenverteilung der Bereitstellung in Server Manager und per PowerShell prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Zertifikatswarnungen der Erstinstallation erklären.
* **Voraussetzungen:** Modul 2 (Prüfpunkt `M2-Basis`).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Bereitstellungsmodelle und Rollenverteilung | 3 |
| 3.2 | Installation der sitzungsbasierten Bereitstellung | 4 |
| 3.3 | Prüfung der Bereitstellung und erste Warnungen | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Vorbereitung:** Melde dich auf `RDS01` als Domänenadministrator an, füge `RDS01` in Server Manager hinzu und prüfe, dass keine Neustarts ausstehen. Nenne in einer Notiz, welche Rolle auf welchem Server liegen wird (alle drei auf `RDS01`).
2. **Installation:** Führe in Server Manager *Add Roles and Features → Remote Desktop Services installation → Standard Deployment → Session-based desktop deployment* aus (Weg laut Learn; deutsche Menünamen nicht bestätigt). Alternativ per PowerShell, Syntax aus dem Cmdlet-Referenzauszug: `New-RDSessionDeployment -ConnectionBroker rds01.rdslab.internal -WebAccessServer rds01.rdslab.internal -SessionHost rds01.rdslab.internal`. Starte den Server neu, wenn gefordert.
3. **Prüfung:** Prüfe die Rollen mit `Get-RDServer` (Ausgabe nicht bestätigt) und in Server Manager unter *Remote Desktop Services → Overview*. Rufe `https://rds.rdslab.internal/RDWeb` von `CL01` auf und notiere die Zertifikatswarnung.
4. **Prüfpunkt:** Erstelle auf allen drei VMs den Prüfpunkt `M3-RDS`.

#### Kontrollfragen
1. Welche drei Rollendienste installiert die sitzungsbasierte Standardbereitstellung, und welchen Server geben die Parameter von `New-RDSessionDeployment` jeweils an?
2. Warum erscheint nach der Installation eine Zertifikatswarnung im Browser?
3. Warum gehört diese Bereitstellung nicht auf den Domänencontroller?

### Modul 4: Sitzungssammlungen und Desktopzugriff
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Sitzungssammlung anlegen und Benutzergruppen zuweisen.
  * Nach Abschluss dieses Moduls kann der Lernende per Remotedesktopverbindung auf einen Sitzungsdesktop zugreifen und aktive Sitzungen anzeigen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie die Gruppenzuweisung den Zugriff steuert.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Sammlungen planen (Server, Gruppen, Anzahl) | 2 |
| 4.2 | Sammlung anlegen und Benutzer zuweisen | 3 |
| 4.3 | Verbindung herstellen und Sitzungen ansehen | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Sammlung anlegen:** Lege die Sammlung `Desktop` an (Server Manager: *Remote Desktop Services → Collections → Tasks → Create Session Collection*, Weg laut Learn) oder mit `New-RDSessionCollection -CollectionName Desktop -SessionHost rds01.rdslab.internal -ConnectionBroker rds01.rdslab.internal` (Cmdlet nicht einzeln gegen die Referenz gelesen). Ersetze die Standardgruppe `Domain Users` durch `SG-RDS-Users`. Die Option für Benutzerprofil-Datenträger bleibt in diesem Modul aus (Modul 9).
2. **Zugriff:** Verbinde dich von `CL01` mit `mstsc` auf `rds01.rdslab.internal` als `RDSLAB\user1` und sieh dir die Sitzung an (`qwinsta` auf `RDS01`; alternativ in Server Manager die Sitzungsliste der Sammlung).
3. **Zugriffsgrenze:** Melde dich als `user2` (nicht in `SG-RDS-Users`) an, notiere die Fehlermeldung, nimm `user2` in die Gruppe auf, melde dich erneut an und entferne ihn danach wieder aus der Gruppe. Melde alle Sitzungen ab.

#### Kontrollfragen
1. Was ist eine Sitzungssammlung, und was verteilt sie auf welche Server?
2. Welche zwei Berechtigungen entscheiden, ob `user2` auf den Desktop darf, und wo werden sie gesetzt?
3. Warum ist die Standardgruppe `Domain Users` für den Produktivbetrieb oft zu weit gefasst?

### Modul 5: RemoteApps und Web Access
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Anwendungen als RemoteApp veröffentlichen.
  * Nach Abschluss dieses Moduls kann der Lernende RemoteApps über RD Web Access starten.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, was RemoteApp von einem Desktop unterscheidet.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | RemoteApp-Konzept und Eignung von Anwendungen | 2 |
| 5.2 | Anwendungen veröffentlichen | 3 |
| 5.3 | Zugriff über Web Access und RDP-Dateien | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Veröffentlichen:** Veröffentliche die auf `RDS01` vorhandenen Programme Editor und Paint (Pfade zum Beispiel `C:\Windows\System32\notepad.exe`, `C:\Windows\System32\mspaint.exe`; Pfade auf dem Server prüfen) in der Sammlung `Desktop` (Server Manager: *Collections → Desktop → RemoteApp Programs → Publish RemoteApp Programs*; Weg nicht bestätigt). Per PowerShell: `New-RDRemoteApp -CollectionName Desktop -DisplayName Editor -FilePath C:\Windows\System32\notepad.exe` (Parameter nicht einzeln gegen die Referenz gelesen).
2. **Web Access:** Melde dich von `CL01` als `user1` an `https://rds.rdslab.internal/RDWeb` an und starte Editor. Die Zertifikatswarnung bestätigst du **nur in diesem Modul**; sie wird in Modul 6 beseitigt. Notiere, wie sich das Fenster vom Desktop unterscheidet.
3. **RDP-Datei:** Lade die `.rdp`-Datei des RemoteApps herunter, öffne sie und prüfe, welche Serveradresse darin steht (Texteditor).

#### Kontrollfragen
1. Warum läuft ein RemoteApp auf dem Server und nicht auf `CL01`, obwohl das Fenster wie ein lokales aussieht?
2. Welche Rolle hat RD Web Access, und was liefert es dem Browser?
3. Warum kommt für ein RemoteApp trotzdem eine RDS-Lizenz in Betracht (siehe Modul 8)?

### Modul 6: Zertifikate für Remotedesktopdienste
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Zertifikatsanforderungen der RDS-Rollen erklären (Serverauthentifizierung, vertrauenswürdige Ausstellung, Name).
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikate für Broker und Web Access in der Bereitstellung erzeugen und zuweisen.
  * Nach Abschluss dieses Moduls kann der Lernende dem Client das Vertrauen herstellen und die Wirkung prüfen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Zertifikatsanforderungen und Rollenzuordnung | 3 |
| 6.2 | Zertifikate erzeugen und in der Bereitstellung zuweisen | 3 |
| 6.3 | Vertrauen auf dem Client herstellen und prüfen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Anforderungen:** Notiere, welche Anforderungen ein Zertifikat laut Quelle erfüllen muss (Serverauthentifizierung, ausgestellt von einer vertrauten CA, exportierbarer privater Schlüssel, `.pfx`-Export) und welche Namen die Rollen brauchen (`rds.rdslab.internal` für Web Access, `rds01.rdslab.internal` für den Broker).
2. **Erzeugen und zuweisen:** Öffne in Server Manager *Remote Desktop Services → Overview → Tasks → Edit Deployment Properties → Certificates* und lege über *Create new certificate* selbst signierte Zertifikate für **RD Connection Broker – Enable Single Sign On**, **RD Connection Broker – Publishing** und **RD Web Access** an (Namen siehe Aufgabe 1; Kennwort der `.pfx` interaktiv; Weg laut Learn). Aktiviere *Allow the certificate to be added to the Trusted Root Certification Authorities certificate store on the destination computers*. Prüfe mit `Get-RDCertificate`.
3. **Vertrauen auf dem Client:** Exportiere die öffentlichen Zertifikate (`.cer`, ohne privaten Schlüssel) und kopiere sie über eine Freigabe nach `CL01`. Importiere sie dort (`Import-Certificate -FilePath … -CertStoreLocation Cert:\LocalMachine\Root`). Rufe `https://rds.rdslab.internal/RDWeb` erneut auf: keine Warnung erwartet (nicht bestätigt; Abweichungen notieren).
4. **Prüfpunkt:** Erstelle den Prüfpunkt `M6-Zert` auf allen drei VMs.

#### Kontrollfragen
1. Warum muss der Name im Zertifikat mit der Adresse übereinstimmen, die der Client aufruft?
2. Welche Rollen der Bereitstellung nutzen Zertifikate, und welche davon hast du in diesem Modul bedient?
3. Warum ist ein selbst signiertes Zertifikat im Produktivbetrieb problematisch?

### Modul 7: Remotedesktopgateway
* **Priorität:** 2
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wozu RD Gateway dient (RDP über HTTPS, Zugriff ohne VPN) und welche Aufgaben die Richtlinien CAP und RAP haben.
  * Nach Abschluss dieses Moduls kann der Lernende RD Gateway installieren und konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine Verbindung über das Gateway herstellen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Gateway-Konzept, CAP und RAP | 3 |
| 7.2 | Installation und Konfiguration | 3 |
| 7.3 | Verbindung über das Gateway testen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Installation:** Füge in Server Manager *Remote Desktop Services → Overview → + RD Gateway* den Dienst auf `RDS01` mit dem externen Namen `rds.rdslab.internal` hinzu (Weg laut Learn). Weise das Zertifikat aus Modul 6 der Rolle zu (`Set-RDCertificate`, Rollenwerte mit `Get-Help Set-RDCertificate` prüfen; alternativ in RD Gateway Manager → Properties → SSL Certificate, laut Learn).
2. **Richtlinien:** Lege im RD Gateway Manager eine Verbindungsautorisierungsrichtlinie (CAP) und eine Ressourcenautorisierungsrichtlinie (RAP) für `SG-RDS-Users` an. Aktiviere in der RAP **nicht** „Only allow computers with support for RD Gateway Messaging“ (der Client unterstützt es laut Quelle nicht).
3. **Test:** Entferne in den Deployment-Eigenschaften unter *RD Gateway* die Option *Bypass RD Gateway server for local addresses* (laut Learn). Stelle in `mstsc` unter *Erweitert → Einstellungen* (Weg nicht bestätigt) das Gateway `rds.rdslab.internal` ein und verbinde dich als `user1`. Notiere, was gegenüber der direkten Verbindung anders ist.
4. **Rückbau:** Stelle die Option *Bypass RD Gateway server for local addresses* wieder auf den Ausgangszustand (aktiviert) und lösche in `mstsc` die Gatewayeinstellung. Ein externer Zugriff aus dem Internet ist im Labor **nicht möglich** und wird nicht getestet.

#### Kontrollfragen
1. Wozu dient RD Gateway im Vergleich zu einem VPN?
2. Was legt die CAP fest und was die RAP?
3. Warum sollte der Name des Gateways im Zertifikat stehen?

### Modul 8: Lizenzierung (RDS-CALs)
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Lizenzmodelle „pro Benutzer“ und „pro Gerät“ vergleichen und für ein Szenario begründet wählen.
  * Nach Abschluss dieses Moduls kann der Lernende den Lizenzserver installieren, den Lizenzmodus der Bereitstellung festlegen und den Grace-Zeitraum auslesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf von Aktivierung und CAL-Installation beschreiben (reine Theorie, im Labor ohne Internet nicht ausführbar).
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | CAL-Modelle: pro Benutzer und pro Gerät | 3 |
| 8.2 | Lizenzserver, Lizenzmodus und Grace-Zeitraum | 3 |
| 8.3 | Aktivierung und CAL-Installation (Theorie) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Modellwahl (schriftlich):** Wähle für drei Szenarien (Schichtbetrieb mit gemeinsamen Geräten, Mitarbeitende mit eigenem Gerät, gemischt) das passende Modell und begründe. Beachte laut Quelle: bei Servern in der Domäne sind beide Modelle möglich, in einer Arbeitsgruppe nur „pro Gerät“.
2. **Lizenzserver installieren:** Füge in Server Manager *Remote Desktop Services → Overview → + RD Licensing* den Dienst auf `RDS01` hinzu (Weg laut Learn). Per PowerShell `Add-RDServer -Server rds01.rdslab.internal -Role RDS-LICENSING -ConnectionBroker rds01.rdslab.internal` (Rollenwert nicht bestätigt).
3. **Lizenzmodus festlegen:** Öffne in Server Manager *Edit Deployment Properties → RD Licensing*, wähle *Per User* und füge `rds01.rdslab.internal` als Lizenzserver hinzu (Weg laut Learn). Alternative: `Set-RDLicenseConfiguration` (Cmdlet auf Microsoft Learn verlinkt, Parameter nicht gelesen). Ohne Connection Broker würde man Lizenzserver und -modus per Gruppenrichtlinie unter *Computer Configuration → Administrative Templates → Windows Components → Remote Desktop Services → Remote Desktop Session Host → Licensing* setzen (Pfad laut Learn; hier nur zur Kenntnis).
4. **Grace-Zeitraum:** Lies ihn aus (`(Get-CimInstance -Namespace root/cimv2/TerminalServices -ClassName Win32_TerminalServiceSetting).GetGracePeriodDays()` nicht bestätigt; die Quelle nennt `GetGracePeriodDays` über WMI) und sieh im *RD Licensing Manager* nach, dass der Server **nicht aktiviert** ist. Das ist im Labor erwartet.
5. **Aktivierung beschreiben:** Beschreibe die drei Wege der Aktivierung (automatisch, Webbrowser, Telefon), den Schritt „Install Licenses“ und warum nichts davon im Labor ausführbar ist. Nenne, welche Informationen du für einen echten Betrieb bräuchtest (Lizenzprogramm, Schlüssel, Version der CALs) und die Versionsregel laut Learn: Die CAL-Version muss zum Session Host passen (CALs älterer Versionen berechtigen nicht für neuere Server) und darf nicht neuer sein als die des Lizenzservers (CALs für Windows Server 2025 lassen sich nicht auf einem Lizenzserver 2022 installieren).

#### Kontrollfragen
1. Was geschieht, wenn der Grace-Zeitraum endet und kein Lizenzserver mit CALs erreichbar ist?
2. Warum zeigt der Server den Grace-Zeitraum auch nach dem Hinzufügen des Lizenzservers weiter an?
3. Worin unterscheiden sich pro Benutzer und pro Gerät bei Entziehung und Überbelegung?
4. Welche drei Möglichkeiten gibt es, einen Lizenzserver zu aktivieren?

### Modul 9: Profilverwaltung mit Benutzerprofil-Datenträgern
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, was ein Benutzerprofil-Datenträger (UPD) ist und welche Grenzen er hat.
  * Nach Abschluss dieses Moduls kann der Lernende eine Freigabe für UPDs anlegen und UPDs für eine Sammlung aktivieren.
  * Nach Abschluss dieses Moduls kann der Lernende nachweisen, dass Daten nach Abmeldung und Neuanmeldung erhalten bleiben.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Profilkonzepte: UPD, servergespeicherte Profile, Ordnerumleitung | 2 |
| 9.2 | UPD einrichten | 3 |
| 9.3 | Betrieb und Grenzen | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Freigabe anlegen:** Lege auf `DC01` den Ordner `C:\UPD` an und gib ihn frei (`New-Item`, `New-SmbShare -Name UPD -Path C:\UPD`). Gib laut Quelle dem Computerkonto `RDS01$` Vollzugriff auf Freigabe und Ordner (`Grant-SmbShareAccess`, NTFS-Rechte mit `icacls`). Dateidienste sind nicht Teil des Kurses; `DC01` als Speicherort ist eine Laborvereinfachung.
2. **Aktivieren:** `Set-RDSessionCollectionConfiguration -CollectionName Desktop -EnableUserProfileDisk -DiskPath \\dc01.rdslab.internal\UPD -MaxUserProfileDiskSizeGB 5 -ConnectionBroker rds01.rdslab.internal` (Parameter laut Referenzauszug). Alternativ in Server Manager *Collections → Desktop → Properties → User Profile Disks* (Weg laut Learn).
3. **Nachweis:** Melde dich als `user1` an, lege eine Datei auf dem Desktop an und passe eine Einstellung an (zum Beispiel Hintergrund), melde dich ab und wieder an. Prüfe, dass beides erhalten ist, und sieh in `C:\UPD` auf `DC01` die `.vhdx`-Datei (Name nicht bestätigt).
4. **Grenzen:** Schreibe auf, warum ein UPD nur innerhalb einer Sammlung gilt (laut Quelle liegt das ganze Benutzerverzeichnis inklusive `AppData\Local` darauf) und welche Folgen das für mehrere Sammlungen hat.

#### Kontrollfragen
1. Wo liegt ein UPD, und wann wird er in die Sitzung eingebunden?
2. Warum können UPDs nicht zwischen Sammlungen wandern?
3. Was bewirkt die Größenbegrenzung, und was passiert, wenn der Datenträger voll ist (nicht bestätigt)?

### Modul 10: Gruppenrichtlinien für RDS
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, welche Einstellungen für Sitzungshosts per Computerkonfiguration wirken und wofür der Loopback-Modus gebraucht wird.
  * Nach Abschluss dieses Moduls kann der Lernende eine GPO für die OU `RDS-Server` anlegen und Verbindungsgrenzen sowie Sitzungslimits setzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung mit `gpresult` nachweisen.
* **Voraussetzungen:** Modul 4; Prüfpunkt `vor-M10` vor Beginn.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Richtlinienstruktur für RDS-Server (OU, Computer- und Benutzerkonfiguration, Loopback) | 2 |
| 10.2 | Verbindungsgrenzen und Sitzungslimits | 3 |
| 10.3 | Wirkung prüfen und Fehlersuche | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Prüfpunkt und GPO:** Erstelle `vor-M10`. Lege auf `DC01` die GPO `RDS-Server` an und verknüpfe sie mit der OU `RDS-Server` (`New-GPO`, `New-GPLink`).
2. **Verbindungsgrenze:** Aktiviere unter *Computer Configuration → Administrative Templates → Windows Components → Remote Desktop Services → Remote Desktop Session Host → Connections* die Richtlinie *Limit number of connections* (Pfad laut Learn) mit dem Wert 2.
3. **Sitzungslimit:** Setze unter *…Remote Desktop Session Host → Session Time Limits* ein Limit für getrennte Sitzungen auf 5 Minuten (Richtlinienname und Pfad nicht bestätigt; im Richtlinieneditor nachsehen).
4. **Prüfung:** Starte `gpupdate /force` auf `RDS01`, erzeuge `gpresult /h bericht.html` und finde die Richtlinien. Melde `user1` zweimal an (zweite Verbindung von einem zweiten Fenster) und notiere das Verhalten; trenne eine Sitzung, warte die Zeit ab und prüfe, ob sie beendet wird.
5. **Rückbau:** Setze beide Richtlinien auf *Not configured* oder lösche die GPO; prüfe mit `gpresult`, dass die Einstellungen nicht mehr gelten.

#### Kontrollfragen
1. Warum wirken die Einstellungen aus diesem Modul über die Computerkonfiguration auf alle Benutzer der OU?
2. Wann benötigt man den Loopback-Modus, und welche zwei Varianten gibt es (nicht bestätigt)?
3. Wie stellst du fest, welche GPO eine bestimmte Einstellung setzt?

### Modul 11: Druck- und Laufwerksumleitung
* **Priorität:** 2
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Umleitungsarten (Laufwerke, Drucker, Zwischenablage) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Umleitung im RDP-Client und per Richtlinie konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Nutzen und Sicherheitsrisiko abwägen.
* **Voraussetzungen:** Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Umleitungsarten und Funktionsweise | 2 |
| 11.2 | Konfiguration im Client und per Richtlinie | 2 |
| 11.3 | Test und Sicherheitsabwägung | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Laufwerke umleiten:** Verbinde dich mit `mstsc` von `CL01` mit aktivierter Laufwerksumleitung (Reiter *Lokale Ressourcen → Weitere*, Weg nicht bestätigt) und prüfe in der Sitzung die Freigabe `\\tsclient\C` (Name nicht bestätigt).
2. **Drucker:** Aktiviere die Druckerumleitung und prüfe, ob der auf `CL01` vorhandene Drucker „Microsoft Print to PDF“ in der Sitzung erscheint. Ein physischer Drucker ist nicht nötig.
3. **Sperren per Richtlinie:** Setze in der GPO `RDS-Server` aus Modul 10 die Richtlinie zum Verbot der Laufwerksumleitung (Pfad unter *…Remote Desktop Session Host → Device and Resource Redirection*, Name nicht bestätigt) und prüfe, dass die Umleitung nicht mehr funktioniert.
4. **Rückbau:** Setze die Richtlinie auf *Not configured* und prüfe mit `gpresult`.

#### Kontrollfragen
1. Welches Risiko entsteht, wenn Laufwerke des Clients in die Serversitzung umgeleitet werden?
2. Warum greift ein Verbot per GPO, auch wenn der Client die Umleitung anfordert (nicht bestätigt)?
3. Welche Vorteile bringt die Umleitung von Druckern, und welche Probleme sind typisch?

### Modul 12: Sicherheit und Netzwerkebenenauthentifizierung
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, was Netzwerkebenenauthentifizierung (NLA) ist und welche Gefahr sie mindert.
  * Nach Abschluss dieses Moduls kann der Lernende NLA und die Zugriffsberechtigung (Gruppe Remote Desktop Users, Anmelderecht) prüfen und konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Schutzmaßnahmen für RDP benennen (Patches, Gateway statt direkter Freigabe, starke Kontenrichtlinien).
* **Voraussetzungen:** Modul 4; Prüfpunkt `vor-M12` vor Beginn.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Gefährdung von RDP und Schutzmaßnahmen | 2 |
| 12.2 | NLA und Zugriffsberechtigung | 3 |
| 12.3 | Härtung und Ereignisse | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Ausgangslage:** Erstelle `vor-M12`. Lies den NLA-Zustand von `RDS01` (Registrywert `UserAuthentication` unter `HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp`; laut Learn bedeutet 0 „aus“) und die GPO *Require user authentication for remote connections by using Network Level Authentication* unter *…Remote Desktop Session Host → Security* (Pfad laut Learn).
2. **Richtlinie setzen:** Aktiviere die Richtlinie in der GPO `RDS-Server` und prüfe mit `gpresult`.
3. **Zugriffsfehler:** Stelle sicher, dass `user2` weder in `SG-RDS-Users` noch in der lokalen Gruppe `Remote Desktop Users` auf `RDS01` ist, und versuche eine direkte Verbindung zu `RDS01` (nicht über die Sammlung). Notiere den Fehler („restricted the types of logon“, laut Quelle) und das Ereignis 4625 im Sicherheitsprotokoll. Behebe den Fehler durch Gruppenmitgliedschaft (`Add-LocalGroupMember`), nicht durch Abschalten von NLA.
4. **Härtungs-Checkliste (schriftlich):** Schreibe auf, was du für einen produktiven RDS-Server zusätzlich tun würdest: Updates einspielen (siehe Modul 13), Gateway statt Portfreigabe, Kontosperre und Kennwortrichtlinie in der Domäne (nicht im Labor ändern), Zugriff nur für benannte Gruppen.
5. **Rückbau:** Entferne die NLA-Richtlinie aus der GPO oder setze sie auf *Not configured* und stelle sicher, dass NLA **nicht** abgeschaltet bleibt.

#### Kontrollfragen
1. Warum erfolgt die Anmeldung bei NLA vor dem Aufbau der Sitzung, und welchen Angriff erschwert das?
2. Welche beiden Gründe führen zu „The system administrator has restricted the types of logon“?
3. Warum ist das Abschalten von NLA keine gute Lösung?
4. Welche Rolle spielt das Ereignis 4625?

### Modul 13: Überwachung und Fehlersuche
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende laufende Sitzungen überwachen und Sitzungen abmelden oder Nachrichten senden.
  * Nach Abschluss dieses Moduls kann der Lernende RDS-Ereignisprotokolle und die Lizenzdiagnose auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende drei vorgegebene Störungen strukturiert eingrenzen und beheben.
* **Voraussetzungen:** Module 3, 4 und 6; Prüfpunkt `vor-M13` vor Beginn (alle drei VMs).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 13.1 | Überwachung von Sitzungen und Servern | 3 |
| 13.2 | Ereignisprotokolle und Diagnosewerkzeuge | 3 |
| 13.3 | Strukturierte Fehlersuche | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Sitzungen überwachen:** Melde `user1` an und liste die Sitzungen (`Get-RDUserSession`, `qwinsta`; Cmdlet nicht einzeln gegen die Referenz gelesen). Sende eine Nachricht (`Send-RDUserMessage`, nicht bestätigt) und beende die Sitzung (`Invoke-RDUserLogoff`, nicht bestätigt; mit `Get-Command *RDUser*` prüfen).
2. **Protokolle und Diagnose:** Suche in der Ereignisanzeige unter *Anwendungs- und Dienstprotokolle → Microsoft → Windows → TerminalServices-…* (Namen nicht bestätigt) die Einträge zur letzten Anmeldung. Starte die Lizenzdiagnose (*RD Licensing Diagnoser*, laut Release-Health-Seite vorhanden) und werte die Meldung zum Grace-Zeitraum aus.
3. **Störung 1 (Namensauflösung):** Ändere auf `DC01` den CNAME `rds` auf eine falsche Adresse. Rufe von `CL01` `https://rds.rdslab.internal/RDWeb` auf. Grenze die Ursache mit `Resolve-DnsName` ein und stelle den Eintrag wieder her.
4. **Störung 2 (Zugriff):** Entferne `user1` aus `SG-RDS-Users`. Verbinde dich als `user1`, notiere die Meldung, finde die Ursache und stelle die Mitgliedschaft wieder her.
5. **Störung 3 (Zertifikatsname):** Verbinde dich von `CL01` über die Adresse `192.168.70.20` statt über den Namen und rufe `https://192.168.70.20/RDWeb` auf. Erkläre die Zertifikatswarnung und nenne die richtige Adresse. Danach ist der Ausgangszustand wieder erreicht.
6. **Lesetext:** Lies auf der Release-Health-Seite von Windows Server 2022 den Eintrag zu Verbindungsproblemen nach dem Update vom September 2026 (laut Seite am 14.09.2026 durch ein Out-of-Band-Update behoben) und beantworte schriftlich: Was bedeutet das für die Reihenfolge, in der du Updates auf RDS-Servern einspielst?

#### Kontrollfragen
1. Welche drei Störungen hast du bearbeitet, und woran hast du jeweils die Ursache erkannt?
2. Welche Informationen zeigt das Ereignisprotokoll, die die Oberfläche nicht zeigt?
3. Warum ist es sinnvoll, vor dem Beseitigen einer Störung einen Prüfpunkt zu haben?
4. Wie bestimmst du, ob ein Problem an Name, Zertifikat, Berechtigung oder Lizenz liegt?
