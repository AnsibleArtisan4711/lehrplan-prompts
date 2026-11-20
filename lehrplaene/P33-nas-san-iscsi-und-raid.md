# Lehrplan: NAS, SAN, iSCSI und RAID

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Terminal) |
| **Gesamtumfang** | 11 Module, 120 UE (zu 45 Minuten; 90 Stunden) |
| **Fokus-Technologien** | Linux-Software-RAID (mdadm), Dateisysteme (ext4, XFS), iSCSI (Target mit tgt, Initiator), NAS-Grundlagen (NFS, SMB), Überwachung (SMART) |
| **Thematische Abgrenzung (Out of Scope)** | Das Backup-Konzept (RPO, RTO, 3-2-1-1-0) und die Notfallplanung stehen in den Kursen „Backup-Konzept“ und „Notfallplanung und DR“ dieses Repositories; hier die Grundlagen der Speichertechnik. Nicht behandelt: Fibre Channel und FCoE im Detail, Storage-Systeme bestimmter Hersteller, Windows Storage Spaces, ZFS und Btrfs, Hardware-RAID-Controller im Detail, Verschlüsselung der Datenträger |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Speicherarten: DAS, NAS, SAN und der Unterschied zwischen Block und Datei | 1 | 10 |
| 2 | RAID-Stufen und ihre Wahl | 1 | 12 |
| 3 | Parität verstehen: XOR, Rekonstruktion und Write Hole | 1 | 12 |
| 4 | Dateisysteme: ext4 und XFS anlegen, vergrößern und prüfen | 1 | 12 |
| 5 | NAS-Grundlagen: NFS und SMB und die Prüfung von Freigaben | 1 | 10 |
| 6 | iSCSI: Target mit tgt einrichten | 1 | 12 |
| 7 | iSCSI: Initiator, Namen und Zugriffsschutz prüfen | 1 | 12 |
| 8 | Multipath im Überblick | 2 | 8 |
| 9 | Kapazitätsplanung | 1 | 10 |
| 10 | SMART und Überwachung | 1 | 10 |
| 11 | Ausfall, Wiederherstellung, Schreib-Cache und USV | 1 | 12 |
| **Gesamt** | 11 Module | 10 × Priorität 1, 1 × Priorität 2 | **120** |

**Priorität 1** (Pflicht) sind die Module 1 bis 7 und 9 bis 11; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 8 (Multipath im Überblick). Fällt Modul 8 weg, verringert sich der Gesamtumfang auf 112 UE; kein Pflichtmodul setzt Modul 8 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von mdadm, tgt, open-iscsi, NFS, Samba und smartmontools sowie die RFCs zu iSCSI (3720) und NFS wurden **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch die Läufe im Labor bestätigt; verbindlich ist die Dokumentation der installierten Version. Zahlen zu Fehlerraten, Plattengeschwindigkeit, Wachstum und USV sind **Annahmen**.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** mdadm 4.3, tgt 1.0.85, libiscsi-bin 1.19.0, e2fsprogs 1.47.0, xfsprogs 6.6.0, smartmontools 7.4, Python 3. Ein Software-RAID mit `mdadm` ließ sich im Container **nicht** anlegen (kein md-Kernelmodul); es wird als Python-Modell gezeigt. Die Beispieldaten (Namen, IQN, Adressen, SMART-Werte, Exports) sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Storage`, `10.33.0.0/24`).

**VMs:** `stor01` (**erforderlich**, `10.33.0.2`): Ubuntu Server 24.04 mit einer Systemplatte und **vier zusätzlichen virtuellen Platten** zu je 2 GB; Pakete `mdadm`, `tgt`, `smartmontools`, `xfsprogs`, `nfs-kernel-server`, `samba` (Namen der Pakete aus Fachwissen, nicht bestätigt). `init01` (**erforderlich ab Modul 7**, `10.33.0.10`): Ubuntu Server 24.04 mit `open-iscsi` oder Windows 11 mit dem iSCSI-Initiator.

**Internetphase:** Für die Paketinstallation braucht `stor01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 3 und vor Modul 6 von `stor01` je einen Prüfpunkt anlegen. **Achtung:** Prüfpunkte mit RAID und iSCSI sind für Versuche praktisch, bilden aber keinen echten Ausfall ab; sie sind **keine** Datensicherung.

**Skripte:** Die Beispielskripte liefen **nicht** in Hyper-V, sondern in einem Cloud-Container mit **Loop-Geräten** (Image-Dateien unter `/tmp/p33`) und einer Userspace-Instanz von `tgtd` auf `127.0.0.1:3260`; als Initiator dienten die Werkzeuge aus `libiscsi-bin` (Userspace) statt des Kernel-Initiators. Auf `stor01` und `init01` stehen echte Platten und der Kernel-Initiator zur Verfügung; Gerätenamen (`/dev/sdb` usw.) sind dort **zu prüfen**.

## B. Detaillierter Modulaufbau

### Modul 1: Speicherarten: DAS, NAS, SAN und der Unterschied zwischen Block und Datei

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende DAS, NAS und SAN unterscheiden und typische Einsatzfälle nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Block-Zugriff und Datei-Zugriff erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Block-Gerät ohne und mit Dateisystem untersuchen.
  * Nach Abschluss dieses Moduls kann der Lernende die Speicherart nach Anforderungen begründet wählen.
* **Voraussetzungen:** IP-Adressen und Ports; Linux-Grundlagen (Terminal).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Speicherarten im Überblick: DAS, NAS, SAN; Block-Zugriff gegen Datei-Zugriff | 3 |
| 1.2 | Praxis: ein Block-Gerät ohne und mit Dateisystem (`blockgeraet_und_dateisystem.sh`) | 3 |
| 1.3 | Auswahl nach Anforderung: Zugriffsart, Zahl der Clients, Verfügbarkeit, Kosten | 2 |
| 1.4 | Labor aufbauen und prüfen: `stor01` mit vier Platten, privater Switch | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Speicherarten zuordnen (Einheit 1.1):** Ordnen Sie sechs Beispiele (USB-Platte am Laptop, Heimserver mit Freigabe, Speichersystem für virtuelle Maschinen, Fotoarchiv, Datenbank-Laufwerk, Projektordner einer Abteilung) DAS, NAS oder SAN zu und begründen Sie.
2. **Block-Gerät untersuchen (Einheit 1.2):** Führen Sie `bash blockgeraet_und_dateisystem.sh` aus. Beschreiben Sie, was `blkid` vor und nach `mkfs` anzeigt und warum die rohen Daten ohne Dateisystem trotzdem lesbar sind.
3. **Auswahl begründen (Einheit 1.3):** Wählen Sie für eine Firma mit 20 Arbeitsplätzen, einem Dateiserver und zwei virtuellen Servern eine Speicherlösung und begründen Sie in fünf Sätzen (Annahmen kennzeichnen).
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie `stor01` mit vier zusätzlichen virtuellen Platten und den privaten Switch auf. Prüfen Sie mit `lsblk`, dass die vier Platten sichtbar sind (Gerätenamen notieren).

#### Kontrollfragen

1. Wer verwaltet das Dateisystem beim NAS und wer beim SAN?
2. Warum kann ein Block-Gerät ohne Dateisystem Daten speichern, aber keine Dateien?
3. Welche Rolle spielt das Netzwerk bei SAN und NAS?
4. Warum ist eine USB-Platte ein DAS und kein NAS?

### Modul 2: RAID-Stufen und ihre Wahl

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende RAID-Stufen mit Kapazität und Ausfalltoleranz berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende den Schreibaufwand der Stufen vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende das Rebuild-Risiko abschätzen und einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Stufe begründet wählen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Ziele von RAID: Ausfallsicherheit, Leistung, Kapazität; RAID ist keine Sicherung | 3 |
| 2.2 | Stufen 0, 1, 5, 6 und 10: Aufbau, Kapazität, Ausfalltoleranz (`raid_rechner.py`) | 3 |
| 2.3 | Schreibaufwand und Rebuild-Risiko: Lesefehler beim Wiederaufbau | 3 |
| 2.4 | Wahl nach Anforderung und Hot-Spare; Grenzen von RAID | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kapazität berechnen (Einheit 2.2):** Berechnen Sie für 6 Platten zu 4 TB die nutzbare Kapazität von RAID 5, 6 und 10 von Hand und prüfen Sie mit `python3 raid_rechner.py 6 4000`.
2. **Risiko abschätzen (Einheit 2.3):** Führen Sie `raid_rechner.py` für 4 Platten zu 8 TB mit URE-Rate 1e-14 und 1e-15 aus und erklären Sie, warum die Ergebnisse so verschieden sind und was an dem Modell vereinfacht ist.
3. **Stufe wählen (Einheit 2.4):** Wählen Sie für drei Fälle (Archiv, Datenbank mit vielen kleinen Schreibvorgängen, Testsystem) eine Stufe und begründen Sie. Kennzeichnen Sie Annahmen.
4. **Grenzen benennen (Einheit 2.1):** Nennen Sie fünf Ereignisse, gegen die RAID **nicht** schützt (z. B. Löschen, Verschlüsselungsschadsoftware, Brand, Fehlkonfiguration, Controller-Fehler).

#### Kontrollfragen

1. Warum ist RAID 5 mit sehr großen Platten problematisch?
2. Warum ist RAID keine Datensicherung?
3. Was kostet RAID 6 gegenüber RAID 5 an Kapazität und Schreibleistung?
4. Wozu dient eine Hot-Spare-Platte?

### Modul 3: Parität verstehen: XOR, Rekonstruktion und Write Hole

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende XOR als Grundlage der Parität erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine ausgefallene Platte aus den übrigen berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen (zwei Ausfälle, Write Hole) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die wichtigsten `mdadm`-Schritte nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | XOR und Parität: warum sich eine fehlende Platte berechnen lässt | 3 |
| 3.2 | Streifen und rotierende Parität (`xor_raid.py`) | 3 |
| 3.3 | Grenzen: zwei Ausfälle, Write Hole, Journal und Cache | 3 |
| 3.4 | Software-RAID mit `mdadm` im Überblick; was im Labor geht und was nicht | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **XOR von Hand (Einheit 3.1):** Berechnen Sie die Parität von 1011, 0110 und 1100 von Hand und rekonstruieren Sie den Wert der zweiten Platte aus den übrigen.
2. **Modell ausführen (Einheit 3.2):** Führen Sie `python3 xor_raid.py` aus. Erklären Sie, wo die Parität je Streifen liegt und warum jede der vier Platten rekonstruierbar ist.
3. **Write Hole erklären (Einheit 3.3):** Beschreiben Sie mit dem Ergebnis des letzten Abschnitts, warum nach einem Stromausfall mitten im Schreibvorgang und einem späteren Plattenausfall falsche Daten entstehen, ohne dass ein Fehler gemeldet wird.
4. **`mdadm` planen (Einheit 3.4):** Schreiben Sie die Befehle auf, mit denen Sie auf `stor01` ein RAID 5 aus drei Platten anlegen, prüfen und beim Ausfall einer Platte ersetzen würden. Kennzeichnen Sie Befehle, die Sie nicht geprüft haben.

#### Kontrollfragen

1. Warum ist XOR für Parität geeignet?
2. Warum verkraftet RAID 5 keinen zweiten Ausfall?
3. Was ist das Write Hole und wie wird es verringert?
4. Warum liegt die Parität nicht immer auf derselben Platte?

### Modul 4: Dateisysteme: ext4 und XFS anlegen, vergrößern und prüfen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aufgaben eines Dateisystems nennen.
  * Nach Abschluss dieses Moduls kann der Lernende ext4 und XFS anlegen und Eckdaten lesen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Dateisystem vergrößern.
  * Nach Abschluss dieses Moduls kann der Lernende ein Dateisystem nur lesend prüfen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Aufgaben eines Dateisystems: Metadaten, Journal, Blockgröße | 3 |
| 4.2 | ext4 und XFS im Vergleich (Eckdaten, Vergrößern, Prüfen) | 3 |
| 4.3 | Praxis: anlegen, einbinden, vergrößern, prüfen (`dateisysteme.sh`) | 4 |
| 4.4 | Einbinden dauerhaft: `/etc/fstab` und UUID (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eckdaten vergleichen (Einheit 4.2):** Führen Sie `bash dateisysteme.sh` aus und stellen Sie Blockgröße, Journal/Log und Größe von ext4 und XFS in einer Tabelle gegenüber.
2. **Vergrößern (Einheit 4.3):** Beschreiben Sie, wie die beiden Dateisysteme im Skript vergrößert wurden (Reihenfolge: Datenträger, Dateisystem) und was dabei eingebunden oder ausgehängt war.
3. **Prüfen (Einheit 4.3):** Erklären Sie die Ausgabe von `e2fsck -fn` und `xfs_repair -n` und warum beide ohne Änderung laufen sollen.
4. **fstab planen (Einheit 4.4):** Schreiben Sie eine Zeile für `/etc/fstab`, die ein Dateisystem anhand der UUID nach `/daten` einbindet (UUID erfinden) und begründen Sie, warum nicht der Gerätename verwendet wird.
5. **Aufgaben nennen (Einheit 4.1):** Nennen Sie vier Aufgaben eines Dateisystems (z. B. Metadaten, Journal) und erklären Sie die Blockgröße an einem Beispiel.

#### Kontrollfragen

1. Warum ist beim Vergrößern die Reihenfolge Datenträger zuerst, Dateisystem danach wichtig?
2. Was ist der Zweck des Journals?
3. Warum wird zum Prüfen die Option „nur lesend“ (`-n`) zuerst genutzt?
4. Warum bindet man Datenträger in `/etc/fstab` über die UUID ein?

### Modul 5: NAS-Grundlagen: NFS und SMB und die Prüfung von Freigaben

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende NFS und SMB unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache Freigabe in beiden Formaten schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationen auf riskante Muster prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte und Zugriffskreis begrenzen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | NAS und Protokolle: NFS (Unix) und SMB (Windows), Aufgaben und Unterschiede | 3 |
| 5.2 | Freigaben konfigurieren: `/etc/exports` und die Samba-Konfiguration (Fachwissen) | 3 |
| 5.3 | Freigaben prüfen: riskante Muster erkennen (`freigaben_pruefen.py`) | 2 |
| 5.4 | Rechte und Konten: wer darf lesen, wer schreiben | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Protokolle vergleichen (Einheit 5.1):** Erstellen Sie eine Tabelle NFS gegen SMB (typische Clients, Anmeldung, Rechte, Einsatz) aus Fachwissen; kennzeichnen Sie, was nicht geprüft ist.
2. **Freigabe schreiben (Einheit 5.2):** Schreiben Sie (ohne Server) eine NFS-Freigabe `/srv/nfs/daten` für das Netz `10.33.0.0/24` nur lesend und eine SMB-Freigabe `[daten]` für die Gruppe `@lab` schreibbar.
3. **Prüfung ausführen (Einheit 5.3):** Führen Sie `python3 freigaben_pruefen.py` aus und beheben Sie jeden Hinweis in einer Kopie der beiden Beispieldateien. Prüfen Sie erneut.
4. **Zugriffskreis festlegen (Einheit 5.4):** Legen Sie fest, welche Clients, Benutzer und Rechte für die Freigabe `projekte` sinnvoll sind, und begründen Sie in vier Sätzen.

#### Kontrollfragen

1. Warum ist `no_root_squash` riskant?
2. Warum sollten Freigaben nicht für alle Clients geöffnet sein?
3. Was bedeutet `async` bei NFS für die Datensicherheit?
4. Warum ist ein Gastzugang bei SMB ein Risiko?

### Modul 6: iSCSI: Target mit tgt einrichten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Begriffe Initiator, Target, LUN, IQN und Portal erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Target mit einer LUN anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende den Zugriff nach Initiator-Name und CHAP einschränken.
  * Nach Abschluss dieses Moduls kann der Lernende Planungsfragen (Netz, Leistung, Sicherung) nennen.
* **Voraussetzungen:** Module 1 und 4; IP-Adressen und Ports.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | iSCSI im Überblick: Initiator, Target, LUN, IQN, Portal, Port 3260 | 3 |
| 6.2 | Praxis: Ziel, LUN, Zugriffsliste anlegen (`target_anlegen.sh`) | 3 |
| 6.3 | Absichern: Zugriff nach Initiator-Name und CHAP | 3 |
| 6.4 | Planung: Netz trennen, Image oder Platte als LUN, Leistung und Sicherung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe zuordnen (Einheit 6.1):** Zeichnen Sie ein Bild mit Initiator, Netzwerk, Target, LUN und Portal und beschriften Sie, wo der IQN steht.
2. **Target anlegen (Einheit 6.2):** Führen Sie `bash target_anlegen.sh` aus und erklären Sie jeden `tgtadm`-Aufruf in einem Satz.
3. **Zugriff beschränken (Einheit 6.3):** Erklären Sie anhand von Schritt 3 und 4, welche zwei Schutzebenen im Skript benutzt werden und warum die ACL allein nicht reicht.
4. **Planung (Einheit 6.4):** Beschreiben Sie, wie Sie auf `stor01` eine reale Platte oder ein logisches Volume als LUN bereitstellen, und was Sie am Netz trennen würden (Fachwissen, nicht geprüft).

#### Kontrollfragen

1. Was ist eine LUN?
2. Wofür steht der IQN und wie ist er aufgebaut?
3. Warum ist eine Zugriffsliste nach Initiator-Name allein kein ausreichender Schutz?
4. Warum gehört iSCSI-Verkehr in ein eigenes Netz?

### Modul 7: iSCSI: Initiator, Namen und Zugriffsschutz prüfen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf Discovery, Login und Sitzung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Ziele entdecken und LUN-Eigenschaften abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler bei Namen und Anmeldung deuten.
  * Nach Abschluss dieses Moduls kann der Lernende IQN-Namen auf das Format prüfen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Der Weg: Discovery, Login, Sitzung, Block-Gerät im Initiator | 3 |
| 7.2 | Praxis: Ziele entdecken und LUN abfragen mit libiscsi-Werkzeugen (`initiator_lesen.sh`) | 3 |
| 7.3 | Zugriffsschutz testen: fremder Name, CHAP (`initiator_lesen.sh`) | 2 |
| 7.4 | Namen prüfen: IQN-Format (`iqn_pruefen.py`) | 2 |
| 7.5 | Kernel-Initiator auf `init01`: `open-iscsi`, Windows-Initiator (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ablauf beschreiben (Einheit 7.1):** Beschreiben Sie in fünf Schritten, was bei Discovery und Login zwischen Initiator und Target geschieht (Fachwissen) und markieren Sie, was nicht geprüft ist.
2. **Abfragen auswerten (Einheit 7.2):** Führen Sie `bash initiator_lesen.sh` aus. Notieren Sie Portal, Zielname, Gerätetyp und Kapazität der LUN.
3. **Fehler deuten (Einheit 7.3):** Erklären Sie die Meldungen „Target not found(515)“ und „Authentication failure(513)“ und die jeweilige Gegenmaßnahme.
4. **IQN prüfen (Einheit 7.4):** Führen Sie `python3 iqn_pruefen.py` mit eigenen Namen aus (drei gültige, drei ungültige) und begründen Sie jede Meldung.
5. **Kernel-Initiator planen (Einheit 7.5):** Beschreiben Sie die Schritte, mit denen Sie auf `init01` (Linux mit `open-iscsi` oder Windows) ein Ziel entdecken und anmelden würden; kennzeichnen Sie ungeprüfte Befehle.

#### Kontrollfragen

1. Was unterscheidet Discovery von Login?
2. Warum meldet das Target bei einem unbekannten Initiator-Namen „Target not found“?
3. Wozu dient die Kapazitätsabfrage vor dem Einbinden?
4. Warum entsteht erst nach dem Login ein Block-Gerät im Initiator?

### Modul 8: Multipath im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Multipath beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Verteilung und Umschaltung im Modell nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen von Multipath bei iSCSI nennen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Warum mehrere Pfade: Ausfall von Karte, Kabel, Switch oder Portal | 2 |
| 8.2 | Richtlinien: aktiv/passiv, Round-Robin (`multipfad_modell.py`) | 3 |
| 8.3 | Multipath bei iSCSI: zwei Portale, Konfiguration im Überblick (Fachwissen) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einzelfehler suchen (Einheit 8.1):** Listen Sie auf einer Skizze alle Stellen zwischen Server und Speicher auf, deren Ausfall den Zugriff ohne Multipath unterbrechen würde.
2. **Modell ausführen (Einheit 8.2):** Führen Sie `python3 multipfad_modell.py` aus und vergleichen Sie die Verteilung von aktiv/passiv und Round-Robin mit und ohne Ausfall.
3. **Voraussetzungen nennen (Einheit 8.3):** Nennen Sie fünf Voraussetzungen, damit zwei Pfade zum selben Speicher wirklich unabhängig sind (z. B. getrennte Netze, Switches, Karten).

#### Kontrollfragen

1. Wie unterscheiden sich aktiv/passiv und Round-Robin?
2. Warum schützt Multipath nicht vor dem Ausfall des Speichers selbst?
3. Warum sollten beide Pfade getrennte Switches nutzen?
4. Was bedeutet es, wenn das Modell die Umschaltzeit nicht berücksichtigt?

### Modul 9: Kapazitätsplanung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende nutzbare Kapazität einer Konfiguration berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende den Zeitpunkt der Füllung abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Überzeichnung bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende eine Erweiterung planen.
* **Voraussetzungen:** Module 2 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Nutzbare Kapazität: RAID, Dateisystem, Reserve, Snapshots | 3 |
| 9.2 | Wachstum abschätzen und Füllzeitpunkt berechnen (`kapazitaet.py`) | 3 |
| 9.3 | Thin Provisioning und Überzeichnung: Nutzen und Risiko | 2 |
| 9.4 | Erweiterung planen: Platten, Verbund, Dateisystem | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kapazität berechnen (Einheit 9.1):** Berechnen Sie für 6 Platten zu 4 TB mit 20 % Reserve die nutzbare Kapazität von RAID 5, 6 und 10 und prüfen Sie mit `python3 kapazitaet.py`.
2. **Füllzeitpunkt (Einheit 9.2):** Ändern Sie Bestand und Wachstum im Skript auf eigene (erfundene) Werte und notieren Sie, in welchem Jahr jede Stufe voll ist.
3. **Überzeichnung bewerten (Einheit 9.3):** Beurteilen Sie, bei welcher Belegung die Überzeichnung aus dem Beispiel gefährlich wird, und welche Überwachung Sie einrichten würden.
4. **Erweiterung planen (Einheit 9.4):** Planen Sie die Erweiterung von RAID 6 auf größere Platten in Schritten (Platte tauschen, Rebuild, Verbund und Dateisystem vergrößern) und nennen Sie die Risiken.

#### Kontrollfragen

1. Warum rechnet man mit einer Reserve?
2. Warum hängt der Füllzeitpunkt stark vom Wachstum ab?
3. Welches Risiko hat Thin Provisioning?
4. Warum ist das Tauschen aller Platten ein längeres Risikofenster?

### Modul 10: SMART und Überwachung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SMART und seine Grenzen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende wichtige Attribute und Rohwerte deuten.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, wann SMART nicht verfügbar ist.
  * Nach Abschluss dieses Moduls kann der Lernende eine regelmäßige Prüfung planen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Was SMART ist und was es nicht kann: Vorwarnung, keine Garantie | 3 |
| 10.2 | Wichtige Attribute und Rohwerte lesen (`smart_auswerten.py`) | 3 |
| 10.3 | `smartctl` bei virtuellen Geräten: warum es im Labor nichts liefert | 2 |
| 10.4 | Überwachung einrichten: regelmäßige Prüfung und Alarm (Fachwissen) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Grenzen nennen (Einheit 10.1):** Nennen Sie drei Fälle, in denen eine Platte ausfällt, ohne dass SMART vorher warnt (Fachwissen), und drei Fälle, in denen SMART warnt, obwohl die Platte noch lange hält.
2. **Attribute auswerten (Einheit 10.2):** Führen Sie `python3 smart_auswerten.py smart_platte_gut.txt smart_platte_auffaellig.txt` aus und erklären Sie jeden Hinweis der auffälligen Platte.
3. **Virtuelle Geräte (Einheit 10.3):** Erklären Sie, warum `smartctl -i` bei einem Loop-Gerät „Unable to detect device type“ meldet und was das für die VM-Platten in Hyper-V bedeutet.
4. **Überwachung planen (Einheit 10.4):** Planen Sie die regelmäßige Prüfung für vier Platten (Zeitplan, Kurz- und Langtest, Alarm per E-Mail, Zuständigkeit); kennzeichnen Sie nicht geprüfte Befehle.

#### Kontrollfragen

1. Warum ist ein SMART-Wert ohne Auffälligkeit keine Garantie?
2. Welche Attribute deuten auf Probleme mit Sektoren hin?
3. Warum helfen SMART-Werte bei einer virtuellen Platte nicht?
4. Warum ersetzt SMART kein Backup?

### Modul 11: Ausfall, Wiederherstellung, Schreib-Cache und USV

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf bei einem Plattenausfall beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Rebuild-Zeit und Risikofenster berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Nutzen und Risiko des Schreib-Caches erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die USV-Laufzeit gegen die Herunterfahrzeit prüfen.
* **Voraussetzungen:** Module 2, 3 und 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Ablauf bei Plattenausfall: erkennen, melden, tauschen, wiederaufbauen, prüfen | 3 |
| 11.2 | Rebuild-Zeit und Risikofenster berechnen (`ausfall_planung.py`) | 3 |
| 11.3 | Schreib-Cache: Nutzen und Risiko bei Stromausfall; USV und sauberes Herunterfahren | 3 |
| 11.4 | Abschlussübung: Notfallablauf für den Verbund schreiben | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ablauf beschreiben (Einheit 11.1):** Schreiben Sie den Ablauf bei einem Plattenausfall als Liste von acht Schritten (Erkennen bis Prüfen) und nennen Sie je Schritt, wer zuständig ist.
2. **Rebuild berechnen (Einheit 11.2):** Führen Sie `python3 ausfall_planung.py` aus und beantworten Sie: Wie lange dauert der Rebuild einer 8-TB-Platte bei 50 % Last, und welches Risiko entsteht?
3. **USV prüfen (Einheit 11.3):** Prüfen Sie mit dem Skript, ob die USV mit 120 Wh bei 300 W für das Herunterfahren reicht, und ändern Sie die Werte für Ihr Labor (erfundene Angaben kennzeichnen).
4. **Notfallablauf (Einheit 11.4):** Schreiben Sie einen einseitigen Ablauf für „Platte im RAID 6 ausgefallen“ mit Prüfung nach dem Rebuild (Zustand, Sicherung, Ersatzplatte nachbestellen).

#### Kontrollfragen

1. Warum ist die Last während des Rebuilds wichtig?
2. Welches Risiko hat ein Schreib-Cache ohne Batteriepufferung?
3. Warum muss die USV-Laufzeit größer sein als die Herunterfahrzeit?
4. Welche Rolle spielt die Sicherung beim Plattenausfall?
