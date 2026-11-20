# Lehrplan: VMware vSphere und ESXi

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Grundlagen der Virtualisierung, Netzwerk- und Speicherkenntnisse |
| **Gesamtumfang** | 13 Module, 106 UE (zu 45 Minuten; 79,5 Stunden) |
| **Fokus-Technologien** | VMware ESXi 8 (kostenloser Hypervisor, Host Client), VMs, vSwitch, Datastores; vCenter-Funktionen als Konzept |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Hyper-V im Kurs „Hyper-V“, Proxmox VE im Kurs „Proxmox VE“. Nicht behandelt: vSAN, NSX, Lizenz- und Vertragsfragen im Detail, Betrieb großer vCenter-Umgebungen |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Architektur, Produktfamilie und die Grenzen des kostenlosen ESXi | 1 | 8 |
| 2 | Installation und Host Client | 1 | 8 |
| 3 | Virtuelle Maschinen und die .vmx-Datei | 1 | 9 |
| 4 | Virtuelle Platten und das VMDK-Format | 1 | 8 |
| 5 | Datastores und Kapazitätsplanung | 1 | 8 |
| 6 | Netzwerk: vSwitch, Portgruppen und VLANs | 1 | 9 |
| 7 | Ressourcenverwaltung: Shares, Reservierungen und Limits | 1 | 8 |
| 8 | Snapshots und Klone | 1 | 7 |
| 9 | Sicherung und Export ohne Sicherungsschnittstelle | 1 | 8 |
| 10 | vCenter, Hochverfügbarkeit und Lastverteilung als Konzept | 1 | 9 |
| 11 | Benutzer, Rollen und Protokolle | 1 | 7 |
| 12 | Automatisierung mit PowerCLI | 2 | 7 |
| 13 | Fehlersuche und Abschluss | 1 | 10 |
| **Gesamt** | 13 Module | 12 × Priorität 1, 1 × Priorität 2 | **106** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 12 (Automatisierung mit PowerCLI). Fällt Modul 12 weg, verringert sich der Gesamtumfang auf 99 UE; kein Pflichtmodul setzt es voraus.

### 2. Quellen

**Gelesen (mit Abrufdatum 20.11.2026):** (1) Broadcom-Wissensartikel **KB 399823** „VMware ESXi 8.0 Update 3e now available as a Free Hypervisor“: Download über das Broadcom Support Portal (Free Software Downloads, Suche „VMware vSphere Hypervisor“); Grenzen: höchstens 2 physische CPUs je Host und 8 vCPUs je VM; kein vCenter; kein vMotion, DRS, HA; keine Sicherung über die VADP-Schnittstelle; Verwaltung nur über den Host Client; API nur lesend bzw. eingeschränkt; kein offizieller Support; die Lizenz ist eingebettet. Die Seite nennt **kein Datum**; Angaben können sich ändern. (2) Bericht von **Techzine** vom 14. April 2025: Der kostenlose ESXi war im Februar 2024 eingestellt worden und kehrte mit 8.0 Update 3 zurück; Registrierung nötig; berichtet wird, dass er in Desktop-Hypervisoren nicht laufe (nicht geprüft); Angaben zu geänderten Mindestkernzahlen bei Lizenzen (72 auf 16 genannt) sind **nicht bestätigt** und werden hier nicht verwendet.

**Nicht gelesen:** alle weiteren Herstellerdokumente (Hardware-Versionen, vSwitch, VMFS, Snapshots, HA/DRS, Rollen, PowerCLI, esxcli). Diese Inhalte stammen aus Fachwissen und sind **nicht bestätigt**; insbesondere Schlüssel der `.vmx`-Dateien, Rollennamen und PowerCLI-Befehle. Es wurde **weder ESXi noch vCenter noch PowerShell** ausgeführt. Die Beispieldaten sind **frei erfunden**. Verfügbarkeit, Lizenzbedingungen und Funktionsumfang des kostenlosen ESXi können sich ändern; vor Einsatz beim Hersteller prüfen.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor-Ebene:** Für ESXi wird ein eigenes physisches Gerät mit zwei freien CPU-Kernen, ausreichend RAM und ESXi-geeigneter Hardware empfohlen (Richtwert: 2 Kerne, 8 GB, 40 GB; **nicht** aus Herstellerdokumentation). **ESXi als verschachtelte VM unter Hyper-V ist nicht bestätigt**; Techzine berichtet, der kostenlose ESXi laufe in Desktop-Hypervisoren nicht. Das Labor ist daher als „eigener Rechner oder anderer Unterbau“ beschrieben.

**Netz:** privater Switch bzw. isoliertes Netz `10.7.0.0/24`; `esx1` (`10.7.0.11`), optional `esx2`, `esx3` für Konzeptübungen (Cluster nur mit vCenter und passender Lizenz; im Kurs nur als Modell). Test-VMs: ein Linux mit wenigen hundert MB RAM.

**Skripte:** Die Beispielskripte liefen in einem Cloud-Container (Ubuntu 24.04) mit `qemu-img` und Python 3, **ohne** ESXi, **ohne** vCenter, **ohne** PowerShell. Sie bilden Konzepte nach (VMDK-Formate, Differenzabbilder, Kapazitäts- und Ressourcenrechnung, Modelle); es sind **keine** VMware-Befehle.

## B. Detaillierter Modulaufbau

### Modul 1: Architektur, Produktfamilie und die Grenzen des kostenlosen ESXi

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Bausteine von vSphere beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen des kostenlosen ESXi nennen und deren Stand kennzeichnen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Plan gegen diese Grenzen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Plattformwahl begründen.
* **Voraussetzungen:** Grundlagen der Virtualisierung.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Bausteine: ESXi, vCenter, Host Client, vSphere Client, Datastore, vSwitch | 2 |
| 1.2 | Der kostenlose ESXi: Bezug, Grenzen und Unsicherheiten (Stand 20.11.2026) | 2 |
| 1.3 | Praxis: einen Laborplan gegen die Grenzen prüfen (`gratis_grenzen_pruefen.py`) | 2 |
| 1.4 | Alternativen und Entscheidung: wann ESXi, wann Hyper-V oder Proxmox VE | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bausteine zuordnen (Einheit 1.1):** Zeichnen Sie ein Schema mit ESXi-Host, Host Client, vCenter, Datastore und virtuellem Switch und beschriften Sie, was davon beim kostenlosen ESXi fehlt.
2. **Grenzen sammeln (Einheit 1.2):** Listen Sie die Grenzen des kostenlosen ESXi auf (CPUs, vCPUs, vCenter, vMotion/DRS/HA, Sicherung, API, Support) und vermerken Sie Quelle, Abrufdatum und die Unsicherheit (die Seite nennt kein Datum).
3. **Plan prüfen (Einheit 1.3):** Führen Sie `bash lauf.sh` aus und erklären Sie für „Cluster-Wunsch“ und „Backup-Wunsch“, was nicht möglich wäre und welche Alternative es gäbe.
4. **Plattform wählen (Einheit 1.4):** Wählen Sie für ein Zwei-Server-Labor mit Hochverfügbarkeits-Wunsch zwischen ESXi (kostenlos), Hyper-V und Proxmox VE und begründen Sie die Wahl in fünf Sätzen. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Warum ist ein Host Client kein Ersatz für vCenter?
2. Warum sollte man bei Angaben zum kostenlosen ESXi immer das Abrufdatum nennen?
3. Welche Funktion fehlt dem kostenlosen ESXi laut gelesener Quelle für die Sicherung über Standard-Schnittstellen?

### Modul 2: Installation und Host Client

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für eine Installation beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende Rechnerwerte gegen eigene Richtwerte prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Erstkonfiguration beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Host Client nutzen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Hardware-Voraussetzungen und Kompatibilität; Registrierung und Download | 2 |
| 2.2 | Praxis: Voraussetzungen des Rechners prüfen (`voraussetzungen_pruefen.sh`) | 2 |
| 2.3 | Installation und erste Konfiguration: Konsole (DCUI), Netzwerk, Kennwort, Zeit | 2 |
| 2.4 | Host Client: Aufbau, wichtige Ansichten, Wartungsmodus | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Voraussetzungen sammeln (Einheit 2.1):** Listen Sie auf, was Sie vor der Installation klären müssen (Kompatibilität der Hardware, Registrierung, Download-Quelle, Netzwerkdaten) und kennzeichnen Sie, was nicht aus der Herstellerdokumentation stammt.
2. **Rechner prüfen (Einheit 2.2):** Führen Sie `bash voraussetzungen_pruefen.sh` aus und erklären Sie die Auswertung. Warum sagt ein Erfolg nichts über die Lauffähigkeit von ESXi?
3. **Erstkonfiguration (Einheit 2.3):** Beschreiben Sie die Schritte der Erstkonfiguration in der Konsole (Kennwort, feste IP, DNS, Hostname, Zeit) und warum sie vor dem ersten VM-Betrieb erfolgen.
4. **Host Client erkunden (Einheit 2.4):** Beschreiben Sie, wo im Host Client Sie VMs, Datastores, Netzwerke und Protokolle finden, und wann Sie den Wartungsmodus einsetzen.

#### Kontrollfragen

1. Warum ist die Kompatibilität der Hardware vor der Installation wichtig?
2. Wozu dient eine feste IP am Host?
3. Wozu dient der Wartungsmodus?

### Modul 3: Virtuelle Maschinen und die .vmx-Datei

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine VM sinnvoll dimensionieren.
  * Nach Abschluss dieses Moduls kann der Lernende Gerätetypen einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine .vmx-Datei lesen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Betriebsabläufe beschreiben.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | VM anlegen: Gastbetriebssystem, CPU, Speicher, Platte, Netzwerk | 2 |
| 3.2 | Gerätetypen: vmxnet3, pvscsi, Hardware-Version, VMware Tools | 2 |
| 3.3 | Praxis: Konfigurationsdatei lesen und prüfen (`vmx_pruefen.py`) | 3 |
| 3.4 | Betrieb: Start, Stopp, Konsole, Ressourcenbedarf | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dimensionierung (Einheit 3.1):** Legen Sie für einen Webserver und einen Datenbankserver je vCPUs, Speicher und Platte fest und begründen Sie die Werte; beachten Sie die Grenze von 8 vCPUs je VM beim kostenlosen ESXi.
2. **Gerätetypen (Einheit 3.2):** Erklären Sie, wofür vmxnet3, pvscsi und die VMware Tools dienen, und kennzeichnen Sie die Angaben als Fachwissen.
3. **Konfiguration prüfen (Einheit 3.3):** Führen Sie `bash lauf.sh` aus (prüft `web01.vmx` und `alt01.vmx`) und beschreiben Sie jede Zeile von `web01.vmx` sowie jeden Hinweis zu `alt01.vmx` mit Behebung.
4. **Betrieb (Einheit 3.4):** Beschreiben Sie, wie Sie eine VM sauber herunterfahren und wann Sie den harten Stopp verwenden.

#### Kontrollfragen

1. Wozu dient die Datei mit der Endung .vmx?
2. Warum werden paravirtuelle Gerätetypen empfohlen?
3. Was ändert sich, wenn die Hardware-Version einer VM höher ist?

### Modul 4: Virtuelle Platten und das VMDK-Format

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau von VMDK-Platten erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Untertypen praktisch vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende dünn und dick zugeteilte Platten bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende Platten zwischen Formaten umwandeln und prüfen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | VMDK-Grundlagen: Beschreibung, Daten, Untertypen | 2 |
| 4.2 | Praxis: Untertypen erzeugen und vergleichen (`vmdk_demo.sh`) | 2 |
| 4.3 | Dünn und dick zugeteilte Platten: Platz, Leistung, Risiko | 2 |
| 4.4 | Umwandlung und Austausch mit anderen Hypervisoren | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **VMDK erklären (Einheit 4.1):** Erklären Sie, was Beschreibungsdatei und Datendatei einer VMDK sind und wozu es mehrere Untertypen gibt (Fachwissen, nicht bestätigt).
2. **Untertypen vergleichen (Einheit 4.2):** Führen Sie `bash vmdk_demo.sh` aus und erklären Sie die belegten Größen von monolithicSparse, monolithicFlat und streamOptimized.
3. **Dünn oder dick (Einheit 4.3):** Stellen Sie Vor- und Nachteile von dünn und dick zugeteilten Platten gegenüber (Platz, Leistung, Risiko eines vollen Datastores).
4. **Umwandlung (Einheit 4.4):** Beschreiben Sie, wie Sie eine VMDK in ein anderes Format wandeln und prüfen, dass der Inhalt gleich bleibt (Schritte 3 und 4 des Skripts).

#### Kontrollfragen

1. Warum belegt eine dünn zugeteilte Platte anfangs wenig Platz?
2. Welches Risiko entsteht bei Überbuchung dünn zugeteilter Platten?
3. Wozu dient der Vergleich nach der Umwandlung?

### Modul 5: Datastores und Kapazitätsplanung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Datastore-Arten unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Zuteilung und Belegung auseinanderhalten.
  * Nach Abschluss dieses Moduls kann der Lernende Schwellenwerte festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Speicherplan begründen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Datastore-Arten: VMFS, NFS; lokal und gemeinsam | 2 |
| 5.2 | Praxis: Kapazität mit Überbuchung rechnen (`datastore_rechner.py`) | 2 |
| 5.3 | Schwellenwerte, Überwachung und Wachstum | 2 |
| 5.4 | Speicherplanung: Leistung, Ausfallsicherheit, Sicherung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Arten vergleichen (Einheit 5.1):** Erstellen Sie eine Tabelle mit VMFS und NFS (Aufbau, gemeinsam nutzbar, Besonderheiten) und kennzeichnen Sie sie als Fachwissen.
2. **Kapazität rechnen (Einheit 5.2):** Führen Sie `bash lauf.sh` aus. Erklären Sie Zuteilung, Belegung und Überbuchung in der Ausgabe und das Ergebnis der Wachstumsrechnung.
3. **Schwellen (Einheit 5.3):** Legen Sie Schwellenwerte (Warnung, Alarm) für die Belegung fest und beschreiben Sie, wer was unternimmt.
4. **Speicherplan (Einheit 5.4):** Entwerfen Sie einen Speicherplan für `esx1`: Datastores, Zweck, Platzbedarf, Sicherung. Begründen Sie die Wahl.

#### Kontrollfragen

1. Warum ist Überbuchung bei dünnen Platten riskant?
2. Wozu dienen Schwellenwerte?
3. Warum sollte die Sicherung nicht auf demselben Datastore liegen wie die VM?

### Modul 6: Netzwerk: vSwitch, Portgruppen und VLANs

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines Standard-vSwitch erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Portgruppen und VLAN-IDs prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Netzkonzept entwerfen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Standard-vSwitch, Uplinks, Portgruppen und VMkernel-Adapter | 2 |
| 6.2 | Praxis: Konfiguration auf Fehler prüfen (`portgruppen_pruefen.py`) | 3 |
| 6.3 | VLANs: ID-Bereich, Zuordnung an Portgruppen | 2 |
| 6.4 | Planung: Management-, VM- und Speichernetz trennen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbau zeichnen (Einheit 6.1):** Zeichnen Sie vSwitch, Uplink, Portgruppen und VM-Adapter und beschriften Sie, was ein VMkernel-Adapter ist (Fachwissen).
2. **Prüfung ausführen (Einheit 6.2):** Führen Sie `bash lauf.sh` aus und erklären Sie die drei Hinweise mit Behebung.
3. **VLANs (Einheit 6.3):** Erklären Sie den zulässigen Bereich der VLAN-ID im Modell und was die ID 0 bedeutet (im Modell: ohne VLAN-Markierung).
4. **Netzkonzept (Einheit 6.4):** Entwerfen Sie ein Netzkonzept mit getrenntem Management- und VM-Netz inklusive Portgruppen, VLAN-IDs und Adressen.

#### Kontrollfragen

1. Was passiert mit einem vSwitch ohne Uplink?
2. Warum muss die Portgruppe einer VM existieren?
3. Warum trennt man Management- und VM-Verkehr?

### Modul 7: Ressourcenverwaltung: Shares, Reservierungen und Limits

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Reservierung, Limit und Shares unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Verteilung bei Überlast nachrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Auswirkungen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Prioritäten festlegen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Begriffe: Reservierung, Limit, Shares; Überbuchung von CPU und RAM | 2 |
| 7.2 | Praxis: Verteilung bei Überlast berechnen (`ressourcen_rechner.py`) | 2 |
| 7.3 | Auswirkungen: Wartezeiten, Auslagerung, Startfehler durch Reservierungen | 2 |
| 7.4 | Planung: Prioritäten und Grenzen festlegen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe (Einheit 7.1):** Erklären Sie Reservierung, Limit und Shares in eigenen Worten und geben Sie je ein Beispiel (Fachwissen).
2. **Verteilung rechnen (Einheit 7.2):** Führen Sie `bash lauf.sh` aus und rechnen Sie die Zuteilung für `db01`, `web01` und `test01` von Hand nach.
3. **Folgen (Einheit 7.3):** Beschreiben Sie, warum eine VM sich nicht starten lässt, wenn die Summe der Reservierungen die Kapazität übersteigt.
4. **Prioritäten (Einheit 7.4):** Legen Sie für drei Dienste (Datenbank, Web, Test) Shares, Reservierung und Limit fest und begründen Sie die Werte.

#### Kontrollfragen

1. Wann greifen Shares?
2. Was bewirkt ein Limit?
3. Warum sind hohe Reservierungen für Testsysteme unüblich?

### Modul 8: Snapshots und Klone

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Snapshots von Sicherungen abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Kette aus Differenzabbildern nachbilden.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln für den Betrieb festlegen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Snapshot und Differenzplatten: Kette, Platzbedarf, Risiken | 2 |
| 8.2 | Praxis: Differenzabbilder und Zusammenführen nachbilden (`snapshot_kette.sh`) | 2 |
| 8.3 | Regeln im Betrieb: kurz halten, wenige, aufräumen; Klone und Vorlagen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Snapshot oder Sicherung (Einheit 8.1):** Erklären Sie, warum ein Snapshot keine Sicherung ist, und nennen Sie drei Probleme langer Snapshot-Ketten.
2. **Kette nachbilden (Einheit 8.2):** Führen Sie `bash snapshot_kette.sh` aus und beschreiben Sie die fünf Schritte; erklären Sie, warum das Zusammenführen die Kette verkürzt.
3. **Regeln (Einheit 8.3):** Formulieren Sie vier Betriebsregeln für Snapshots, Klone und Vorlagen und begründen Sie sie.

#### Kontrollfragen

1. Warum wächst das Differenzabbild mit der Zeit?
2. Was bewirkt das Zusammenführen einer Kette?
3. Warum sind lange Ketten ein Betriebsrisiko?

### Modul 9: Sicherung und Export ohne Sicherungsschnittstelle

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Einschränkung der Sicherung benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Export und Prüfsumme praktisch nachbilden.
  * Nach Abschluss dieses Moduls kann der Lernende Alternativen bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende einen Plan mit Test aufstellen.
* **Voraussetzungen:** Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Was beim kostenlosen ESXi für die Sicherung fehlt (VADP) und was bleibt | 2 |
| 9.2 | Praxis: Export mit Prüfsumme und Wiederimport (`export_import.sh`) | 2 |
| 9.3 | Alternativen: Export als OVF, Kopie der Dateien, Sicherung im Gast | 2 |
| 9.4 | Sicherungsplan und Wiederherstellungstest | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einschränkung (Einheit 9.1):** Erklären Sie, welche Sicherungswege beim kostenlosen ESXi laut gelesener Quelle fehlen und welche Wege Ihnen bleiben (Fachwissen kennzeichnen).
2. **Export prüfen (Einheit 9.2):** Führen Sie `bash export_import.sh` aus und erklären Sie, wie die Prüfsumme eine Veränderung der Datei erkennbar macht.
3. **Alternativen bewerten (Einheit 9.3):** Bewerten Sie Export als OVF, Dateikopie und Sicherung im Gast nach Aufwand, Konsistenz und Wiederherstellung.
4. **Plan und Test (Einheit 9.4):** Erstellen Sie einen Sicherungsplan für `esx1` mit Häufigkeit, Aufbewahrung, Ziel, Prüfsummen und Wiederherstellungstest.

#### Kontrollfragen

1. Warum genügt eine Sicherung ohne Wiederherstellungstest nicht?
2. Was belegt eine unveränderte Prüfsumme?
3. Warum ist Dateikopie bei laufender VM riskant?

### Modul 10: vCenter, Hochverfügbarkeit und Lastverteilung als Konzept

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle von vCenter beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Zulassungsprüfung nachrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen von HA, vMotion und DRS nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Reserven planen.
* **Voraussetzungen:** Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Wofür vCenter gebraucht wird und was es voraussetzt | 2 |
| 10.2 | Praxis: Zulassungsprüfung und Lastverteilung als Modell (`ha_modell.py`) | 3 |
| 10.3 | Hochverfügbarkeit, vMotion und DRS: Voraussetzungen und Grenzen | 2 |
| 10.4 | Planung: Reserve für Ausfälle, Netz, Speicher, Lizenz | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **vCenter-Rolle (Einheit 10.1):** Erklären Sie, welche Aufgaben vCenter übernimmt und warum der kostenlose ESXi sie nicht bietet.
2. **Ausfalltest rechnen (Einheit 10.2):** Führen Sie `bash lauf.sh` aus und erklären Sie, warum beim Ausfall von `esx2` kein Platz für `app01` bleibt.
3. **Voraussetzungen (Einheit 10.3):** Nennen Sie Voraussetzungen für HA, vMotion und DRS (gemeinsamer Speicher, Netz, Lizenz, vCenter) und kennzeichnen Sie sie als Fachwissen.
4. **Reserve planen (Einheit 10.4):** Berechnen Sie, wie viel Arbeitsspeicher Sie in einem Drei-Host-Cluster frei halten müssen, damit ein Host ausfallen darf.

#### Kontrollfragen

1. Warum bedeutet HA nicht, dass nichts ausfällt?
2. Wozu dient die Zulassungsprüfung?
3. Warum braucht vMotion gemeinsamen Speicher oder geeignetes Netz?

### Modul 11: Benutzer, Rollen und Protokolle

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rollen und Vererbung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte im Modell prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldefehlschläge erkennen.
* **Voraussetzungen:** Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Lokale Benutzer, Rollen und Vererbung | 2 |
| 11.2 | Praxis: Rechte und Anmeldefehlschläge im Modell (`rollen_modell.py`) | 3 |
| 11.3 | Protokolle: Wo Meldungen zu finden sind, was zu prüfen ist | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rollenkonzept (Einheit 11.1):** Beschreiben Sie Benutzer und Rollen für ein kleines Team und kennzeichnen Sie, dass dies Fachwissen und nicht aus der Dokumentation ist.
2. **Modell ausführen (Einheit 11.2):** Führen Sie `bash lauf.sh` aus und erklären Sie, warum `anna` `web01` einschalten, aber nicht ändern darf und warum `cem` `db01` nicht ansehen darf.
3. **Fehlschläge (Einheit 11.2):** Erklären Sie die Warnung zu den Anmeldefehlschlägen von 10.7.0.99 und nennen Sie zwei Maßnahmen.
4. **Protokolle (Einheit 11.3):** Listen Sie auf, in welchen Protokollen Sie bei einer fehlgeschlagenen VM-Aktion nachsehen (Host-Dienstprotokoll, VM-Protokoll, Kernelprotokoll) und kennzeichnen Sie das als Fachwissen.

#### Kontrollfragen

1. Warum sollte root nicht für die tägliche Arbeit verwendet werden?
2. Wozu dient Vererbung von Rechten?
3. Warum zählt man Anmeldefehlschläge je Quelle?

### Modul 12: Automatisierung mit PowerCLI

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Möglichkeiten und Grenzen der Automatisierung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende aus einem Plan Befehle erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken wie Anmeldedaten im Skript vermeiden.
* **Voraussetzungen:** Modul 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Automatisierung und Einschränkung beim kostenlosen ESXi (API nur lesend/eingeschränkt) | 2 |
| 12.2 | Praxis: Plan in PowerCLI-Befehle umsetzen (`plan_zu_powercli.py`) | 2 |
| 12.3 | Absicherung: Anmeldedaten, Prüfen vor Ausführen, Protokoll | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Möglichkeiten und Grenzen (Einheit 12.1):** Beschreiben Sie, was Automatisierung nützt und warum beim kostenlosen ESXi schreibende Automatisierung eingeschränkt sein kann (laut gelesener Quelle API nur lesend/eingeschränkt; nicht geprüft).
2. **Befehle erzeugen (Einheit 12.2):** Führen Sie `bash lauf.sh` aus und prüfen Sie die Form der Befehle gegen die Hersteller-Dokumentation zu PowerCLI. Beschreiben Sie, was nicht bestätigt ist.
3. **Absicherung (Einheit 12.3):** Beschreiben Sie, wie Sie Anmeldedaten schützen, vor dem Ausführen prüfen und protokollieren.

#### Kontrollfragen

1. Warum werden Anmeldedaten nie im Skript abgelegt?
2. Warum werden Befehle zuerst als Text erzeugt?
3. Warum ist das Ausführen gegen den kostenlosen ESXi unsicher?

### Modul 13: Fehlersuche und Abschluss

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Fehler systematisch eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Meldungen typischen Ursachen zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Gegenmaßnahmen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Betriebshandbuch erstellen.
* **Voraussetzungen:** Module 1 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Systematische Fehlersuche: Protokolle, Ressourcen, Speicher, Netz | 2 |
| 13.2 | Praxis: Meldungen Ursachen zuordnen (`fehler_zuordnen.py`) | 2 |
| 13.3 | Typische Fehlerbilder und erste Prüfungen | 3 |
| 13.4 | Abschlussprojekt: Betriebshandbuch für `esx1` | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorgehen (Einheit 13.1):** Beschreiben Sie in sechs Schritten Ihr Vorgehen bei „VM startet nicht“.
2. **Meldungen zuordnen (Einheit 13.2):** Führen Sie `bash lauf.sh` aus. Begründen Sie je Zeile, ob die Zuordnung stimmt, und erklären Sie die Zeile ohne Zuordnung.
3. **Fehlerbilder (Einheit 13.3):** Erstellen Sie eine Tabelle mit fünf Fehlerbildern (Ursache, erste Prüfung, Gegenmaßnahme) und kennzeichnen Sie sie als Erfahrungswerte.
4. **Betriebshandbuch (Einheit 13.4):** Erstellen Sie ein Betriebshandbuch für `esx1`: Netzplan, Speicherplan, Sicherungsplan, Rollen, Aktualisierung, Notfallverfahren; vermerken Sie die Grenzen des kostenlosen ESXi mit Stand.

#### Kontrollfragen

1. Warum ist die Reihenfolge der Prüfschritte wichtig?
2. Warum gehört der Stand der Lizenzgrenzen ins Betriebshandbuch?
3. Warum gehört der Wiederherstellungstest ins Betriebshandbuch?
