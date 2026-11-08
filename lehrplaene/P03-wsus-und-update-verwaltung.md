# Lehrplan: WSUS und Update-Verwaltung

| Kategorie | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU). |
| **Vorkenntnisse** | IT-Grundlagen, Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze), Active-Directory-Grundlagen, Grundkenntnisse zu Gruppenrichtlinien (GPO anlegen und mit einer OU verknüpfen), erste Erfahrung mit PowerShell |
| **Gesamtumfang** | 12 Module, 104 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows Server Update Services (WSUS), Windows Server, Windows 11 |
| **Thematische Abgrenzung (Out of Scope)** | Detaillierte AD-Architektur (Active Directory wird in Modul 2 nur als minimale Laborumgebung aufgebaut), erweiterte Routing-Protokolle, detaillierte Microsoft 365/Azure-Infrastrukturen (nur als Ausblick). Keine Überschneidung mit bestehenden Netzwerk- oder AD-Lehrplänen. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen der Update-Verwaltung & WSUS-Lebenszyklus | 1 | 8 |
| 2 | Vorbereitung der Laborumgebung (AD & Netzwerk) | 1 | 8 |
| 3 | WSUS Installation und Grundkonfiguration | 1 | 10 |
| 4 | Client-Anbindung mittels Gruppenrichtlinien (GPO) | 1 | 10 |
| 5 | WSUS-Computergruppen und Zielgruppenadressierung | 1 | 8 |
| 6 | Update-Verwaltung, Genehmigungen und Zeitpläne | 1 | 10 |
| 7 | Überwachung, Berichterstattung und Compliance | 1 | 8 |
| 8 | Wartung, Bereinigung (Cleanup) und Optimierung | 1 | 8 |
| 9 | Datenbankverwaltung (WID vs. SQL) und Speicher | 2 | 8 |
| 10 | Troubleshooting und Diagnosewerkzeuge | 1 | 10 |
| 11 | Sicherheit und Best Practices (SSL/TLS für WSUS) | 2 | 8 |
| 12 | Moderne Alternativen: WUfB, Intune und Azure Update Manager | 2 | 8 |
| **Gesamt** | **12 Module (9x Prio 1, 3x Prio 2)** | | **104 UE** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (Pflicht) bilden die Kernkompetenz. Module mit Priorität 2 (Vertiefung) können bei Zeitmangel gekürzt oder als Selbststudium ausgelagert werden.*

### 2. Quellen

* **Microsoft Learn: Windows Server Update Services (WSUS)** (Microsoft, laufend aktualisiert) - `https://learn.microsoft.com/de-de/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus`
* **Microsoft Learn: Features removed or no longer developed in Windows Server** (Microsoft, laufend aktualisiert; Einträge zu WSUS und zur Windows Internal Database, abgerufen am 08.11.2026) - `https://learn.microsoft.com/windows-server/get-started/removed-deprecated-features-windows-server`
* **RFC 1918: Address Allocation for Private Internets** (IETF, Februar 1996) - `https://datatracker.ietf.org/doc/html/rfc1918`
* **BSI IT-Grundschutz-Kompendium: SYS.1.1 Allgemeiner Server** (BSI, Edition 2023; die URL führt nur zur Übersichtsseite, der Baustein-Text wurde nicht geprüft) - `https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html`
* **BSI IT-Grundschutz-Kompendium: OPS.1.1.3 Patch- und Änderungsmanagement** (BSI, Edition 2023; Titel und Zuordnung nicht an der Originalquelle geprüft, daher vor Kursstart zu bestätigen) - `https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html`
* **Microsoft Learn: Plan your WSUS deployment** (Microsoft, abgerufen am 08.11.2026; Systemanforderungen, UUP, Report Viewer) - `https://learn.microsoft.com/windows-server/administration/windows-server-update-services/plan/plan-your-wsus-deployment`
* **Microsoft Learn: Step 2: Configure WSUS** (Microsoft, abgerufen am 08.11.2026; Client-Konfiguration, TLS/SSL) - `https://learn.microsoft.com/windows-server/administration/windows-server-update-services/deploy/2-configure-wsus`
* **Microsoft Learn: Deploy Windows client updates using WSUS** (Microsoft, abgerufen am 08.11.2026; Gruppenrichtlinien, automatische Genehmigungen) - `https://learn.microsoft.com/windows/deployment/update/waas-manage-updates-wsus`
* **Microsoft Learn: Reindex the WSUS database** (Microsoft, abgerufen am 08.11.2026) - `https://learn.microsoft.com/troubleshoot/mem/configmgr/update-management/reindex-the-wsus-database`
* **Microsoft Learn: Get-WindowsUpdateLog** (Microsoft, abgerufen am 08.11.2026) - `https://learn.microsoft.com/powershell/module/windowsupdate/get-windowsupdatelog`

### 3. Labor-Setup & Rahmenbedingungen

* **VM 1: Server-VM (erforderlich ab Modul 2)**
  * OS: Windows Server 2022 (Evaluationsversion), Computername `WSUS01`. Ressourcen (Redaktionsempfehlung): 2 vCPU, mindestens 6 GB RAM, virtuelle Festplatte mit 100 GB (dynamisch). Hintergrund: Microsoft nennt für WSUS zusätzlich 2 GB RAM zum Bedarf des Servers, mindestens 40 GB Speicher und je Windows-Version rund 10 GB für UUP-Inhalte (Quelle: *Plan your WSUS deployment*).
  * Rollen: Active Directory Domain Services (AD DS), DNS, WSUS (ab Modul 3). *Hinweis: Die Kombination von WSUS und AD auf demselben Server ist eine laborspezifische Notwendigkeit aufgrund der Beschränkung auf zwei VMs.*
  * Netzwerk: Adapter 1 (`LAB`) am isolierten privaten Hyper-V-Switch `vSwitch-WSUS-Privat`. Adapter 2 (`EXTERN`) wird nur in den **Internetphasen** (Modul 3 und 6, bei Bedarf 7 und 9) an den Hyper-V-Switch `Default Switch` (NAT, Internetzugriff über den Host) angeschlossen und danach wieder getrennt. Auf `EXTERN` wird „Adressen dieser Verbindung in DNS registrieren“ deaktiviert, damit der Domänencontroller keine zweite Adresse in DNS einträgt (nicht bestätigt).
* **VM 2: Client-VM (erforderlich ab Modul 2)**
  * OS: Windows 11 Enterprise (Evaluationsversion), Computername `CLIENT01`. Generation-2-VM mit virtuellem TPM, mindestens 4 GB RAM und 64 GB Festplatte (Mindestanforderungen von Windows 11).
  * Netzwerk: Nur an den isolierten privaten Hyper-V-Switch angebunden. Der Client benötigt zu keinem Zeitpunkt Internetzugriff; Updates bezieht er ausschließlich von `WSUS01`.
* **Netzwerk:** Privater IP-Bereich nach RFC 1918 (z. B. `192.168.100.0/24`). Domänenname: `wsuslab.internal`. Namen und Adressen: `WSUS01` = `192.168.100.10`, `CLIENT01` = `192.168.100.20`. Es gibt keinen DHCP-Server, alle Adressen sind statisch.
* **Software:** Offizielle ISO-Dateien von Microsoft (Windows Server, Windows 11). **Vorab zu beschaffen (Internetphase):** Microsoft Report Viewer samt Zusatzpaketen für die WSUS-Berichte (Modul 7) sowie `sqlcmd` und das T-SQL-Skript „Reindex the WSUS database“ (Modul 9). Ob diese Installationspakete zum Kurszeitpunkt noch verfügbar sind, ist nicht bestätigt und vor Kursbeginn zu prüfen.
* **Internetphasen:** Das Labor ist grundsätzlich isoliert. `WSUS01` braucht Internet (Adapter `EXTERN`) nur für Modul 3 (Synchronisierung mit Microsoft Update), Modul 6 (WSUS lädt die Dateien genehmigter Updates erst nach der Genehmigung herunter) und zum Beschaffen der Software für Modul 7 und 9. Danach ist `EXTERN` wieder zu trennen.
* **Prüfpunkte:** Hyper-V-Prüfpunkte beider VMs am Ende von Modul 2 (`M2-Basis`), nach Modul 3 (`M3-WSUS`), vor Modul 6 und vor Modul 11. Damit lässt sich jederzeit ohne Neuaufbau in einen bekannten Zustand zurückkehren.

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen der Update-Verwaltung & WSUS-Lebenszyklus

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Notwendigkeit von Patch-Management im Unternehmensumfeld (z. B. nach BSI IT-Grundschutz OPS.1.1.3 und SYS.1.1) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Architektur von WSUS skizzieren.
  * Nach Abschluss dieses Moduls kann der Lernende den aktuellen Lebenszyklus-Status von WSUS (Deprecated) und dessen Bedeutung einschätzen.
* **Voraussetzungen:** Keine.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Einführung in das Patch-Management und Sicherheitsstandards (BSI OPS.1.1.3, SYS.1.1) | 3 |
| 1.2 | Architektur und Funktionsweise von WSUS | 3 |
| 1.3 | Lebenszyklus: WSUS „deprecated“ (nicht mehr aktiv weiterentwickelt, laut Microsoft weiter unterstützt) und Deprecation der Windows Internal Database | 2 |

#### Praxisaufgaben (Hands-on Lab)
*Da dieses Modul rein theoretisch und konzeptionell ist, wird kein technisches Labor benötigt. Die Praxisaufgabe wird durch eine Fallstudie ersetzt.*

1. **Fallstudie Patch-Management:** Erstellen Sie ein kurzes Konzept (1 Seite) für das fiktive Unternehmen "Contoso Austria", das erklärt, warum ein zentrales Patch-Management eingeführt werden muss und welche Risiken unkontrollierte Updates (direkt über das Internet) bergen.
2. **Architekturskizze:** Zeichnen Sie die WSUS-Architektur (Microsoft Update als Upstream, WSUS-Server mit IIS, Datenbank WID oder SQL Server und Inhaltsordner, Clients per Gruppenrichtlinie, optional Downstream-Server) und beschriften Sie die Datenflüsse (Metadaten, Update-Dateien, Statusberichte).
3. **Recherche-Aufgabe:** Dokumentieren Sie anhand der Microsoft-Quelle (siehe A.2), was der Status „deprecated“ bei Microsoft-Produkten bedeutet und was er für die Nutzung von WSUS in Windows Server 2025 bedeutet. Belegen Sie jede Aussage mit der Quelle.

#### Kontrollfragen
1. Warum ist ein kontrolliertes Patch-Management (Updates prüfen, testen und zentral verteilen) im IT-Grundschutz (Baustein OPS.1.1.3) wichtig?
2. Welche Komponenten sind für eine funktionierende WSUS-Infrastruktur erforderlich?
3. Was bedeutet die Einstufung von WSUS als "deprecated" für zukünftige Neuinstallationen?

### Modul 2: Vorbereitung der Laborumgebung (AD & Netzwerk)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein isoliertes IPv4-Netzwerk nach RFC 1918 konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine grundlegende Active-Directory-Domäne bereitstellen und einen Client aufnehmen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Netzwerkkonfiguration (Hyper-V Switch, IP-Adressierung nach RFC 1918) | 2 |
| 2.2 | Installation AD DS und Heraufstufen zum Domänencontroller | 3 |
| 2.3 | Client-Integration (Domänenbeitritt) und Test der Kommunikation | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Netzwerk-Setup:** Konfigurieren Sie in Hyper-V einen privaten virtuellen Switch `vSwitch-WSUS-Privat`. Benennen Sie die Server-VM in `WSUS01` um (Neustart) und vergeben Sie die statische IP `192.168.100.10/24` (Gateway leer, DNS `127.0.0.1`).
2. **Active Directory:** Installieren Sie die Rolle „AD DS“ auf `WSUS01` und stufen Sie den Server zum Domänencontroller für die neue Gesamtstruktur `wsuslab.internal` herauf (die DNS-Serverrolle wird im Assistenten mit installiert; DSRM-Kennwort notieren). Prüfen Sie nach dem Neustart mit `Get-ADDomain` und `Resolve-DnsName wsus01.wsuslab.internal`. Legen Sie die Organisationseinheit `Clients` an: `New-ADOrganizationalUnit -Name Clients -Path "DC=wsuslab,DC=internal"`.
3. **Client-Anbindung:** Benennen Sie `CLIENT01` in `CLIENT01` um und konfigurieren Sie die IP `192.168.100.20/24` mit dem DNS-Server `192.168.100.10`. Fügen Sie `CLIENT01` der Domäne `wsuslab.internal` hinzu und verschieben Sie das Computerkonto in die OU `Clients`. Testen Sie die Namensauflösung mit `Resolve-DnsName wsus01.wsuslab.internal` und die Erreichbarkeit mit `Test-NetConnection wsus01.wsuslab.internal -Port 389`. *Hinweis: `ping` eignet sich hier nicht als Test, weil eingehende Echo-Anfragen in der Standard-Firewall blockiert sind (Standardverhalten, im Labor zu bestätigen).*
4. **Prüfpunkt:** Erstellen Sie für beide VMs je einen Hyper-V-Prüfpunkt `M2-Basis`.

#### Kontrollfragen
1. Warum wird für das Lab ein privater IP-Bereich nach RFC 1918 verwendet?
2. Welche Funktion übernimmt der DNS-Server in unserer neuen Domäne zwingend?
3. Warum ist eine Active-Directory-Domäne für die zentrale Verwaltung von WSUS-Clients von Vorteil?

### Modul 3: WSUS Installation und Grundkonfiguration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die WSUS-Rolle auf einem Windows Server installieren.
  * Nach Abschluss dieses Moduls kann der Lernende den WSUS-Konfigurationsassistenten durchlaufen und Produkte sowie Klassifizierungen auswählen.
* **Voraussetzungen:** Modul 2 (Laufende Domäne); für Aufgabe 4 eine Internetphase (siehe A.3).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Voraussetzungen für WSUS (IIS, WID, Speicherplatz) | 2 |
| 3.2 | Installation der Serverrolle WSUS | 3 |
| 3.3 | Der WSUS-Konfigurationsassistent und Initialsynchronisation | 5 |

#### Praxisaufgaben (Hands-on Lab)
1. **Rolleninstallation:** Legen Sie den Ordner `C:\WSUS` an. Fügen Sie dem Server über den Server-Manager die Rolle „Windows Server Update Services“ hinzu. Wählen Sie „WID Connectivity“ und „WSUS Services“ und tragen Sie `C:\WSUS` als Inhaltsablage ein (im Labor auf C:, weil nur eine virtuelle Festplatte vorhanden ist; Begründung siehe Kontrollfrage 2). Starten Sie den Server neu, falls gefordert.
2. **Post-Installations-Task:** Führen Sie die Konfiguration nach der Installation aus, entweder über die Benachrichtigung im Server-Manager oder in PowerShell: `cd "C:\Program Files\Update Services\Tools"`, danach `.\WsusUtil.exe postinstall CONTENT_DIR=C:\WSUS` (Syntax laut Microsoft Learn bestätigt).
3. **MIME-Typen für UUP prüfen:** Windows 11 erhält Qualitätsupdates ab Version 22H2 über die Unified Update Platform (UUP). Auf Windows Server 2022 setzt das das Kumulative Update 2023-02 oder neuer voraus, oder die MIME-Typen `.wim` (`application/x-ms-wim`) und `.msu` (`application/octet-stream`). Ob die Evaluations-ISO dieses Update schon enthält, ist nicht bestätigt. Prüfen Sie im IIS-Manager auf **Serverebene** unter „MIME-Typen“, ob beide Einträge vorhanden sind, und ergänzen Sie sie andernfalls dort (nicht auf der Website „WSUS-Verwaltung“). Dieser Schritt braucht kein Internet. (Quelle: *Plan your WSUS deployment*.)
4. **Grundkonfiguration & Initialsynchronisation (Internetphase):** Verbinden Sie `WSUS01` über den zusätzlichen Adapter `EXTERN` mit dem `Default Switch` und prüfen Sie die Verbindung mit `Test-NetConnection www.microsoft.com -Port 443`. Schlägt die Namensauflösung fehl, richten Sie auf dem DNS-Server von `WSUS01` eine Weiterleitung ein (Details nicht bestätigt). Starten Sie den WSUS-Assistenten, wählen Sie „Von Microsoft Update synchronisieren“ und beschränken Sie die Sprachen auf die benötigte (Deutsch). Wählen Sie als Produkte „Windows 11“ (passend zur Version von `CLIENT01`; neuere Windows-11-Versionen können eigene Einträge haben, Namen nicht bestätigt) und „Microsoft Defender Antivirus“ (in älteren Katalogen „Windows Defender“) sowie als Klassifizierungen „Kritische Updates“, „Sicherheitsupdates“ und „Definitionsupdates“. Die Definitionsupdates werden in Modul 6 für die erste manuelle Genehmigung gebraucht. Starten Sie die initiale Synchronisation und warten Sie in der WSUS-Konsole deren Ende ab (Dauer: Minuten bis Stunden). Die Update-Dateien werden dabei noch nicht geladen, weil WSUS sie standardmäßig erst nach der Genehmigung herunterlädt. Trennen Sie danach den Adapter `EXTERN` wieder.
5. **Prüfpunkt:** Erstellen Sie für beide VMs einen Hyper-V-Prüfpunkt `M3-WSUS`.

#### Kontrollfragen
1. Was ist die Windows Internal Database (WID) und welche Rolle spielt sie bei WSUS?
2. Warum ist es wichtig, den Inhaltsordner von WSUS nicht auf der Systempartition (Laufwerk C:) unterzubringen, wenn dies produktiv genutzt wird?
3. Welche Auswirkungen hat es, wenn zu viele Produkte und Klassifizierungen ausgewählt werden?
4. Warum lädt WSUS Update-Dateien standardmäßig erst nach der Genehmigung herunter (verzögerter Download), und welche Folge hat das für Modul 6?

### Modul 4: Client-Anbindung mittels Gruppenrichtlinien (GPO)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein GPO erstellen, um Clients an den internen WSUS-Server zu binden.
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsfähigkeit der Client-zu-Server-Kommunikation prüfen.
* **Voraussetzungen:** Modul 3 (Laufender WSUS-Dienst).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Funktionsweise der Windows Update GPOs | 3 |
| 4.2 | Konfiguration des internen Update-Dienstpfads | 4 |
| 4.3 | Client-seitiges Troubleshooting (Scan auslösen, Richtlinienprüfung, Ereignisanzeige; Hinweis zu wuauclt / usoclient) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **GPO-Erstellung:** Erstellen Sie in der Gruppenrichtlinienverwaltung ein GPO namens `WSUS-Clients` und verknüpfen Sie es mit der OU `Clients` (nicht mit der Domäne, damit `WSUS01` als Domänencontroller nicht selbst als Client seines eigenen WSUS erfasst wird).
2. **GPO-Konfiguration:** Konfigurieren Sie unter *Computerkonfiguration > Richtlinien > Administrative Vorlagen > Windows-Komponenten > Windows Update* (bei Windows 10/11 liegen die Einstellungen in Unterknoten: die Updatedienst-Einstellung unter „Von Windows Server Update Service angebotene Updates verwalten“, „Automatische Updates konfigurieren“ unter „Endbenutzererfahrung verwalten“; die deutschen Bezeichnungen sind nicht bestätigt):
   * „Internen Pfad für den Microsoft Updatedienst angeben“: aktiviert; **beide** Felder („Intranetupdatedienst zum Ermitteln von Updates festlegen“ und „Intranetstatistikserver festlegen“) auf `http://wsus01.wsuslab.internal:8530` (die URL muss mit `http://` oder `https://` beginnen).
   * „Automatische Updates konfigurieren“: aktiviert, Option 3 (Autom. Herunterladen und vor Installation benachrichtigen).
3. **Client-Test:** Prüfen Sie auf `CLIENT01` zuerst die Erreichbarkeit mit `Test-NetConnection wsus01.wsuslab.internal -Port 8530` (schlägt sie fehl, prüfen Sie die Windows-Firewall auf `WSUS01`; ob die WSUS-Installation die Regel selbst anlegt, ist nicht bestätigt). Führen Sie `gpupdate /force` aus und prüfen Sie die Wirkung mit `reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate /v WUServer`. Lösen Sie dann einen Scan aus, am sichersten über *Einstellungen > Windows Update > Nach Updates suchen*; `usoclient StartScan` ist nicht offiziell dokumentiert und seine Wirkung unter Windows 11 nicht bestätigt. Prüfen Sie in der WSUS-Konsole, ob `CLIENT01` unter „Nicht zugewiesene Computer“ auftaucht (das kann einige Minuten dauern; andernfalls das Protokoll *Microsoft-Windows-WindowsUpdateClient/Operational* in der Ereignisanzeige auswerten).

#### Kontrollfragen
1. Über welchen Standard-Port kommuniziert WSUS ohne SSL?
2. Warum muss in der GPO sowohl der Update-Dienst als auch der Statistikserver angegeben werden?
3. Wie lösen Sie unter Windows 11 eine sofortige Update-Suche aus, und was ist beim Werkzeug `usoclient` zu beachten?

### Modul 5: WSUS-Computergruppen und Zielgruppenadressierung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Computergruppen im WSUS anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende die clientseitige Zielgruppenadressierung konfigurieren und anwenden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Konzept der Computergruppen (Serverseitig vs. Clientseitig) | 2 |
| 5.2 | Erstellen von Computergruppen im WSUS | 2 |
| 5.3 | Clientseitige Zielgruppenadressierung per GPO | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Gruppen anlegen:** Erstellen Sie in der WSUS-Konsole die Computergruppen "Test-Clients" und "Produktiv-Clients".
2. **Serverseitige Zuweisung (temporär):** Verschieben Sie `CLIENT01` manuell in der WSUS-Konsole in die Gruppe „Produktiv-Clients“ (absichtlich nicht nach „Test-Clients“, damit der Unterschied zur clientseitigen Adressierung in Aufgabe 3 sichtbar wird).
3. **Clientseitige Adressierung (Dauerhaft):** Ändern Sie in der WSUS-Konsole unter *Optionen > Computer* die Einstellung auf „Gruppenrichtlinie oder Registrierungseinstellungen auf Computern verwenden“. Erweitern Sie das GPO `WSUS-Clients` um die Einstellung „Clientseitige Zielzuordnung aktivieren“ und tragen Sie als Zielgruppenname `Test-Clients` ein. Führen Sie `gpupdate /force` auf `CLIENT01` aus, lösen Sie einen Scan aus und prüfen Sie nach einigen Minuten im WSUS, dass `CLIENT01` nun in „Test-Clients“ steht, obwohl er zuvor manuell in „Produktiv-Clients“ lag (die Zuordnung ändert sich erst mit dem nächsten Statusbericht des Clients).

#### Kontrollfragen
1. Was ist der Hauptunterschied zwischen serverseitiger und clientseitiger Zielgruppenadressierung?
2. Warum macht die clientseitige Adressierung in großen Domänenumgebungen meist mehr Sinn?
3. Welche GPO-Einstellung aktiviert die clientseitige Adressierung?

### Modul 6: Update-Verwaltung, Genehmigungen und Zeitpläne

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Updates für spezifische Gruppen genehmigen oder ablehnen.
  * Nach Abschluss dieses Moduls kann der Lernende automatische Genehmigungsregeln erstellen.
* **Voraussetzungen:** Modul 3 und 5; für Aufgabe 4 eine Internetphase (siehe A.3).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Update-Status (Erforderlich, Installiert, Nicht zutreffend) | 2 |
| 6.2 | Manuelle Genehmigung und Ablehnung | 4 |
| 6.3 | Automatische Genehmigungsregeln konfigurieren | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Manuelle Genehmigung:** Erstellen Sie vorab Hyper-V-Prüfpunkte beider VMs. Suchen Sie in der WSUS-Konsole unter *Updates* mit den Filtern „Genehmigung: Alle“ und „Status: Erforderlich“ nach Updates für `CLIENT01`. Genehmigen Sie ein kleines Update, am besten ein neues Definitionsupdate (Klassifizierung „Definitionsupdates“, Produkt „Microsoft Defender Antivirus“; setzt die in Modul 3 gewählte Auswahl voraus), für die Gruppe „Test-Clients“ (Rechtsklick > Genehmigen > Zur Installation freigegeben). Updates mit Lizenzbedingungen (EULA) müssen zuerst akzeptiert werden.
2. **Ablehnen:** Lehnen Sie ein Update ab, das für `CLIENT01` nicht benötigt wird (Rechtsklick > Ablehnen), und prüfen Sie mit dem Filter „Genehmigung: Abgelehnt“, dass es dort erscheint. Notieren Sie den Titel für Modul 8.
3. **Automatische Regeln:** Erstellen Sie unter *Optionen > Automatische Genehmigungen* eine Regel „Sicherheitsupdates → Test-Clients“ (Klassifizierung: Sicherheitsupdates, Computergruppe: Test-Clients). **Klicken Sie nicht auf „Regel ausführen“:** Dabei werden alle passenden Updates genehmigt, auch ältere, was sehr große Downloads auslösen kann (Quelle: Microsoft Learn, *Deploy Windows client updates using WSUS*). Deaktivieren Sie die Regel nach dem Anlegen (Häkchen entfernen), damit in Aufgabe 4 nur das manuell genehmigte Update installiert wird. Beschreiben Sie schriftlich, wann die aktivierte Regel Updates genehmigen würde (laut Microsoft Learn bei neu synchronisierten Updates, nicht rückwirkend).
4. **Client-Installation (Internetphase):** WSUS lädt die Dateien eines Updates erst nach der Genehmigung von Microsoft herunter. Verbinden Sie `WSUS01` dafür wieder mit dem Adapter `EXTERN` und warten Sie, bis der Download in der WSUS-Konsole abgeschlossen ist. Trennen Sie `EXTERN` danach wieder. Lösen Sie auf `CLIENT01` einen Scan aus, laden Sie das genehmigte Update herunter und installieren Sie es (Option 3 benachrichtigt vor der Installation, ggf. manuell auslösen). Überprüfen Sie den Erfolgsstatus im WSUS (die Rückmeldung des Clients kann dauern).

#### Kontrollfragen
1. Was bedeutet der Status "Nicht zutreffend" bei einem Update?
2. Warum sollten Updates für Server-Infrastrukturen in der Regel nicht durch automatische Genehmigungsregeln freigegeben werden?
3. Was geschieht, wenn ein Update für eine Gruppe auf "Ablehnen" gesetzt wird?
4. Warum sollte die Schaltfläche „Regel ausführen“ bei einer Regel für Sicherheitsupdates nicht unüberlegt verwendet werden?

### Modul 7: Überwachung, Berichterstattung und Compliance

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den WSUS-Berichts-Viewer nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Update-Compliance der Infrastruktur bewerten.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Dashboard und Statusüberwachung | 2 |
| 7.2 | Generieren von Update- und Computerberichten | 4 |
| 7.3 | Interpretation der Compliance-Daten | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Dashboard und Status:** Öffnen Sie die Übersicht der WSUS-Konsole und notieren Sie den Synchronisierungsstatus, die Anzahl der Computer mit „Erforderlich“ bzw. „Fehlgeschlagen“ und den Zeitpunkt der letzten Statusmeldung von `CLIENT01`.
2. **Berichts-Viewer vorbereiten:** Die WSUS-Berichte benötigen den *Microsoft Report Viewer*. Microsoft Learn nennt den Report Viewer Redistributable 2008, für Windows Server 2016 die Runtime 2012. Für Windows Server 2022 wird in Foren die Runtime 2012 zusammen mit den *Microsoft System CLR Types for SQL Server 2012* genannt; das und die weitere Verfügbarkeit der Downloads sind nicht bestätigt. Beschaffen Sie die Pakete in einer Internetphase (z. B. aus Modul 3 oder 6) und installieren Sie sie auf `WSUS01`. Ist das nicht möglich, bearbeiten Sie statt der Aufgaben 3 und 4 die Ersatzaufgabe 6.
3. **Bericht generieren:** Erstellen Sie einen „Update-Status-Zusammenfassungsbericht“ für die Gruppe „Test-Clients“ und zusätzlich eine „Computerstatus-Zusammenfassung“ (englisch *Computer Status Summary*; die deutsche Bezeichnung ist nicht bestätigt).
4. **Export und Analyse:** Exportieren Sie den Bericht als PDF oder Excel-Datei, analysieren Sie, welche Updates noch fehlen, und bewerten Sie die Compliance von `CLIENT01`.
5. **Hinweis zum Zeitbedarf:** Der Client meldet seinen Status erst nach dem Scan und dem Neustart-/Installationsvorgang; planen Sie Wartezeit zwischen Modul 6 und diesem Modul ein.
6. **Ersatzaufgabe ohne Report Viewer:** Ermitteln Sie den Update-Stand mit PowerShell, z. B. mit `Get-WsusComputer` und `Get-WsusUpdate` (Parameter nicht bestätigt, mit `Get-Help` prüfen), und vergleichen Sie das Ergebnis mit dem Dashboard.

#### Kontrollfragen
1. Welche zusätzliche Softwarekomponente wird häufig für die WSUS-Berichterstattung benötigt?
2. Wie berechnet sich die "Prozentuale Übereinstimmung" (Compliance) eines Computers in WSUS?
3. Warum kann es passieren, dass ein Client im Bericht mit Status "Unbekannt" (Kein Status) auftaucht?

### Modul 8: Wartung, Bereinigung (Cleanup) und Optimierung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den WSUS-Serverbereinigungs-Assistenten ausführen.
  * Nach Abschluss dieses Moduls kann der Lernende veraltete Updates und Computer entfernen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Notwendigkeit der WSUS-Wartung | 2 |
| 8.2 | Der Serverbereinigungs-Assistent | 3 |
| 8.3 | Automatisierung der Bereinigung mittels PowerShell | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Ausgangsmessung:** Notieren Sie den belegten Platz im Ordner `C:\WSUS` (z. B. `(Get-ChildItem C:\WSUS -Recurse -File | Measure-Object Length -Sum).Sum / 1MB`) und den freien Speicherplatz auf Laufwerk C:.
2. **Manuelles Cleanup:** Führen Sie unter *Optionen* den *Assistenten für die Serverbereinigung* aus. Wählen Sie alle Optionen (nicht verwendete Updates, abgelaufene Updates, inaktive Computer etc.) und starten Sie den Vorgang. Notieren Sie die Zusammenfassung am Ende des Assistenten.
3. **PowerShell-Automatisierung:** Öffnen Sie PowerShell als Administrator und führen Sie das Cmdlet `Invoke-WsusServerCleanup -CleanupObsoleteUpdates -CleanupUnneededContentFiles` aus. Notieren Sie die Ausgabe.
4. **Computer entfernen:** Entfernen Sie `CLIENT01` in der WSUS-Konsole unter *Computer* (Rechtsklick > Entfernen). Lösen Sie anschließend auf dem Client einen Scan aus und prüfen Sie, dass `CLIENT01` nach dem nächsten Statusbericht wieder erscheint und in „Test-Clients“ steht (erwartetes Verhalten, nicht bestätigt). Erklären Sie, wie die Assistentenoption für Computer, die sich länger nicht gemeldet haben, diese Aufgabe automatisiert.
5. **Ergebnisprüfung:** Wiederholen Sie die Messung aus Aufgabe 1 und vergleichen Sie. Im Labor kann die Veränderung klein oder null sein, weil nur wenig Inhalt vorhanden ist; dokumentieren Sie das Ergebnis trotzdem und begründen Sie es.

#### Kontrollfragen
1. Was passiert mit Updates, die durch Microsoft durch neuere Versionen "ersetzt" (superseded) wurden?
2. Warum führt eine fehlende Bereinigung langfristig zum Ausfall der WSUS-Konsole?
3. Welches PowerShell-Cmdlet wird verwendet, um WSUS zu bereinigen?

### Modul 9: Datenbankverwaltung (WID vs. SQL) und Speicher

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen WID und einem dedizierten SQL-Server für WSUS erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Reindizierung der WSUS-Datenbank durchführen.
* **Voraussetzungen:** Modul 3; für Aufgabe 1 eine Internetphase (siehe A.3).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Datenbankarchitektur: WID vs. SQL Server (inklusive Deprecation der WID) | 2 |
| 9.2 | Verbindung zur WID herstellen (sqlcmd; SQL Server Management Studio optional) | 3 |
| 9.3 | Wartung der Datenbank (Reindexierung) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Vorbereitung (Internetphase):** Laden Sie die `sqlcmd`-Werkzeuge (Microsoft Command Line Utilities for SQL Server samt passendem ODBC-Treiber) und das T-SQL-Skript „Reindex the WSUS database“ (Quelle in A.2) herunter, installieren Sie `sqlcmd` auf `WSUS01` und speichern Sie das Skript als `C:\Skripte\SUSDBMaint.sql`. Genaue Paketnamen und Versionen sind nicht bestätigt; prüfen Sie die aktuelle Microsoft-Downloadseite.
2. **Verbindung herstellen und sichern:** Prüfen Sie in der Registry (`HKLM\Software\Microsoft\Update Services\Server\Setup`, Wert `SQLServerName`), dass SUSDB auf der WID läuft (der Wert enthält `##WID`). Verbinden Sie sich über den Named Pipe `\\.\pipe\MICROSOFT##WID\tsql\query`, z. B. mit `sqlcmd -S np:\\.\pipe\MICROSOFT##WID\tsql\query -E -Q "SELECT name FROM sys.databases"` (Schreibweise mit `np:` nicht bestätigt). Sichern Sie SUSDB vor jedem Eingriff: `BACKUP DATABASE SUSDB TO DISK = 'C:\Backup\SUSDB.bak'` (Ordner vorher anlegen).
3. **Reindex-Skript ausführen:** Starten Sie während der Wartung keine Synchronisierung. Führen Sie das gespeicherte Skript aus: `sqlcmd -S np:\\.\pipe\MICROSOFT##WID\tsql\query -E -i C:\Skripte\SUSDBMaint.sql -o C:\Skripte\reindex.log` und werten Sie das Logfile aus (Meldungen zu den neu aufgebauten Indizes).
4. **Speicherort verschieben:** Legen Sie `C:\WSUS_New` an (der Pfad muss existieren) und verschieben Sie den Inhaltsordner im Ordner `C:\Program Files\Update Services\Tools` mit `.\WsusUtil.exe movecontent C:\WSUS_New C:\Skripte\movecontent.log` (kopiert die Dateien; laut Microsoft Learn bleibt der alte Ordner bestehen). Prüfen Sie den neuen Pfad im IIS-Manager (virtuelles Verzeichnis `Content`). **Rückbau:** `.\WsusUtil.exe movecontent C:\WSUS C:\Skripte\movecontent_zurueck.log`, danach `C:\WSUS_New` löschen und prüfen, dass `CLIENT01` weiterhin Updates findet.

#### Kontrollfragen
1. Wann sollte ein dedizierter SQL-Server anstelle der WID verwendet werden?
2. Warum reicht der Serverbereinigungs-Assistent allein nicht aus, um die Leistung der WSUS-Konsole zu erhalten?
3. Wofür wird das Kommandozeilenwerkzeug `wsusutil.exe` verwendet?
4. Warum wird die Windows Internal Database laut Microsoft Learn als „deprecated“ geführt, und was bedeutet das für Neuplanungen?

### Modul 10: Troubleshooting und Diagnosewerkzeuge

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler bei der Client-Kommunikation analysieren.
  * Nach Abschluss dieses Moduls kann der Lernende Windows-Update-Protokolldateien lesen und interpretieren.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | WSUS-Fehlercodes (z. B. 0x8024402C, 0x80072EE2, 0x80072EE6) | 3 |
| 10.2 | Auswerten von WindowsUpdate.log (Get-WindowsUpdateLog) | 4 |
| 10.3 | Zurücksetzen des Windows Update-Agenten auf dem Client | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Logfile generieren:** Führen Sie auf `CLIENT01` in PowerShell den Befehl `Get-WindowsUpdateLog` aus und öffnen Sie die generierte Log-Datei auf dem Desktop. (Ab Windows 10 Version 1709 braucht die Umwandlung laut Microsoft Learn keinen Symbolserver, funktioniert also im isolierten Labor.) Sehen Sie sich zusätzlich in der Ereignisanzeige das Protokoll *Anwendungs- und Dienstprotokolle > Microsoft > Windows > WindowsUpdateClient > Betriebsbereit* an.
2. **Fehler provozieren (Port):** Ändern Sie im GPO den Port des Updatedienstes absichtlich auf `8531` (`http://wsus01.wsuslab.internal:8531`, ohne dass SSL eingerichtet ist). Führen Sie auf `CLIENT01` `gpupdate /force` und eine Update-Suche aus, analysieren Sie Fehlermeldung und Log und notieren Sie den beobachteten Fehlercode (er hängt vom Verbindungsverhalten ab und ist hier nicht vorab festgelegt). Korrigieren Sie den Port anschließend wieder auf `8530`.
3. **Fehler provozieren (Namensauflösung):** Ändern Sie im GPO den Servernamen auf einen nicht existierenden (`http://wsus01x.wsuslab.internal:8530`), wiederholen Sie die Schritte und suchen Sie im Log nach dem Fehler zur Namensauflösung (erwartet: `0x8024402C`, nicht bestätigt). Stellen Sie die URL danach wieder auf `http://wsus01.wsuslab.internal:8530` zurück.
4. **Rückbau prüfen:** Führen Sie auf `CLIENT01` `gpupdate /force` aus, prüfen Sie mit `reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate /v WUServer`, dass wieder die richtige URL gilt, lösen Sie einen Scan aus und kontrollieren Sie in der WSUS-Konsole, dass `CLIENT01` aktuell meldet. Erst danach darf mit den folgenden Modulen weitergearbeitet werden.
5. **Agent-Reset:** Schreiben Sie auf `CLIENT01` ein Batch-Skript `reset-wu.cmd` (als Administrator ausführen), das die Dienste `wuauserv` und `bits` stoppt (`net stop wuauserv`, `net stop bits`), den Ordner `C:\Windows\SoftwareDistribution` in `SoftwareDistribution.old` umbenennt (`ren`; existiert der Zielname schon, zuvor löschen) und die Dienste wieder startet. Prüfen Sie danach, dass der Ordner neu angelegt wurde und eine Update-Suche funktioniert.

#### Kontrollfragen
1. Warum ist die Datei `WindowsUpdate.log` in neueren Windows-Versionen standardmäßig nicht direkt als Textdatei lesbar?
2. Welcher Fehler wird meist durch eine fehlerhafte Namensauflösung (DNS) verursacht?
3. Welcher Dienst steuert auf dem Client die Suche und den Download von Updates?

### Modul 11: Sicherheit und Best Practices (SSL/TLS für WSUS)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende WSUS für die Nutzung von HTTPS (SSL/TLS) konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die entsprechenden GPO-Anpassungen vornehmen.
* **Voraussetzungen:** Modul 4 und abgeschlossener Rückbau aus Modul 10. Erstellen Sie vor Beginn Hyper-V-Prüfpunkte beider VMs (`vor-M11`).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Bedeutung von Verschlüsselung im Update-Prozess | 2 |
| 11.2 | Zertifikatserstellung und IIS-Bindung | 3 |
| 11.3 | Konfiguration von WSUS und GPO für HTTPS | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Zertifikat erstellen:** Erstellen Sie auf `WSUS01` in PowerShell ein selbstsigniertes Zertifikat mit dem FQDN als DNS-Namen: `$cert = New-SelfSignedCertificate -DnsName wsus01.wsuslab.internal -CertStoreLocation Cert:\LocalMachine\My`. Das Zertifikat muss auf den Namen ausgestellt sein, den die Clients in der URL verwenden; der Assistent im IIS-Manager stellt es dagegen in der Regel auf den Computernamen aus, was zu einer Namensabweichung führt (nicht bestätigt). Exportieren Sie den öffentlichen Teil (`Export-Certificate -Cert $cert -FilePath C:\Zertifikate\wsus01.cer`, Ordner vorher anlegen) und importieren Sie ihn auf `WSUS01` in die vertrauenswürdigen Stammzertifizierungsstellen des Computers (`Import-Certificate -FilePath C:\Zertifikate\wsus01.cer -CertStoreLocation Cert:\LocalMachine\Root`).
2. **IIS konfigurieren:** Fügen Sie im IIS auf der Website „WSUS-Verwaltung“ eine HTTPS-Bindung (Port 8531) mit dem erstellten Zertifikat hinzu. Setzen Sie die virtuellen Verzeichnisse `ApiRemoting30`, `ClientWebService`, `DssAuthWebService`, `ServerSyncWebService` und `SimpleAuthWebService` auf „SSL erforderlich“. `Content`, `Inventory`, `ReportingWebService` und `SelfUpdate` bleiben ohne SSL-Pflicht (Quelle: Microsoft Learn, *Step 2: Configure WSUS*).
3. **WSUSutil, GPO und Test:** Führen Sie im Ordner `C:\Program Files\Update Services\Tools` `.\WsusUtil.exe configuressl wsus01.wsuslab.internal` aus. Ändern Sie im GPO beide URL-Felder auf `https://wsus01.wsuslab.internal:8531`. Verteilen Sie `wsus01.cer` an `CLIENT01` in die vertrauenswürdigen Stammzertifizierungsstellen (per GPO unter *Windows-Einstellungen > Sicherheitseinstellungen > Richtlinien für öffentliche Schlüssel*, Menünamen nicht bestätigt, oder auf `CLIENT01` mit `Import-Certificate`). Führen Sie `gpupdate /force` und eine Update-Suche aus und prüfen Sie `Test-NetConnection wsus01.wsuslab.internal -Port 8531` sowie die Meldung von `CLIENT01` im WSUS. Verbinden Sie die WSUS-Konsole bei Bedarf über einen sicheren Anschluss (Port 8531) mit dem Server.
4. **Rückbau (empfohlen):** Stellen Sie die Prüfpunkte `vor-M11` beider VMs wieder her. Manuell wäre die URL im GPO wieder auf `http://wsus01.wsuslab.internal:8530` (beide Felder) zu setzen und „SSL erforderlich“ aufzuheben; ob `configuressl` damit vollständig zurückgenommen ist, ist nicht bestätigt, daher ist der Prüfpunkt der verlässliche Weg. Spätere Module hängen nicht vom HTTPS-Zustand ab.

#### Kontrollfragen
1. Warum sollte die WSUS-Kommunikation in einem Unternehmensnetzwerk verschlüsselt werden, obwohl die Updates selbst digital signiert sind?
2. Über welchen Port läuft WSUS standardmäßig, wenn HTTPS aktiviert wird?
3. Welche virtuellen IIS-Verzeichnisse benötigen zwingend die Einstellung "SSL erforderlich"?
4. Welche virtuellen IIS-Verzeichnisse dürfen nicht auf „SSL erforderlich“ gesetzt werden?

### Modul 12: Moderne Alternativen: WUfB, Intune und Azure Update Manager

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Unterschiede zwischen WSUS, Windows Update for Business (WUfB) und Cloud-basierten Lösungen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Migrationsstrategien von WSUS in die Cloud beschreiben.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Windows Update for Business (WUfB) Konzepte | 3 |
| 12.2 | Update-Verwaltung über Microsoft Intune | 3 |
| 12.3 | Azure Update Manager für hybride Server-Infrastrukturen | 2 |

#### Praxisaufgaben (Hands-on Lab)
*Da keine Cloud-Tenants vorausgesetzt werden, wird die Praxisaufgabe durch eine Konzeptionsaufgabe ersetzt.*

1. **Konzept Cloud-Migration:** Erstellen Sie eine Migrationsskizze für "Contoso Austria", um die Windows-11-Clients künftig über WUfB und Intune (statt WSUS) mit Updates zu versorgen. Beantworten Sie dabei die Frage, wie die Netzwerkauslastung ohne lokalen WSUS reduziert werden kann (Stichwort: Delivery Optimization / Übermittlungsoptimierung).
2. **Recherche:** Ermitteln Sie anhand der Microsoft-Dokumentation (Quelle angeben), welche Server-Betriebssysteme durch den Azure Update Manager (via Azure Arc) verwaltet werden können.

#### Kontrollfragen
1. Wie löst WUfB das Problem der Zielgruppenadressierung im Vergleich zu WSUS? (Stichwort: Deployment Rings)
2. Welche Technologie in Windows 10/11 hilft dabei, Bandbreite beim Download direkt aus dem Internet (WUfB) zu sparen?
3. Für welche Einsatzszenarien eignet sich der Azure Update Manager (Server, hybrid über Azure Arc) und für welche Intune bzw. Windows Update for Business (Clients)? Beurteilen Sie anhand der Quellen, ob die Aussage „Der Azure Update Manager ist der Nachfolger von WSUS für Server“ belegt ist.

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Die erste Fassung wurde geprüft und an den folgenden Stellen geändert. Stundensummen (104 UE), Prioritäten (9x P1, 3x P2) und Modulreihenfolge blieben unverändert. Einzelne Module enthalten jetzt mehr Aufgaben; ob der Zeitrahmen im Labor ausreicht (besonders Modul 3, 6 und 7), ist nicht erprobt.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf, A.2 | Vorkenntnis GPO und PowerShell; Quellen: WSUS-Deprecation mit geprüfter URL, BSI OPS.1.1.3, fünf Microsoft-Learn-Seiten | Quelle war „nicht geprüft“ und ohne URL; Patch-Management steht im Baustein OPS.1.1.3 (Titel nicht an der Originalquelle geprüft); Aussagen zu Deprecation, TLS, Reindex, Report Viewer und UUP hatten keine Quelle |
| A.3 | Servername `WSUS01`, Clientname `CLIENT01`, Ressourcen, zweiter Adapter `EXTERN` für Internetphasen, Vorab-Downloads, Prüfpunkte | Die URL `server.wsuslab.internal` bezog sich auf einen nie benannten Server; „NAT-Switch zuweisen“ war bei statischer IP, fehlendem Gateway und DNS `127.0.0.1` nicht umsetzbar; Speicherbedarf (UUP) war nicht angegeben |
| Modul 1 | Aufgabe Architekturskizze; Quellen und Lebenszyklus präzisiert; Kontrollfrage 1 | Lernziel „skizzieren“ hatte keine Aufgabe; SYS.1.1 ist nicht der Baustein für Patch-Management |
| Modul 2 | Rechnernamen, OU `Clients`, Tests ohne `ping`, Prüfpunkt | Eingehende Echo-Anfragen sind standardmäßig blockiert; der Gem-Test hätte Zeitüberschreitungen gemeldet |
| Modul 3 | `wsusutil postinstall`, MIME-Typen für UUP, Sprachen, Produkte/Klassifizierungen um Definitionsupdates und Defender erweitert, Internetphase, Kontrollfrage 4, Prüfpunkt | Windows 11 22H2+ braucht UUP-Unterstützung auf Server 2022; Modul 6 nutzte ein „Definitionsupdate“, das mit der Auswahl aus Modul 3 gar nicht synchronisiert wurde |
| Modul 4 | GPO an OU `Clients` statt Domäne; beide URL-Felder (Updatedienst und Statistikserver); Pfade der Einstellungen bei Windows 10/11; Erreichbarkeits- und Richtlinienprüfung; `usoclient` relativiert; Kontrollfrage 3 | Die Aufgabe setzte nur ein Feld, Kontrollfrage 2 fragte aber nach beiden; der DC wäre selbst Client geworden; `usoclient` ist nicht offiziell dokumentiert |
| Modul 5 | Manuelle Zuweisung nach „Produktiv-Clients“, danach Wechsel durch Clientseitige Zielzuordnung nach „Test-Clients“ | Der Unterschied zwischen server- und clientseitiger Adressierung war mit Zuweisung zur selben Gruppe nicht sichtbar |
| Modul 6 | Ablehnen (neue Aufgabe), Regel nicht ausführen und deaktivieren, Internetphase für den Content-Download, Kontrollfrage 4, Prüfpunkt | Lernziel „ablehnen“ hatte keine Aufgabe; die Regel hätte ältere Updates mit riesigen Downloads genehmigt und mit „nur das manuell genehmigte Update“ kollidiert; der Server war nach Modul 3 offline und konnte den Update-Inhalt nicht laden |
| Modul 7 | Dashboard-Aufgabe, Report-Viewer-Hinweis mit Unsicherheit, Computerstatus-Bericht, Ersatzaufgabe per PowerShell | Einheit 7.1 (Dashboard) und 7.2 (Computerberichte) hatten keine Aufgabe; Report Viewer ist ein Offline-Risiko |
| Modul 8 | Ausgangsmessung, Aufgabe „Computer entfernen“, Hinweis auf kleine Veränderung | Lernziel „Computer entfernen“ hatte keine Aufgabe; der Vorher-Wert wurde erst nach der Bereinigung gemessen |
| Modul 9 | `sqlcmd` und Skript als Vorbereitung, SUSDB-Sicherung, Reindex mit Logfile, `movecontent` real mit Rückbau, Kontrollfrage 4 (WID deprecated) | Das T-SQL-Skript war nicht beschafft, `sqlcmd` ist nicht installiert, „fiktiv“ verschieben ist nicht möglich, die Aufgabe 1 war nur theoretisch |
| Modul 10 | Ereignisanzeige, zwei Fehlerszenarien (Port, Namensauflösung), Rückbauprüfung, Reset-Skript genauer | Kontrollfrage 2 (DNS-Fehler) hatte keine Übung; der Rückbau wurde nicht geprüft |
| Modul 11 | Zertifikat mit FQDN per PowerShell, Zertifikat auf Server und Client vertrauen, Ausnahmen der SSL-Pflicht, Rückbau über Prüfpunkt, Kontrollfrage 4 | Ein IIS-Zertifikat auf den Computernamen passt nicht zur URL; ohne Vertrauen auf Server und Client schlägt die HTTPS-Verbindung fehl; Rückbau fehlte |
| Modul 12 | Quellenangabe in der Recherche; Kontrollfrage 3 als Beurteilung | „Nachfolger von WSUS“ ist in der verwendeten Microsoft-Quelle nicht belegt |
| Dateiende | Reststück (einzelnes Backtick-Zeichen) entfernt | Formatierungsfehler |

**Bewertung des Prüfvermerks der ersten Fassung:** Punkt 1 (Summen, Prioritäten) ist korrekt. Punkt 2 (erforderliche VMs) ist formal erfüllt, die Namen fehlten. Punkt 3 war nur teilweise erfüllt (WSUS-Deprecation „nicht geprüft“, BSI-Baustein unpassend). Punkt 4 ist nicht erfüllt: Definitionsupdate ohne Synchronisierung, Regel kollidiert mit manuellem Update. Punkt 5 ist nicht erfüllt: Lernziele zu Skizzieren, Ablehnen, Computer-Entfernen und Reindizieren hatten keine echte Aufgabe. Punkt 6 ist nicht erfüllt: Internet für den Content-Download, Report Viewer und `sqlcmd` waren nicht gelöst. Punkt 7 ist teilweise erfüllt: Die Domäne wurde aufgebaut, Namen und Software-Beschaffung fehlten.

**Hinweise und offene Punkte:**

* Alle neu ergänzten Befehle und Einstellungen wurden nur gegen Microsoft Learn und den Wissensstand geprüft, **nicht im Labor ausgeführt**.
* **Nicht bestätigt, vor Kursstart zu klären:** Verfügbarkeit von Report Viewer 2012 und System CLR Types; Paketnamen für `sqlcmd`; Schreibweise `np:` bei `sqlcmd`; ob die Server-2022-Evaluations-ISO schon UUP-fähig ist; Produktnamen für neuere Windows-11-Versionen im WSUS-Katalog; Wirkung von `usoclient`; Firewall-Regel für Port 8530; deutsche Menü- und Gruppenrichtlinienbezeichnungen; Fehlercodes in Modul 10 (Port-Fehler ohne festen Code); Rückbau von `configuressl`; Verhalten beim Entfernen und erneuten Anmelden von `CLIENT01`; Weiterleitung der DNS-Namensauflösung in der Internetphase; Titel und Zuordnung des BSI-Bausteins OPS.1.1.3.
* Microsoft führt WSUS laut der verwendeten Seite als „deprecated“ (nicht mehr aktiv weiterentwickelt, weiter unterstützt, mit Sicherheits- und Qualitätsupdates versorgt) und nennt die Windows Internal Database als zu ersetzende Komponente. Beides ist für Neuplanungen relevant und sollte vor Kursstart erneut geprüft werden.
* Das Labor hat einen einzigen Server, der Domänencontroller und WSUS zugleich ist. Das ist eine Laborvereinfachung und nicht als Produktivdesign gedacht.