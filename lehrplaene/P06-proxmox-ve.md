# Lehrplan: Proxmox VE

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Linux-Grundlagen (Shell, Netzwerk, Speicher) und Grundbegriffe der Virtualisierung |
| **Gesamtumfang** | 14 Module, 115 UE (zu 45 Minuten; 86,25 Stunden) |
| **Fokus-Technologien** | Proxmox VE 9.x (KVM-VMs, LXC-Container), Proxmox Backup Server; Labor verschachtelt unter Hyper-V |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Grundlagen der Virtualisierung und Hyper-V im Kurs „Hyper-V“, VMware im Kurs „VMware vSphere/ESXi“, Datensicherungskonzepte im Kurs „Datensicherung“. Nicht behandelt: Ceph-Betrieb im Detail, Software-defined Networking über Grundlagen hinaus, Betrieb großer Cluster, Lizenz- und Supportverträge im Detail |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Architektur, Installation und verschachtelte Virtualisierung | 1 | 8 |
| 2 | Weboberfläche, Shell und die Speicherkonfiguration | 1 | 8 |
| 3 | Virtuelle Maschinen mit KVM | 1 | 8 |
| 4 | Container mit LXC | 1 | 8 |
| 5 | Speicher: Verzeichnis, LVM, ZFS, NFS und Ceph | 1 | 9 |
| 6 | Netzwerk: Linux-Bridges und VLANs | 1 | 9 |
| 7 | Vorlagen, Klone und Abbild-Formate | 1 | 7 |
| 8 | Snapshots | 1 | 7 |
| 9 | Datensicherung und Proxmox Backup Server | 1 | 9 |
| 10 | Cluster, Quorum und Hochverfügbarkeit | 1 | 9 |
| 11 | Migration: Live-Migration und Wechsel von anderen Hypervisoren | 1 | 8 |
| 12 | Benutzer, Rollen und Berechtigungen | 1 | 8 |
| 13 | Fehlersuche und Abschluss | 1 | 10 |
| 14 | Automatisierung mit CLI und API | 2 | 7 |
| **Gesamt** | 14 Module | 13 × Priorität 1, 1 × Priorität 2 | **115** |

**Priorität 1** (Pflicht) sind die Module 1 bis 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 14 (Automatisierung mit CLI und API). Fällt Modul 14 weg, verringert sich der Gesamtumfang auf 108 UE; kein Pflichtmodul setzt es voraus.

### 2. Quellen

**Gelesen (mit Abrufdatum 20.11.2026):** (1) Ankündigung/Release-Notizen zu **Proxmox VE 9.2** vom 21. Mai 2026: Basis Debian 13.5 („Trixie“), Kernel 7.0, QEMU 11.0, LXC 7.0, ZFS 2.4; Neuerungen u. a. Dynamic Load Balancer, SDN mit WireGuard/BGP, HA arm/disarm. (2) Handbuchseite **Storage** (Tabelle der Speichertypen und Inhaltsarten, `/etc/pve/storage.cfg`; Snapshots auf Verzeichnis-/NFS-/CIFS-Speicher nur mit qcow2). (3) Dokumentation **Proxmox Backup Server** (Prune entfernt nur Sicherungseinträge, Speicherbereinigung gibt Chunks frei mit 24 h 5 min Schonfrist, Verify unabhängig, Befehle `proxmox-backup-manager`). (4) Handbuchseiten **Netzwerk** (Bridge `vmbr0`, VLAN-aware, `ifreload -a`, `/etc/network/interfaces.new`) und **Cluster-Manager** (UDP 5405–5412, Latenz unter 5 ms, mindestens drei Knoten für HA, Quorum, `pvecm`, QDevice). (5) Microsoft-Dokumentation zu **verschachtelter Virtualisierung unter Hyper-V** (`Set-VMProcessor -ExposeVirtualizationExtensions $true`, MAC-Adress-Spoofing oder NAT, Mindest-Konfigurationsversion 8.0 Intel bzw. 9.3 AMD).

**Nicht gelesen:** Handbuchseiten zu Benutzerverwaltung/Berechtigungen, Containern (LXC), Vorlagen/Klonen, Migration, `qm`/`pct`/API; Mindestanforderungen an Hardware; Lizenz-/Support-Modelle. Diese Inhalte stammen aus Fachwissen und sind **nicht bestätigt**. Die Befehle von `qm`, `pct`, `pvesm`, `pvecm` und `vzdump` wurden **nicht ausgeführt**, weil keine Proxmox-Umgebung zur Verfügung stand. Die Beispieldaten (Konfigurationsdateien, Protokollzeilen, Rollen) sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V (Host) mit **verschachtelter Virtualisierung**. **Switch:** ein privater Switch `Lab-PVE` (`10.6.0.0/24`) ohne Verbindung zum Heimnetz; für Installation und Updates vorübergehend ein zweiter Adapter an einem externen Switch.

**VMs:** `pve1` (**erforderlich**, `10.6.0.11`): Proxmox-VE-Host als VM mit eingeschalteten Virtualisierungserweiterungen (Richtwert 4 vCPU, 8 GB RAM, 64 GB Platte; **nicht geprüft**). `pve2` (`10.6.0.12`) und `pve3` (`10.6.0.13`) für die Module 10 und 11 (Cluster, Migration). `pbs1` (`10.6.0.20`, optional) für Modul 9. Auf den PVE-Hosts laufen kleine Test-VMs und -Container (ein Linux mit wenigen hundert MB RAM).

**Hinweis zu Nested:** Bei Hyper-V muss die Erweiterung für jede VM bei ausgeschalteter VM aktiviert werden (laut Microsoft-Dokumentation `Set-VMProcessor -VMName <Name> -ExposeVirtualizationExtensions $true`), außerdem MAC-Adress-Spoofing am Adapter oder NAT. Ohne diese Einstellung meldet Proxmox VE, dass keine Hardwarebeschleunigung (KVM) vorhanden ist.

**Prüfpunkt (Checkpoint):** Vor Modul 8 von `pve1` einen Prüfpunkt anlegen. **Skripte:** Die Beispielskripte liefen in einem Cloud-Container (Ubuntu 24.04) **ohne** KVM, ohne Proxmox, mit `qemu-img`, Netzwerk-Namespaces, Bridges und LVM auf Loop-Geräten. Sie bilden Konzepte nach (Abbild-Formate, Snapshots, Bridge, Quorum, Chunk-Speicher); es sind **keine** Proxmox-Befehle.

## B. Detaillierter Modulaufbau

### Modul 1: Architektur, Installation und verschachtelte Virtualisierung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau von Proxmox VE mit KVM und LXC beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für Hardware-Virtualisierung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende verschachtelte Virtualisierung unter Hyper-V einschalten.
  * Nach Abschluss dieses Moduls kann der Lernende Installationsschritte und Nacharbeiten festhalten.
* **Voraussetzungen:** Linux-Grundlagen; Grundbegriffe der Virtualisierung.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Aufbau von Proxmox VE: Debian-Basis, KVM für VMs, LXC für Container, Weboberfläche | 2 |
| 1.2 | Voraussetzungen: CPU-Erweiterungen, `/dev/kvm`, verschachtelte Virtualisierung unter Hyper-V | 2 |
| 1.3 | Praxis: Voraussetzungen prüfen (`nested_pruefen.sh`) | 2 |
| 1.4 | Installation, erste Anmeldung und Nacharbeiten (Repositories, Updates, Hostname) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bausteine zuordnen (Einheit 1.1):** Zeichnen Sie ein Schema mit Host-Hardware, Debian-Basis, KVM, QEMU, LXC und Weboberfläche und beschriften Sie, was eine VM von einem Container unterscheidet.
2. **Nested-Befehle notieren (Einheit 1.2):** Schreiben Sie auf, welche Einstellungen unter Hyper-V für verschachtelte Virtualisierung nötig sind (Erweiterungen, MAC-Spoofing oder NAT, VM aus), und ordnen Sie sie dem Fehlerbild „keine KVM-Hardwarebeschleunigung“ zu.
3. **Voraussetzungen prüfen (Einheit 1.3):** Führen Sie `bash nested_pruefen.sh` aus. Erklären Sie die Auswertung und was auf einem Rechner mit der Meldung „KEIN KVM“ zu tun wäre.
4. **Installationsprotokoll (Einheit 1.4):** Legen Sie eine Checkliste für die Installation von `pve1` an: Hostname (FQDN), feste IP, Zeitzone, Passwort, Repository-Wahl, erste Updates. Vermerken Sie, was später nicht mehr leicht zu ändern ist (z. B. Hostname im Cluster).

#### Kontrollfragen

1. Wozu braucht Proxmox VE die CPU-Erweiterungen vmx oder svm?
2. Worin unterscheidet sich ein LXC-Container von einer KVM-VM?
3. Warum muss die Virtualisierungserweiterung unter Hyper-V bei ausgeschalteter VM gesetzt werden?
4. Warum sollte der Hostname vor dem Aufbau eines Clusters feststehen?

### Modul 2: Weboberfläche, Shell und die Speicherkonfiguration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Weboberfläche und die Aufgabenprotokolle sicher bedienen.
  * Nach Abschluss dieses Moduls kann der Lernende die wichtigsten Kommandozeilenwerkzeuge zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau von `storage.cfg` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Inhaltsarten gegen die Tabelle der Speichertypen prüfen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Weboberfläche, Datenzentrum-Ansicht, Knoten, Protokolle und Aufgaben | 2 |
| 2.2 | Die Shell: Werkzeuge `qm`, `pct`, `pvesm`, `pvecm` im Überblick | 2 |
| 2.3 | Die Datei `storage.cfg` und die erlaubten Inhaltsarten je Speichertyp | 2 |
| 2.4 | Praxis: Speicherkonfiguration automatisch prüfen (`storage_pruefen.py`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Oberfläche erkunden (Einheit 2.1):** Beschreiben Sie, wo in der Weboberfläche Sie den Zustand des Hosts, die Aufgabenprotokolle und die Speicher sehen. Notieren Sie, was Sie nach einem fehlgeschlagenen Start einer VM zuerst ansehen.
2. **Werkzeuge zuordnen (Einheit 2.2):** Ordnen Sie `qm`, `pct`, `pvesm`, `pvecm` und `vzdump` ihren Aufgaben zu und nennen Sie je einen Beispielzweck. Kennzeichnen Sie, was Sie nur aus Fachwissen angeben.
3. **Konfiguration lesen (Einheit 2.3):** Lesen Sie `storage.cfg` und beschreiben Sie je Eintrag Typ, Pfad bzw. Server und erlaubte Inhaltsarten.
4. **Prüfung ausführen (Einheit 2.4):** Führen Sie `python3 storage_pruefen.py storage.cfg` aus. Erklären Sie die beiden gemeldeten Verstöße und wie Sie sie beheben.

#### Kontrollfragen

1. Warum ist die Aufgabenansicht beim Fehlersuchen wichtig?
2. Welche Inhaltsart ist bei einem Backup-Server-Speicher (pbs) laut Tabelle erlaubt?
3. Warum kann eine Speicherkonfiguration mit falscher Inhaltsart zu Fehlern führen?

### Modul 3: Virtuelle Maschinen mit KVM

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine VM sinnvoll dimensionieren.
  * Nach Abschluss dieses Moduls kann der Lernende Gerätemodelle und Treiber auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende eine VM-Konfigurationsdatei lesen und auf Auffälligkeiten prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Betriebsabläufe für VMs beschreiben.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | VM anlegen: CPU, Speicher, Platte, Netzwerkkarte, BIOS/UEFI | 2 |
| 3.2 | Gerätemodelle: virtio, SCSI-Controller, VirtIO-Treiber unter Windows | 2 |
| 3.3 | Praxis: VM-Konfigurationsdatei lesen und prüfen (`vm_conf_pruefen.py`) | 2 |
| 3.4 | Betrieb: Start, Stopp, Konsole, Gast-Agent, Ressourcenplanung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dimensionierung (Einheit 3.1):** Legen Sie für einen kleinen Webserver und einen Datenbankserver je CPU-Kerne, Arbeitsspeicher und Plattengröße fest und begründen Sie die Werte. Rechnen Sie nach, was beide zusammen auf `pve1` belegen.
2. **Gerätemodelle (Einheit 3.2):** Erklären Sie, warum virtio-Geräte für Linux-Gäste meist gewählt werden und was bei einem Windows-Gast zusätzlich nötig ist (Treiber), und kennzeichnen Sie das als Fachwissen.
3. **Konfiguration prüfen (Einheit 3.3):** Führen Sie `bash lauf.sh` aus (prüft `100.conf` und `101.conf`) und beschreiben Sie jede Zeile von `100.conf` sowie jeden Hinweis zu `101.conf` mit Behebung.
4. **Betriebsablauf (Einheit 3.4):** Beschreiben Sie in fünf Schritten, wie Sie eine VM sauber herunterfahren und was passiert, wenn der Gast-Agent fehlt.

#### Kontrollfragen

1. Warum ist Überbuchung von Arbeitsspeicher riskanter als Überbuchung von CPU-Kernen?
2. Wozu dient ein Gast-Agent?
3. Was bedeutet es, wenn eine VM-Konfiguration einen Netzwerkadapter einer nicht vorhandenen Bridge nennt?

### Modul 4: Container mit LXC

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Container Isolation herstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Namespaces praktisch beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende privilegierte und unprivilegierte Container unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende zwischen VM und Container begründet entscheiden.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Wie Container funktionieren: Kernel-Namespaces und Ressourcengrenzen | 2 |
| 4.2 | Praxis: Namespaces selbst erzeugen (`namespaces_demo.sh`) | 2 |
| 4.3 | Container in Proxmox: Vorlagen, privilegiert oder unprivilegiert, Ressourcen | 2 |
| 4.4 | Wann VM, wann Container: Entscheidungskriterien | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Isolation erklären (Einheit 4.1):** Erklären Sie in eigenen Worten die Namespaces für Hostname, Prozesse und Netzwerk und warum alle Container denselben Kernel nutzen.
2. **Namespaces beobachten (Einheit 4.2):** Führen Sie `bash namespaces_demo.sh` aus und erläutern Sie jede Ausgabe (Hostname, Prozess-ID 1, Netzwerkschnittstellen).
3. **Container-Arten (Einheit 4.3):** Beschreiben Sie den Unterschied zwischen privilegierten und unprivilegierten Containern und warum unprivilegiert als sicherer gilt (Fachwissen, nicht bestätigt).
4. **Entscheidungshilfe (Einheit 4.4):** Entscheiden Sie für fünf Anwendungen (Webserver Linux, Windows-Server, Datenbank mit eigenem Kernelmodul, DNS-Dienst, Test mit anderem Betriebssystem), ob VM oder Container passt, und begründen Sie.

#### Kontrollfragen

1. Warum kann ein Container keinen anderen Kernel als der Host verwenden?
2. Was zeigt `PID 1` im neuen PID-Namespace?
3. Warum sind Container schneller gestartet als VMs?

### Modul 5: Speicher: Verzeichnis, LVM, ZFS, NFS und Ceph

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Speichertypen anhand der Tabelle auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende LVM-Begriffe praktisch beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende raw und qcow2 unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Speicherplan begründen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Speichertypen und was sie können: Verzeichnis, LVM, LVM-thin, ZFS, NFS, CIFS, Ceph | 2 |
| 5.2 | Praxis: Volume-Gruppen mit LVM (`lvm_demo.sh`) | 2 |
| 5.3 | Abbild-Formate und Snapshots je Speichertyp (raw, qcow2) | 2 |
| 5.4 | Speicher planen: Kapazität, Leistung, Ausfallsicherheit, gemeinsamer Speicher | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Speichertypen vergleichen (Einheit 5.1):** Erstellen Sie eine Tabelle mit Verzeichnis, LVM, LVM-thin, ZFS, NFS und Ceph und tragen Sie ein, ob der Speicher gemeinsam nutzbar ist und ob Snapshots möglich sind (laut gelesener Tabelle, sonst Fachwissen kennzeichnen).
2. **LVM beobachten (Einheit 5.2):** Führen Sie `bash lvm_demo.sh` aus und erklären Sie Physical Volume und Volume Group. Erklären Sie die gezeigte Fehlermeldung bei der Erstellung eines Logical Volumes und warum sie im Container auftritt.
3. **Formate (Einheit 5.3):** Erklären Sie, warum Snapshots auf Verzeichnis-, NFS- und CIFS-Speicher laut Dokumentation qcow2 voraussetzen, und welchen Nachteil qcow2 gegenüber raw haben kann (Fachwissen).
4. **Speicherplan (Einheit 5.4):** Entwerfen Sie für `pve1` einen Speicherplan für System, VMs, Container-Vorlagen und Sicherungen und begründen Sie die Wahl der Speichertypen.

#### Kontrollfragen

1. Warum ist für Migration im laufenden Betrieb gemeinsamer Speicher hilfreich?
2. Was ist der Unterschied zwischen LVM und LVM-thin?
3. Warum sollte Sicherung nicht auf derselben Platte wie die VM liegen?

### Modul 6: Netzwerk: Linux-Bridges und VLANs

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Linux-Bridge erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Bridge mit zwei Gästen praktisch nachbauen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Netzwerkkonfiguration auf typische Fehler prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende VLAN-aware Bridges und NAT-Netze beschreiben.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Linux-Bridge `vmbr0`: Aufbau und Aufgabe, Zuordnung zu VMs | 2 |
| 6.2 | Praxis: Bridge mit zwei Gästen nachbauen (`bridge_demo.sh`) | 2 |
| 6.3 | Konfigurationsdatei `interfaces` lesen und prüfen (`interfaces_pruefen.py`) | 2 |
| 6.4 | VLAN-aware Bridge, NAT-Netz und Änderungen übernehmen (`ifreload -a`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bridge erklären (Einheit 6.1):** Erklären Sie anhand einer Zeichnung, wie `vmbr0`, die physische Schnittstelle und die virtuellen Adapter der VMs zusammenhängen.
2. **Bridge nachbauen (Einheit 6.2):** Führen Sie `bash bridge_demo.sh` aus. Beschreiben Sie, warum der Ping zwischen den Gästen funktioniert und was nach dem Abhängen eines Gastes geschieht.
3. **Konfiguration prüfen (Einheit 6.3):** Führen Sie `python3 interfaces_pruefen.py interfaces` aus und erklären Sie den gemeldeten Fehler der Bridge `vmbr2`.
4. **Änderungen übernehmen (Einheit 6.4):** Beschreiben Sie, wie Sie eine Netzwerkänderung vorbereiten und übernehmen (`/etc/network/interfaces.new`, `ifreload -a`) und warum Sie auf der Konsole bleiben sollten.

#### Kontrollfragen

1. Wozu dient eine Bridge im Vergleich zu einem Switch?
2. Warum kann eine fehlerhafte Netzwerkänderung den Zugriff auf den Host verhindern?
3. Wozu dient ein NAT-Netz für Test-VMs?

### Modul 7: Vorlagen, Klone und Abbild-Formate

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende verknüpfte und vollständige Klone unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Abbilder mit `qemu-img` umwandeln.
  * Nach Abschluss dieses Moduls kann der Lernende Abbilder anderer Hypervisoren für den Import vorbereiten.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Vorlage und Klon: verknüpft oder vollständig | 2 |
| 7.2 | Praxis: Abbilder umwandeln und Overlays anlegen (`qemu_img_demo.sh`) | 2 |
| 7.3 | Abbilder anderer Hypervisoren übernehmen (VMDK, VHDX) und Plattenwechsel | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Klonarten (Einheit 7.1):** Erklären Sie anhand von `qemu_img_demo.sh`, wie ein verknüpfter Klon (Overlay mit Basisabbild) im Vergleich zu einem vollständigen Klon Platz belegt und was bei Löschen der Basis passiert.
2. **Abbilder umwandeln (Einheit 7.2):** Führen Sie `bash qemu_img_demo.sh` aus und beschreiben Sie die Größen der Formate raw, qcow2, vmdk und vhdx sowie das Ergebnis von `qemu-img compare`.
3. **Import vorbereiten (Einheit 7.3):** Beschreiben Sie, wie Sie eine VHDX-Platte aus Hyper-V für Proxmox VE vorbereiten und worauf Sie vor dem Wechsel achten (Treiber, Firmware).

#### Kontrollfragen

1. Warum belegt ein verknüpfter Klon anfangs fast keinen Platz?
2. Was bedeutet „Images are identical“ nach einer Umwandlung?
3. Warum garantiert ein identisches Abbild nicht, dass der Gast nach dem Wechsel startet?

### Modul 8: Snapshots

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Snapshot und Sicherung unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Snapshots auf Abbildebene anlegen, zurückrollen und löschen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln für den Einsatz im Betrieb festlegen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Was ein Snapshot ist und was nicht: Zustand, Kette, Platzbedarf | 2 |
| 8.2 | Praxis: Snapshots auf Abbild-Ebene (`snapshot_demo.sh`) | 2 |
| 8.3 | Snapshots im Betrieb: Einsatz vor Änderungen, Aufräumen, Grenzen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Snapshot oder Sicherung (Einheit 8.1):** Erklären Sie, warum ein Snapshot keine Sicherung ist, und nennen Sie drei Szenarien, in denen ein Snapshot nicht hilft.
2. **Snapshots ausprobieren (Einheit 8.2):** Führen Sie `bash snapshot_demo.sh` aus und beschreiben Sie die fünf Schritte und die Veränderung der Größe.
3. **Regeln (Einheit 8.3):** Formulieren Sie vier Regeln für den Einsatz von Snapshots (Dauer, Anzahl, Vorbedingungen, Aufräumen) und begründen Sie sie.

#### Kontrollfragen

1. Warum ist ein Snapshot auf demselben Speicher keine Sicherung?
2. Warum wachsen Snapshots mit der Zeit?
3. Was geschieht mit Änderungen nach dem Zurückrollen?

### Modul 9: Datensicherung und Proxmox Backup Server

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Deduplizierung am Beispiel erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Prune, Speicherbereinigung und Verify unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Sicherungsplan aufstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wiederherstellung als festen Bestandteil planen.
* **Voraussetzungen:** Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Sicherungsarten: Vollsicherung, Inkrement, Deduplizierung | 2 |
| 9.2 | Praxis: Chunk-Speicher nachbilden (`pbs_modell.py`) | 2 |
| 9.3 | Prune, Speicherbereinigung (GC) und Verify beim Backup-Server | 2 |
| 9.4 | Wiederherstellung testen und Sicherungsplan erstellen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Deduplizierung (Einheit 9.1):** Erklären Sie, wie ein Chunk-Speicher mit Hash-Adressen gleiche Blöcke nur einmal ablegt, und warum die zweite unveränderte Sicherung kaum Platz belegt.
2. **Modell ausführen (Einheit 9.2):** Führen Sie `python3 pbs_modell.py` aus und beschreiben Sie die fünf Zeilen der Ausgabe, besonders den Unterschied vor und nach der Speicherbereinigung.
3. **Prune und GC (Einheit 9.3):** Beschreiben Sie, warum nach dem Entfernen von Sicherungen (Prune) der Platz erst nach der Speicherbereinigung frei wird, und welche Schonfrist laut gelesener Dokumentation gilt.
4. **Sicherungsplan (Einheit 9.4):** Erstellen Sie einen Plan für `pve1`: was wird gesichert, wie oft, wie lange aufbewahrt, wohin, wann geprüft (Verify) und wie getestet wird.

#### Kontrollfragen

1. Warum ist Prune allein kein Weg, Platz zu gewinnen?
2. Wozu dient Verify?
3. Warum genügt eine Sicherung ohne Wiederherstellungstest nicht?

### Modul 10: Cluster, Quorum und Hochverfügbarkeit

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Quorum berechnen und Folgen eines Ausfalls einschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für HA nennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Clusteraufbau planen.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken wie Split-Brain und Zeitverhalten erklären.
* **Voraussetzungen:** Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Cluster-Grundlagen: Knoten, Corosync, gemeinsames Cluster-Dateisystem | 2 |
| 10.2 | Praxis: Quorum nachrechnen (`quorum_rechner.py`) | 2 |
| 10.3 | Hochverfügbarkeit (HA): Voraussetzungen, Ressourcen, Verhalten bei Ausfall | 2 |
| 10.4 | Cluster aufbauen und ändern: Planung, Befehle, Fehler vermeiden | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Cluster-Elemente (Einheit 10.1):** Beschreiben Sie Corosync, das Cluster-Dateisystem und die benötigten Ports (UDP 5405 bis 5412 laut gelesener Dokumentation) sowie die Anforderung an die Netzwerklatenz.
2. **Quorum rechnen (Einheit 10.2):** Führen Sie `python3 quorum_rechner.py` aus. Erklären Sie die Zeilen für zwei Knoten mit und ohne QDevice und für vier Knoten bei zwei Ausfällen.
3. **HA-Voraussetzungen (Einheit 10.3):** Nennen Sie die Voraussetzungen für HA (mindestens drei Knoten, gemeinsamer Speicher, Quorum) und beschreiben Sie, was bei Quorumverlust geschieht.
4. **Aufbauplan (Einheit 10.4):** Planen Sie den Aufbau von `pve1` bis `pve3`: Hostnamen und IPs vorab, Reihenfolge der Befehle (`pvecm create`, `pvecm add`, `pvecm status`), Prüfungen danach. Befehle als Fachwissen/Doku kennzeichnen.

#### Kontrollfragen

1. Warum sind zwei Knoten ohne QDevice für ein Cluster problematisch?
2. Was passiert mit dem Cluster-Dateisystem ohne Quorum?
3. Warum ist eine geringe Latenz im Cluster-Netz wichtig?

### Modul 11: Migration: Live-Migration und Wechsel von anderen Hypervisoren

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen der Live-Migration nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Platten aus Hyper-V für andere Hypervisoren umwandeln.
  * Nach Abschluss dieses Moduls kann der Lernende eine Migration planen und Rückweg sichern.
  * Nach Abschluss dieses Moduls kann der Lernende das Ergebnis prüfen.
* **Voraussetzungen:** Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Live-Migration zwischen Knoten: Voraussetzungen und Grenzen | 2 |
| 11.2 | Praxis: VHDX nach qcow2 und VMDK umwandeln (`migration_vhdx.sh`) | 2 |
| 11.3 | Migrationsplanung: Treiber, Firmware, Netzwerk, Rückweg | 2 |
| 11.4 | Durchführung und Prüfung nach der Migration | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Live-Migration (Einheit 11.1):** Nennen Sie Voraussetzungen für die Live-Migration (gemeinsamer Speicher oder Kopie, ähnliche CPUs, Netz) und erklären Sie, warum CPU-Hersteller gleich sein sollten (laut gelesener Dokumentation für Online-Migration).
2. **Abbild umwandeln (Einheit 11.2):** Führen Sie `bash migration_vhdx.sh` aus und beschreiben Sie Größen und Vergleichsergebnis der Umwandlung.
3. **Planung (Einheit 11.3):** Erstellen Sie eine Migrationsplanung mit Checkliste (Treiber, Firmware, Netzwerk, Test, Rückweg) für eine Windows-VM von Hyper-V nach Proxmox VE.
4. **Nachkontrolle (Einheit 11.4):** Legen Sie fest, was Sie nach der Migration prüfen (Start, Netz, Dienste, Zeit, Sicherung) und wie Sie die alte VM bis zur Freigabe aufbewahren.

#### Kontrollfragen

1. Warum ist ein Rückweg bei jeder Migration wichtig?
2. Wozu dient der Vergleich nach `qemu-img convert`?
3. Warum werden Treiber vor dem Wechsel vorbereitet?

### Modul 12: Benutzer, Rollen und Berechtigungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Benutzer, Gruppen und Rollen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Rechtevergabe über Pfade mit Vererbung verstehen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Rechtemodell prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Grundsätze zur Rechtevergabe anwenden.
* **Voraussetzungen:** Modul 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Benutzerverwaltung: Bereiche (Realms), Benutzer, Gruppen, API-Token | 2 |
| 12.2 | Rollen, Pfade und Vererbung | 2 |
| 12.3 | Praxis: Rechteprüfung modellieren (`acl_modell.py`) | 2 |
| 12.4 | Grundsätze: geringste Rechte, Trennung, Protokollierung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Benutzerkonzept (Einheit 12.1):** Beschreiben Sie Benutzer, Gruppen und Rollen für ein kleines Team (Administration, Betrieb, Prüfer) und kennzeichnen Sie, dass diese Angaben nicht aus der Dokumentation, sondern Fachwissen sind.
2. **Vererbung (Einheit 12.2):** Erklären Sie anhand eines Pfadbaums, wie eine Rolle an einem Pfad für untergeordnete Pfade gilt und wie ein tieferer Eintrag sie überlagert.
3. **Modell prüfen (Einheit 12.3):** Führen Sie `python3 acl_modell.py` aus und erklären Sie, warum `anna` die VM 100 bedienen, aber VM 101 nur ansehen darf.
4. **Grundsätze (Einheit 12.4):** Formulieren Sie vier Regeln für die Rechtevergabe (geringste Rechte, keine gemeinsamen Konten, Prüfung, Protokoll) und begründen Sie sie.

#### Kontrollfragen

1. Warum sollten Berechtigungen an Gruppen statt einzelne Benutzer vergeben werden?
2. Was bedeutet Vererbung bei Pfaden?
3. Warum sind API-Token sinnvoll für Automatisierung?

### Modul 13: Fehlersuche und Abschluss

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Fehler systematisch eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Meldungen typischen Ursachen zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Gegenmaßnahmen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Betriebshandbuch erstellen.
* **Voraussetzungen:** Module 1 bis 12.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Systematische Fehlersuche: Aufgabenprotokoll, Systemprotokoll, Dienste | 2 |
| 13.2 | Praxis: Meldungen Ursachen zuordnen (`fehler_zuordnen.py`) | 2 |
| 13.3 | Typische Fehlerbilder: Nested/KVM, Quorum, Speicher voll, Namensauflösung, Rechte | 3 |
| 13.4 | Abschlussprojekt: Betriebshandbuch für `pve1` bis `pve3` | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorgehen (Einheit 13.1):** Beschreiben Sie in sechs Schritten Ihr Vorgehen bei „VM startet nicht“ (Aufgabenprotokoll, Speicher, Netz, Ressourcen, Rechte, Wiederholung).
2. **Meldungen zuordnen (Einheit 13.2):** Führen Sie `python3 fehler_zuordnen.py` aus. Begründen Sie je Zeile, ob die Zuordnung stimmt, und erklären Sie die Zeile ohne Zuordnung.
3. **Fehlerbilder (Einheit 13.3):** Erstellen Sie eine Tabelle mit fünf Fehlerbildern (Ursache, erste Prüfung, Gegenmaßnahme) und kennzeichnen Sie, welche Zeilen aus der gelesenen Dokumentation und welche aus Fachwissen stammen.
4. **Betriebshandbuch (Einheit 13.4):** Erstellen Sie ein Betriebshandbuch für `pve1` bis `pve3`: Netzwerkplan, Speicherplan, Sicherungsplan, Rechte, Aktualisierung, Notfallverfahren.

#### Kontrollfragen

1. Warum ist die Reihenfolge der Prüfschritte wichtig?
2. Wo zeigt sich fehlendes Quorum zuerst?
3. Warum gehört der Wiederherstellungstest ins Betriebshandbuch?

### Modul 14: Automatisierung mit CLI und API

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Nutzen von Automatisierung begründen.
  * Nach Abschluss dieses Moduls kann der Lernende aus einem Plan Befehle erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen und Risiken beschreiben.
* **Voraussetzungen:** Modul 13.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 14.1 | Aufgaben per Kommandozeile und API statt Oberfläche | 2 |
| 14.2 | Praxis: Plan in Befehle umsetzen (`plan_zu_befehlen.py`) | 2 |
| 14.3 | Grenzen der Automatisierung: Idempotenz, Fehlerbehandlung, Berechtigungen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Nutzen und Risiko (Einheit 14.1):** Nennen Sie drei Vorteile und drei Risiken, wenn VMs per Skript statt per Oberfläche angelegt werden.
2. **Befehle erzeugen (Einheit 14.2):** Führen Sie `python3 plan_zu_befehlen.py` aus. Beschreiben Sie, wie aus dem Plan die Befehle entstehen und prüfen Sie ihre Form gegen die Handbuchseite von `qm`.
3. **Absicherung (Einheit 14.3):** Beschreiben Sie, wie Sie Doppelanlegen verhindern und Fehler abfangen (Prüfen vor Anlegen, Abbruch, Protokoll), und welche Rechte ein API-Token dafür braucht.

#### Kontrollfragen

1. Warum werden Skripte zuerst als Text erzeugt und nicht gleich ausgeführt?
2. Was bedeutet Idempotenz bei Automatisierung?
3. Warum sollte ein Token nur die nötigen Rechte haben?
