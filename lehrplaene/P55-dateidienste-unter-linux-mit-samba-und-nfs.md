# Lehrplan: Dateidienste unter Linux mit Samba und NFS

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen; Grundkenntnisse in Berechtigungen |
| **Gesamtumfang** | 8 Module, 98 UE (zu 45 Minuten; 73,5 Stunden) |
| **Fokus-Technologien** | Debian/Ubuntu Linux, Samba, NFS; Samba als Standalone-Server; Freigaben, Benutzer, POSIX-Rechte und ACLs; Samba als Domänenmitglied (Grundzüge); NFS-Exporte und Mount-Optionen; Zugriff von Windows- und Linux-Clients; Sicherheit; Fehlersuche; Sicherung |
| **Thematische Abgrenzung (Out of Scope)** | Windows-Dateidienste und DFS sind der Kurs „Dateidienste, DFS und Druckserver“ dieses Lehrplans; Active Directory nur soweit für den Domänenbeitritt nötig. Nicht behandelt: Samba als Domänencontroller, Cluster-Dateisysteme, CTDB, Kerberos-gesichertes NFS im Detail, automatische Einhängung mit `autofs` |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | SMB und NFS im Überblick | 1 | 12 |
| 2 | Samba als Standalone-Server | 1 | 14 |
| 3 | Freigaben und Berechtigungen | 1 | 14 |
| 4 | ACLs für Freigaben | 1 | 12 |
| 5 | Samba als Domänenmitglied (Grundzüge) | 2 | 10 |
| 6 | NFS-Exporte und Mount-Optionen | 1 | 12 |
| 7 | Sicherheit bei Dateidiensten | 1 | 12 |
| 8 | Fehlersuche und Sicherung | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **98** |

**Priorität 1** (Pflicht) sind die Module 1 bis 4 und 6 bis 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 5 (Samba als Domänenmitglied). Fällt Modul 5 weg, verringert sich der Gesamtumfang auf 88 UE; kein Pflichtmodul setzt Modul 5 voraus.

### 2. Quellen

**Nicht gelesen:** Die Handbücher von Samba und NFS (`smb.conf`, `exports`, `nfs`) wurden **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt; verbindlich ist die Dokumentation der eingesetzten Version. Zahlen und Namen sind erfundene Beispieldaten.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container, Kernel 6.18.44):** Samba 4.19.5 (`smbd`, `smbclient`, `testparm`, `smbpasswd`, `pdbedit`) als Standalone-Server auf `127.0.0.1:4455`, `setfacl`/`getfacl`, `tar`, Python 3. **Nicht ausführbar im Container:** NFS (kein NFS im Kernel, daher weder Server noch Client), Windows-Clients, ein Domänencontroller und damit der Domänenbeitritt. Diese Teile sind Modelle oder Textdateien mit der Kennzeichnung „nicht ausgeführt“ und **nicht bestätigt**. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Dateidienste`, `10.55.0.0/24`).

**VMs:** `fs01` (**erforderlich**, `10.55.0.2`): Linux-Server (Debian oder Ubuntu Server) mit den Paketen `samba`, `acl`, `nfs-kernel-server`; `win11` (`10.55.0.10`): Windows-11-Client; `lx01` (`10.55.0.11`): Linux-Client mit `smbclient`, `cifs-utils` und `nfs-common`. Für Modul 5 zusätzlich ein Domänencontroller (`dc01`, `10.55.0.5`) aus einem anderen Kurs.

**Internetphase:** Für die Installation der Pakete brauchen die Linux-VMs vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es werden nur erfundene Beispieldaten verwendet.

**Prüfpunkt (Checkpoint):** Vor Modul 3 und vor Modul 7 von `fs01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte im Test-Container starten einen eigenen Samba-Server auf `127.0.0.1` Port 4455 (Konfiguration und Daten unter `/tmp/p55`), legen die Testbenutzer `anna` und `ben` und die Gruppe `projekt` an und entfernen alles am Ende. Auf `fs01` läuft Samba auf dem Standardport 445.

## B. Detaillierter Modulaufbau

### Modul 1: SMB und NFS im Überblick

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SMB und NFS nach Clients, Anmeldung, Versionen und Berechtigungen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende zwischen geprüften (L) und nicht bestätigten (F) Aussagen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende für ein Szenario das passende Protokoll begründen.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor aufbauen.
* **Voraussetzungen:** Grundkenntnisse in Berechtigungen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Protokolle vergleichen: Tabelle mit Status L und F (`protokolle.py`) | 4 |
| 1.2 | Einsatzszenarien zuordnen: Windows-, Linux- und gemischte Umgebungen | 3 |
| 1.3 | Pakete und Dienste auf `fs01`: `smbd`, `nmbd`, `nfs-server` (Fachwissen) | 2 |
| 1.4 | Labor aufbauen: `fs01`, `win11`, `lx01`, privater Switch | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tabelle lesen (Einheit 1.1):** Führen Sie `python3 protokolle.py` aus. Erklären Sie jede Zeile und warum nur drei mit L gekennzeichnet sind.
2. **Szenarien zuordnen (Einheit 1.2):** Ordnen Sie drei Szenarien (Windows-11-Abteilung, Linux-Entwicklungsrechner, gemischtes Büro) SMB oder NFS zu und begründen Sie jede Wahl in zwei Sätzen. Nennen Sie, was Sie noch prüfen müssten.
3. **Pakete und Dienste (Einheit 1.3):** Listen Sie auf, welche Pakete und Dienste für Samba und für NFS auf `fs01` nötig sind und woran Sie erkennen, dass sie laufen. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie `fs01`, `win11` und `lx01` am Switch `Lab-Dateidienste` auf und prüfen Sie die Verbindung mit `ping`.

#### Kontrollfragen

1. Wofür steht SMB, und welches Programmpaket setzt es unter Linux um?
2. Worin unterscheiden sich SMB und NFS bei der Anmeldung?
3. Warum sollte SMB1 nicht mehr verwendet werden (Fachwissen)?
4. Welche Rolle spielen UID und GID bei NFS (Fachwissen)?

### Modul 2: Samba als Standalone-Server

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Standalone-Konfiguration mit `[global]` und einer Freigabe schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Samba-Benutzer anlegen und die Datenbank lesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Zugriff mit `smbclient` testen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wem eine über Samba angelegte Datei gehört.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Konfiguration schreiben und mit `testparm` prüfen (`standalone.sh`) | 4 |
| 2.2 | Linux-Konto und Samba-Passwort: `useradd`, `smbpasswd`, `pdbedit` (`standalone.sh`) | 3 |
| 2.3 | Zugriff mit `smbclient` testen, Dateibesitz auf dem Server (`standalone.sh`) | 3 |
| 2.4 | Zugriff von `win11` und `lx01` (Befehle als Fachwissen, nicht ausgeführt) | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration prüfen (Einheit 2.1):** Führen Sie `bash standalone.sh` aus. Erklären Sie jede Zeile der Konfiguration und die Ausgabe von `testparm`.
2. **Benutzer anlegen (Einheit 2.2):** Erklären Sie, warum ein Benutzer sowohl ein Linux-Konto als auch ein Samba-Passwort braucht und was `pdbedit -L` anzeigt.
3. **Zugriff testen (Einheit 2.3):** Erklären Sie Schritt 3 und 4: Wer ist Eigentümer der angelegten Datei, und warum zeigt sie die Rechte `rwxr--r--`?
4. **Clients (Einheit 2.4):** Schreiben Sie auf, wie `win11` (`\\10.55.0.2\daten`) und `lx01` (`smbclient`, `mount -t cifs`) auf die Freigabe zugreifen. Kennzeichnen Sie, was Sie nicht geprüft haben, und führen Sie es auf den VMs aus.

#### Kontrollfragen

1. Was bedeutet `server role = standalone server`?
2. Warum braucht ein Samba-Benutzer ein eigenes Passwort?
3. Welche Meldung erscheint bei falschem Passwort?
4. Wo speichert `passdb backend = tdbsam` die Passwörter?

### Modul 3: Freigaben und Berechtigungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zugriff auf Freigaben mit `valid users`, `read only` und `write list` steuern.
  * Nach Abschluss dieses Moduls kann der Lernende mit `force group`, `create mask` und `directory mask` Gruppenarbeit ermöglichen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Freigabe- und Dateirechte zusammenwirken.
  * Nach Abschluss dieses Moduls kann der Lernende Berechtigungen für ein Projekt planen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Gruppenfreigabe mit `valid users`, `force group` und Masken (`freigaben.sh`) | 4 |
| 3.2 | Nur-Lesen-Freigabe mit `write list` (`freigaben.sh`) | 3 |
| 3.3 | Freigaberecht und Dateirecht: das strengere gilt (`freigaben.sh`) | 4 |
| 3.4 | Berechtigungen für ein Beispielprojekt planen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Gruppenfreigabe (Einheit 3.1):** Führen Sie `bash freigaben.sh` aus. Erklären Sie die Konfiguration der Freigabe `projekt` und warum die Datei von `anna` die Gruppe `projekt` und die Rechte `rw-rw----` hat.
2. **Nur lesen (Einheit 3.2):** Erklären Sie Schritt 2: Warum kann `ben` nicht schreiben, `anna` schon?
3. **Freigabe und Datei (Einheit 3.3):** Erklären Sie Schritt 3 und 4: Warum scheitert der Zugriff auf `privat` bzw. `nur_root`, obwohl die Freigabe schreibbar ist?
4. **Projekt planen (Einheit 3.4):** Planen Sie die Freigaben für eine Firma mit den Gruppen `buchhaltung` und `vertrieb` und einer gemeinsamen Freigabe; geben Sie Verzeichnisrechte und Samba-Optionen an.

#### Kontrollfragen

1. Wofür dient `valid users`?
2. Was bewirkt `force group`?
3. Welche Rechte gelten, wenn die Freigabe schreibbar ist, das Verzeichnis aber `root` gehört?
4. Welche Fehlermeldung erscheint bei fehlendem Zugriff?

### Modul 4: ACLs für Freigaben

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende POSIX-ACLs für Benutzer setzen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Standard-ACL für neue Dateien erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung der Maske auf effektive Rechte erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ACLs für eine Freigabe planen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | POSIX-ACLs setzen und lesen: `setfacl`, `getfacl` (`acl.sh`) | 4 |
| 4.2 | Standard-ACL (`default`) für neue Dateien (`acl.sh`) | 3 |
| 4.3 | Wirkung über Samba und die Maske (`acl.sh`) | 3 |
| 4.4 | Windows-Sicht auf ACLs (Fachwissen, nicht ausgeführt) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **ACL setzen (Einheit 4.1):** Führen Sie `bash acl.sh` aus. Erklären Sie jede Zeile der Ausgabe von `getfacl` in Schritt 2.
2. **Zugriff (Einheit 4.2):** Erklären Sie Schritt 3: Warum kann `ben` lesen, aber nicht schreiben?
3. **Maske (Einheit 4.3):** Erklären Sie Schritt 4: Warum zeigt `getfacl` für die neue Datei `#effective:r--`, obwohl die Standard-ACL `rwx` für `anna` enthält?
4. **Planen (Einheit 4.4):** Planen Sie ACLs für ein Verzeichnis, auf das zwei Gruppen mit unterschiedlichen Rechten zugreifen.

#### Kontrollfragen

1. Was ist der Unterschied zwischen einer ACL und einer Standard-ACL?
2. Wozu dient die Maske (`mask`)?
3. Wie zeigt `getfacl` die Rechte aus der ACL?
4. Wie kann man ACLs in einer Sicherung erhalten?

### Modul 5: Samba als Domänenmitglied (Grundzüge)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die wesentlichen Parameter eines Domänenmitglieds nennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzungen für den Beitritt aufzählen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wozu die ID-Zuordnung dient.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Konfiguration für Domänenmitglied lesen und mit `testparm` prüfen (`lauf.sh`) | 4 |
| 5.2 | Beitritt: Voraussetzungen und Befehle (`beitritt.txt`, nicht ausgeführt) | 3 |
| 5.3 | ID-Zuordnung (`idmap`) im Überblick | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration (Einheit 5.1):** Führen Sie `bash lauf.sh` aus. Erklären Sie jede Zeile von `domaene_smb.conf` und die Ausgabe von `testparm`.
2. **Beitritt (Einheit 5.2):** Lesen Sie `beitritt.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.
3. **ID-Zuordnung (Einheit 5.3):** Erklären Sie, warum Samba Domänenbenutzer auf Linux-UIDs abbilden muss.

#### Kontrollfragen

1. Welche Voraussetzungen müssen für einen Beitritt erfüllt sein?
2. Was bedeutet `security = ads`?
3. Wozu dient `idmap config`?

### Modul 6: NFS-Exporte und Mount-Optionen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine `/etc/exports`-Zeile lesen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende die Befehle für Export und Einhängen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende riskante Optionen wie `no_root_squash` und `async` erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Exporte planen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Exports-Zeilen prüfen (`exports_pruefen.py`) | 4 |
| 6.2 | Server und Client: Befehle lesen (`beispiel_nfs.txt`, nicht ausgeführt) | 4 |
| 6.3 | Mount-Optionen: `hard`/`soft`, `vers`, `_netdev` im Überblick | 2 |
| 6.4 | Exporte für ein Beispielnetz planen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Exports prüfen (Einheit 6.1):** Führen Sie `python3 exports_pruefen.py` aus. Erklären Sie jede Meldung und korrigieren Sie die Zeilen.
2. **Befehle lesen (Einheit 6.2):** Lesen Sie `beispiel_nfs.txt` und erklären Sie jeden Befehl auf Server und Client. Führen Sie sie auf `fs01` und `lx01` aus.
3. **Mount-Optionen (Einheit 6.3):** Beschreiben Sie, was `hard` und `soft` bei einem Serverausfall bewirken (Handbuch lesen).
4. **Exporte planen (Einheit 6.4):** Planen Sie drei Exporte für `10.55.0.0/24` (`daten`, `info`, `backup`) mit begründeten Optionen.

#### Kontrollfragen

1. Wozu dient `exportfs -ra`?
2. Was bewirkt `no_root_squash`, und warum ist es riskant?
3. Warum ist ein Leerzeichen vor der Klammer in `exports` gefährlich?
4. Welche Option verhindert, dass beim Systemstart ohne Netz gewartet wird (Fachwissen)?

### Modul 7: Sicherheit bei Dateidiensten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Protokollversion eines Samba-Servers begrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Signierung und Verschlüsselung einschalten.
  * Nach Abschluss dieses Moduls kann der Lernende die Auswirkung auf Clients beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende ein Sicherheitskonzept formulieren.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Protokollversion begrenzen: `server min protocol` (`sicherheit.sh`) | 3 |
| 7.2 | Signierung erzwingen: `server signing` (`sicherheit.sh`) | 3 |
| 7.3 | Verschlüsselung erzwingen: `server smb encrypt` (`sicherheit.sh`) | 3 |
| 7.4 | Sicherheitskonzept für `fs01` schreiben | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration (Einheit 7.1):** Führen Sie `bash sicherheit.sh` aus. Erklären Sie die drei Parameter und die Ausgabe von `testparm`.
2. **Alte Protokolle (Einheit 7.2):** Erklären Sie Schritt 3: Warum scheitert der Client mit NT1 (SMB1)?
3. **Verschlüsselung (Einheit 7.3):** Erklären Sie Schritt 4: Warum scheitert der Zugriff mit SMB2, aber nicht mit SMB3 und Verschlüsselung?
4. **Konzept (Einheit 7.4):** Schreiben Sie ein Sicherheitskonzept für `fs01`: Protokolle, Signierung, Verschlüsselung, Benutzer, Firewall (Port 445).

#### Kontrollfragen

1. Was bewirkt `server min protocol = SMB2`?
2. Wozu dient die Signierung?
3. Welche Folge hat `server smb encrypt = required` für ältere Clients?
4. Warum nennt die Ausgabe von `testparm` `server signing = required`, obwohl `mandatory` konfiguriert war?

### Modul 8: Fehlersuche und Sicherung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationsfehler mit `testparm` finden.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlermeldungen von `smbclient` zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien samt ACLs sichern und wiederherstellen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Fehlersuche systematisch durchführen.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Konfigurationsfehler mit `testparm` finden (`fehlersuche.sh`) | 3 |
| 8.2 | Typische Fehlermeldungen lesen und zuordnen (`fehlersuche.sh`) | 4 |
| 8.3 | Sicherung mit `tar --acls --xattrs` (`fehlersuche.sh`) | 3 |
| 8.4 | Ablaufplan für Fehlersuche und Sicherung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tippfehler (Einheit 8.1):** Führen Sie `bash fehlersuche.sh` aus. Erklären Sie, wie `testparm` den Tippfehler `read onyl` meldet.
2. **Fehlermeldungen (Einheit 8.2):** Ordnen Sie die vier Meldungen aus Schritt 2 den Ursachen zu. Was fällt bei „falsches Passwort“ und „unbekannter Benutzer“ auf?
3. **Sicherung (Einheit 8.3):** Erklären Sie Schritt 3: Was zeigt, dass Besitzer und ACL erhalten blieben, und was würde ohne `--acls` fehlen?
4. **Ablaufplan (Einheit 8.4):** Schreiben Sie einen Ablaufplan „Benutzer kann nicht auf die Freigabe zugreifen“ mit Reihenfolge der Prüfungen.

#### Kontrollfragen

1. Welche Meldung erscheint bei einer unbekannten Freigabe?
2. Warum sollte der Server bei falschem und unbekanntem Benutzer dieselbe Meldung liefern (Fachwissen)?
3. Welche Dateien gehören zusätzlich zu den Daten in die Sicherung?
4. Welche Meldung zeigt, dass der Server nicht erreichbar ist?
