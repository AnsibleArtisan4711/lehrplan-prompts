# Lehrplan: Windows Admin Center

| Kategorie | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen, Grundkenntnisse Netzwerke (IP-Adressen, Subnetze), Windows-Server-Grundlagen, Active-Directory-Grundlagen (Begriffe wie Domäne, Benutzer, Gruppen; im Labor wird **keine** Domäne aufgebaut, siehe Labor-Setup), erste Erfahrung mit PowerShell |
| **Gesamtumfang** | 9 Module, 52 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows Admin Center (modernisiertes Gateway), Windows Server 2025 (Desktopdarstellung) als Gateway und als Verwaltungsziel, Windows PowerShell 5.1 (in Windows Server enthalten) |
| **Thematische Abgrenzung (Out of Scope)** | Hyper-V (eigener Kurs; Modul 8 zeigt nur, wie man vorhandene Hyper-V-Funktionen im Windows Admin Center bedient), Failover-Clustering und Hyperkonvergenz (eigener Kurs; Clusterverbindungen nur als Theorie in Modul 3), PowerShell-Programmierung (eigener Kurs), Active Directory und Gruppenrichtlinien (eigene Kurse; im Labor keine Domäne, AD-abhängige Funktionen nur als Theorie), Azure-Integration und Windows Admin Center im Azure-Portal (nur im Überblick, nicht geübt), Entwicklung eigener Erweiterungen, Hochverfügbarkeit des Gateways |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen, Architektur, Lebenszyklus und Einordnung | 1 | 4 |
| 2 | Laborvorbereitung und Installation des Gateways | 1 | 8 |
| 3 | Verbindungen und Authentifizierung | 1 | 5 |
| 4 | Verwaltung von Rollen, Diensten, Speicher und Dateien | 1 | 8 |
| 5 | Zertifikate und Absicherung des Gateways | 1 | 5 |
| 6 | Berechtigungen, rollenbasierte Zugriffssteuerung und Protokollierung | 1 | 6 |
| 7 | Updates und Erweiterungen | 2 | 5 |
| 8 | Hyper-V-Verwaltung im Windows Admin Center | 2 | 5 |
| 9 | Fehlersuche, Diagnosewerkzeuge und Abgrenzung | 1 | 6 |
| **Gesamt** | **7x Prio 1, 2x Prio 2** | | **52** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (Pflicht, zusammen 42 UE) bilden die Kernkompetenz. Module mit Priorität 2 (Vertiefung, zusammen 10 UE) können bei Zeitmangel entfallen; kein Pflichtmodul setzt sie voraus und kein Rückbau hängt von ihnen ab.*

### 2. Quellen

Die Seiten wurden am 12.11.2026 über die Suche von Microsoft Learn in Auszügen gelesen, nicht vollständig. Die Seiten wurden nicht einzeln aufgerufen. Was nur aus dem Gedächtnis stammt, ist im Text als `nicht bestätigt` gekennzeichnet. Alle Inhalte sind eigenständig formuliert.

*   **Windows Admin Center overview** (Download über das Microsoft Evaluation Center, Update und Supportdauer je Version), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/overview](https://learn.microsoft.com/windows-server/manage/windows-admin-center/overview)
*   **What is Windows Admin Center?** (Architektur, .NET-8-Gateway), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/understand/what-is](https://learn.microsoft.com/windows-server/manage/windows-admin-center/understand/what-is)
*   **Windows Admin Center frequently asked questions** (Produktionseinsatz, Kosten, verwaltbare Versionen, Ports ändern), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/understand/faq](https://learn.microsoft.com/windows-server/manage/windows-admin-center/understand/faq)
*   **What type of installation is right for you?** (Installationsmodi, unterstützte Betriebssysteme und Browser), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/plan/installation-options](https://learn.microsoft.com/windows-server/manage/windows-admin-center/plan/installation-options)
*   **Install Windows Admin Center** (Installer, Express/Custom, Port, Zertifikat), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/deploy/install](https://learn.microsoft.com/windows-server/manage/windows-admin-center/deploy/install)
*   **Prepare your environment for Windows Admin Center** (Voraussetzungen, WinRM, Workgroup), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/deploy/prepare-environment](https://learn.microsoft.com/windows-server/manage/windows-admin-center/deploy/prepare-environment)
*   **Windows Admin Center network requirements** (Ports, ausgehender Verkehr), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/deploy/network-requirements](https://learn.microsoft.com/windows-server/manage/windows-admin-center/deploy/network-requirements)
*   **Windows Admin Center release history** (jüngste Version und Versionsübersicht), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/release-history](https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/release-history)
*   **Windows Admin Center support policy** (Modern Lifecycle Policy), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/](https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/)
*   **Windows Admin Center known issues**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/known-issues](https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/known-issues)
*   **Troubleshoot Windows Admin Center**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/troubleshooting](https://learn.microsoft.com/windows-server/manage/windows-admin-center/support/troubleshooting)
*   **Get started with Windows Admin Center** (Verbindungen hinzufügen, „Manage as“, Authentifizierung), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/use/get-started](https://learn.microsoft.com/windows-server/manage/windows-admin-center/use/get-started)
*   **Manage servers in Windows Admin Center** (Werkzeugübersicht, Updates, virtuelle Switches), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/use/manage-servers](https://learn.microsoft.com/windows-server/manage/windows-admin-center/use/manage-servers)
*   **Configure shared connections for all users of the Windows Admin Center gateway**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/shared-connections](https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/shared-connections)
*   **Configure User Access Control and Permissions** (Gateway-Zugriff, Rollen, Einmalanmeldung per ressourcenbasierter eingeschränkter Delegierung), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/user-access-control](https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/user-access-control)
*   **Update the Windows Admin Center certificate** (Zertifikat des modernisierten Gateways, Cmdlets des Konfigurationsmoduls), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/update-certificate](https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/update-certificate)
*   **Extensions for Windows Admin Center** (Erweiterungen verwalten, Feeds), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/using-extensions](https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/using-extensions)
*   **Event logging in Windows Admin Center**, Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/use/logging](https://learn.microsoft.com/windows-server/manage/windows-admin-center/use/logging)
*   **Customize WebSocket validation for Windows Admin Center gateway** (Zugriff über Namen, die nicht im Zertifikat stehen), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/websocket-validation](https://learn.microsoft.com/windows-server/manage/windows-admin-center/configure/websocket-validation)
*   **Kerberos Constrained Delegation Overview** (ressourcenbasierte eingeschränkte Delegierung), Microsoft Corporation, gelesen am 12.11.2026 (Auszug), [https://learn.microsoft.com/windows-server/security/kerberos/kerberos-constrained-delegation-overview](https://learn.microsoft.com/windows-server/security/kerberos/kerberos-constrained-delegation-overview)
*   **Hyper-V-Hinweise zu verschachtelter Virtualisierung** (`Set-VMProcessor -ExposeVirtualizationExtensions`), enthalten auf der Seite *Windows Admin Center known issues* (siehe oben).
*   Die genannten Protokolle (HTTPS/TLS, WinRM, SMB, Kerberos) werden nur in ihrer Rolle für das Windows Admin Center behandelt, soweit die obigen Quellen sie beschreiben; ihre eigenen Spezifikationen wurden **nicht** gelesen.
*   Für Lizenzbedingungen im Einzelfall (Windows-Server-Lizenzen, Evaluationsbedingungen) gilt: **Keine geprüfte Quelle** in diesem Lehrplan; sie hängen vom Vertrag ab und werden nicht genannt.

### 3. Labor-Setup & Rahmenbedingungen

Alle Praxisaufgaben finden in einer isolierten Hyper-V-Umgebung statt, ohne unkontrollierte Verbindung zum Heim- oder Produktivnetz. Das Labor besteht aus **zwei** Servern. Es gibt **keine Domäne** und **keinen Client**, weil die Kursvorgabe nur zwei Server-VMs vorsieht und das Gateway nicht auf einem Domänencontroller installiert werden darf (siehe Modul 1). Alle Funktionen, die eine Domäne brauchen (Einmalanmeldung, gruppenbasierter Gateway-Zugriff, Suche im Active Directory), werden **nur als Theorie** behandelt.

*   **Privater virtueller Switch `vSwitch-WAC-Privat`:** Netz `192.168.80.0/24`, ohne Gateway, ohne DHCP, ohne DNS-Server, alle Adressen statisch. Erforderlich ab Modul 2.
*   **VM 1: Gateway-Server (WAC01):** Windows Server 2025 (Evaluation, Desktopdarstellung), `192.168.80.10`, Arbeitsgruppe `WORKGROUP`. Trägt das Windows Admin Center als **Gateway-Server** (nach Installation in Modul 2). Der **Browser läuft auf `WAC01`** (Microsoft Edge; ob Edge auf der Desktopdarstellung vorinstalliert ist, ist `nicht bestätigt` und vor Kursbeginn zu prüfen). Das ist eine Laborvereinfachung, weil der Switch privat ist und es keinen Client gibt. Erforderlich ab Modul 2.
*   **VM 2: Verwaltungsziel (ZIEL01):** Windows Server 2025 (Evaluation, Desktopdarstellung), `192.168.80.20`, Arbeitsgruppe `WORKGROUP`. Wird in den Modulen 3 bis 9 verwaltet. Erhält in Modul 4 eine zweite virtuelle Festplatte (10 GB, leer). Erforderlich ab Modul 2.
*   **Namen:** Es gibt keinen DNS-Server. Auf beiden VMs werden in Modul 2 Einträge in der Datei `hosts` angelegt: `wac01.wac.internal` (`192.168.80.10`) und `ziel01.wac.internal` (`192.168.80.20`). Das Zertifikat des Gateways trägt in Modul 5 den Namen `wac01.wac.internal`. Verwaltungskonto auf beiden Servern: das eingebaute lokale Konto **Administrator**; die Kennwörter werden interaktiv vergeben und nicht notiert oder abgelegt. Weitere lokale Konten legen die Module selbst an (Modul 6: `leser01`).
*   **Fiktives Unternehmen:** „Alpenwerk“ (Szenarien in den Aufgaben).
*   **Software:** Das **Windows-Admin-Center-Installationsprogramm** stammt aus dem Microsoft Evaluation Center (siehe Quellen) und wird **vor Modul 2** außerhalb des Labors geladen. Ebenso die Evaluationsmedien für Windows Server 2025. Beides gelangt per virtueller Festplatte oder ISO in die VMs (Transferweg: auf dem Host eine kleine VHDX oder ISO mit der Datei erstellen und an `WAC01` anhängen). Danach hat das Labor **kein Internet**.
*   **Folgen ohne Internet:** Das Gateway und der Browser können die Microsoft-Endpunkte nicht erreichen (laut Netzwerkanforderungen geht der Verkehr ausgehend über TCP 443). Es gibt daher **keinen Erweiterungsfeed**, **keine Azure-Funktionen** und **keine Online-Prüfung auf Updates** (Modul 7). Diese Punkte werden als Theorie oder als Offline-Variante behandelt.
*   **Zertifikate:** Es gibt keine Zertifizierungsstelle im Labor. Das Gateway verwendet in Modul 2 das vom Installer erzeugte selbstsignierte Zertifikat (laut Learn läuft es nach 60 Tagen ab und ist nur für Tests gedacht). In Modul 5 wird es durch ein mit PowerShell erzeugtes, selbstsigniertes Zertifikat mit eigener Laufzeit ersetzt. Selbstsignierte Zertifikate sind ein Laborbehelf.
*   **Prüfpunkte (Hyper-V-Checkpoints), immer für beide VMs gemeinsam erstellen und gemeinsam zurücksetzen:** `M2-Basis` (Ende der Vorbereitung in Modul 2, vor der Installation), `M2-WAC` (Ende Modul 2), `vor-M4` (vor dem Anlegen des Volumes), `vor-M5`, `vor-M6`, `vor-M8`, `vor-M9`. Der Rückbau von Pflichtmodulen verwendet nur diese Prüfpunkte und nie ein Prio-2-Modul.
*   **Versions- und Supportstand (12.11.2026):** Laut der Release-History-Seite ist Version **2606** die jüngste allgemein verfügbare Version (GA). Version 2410 führte das modernisierte Gateway auf Basis von .NET 8 ein; Version 2511 stellte laut Seite die Hochverfügbarkeit wieder her. Ob nach 2606 eine neuere Version erschienen ist, und das Veröffentlichungsdatum von 2606, sind `nicht bestätigt`. Vor Kursstart die Download- und Release-Seite prüfen und die tatsächlich geladene Version notieren. Laut Support-Policy wird nur die **jeweils neueste Version ohne Vorschau** gewartet und unterstützt; man muss binnen 30 Tagen nach Erscheinen der nächsten Version aktualisieren (Modern Lifecycle Policy). Laut Learn gibt es keine zusätzlichen Kosten über die Windows-Lizenz hinaus und der Einsatz in der Produktion ist erlaubt. Windows Server 2025 ist laut Learn das am besten unterstützte Zielsystem; Windows Server 2016 und neuer werden voll unterstützt. Der Evaluationszeitraum von Windows Server 2025 ist `nicht geprüft` (aus dem Kurs „Remotedesktopdienste“ ist 180 Tage bekannt, hier nicht erneut gelesen). Menünamen sind im Text auf Englisch angegeben, wo Microsoft Learn sie so führt; deutsche Bezeichnungen sind `nicht bestätigt`.

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen, Architektur, Lebenszyklus und Einordnung
* **Priorität:** 1
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau des Windows Admin Center (Browser, Gateway, Zielserver) und die Übertragungswege (HTTPS, WinRM) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die vier Installationsmodi (lokaler Client, Gateway-Server, verwalteter Server, Failover-Cluster) unterscheiden und für eine Situation begründet wählen.
  * Nach Abschluss dieses Moduls kann der Lernende das Windows Admin Center vom Server-Manager, von PowerShell und von RSAT/MMC abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Versions-, Support- und Lizenzstand mit Datum nennen und die Einschränkung „Installation nicht auf einem Domänencontroller“ erklären.
* **Voraussetzungen:** Keine; kein Labor nötig.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Zweck und Architektur: Browser, Gateway, Zielserver; HTTPS, WinRM; modernisiertes Gateway | 2 |
| 1.2 | Installationsmodi und Abgrenzung zu Server-Manager, PowerShell und RSAT/MMC | 1 |
| 1.3 | Versions-, Support- und Lizenzstand | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Architekturzeichnung:** Zeichne für das fiktive Unternehmen „Alpenwerk“ (zwei Server, ein Administrator) die Verbindungen Browser → Gateway → Zielserver und beschrifte Protokolle und Ports (HTTPS Gateway 443, WinRM 5985/5986, SMB 445, laut Quellen; weitere Ports `nicht bestätigt`).
2. **Variantenwahl:** Wähle für drei kurze Szenarien (Einzelarbeitsplatz eines Administrators, Team mit zehn Administratoren, Cluster mit Ausfallsicherheit) den passenden Installationsmodus und begründe schriftlich.
3. **Abgrenzung:** Erstelle eine Tabelle mit je zwei Stärken und Grenzen von Windows Admin Center, Server-Manager, PowerShell und RSAT/MMC. Welche Aufgaben haben im Windows Admin Center **keine** Entsprechung? Prüfe auf den Quellseiten und notiere, was du nicht klären konntest (laut FAQ ersetzt das Windows Admin Center MMC nicht vollständig; ob Werkzeuge für Active Directory, DHCP und DNS dazugehören, wird in der Release-History für 1903 erwähnt und ist hier `nicht bestätigt`).
4. **Stand notieren:** Notiere mit Datum den Stand von Version, Supportmodell, Kosten und unterstützten Systemen und schreibe auf, was du nicht geprüft hast (zum Beispiel Datum der Version 2606).

#### Kontrollfragen
1. Auf welchem Weg spricht das Gateway mit den verwalteten Servern, und welchen Port nutzt die Verbindung vom Browser zum Gateway?
2. Warum darf das Gateway nicht auf einem Domänencontroller installiert werden?
3. Was bedeutet „Modern Lifecycle Policy“ für den Betrieb eines Gateways?
4. Nenne zwei Aufgaben, für die du eher PowerShell als das Windows Admin Center einsetzen würdest, und begründe.

### Modul 2: Laborvorbereitung und Installation des Gateways
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen privaten Hyper-V-Switch, statische Adressen und Namen über die Datei `hosts` für zwei Server einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende einen Arbeitsgruppen-Zielserver für die Verwaltung per WinRM vorbereiten (TrustedHosts, Firewall).
  * Nach Abschluss dieses Moduls kann der Lernende das Windows Admin Center im Gateway-Modus installieren und Dienst, Port und Anmeldung prüfen.
* **Voraussetzungen:** Modul 1; Installationsmedien und Installationsprogramm liegen vor (siehe Labor-Setup, Internet und Software).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Netzwerk, Adressplan, Namen über `hosts`, Arbeitsgruppe | 2 |
| 2.2 | Zielserver vorbereiten: WinRM, TrustedHosts, Firewall | 2 |
| 2.3 | Installation des Gateways (Installer, Port, Zertifikat) | 3 |
| 2.4 | Erster Start, Dienstprüfung und Prüfpunkt | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Netzwerk:** Lege `vSwitch-WAC-Privat` (privat) an und verbinde `WAC01` und `ZIEL01`. Vergib die Adressen statisch (`New-NetIPAddress`, kein Gateway) und prüfe mit `Test-NetConnection 192.168.80.20`.
2. **Namen:** Trage auf beiden VMs in `C:\Windows\System32\drivers\etc\hosts` `wac01.wac.internal` und `ziel01.wac.internal` ein (Editor mit Administratorrechten). Prüfe mit `Resolve-DnsName ziel01.wac.internal` (Hinweis: ob `Resolve-DnsName` die Datei `hosts` auswertet, ist `nicht bestätigt`; sonst `Test-NetConnection ziel01.wac.internal`).
3. **Zielserver vorbereiten:** Prüfe auf `ZIEL01` den Dienst `WinRM` (`Get-Service WinRM`), aktiviere die Remoteverwaltung bei Bedarf (`Enable-PSRemoting -Force`; ob das auf einem Server mit öffentlichem Netzwerkprofil ohne weiteren Schalter gelingt, ist `nicht bestätigt`) und prüfe die Firewallregel `WINRM-HTTP-In-TCP-PUBLIC` (`Get-NetFirewallRule -Name WINRM-HTTP-In-TCP-PUBLIC`, Name laut Learn). Beide Server liegen im selben Subnetz, die Regel braucht deshalb keine Änderung der erlaubten Adressen.
4. **TrustedHosts auf `WAC01`:** Setze `Set-Item WSMan:\localhost\Client\TrustedHosts -Value 'ziel01.wac.internal,192.168.80.20'` und lies mit `Get-Item WSMan:\localhost\Client\TrustedHosts` zurück. Teste von `WAC01` aus mit `Test-WSMan ziel01.wac.internal -Credential Administrator -Authentication Negotiate` (Parameterkombination `nicht bestätigt`; im Fehlerfall `Test-NetConnection ziel01.wac.internal -Port 5985`). Erstelle den Prüfpunkt `M2-Basis` für beide VMs.
5. **Installation:** Installiere das Windows Admin Center auf `WAC01` mit dem Installationsprogramm (Installationsart **Gateway** bei Bedarf **Custom setup**; nimm Port **443** und das vom Installer erzeugte selbstsignierte Zertifikat; deaktiviere die automatische Aktualisierung und die Übermittlung von Diagnosedaten, soweit der Assistent diese Optionen anbietet; Wortlaut der Optionen `nicht bestätigt`). Prüfe danach `Get-Service WindowsAdminCenter` (Dienstname laut Learn für das modernisierte Gateway; ältere Builds `ServerManagementGateway`) und `Get-NetTCPConnection -LocalPort 443 -State Listen`.
6. **Erster Start und Prüfpunkt:** Öffne in Edge auf `WAC01` `https://wac01.wac.internal`. Du erhältst eine Zertifikatswarnung (selbstsigniertes Zertifikat); die Warnung ist hier erwartet und wird in Modul 5 behoben. Melde dich mit dem Konto `Administrator` an (Anmeldeablauf `nicht bestätigt`) und notiere die Version aus der Oberfläche (Fundstelle `nicht bestätigt`). Erstelle den Prüfpunkt `M2-WAC` für beide VMs.

#### Kontrollfragen
1. Warum ist der virtuelle Switch privat und warum hat er kein Gateway?
2. Wozu dient `TrustedHosts` und warum ist ein weiter Eintrag wie `*` im Labor eine schlechte Gewohnheit?
3. Warum läuft der Browser im Labor auf `WAC01`, und was wäre in der Praxis besser?
4. Warum erscheint die Zertifikatswarnung, und warum ist sie in Modul 2 zulässig, aber nicht auf Dauer?

### Modul 3: Verbindungen und Authentifizierung
* **Priorität:** 1
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Server als Verbindung hinzufügen, mit alternativen Anmeldedaten („Manage as“) verwalten und Verbindungen taggen.
  * Nach Abschluss dieses Moduls kann der Lernende Verbindungslisten importieren und gemeinsame Verbindungen (Shared connections) einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende die Authentifizierungsarten (Einmalanmeldung, „Manage as“, LAPS) und die Verbindung zu Failover-Clustern erklären sowie die Einmalanmeldung per ressourcenbasierter eingeschränkter Delegierung in einer Domäne beschreiben (Theorie).
* **Voraussetzungen:** Modul 2 (Prüfpunkt `M2-WAC`).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Verbindungen hinzufügen, „Manage as“, Tags | 2 |
| 3.2 | Listen importieren, gemeinsame Verbindungen | 1 |
| 3.3 | Authentifizierungsarten und Delegierung (Theorie), Clusterverbindungen (Theorie) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Server hinzufügen:** Füge unter *All connections → Add* den Servertyp **Servers** mit dem Namen `ziel01.wac.internal` hinzu und gib die Anmeldedaten des lokalen `Administrator` an. Öffne die Verbindung und notiere die Spalte *Managing As*.
2. **Anmeldedaten wechseln:** Wähle bei der Verbindung *Manage as*, gib die Anmeldedaten erneut an und beschreibe, wie lange sie laut Quelle gelten (bis zum Neuladen des Browsers, wenn sie auf alle Verbindungen angewendet werden).
3. **Tags und Liste:** Vergib der Verbindung das Tag `labor`. Entferne sie dann aus der Liste, lege auf `WAC01` eine Textdatei an, die nur die Zeile `ziel01.wac.internal` enthält, und füge die Verbindung über *Import a list* wieder hinzu (Anmeldedaten danach erneut mit *Manage as* setzen) (laut Learn sind `.txt` und `.csv` möglich; eine durch PowerShell exportierte `.csv` ist nicht geeignet).
4. **Gemeinsame Verbindungen:** Lege als Gateway-Administrator (lokale Administratorgruppe auf `WAC01`) in den Einstellungen unter *Shared Connections* die Verbindung `ziel01.wac.internal` an und prüfe, dass die Verbindungsliste die Gruppen *Personal* und *Shared* zeigt.
5. **Theorie Einmalanmeldung (schriftlich):** Beschreibe, warum die Einmalanmeldung bei einem Gateway auf Windows Server eine Kerberos-Delegierung braucht, und gib den Befehl aus der Quelle wieder (`Set-ADComputer -Identity <Ziel> -PrincipalsAllowedToDelegateToAccount <Gateway>`, laut Learn). **Führe ihn nicht aus**, es gibt keine Domäne. Erkläre, warum im Labor (Arbeitsgruppe) stattdessen „Manage as“ nötig ist.
6. **Theorie Cluster:** Beschreibe in drei Sätzen, wie ein Failover-Cluster als eigene Verbindung hinzugefügt wird (Servertyp *Server clusters*, laut Learn) und warum das im Kurs nicht geübt wird.

#### Kontrollfragen
1. Was steht in der Spalte *Managing As*, und wozu dient sie?
2. Warum funktioniert die Einmalanmeldung im Labor nicht?
3. Welche Wirkung hat die gemeinsame Verbindungsliste für andere Benutzer des Gateways?
4. Wie unterscheidet sich die Verbindung zu einem Cluster von der Verbindung zu den einzelnen Knoten?

### Modul 4: Verwaltung von Rollen, Diensten, Speicher und Dateien
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rollen und Features installieren und entfernen, Dienste verwalten und die Wirkung per PowerShell nachprüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen neuen Datenträger initialisieren, formatieren und als Volume bereitstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse lesen, Firewallregeln und lokale Benutzer verwalten und Dateien durchsuchen.
  * Nach Abschluss dieses Moduls kann der Lernende die vom Windows Admin Center ausgeführten PowerShell-Skripte anzeigen und mit dem Werkzeug „PowerShell“ arbeiten.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Übersicht, Roles & features, Services | 2 |
| 4.2 | Speicher: Datenträger, Volumes | 2 |
| 4.3 | Files, Events, Firewall, Local users & groups | 2 |
| 4.4 | Werkzeug PowerShell und „Show PowerShell scripts“ | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Feature installieren und prüfen:** Installiere über *Roles & features* das Feature **Windows Server Backup** (harmlos, Feature-Name `Windows-Server-Backup`, Name `nicht bestätigt`; Anzeigename in der Oberfläche prüfen). Prüfe die Wirkung auf `ZIEL01` mit `Get-WindowsFeature Windows-Server-Backup`. Entferne das Feature danach wieder.
2. **Dienst verwalten:** Beende und starte den Dienst `Spooler` (Druckerwarteschlange) über das Werkzeug *Services* und prüfe mit `Get-Service Spooler`. Ändere den Starttyp nicht.
3. **Zweite Festplatte (Host):** Hänge auf dem Hyper-V-Host an `ZIEL01` eine neue, leere virtuelle Festplatte (10 GB) an. Befehl auf dem Host: `New-VHD -Path <Pfad>\ziel01-daten.vhdx -SizeBytes 10GB -Dynamic`, dann `Add-VMHardDiskDrive -VMName ZIEL01 -Path <Pfad>\ziel01-daten.vhdx` (die Ablage richtet sich nach dem Host, der Pfad ist nur ein Beispiel; hot-add auf SCSI-Controller `nicht bestätigt`, sonst die VM kurz ausschalten).
4. **Datenträger prüfen und bereitstellen:** Prüfe auf `ZIEL01` mit `Get-Disk`, dass der neue Datenträger **leer** ist (Partitionsstil *RAW*, ca. 10 GB) und notiere seine Nummer. Erstelle erst dann im Werkzeug *Storage* (Menüpunkt `nicht bestätigt`) ein Volume mit dem Laufwerksbuchstaben `E:` und der Bezeichnung `Daten`. Prüfe mit `Get-Volume -DriveLetter E`. Erstelle vorher den Prüfpunkt `vor-M4` für beide VMs.
5. **Ereignisse, Firewall, Benutzer, Dateien:** Lies im Werkzeug *Events* die letzten Einträge des Systemprotokolls, lege im Werkzeug *Firewall* eine Regel `WAC-Test` an, die TCP 8080 eingehend blockiert (Anlegen, Prüfen mit `Get-NetFirewallRule -DisplayName WAC-Test`, dann löschen), lege im Werkzeug *Local users & groups* den Benutzer `testuser01` an (Kennwort interaktiv) und lösche ihn wieder. Lege über das Werkzeug *Files* einen Ordner `E:\Alpenwerk` an.
6. **PowerShell-Werkzeug und Skripte anzeigen:** Öffne das Werkzeug *PowerShell* auf `ZIEL01` und führe `Get-Volume` aus. Aktiviere in der Oberfläche die Anzeige der PowerShell-Skripte („Show PowerShell scripts“, laut Troubleshooting-Seite) und notiere für eine der Aktionen aus Aufgabe 1 bis 5 den Skriptauszug. Vergleiche mit dem Befehl, den du selbst nutzen würdest.

#### Kontrollfragen
1. Warum prüfst du ein Ergebnis aus dem Windows Admin Center zusätzlich mit PowerShell?
2. Warum prüfst du den neuen Datenträger vor dem Formatieren mit `Get-Disk`?
3. Welche Aufgaben lösen die Werkzeuge *Services* und *Roles & features* jeweils, und wo überschneiden sie sich mit dem Server-Manager?
4. Wozu nützt „Show PowerShell scripts“ beim Lernen und beim Troubleshooting?

### Modul 5: Zertifikate und Absicherung des Gateways
* **Priorität:** 1
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Anforderungen an das TLS-Zertifikat des Gateways nennen (Serverauthentifizierung, vertrauenswürdige Zertifizierungsstelle, passender Name, privater Schlüssel).
  * Nach Abschluss dieses Moduls kann der Lernende ein Zertifikat mit PowerShell erzeugen und im Gateway mit dem Konfigurationsmodul zuweisen.
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikatsfehler (falscher Name, fehlendes Vertrauen, kein Zugriff auf den privaten Schlüssel) erkennen und beheben.
* **Voraussetzungen:** Modul 2; Prüfpunkt `vor-M5` vor Beginn.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Anforderungen an das Zertifikat; selbstsigniert und Zertifizierungsstelle | 2 |
| 5.2 | Zertifikat zuweisen mit dem Konfigurationsmodul | 2 |
| 5.3 | Browser-Vertrauen und Fehlerbilder | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Ausgangslage:** Erstelle `vor-M5`. Lies das aktuelle Zertifikat (Name, Ablaufdatum) im Browser und notiere die Laufzeit des Installer-Zertifikats.
2. **Zertifikat erzeugen:** Erzeuge auf `WAC01` ein selbstsigniertes Zertifikat: `New-SelfSignedCertificate -DnsName wac01.wac.internal -CertStoreLocation Cert:\LocalMachine\My -NotAfter (Get-Date).AddYears(1)` (Parameter laut Cmdlet-Referenz, hier nicht erneut gelesen) und prüfe Verwendung und privaten Schlüssel (`Get-ChildItem Cert:\LocalMachine\My | Format-List Subject,Thumbprint,HasPrivateKey,EnhancedKeyUsageList`; ob die Verwendung *Serverauthentifizierung* standardmäßig enthalten ist, `nicht bestätigt`).
3. **Zuweisen:** Importiere das Modul `Microsoft.WindowsAdminCenter.Configuration` (`Import-Module "$env:ProgramFiles\WindowsAdminCenter\PowerShellModules\Microsoft.WindowsAdminCenter.Configuration"`), setze das Zertifikat mit `Set-WACCertificateSubjectName -SubjectName "wac01.wac.internal"` (alternativ `-Thumbprint`), vergib den Zugriff für „Network Service“ mit `Set-WACCertificateAcl -SubjectName "wac01.wac.internal"` und starte den Dienst neu (`Restart-Service -Name WindowsAdminCenter`). Alle Cmdlets laut Learn.
4. **Vertrauen herstellen:** Exportiere die öffentliche Seite (`Export-Certificate`) und importiere sie auf `WAC01` in *Trusted Root Certification Authorities* (`Import-Certificate -CertStoreLocation Cert:\LocalMachine\Root`). Das ist ein **Laborbehelf**: in der Praxis stellt eine vertrauenswürdige Zertifizierungsstelle das Zertifikat aus. Rufe `https://wac01.wac.internal` erneut auf; die Warnung entfällt. Prüfe den Fingerabdruck des ausgelieferten Zertifikats (Thumbprint im Browser mit dem aus Aufgabe 2 vergleichen).
5. **Fehlerbild Name:** Rufe `https://192.168.80.10` auf. Erkläre die Warnung (Name nicht im Zertifikat). Notiere, dass laut Learn die Prüfung der WebSocket-Verbindung bei Zugriff über einen nicht im Zertifikat enthaltenen Namen den Zugriff verweigern kann, und beschreibe (ohne die Registry zu ändern), welche Einstellung die Quelle nennt.
6. **Fehlerbild Schlüsselzugriff (schriftlich):** Beschreibe anhand der Quelle, welches Symptom entsteht, wenn „Network Service“ keinen Zugriff auf den privaten Schlüssel hat, und wo du in der Ereignisanzeige (Protokoll *WindowsAdminCenter*) und über `certlm.msc` nachsiehst (**nicht ausführen**).

#### Kontrollfragen
1. Welche vier Anforderungen muss das Gateway-Zertifikat laut Quelle erfüllen?
2. Warum ist ein selbstsigniertes Zertifikat in der Produktion keine gute Wahl?
3. Welche Aufgabe hat `Set-WACCertificateAcl`?
4. Warum ist der Import in die vertrauenswürdigen Stammzertifizierungsstellen auf `WAC01` nur ein Laborbehelf?

### Modul 6: Berechtigungen, rollenbasierte Zugriffssteuerung und Protokollierung
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die beiden Rollen für den Zugriff auf das Gateway (Gateway users, Gateway administrators) und deren Grenzen in einer Arbeitsgruppe beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die rollenbasierte Zugriffssteuerung (RBAC) auf einem Zielserver einrichten und die drei lokalen Gruppen nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung der Rolle *Readers* prüfen und die Protokollierung der Verwaltungsaktionen auswerten.
* **Voraussetzungen:** Modul 3; Prüfpunkt `vor-M6` vor Beginn.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Zugriff auf das Gateway: Benutzer und Administratoren | 2 |
| 6.2 | RBAC auf dem Zielserver (JEA, drei lokale Gruppen) | 2 |
| 6.3 | Protokollierung der Verwaltungsaktionen und Sicherheitsgrundsätze | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Gateway-Zugriff lesen (nicht ändern):** Öffne die Einstellungen des Gateways zum Zugriff (Menüname `nicht bestätigt`) und notiere, wer Gateway-Benutzer und -Administrator ist (laut Learn sind lokale Administratoren des Gateway-Servers immer Gateway-Administratoren). Ändere nichts, weil eine falsche Änderung den Zugang sperren kann; Ersatzzugang wäre die Hyper-V-Konsole von `WAC01`. Notiere, welche Zugriffssteuerung in einer Arbeitsgruppe nicht möglich ist (laut Learn keine gruppenbasierte Steuerung in Arbeitsgruppen oder zwischen nicht vertrauten Domänen).
2. **Konto anlegen:** Lege auf `ZIEL01` den lokalen Benutzer `leser01` an (`New-LocalUser`, Kennwort interaktiv über `Read-Host -AsSecureString`). Der Benutzer ist **kein** Administrator.
3. **RBAC einschalten:** Erstelle `vor-M6`. Wende unter den Einstellungen der Verbindung `ziel01.wac.internal` die rollenbasierte Zugriffssteuerung an (laut Learn *Settings → Role-based access control → Apply*; der Vorgang dauert bis zu etwa zehn Minuten und startet WinRM neu). Prüfe danach auf `ZIEL01` mit `Get-LocalGroup -Name 'Windows Admin Center*'` die drei Gruppen *Windows Admin Center Administrators*, *… Hyper-V Administrators* und *… Readers*.
4. **Leserrolle prüfen:** Nimm `leser01` in die Gruppe *Windows Admin Center Readers* auf (`Add-LocalGroupMember`) und verbinde dich mit „Manage as“ als `leser01`. Notiere, welche Werkzeuge laut Learn eingeschränkt sind (PowerShell, Remote Desktop, Storage Replica nicht verfügbar; Files ohne Upload und Download) und prüfe, welche davon du tatsächlich so vorfindest. Schreibe auf, welche Beobachtungen von der Quelle abweichen.
5. **Protokoll auswerten:** Lies auf `ZIEL01` die Ereignisse des Kanals *WindowsAdminCenter* (`Get-WinEvent -LogName 'WindowsAdminCenter' -MaxEvents 10`; Kanalname laut Learn, Abfrage `nicht bestätigt`). Laut Learn ist die Ereignis-ID 4000 mit der Quelle `SMEGateway` für Verwaltungsaktionen vorgesehen. Finde die Aktion aus Modul 4 (zum Beispiel das Anlegen der Firewallregel) und notiere die Felder `UserOnGateway` und `UserOnTarget`.
6. **Rückbau:** Setze beide VMs auf den Prüfpunkt `vor-M6` zurück. Beschreibe dazu, warum ein gemeinsames Zurücksetzen nötig ist. (Eine Befehlszeile zum Entfernen von RBAC ist `nicht bestätigt` und wird deshalb nicht verwendet.)

#### Kontrollfragen
1. Warum bedeutet Zugriff auf das Gateway nicht automatisch Zugriff auf die Zielserver?
2. Welche drei lokalen Gruppen entstehen durch RBAC, und welche Einschränkungen hat die Leserrolle?
3. Warum gibt es laut Quelle keine eigenen (benutzerdefinierten) Rollen, und was bedeutet das für die Planung?
4. Welche Informationen enthält ein Protokolleintrag der Verwaltungsaktionen, und wie hilft er bei einer Untersuchung?

### Modul 7: Updates und Erweiterungen
* **Priorität:** 2
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Werkzeug *Updates* bedienen (verfügbare Updates, Verlauf) und erklären, welche Update-Quellen im isolierten Labor fehlen.
  * Nach Abschluss dieses Moduls kann der Lernende installierte Erweiterungen anzeigen und einen Feed auf einer Dateifreigabe (Offline-Variante) einrichten und wieder entfernen.
  * Nach Abschluss dieses Moduls kann der Lernende das Gateway selbst als Update-Aufgabe einordnen (Modern Lifecycle Policy).
* **Voraussetzungen:** Modul 3 und Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Werkzeug *Updates* und Update-Quellen | 2 |
| 7.2 | Erweiterungen und Feeds (online und offline) | 2 |
| 7.3 | Aktualisierung des Gateways selbst | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Updates ansehen:** Öffne bei `ziel01.wac.internal` das Werkzeug *Updates*, sieh dir den Update-Verlauf an und vergleiche ihn mit `Get-HotFix` auf `ZIEL01`. Löse „Online prüfen“ aus (laut Learn möglich) und notiere das Ergebnis; weil das Labor kein Internet hat, wird kein Ergebnis oder ein Fehler erwartet (Wortlaut `nicht bestätigt`).
2. **Update-Quellen (schriftlich):** Erkläre in einem Absatz, welche Quellen ein produktiver Server hätte (Microsoft Update, WSUS, Azure-Update-Verwaltung; die Azure-Integration wird nicht geübt, laut Learn setzt sie die Registrierung des Gateways bei Azure voraus).
3. **Erweiterungen ansehen:** Öffne in den Einstellungen *Extensions* und liste die installierten Erweiterungen (laut Learn mit den Reitern *Available extensions*, *Installed extensions*, *Feeds*). Notiere, warum die Liste *Available extensions* im Labor leer bleibt oder einen Fehler zeigt (kein Internet, `nicht bestätigt`).
4. **Offline-Feed:** Lege auf `WAC01` den Ordner `C:\WACFeed` an (nicht unter `C:\Users`, laut Learn) und gib „Network Service“ Lesezugriff (`icacls C:\WACFeed /grant "NT AUTHORITY\NETWORK SERVICE:(OI)(CI)RX"`; Syntax und Kontoname `nicht bestätigt`). Trage den Ordner unter *Feeds* ein und notiere das Ergebnis (der Ordner ist leer, weil es offline keine signierten Pakete gibt). Entferne den Feed danach wieder und lösche den Ordner.
5. **Gateway aktualisieren (schriftlich):** Beschreibe, wie das Gateway aktualisiert wird (neues Installationsprogramm, Microsoft Update; laut Learn beides möglich), und was dabei mit Ports und Zertifikat passiert (laut Known-Issues-Seite kann beim Wechsel von 2311 auf 2410 das Zertifikat nicht übernommen werden, siehe Modul 5).

#### Kontrollfragen
1. Warum zeigt das Werkzeug *Updates* im Labor keine verfügbaren Updates?
2. Wie gelangt eine Erweiterung in eine Umgebung ohne Internetzugang?
3. Warum prüfst du nach einem Gateway-Update das Zertifikat?
4. Was bedeutet „Update binnen 30 Tagen“ für die Betriebsplanung?

### Modul 8: Hyper-V-Verwaltung im Windows Admin Center
* **Priorität:** 2
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzung „verschachtelte Virtualisierung“ für eine VM im Labor herstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Hyper-V-Rolle über das Windows Admin Center installieren und die Werkzeuge *Virtual switches* und *Virtual machines* bedienen.
  * Nach Abschluss dieses Moduls kann der Lernende eine leere VM anlegen, starten, beenden und löschen und die Grenze zum Hyper-V-Kurs benennen.
* **Voraussetzungen:** Modul 3; Prüfpunkt `vor-M8` vor Beginn. Kein Pflichtmodul setzt dieses Modul voraus.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Voraussetzungen: verschachtelte Virtualisierung, Hyper-V-Rolle | 2 |
| 8.2 | Virtuelle Switches und virtuelle Maschinen im Windows Admin Center | 2 |
| 8.3 | Abgrenzung zum Hyper-V-Kurs und zum Hyper-V-Manager | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Ausgangslage und Host-Einstellung:** Erstelle `vor-M8`. Fahre `ZIEL01` herunter und aktiviere auf dem Host die verschachtelte Virtualisierung: `Set-VMProcessor -VMName ZIEL01 -ExposeVirtualizationExtensions $true` (Befehl laut Known-Issues-Seite). Starte `ZIEL01`.
2. **Hyper-V-Rolle installieren:** Installiere über *Roles & features* die Rolle **Hyper-V** auf `ZIEL01` (Neustart; Verwaltungswerkzeuge optional) und prüfe mit `Get-WindowsFeature Hyper-V`. Ob die Installation in der verschachtelten VM gelingt, ist `nicht bestätigt`; notiere eine Fehlermeldung wörtlich.
3. **Virtuellen Switch anlegen:** Lege im Werkzeug *Virtual switches* einen privaten Switch `vSwitch-Geschachtelt` an (laut Learn: erstellen, umbenennen, löschen). Prüfe mit `Get-VMSwitch`.
4. **Leere VM:** Lege im Werkzeug *Virtual machines* eine leere Generation-2-VM `test-vm01` ohne Betriebssystem an (Assistent und Optionen `nicht bestätigt`), starte und beende sie und lösche sie danach samt Festplatte.
5. **Rückbau und Abgrenzung:** Lösche den Switch `vSwitch-Geschachtelt`. Setze beide VMs auf den Prüfpunkt `vor-M8` zurück. Notiere schriftlich zwei Dinge, die im Hyper-V-Kurs und nicht hier behandelt werden.

#### Kontrollfragen
1. Warum ist für Hyper-V in einer VM die Option der verschachtelten Virtualisierung nötig?
2. Welche Aufgaben lassen sich im Werkzeug *Virtual machines* ausführen, und welche würdest du im Hyper-V-Manager oder per PowerShell erledigen?
3. Warum gehört das Modul zur Priorität 2?
4. Warum setzt du beide VMs gemeinsam auf `vor-M8` zurück?

### Modul 9: Fehlersuche, Diagnosewerkzeuge und Abgrenzung
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Dienst, Port, Ereignisprotokoll und Netzwerkverbindung des Gateways systematisch prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende drei vorgegebene Störungen (Gateway-Dienst, WinRM auf dem Ziel, TrustedHosts) eingrenzen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende begründet entscheiden, wann Windows Admin Center, Server-Manager, PowerShell oder RSAT/MMC das passende Werkzeug ist.
* **Voraussetzungen:** Module 2 und 3; Prüfpunkt `vor-M9` vor Beginn. Kein Prio-2-Modul ist nötig.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Diagnosewerkzeuge: Dienst, Port, Ereignisprotokoll, `Test-NetConnection`, `Test-WSMan` | 2 |
| 9.2 | Drei Störungen eingrenzen und beheben | 3 |
| 9.3 | Entscheidungshilfe: Windows Admin Center, Server-Manager, PowerShell, RSAT/MMC | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Werkzeugkasten:** Erstelle `vor-M9`. Schreibe die Diagnoseschritte auf und führe sie einmal im Gutzustand aus: `Get-Service WindowsAdminCenter`, `Test-NetConnection -ComputerName wac01.wac.internal -Port 443 -InformationLevel Detailed` (laut Troubleshooting-Seite mit `Test-NetConnection`), `Get-Service WinRM` auf `ZIEL01`, `Get-Item WSMan:\localhost\Client\TrustedHosts` auf `WAC01` und die Ereignisse des Kanals *WindowsAdminCenter*.
2. **Störung 1 (Gateway-Dienst):** Beende auf `WAC01` den Dienst `WindowsAdminCenter` (`Stop-Service`). Rufe die Oberfläche auf und notiere die Browsermeldung. Grenze die Ursache mit den Schritten aus Aufgabe 1 ein und starte den Dienst wieder.
3. **Störung 2 (WinRM auf dem Ziel):** Beende auf `ZIEL01` den Dienst `WinRM` (**erst nach dem Prüfpunkt**; Ersatzzugang ist die Hyper-V-Konsole). Öffne die Verbindung zu `ziel01.wac.internal` und notiere die Meldung (Wortlaut `nicht bestätigt`). Grenze mit `Test-NetConnection ziel01.wac.internal -Port 5985` und `Get-Service WinRM` ein und starte den Dienst wieder.
4. **Störung 3 (TrustedHosts):** Notiere den Eintrag aus `Get-Item WSMan:\localhost\Client\TrustedHosts`, leere ihn (`Clear-Item WSMan:\localhost\Client\TrustedHosts`) und öffne die Verbindung zu `ziel01.wac.internal`. Notiere die Meldung, stelle den Eintrag mit `Set-Item` wieder her und prüfe erneut.
5. **Dokumentation:** Schreibe für jede Störung Symptom, Ursache, Prüfschritt und Behebung in je drei Zeilen. Das Ergebnis ist die Grundlage für die Kontrollfrage 1.
6. **Entscheidungshilfe (Fallstudie):** Entscheide für „Alpenwerk“ (10 Server, ein Team) mit je einer Begründung, welche Aufgaben du im Windows Admin Center, im Server-Manager, in PowerShell oder mit RSAT/MMC erledigst (zum Beispiel Rolle installieren, Skript auf 10 Servern ausführen, Benutzer in AD anlegen, Leistungsüberwachung). Führe auf, was nach deinen Quellen nicht klar ist (zum Beispiel die Reichweite der Werkzeuge für AD, DHCP und DNS, `nicht bestätigt`).
7. **Rückbau:** Prüfe, dass `WindowsAdminCenter` und `WinRM` laufen und `TrustedHosts` den Eintrag trägt. Sonst setze beide VMs auf `vor-M9` zurück.

#### Kontrollfragen
1. Welche drei Störungen hast du bearbeitet, und woran hast du jeweils die Ursache erkannt?
2. Welche Prüfung unterscheidet „Gateway nicht erreichbar“ von „Zielserver nicht erreichbar“?
3. Warum ist ein Prüfpunkt vor dem Beenden von `WinRM` sinnvoll, und welchen Ersatzzugang hast du?
4. Wann ist PowerShell dem Windows Admin Center vorzuziehen?
