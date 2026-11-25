# Lehrplan: LPIC-3

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | LPIC-2 oder gleichwertige Linux-Kenntnisse (Netzwerkdienste, Speicher, Sicherheit, Skripte) |
| **Gesamtumfang** | 12 Module, 114 UE (zu 45 Minuten; 85,5 Stunden) |
| **Fokus-Technologien** | Spezialisierung auf Enterprise-Niveau (Prüfungsvorbereitung LPIC-3): Mixed Environments (Samba, Active Directory, FreeIPA, NFS), Security (Kryptografie, Host- und Netzwerksicherheit), Virtualization and Containerization sowie High Availability and Storage Clusters; Debian/Ubuntu |
| **Thematische Abgrenzung (Out of Scope)** | LPIC-1 und LPIC-2 stehen im selben Repository und werden vorausgesetzt. LPIC-3 besteht aus getrennten Spezialisierungen; dieser Kurs führt durch vier davon im Überblick und ersetzt keine Herstellerdokumentation. Cluster-Betrieb, Hypervisor-Betrieb, Windows-Clients und FreeIPA lassen sich im Labor-Container nicht ausführen und sind gekennzeichnet. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2/3) | Stunden (UE) |
|---|---|---|---|
| 1 | LPIC-3 Grundlagen und Enterprise Linux Professional Roadmap | 1 | 8 |
| 2 | LPIC-3 Mixed Environment – Samba Basics und Active Directory Domains | 1 | 10 |
| 3 | LPIC-3 Mixed Environment – Samba-Freigaben, Clients und Identity Management (FreeIPA, NFS) | 1 | 10 |
| 4 | LPIC-3 Security – Cryptography and PKI | 1 | 10 |
| 5 | LPIC-3 Security – Host Security and Access Control | 1 | 10 |
| 6 | LPIC-3 Security – Network Security and Vulnerability Assessment | 1 | 10 |
| 7 | LPIC-3 Virtualization – Full Virtualization | 1 | 10 |
| 8 | LPIC-3 Containerization and VM Provisioning | 1 | 10 |
| 9 | LPIC-3 High Availability – Cluster Architecture | 1 | 10 |
| 10 | LPIC-3 High Availability – Storage and Load Balancing | 1 | 10 |
| 11 | Enterprise Operations, Troubleshooting and Documentation | 1 | 8 |
| 12 | LPIC-3 Exam Readiness und Abschluss-Lab | 3 | 8 |
| **Gesamt** | 12 Module | 11 × Priorität 1, 0 × Priorität 2, 1 × Priorität 3 | **114** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11. **Priorität 3** (nur bei Zeit, entfällt zuerst) ist Modul 12 (Prüfungsvorbereitung und Abschluss-Labor); ohne Modul 12 verringert sich der Gesamtumfang von 114 auf 106 UE. **Abweichung vom Excel-Lehrplan:** Die Module 2 und 3 folgen den Prüfungszielen 300-300 Version 3.0 und nicht dem Excel-Blatt (siehe `lehrplan-korrekturen.md`).

### 2. Quellen

**Gelesen (lpi.org, 25.11.2026):** LPIC-3 besteht aus getrennten Spezialisierungen; aktuelle Version der Prüfungsziele 3.0. Genannt werden 300 Mixed Environments, 303 Security, 305 Virtualization and Containerization und 306 High Availability and Storage Clusters. Für 300-300 wurde die Gliederung der Prüfungsziele gelesen: Samba (Ziele 301 bis 304) sowie FreeIPA und NFS (Ziel 305); **OpenLDAP kommt in 300-300 nicht vor.** Für 303, 305 und 306 wurden nur die Themenüberschriften gelesen.

**Zuordnung (meine Annahme):** Die Module 2 und 3 folgen den Zielen von 300-300 (die Titel der Lerneinheiten dieser beiden Module sind meine eigene Einteilung des Stoffes, nicht die Nummern von LPI). Modul 4 bis 6 gehören zu 303 Security, Modul 7 und 8 zu 305 Virtualization and Containerization, Modul 9 und 10 zu 306 High Availability and Storage Clusters; Modul 1, 11 und 12 sind übergreifend.

**Nicht gelesen:** Die Einzelziele und Gewichtungen von 303, 305 und 306 sowie das Prüfungsformat (Dauer, Anzahl der Fragen, Voraussetzungen). Aussagen zu Befehlen, Dateien und Pfaden sind Fachwissen, soweit sie nicht im Container ausgeführt wurden, und **nicht bestätigt**. Prüfungsfragen werden nicht wiedergegeben. **Getestet mit (Ubuntu 24.04.5, Cloud-Container, root, ohne systemd als init):** Samba 4.19.5, OpenSSL 3.0.13, GnuPG 2.4.4, AIDE 0.18.6, Suricata 7.0.3, wireguard-tools 1.0.20210914, OpenVPN 2.6.19, qemu-img 8.2.2, libvirt 10.0.0, Podman 4.9.3, Docker-Client 29.9.2 (ohne Dienst), HAProxy 2.8.30, Keepalived 2.2.8, Corosync 3.1.7, Pacemaker 2.1.6, DRBD-Werkzeuge 9.22.0, ansible-core 2.22.0.

### 3. Labor-Setup & Rahmenbedingungen

**Labor laut Lehrplan:** Eine Linux-Server-VM (Debian oder Ubuntu Server) und eine Linux-Client-VM auf einem privaten Hyper-V-Switch ohne Verbindung zum Heimnetz; Snapshots vor jeder Übung. Das Hyper-V-Labor wurde **nicht** aufgebaut. Für echte Gast-VMs (KVM) wäre in der Hyper-V-VM verschachtelte Virtualisierung nötig; das wurde nicht geprüft.

**Skripte:** Alle Übungsskripte laufen unter Linux als root im Sandkasten `/tmp/lpic3` mit eigenen Konfigurationsdateien, Ports über 1024 (z. B. SMB 4456 und 4457, TLS-Test 8443, HAProxy 8100) und eigenen Netzwerk-Namensräumen (u. a. `dct`, `mbt`, `ns6s`, `ha9`, `ka1`, `ka2`), räumen am Ende auf und legen nur kurzlebige Testkonten an. **Nie auf einem Produktivsystem ausführen.**

**Nicht ausgeführt, weil im Container nicht möglich:** FreeIPA, Domänenbeitritt mit `net ads` und Kerberos-Tickets (`kinit`, `klist` fehlen), Windows-Clients und Gruppenrichtlinien, Einhängen von CIFS und NFS, LUKS-Öffnen (kein Device-Mapper), ACME, WireGuard-Tunnel, AppArmor und SELinux im Betrieb, Audit-Regeln, cgroup-Grenzen, Xen, Start von KVM/QEMU-VMs, Docker-Dienst, LXC, Kubernetes, Betrieb von Pacemaker, DRBD und geclusterten Dateisystemen, iSCSI-Initiator, Multipath im Betrieb.

## B. Detaillierter Modulaufbau

### Modul 1: LPIC-3 Grundlagen und Enterprise Linux Professional Roadmap

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rolle von LPIC-3 und die Spezialisierungen benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Spezialisierungen den Modulen dieses Kurses zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Werkzeuge je Spezialisierung im Labor inventarisieren und Versionen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungen mit einem festen Protokoll dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationen prüfen, bevor man einen Dienst neu lädt.
* **Voraussetzungen:** LPIC-2 oder gleichwertige Kenntnisse.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | LPIC-3 Rolle | 1 |
| 1.2 | Spezialisierungen | 1 |
| 1.3 | Voraussetzungen | 1 |
| 1.4 | Exam Format | 1 |
| 1.5 | Enterprise Lab | 1 |
| 1.6 | Distribution Neutrality | 1 |
| 1.7 | Betriebsverantwortung | 1 |
| 1.8 | Grundlagen-Troubleshooting | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rolle und Spezialisierungen (Einheiten 1.1 und 1.2):** Führe `bash grundlagen.sh` aus. Lies in Schritt 1 die Tabelle der Spezialisierungen und ordne jeder ein Modul dieses Kurses zu. Beschreibe in vier Sätzen, wodurch sich LPIC-3 von LPIC-2 unterscheidet.
2. **Voraussetzungen und Prüfungsformat (Einheiten 1.3 und 1.4):** Lies auf lpi.org die Seite zu LPIC-3 und notiere in drei Sätzen die Voraussetzungen und das Prüfungsformat der Spezialisierung, die dich interessiert. Schreibe das Datum des Lesens dazu. Zu diesem Punkt gibt es in diesem Kurs keine Ausgabe, weil die Einzelheiten nicht gelesen wurden.
3. **Labor und Distributionsneutralität (Einheiten 1.5 und 1.6):** Lies in Schritt 2 die Werkzeuge je Spezialisierung und in Schritt 3 ihre Versionen. Notiere, welche Werkzeuge in deiner VM noch zu installieren wären, und nenne zwei Befehle, die sich zwischen Debian und anderen Distributionen unterscheiden können.
4. **Betriebsverantwortung und Fehlersuche (Einheiten 1.7 und 1.8):** Erkläre in Schritt 4 die Felder des Änderungsprotokolls. Lies in Schritt 5 die Meldung von `haproxy -c` für die kaputte und die gute Datei und beschreibe das Vorgehen „erst prüfen, dann neu laden“ in vier Schritten.

#### Kontrollfragen

1. Welche vier Spezialisierungen kennt dieser Kurs und welche Module gehören dazu?
2. Wodurch zeigt `haproxy -c` einen Fehler an?
3. Warum steht im Änderungsprotokoll ein Feld „Rollback“?
4. Welche Felder hat das Änderungsprotokoll im Beispiel?

### Modul 2: LPIC-3 Mixed Environment – Samba Basics und Active Directory Domains

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Programme und Rollen von Samba unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine Active-Directory-Domäne mit Samba provisionieren und die Konfiguration lesen.
  * Nach Abschluss dieses Moduls kann der Lernende SRV-Einträge eines Domänencontrollers prüfen und einen fehlenden A-Eintrag ergänzen.
  * Nach Abschluss dieses Moduls kann der Lernende Benutzer, Gruppen und die Kennwortrichtlinie mit `samba-tool` verwalten.
  * Nach Abschluss dieses Moduls kann der Lernende einen Linux-Rechner mit `net rpc join` in die Domäne aufnehmen und typische Fehler eingrenzen.
* **Voraussetzungen:** Modul 1; LPIC-2 Modul 9 (Samba-Grundlagen) und Modul 7 (DNS).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Samba-Architektur und Rollen | 1,25 |
| 2.2 | AD-Domäne anlegen (Provisioning) | 1,25 |
| 2.3 | DNS und SRV-Records | 1,25 |
| 2.4 | Benutzer, Gruppen, Kennwortrichtlinien | 1,25 |
| 2.5 | Kerberos und Zeit | 1,25 |
| 2.6 | Domänenbeitritt eines Linux-Mitglieds | 1,25 |
| 2.7 | Zugriff und Sicherheit | 1,25 |
| 2.8 | Fehlersuche | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Architektur und Provisioning (Einheiten 2.1 und 2.2):** Führe `bash samba-ad.sh` aus. Lies in Schritt 1 die Programme und die Unterbefehle von `samba-tool domain`. Lies in Schritt 2 bis 4 die Daten der angelegten Domäne (Rolle, Rechnername, NetBIOS-Name, DNS-Name), die Dateien unter `private` und die Ports des Domänencontrollers und erkläre, wofür DNS, Kerberos (88) und LDAP (389) dort gebraucht werden.
2. **DNS und Benutzerverwaltung (Einheiten 2.3 und 2.4):** Lies in Schritt 5 die SRV-Einträge für LDAP und Kerberos und erkläre, warum der A-Eintrag von `dc1` erst ergänzt werden musste. Lies in Schritt 6 die angelegten Benutzer, die Gruppe `team`, die Kennwortrichtlinie und die Funktionsebene.
3. **Kerberos, Anmeldung und Domänenbeitritt (Einheiten 2.5 und 2.6):** Lies in Schritt 7 die Kerberos-Einstellungen (`default_realm`, `dns_lookup_kdc`) und die SMB-Anmeldung eines Domänenbenutzers; erkläre, warum `kinit` fehlt und was das für die Übung bedeutet. Lies in Schritt 8 den Beitritt des Mitglieds mit `net rpc join` und die Liste der Computerkonten.
4. **Zugriff und Fehlersuche (Einheiten 2.7 und 2.8):** Lies in Schritt 9 die drei Fehlerfälle (falsches Kennwort, Datenbankprüfung, falsche Namensauflösung) und beschreibe zu jedem die Ursache und den nächsten Prüfschritt. Erkläre in eigenen Worten, wozu die SMB-Signierung dient (siehe Modul 3, Schritt 2: `server signing = required`).

#### Kontrollfragen

1. Welche Rolle meldet `testparm` für den Domänencontroller?
2. Welche Dienste lauschen auf dem Domänencontroller unterhalb von Port 1024 und auf 3268?
3. Was lieferte die Abfrage des SRV-Eintrags `_ldap._tcp.lab.example`?
4. Welche Kennwortrichtlinie ist im Labor eingestellt?
5. Welche Fehlermeldung liefert ein falsches Kennwort?

### Modul 3: LPIC-3 Mixed Environment – Samba-Freigaben, Clients und Identity Management (FreeIPA, NFS)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Samba-Freigabe mit POSIX-Rechten und ACLs einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende VFS-Module (Papierkorb, Sperrliste) und Freigabeoptionen anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende als Linux-Client auf eine Freigabe zugreifen und Erweiterte Attribute für NT-ACLs lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Bestandteile von FreeIPA und die Vertrauensstellung zu Active Directory beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende NFS-Exporte mit Kerberos-Sicherheit konfigurieren und Fehler bei Anmeldung und Freigabe eingrenzen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Freigaben und Rechte (POSIX und NT-ACLs) | 1,25 |
| 3.2 | VFS-Module und Freigabeoptionen | 1,25 |
| 3.3 | Linux-Clients | 1,25 |
| 3.4 | Windows-Clients und Gruppenrichtlinien | 1,25 |
| 3.5 | FreeIPA: Architektur | 1,25 |
| 3.6 | FreeIPA: Verwaltung und AD-Vertrauensstellung | 1,25 |
| 3.7 | NFS mit Kerberos | 1,25 |
| 3.8 | Fehlersuche | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Freigabe, Rechte und VFS-Module (Einheiten 3.1 und 3.2):** Führe `bash freigaben-identity.sh` aus. Lies in Schritt 1 die Rechte des Freigabeverzeichnisses und die ACL-Einträge für `nobody`. Lies in Schritt 2 die Optionen `vfs objects`, `veto files` und `server signing` und erkläre, was der Papierkorb und die Sperrliste bewirken.
2. **Linux- und Windows-Clients (Einheiten 3.3 und 3.4):** Lies in Schritt 3 die Erweiterten Attribute (`security.NTACL`) und den Zugriff mit `smbclient`; erkläre, warum `mount.cifs` fehlt. Lies in Schritt 4 den Hinweis zu Windows-Clients und beschreibe in drei Sätzen die Rolle von SYSVOL für Gruppenrichtlinien (nicht ausgeführt).
3. **FreeIPA (Einheiten 3.5 und 3.6):** Lies in Schritt 5 und 6 die Bestandteile von FreeIPA und die Beispielbefehle für Benutzer, Gruppe, HBAC-Regel und Vertrauensstellung. Alles ist **nicht ausgeführt**; erkläre zu jedem Befehl, was er bewirken würde, und nenne, welche Werkzeuge im Labor fehlen.
4. **NFS und Fehlersuche (Einheiten 3.7 und 3.8):** Lies in Schritt 7 die Exportoption `sec=krb5p` und erkläre, warum das Einhängen nicht ausgeführt wurde. Lies in Schritt 8 die drei Fehlerbilder (falsches Kennwort, unbekannte Freigabe, unbekannter Parameter in der Konfiguration) und ordne ihnen je einen Prüfschritt zu.

#### Kontrollfragen

1. Welche Sicherheitsoption für NFS wurde im Beispiel exportiert?
2. Welche Wirkung haben `veto files = /*.tmp/` und das Modul `recycle`?
3. Wo speichert Samba mit `acl_xattr` die NT-ACL?
4. Welche Fehlermeldung ergibt eine nicht vorhandene Freigabe?
5. Aus welchen Bestandteilen besteht FreeIPA laut Fachwissen?

### Modul 4: LPIC-3 Security – Cryptography and PKI

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer PKI mit Wurzel- und Zwischen-CA beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende mit OpenSSL ein Serverzertifikat ausstellen, prüfen, widerrufen und eine Sperrliste erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende TLS-Verbindungen mit `s_client` und `s_server` testen.
  * Nach Abschluss dieses Moduls kann der Lernende Schlüssel mit GnuPG erzeugen, Dateien signieren und verschlüsseln.
  * Nach Abschluss dieses Moduls kann der Lernende typische Zertifikatsfehler (Kette, Ablauf, Hostname, Schlüsselpaar) eingrenzen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | X.509 and PKI | 1,25 |
| 4.2 | OpenSSL CA Operations | 1,25 |
| 4.3 | TLS for Services | 1,25 |
| 4.4 | GPG and File Encryption | 1,25 |
| 4.5 | Encrypted Filesystems | 1,25 |
| 4.6 | DNS and Cryptography | 1,25 |
| 4.7 | ACME and Automation | 1,25 |
| 4.8 | Crypto Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **PKI und OpenSSL-CA (Einheiten 4.1 und 4.2):** Führe `bash krypto-pki.sh` aus. Lies in Schritt 1 den Aufbau von Wurzel- und Zwischen-CA und in Schritt 2 das Serverzertifikat (Subject, Aussteller, Schlüsselverwendung, Subject Alternative Name). Erkläre, warum die Prüfung `openssl verify` mit `-untrusted` die Zwischen-CA angibt, und was das Widerrufen und die Sperrliste bewirken.
2. **TLS und GnuPG (Einheiten 4.3 und 4.4):** Lies in Schritt 3 die Ergebnisse der TLS-Verbindung (Protokoll, Verschlüsselung, Rückgabecode) für den richtigen und den falschen Hostnamen. Lies in Schritt 4, wie ein Schlüssel erzeugt, eine Signatur geprüft und eine Datei entschlüsselt wird.
3. **Verschlüsselte Dateisysteme und DNS (Einheiten 4.5 und 4.6):** Lies in Schritt 5, warum `luksFormat` gelingt, das Öffnen aber nicht, und erkläre die Rolle des Device-Mappers. Lies in Schritt 6, wie der TLSA-Datensatz (DANE) aus dem Zertifikat berechnet wird, und was der DNSSEC-Schlüssel erzeugt.
4. **ACME und Fehlersuche (Einheiten 4.7 und 4.8):** Beschreibe in Schritt 7 den Ablauf von ACME laut Fachwissen (nicht ausgeführt). Lies in Schritt 8 die vier Fehlerbilder (Kette, Ablauf, Hostname, Schlüsselpaar) und nenne zu jedem den Prüfbefehl.

#### Kontrollfragen

1. Welchen Fehler meldet `openssl verify` bei einer CRL-Prüfung eines widerrufenen Zertifikats?
2. Welcher Rückgabecode erscheint bei falschem Hostnamen in `s_client`?
3. Warum scheitert `cryptsetup open` im Container?
4. Was bedeutet `error 20 … unable to get local issuer certificate`?
5. Wie lang ist ein TLSA-Datensatz „3 1 1“?

### Modul 5: LPIC-3 Security – Host Security and Access Control

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Kernel-Parameter und Rechte eines Hosts auf Härtung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Integrität mit Prüfsummen und AIDE kontrollieren.
  * Nach Abschluss dieses Moduls kann der Lernende Audit-Ereignisse mit `ausearch` und `aureport` auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende ulimit, prlimit und cgroups einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende DAC (Rechte, ACLs, Attribute, Capabilities) und MAC (AppArmor, SELinux) unterscheiden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Host Hardening | 1,25 |
| 5.2 | Secure Boot and Integrity | 1,25 |
| 5.3 | Host Intrusion Detection | 1,25 |
| 5.4 | Audit Framework | 1,25 |
| 5.5 | Resource Control | 1,25 |
| 5.6 | Discretionary Access Control | 1,25 |
| 5.7 | Mandatory Access Control | 1,25 |
| 5.8 | Host Security Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Härtung und Integrität (Einheiten 5.1 und 5.2):** Führe `bash host-sicherheit.sh` aus. Lies in Schritt 1 die Kernel-Parameter, die Zahl der SUID-Programme und die Prüfung auf Konten ohne Kennwort. Erkläre in Schritt 2, warum Secure Boot und IMA im Container nicht prüfbar sind, und was `sha256sum -c` bei einer veränderten Datei meldet.
2. **AIDE und Audit (Einheiten 5.3 und 5.4):** Lies in Schritt 3 die drei AIDE-Läufe (Initialisierung, ohne Änderung, mit Änderung) und erkläre die Abschnitte „Added“, „Removed“ und „Changed“. Lies in Schritt 4 die Auswertung der Beispieldatei mit `ausearch` und `aureport` und erkläre, warum `auditctl -s` hier `enabled 0` meldet.
3. **Ressourcen und DAC (Einheiten 5.5 und 5.6):** Lies in Schritt 5 die Werte von `ulimit` und `prlimit` und die cgroup-Version. Lies in Schritt 6 die Wirkung von `chmod`, `setfacl`, `chattr +i` und `setcap` und erkläre, warum das Anhängen an die unveränderliche Datei scheitert.
4. **MAC und Fehlersuche (Einheiten 5.7 und 5.8):** Lies in Schritt 7 die Syntaxprüfung des AppArmor-Profils und erkläre, warum AppArmor und SELinux im Container nicht aktiv sind. Lies in Schritt 8 die drei Fehlerbilder (AIDE-Gruppe, AppArmor-Profil, `sysctl`) und nenne zu jedem den Prüfschritt.

#### Kontrollfragen

1. Welche Konsequenz hat `chattr +i` für eine Datei?
2. Was zeigt der AIDE-Lauf nach einer Änderung im überwachten Verzeichnis?
3. Wie viele SUID-Programme liegen in `/usr/bin` und `/usr/sbin` im Labor?
4. Warum meldet `aa-status` „apparmor not present“?

### Modul 6: LPIC-3 Security – Network Security and Vulnerability Assessment

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Kernel-Parameter und lauschende Dienste auf Härtung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Paketfilter mit Standard-Verwerfen und Ausnahmen mit nftables aufbauen und testen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Netzwerk-IDS (Suricata) mit einer eigenen Regel auf einen Mitschnitt anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende WireGuard-Schlüssel und Konfiguration prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Angriffsspuren erkennen und einen Portscan mit nmap lesen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Network Hardening | 1,25 |
| 6.2 | Packet Filtering | 1,25 |
| 6.3 | Network IDS | 1,25 |
| 6.4 | VPN | 1,25 |
| 6.5 | Secure Routing | 1,25 |
| 6.6 | Common Threats | 1,25 |
| 6.7 | Vulnerability Assessment and Pentest | 1,25 |
| 6.8 | Network Security Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Härtung und Paketfilter (Einheiten 6.1 und 6.2):** Führe `bash netz-sicherheit.sh` aus. Lies in Schritt 1 die Kernel-Parameter und die lauschenden Dienste. Lies in Schritt 2 die Regeln des Paketfilters und erkläre, warum Port 8080 antwortet (200), Port 8081 in eine Zeitüberschreitung läuft und ein geschlossener Port eine Ablehnung liefert.
2. **IDS und VPN (Einheiten 6.3 und 6.4):** Lies in Schritt 3 die Prüfung der Suricata-Konfiguration, den Alarm der eigenen Regel und die Ereignistypen. Lies in Schritt 4, warum `ip link add wg0 type wireguard` scheitert, und erkläre die Länge des öffentlichen Schlüssels und den Inhalt von `wg-quick strip`.
3. **Routing und Angriffe (Einheiten 6.5 und 6.6):** Lies in Schritt 5 `ip_forward`, `rp_filter` und die Anti-Spoofing-Regel. Lies in Schritt 6 die Auswertung der Anmeldeversuche mit `fail2ban-regex` und der Quelladressen.
4. **Schwachstellenanalyse und Fehlersuche (Einheiten 6.7 und 6.8):** Lies in Schritt 7 die Ergebnisse von `nmap` (Port und erkannter Dienst) und erkläre den Unterschied zwischen Host-Erkennung und Portscan. Lies in Schritt 8 die vier Fehlerbilder und nenne zu jedem den Prüfschritt.

#### Kontrollfragen

1. Welche Rückgabewerte hat `curl` bei gefiltertem und bei geschlossenem Port?
2. Welche Richtlinie hat die Eingangskette im Beispiel und welche Ausnahmen gibt es?
3. Wie viele Alarme meldet Suricata für den Mitschnitt und welche Regel löst aus?
4. Welche Wirkung hat die Option `rp_filter = 1`?
5. Wie viele Zeilen der Beispieldatei trifft die Fail2ban-Regel?

### Modul 7: LPIC-3 Virtualization – Full Virtualization

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für Hardware-Virtualisierung auf einem System prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Xen, KVM und QEMU gegeneinander abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende mit libvirt Domänen definieren, starten, anhalten und löschen (Testtreiber).
  * Nach Abschluss dieses Moduls kann der Lernende VM-Abbilder mit `qemu-img` anlegen, konvertieren, vergrößern und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Bridge und TAP-Gerät als Netzwerkanschluss einer VM aufbauen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Virtualization Concepts | 1,25 |
| 7.2 | Xen | 1,25 |
| 7.3 | KVM and QEMU | 1,25 |
| 7.4 | libvirt | 1,25 |
| 7.5 | VM Disk Images | 1,25 |
| 7.6 | VM Networking | 1,25 |
| 7.7 | VM Management | 1,25 |
| 7.8 | Virtualization Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konzepte und Xen (Einheiten 7.1 und 7.2):** Führe `bash virtualisierung.sh` aus. Lies in Schritt 1 die Prüfung auf `vmx` oder `svm`, den Hypervisor-Hersteller und `/dev/kvm`. Lies in Schritt 2 die Felder der Xen-Beispieldatei `domu.cfg` und erkläre, warum `xl` fehlt.
2. **KVM, QEMU und libvirt (Einheiten 7.3 und 7.4):** Lies in Schritt 3, welche QEMU-Werkzeuge vorhanden sind und warum der Beispielbefehl mit `-enable-kvm` nicht ausgeführt wurde. Lies in Schritt 4 die Verbindung zum Testtreiber, die Domänen- und Netzwerkliste und die Prüfung der XML-Datei.
3. **Abbilder und Netzwerk (Einheiten 7.5 und 7.6):** Lies in Schritt 5 die Befehle für Basis-Abbild, Overlay, Konvertierung, Vergrößerung und Schnappschuss und erkläre den Unterschied zwischen scheinbarer und belegter Größe des Rohabbilds. Lies in Schritt 6 den Aufbau von Bridge und TAP-Gerät.
4. **VM-Verwaltung und Fehlersuche (Einheiten 7.7 und 7.8):** Lies in Schritt 7 den Lebenszyklus einer Domäne mit `virsh` (definieren, starten, anhalten, fortsetzen, Autostart, beenden, entfernen). Lies in Schritt 8 die vier Fehlerbilder und nenne zu jedem den Prüfschritt.

#### Kontrollfragen

1. Woran erkennt man im Labor, dass keine Hardware-Virtualisierung nutzbar ist?
2. Was ist der Vorteil eines Overlay-Abbilds mit Backing File?
3. Welche Meldung erscheint, wenn das Basisabbild eines Overlays fehlt?
4. Was meldet `virsh -c qemu:///system list` im Container?

### Modul 8: LPIC-3 Containerization and VM Provisioning

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Namensräume als Grundlage von Containern erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen einfachen Container aus Wurzelverzeichnis, chroot und Namensräumen bauen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abbild mit Buildah bauen und mit Podman ausführen.
  * Nach Abschluss dieses Moduls kann der Lernende OCI-Abbilder untersuchen und exportieren.
  * Nach Abschluss dieses Moduls kann der Lernende Systeme mit cloud-init und Ansible reproduzierbar einrichten.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Container Concepts | 1,25 |
| 8.2 | LXC | 1,25 |
| 8.3 | Docker | 1,25 |
| 8.4 | OCI and Images | 1,25 |
| 8.5 | Container Networking and Storage | 1,25 |
| 8.6 | Orchestration Concepts | 1,25 |
| 8.7 | Provisioning Tools | 1,25 |
| 8.8 | Container Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Namensräume und LXC (Einheiten 8.1 und 8.2):** Führe `bash container-provisionierung.sh` aus. Lies in Schritt 1 die Namensräume und erkläre, warum Rechnername und Prozessliste im neuen Namensraum eigene Werte haben. Lies in Schritt 2, wie ein Container aus Wurzelverzeichnis, `chroot` und Namensräumen entsteht, und warum LXC nicht ausgeführt wurde.
2. **Docker, Podman und OCI (Einheiten 8.3 und 8.4):** Lies in Schritt 3, warum `docker info` scheitert und das Abbild stattdessen mit Buildah und einer Containerfile gebaut wird. Lies in Schritt 4 die Metadaten des Abbilds (Architektur, Schichten) und den Aufbau des OCI-Archivs.
3. **Netzwerk, Speicher und Orchestrierung (Einheiten 8.5 und 8.6):** Lies in Schritt 5 die Wirkung von `--network=none` und des Bind-Mounts mit `:ro`. Lies in Schritt 6, was die YAML-Beschreibung eines Pods enthält, und erkläre, warum ohne `kubectl` kein Cluster geprüft wurde.
4. **Provisionierung und Fehlersuche (Einheiten 8.7 und 8.8):** Lies in Schritt 7 die Prüfung von cloud-init und den Ablauf von Ansible beim ersten und zweiten Lauf und erkläre Idempotenz. Lies in Schritt 8 die fünf Fehlerbilder und nenne zu jedem den Prüfschritt.

#### Kontrollfragen

1. Wie viele Prozesse sieht eine Shell im neuen PID-Namensraum?
2. Warum zeigt Ansible beim zweiten Lauf `changed=0`?
3. Was bewirkt `-v …:/daten:ro` bei `podman run`?
4. Welche Dateien enthält ein OCI-Archiv?

### Modul 9: LPIC-3 High Availability – Cluster Architecture

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Verfügbarkeitsziele in Ausfallzeit umrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Corosync und Pacemaker als Bausteine eines Clusters einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Corosync-Konfiguration schreiben und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Pacemaker-CIB mit Ressourcen und Einschränkungen prüfen und simulieren.
  * Nach Abschluss dieses Moduls kann der Lernende Quorum, Fencing und Ressourcen-Agenten erklären.
* **Voraussetzungen:** Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | HA Concepts | 1,25 |
| 9.2 | Cluster Architecture | 1,25 |
| 9.3 | Corosync | 1,25 |
| 9.4 | Pacemaker | 1,25 |
| 9.5 | Quorum | 1,25 |
| 9.6 | STONITH/Fencing | 1,25 |
| 9.7 | Resource Agents | 1,25 |
| 9.8 | Cluster Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konzepte und Architektur (Einheiten 9.1 und 9.2):** Führe `bash ha-cluster.sh` aus. Lies in Schritt 1 die Ausfallzeit je Jahr für 99 bis 99,999 Prozent. Lies in Schritt 2 die Werkzeuge und Versionen und beschreibe in drei Sätzen die Rollen von Corosync und Pacemaker.
2. **Corosync und Pacemaker (Einheiten 9.3 und 9.4):** Lies in Schritt 3 den Konfigurationstest, die Meldung bei fremdem Rechnernamen und die Größe des Authentifizierungsschlüssels. Lies in Schritt 4 `crm_verify`, den Plan von `crm_simulate` und die Allokationswerte der Ressourcen.
3. **Quorum und Fencing (Einheiten 9.5 und 9.6):** Lies in Schritt 5 die Quorum-Tabelle und erkläre `two_node`. Lies in Schritt 6 die Geräte von `stonith_admin` und warum `crm_verify` ohne Fencing-Geräte den Rückgabewert 78 liefert.
4. **Ressourcen-Agenten und Fehlersuche (Einheiten 9.7 und 9.8):** Lies in Schritt 7 die Rückgabewerte des Dummy-Agenten für `monitor`, `start` und `stop` und die Parameter von `IPaddr2`. Lies in Schritt 8 die Fehlerbilder und erkläre, warum `crm_verify` einen unbekannten Agenten nicht meldet.

#### Kontrollfragen

1. Wie viel Ausfallzeit im Jahr erlaubt eine Verfügbarkeit von 99,99 Prozent?
2. Wie viele Stimmen braucht ein Cluster mit 5 Knoten für das Quorum und wie viele Ausfälle verträgt er?
3. Welche Rückgabewerte liefert der Dummy-Agent für `monitor` vor dem Start und danach?
4. Warum ist Fencing in Produktionsclustern Pflicht?

### Modul 10: LPIC-3 High Availability – Storage and Load Balancing

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine DRBD-Ressource beschreiben und die Konfiguration einlesen.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für geclusterte Dateisysteme nennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein iSCSI-Ziel mit tgt bereitstellen und lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Multipath-Voreinstellungen deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Lastverteilung mit HAProxy und virtuelle Adressen mit keepalived einrichten und testen.
* **Voraussetzungen:** Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | DRBD | 1,25 |
| 10.2 | Clustered Filesystems | 1,25 |
| 10.3 | iSCSI | 1,25 |
| 10.4 | Multipath | 1,25 |
| 10.5 | Load Balancing Concepts | 1,25 |
| 10.6 | HAProxy | 1,25 |
| 10.7 | Keepalived and VRRP | 1,25 |
| 10.8 | HA Storage/LB Troubleshooting | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **DRBD und geclusterte Dateisysteme (Einheiten 10.1 und 10.2):** Führe `bash ha-speicher-lastverteilung.sh` aus. Lies in Schritt 1 die DRBD-Konfiguration (Gerät, Adressen, Protokoll) und erkläre, warum `drbdadm up` scheitert. Lies in Schritt 2, warum GFS2 und OCFS2 im Labor nicht möglich sind.
2. **iSCSI und Multipath (Einheiten 10.3 und 10.4):** Lies in Schritt 3 den Aufbau von Ziel und LUN mit `tgtadm` und erkläre, warum der Initiator nicht ausgeführt wurde. Lies in Schritt 4 die Voreinstellungen von `multipath -t` und den Rückgabewert von `multipath -ll`.
3. **Lastverteilung und HAProxy (Einheiten 10.5 und 10.6):** Lies in Schritt 5 die Verteilung nach Round Robin und nenne zwei weitere Verfahren. Lies in Schritt 6 die Antworten von HAProxy, den Zustand der Backends nach dem Ausfall und die Antwort bei Ausfall beider.
4. **keepalived und Fehlersuche (Einheiten 10.7 und 10.8):** Lies in Schritt 7, welcher Knoten die virtuelle Adresse vor und nach dem Ausfall hält. Lies in Schritt 8 die vier Fehlerbilder und nenne zu jedem den Prüfschritt.

#### Kontrollfragen

1. Warum scheitert `drbdadm up r0` im Container?
2. Welche Antworten liefert HAProxy bei Round Robin und was bei Ausfall beider Server?
3. Wie unterscheiden sich Ziel und Initiator bei iSCSI?
4. Welcher Knoten hält die virtuelle Adresse nach dem Ausfall von `ka1`?

### Modul 11: Enterprise Operations, Troubleshooting and Documentation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Dienste mit Prüfskripten (Nagios-Rückgabewerte) und Prometheus-Regeln überwachen.
  * Nach Abschluss dieses Moduls kann der Lernende Protokolle zentral sammeln und rotieren.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationen mit Ansible und Git verwalten und Änderungen zurücknehmen.
  * Nach Abschluss dieses Moduls kann der Lernende Daten mit restic sichern, prüfen und wiederherstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Störungen anhand von Protokollen als Zeitleiste darstellen und dokumentieren.
* **Voraussetzungen:** Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Monitoring | 1 |
| 11.2 | Central Logging | 1 |
| 11.3 | Automation | 1 |
| 11.4 | Change Control | 1 |
| 11.5 | Backup and Recovery | 1 |
| 11.6 | Incident Handling | 1 |
| 11.7 | Documentation | 1 |
| 11.8 | Operations Troubleshooting | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Monitoring und Logging (Einheiten 11.1 und 11.2):** Führe `bash betrieb.sh` aus. Lies in Schritt 1 die vier Rückgabewerte des Prüfskripts (OK, WARNING, CRITICAL, UNKNOWN) und die Prüfung der Prometheus-Dateien. Lies in Schritt 2, wie eine Meldung vom Client zum Server weitergeleitet wird, und erkläre die Rotation.
2. **Automatisierung und Änderungsverwaltung (Einheiten 11.3 und 11.4):** Lies in Schritt 3 das Inventar und den Trockenlauf mit `--check --diff` und erkläre `changed` beim ersten und zweiten Lauf. Lies in Schritt 4 den Ablauf von Änderung, Commit und `git revert`.
3. **Sicherung und Störungen (Einheiten 11.5 und 11.6):** Lies in Schritt 5 den Ablauf von `restic` (Initialisieren, Sichern, Prüfen, Wiederherstellen) und erkläre, warum der zweite Lauf nur „1 changed“ meldet. Lies in Schritt 6 die Zeitleiste und die Dauer der Störung.
4. **Dokumentation und Fehlersuche (Einheiten 11.7 und 11.8):** Lies in Schritt 7 die Prüfung der Abschnitte des Betriebshandbuchs und nenne den fehlenden. Lies in Schritt 8 die vier Fehlerbilder und nenne zu jedem den Prüfschritt.

#### Kontrollfragen

1. Welche Rückgabewerte nutzen Nagios-kompatible Prüfskripte?
2. Wie lange dauerte die Störung im Beispielprotokoll?
3. Was bewirkt `git revert` im Unterschied zu `git reset`?
4. Welche Abschnitte hat das Beispielhandbuch und welcher fehlt?
5. Welche Meldung zeigt ein beschädigtes restic-Repository?

### Modul 12: LPIC-3 Exam Readiness und Abschluss-Lab

* **Priorität:** 3 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Spezialisierung nach Berufsziel auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende die Werkzeuge der Module 2 bis 11 im Labor prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationen vor dem Neuladen mit einem Befehl je Dienst prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende drei Szenarien (Mixed, Security, Virtualisierung und HA) mit Werkzeugen des Kurses durchspielen.
  * Nach Abschluss dieses Moduls kann der Lernende einen eigenen Lernplan und eine Prüfungsstrategie festlegen.
* **Voraussetzungen:** Module 2 bis 11 (soweit gewählt).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Specialty Selection | 1 |
| 12.2 | Objective Review | 1 |
| 12.3 | Command Drill | 1 |
| 12.4 | Scenario Lab Mixed Environment | 1 |
| 12.5 | Scenario Lab Security | 1 |
| 12.6 | Scenario Lab Virtualization/HA | 1 |
| 12.7 | Exam Strategy | 1 |
| 12.8 | Career Roadmap | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auswahl und Zielübersicht (Einheiten 12.1 und 12.2):** Führe `bash abschluss.sh` aus. Lies in Schritt 1 die Prüfung der Werkzeuge je Modul und wähle eine Spezialisierung nach deinem Berufsziel. Lies in Schritt 2 die Themen je Spezialisierung und markiere, welche du sicher beherrschst.
2. **Prüfbefehle und Szenario Mixed (Einheiten 12.3 und 12.4):** Lies in Schritt 3 die Prüfbefehle je Dienst. Lies in Schritt 4 das Szenario Mixed Environment (Dateiserver mit Gruppenzugriff) und erkläre, warum ein fremdes Konto `NT_STATUS_ACCESS_DENIED` erhält.
3. **Szenarien Security und Virtualisierung/HA (Einheiten 12.5 und 12.6):** Lies in Schritt 5 das Szenario Security (Zertifikat ausstellen, prüfen, Datei überwachen) und in Schritt 6 das Szenario Virtualisierung und HA (Abbild, Domäne, CIB, Plan). Beschreibe, welche Prüfungen jeweils gelaufen sind.
4. **Strategie und Lernplan (Einheiten 12.7 und 12.8):** Rechne in Schritt 7 den Zeitplan nach (die Zahlen sind selbst gewählt, keine Vorgaben von LPI) und lege eigene Regeln fest. Lies in Schritt 8 den Lernplan und ergänze ihn um dein eigenes Fehlerbild je Modul.

#### Kontrollfragen

1. Wie lange hat man bei 40 Aufgaben in 120 Minuten je Aufgabe?
2. Welche Prüfung gehört zum Szenario Mixed Environment und welche Rolle meldet `testparm`?
3. Welcher Befehl prüft eine Cluster-Konfiguration vor dem Einspielen?
4. Warum ist Modul 12 Priorität 3?
