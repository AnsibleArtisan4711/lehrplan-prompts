# Lehrplan: Dateidienste, DFS und Druckserver

| Attribut | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger, angehende Systemadministratoren und Systemtechniker |
| **Vorkenntnisse** | IT-Grundlagen, Netzwerk-Grundlagen (IP-Adressen, Subnetze), Active-Directory-Grundlagen, Grundkenntnisse zu Gruppenrichtlinien (GPO anlegen und mit einer OU verknüpfen) |
| **Gesamtumfang** | 12 Module, 120 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows Server 2022 (Dateiserver, DFS, Druckserver), Windows 11 |
| **Thematische Abgrenzung (Out of Scope)** | Grundlagen zu Gruppenrichtlinien (GPO) und tiefergehende Active-Directory-Verwaltung (werden in separaten Lehrplänen behandelt) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen Windows Dateiserver & SMB | 1 | 10 |
| 2 | Berechtigungskonzepte: Freigabe- und NTFS-Berechtigungen | 1 | 12 |
| 3 | Dateiserver-Verwaltung, Schattenkopien & Vorgängerversionen | 1 | 8 |
| 4 | FSRM Teil 1: Kontingente (Quotas) und Dateiprüfung | 1 | 10 |
| 5 | FSRM Teil 2: Dateiklassifizierung und Speicherberichte | 2 | 8 |
| 6 | Distributed File System (DFS) - Namespaces | 1 | 10 |
| 7 | Distributed File System (DFS) - Replikation | 1 | 10 |
| 8 | Offlinedateien und BranchCache | 2 | 8 |
| 9 | Grundlagen Windows Druckserver | 1 | 10 |
| 10 | Fortgeschrittenes Druckmanagement & GPO-Verteilung | 1 | 10 |
| 11 | Troubleshooting: Dateidienste & Druckserver | 1 | 10 |
| 12 | Abschlussprojekt: Datei- und Druckdienste mit DFS-Ausfallsicherheit | 1 | 14 |
| **Gesamt** | **12 Module (10x Prio 1, 2x Prio 2)** | | **120** |

*Hinweis zur Priorisierung: Priorität 1 kennzeichnet essenzielle Kernkompetenzen (Pflicht). Priorität 2 kennzeichnet vertiefende oder optionale Themen.*

### 2. Quellen

* **Windows Server Storage Documentation** (Herausgeber: Microsoft, Stand nicht geprüft), URL: `https://learn.microsoft.com/en-us/windows-server/storage/` (nicht geprüft)
* **DFS Namespaces overview** (Herausgeber: Microsoft, Stand nicht geprüft), URL: `https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview` (nicht geprüft)
* **File Server Resource Manager (FSRM) overview** (Herausgeber: Microsoft, Stand nicht geprüft), URL: `https://learn.microsoft.com/en-us/windows-server/storage/fsrm/fsrm-overview` (nicht geprüft)
* **Print and Document Services (Microsoft Learn)** (Herausgeber: Microsoft, Stand nicht geprüft), Keine geprüfte Quelle (URL); die ursprünglich genannte Adresse betrifft den Befehl `print` und nicht die Druckdienste
* **RFC 1918 - Address Allocation for Private Internets** (Herausgeber: IETF, Februar 1996), URL: `https://datatracker.ietf.org/doc/html/rfc1918` (nicht geprüft)

### 3. Labor-Setup & Rahmenbedingungen

Alle Praxisaufgaben werden in einer isolierten Hyper-V-Umgebung ohne physische Verbindung zum Heim- oder Produktivnetz durchgeführt. 

* **Netzwerk:** Privater Hyper-V Switch `vSwitch-File-Privat` (Netz: `192.168.10.0/24`, ohne Standardgateway). Alle VMs sind statisch konfiguriert, es gibt keinen DHCP-Server im Labor. – *Erforderlich ab Vorbereitung*.
* **VM1 (DC1):** Windows Server 2022 (Evaluation). Statische IP `192.168.10.10`. Rolle: Active Directory Domain Services (AD DS) & DNS (DNS-Server für alle VMs). Domäne: `corp.example.internal`. Dient als Voraussetzung für AGDLP, DFS und GPO. – *Erforderlich ab Vorbereitung / Modul 1*.
* **VM2 (FS1):** Windows Server 2022 (Evaluation). Statische IP `192.168.10.20`. Mitglied der Domäne. Zentrale Dateiserver- und Druckserver-Instanz. – *Erforderlich ab Modul 1*.
* **VM3 (FS2):** Windows Server 2022 (Evaluation). Statische IP `192.168.10.21`. Mitglied der Domäne. Zweiter Server für DFS-R und DFS-N. – *Erforderlich ab Modul 6*.
* **VM4 (CL1):** Windows 11 Enterprise (Evaluation). Statische IP `192.168.10.50` (kein DHCP). Mitglied der Domäne. Dient zum Testen der Freigaben, Drucker und GPOs. – *Erforderlich ab Modul 1*.

*(Vorbereitungsaufgabe für den Lehrenden/Lernenden vor Kursbeginn: Installation der VMs, statische IP-Adressen mit `192.168.10.10` (DC1) als DNS-Server auf allen VMs, Installation von AD DS und Promotion von DC1 zur Domäne `corp.example.internal`, Domain-Join von FS1, FS2 und CL1. Es wird keine Internetverbindung benötigt, alle Rollen sind im Windows Server enthalten.)*

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen Windows Dateiserver & SMB
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktion des Server Message Block (SMB) Protokolls erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Serverrolle "Dateiserver" über den Server-Manager oder PowerShell installieren.
  * Nach Abschluss dieses Moduls kann der Lernende grundlegende SMB-Freigaben erstellen und verwalten.
* **Voraussetzungen:** Betriebsbereites Labor-Setup (DC1, FS1, CL1).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Einführung in SMB-Protokolle (SMBv2, SMBv3, Verschlüsselung) | 3 |
| 1.2 | Installation der Dateiserver-Rollen | 3 |
| 1.3 | Erstellung und Verwaltung von Standard-Dateifreigaben | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Rolleninstallation:** Installiere auf `FS1` die Rolle "Dateiserver" über den Server-Manager.
2. **Freigabeerstellung:** Erstelle auf dem Laufwerk C: (oder einer dedizierten Daten-VHDX) den Ordner `C:\Shares\Public`. Gib diesen Ordner über SMB als `Public$` frei (versteckte Freigabe, Freigabeberechtigung „Domänen-Benutzer: Lesen“).
3. **Client-Test:** Melde dich an `CL1` mit einem Domänenbenutzer an und verbinde die versteckte Freigabe `\\FS1\Public$` als Netzlaufwerk.

#### Kontrollfragen
1. Welchen TCP-Port nutzt das moderne SMB-Protokoll standardmäßig?
2. Wie unterscheidet sich SMBv3 von älteren Versionen in Bezug auf Sicherheit im Netzwerk?
3. Warum ist das Anhängen eines `$`-Zeichens an den Freigabenamen in Windows-Netzwerken nützlich?

---

### Modul 2: Berechtigungskonzepte: Freigabe- und NTFS-Berechtigungen
* **Priorität:** 1
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied und das Zusammenspiel von NTFS- und Freigabeberechtigungen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende das AGDLP-Prinzip (Account, Global, Domain Local, Permission) anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende komplexe Berechtigungsstrukturen inklusive Vererbung und Zugriffsbasierter Aufzählung (ABE) konfigurieren.
* **Voraussetzungen:** Modul 1. Funktionierendes AD (DC1) für die Gruppenanlage.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Theorie: NTFS vs. Freigabeberechtigungen | 3 |
| 2.2 | Das AGDLP-Prinzip in der Praxis | 4 |
| 2.3 | Vererbung blockieren und Access-Based Enumeration (ABE) | 5 |

#### Praxisaufgaben (Hands-on Lab)
1. **AGDLP-Vorbereitung:** Lege auf `DC1` die Benutzer `IT_Admin` und `Sales_User` an sowie die globalen Gruppen `G_IT` und `G_Sales` und die domänenlokalen Gruppen `DL_Sales_Modify`, `DL_Sales_Read` und `DL_IT_Full`. Nimm die Benutzer in ihre globalen Gruppen auf (`IT_Admin` in `G_IT`, `Sales_User` in `G_Sales`) und die globalen Gruppen in die domänenlokalen: `G_Sales` in `DL_Sales_Modify`, `G_IT` in `DL_Sales_Read` und in `DL_IT_Full`.
2. **NTFS-Konfiguration:** Erstelle auf `FS1` den Ordner `C:\Shares\Unternehmensdaten` mit den Unterordnern `Vertrieb` und `IT` und gib `Unternehmensdaten` frei (Freigabeberechtigung: „Jeder - Vollzugriff“). Konfiguriere die NTFS-Berechtigungen strikt nach AGDLP: auf `Unternehmensdaten` erhält die Gruppe „Domänen-Benutzer“ nur „Ordnerinhalt auflisten“ für diesen Ordner; `Vertrieb` (Vererbung deaktiviert): `DL_Sales_Modify` Ändern, `DL_Sales_Read` Lesen; `IT` (Vererbung deaktiviert): `DL_IT_Full` Vollzugriff. Die Gruppe „Administratoren“ behält überall Vollzugriff.
3. **Access-Based Enumeration:** Aktiviere ABE für die Freigabe `Unternehmensdaten` (Freigabeeigenschaften oder `Set-SmbShare -Name Unternehmensdaten -FolderEnumerationMode AccessBased`). Prüfe mit `CL1`, dass `Sales_User` nur `Vertrieb` sieht und `IT_Admin` beide Ordner.

#### Kontrollfragen
1. Wenn ein Benutzer über die Freigabe "Lesen" hat, über NTFS aber "Ändern", welche effektive Berechtigung gilt beim Zugriff über das Netzwerk?
2. Wofür stehen die Buchstaben des AGDLP-Prinzips und warum nutzt man Domänenlokale Gruppen für die NTFS-Berechtigungsvergabe?
3. Welchen Effekt hat die Aktivierung der Zugriffsbasierte Aufzählung (Access-Based Enumeration) für Endanwender?

---

### Modul 3: Dateiserver-Verwaltung, Schattenkopien & Vorgängerversionen
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Volume Shadow Copy Service (VSS) für Dateiserver aktivieren und konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien über den Client mittels "Vorgängerversionen" wiederherstellen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Konzepte des Volume Shadow Copy Service (VSS) | 3 |
| 3.2 | Einrichtung und Zeitplanung von Schattenkopien | 3 |
| 3.3 | Wiederherstellung durch den Endanwender | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Schattenkopien aktivieren:** Aktiviere auf `FS1` für das Volume C: (bzw. das Datenvolume) Schattenkopien. Erstelle einen Zeitplan für 07:00 und 12:00 Uhr.
2. **Testdatei, manuelle Schattenkopie, Änderung (Reihenfolge einhalten):** Lege von `CL1` aus als `Sales_User` die Textdatei `Test.txt` mit dem Inhalt „Version 1“ im Ordner `Vertrieb` der Freigabe `\\FS1\Unternehmensdaten` an. Erstelle erst danach auf `FS1` sofort eine manuelle Schattenkopie. Ändere dann den Inhalt der Datei auf „Version 2“ und speichere sie.
3. **Wiederherstellung testen:** Stelle über den Windows-Explorer-Reiter „Vorgängerversionen“ auf `CL1` den Zustand „Version 1“ der Datei `Test.txt` wieder her und prüfe den Inhalt.

#### Kontrollfragen
1. Ersetzt der Volume Shadow Copy Service (VSS) ein externes Backup-System? Begründe.
2. Wo werden die Schattenkopien standardmäßig gespeichert und wie kann man Speicherplatzprobleme verhindern?
3. Welche Rolle spielt der VSS-Provider bei der Erstellung der Schattenkopie?

---

### Modul 4: FSRM Teil 1: Kontingente (Quotas) und Dateiprüfung
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ressourcen-Manager für Dateiserver (FSRM) installieren.
  * Nach Abschluss dieses Moduls kann der Lernende weiche und harte Speicherplatzkontingente (Quotas) konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Dateiprüfungsfilter (File Screening) einrichten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Installation FSRM und Grundlagen | 2 |
| 4.2 | Konfiguration von weichen und harten Kontingenten | 4 |
| 4.3 | Einrichten von Dateiprüfungsrichtlinien (File Screens) | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **FSRM Installation:** Installiere die Rolle "Ressourcen-Manager für Dateiserver" auf `FS1`.
2. **Kontingente:** Richte auf den Ordner `C:\Shares\Unternehmensdaten\Vertrieb` ein hartes Kontingent von 500 MB ein. Lege auf `FS1` die Ordner `C:\Shares\Home\IT_Admin` und `C:\Shares\Home\Sales_User` an und erstelle für `C:\Shares\Home` ein weiches Kontingent mit automatischer Anwendung auf Unterordner (Warnung bei 85 %). *Hinweis: Das harte Kontingent auf `Vertrieb` wird in Modul 7 vor der Replikation wieder entfernt.*
3. **Dateiprüfung:** Erstelle für den Ordner `C:\Shares` (damit gelten die Regeln für alle Freigaben darunter) einen aktiven Dateiprüfungsfilter nach der Vorlage „Audio- und Videodateien blockieren“. Teste die Blockierung von `CL1` aus mit einer Datei `test.mp3` im Ordner `Vertrieb`.

#### Kontrollfragen
1. Was ist der Unterschied zwischen einem harten (Hard) und einem weichen (Soft) Kontingent?
2. Warum ist die Dateiprüfung (File Screening) keine zuverlässige Anti-Malware-Lösung?
3. Wie reagiert Windows auf dem Client, wenn ein Dateiprüfungsfilter zuschlägt?

---

### Modul 5: FSRM Teil 2: Dateiklassifizierung und Speicherberichte
* **Priorität:** 2
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Klassifizierungsregeln erstellen, um Dateien automatisch mit Metadaten zu versehen.
  * Nach Abschluss dieses Moduls kann der Lernende Speicherberichte zur Analyse der Dateiserver-Nutzung generieren.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Infrastruktur für die Dateiklassifizierung | 4 |
| 5.2 | Erstellung und Planung von Speicherberichten | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Klassifizierungsregel:** Lege im Ordner `Vertrieb` zwei Textdateien an, eine davon mit dem Wort „Geheim“. Konfiguriere in FSRM auf `FS1` eine Eigenschaft `Vertraulichkeit` (Werte: Hoch, Mittel, Niedrig). Erstelle eine Klassifizierungsregel für den Ordner `Vertrieb`, die nach dem Wort „Geheim“ in Textdokumenten sucht und die Eigenschaft auf „Hoch“ setzt. Lasse die Regel manuell laufen und prüfe das Ergebnis in den Dateieigenschaften.
2. **Speicherbericht:** Erzeuge im Ordner `Vertrieb` eine Testdatei (`fsutil file createnew C:\Shares\Unternehmensdaten\Vertrieb\gross.bin 125829120`). Plane einen Speicherbericht auf `FS1`, der alle Dateien größer als 100 MB auflistet, und generiere den Bericht sofort im HTML-Format. Lösche die Testdatei danach wieder.

#### Kontrollfragen
1. In welchen Szenarien ist eine automatisierte Dateiklassifizierung besonders hilfreich?
2. In welchen Standardordner legt FSRM die generierten Speicherberichte ab?
3. Welche Herausforderung entsteht bei der inhaltsbasierten Klassifizierung bei verschlüsselten Dokumenten?

---

### Modul 6: Distributed File System (DFS) - Namespaces
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen domänenbasierten und eigenständigen DFS-Namespaces erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen domänenbasierten Namespace implementieren.
  * Nach Abschluss dieses Moduls kann der Lernende Ordnerziele hinzufügen und Verweise konfigurieren.
* **Voraussetzungen:** Modul 1 und Modul 2 (Freigabe `Unternehmensdaten` mit Ordner `Vertrieb`). `FS2` muss installiert und der Domäne beigetreten sein.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Architektur von DFS-Namespaces | 3 |
| 6.2 | Installation und Einrichtung eines domänenbasierten DFS-N | 4 |
| 6.3 | Verwaltung von Ordnern und Ordnerzielen | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Rolleninstallation:** Installiere auf `FS1` und `FS2` die DFS-Namespace-Rolle.
2. **Namespace erstellen:** Erstelle über `FS1` einen domänenbasierten Namespace namens `\\corp.example.internal\GlobalFiles`. Füge `FS1` und `FS2` als Namespaceserver hinzu.
3. **Ordnerziele verknüpfen:** Erstelle in der DFS-Verwaltung den Ordner `Vertrieb` und verknüpfe ihn mit dem UNC-Pfad `\\FS1\Unternehmensdaten\Vertrieb`. Teste den Zugriff von `CL1` auf `\\corp.example.internal\GlobalFiles\Vertrieb`.
4. **Zweites Ordnerziel und Verweise:** Erstelle auf `FS2` den Ordner `C:\Shares\Vertrieb_Replika` und gib ihn als `Vertrieb_Replika` frei (Freigabeberechtigung „Jeder - Vollzugriff“, NTFS: „Domänen-Benutzer: Ändern“). Füge `\\FS2\Vertrieb_Replika` als zweites Ordnerziel zum DFS-Ordner `Vertrieb` hinzu (die Frage nach Replikation mit „Nein“ beantworten). Stelle die Verweisreihenfolge auf „Zufällige Reihenfolge“ und prüfe in den Eigenschaften des DFS-Ordners auf `CL1` (Registerkarte „DFS“; Menünamen nicht bestätigt), mit welchem Ziel der Client verbunden ist. Ohne Replikation ist das Ziel auf `FS2` noch leer; der Test dient nur der Verweisauswahl.

#### Kontrollfragen
1. Warum bietet ein domänenbasierter Namespace eine höhere Ausfallsicherheit als ein eigenständiger (Standalone) Namespace?
2. Wie entscheiden DFS-Clients, zu welchem Zielserver sie sich verbinden, wenn mehrere Ziele für denselben Ordner existieren?
3. Was geschieht mit den echten Dateidaten auf der Festplatte, wenn man ein DFS-Ordnerziel in der Verwaltungskonsole löscht?

---

### Modul 7: Distributed File System (DFS) - Replikation
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende DFS-Replikation (DFS-R) für Daten-Redundanz konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Replikationstopologien verstehen und Bandbreitendrosselung anwenden.
* **Voraussetzungen:** Modul 6 (inklusive zweitem Ordnerziel auf `FS2`).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Funktionsweise von DFS-R (RDC-Algorithmus) | 3 |
| 7.2 | Erstellung von Replikationsgruppen, Topologien (Vollständiges Netz, Hub-and-Spoke) und Bandbreitenzeitplan | 4 |
| 7.3 | Staging-Ordner und Konfliktlösung | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Vorbereitung:** Installiere auf `FS1` und `FS2` den Rollendienst „DFS-Replikation“ (`Install-WindowsFeature -Name FS-DFS-Replication -IncludeManagementTools`). Entferne auf `FS1` das harte Kontingent auf `Vertrieb` (`Get-FsrmQuota -Path C:\Shares\Unternehmensdaten\Vertrieb | Remove-FsrmQuota`), damit Staging-Daten von DFS-R das Kontingent nicht belasten (Wechselwirkung nicht bestätigt).
2. **Replikationsgruppe:** Konfiguriere eine DFS-Replikationsgruppe `RG-Vertrieb` mit dem replizierten Ordner `Vertrieb` zwischen `FS1` (Primärmitglied, Inhalt `C:\Shares\Unternehmensdaten\Vertrieb`) und `FS2` (`C:\Shares\Vertrieb_Replika`). Wähle die Topologie „Vollständiges Netz“; Hub-and-Spoke setzt mindestens drei Mitglieder voraus (nicht bestätigt) und ist mit zwei Servern nicht sinnvoll.
3. **Testen der Replikation:** Erstelle auf `CL1` eine Datei im DFS-Pfad `\\corp.example.internal\GlobalFiles\Vertrieb` (keine Audio- oder Videodateien, da die Dateiprüfung nur auf `FS1` aktiv ist). Prüfe direkt auf der Festplatte von `FS1` und `FS2`, ob die Datei auf beiden Servern repliziert wurde.
4. **Bandbreitendrosselung:** Ändere in der Replikationsgruppe `RG-Vertrieb` den Zeitplan der Verbindung zwischen `FS1` und `FS2` auf eine begrenzte Bandbreite (z. B. 256 Kbit/s von 08:00 bis 17:00 Uhr), prüfe die Einstellung und stelle danach wieder „Volle Bandbreite“ ein.

#### Kontrollfragen
1. Wofür nutzt DFS-R den Remote Differential Compression (RDC) Algorithmus?
2. Was passiert, wenn zwei Benutzer fast gleichzeitig dieselbe Datei auf zwei unterschiedlichen DFS-R Mitgliedsservern ändern?
3. Welche Aufgabe erfüllt der "Staging-Ordner" bei der DFS-Replikation?
4. Warum erfordert die Topologie Hub-and-Spoke mindestens drei Mitglieder, und wann ist sie dem vollständigen Netz vorzuziehen?
5. Wozu dient der Bandbreitenzeitplan einer DFS-R-Verbindung, und was ist bei einer starken Drosselung zu erwarten?

---

### Modul 8: Offlinedateien und BranchCache
* **Priorität:** 2
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Offlinedateien auf Dateiserver und Client konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip von BranchCache (Hosted vs. Distributed) erklären.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Konfiguration von Offlinedateien (Client Side Caching) | 4 |
| 8.2 | Einführung und Architektur von BranchCache | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Serverkonfiguration:** Aktiviere in den Freigabeeinstellungen der Freigabe `Unternehmensdaten` auf `FS1` die Zwischenspeicherung (Caching) für Offlinedateien (alle Dateien, die der Benutzer öffnet, werden automatisch offline verfügbar gemacht).
2. **Client-Test:** Aktiviere auf `CL1` die Offlinedateien (Synchronisierungscenter bzw. Systemsteuerung „Offlinedateien“, Menünamen nicht bestätigt) und starte `CL1` neu. Greife als `Sales_User` auf die Freigabe zu und markiere den Ordner `Vertrieb` manuell für „Immer offline verfügbar“. Trenne die Netzwerkverbindung von `CL1` (VM-Netzwerkkarte trennen), bearbeite eine Datei, verbinde das Netz wieder und prüfe die Synchronisation (Sync-Center).

#### Kontrollfragen
1. Welche Konflikte können bei der Nutzung von Offlinedateien auftreten, und wie werden sie im Sync-Center gelöst?
2. Was ist der Hauptunterschied zwischen dem "Hosted Cache"-Modus und dem "Distributed Cache"-Modus bei BranchCache?
3. Warum ist BranchCache in WAN-Szenarien besonders ressourcenschonend?

---

### Modul 9: Grundlagen Windows Druckserver
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Druckerserver-Rolle installieren und die Druckverwaltungskonsole bedienen.
  * Nach Abschluss dieses Moduls kann der Lernende Netzwerkdrucker, lokale Ports und Druckertreiber verwalten.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Druckarchitektur in Windows Server | 3 |
| 9.2 | Installation und Konfiguration der Druckerserver-Rolle | 3 |
| 9.3 | Verwaltung von Ports, Warteschlangen und Treibern | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Installation:** Installiere die Rolle "Druck- und Dokumentdienste" auf `FS1`.
2. **Drucker anlegen:** Öffne die Druckverwaltung. Erstelle einen lokalen TCP/IP-Port auf die fiktive IP `192.168.10.150`. Installiere den Standardtreiber „Generic / Text Only“ (Verfügbarkeit nicht bestätigt) und richte einen Drucker namens `PRN-Sales-Color` ein.
3. **Freigabe:** Gib den Drucker als `PRNSalesColor` frei. Verbinde ihn manuell auf dem Client `CL1`.

#### Kontrollfragen
1. Was ist der Unterschied zwischen einem Druckgerät (Hardware) und einem logischen Drucker (Warteschlange) im Windows-Kontext?
2. Warum ist die Trennung der Druckertreiber (Isolation) für die Stabilität des Spooler-Dienstes essenziell?
3. Welchen Standardport nutzen moderne Netzwerkdrucker typischerweise?

---

### Modul 10: Fortgeschrittenes Druckmanagement & GPO-Verteilung
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Druckerpools zur Lastverteilung einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Drucker automatisiert mittels Gruppenrichtlinien (GPOs) an Clients verteilen.
* **Voraussetzungen:** Modul 9, Basiswissen Gruppenrichtlinien. DC1.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Druckerpools und Priorisierung von Warteschlangen | 4 |
| 10.2 | Bereitstellung von Druckern per Gruppenrichtlinien | 6 |

#### Praxisaufgaben (Hands-on Lab)
1. **Druckerpool (simuliert):** Erstelle auf `FS1` einen zweiten TCP/IP-Port auf die fiktive IP `192.168.10.151`. Aktiviere für den Drucker `PRN-Sales-Color` das Druckerpooling mit beiden Ports (`192.168.10.150` und `192.168.10.151`). Es gibt keine echten Druckgeräte, geprüft wird die Konfiguration.
2. **GPO-Vorbereitung:** Erstelle auf `DC1` die OU `Sales` und verschiebe das Computerkonto `CL1` sowie den Benutzer `Sales_User` dorthin (Standardcontainer „Computers“ und „Users“ lassen sich nicht mit einem GPO verknüpfen). Erstelle ein neues GPO `GPO_Printer_Sales` und verknüpfe es mit der OU `Sales`.
3. **Verteilung:** Nutze auf `FS1` die Druckverwaltung, um den Drucker `PRN-Sales-Color` mittels „Mit Gruppenrichtlinie bereitstellen“ dem GPO `GPO_Printer_Sales` hinzuzufügen und wähle die Benutzerrichtlinie. Führe auf `CL1` `gpupdate /force` aus, melde dich als `Sales_User` neu an und prüfe mit `Get-Printer`, ob der Drucker automatisch verbunden wurde.

#### Kontrollfragen
1. Welche technische Voraussetzung (Hardware/Treiber) muss erfüllt sein, damit ein Druckerpool reibungslos funktioniert?
2. Wenn ein Drucker per "Computerrichtlinie" verteilt wird, für wen ist er auf dem Client-PC sichtbar?
3. Wie kann man mit zwei logischen Druckern und unterschiedlichen Prioritäten auf dasselbe physische Druckgerät dafür sorgen, dass Geschäftsführer-Druckaufträge bevorzugt gedruckt werden?

---

### Modul 11: Troubleshooting: Dateidienste & Druckserver
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehlerquellen (z. B. Print Spooler Crash, DFS-R Backlog) analysieren und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende NTFS-Berechtigungskonflikte auflösen.
* **Voraussetzungen:** Modul 2, Modul 7, Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Spooler-Probleme analysieren und beheben | 3 |
| 11.2 | Effektiver NTFS-Zugriff und Besitzerübernahme | 3 |
| 11.3 | Überwachung und Fehlerbehebung in DFS-R | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Druckwarteschlange bereinigen:** Drucke auf `FS1` eine Testseite auf `PRN-Sales-Color` (die IP `192.168.10.150` existiert nicht, der Auftrag bleibt in der Warteschlange hängen). Stoppe den Dienst „Druckwarteschlange“ (Spooler), lösche manuell die Dateien im Ordner `C:\Windows\System32\spool\PRINTERS` und starte den Dienst neu.
2. **Besitz übernehmen:** Lege auf `FS1` den Testordner `C:\Shares\Test_Besitz` an (außerhalb der DFS-Ordner). Entferne (als Admin) mutwillig alle Rechte für die Gruppe „Administratoren“ von diesem Ordner. Nutze den Reiter „Sicherheit -> Erweitert“, um als Administrator den Besitz zu übernehmen und die Rechte zurückzusetzen.
3. **DFS-R Backlog erzeugen, analysieren und beheben:** Stoppe auf `FS2` den Dienst `DFSR` (`Stop-Service DFSR`). Lege auf `FS1` im Ordner `Vertrieb` fünf Textdateien an. Miss den Rückstand mit `dfsrdiag backlog /rgname:RG-Vertrieb /rfname:Vertrieb /smem:FS1 /rmem:FS2` (er sollte größer als 0 sein). Starte den Dienst auf `FS2` wieder (`Start-Service DFSR`), wiederhole die Messung bis der Rückstand 0 ist und erzeuge in der DFS-Verwaltung einen Diagnosebericht für `RG-Vertrieb`, um Fehler und Rückstände auszuwerten.

#### Kontrollfragen
1. Welche Schritte sind zwingend erforderlich, um einen hängenden Druckauftrag, der sich in der GUI nicht löschen lässt, auf Dateiebene zu entfernen?
2. Warum nützt die Mitgliedschaft in der lokalen Administratorengruppe nichts, wenn die NTFS-Rechte für "Administratoren" explizit auf "Verweigern" gesetzt sind?
3. Was bedeutet der Zustand "Journal Wrap Error" im Kontext der DFS-Replikation?

---

### Modul 12: Abschlussprojekt: Datei- und Druckdienste mit DFS-Ausfallsicherheit
* **Priorität:** 1
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die gelernten Konzepte (AGDLP, DFS-N, DFS-R, GPO-Verteilung) in einer ganzheitlichen Architektur zusammenführen und validieren.
* **Voraussetzungen:** Module 1 bis 4, 6, 7 und 9 bis 11 (Modul 5 und 8 sind nicht nötig). Die Konfigurationen der vorherigen Labore werden als Basis verwendet.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Konzeptionierung und Design der Infrastruktur | 4 |
| 12.2 | Umsetzung: Rollout und Konfiguration | 6 |
| 12.3 | Validierung, Failover-Tests und Dokumentation | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Strukturaufbau:** Ergänze den Namespace `\\corp.example.internal\GlobalFiles` um die Ordner `HR` und `IT` (der Ordner `Vertrieb` entspricht der Abteilung Sales). Lege dafür auf `FS1` die Ordner `C:\Shares\HR` und `C:\Shares\IT_Daten`, auf `FS2` die Ordner `C:\Shares\HR_Replika` und `C:\Shares\IT_Replika` an, gib sie frei und verknüpfe beide Ziele je DFS-Ordner. Konfiguriere die Replikationsgruppen `RG-HR` und `RG-IT` zwischen `FS1` und `FS2` (zusätzlich zu `RG-Vertrieb`).
2. **Rechtevergabe:** Wende auf alle Abteilungsordner AGDLP an: lege `G_HR`, `DL_HR_Modify` und `DL_IT_ReadAll` an. HR bekommt Ändern nur auf `HR`, Sales nur auf `Vertrieb`, IT darf alle drei Ordner lesen und `IT_Daten` ändern. Weise die Rechte auf beiden Servern identisch zu (DFS-R repliziert keine Freigabeberechtigungen und Sie müssen beide Ziele prüfen) und teste mit je einem Benutzer pro Gruppe.
3. **Druckerverteilung integrieren:** Verteile den Drucker `PRN-Sales-Color` per GPO `GPO_Printer_Sales` nur an die OU `Sales` (siehe Modul 10) und weise nach, dass ein Benutzer außerhalb dieser OU den Drucker nicht erhält.
4. **Ausfallsimulation (Failover-Test):** Greife von `CL1` über den DFS-Namespace auf die Daten zu. Schalte den Server `FS1` abrupt ab (Hyper-V „Ausschalten“); `DC1` und `FS2` bleiben an. Prüfe, wie sich der Client verhält, wie lange das Failover zu `FS2` dauert, und dokumentiere die Resultate. Prüfe zusätzlich den Drucker `PRN-Sales-Color` (er läuft nur auf `FS1` und ist beim Ausfall nicht erreichbar; ein Druckserver-Cluster gehört nicht zum Lehrplan) und halte fest, dass `DC1` ein Single Point of Failure ist. Behebe nach dem Neustart von `FS1` eventuelle Replikationsfehler.

#### Kontrollfragen
1. Warum schützt DFS-R allein nicht vor versehentlichem Löschen von Dateien (Ransomware/Anwenderfehler) und welche Rolle spielen Schattenkopien in diesem Szenario?
2. Welcher Mechanismus im AD sichert die Aktualisierung der DFS-Ordnerziele auf dem Client bei einem Ausfall?
3. Inwiefern unterstützt eine saubere Trennung von Namespaces und physischen Servern zukünftige Hardware-Migrationen?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Die erste Fassung wurde geprüft und an den folgenden Stellen geändert. Stundensummen, Prioritäten (10x P1 mit 104 UE, 2x P2 mit 16 UE) und Modulreihenfolge blieben unverändert (12 Module, 120 UE).

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf, A.2 | Vorkenntnis „Gruppenrichtlinien“ ergänzt; Quelle zu den Druckdiensten ohne falsche URL | Modul 10 setzt GPO-Basiswissen voraus, das aber „Out of Scope“ war; die URL betraf den Befehl `print` |
| A.3 | Switch-Name, DNS auf DC1, CL1 statisch statt „DHCP oder statisch“, Vorbereitung konkretisiert | Im Labor gibt es keinen DHCP-Server; Domänenbeitritt braucht DNS auf DC1 |
| Modul 2 | Benutzer in globale Gruppen aufgenommen, Gruppen klar zugeordnet, zweiter Ordner `IT` und Rechte festgelegt, ABE-Test konkret | AGDLP war unvollständig (kein Schritt A nach G), ABE war mit nur einem Ordner nicht prüfbar |
| Modul 3 | Reihenfolge geändert: Testdatei, dann Schattenkopie, dann Änderung; „Vertriebs-Freigabe“ ersetzt | Die Schattenkopie entstand vor der Datei, eine Vorgängerversion war so nicht vorhanden |
| Modul 4 | Home-Ordner angelegt (weiches Kontingent war nur „falls vorhanden“), Dateiprüfung auf `C:\Shares` mit Vorlage | Lernziel weiche Kontingente war nicht sicher geübt, „alle Freigaben“ war unklar |
| Modul 5 | Testdateien angelegt und aufgeräumt | Klassifizierung und Bericht hatten keine Daten |
| Modul 6 | Voraussetzung Modul 2; Aufgabe 4 (zweites Ziel, Verweise) | Lernziel „Verweise konfigurieren“ und „Ordnerziele hinzufügen“ waren nur Theorie bzw. nur ein Ziel |
| Modul 7 | Rollendienst DFS-Replikation installieren; Hub-and-Spoke entfernt (mind. drei Mitglieder); Gruppenname `RG-Vertrieb`; Kontingent entfernen; Aufgabe 4 (Bandbreite); Kontrollfragen 4 und 5 | Die Rolle wurde nie installiert, die Topologie war mit zwei Servern nicht möglich, Lernziel Bandbreitendrosselung war ungeprüft |
| Modul 8 | Freigabe `Unternehmensdaten`; Offlinedateien auf dem Client aktivieren | Es gab keine „Vertriebs-Freigabe“, die Client-Konfiguration fehlte |
| Modul 9 | Standardtreiber ohne „Microsoft Print to PDF“ | Verfügbarkeit des Treibers auf dem Server nicht bestätigt |
| Modul 10 | Zweiter Port, OU `Sales` mit CL1 und Benutzer, Benutzerrichtlinie, Prüfung mit `Get-Printer` | GPOs lassen sich nicht mit dem Container „Computers“ verknüpfen, der Pool hatte keinen zweiten Port |
| Modul 11 | Hängender Druckauftrag konkret, Testordner, DFS-R-Rückstand erzeugt und mit `dfsrdiag backlog` behoben | „Beheben“ von Rückständen (Lernziel) war nur ein Bericht, ohne Fehler |
| Modul 12 | Titel angepasst („hochverfügbare Druckdienste“ sind ohne Cluster nicht möglich); Voraussetzungen ohne optionale Module 5 und 8; Strukturen, Rechte, Druckerverteilung, Failover mit Hinweis auf Druckserver und DC1 | Pflichtmodul setzte optionale Module voraus; GPO-Verteilung fehlte; Titel versprach mehr, als das Labor leistet |

**Hinweise und offene Punkte:**

* Alle neu ergänzten Befehle und Einstellungen wurden nur gegen den Wissensstand geprüft, **nicht im Labor ausgeführt**. Vor Kursstart zu prüfen: Wechselwirkung von FSRM-Kontingent und Dateiprüfung mit DFS-R (Modul 7), Hub-and-Spoke mit zwei Mitgliedern, Registerkarte „DFS“ und Menünamen der Offlinedateien, `dfsrdiag backlog`-Syntax, Verfügbarkeit von „Generic / Text Only“, Verhalten der Benutzerrichtlinie bei der Druckerbereitstellung (für die Computerrichtlinie ist zusätzlich `PushPrinterConnections.exe` nötig; nicht bestätigt).
* Im Labor gibt es nur einen Domänencontroller. Das DFS-Failover in Modul 12 funktioniert nur, solange `DC1` läuft; echte Hochverfügbarkeit des Namespace würde einen zweiten DC erfordern.
* Der Druckserver bleibt ein Single Point of Failure (kein Cluster im Lehrplan). Das ist in Modul 12 ausdrücklich dokumentiert.