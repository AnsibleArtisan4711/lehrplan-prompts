# Lehrplan: PC-Hardware und Fehlersuche

| Eigenschaft | Wert |
|---|---|
| **Zielgruppe** | Auszubildende, Quereinsteiger, angehende Systemtechniker und Systemadministratoren (Raum Österreich/EU) |
| **Vorkenntnisse** | Keine |
| **Gesamtumfang** | 8 Module, 42 UE (1 UE = 45 Minuten) |
| **Fokus-Technologien** | PC-Hardware, Windows 11, Linux Live-System (z. B. Ubuntu 24.04) |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit tiefergehender OS-Administration (z. B. Active Directory), Routing-Protokollen oder Enterprise-Server-Hardware (SAN/Blade-Server) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Grundlagen der PC-Architektur und Arbeitssicherheit | 1 | 5 |
| 2 | Hauptplatine, Firmware (BIOS/UEFI) und Schnittstellen | 1 | 6 |
| 3 | Prozessor (CPU), Arbeitsspeicher (RAM) und Kühlung | 1 | 5 |
| 4 | Massenspeicher und Dateisysteme | 1 | 6 |
| 5 | Erweiterungskarten (Netzwerk, Grafik) und Peripheriegeräte | 1 | 4 |
| 6 | Systematische Fehlersuche und Diagnosewerkzeuge | 1 | 6 |
| 7 | Systemwartung, Datensicherung und Wiederherstellung | 1 | 6 |
| 8 | Spezifische Fehlerbilder und Fallstudien | 2 | 4 |
| **Gesamt** | **8 Module (7x Prio 1, 1x Prio 2)** | | **42 UE** |

*Hinweis zur Priorisierung: Priorität 1 kennzeichnet verpflichtende Kernkompetenzen. Priorität 2 dient der Vertiefung und kann bei Zeitmangel gekürzt werden.*

### 2. Quellen

* **CompTIA A+ Certification Objectives** (Hardware und Fehlersuche), CompTIA, URL: https://www.comptia.org/certifications/a (nicht geprüft). Die Serie 220-1101/1102 von 2022 wurde laut einer Sekundärquelle (Professor Messer, „Differences between 220-1101 and 220-1201“, abgerufen am 08.11.2026, https://www.professormesser.com/free-a-plus-training/a-plus-articles/differences-between-220-1101-and-220-1201/) am 25.09.2025 durch 220-1201/1202 (veröffentlicht 25.03.2025) abgelöst. Der Lehrplan orientiert sich nur thematisch daran. Welche Fassung das hier verwendete Fehlersuche-Modell mit sechs Schritten enthält, ist nicht geprüft.
* **Windows-Clientdokumentation (Windows client management)**, Microsoft, Stand fortlaufend, https://learn.microsoft.com/de-de/windows/client-management/ (Titel und URL nicht geprüft)
* **Ubuntu Desktop Guide**, Canonical Ltd., Version 24.04, https://help.ubuntu.com/24.04/ubuntu-help/index.html (nicht geprüft)
* **Hyper-V generation 2 virtual machine security features** (Secure Boot, Vorlagen „Microsoft Windows“ und „Microsoft UEFI Certificate Authority“), Microsoft, abgerufen am 08.11.2026, https://learn.microsoft.com/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features
* **Should I create a generation 1 or 2 virtual machine in Hyper-V?**, Microsoft, abgerufen am 08.11.2026, https://learn.microsoft.com/windows-server/virtualization/hyper-v/plan/should-i-create-a-generation-1-or-2-virtual-machine-in-hyper-v
* **Windows 11 requirements** (TPM 2.0, UEFI, Secure Boot), Microsoft, Stand nicht geprüft, https://learn.microsoft.com/windows/whats-new/windows-11-requirements (nicht geprüft)
* **UEFI Specification**, UEFI Forum, Stand nicht geprüft, https://uefi.org/specifications (nicht geprüft)
* Hardware-Standards (ATX, PCI Express, USB, NVMe, SMART) und ESD-Normen (z. B. IEC 61340-5-1, ANSI/ESD S20.20): Keine geprüfte Quelle. Der Lehrplan nennt sie nur als Begriffe.
* Evaluationsmedien: Windows 11 Enterprise Evaluation (Microsoft Evaluation Center, https://www.microsoft.com/evalcenter/, nicht geprüft) und Ubuntu 24.04 LTS Desktop (https://ubuntu.com/download/desktop, nicht geprüft).
* Die URLs wurden bis auf die mit „abgerufen“ gekennzeichneten nicht abgerufen; die Verfügbarkeit ist vor Kursbeginn zu prüfen.

### 3. Labor-Setup & Rahmenbedingungen

Alle Praxisaufgaben werden in einer sicheren und teilweise isolierten Umgebung durchgeführt. Für diesen Kurs wird folgendes Setup benötigt:

* **Hardware / Altgeräte (erforderlich in Modul 1 und 2, ersatzweise Bildmaterial):** Mindestens ein ausgemusterter Desktop-PC mit geöffnetem Gehäuse (ohne Netzkabel, nie am Strom), ein ESD-Armband und ein Schraubendreher. Ist kein Altgerät verfügbar, stellt der Kursleiter Bildmaterial (beschriftete Fotos eines geöffneten PCs mit Netzteil, Mainboard, Laufwerken, CPU-Kühler, RAM und Anschlüssen) bereit; die Aufgaben in Modul 1 und 2 sind dann Bildanalysen. Die ESD-Übung in Modul 1 braucht Armband und Gehäuse.
* **Hyper-V Host:** Ein Arbeitsplatzrechner mit installiertem Hyper-V (Windows 10/11 Pro oder Enterprise) und genügend Arbeitsspeicher und Speicherplatz (mindestens 8 GB frei für eine laufende VM, mehrere GB für die ISO-Dateien). Die beiden VMs laufen nie gleichzeitig.
* **Virtueller Switch (erforderlich ab Modul 5):** Ein privater virtueller Switch (`vSwitch-Private`), der keine Verbindung zum physischen Heim- oder Produktivnetz hat. Der Netzwerkadapter von `WIN11-TEST` wird daran angeschlossen.
* **VM1: "WIN11-TEST" (erforderlich ab Modul 2):** Eine Hyper-V Gen2-VM mit 4 vCPUs, 4 GB RAM, 64 GB vHD, aktiviertem TPM und aktiviertem Secure Boot, Betriebssystem Windows 11 Enterprise Evaluation (ISO aus dem Microsoft Evaluation Center; der Download braucht Internet am Host, die VM selbst braucht keins). Der Kursleiter installiert Windows vor Kursbeginn und legt das lokale Administratorkonto `labadmin` an (Kennwort vom Kursleiter). Verlangt die Einrichtung ein Microsoft-Konto, erfolgt sie vor dem Anschluss an den privaten Switch mit vorübergehendem Internet. Nach der Installation wird der Hyper-V-Prüfpunkt `M2-Start` erstellt. Die Evaluation ist zeitlich begrenzt (nicht bestätigt: 90 Tage).
  * Konfiguration: 4 vCPUs, 4 GB RAM, 64 GB vHD, TPM aktiviert, Secure Boot aktiviert. 
  * OS: Windows 11 Enterprise Evaluation (kostenlose ISO von Microsoft).
* **VM2: "LINUX-LIVE" (erforderlich ab Modul 6):** Eine Hyper-V Gen2-VM ohne virtuelle Festplatte (2 vCPUs, 4 GB RAM), die in Modul 6 von den Lernenden angelegt und konfiguriert wird (Secure-Boot-Vorlage, DVD-Laufwerk mit ISO).
* **Linux Live-ISO (erforderlich ab Modul 6):** Ubuntu 24.04 LTS Desktop ISO. Die ISO muss vorab am Host heruntergeladen und abgelegt werden; die Prüfsumme wird nach Angabe von Canonical verglichen. Ein Internetzugang der VMs ist nicht erforderlich.
* **Vom Kursleiter bereitzustellen:** Altgerät oder Bildmaterial (Modul 1 und 2), Falldokumente zu den Fallstudien in Modul 8 und vorbereitete Prüfpunkte (`M2-Start` nach der Windows-Installation, `M7-Start` vor Modul 7).


## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen der PC-Architektur und Arbeitssicherheit
* **Priorität:** 1
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die grundlegenden Gefahren am Arbeitsplatz (ESD, Stromschlag) benennen und Schutzmaßnahmen anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende die primären Bausteine eines Personal Computers benennen und ihre grundlegende Funktion erklären.
* **Voraussetzungen:** Keine.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Arbeitssicherheit, ESD-Schutz (Elektrostatische Entladung) und Werkzeugkunde | 2 |
| 1.2 | Das EVA-Prinzip (Eingabe, Verarbeitung, Ausgabe) | 1 |
| 1.3 | Gehäusebauformen, Netzteile (ATX-Standard) und physischer Aufbau | 2 |
#### Praxisaufgaben (Hands-on Lab)
1. **Hardware-Identifikation:** Betrachte das Altgerät oder das bereitgestellte Bildmaterial. Identifiziere und dokumentiere (Foto oder Skizze mit Beschriftung) die Position von Netzteil, Mainboard, Laufwerken, CPU-Kühler und Arbeitsspeicher und nenne je Baustein seine Aufgabe.
2. **ESD-Schutzmaßnahmen anwenden:** Lege das ESD-Armband an und verbinde es mit dem stromlosen, vom Netz getrennten PC-Gehäuse. Beschreibe schriftlich die Schritte vor dem Öffnen eines Gehäuses (ausschalten, Netzkabel ziehen, Restladung abbauen) und erkläre, warum das Netzteil dabei nicht geöffnet wird.
#### Kontrollfragen
1. Welche Maßnahmen verhindern elektrostatische Entladungen (ESD) bei der Arbeit an PC-Komponenten?
2. Warum darf ein PC-Netzteil nicht von Personen ohne elektrotechnische Ausbildung geöffnet werden (Stichwort: gespeicherte Ladung in Kondensatoren)?
3. Wofür steht das EVA-Prinzip und welche Hardware-Komponenten repräsentieren jeweils das "E", das "V" und das "A"?

### Modul 2: Hauptplatine, Firmware (BIOS/UEFI) und Schnittstellen
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Unterschiede zwischen Legacy-BIOS und UEFI erklären.
  * Nach Abschluss dieses Moduls kann der Lernende grundlegende Systemkonfigurationen (Boot-Reihenfolge, Secure Boot) im UEFI einer Hyper-V VM konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende gängige externe und interne Schnittstellen (USB, PCIe, SATA) identifizieren.
* **Voraussetzungen:** Abgeschlossenes Modul 1. VM "WIN11-TEST" (ausgeschaltet, Prüfpunkt `M2-Start` vorhanden).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Formfaktoren (ATX, Micro-ATX, Mini-ITX) und Bussysteme (PCIe) | 2 |
| 2.2 | Interne und externe Schnittstellen (SATA, M.2, USB 3.x/4, USB-C) | 2 |
| 2.3 | Firmware: BIOS vs. UEFI, Secure Boot, TPM (Trusted Platform Module) | 2 |
#### Praxisaufgaben (Hands-on Lab)
1. **UEFI-Konfiguration in Hyper-V:** Öffne bei ausgeschalteter VM "WIN11-TEST" die Einstellungen und den Abschnitt "Sicherheit". Verifiziere, dass "Secure Boot" (Sicherer Start) mit der Vorlage "Microsoft Windows" und das "Trusted Platform Module" aktiviert sind. Deaktiviere Secure Boot testweise, speichere, aktiviere es wieder und speichere erneut. Notiere, wofür die Vorlage "Microsoft Windows" steht (für Windows-Betriebssysteme; für Linux gibt es eine andere Vorlage, siehe Modul 6).
2. **Boot-Reihenfolge anpassen:** Öffne im Bereich "Firmware" der VM-Einstellungen die Boot-Reihenfolge und notiere sie. Existiert kein virtuelles DVD-Laufwerk (am SCSI-Controller), füge eines ohne Image hinzu. Stelle das DVD-Laufwerk vor die Festplatte und notiere die neue Reihenfolge. Stelle danach die ursprüngliche Reihenfolge wieder her. Ein Start der VM ist für diese Aufgabe nicht nötig.
3. **Schnittstellen identifizieren:** Finde am Altgerät oder im Bildmaterial je einen Anschluss für SATA, M.2, PCIe, USB-A, USB-C und Netzwerk (RJ45), beschrifte sie und notiere die Verwendung.
#### Kontrollfragen
1. Nenne zwei technische Vorteile von UEFI gegenüber dem älteren Legacy-BIOS.
2. Was ist die Hauptfunktion eines TPM-Chips im Kontext moderner Betriebssysteme wie Windows 11?
3. Welche Bus-Architektur hat den AGP- und PCI-Standard abgelöst und wird primär für moderne Grafikkarten und schnelle NVMe-SSDs verwendet?
4. Erkläre den Unterschied zwischen dem physischen Stecker "USB-C" und dem Protokoll "USB 3.2".

### Modul 3: Prozessor (CPU), Arbeitsspeicher (RAM) und Kühlung
* **Priorität:** 1
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Architekturen von modernen CPUs (Kerne, Threads, Cache) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende RAM-Typen (DDR4, DDR5, SO-DIMM) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Hardwarespezifikationen mithilfe von Windows-Bordmitteln auslesen.
* **Voraussetzungen:** Abgeschlossenes Modul 2. Die VM "WIN11-TEST" ist gestartet (Windows ist vom Kursleiter installiert).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | CPU-Architekturen, Taktung, Cache (L1/L2/L3) und Multithreading | 2 |
| 3.2 | Arbeitsspeicher: Typen (DDR-Generationen), Bauformen (DIMM, SO-DIMM), ECC vs. Non-ECC | 1 |
| 3.3 | Kühlungskonzepte (Luft, passiv, AIO/Wasserkühlung) und Wärmeleitpaste | 1 |
| 3.4 | Hardware-Analyse im Betriebssystem | 1 |
#### Praxisaufgaben (Hands-on Lab)
1. **Systeminformationen auslesen:** Melde dich an der VM "WIN11-TEST" an. Öffne den Task-Manager (Strg+Shift+Esc), wechsle zum Tab "Leistung" und notiere die Anzahl der logischen Prozessoren, den zugewiesenen Arbeitsspeicher und die angezeigten Cache-Größen. In einer VM kann die Cache-Angabe fehlen (nicht bestätigt); notiere dann, was angezeigt wird.
2. **Detailanalyse mit msinfo32:** Öffne den Ausführen-Dialog (Win+R) und starte `msinfo32`. Finde und dokumentiere den "BIOS-Modus", den Status des sicheren Starts (Bezeichnung in der deutschen Oberfläche nicht bestätigt) und den genauen Prozessortyp. Vergleiche den Secure-Boot-Status mit der Einstellung aus Modul 2.
#### Kontrollfragen
1. Was ist der Unterschied zwischen physischen CPU-Kernen und logischen Prozessoren (Threads)?
2. Wofür wird ECC-RAM verwendet und warum kommt er selten in Standard-Heim-PCs zum Einsatz?
3. Warum ist das korrekte Auftragen von Wärmeleitpaste zwischen CPU und Kühlkörper zwingend erforderlich?
4. Worin unterscheiden sich DDR4 und DDR5 (z. B. Steckplatz, Kompatibilität) und wofür wird die Bauform SO-DIMM verwendet?

### Modul 4: Massenspeicher und Dateisysteme
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsweisen von HDD, SATA-SSD und NVMe-SSD unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Datenträger partitionieren und mit einem Dateisystem formatieren.
  * Nach Abschluss dieses Moduls kann der Lernende den Zustand von Speicherlaufwerken beurteilen (SMART-Werte in der Theorie).
* **Voraussetzungen:** Abgeschlossenes Modul 3. Zugriff auf "WIN11-TEST".
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Speichertechnologien: HDD (magnetisch) vs. SSD (NAND-Flash); Zustandsbeurteilung mit SMART (Theorie) | 2 |
| 4.2 | Logische Struktur: MBR vs. GPT, Partitionen und Volumes | 2 |
| 4.3 | Dateisysteme: NTFS, exFAT, FAT32 im Windows-Umfeld | 2 |
#### Praxisaufgaben (Hands-on Lab)
1. **Virtuelle Festplatte hinzufügen:** Fahre die VM "WIN11-TEST" herunter. Füge in den Einstellungen am SCSI-Controller eine neue virtuelle Festplatte hinzu (Neu > VHDX > dynamisch erweiterbar, 10 GB, Name `DatenTest.vhdx`). Starte die VM neu.
2. **Datenträgerverwaltung:** Öffne `diskmgmt.msc` in Windows. Initialisiere den neuen Datenträger als GPT (GUID Partition Table).
3. **Partitionierung und Formatierung:** Erstelle auf dem neuen Datenträger ein neues "Einfaches Volume", weise den Laufwerksbuchstaben "Z:" zu und formatiere es als NTFS (Schnellformatierung) mit der Bezeichnung "Daten-Test". (Hinweis: Dieses Laufwerk wird für Modul 7 benötigt und darf vorerst nicht gelöscht werden).
#### Kontrollfragen
1. Warum sollte ein modernes Betriebssystem auf einer NVMe-SSD statt auf einer HDD installiert werden?
2. Welche technischen Grenzen hat der MBR (Master Boot Record) im Vergleich zu GPT (GUID Partition Table)?
3. Welches Dateisystem würdest du wählen, wenn ein USB-Stick große Dateien (>4GB) speichern soll und auf Windows sowie macOS lesbar sein muss?
4. Welche Aufgabe hat SMART bei einem Laufwerk, und welche Hinweise (z. B. wachsende Zahl neu zugewiesener Sektoren) deuten auf einen drohenden Ausfall hin?

### Modul 5: Erweiterungskarten (Netzwerk, Grafik) und Peripheriegeräte
* **Priorität:** 1
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle von GPUs und NICs im System beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Treiber in Windows verwalten (Treiberdaten prüfen, Geräte deaktivieren und aktivieren) und das Aktualisieren sowie den Rollback eines Treibers erklären.
* **Voraussetzungen:** Abgeschlossenes Modul 4. Zugriff auf "WIN11-TEST".
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Grafikkarten (Onboard vs. dediziert) und Video-Schnittstellen (HDMI, DP) | 1 |
| 5.2 | Netzwerkkarten (NIC, WLAN-Module, Bluetooth) | 1 |
| 5.3 | Peripherie und Drucker (Laserdrucker-Prozess, Tintenstrahl) | 1 |
| 5.4 | Treiberverwaltung und Gerätemanager in Windows | 1 |
#### Praxisaufgaben (Hands-on Lab)
1. **Gerätemanager-Analyse:** Öffne in "WIN11-TEST" den Gerätemanager (`devmgmt.msc`). Navigiere zur Kategorie "Netzwerkadapter".
2. **Treiber-Verwaltung:** Öffne die Eigenschaften des Netzwerkadapters (in Hyper-V-Gästen üblicherweise "Microsoft Hyper-V Network Adapter", Bezeichnung nicht bestätigt). Notiere auf der Registerkarte "Treiber" Anbieter, Datum und Version und prüfe, ob "Vorheriger Treiber" auswählbar ist (erwartet: nicht auswählbar, da der Treiber nie aktualisiert wurde; nicht bestätigt). Deaktiviere das Gerät testweise, notiere die Warnmeldung und den Netzwerkstatus in der Taskleiste und aktiviere das Gerät wieder. Beschreibe schriftlich, wie ein Treiber ohne Internet aus einer Liste oder von einem Datenträger aktualisiert würde.
#### Kontrollfragen
1. Erkläre den Unterschied zwischen einem integrierten Grafikprozessor (IGP) und einer dedizierten Grafikkarte.
2. Beschreibe den Ablauf des Laserdruckprozesses (Aufladen der Bildtrommel, Belichten, Entwickeln, Übertragen, Fixieren, Reinigen).
3. Was ist die Funktion eines Gerätetreibers im Betriebssystem?
4. Was bewirkt die Funktion "Vorheriger Treiber" (Rollback) im Windows-Gerätemanager?
5. Welche Aufgabe hat eine Netzwerkkarte (NIC), und was ist eine MAC-Adresse?

### Modul 6: Systematische Fehlersuche und Diagnosewerkzeuge
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Fehlersuche nach strukturierten Modellen (z. B. CompTIA Troubleshooting-Modell) durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Linux-Live-System booten, um Hardwareinformationen unabhängig vom installierten Windows auszulesen, und den Einsatz bei nicht startendem Windows erklären.
* **Voraussetzungen:** Abgeschlossenes Modul 5. Die Ubuntu-ISO liegt auf dem Hyper-V-Host; die VM "LINUX-LIVE" wird in Aufgabe 3 angelegt.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Methodik der Fehlersuche (Identifikation, Theorie, Test, Plan, Verifikation, Dokumentation) | 2 |
| 6.2 | POST (Power-On Self-Test), Beep-Codes und Diagnose-LEDs | 1 |
| 6.3 | Windows-Diagnose (Ereignisanzeige, Zuverlässigkeitsverlauf) | 1 |
| 6.4 | Live-Systeme zur Hardware-Diagnose (Linux) | 2 |
#### Praxisaufgaben (Hands-on Lab)
1. **Ereignisanzeige und Zuverlässigkeitsverlauf (Windows):** Melde dich an "WIN11-TEST" an, öffne `eventvwr.msc`, navigiere zu "Windows-Protokolle" > "System" und filtere nach Fehlern der letzten 7 Tage (gibt es keine, nimm Warnungen). Notiere gefundene Event-IDs. Öffne den Zuverlässigkeitsverlauf mit `perfmon /rel` und notiere, was er anzeigt.
2. **Fehlersuche-Modell anwenden:** Ein Anwender meldet: "Der PC startet, aber der Bildschirm bleibt nach dem Windows-Logo schwarz." Dokumentiere das Vorgehen in den sechs Schritten Identifikation, Theorie, Test, Plan, Verifikation, Dokumentation, jeweils mit zwei Sätzen. Nenne mindestens zwei mögliche Ursachen und wie du sie testest.
3. **Live-System booten:** Lege in Hyper-V die VM "LINUX-LIVE" an (Generation 2, 2 vCPUs, 4 GB RAM, ohne virtuelle Festplatte). Stelle in den Einstellungen unter "Sicherheit" die Secure-Boot-Vorlage "Microsoft UEFI Certificate Authority" ein (Microsoft gibt diese Vorlage für Linux-Distributionen an). Füge am SCSI-Controller ein DVD-Laufwerk mit der Ubuntu-ISO hinzu und setze es in der Boot-Reihenfolge an die erste Stelle. Starte die VM und wähle "Try Ubuntu" (ohne Installation). Optional: Teste vorher die Vorlage "Microsoft Windows" und dokumentiere das Ergebnis.
4. **Linux-Diagnosebefehle:** Öffne im Ubuntu-Desktop ein Terminal. Führe `lsblk` (Laufwerke; hier nur das ISO-Laufwerk), `lscpu`, `free -h` und `sudo dmesg | less` aus (Beenden mit "q"; ohne `sudo` kann Ubuntu den Zugriff auf die Kernel-Meldungen verweigern, nicht bestätigt). Notiere, welche Hardware angezeigt wird.
5. **Rückbau:** Fahre die VM "LINUX-LIVE" geordnet herunter und trenne die ISO.
#### Kontrollfragen
1. Nenne die 6 Schritte des systematischen Troubleshooting-Prozesses nach CompTIA.
2. Warum ist ein Linux-Live-System ein wertvolles Werkzeug, wenn der PC nicht mehr in Windows bootet?
3. Was bedeutet der Begriff "POST" und wann wird dieser durchgeführt?
4. Warum startet das Ubuntu-ISO in einer Generation-2-VM mit der Secure-Boot-Vorlage "Microsoft Windows" nicht, mit der Vorlage "Microsoft UEFI Certificate Authority" aber schon?

### Modul 7: Systemwartung, Datensicherung und Wiederherstellung
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Strategien zur Datensicherung (3-2-1-Regel) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen Windows-Wiederherstellungspunkt erstellen und anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende logische Fehler in Dateisystemen beheben.
* **Voraussetzungen:** Abgeschlossenes Modul 4 (Laufwerk Z: "Daten-Test" muss in der VM "WIN11-TEST" existieren). Erstelle vorab den Hyper-V-Prüfpunkt `M7-Start`.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Backup-Strategien (Voll, Differentiell, Inkrementell) und die 3-2-1-Regel | 2 |
| 7.2 | Laufwerkswartung: CHKDSK, Defragmentierung vs. TRIM für SSDs | 2 |
| 7.3 | Systemwiederherstellung und Wiederherstellungslaufwerke in Windows | 2 |
#### Praxisaufgaben (Hands-on Lab)
1. **Wiederherstellungspunkt erstellen:** Aktiviere in "WIN11-TEST" unter `sysdm.cpl` > "Computerschutz" den Systemschutz für Laufwerk C: (ist er deaktiviert, lässt sich kein Punkt erstellen). Lege zuvor eine Umgebungsvariable `LAB_TEST=1` an (Systemeigenschaften > Umgebungsvariablen), erstelle dann einen Wiederherstellungspunkt mit dem Namen "Vor-Wartung" und ändere danach den Wert der Variablen auf `2`.
2. **Wiederherstellung anwenden:** Starte `rstrui.exe`, wähle den Punkt "Vor-Wartung", lasse mit "Nach betroffenen Programmen suchen" prüfen und führe die Wiederherstellung durch (die VM startet neu). Prüfe nach dem Neustart den Wert von `LAB_TEST` und dokumentiere das Ergebnis (Verhalten bei Umgebungsvariablen nicht bestätigt).
3. **Datensicherung mit robocopy:** Lege `C:\Daten` mit drei Textdateien an und sichere sie mit `robocopy C:\Daten Z:\Sicherung /E`. Ändere eine Datei und füge eine hinzu, wiederhole den Befehl und notiere, welche Dateien kopiert wurden. Lösche eine Datei in `C:\Daten` und stelle sie mit `robocopy Z:\Sicherung C:\Daten /E` wieder her. Ordne das Verfahren den Begriffen Voll-, differentielle und inkrementelle Sicherung zu.
4. **Dateisystemprüfung:** Öffne eine administrative Eingabeaufforderung. Markiere das Laufwerk testweise als fehlerhaft (`fsutil dirty set Z:`), prüfe mit `fsutil dirty query Z:` und `chkdsk Z:` (nur lesen) und repariere mit `chkdsk Z: /f`. Prüfe danach erneut mit `fsutil dirty query Z:`. Die Markierung simuliert einen logischen Fehler; das Laufwerk enthält keine wichtigen Daten.
5. **Rückbau (Bereinigung):** Öffne die Datenträgerverwaltung, lösche das Volume "Daten-Test" (Laufwerk Z:) und fahre die VM herunter. Entferne die virtuelle 10-GB-Festplatte in den Einstellungen der VM und lösche die Datei `DatenTest.vhdx` auf dem Host.
#### Kontrollfragen
1. Erkläre die 3-2-1-Regel für Backups.
2. Warum sollte eine SSD nicht klassisch defragmentiert werden (Verschleiß, kein Geschwindigkeitsvorteil), und welche Aufgabe hat stattdessen der TRIM-Befehl?
3. Was ist der Unterschied zwischen einem inkrementellen und einem differentiellen Backup?

### Modul 8: Spezifische Fehlerbilder und Fallstudien
* **Priorität:** 2
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende spezifische Fehlerbilder (z. B. BSOD, Überhitzung, Netzteildefekt) systematisch analysieren und theoretische Lösungswege ableiten.
* **Voraussetzungen:** Abgeschlossene Module 1 bis 7.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Fallstudie 1: System startet nicht (Kein Strom / POST-Fehler) | 1 |
| 8.2 | Fallstudie 2: Unerwartete Neustarts und Blue Screens of Death (BSOD) | 1 |
| 8.3 | Fallstudie 3: Langsame Performance und thermisches Drosseln (Thermal Throttling) | 1 |
| 8.4 | Fallstudie 4: Peripheriegeräte werden nicht erkannt | 1 |
#### Praxisaufgaben (Hands-on Lab)
*Hinweis: Dieses Modul beinhaltet kein technisches Labor. Die Praxisaufgaben bestehen aus strukturierten Falldiskussionen.*
1. **BSOD-Analyse:** Gegeben ist ein Fall, bei dem ein Windows-PC unregelmäßig mit dem Fehler "IRQL_NOT_LESS_OR_EQUAL" abstürzt. Erstelle ein schriftliches Kurzkonzept (max. 1 Seite) mit den nächsten vier Untersuchungsschritten (z. B. RAM-Diagnose, Treiberprüfung).
2. **Thermisches Problem:** Ein PC schaltet sich bei hoher Last (z.B. nach 10 Minuten Rendering) ab. Definiere die Schritte zur Überprüfung von Lüftern, Luftstrom und Wärmeleitpaste.
3. **Fallstudie "System startet nicht":** Erstelle einen Entscheidungsbaum (höchstens acht Knoten) für einen PC ohne Lüfter und LEDs, vom Netzkabel bis zum Austausch des Netzteils.
4. **Fallstudie "Peripherie wird nicht erkannt":** Erstelle eine Checkliste mit sechs Prüfungen in sinnvoller Reihenfolge für ein USB-Headset, das nicht erkannt wird (Kabel und Anschluss, anderer Port, Gerätemanager, Treiber, anderes Gerät, Energieeinstellungen).
#### Kontrollfragen
1. Welche typischen Hardwaredefekte verursachen zufällige Neustarts ohne Warnmeldung?
2. Was ist Thermal Throttling und wie schützt es die CPU?
3. Wo würdest du bei einem komplett "toten" PC (keine Lüfter, keine LEDs) als erstes mit der Fehlersuche beginnen?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (42 UE), Prioritäten (7x P1, 1x P2) und Module blieben unverändert. Aufgaben kamen hinzu; ob die Stunden dafür reichen, ist unerprobt (besonders Modul 6 und 7). Die Aufgaben mit Hyper-V und Windows wurden nicht ausgeführt, sondern nur gegen Microsoft Learn und den Wissensstand geprüft.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| A.2 | CompTIA-Quelle ersetzt (Serie 220-1101 am 25.09.2025 abgelöst), Hyper-V-, Windows-11- und UEFI-Quellen, Hardware-Standards als „keine geprüfte Quelle“; der Satz „Alle URLs wurden auf Struktur geprüft“ entfernt | Die Quelle war veraltet; der Satz widersprach der Verifikationsregel; USB, PCIe, NVMe, ATX, UEFI, TPM, SMART und ESD hatten keine Quelle |
| A.3 | Altgerät/Bildmaterial als erforderlich, Windows-Installation durch den Kursleiter mit Konto `labadmin`, Prüfpunkte, Anschluss des Adapters am Switch, VM `LINUX-LIVE` mit Daten, Material des Kursleiters | Die Windows-Installation war nirgends geplant (Modul 3 setzte sie voraus); das Altgerät war „optional“, obwohl Aufgaben es brauchten |
| Modul 1 | Aufgaben 1 und 2 präzisiert, Frage 2 | Stromschlag-Schutz im Lernziel hatte keine Aufgabe; „nicht-zertifiziertes Personal“ war unklar |
| Modul 2 | Aufgabe 1 (Secure Boot aus und ein), Aufgabe 2 mit Rückbau, Aufgabe 3 (Schnittstellen) | Ein virtuelles DVD-Laufwerk existiert in Generation-2-VMs nicht von selbst; die DVD-Reihenfolge sollte „für spätere Module“ bleiben, wurde aber nie gebraucht; das Lernziel „Schnittstellen identifizieren“ hatte keine Aufgabe |
| Modul 3 | Einheit 3.2 (SO-DIMM), Aufgaben 1 und 2, Frage 4 | SO-DIMM und DDR-Typen im Lernziel hatten keine Frage; in VMs fehlt die Cache-Angabe häufig |
| Modul 4 | Einheit 4.1 (SMART), Aufgabe 1 (VHDX anlegen), Frage 4 | SMART im Lernziel kam in keiner Einheit, Aufgabe oder Frage vor; die Anlage der virtuellen Festplatte war nicht beschrieben |
| Modul 5 | Lernziel 2, Aufgabe 2, Fragen 2 und 5 | Der Name „Hyper-V Virtual Ethernet Adapter“ ist der Adapter des Hosts; im Gast heißt der Adapter üblicherweise „Microsoft Hyper-V Network Adapter“. Aktualisieren und Rollback wurden nie geübt und sind ohne Internet nicht sinnvoll machbar, das Lernziel wurde auf „erklären“ gesenkt. „Vier Hauptschritte“ beim Laserdruck ist nicht belegt |
| Modul 6 | Lernziel 2, Aufgaben 1 bis 5, Frage 4 | Das Fehlersuche-Modell wurde nie angewendet; mit der Standard-Vorlage „Microsoft Windows“ bootet das Ubuntu-ISO in einer Generation-2-VM nicht (Microsoft nennt für Linux die Vorlage „Microsoft UEFI Certificate Authority“); eine VM ohne Festplatte kann keine „Hardware-Diagnose unabhängig vom OS“ zeigen, daher wurde das Lernziel angepasst; `dmesg` braucht unter Ubuntu ggf. `sudo`; der Zuverlässigkeitsverlauf aus Einheit 6.3 wurde nie benutzt |
| Modul 7 | Aufgaben 1 bis 5, Prüfpunkt, Frage 2 | Der Wiederherstellungspunkt wurde nur erstellt, nicht angewendet; Systemschutz ist ggf. deaktiviert; „Datensicherung“ im Titel hatte keine Aufgabe; „logische Fehler beheben“ ist auf einem sauberen Laufwerk mit `chkdsk` nicht zu zeigen; „niemals defragmentieren“ war zu absolut |
| Modul 8 | Aufgaben 3 und 4, Frage 1 | Zwei der vier Fallstudien hatten keine Aufgabe; Tippfehler „Hardwarededekte“ |

**Bewertung des Prüfvermerks der ersten Fassung:** Punkt 1 ist korrekt. Punkt 2 ist nicht erfüllt: Die Installation von Windows war nirgends geplant, und das Altgerät war optional. Punkt 3 ist nicht erfüllt: Die CompTIA-Fassung war abgelöst, die Standards hatten keine Quelle, und die Aussage „URLs auf Struktur geprüft“ ist keine Prüfung. Punkt 4 ist teilweise erfüllt (DVD-Reihenfolge, Secure-Boot-Vorlage). Punkt 5 ist nicht erfüllt (SMART, Schnittstellen, Treiber-Update, Wiederherstellung anwenden, Fehlersuche-Modell, Fallstudien). Punkt 6 ist teilweise erfüllt (Boot-Reihenfolge wurde nie zurückgesetzt). Punkt 8 ist teilweise erfüllt (Windows-Beschaffung, Namen des Adapters). Punkt 9 ist erfüllt, aber ohne Prüfpunkt vor dem Löschen. Punkt 7 ist erfüllt.

**Hinweise und offene Punkte:**

* **Nicht bestätigt, vor Kursstart prüfen:** Bezeichnung des Adapters im Gast; Bezeichnung des Secure-Boot-Status in `msinfo32`; ob `dmesg` ohne `sudo` gesperrt ist; Verhalten von Umgebungsvariablen bei der Systemwiederherstellung; Laufzeit der Evaluation (90 Tage); Anzeige der Cache-Größen im Task-Manager einer VM; die Namen der Menüs in der deutschen Oberfläche; welche CompTIA-Fassung die sechs Schritte der Fehlersuche enthält.
* Die Aufgaben mit einem Altgerät setzen ein Gehäuse ohne Netzkabel voraus. Arbeiten am Netzteil sind ausgeschlossen.