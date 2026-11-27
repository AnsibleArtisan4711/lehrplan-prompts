# Lehrplan: Cisco CCNA

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Grundkenntnisse in Windows oder Linux (Befehlszeile, Netzwerkeinstellungen eines Endgeräts); keine Cisco-Vorkenntnisse nötig |
| **Gesamtumfang** | 12 Module, 106 UE (zu 45 Minuten; 79,5 Stunden) |
| **Fokus-Technologien** | Netzwerkgrundlagen, Ethernet-Switching, VLANs und Trunks, Spanning Tree und EtherChannel, IPv4/IPv6-Adressierung, statisches Routing und OSPF, IP-Dienste (DHCP, DNS, NAT, NTP, FHRP), WLAN, Layer-2- und Geräte-Sicherheit mit ACLs, Betrieb mit SNMP und Syslog, Overlay und Virtualisierung, Automatisierung und Einsatz von KI im Netzwerkbetrieb (Prüfungsvorbereitung CCNA 200-301, Prüfungsthemen Version 2.0) |
| **Thematische Abgrenzung (Out of Scope)** | Der Kurs ersetzt weder die Cisco-Dokumentation noch ein Cisco-Gerät. **Es läuft weder Cisco IOS noch Packet Tracer:** Die Übungen zeigen die Konzepte an Linux-Werkzeugen (Namensräume, Bridges, FRR, dnsmasq, nftables, keepalived, Net-SNMP, rsyslog) und an Python-Modellen. Cisco-Befehle stehen als Aufgabentext und sind **nicht ausgeführt und nicht bestätigt**. Nicht behandelt werden CCNP-Themen (BGP, EIGRP, MPLS, QoS-Details), Wireless-Controller-Konfiguration am Gerät und Cisco-Produktnamen. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2/3) | Stunden (UE) |
|---|---|---|---|
| 1 | Netzwerkgrundlagen und Cisco-Architektur | 1 | 8 |
| 2 | Ethernet, Verkabelung und Switching-Grundlagen | 1 | 8 |
| 3 | VLANs, Trunks und Inter-VLAN Routing | 1 | 9 |
| 4 | STP, EtherChannel und Layer-2-Redundanz | 2 | 8 |
| 5 | IPv4/IPv6-Adressierung und Subnetting | 1 | 10 |
| 6 | Routing-Grundlagen, Statische Routen und OSPF | 1 | 10 |
| 7 | IP-Services und Netzwerkdienste | 2 | 9 |
| 8 | Wireless LAN und Netzwerkintegration | 2 | 8 |
| 9 | Security, Hardening und Zugriffskontrolle | 1 | 10 |
| 10 | Betrieb, Monitoring, Logging und Troubleshooting | 1 | 9 |
| 11 | WAN, Virtualisierung, Cloud und SDN-Grundlagen | 2 | 8 |
| 12 | Automation, Programmability, Migration und BCDR | 3 | 9 |
| **Gesamt** | 12 Module | 7 × Priorität 1, 4 × Priorität 2, 1 × Priorität 3 | **106** |

**Priorität 1** (Pflicht) sind die Module 1, 2, 3, 5, 6, 9 und 10 (64 UE). **Priorität 2** (Vertiefung, kann bei Zeitmangel entfallen) sind die Module 4, 7, 8 und 11 (33 UE). **Priorität 3** (nur bei Zeit, entfällt zuerst) ist Modul 12 (9 UE); ohne Modul 12 verringert sich der Gesamtumfang von 106 auf 97 UE. **Hinweis zur Prüfung:** Die Prüfungsthemen der Version 2.0 enthalten Spanning Tree (Modul 4), DHCP, NAT, DNS und FHRP (Modul 7), WLAN-Grundlagen (Modul 8), Virtualisierung und VPN (Modul 11) sowie KI und Automatisierung (Modul 12) als prüfungsrelevante Themen; wer die Prüfung ablegen will, sollte die Module 2 und 3 der Priorität nicht streichen. Die Prioritäten selbst sind unverändert aus dem Excel-Lehrplan übernommen.

### 2. Quellen

**Gelesen (cisco.com, 27.11.2026):** Prüfungsthemen **200-301 CCNA, Version 2.0** (PDF „200-301_CCNA_v2.0_Exam_Topics_PDF“ auf learningcontent.cisco.com). Das Dokument nennt **kein Gültigkeitsdatum**. Es gliedert sich in fünf Bereiche: 1.0 Network Infrastructure and Connectivity (25 %), 2.0 Switching and Network Access (25 %), 3.0 IP Routing (20 %), 4.0 Network Services and Security (20 %) und 5.0 AI, and Network Operations and Management (10 %). Lange Prüfungsthemen waren in der gelesenen Fassung gekürzt.

**Abweichung vom Excel-Lehrplan (auf Wunsch):** Die Lerneinheiten folgen den Prüfungsthemen der Version 2.0 und nicht den Einheiten des Excel-Blatts. Der Rahmen (12 Module, Reihenfolge, Priorität, UE je Modul, 106 UE) ist unverändert. Das Excel-Blatt „Lehrplan in Details“ listet 96 Einheiten zu je einer Stunde, die Module summieren sich dagegen auf 106 UE; die Differenz wurde nicht aufgelöst (siehe `lehrplan-korrekturen.md`). QoS und NetFlow stehen im Excel-Blatt, aber **nicht** in den Prüfungsthemen 2.0 und werden nicht behandelt; neu sind KI im Netzwerkbetrieb (5.1, 5.2) und Layer-2-Sicherheit mit Storm Control und RA Guard (4.7).

**Zuordnung der Prüfungsthemen zu den Modulen (meine Annahme, nicht von Cisco):**

| Prüfungsthema (Version 2.0) | Modul |
|---|---|
| 1.1 Schnittstellen- und Kabelprobleme, 2.3 CDP und LLDP, 2.4 Show-Befehle und Protokolle | 2, 10 |
| 1.2 Hypervisor, VM, Container | 11 |
| 1.3 IPv4-Adressierung und Subnetting, 1.4 IPv6 | 5 |
| 1.5 Wireless-Grundlagen, 1.6 Client-Fehlersuche | 8 |
| 1.7 DHCPv4 auf IOS (Client, Server, Relay) | 7 |
| 2.1 Switch-Verbindungen (Schnittstellen, Trunks, SVI, LACP), 2.2 Edge-Ports | 2, 3, 4 |
| 2.5 Rapid PVST+ (Root, Zustände, PortFast, Root/Loop/BPDU Guard) | 4 |
| 3.1 Routingtabelle, 3.2 statische Routen, 3.3 OSPF | 6 |
| 3.4 FHRP (HSRP und VRRP) | 7 |
| 4.1 Lokale Benutzer und AAA, 4.6 ACLs, 4.7 Layer-2-Sicherheit | 9 |
| 4.2 SFTP/SCP, 5.4 SNMP, 5.6 Syslog | 10 |
| 4.3 NAT/PAT, 4.4 DNS-Einträge | 7 |
| 4.5 IPsec-VPN, 5.3 Verwaltungsansätze | 11 |
| 5.1 Agentic AI, 5.2 Prompts, 5.5 Ansible | 12 |

**Nicht gelesen:** Prüfungsformat (Dauer, Anzahl der Fragen, Bestehensgrenze), Preise, Wiederholungsregeln und alle Herstellerhandbücher. Aussagen zu Cisco-Befehlen, Standardwerten und Ausgabeformaten sind Fachwissen und **nicht bestätigt**. Prüfungsfragen werden nicht wiedergegeben. **Getestet mit (Ubuntu 24.04.5, Cloud-Container, root, ohne systemd als init):** Linux-Namensräume und Bridges (iproute2), FRRouting (zebra, ospfd), dnsmasq, nftables, keepalived, Net-SNMP, rsyslog, lldpd, chrony, OpenSSH, tshark/tcpdump, Python 3.12 mit networkx, PyYAML, Jinja2 und Flask, ansible-core 2.22.0.

### 3. Labor-Setup & Rahmenbedingungen

**Labor laut Lehrplan:** Linux-VMs und Cisco-Geräte oder ein Simulator auf einem privaten Hyper-V-Switch ohne Verbindung zum Heimnetz; Snapshots vor jeder Übung. Das Hyper-V-Labor wurde **nicht** aufgebaut, und es wurde weder Cisco IOS noch Packet Tracer verwendet.

**Skripte:** Alle Übungsskripte laufen unter Linux als root im Sandkasten `/tmp/ccna` mit eigenen Netzwerk-Namensräumen (Präfix `cc`), Ports über 1024 (z. B. SNMP 1161, Syslog 5514, SSH 2222/2223) und Hintergrunddiensten, die am Ende beendet werden. **Nie auf einem Produktivsystem ausführen.** Wo Cisco-Befehle gefragt sind, bearbeitest du sie im Simulator oder auf einem Gerät; die Musterlösung nennt sie als Fachwissen.

**Nicht ausgeführt, weil im Container nicht möglich:** alle Cisco-IOS-Befehle, VLAN-Trunks mit dem Kernelmodul 8021q und VLAN-Filterung der Bridge, Rapid PVST+, PortFast, Loop Guard, LACP/PAgP (kein bonding-Modul), OSPFv3 und IPv6-Routing, HSRP, IPsec/ESP und GRE (keine xfrm-Unterstützung), WLAN-Funk, Cloud-Controller, generative KI.

## B. Detaillierter Modulaufbau

### Modul 1: Netzwerkgrundlagen und Cisco-Architektur

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Schichten des OSI- und des TCP/IP-Modells nennen und den Feldern eines Pakets zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende beschreiben, warum sich MAC-Adressen und IP-Adressen auf dem Weg unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Topologien nach Linkzahl, Wegen und Ausfallverhalten vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rollen Access, Distribution und Core im Campus erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Namensschema und eine Geräteliste auf Fehler prüfen.
* **Voraussetzungen:** Grundkenntnisse in Windows oder Linux.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | OSI- und TCP/IP-Modell, Kapselung | 1,5 |
| 1.2 | Topologien und Gerätearten | 1 |
| 1.3 | Campus-Architektur (Access, Distribution, Core) | 1,25 |
| 1.4 | Befehlszeile und Modi (Cisco-Modell) | 1,25 |
| 1.5 | Basiswerkzeuge: ping, traceroute, show | 1 |
| 1.6 | Dokumentation und Namensschema | 0,75 |
| 1.7 | Prüfungsüberblick Version 2.0 und Labor | 1 |
| 1.8 | Methodik der Fehlersuche | 0,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kapselung im Mitschnitt (Einheiten 1.1 und 1.2):** Führe `bash grundlagen.sh` aus. Lies in Schritt 2 das erste TCP-Paket des Clients und ordne die Felder den Schichten 2, 3 und 4 zu. Erkläre, warum die Quell-MAC am Server die des Routers ist, die Quell-IP aber die des Clients, und was der TTL-Wert 63 aussagt. Lies die TCP-Flags der ersten drei Pakete (Dreiwege-Handshake).
2. **Topologien und Cisco-Modi (Einheiten 1.3 und 1.4):** Lies in Schritt 5 die Tabelle der Topologien und begründe, warum der Ring einen Linkausfall übersteht, der Stern aber nicht. Zeichne einen Entwurf mit drei Schichten und einen Entwurf mit zwei Schichten (Collapsed Core) für 200 Endgeräte. Lies in Schritt 6 das Modell der Befehlsmodi und ordne user EXEC, privileged EXEC und global configuration den Beispielwörtern zu (Fachwissen, nicht auf einem Gerät geprüft).
3. **Werkzeuge und Dokumentation (Einheiten 1.5 und 1.6):** Lies in Schritt 3 die ARP-Tabellen und in Schritt 4 das traceroute-Ergebnis und erkläre, warum der Router als erster Hop erscheint. Prüfe in Schritt 7 die Geräteliste und nenne die Regel, gegen die `SW_Lab_03` verstößt, und den zweiten Fehler.
4. **Prüfungsüberblick und Methodik (Einheiten 1.7 und 1.8):** Lies die Gewichtung der fünf Bereiche der Prüfungsthemen Version 2.0 in `lehrplan-korrekturen.md` und ordne jedem Bereich die Module dieses Kurses zu. Beschreibe die Fehlersuche von unten nach oben (physisch, Sicherung, Netzwerk, Transport, Anwendung) in fünf Sätzen.

#### Kontrollfragen

1. Warum ändert sich die MAC-Adresse eines Pakets auf dem Weg über einen Router, die IP-Adresse aber nicht?
2. Welche TCP-Flags zeigt der Dreiwege-Handshake?
3. Welche Topologie überlebt den Ausfall eines Links, und was kostet die voll vermaschte?
4. Welche Fehler enthält die Geräteliste im Beispiel?

### Modul 2: Ethernet, Verkabelung und Switching-Grundlagen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende MAC-Adressen in Individual/Group- und Universal/Local-Bit zerlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Lernen, Fluten und Altern der MAC-Tabelle an einem Switch beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende Schnittstellenzähler und Fehlerbilder (CRC, Runts, Late Collisions, Flaps) deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Nachbarn mit LLDP und CDP-Rahmen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Kabeltypen und Pinbelegung nach T568B beschreiben.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Ethernet-Rahmen und MAC-Adressen | 1,25 |
| 2.2 | Switching: Lernen, Fluten, Altern | 1,25 |
| 2.3 | Schnittstellen: Geschwindigkeit, Duplex, Auto-Negotiation | 1 |
| 2.4 | Verkabelung: Kupfer und Glasfaser | 1 |
| 2.5 | Zähler und Fehlerbilder (Kollisionen, CRC) | 1,25 |
| 2.6 | CDP und LLDP | 1 |
| 2.7 | Show-Befehle für Layer 1 und 2 | 0,75 |
| 2.8 | Dokumentation mit Nachbardaten prüfen | 0,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rahmen und Lernen (Einheiten 2.1 und 2.2):** Führe `bash ethernet-l2.sh` aus. Lies in Schritt 2 die Zerlegung der MAC-Adressen. Lies in Schritt 3 und 4, warum Gerät 3 nur die Broadcast-Anfrage sieht, und lies die MAC-Tabelle. Erkläre das Verhalten bei unbekannter Ziel-MAC.
2. **Schnittstellen, Altern und Kabel (Einheiten 2.3 und 2.4):** Lies in Schritt 5 die Alterung der Einträge (Alterungszeit im Skript 3 s) und in Schritt 6 den Linkzustand mit `ethtool`. Erkläre, was ein Schnittstellenausfall (`Link detected: no`) für beide Seiten bedeutet. Lies in Schritt 8 die Pinbelegung T568B und die Kabelregeln (Fachwissen).
3. **Fehlerbilder und Nachbarn (Einheiten 2.5 und 2.6):** Deute in Schritt 8 die Zählerwerte der vier Anschlüsse (die Werte sind erfunden) und nenne zu jedem eine Ursache. Lies in Schritt 7 und 7b die LLDP-Nachbarn und den CDP-Rahmen mit der Zieladresse 01:00:0c:cc:cc:cc.
4. **Show-Befehle und Dokumentation (Einheiten 2.7 und 2.8):** Ordne die Linux-Befehle `ip link`, `bridge fdb`, `ethtool` und `lldpcli show neighbors` den Cisco-Befehlen `show interfaces`, `show mac address-table`, `show interfaces status` und `show cdp neighbors` zu (Fachwissen, nicht auf einem Gerät geprüft). Beschreibe, wie du mit Nachbardaten eine Netzdokumentation prüfst.

#### Kontrollfragen

1. Was macht ein Switch mit einer Ziel-MAC, die er nicht kennt?
2. Wie erkennt man an einer MAC-Adresse Multicast und lokal vergebene Adressen?
3. Wofür steht ein CRC-Zähler größer als 0 und was bedeutet „Late Collisions“?
4. Welche Zieladresse nutzt CDP?

### Modul 3: VLANs, Trunks und Inter-VLAN Routing

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau des 802.1Q-Tags (VLAN-ID, Priorität) im Mitschnitt lesen.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten von Access- und Trunk-Ports mit Native VLAN und erlaubter Liste vorhersagen.
  * Nach Abschluss dieses Moduls kann der Lernende einen VLAN-Plan auf doppelte IDs, ungültige Bereiche und überlappende Netze prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Hosts in verschiedenen VLANs einen Router brauchen.
  * Nach Abschluss dieses Moduls kann der Lernende Router-on-a-Stick und SVI unterscheiden.
* **Voraussetzungen:** Modul 1 und 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | VLAN-Konzept und Broadcast-Domänen | 1 |
| 3.2 | 802.1Q-Tag | 1,25 |
| 3.3 | Access- und Trunk-Ports | 1,25 |
| 3.4 | Native VLAN und erlaubte VLANs | 1 |
| 3.5 | Inter-VLAN-Routing: Router-on-a-Stick | 1,25 |
| 3.6 | Layer-3-Switch und SVI | 1,25 |
| 3.7 | Edge-Ports: Telefon, Access Point, Drucker, virtualisierte Hosts | 1,25 |
| 3.8 | Fehlersuche bei VLANs | 0,75 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tag im Mitschnitt (Einheiten 3.1 und 3.2):** Führe `bash vlan.sh` aus. Lies in Schritt 1 die drei von Hand gebauten Rahmen (VLAN 10, 20, 30, Priorität 5 bei 30) und beschreibe die vier Felder des 802.1Q-Tags. Erkläre, warum ein Rahmen ohne Tag im Trunk zum Native VLAN gehört.
2. **Ports im Modell (Einheiten 3.3 und 3.4):** Lies in Schritt 2 die Tabelle des Port-Modells und sage für zwei weitere Fälle (Rahmen mit Tag 10 am Trunk; Rahmen ohne Tag an Fa0/2) das Ergebnis voraus. Prüfe deine Vorhersage mit dem Modell im Skript.
3. **Routing zwischen VLANs (Einheiten 3.5 und 3.6):** Lies in Schritt 4 den Ping über den Router und die ARP-Tabelle des Clients. Erkläre, warum der Client nur die MAC des Routers kennt. Beschreibe in Cisco-Befehlen (Fachwissen) Router-on-a-Stick mit Subinterface und SVI auf einem Layer-3-Switch; beide Varianten sind nicht ausgeführt.
4. **Plan prüfen und Fehler suchen (Einheiten 3.7 und 3.8):** Lies in Schritt 3 die Prüfung von `plan.yaml` (doppelte ID, ID 4095, überlappende Netze). Korrigiere den Plan, lass das Skript neu laufen und beschreibe die Fehlersuche, wenn ein Host im VLAN 20 keine Verbindung bekommt (Schritt 4: Router-Seite ausgefallen).

#### Kontrollfragen

1. Aus welchen Feldern besteht der 802.1Q-Tag und welche VLAN-IDs sind gültig?
2. Was passiert im Modell mit einem Rahmen in VLAN 30 am Trunk, wenn nur 1, 10 und 20 erlaubt sind?
3. Warum erreicht ein Host in VLAN 10 einen Host in VLAN 20 nur über einen Router?
4. Welche Meldung liefert der Router, wenn seine Schnittstelle ins Zielnetz ausfällt?

### Modul 4: STP, EtherChannel und Layer-2-Redundanz

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Wahl der Root-Bridge nach Bridge-ID (Priorität, MAC) nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Portzustände und Wurzelpfad an drei Bridges lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Umschaltzeit nach einem Linkausfall messen und bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende BPDU Guard und Root Guard durch ihre Linux-Entsprechungen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Lastverteilung bei EtherChannel und die Aushandlung mit LACP beschreiben.
* **Voraussetzungen:** Modul 2 und 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Spanning Tree: Problem und Grundidee | 1 |
| 4.2 | Wahl der Root-Bridge | 1,25 |
| 4.3 | Portrollen und Portzustände | 1 |
| 4.4 | Rapid PVST+ | 1,25 |
| 4.5 | PortFast, BPDU Guard, Root Guard, Loop Guard | 1,25 |
| 4.6 | EtherChannel und LACP | 1,25 |
| 4.7 | Layer-2-Redundanz im Entwurf | 0,5 |
| 4.8 | Fehlersuche bei STP | 0,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Wahl der Root-Bridge (Einheiten 4.1 und 4.2):** Führe `bash stp-etherchannel.sh` aus. Lies in Schritt 1 die Bridge-IDs und die Root-ID aller drei Bridges und erkläre, warum `ccs1` Root-Bridge ist. Lies in Schritt 2, was nach der Priorität 4096 auf `ccs3` geschieht, und beschreibe die Änderung der Portzustände.
2. **Zustände, Ausfall und Rapid PVST+ (Einheiten 4.3 und 4.4):** Lies die Portzustände (forwarding, blocking) und nenne je Bridge Root-Port und designierte Ports. Lies in Schritt 3 die gemessene Zeit ohne Antwort nach dem Linkausfall und vergleiche sie mit den verkürzten Zeitgebern (Forward-Delay 4 s). Beschreibe in eigenen Worten, wie Rapid PVST+ die Umschaltung beschleunigt (Fachwissen, nicht ausgeführt).
3. **Schutzfunktionen und EtherChannel (Einheiten 4.5 und 4.6):** Lies in Schritt 4 und 4b, was `guard on` (BPDU-Guard-Entsprechung) und `root_block on` (Root-Guard-Entsprechung) bewirken, und beschreibe PortFast und Loop Guard (nicht ausgeführt). Lies in Schritt 6 die Lastverteilung für 40 Flüsse mit drei Hash-Verfahren und die Tabelle der Modus-Kombinationen für LACP und PAgP.
4. **Entwurf und Fehlersuche (Einheiten 4.7 und 4.8):** Lies in Schritt 5 den Zähler eines Anschlusses im Dreieck ohne STP und beschreibe die Symptome eines Broadcast-Sturms (hohe CPU-Last, Pakete steigen schnell, alle Verbindungen langsam). Erstelle eine Prüfliste für die Fehlersuche bei STP (Root-Bridge, Portzustände, Zähler, Kabel).

#### Kontrollfragen

1. Nach welcher Regel wird die Root-Bridge gewählt?
2. Was geschah, als `ccs3` die Priorität 4096 bekam?
3. Was bewirkt Root Guard im Unterschied zu BPDU Guard?
4. Wie wird ein einzelner Fluss bei EtherChannel verteilt?
5. Welche LACP-Kombinationen bilden einen Channel?

### Modul 5: IPv4/IPv6-Adressierung und Subnetting

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende IPv4-Adresse, Netz, Broadcast und Hostzahl berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende ein VLSM-Netz aus einem Adressblock planen.
  * Nach Abschluss dieses Moduls kann der Lernende private und besondere Adressen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende IPv6-Adresse kürzen, EUI-64-Adresse und Solicited-Node-Adresse ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende typische Konfigurationsfehler (Gateway, Maske, doppelte Adresse) an ihren Symptomen erkennen.
* **Voraussetzungen:** Modul 1 und 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | IPv4-Adresse und Maske | 1,25 |
| 5.2 | Subnetting | 1,5 |
| 5.3 | VLSM und Zusammenfassung | 1,5 |
| 5.4 | Private und besondere Adressen | 1 |
| 5.5 | IPv6: Aufbau und Adresstypen | 1,5 |
| 5.6 | EUI-64, Präfixlängen und SLAAC | 1,25 |
| 5.7 | Dual Stack | 0,75 |
| 5.8 | Fehlersuche bei IPv4 und IPv6 | 1,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rechnen mit IPv4 (Einheiten 5.1 und 5.2):** Führe `bash adressierung.sh` aus. Lies Schritt 1 und rechne die drei Beispiele von Hand nach (Netz, Broadcast, Hostzahl). Berechne zusätzlich Netz und Broadcast von 172.20.99.130/27 und prüfe das Ergebnis mit `python3 -c "import ipaddress; …"`.
2. **VLSM und besondere Adressen (Einheiten 5.3 und 5.4):** Lies in Schritt 2 den VLSM-Plan für 192.168.100.0/24 und erkläre, warum die Netze nach Größe sortiert werden. Ergänze einen weiteren Bedarf von 6 Hosts und finde den Platz im Rest. Lies Schritt 3 und nenne zu jeder Adresse die Eigenschaft (Loopback, APIPA, privat, Dokumentation, Multicast, öffentlich).
3. **IPv6 als Rechnung (Einheiten 5.5 und 5.6):** Lies Schritt 4 und leite für die MAC `00:1b:63:84:45:e6` die EUI-64-Schnittstellenkennung und die Solicited-Node-Adresse ab (das Ergebnis steht im Skript). Erkläre, warum das 7. Bit des ersten Bytes umgedreht wird. IPv6 ist im Container nicht aktiv; alles ist Rechnung.
4. **Dual Stack und Fehlerbilder (Einheiten 5.7 und 5.8):** Beschreibe, was ein Dual-Stack-Host je Protokoll braucht (Adresse, Gateway, DNS). Lies Schritt 6 mit den Fällen falsches Gateway, Maske /30, Maske /16 und doppelte Adresse. Ordne jedem Fall das Symptom und den ersten Prüfschritt zu und beschreibe, woran man eine doppelte Adresse im Mitschnitt erkennt.

#### Kontrollfragen

1. Wie viele nutzbare Hosts hat ein /26, ein /30 und ein /20?
2. Warum werden die Netze beim VLSM nach Größe sortiert?
3. Wie entsteht die EUI-64-Adresse aus einer MAC?
4. Welches Symptom zeigt ein Host mit Maske /16 statt /24?

### Modul 6: Routing-Grundlagen, Statische Routen und OSPF

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende in einer Routingtabelle den nächsten Hop eines Pakets bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende statische Routen setzen und die Notwendigkeit des Rückwegs begründen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Floating-Static-Route als Ersatzweg einrichten und den Umschaltvorgang beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende OSPF-Nachbarschaft, Kosten und Pfadwechsel in FRRouting lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wahl von DR und BDR an einem Broadcast-Segment nachvollziehen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Routingtabelle lesen | 1,5 |
| 6.2 | Statische Routen | 1,25 |
| 6.3 | Default-, Host- und Floating-Routen | 1,25 |
| 6.4 | Längster Präfix und Administrative Distance | 1 |
| 6.5 | OSPFv2: Nachbarschaft und Kosten | 1,5 |
| 6.6 | OSPF: Punkt-zu-Punkt und DR/BDR | 1,5 |
| 6.7 | Router-ID und OSPFv3 | 1 |
| 6.8 | Fehlersuche beim Routing | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Statische Routen (Einheiten 6.1 und 6.2):** Führe `bash routing.sh` aus. Lies in Teil A1 die Fehlerbilder „keine Route“, „nur Hinweg“ und „Hin- und Rückweg“ und beschreibe, warum auch der Rückweg konfiguriert sein muss. Lies das traceroute-Ergebnis und die Routen von R1.
2. **Spezifischer Weg und Ersatzweg (Einheiten 6.3 und 6.4):** Lies Teil A2 (Sperrroute /25 gegen Route /24) und erkläre „längster Präfix gewinnt“. Lies Teil A3 und beschreibe, was nach dem Ausfall der direkten Verbindung mit der Route der Metrik 200 geschieht. Lies Teil C (Python-Modell) und erkläre die Reihenfolge Präfix, Administrative Distance, Metrik.
3. **OSPF im Dreieck und am Broadcast-Segment (Einheiten 6.5 und 6.6):** Lies Teil B1: Nachbarn im Zustand Full, Routen mit Kosten 10/20, Pfadwechsel nach dem Setzen der Kosten 100, Verlust der Nachbarschaft bei abweichenden Hello- und Dead-Zeiten. Lies Teil B2: Wahl von DR und BDR bei Priorität 200, 100 und 1, Ausfall des DR und Rückkehr.
4. **Router-ID, OSPFv3 und Fehlersuche (Einheiten 6.7 und 6.8):** Erkläre, wie die Router-ID gewählt wird und warum sie im Skript fest gesetzt ist. Beschreibe OSPFv3 im Unterschied zu OSPFv2 (nicht ausgeführt; im Container kein IPv6-Routing). Erstelle eine Prüfliste für „keine Nachbarschaft“ (Verbindung, Adresse, Bereich, Timer, Netzwerktyp).

#### Kontrollfragen

1. Warum scheitert der Ping, wenn nur R1 eine Route zum LAN von R3 kennt?
2. Welche Route gewinnt, wenn 192.168.3.0/24 und 192.168.3.128/25 vorhanden sind?
3. Was bewirkt die höhere Metrik der Floating-Static-Route?
4. Welche Parameter müssen bei OSPF-Nachbarn übereinstimmen?
5. Wer wird DR, und was passiert bei dessen Rückkehr?

### Modul 7: IP-Services und Netzwerkdienste

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den DHCP-Ablauf (Discover, Offer, Request, Ack) im Mitschnitt erkennen und die Rolle des Relays erklären.
  * Nach Abschluss dieses Moduls kann der Lernende DNS-Einträge (A, AAAA, CNAME, MX, NS, PTR, TXT) abfragen und ein NXDOMAIN deuten.
  * Nach Abschluss dieses Moduls kann der Lernende PAT mit Portumsetzung und eine Portweiterleitung an der Verbindungstabelle erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen NTP-Abruf im Mitschnitt lesen (Modus, Schicht).
  * Nach Abschluss dieses Moduls kann der Lernende den Master-Wechsel bei VRRP messen und die virtuelle MAC erklären.
* **Voraussetzungen:** Modul 5 und 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | DHCP: Server, Relay und Reservierung | 1,25 |
| 7.2 | DHCP-Fehlersuche (Client, Server, Relay) | 1 |
| 7.3 | DNS: Einträge und Abfragen | 1,25 |
| 7.4 | NAT und PAT | 1,5 |
| 7.5 | NTP | 0,75 |
| 7.6 | First Hop Redundancy: VRRP und HSRP | 1,5 |
| 7.7 | Fehlersuche bei IP-Diensten | 1 |
| 7.8 | Dokumentation der Dienste | 0,75 |

#### Praxisaufgaben (Hands-on Lab)

1. **DHCP mit und ohne Relay (Einheiten 7.1 und 7.2):** Führe `bash dhcp-dns.sh` aus. Lies Schritt 1 (ohne Relay nur DISCOVER), Schritt 2 (mit Relay: alle vier Nachrichten, giaddr) und Schritt 3 (Reservierung). Beschreibe, wozu „ip helper-address“ dient (Fachwissen, nicht ausgeführt) und welche Prüfschritte du bei „Client bekommt keine Adresse“ gehst.
2. **DNS und NAT (Einheiten 7.3 und 7.4):** Lies in Schritt 4 von `dhcp-dns.sh` die Abfragen (A, AAAA, CNAME, MX, TXT, NS, PTR) und den NXDOMAIN. Führe `bash nat-ntp.sh` aus und lies Schritt 2 (PAT, Verbindungstabelle) und Schritt 3 (DNAT). Erkläre, warum der Server beide Clients mit derselben Adresse sieht.
3. **NTP und First Hop Redundancy (Einheiten 7.5 und 7.6):** Lies in `nat-ntp.sh` Schritt 4 (NTP-Modus 3 und 4, Schicht 8) und führe `bash fhrp.sh` aus. Lies die Wahl des Masters, die virtuelle MAC, den Mitschnitt der Advertisements, die gemessene Lücke beim Ausfall und das Verhalten bei der Rückkehr des alten Masters.
4. **Fehlersuche und Dokumentation (Einheiten 7.7 und 7.8):** Erstelle eine Prüfliste für „Host erreicht Internet nicht“ (Adresse, Gateway, DNS, NAT-Tabelle, Rückweg) und trage zu jedem Punkt den passenden Befehl ein. Dokumentiere die Dienste des Labors (Server, Relay, Adressbereich, Reservierung, Namen) in einer Tabelle.

#### Kontrollfragen

1. Warum erreicht ein DHCP-Discover den Server in einem anderen Netz nicht ohne Relay?
2. Was zeigt das Feld giaddr?
3. Wie unterscheidet PAT zwei Clients mit demselben lokalen Port?
4. Welche virtuelle MAC nutzt VRRP mit der Gruppe 10?

### Modul 8: Wireless LAN und Netzwerkintegration

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende überlappungsfreie Kanäle im 2,4-GHz-Band bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende Leistung in dBm umrechnen und Dämpfung, Empfangspegel und SNR abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende beschreiben, wie ein WPA2-Schlüssel aus Passphrase und SSID entsteht und warum die SSID mitspielt.
  * Nach Abschluss dieses Moduls kann der Lernende ein PoE-Budget prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Pegelprobleme von Authentifizierungsproblemen unterscheiden.
* **Voraussetzungen:** Modul 5 und 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | WLAN-Grundlagen und Standards | 1 |
| 8.2 | Bänder und Kanäle | 1,25 |
| 8.3 | RF-Eigenschaften: dBm, Dämpfung, SNR | 1,25 |
| 8.4 | Sicherheitsprotokolle | 1,25 |
| 8.5 | Störungsursachen | 0,75 |
| 8.6 | AP-Betrieb: autonom, Controller, PoE | 1,25 |
| 8.7 | Fehlersuche bei WLAN-Clients | 1 |
| 8.8 | SSID-, VLAN- und Subnetzplan | 0,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kanäle (Einheiten 8.1 und 8.2):** Führe `bash wlan.sh` aus. Lies Schritt 1 und nenne die überlappungsfreien Kanäle im 2,4-GHz-Band. Erkläre, warum bei 20 MHz Abstand eine Überlappung entsteht (Modell mit 22 MHz Kanalbreite).
2. **Pegel und Sicherheit (Einheiten 8.3 und 8.4):** Lies Schritt 2 (EIRP 19 dBm, Dämpfung, SNR) und Schritt 3 (WPA2-Schlüsselableitung, Testvektor stimmt überein). Erkläre, warum dieselbe Passphrase bei anderer SSID einen anderen Schlüssel ergibt und was WPA3-Personal ändert (nicht ausgeführt).
3. **Störungen und AP-Betrieb (Einheiten 8.5 und 8.6):** Beschreibe drei Störquellen im 2,4-GHz-Band (Fachwissen, nicht gemessen). Lies Schritt 5 und prüfe das PoE-Budget: Welche Last überschreitet das Budget, und was änderst du? Beschreibe den Unterschied zwischen autonomen und Controller-basierten Access Points (Fachwissen).
4. **Client-Fehlersuche und Plan (Einheiten 8.7 und 8.8):** Lies Schritt 6 (Pegel, Rauschen, SNR) und Schritt 7 (Befehle unter Windows, macOS, Linux). Lies Schritt 4 (SSID-, VLAN- und Subnetzplan) und korrigiere die vier Fehler des Plans. Beschreibe die Prüfreihenfolge bei „WLAN verbunden, aber kein Internet“.

#### Kontrollfragen

1. Welche Kanäle im 2,4-GHz-Band sind überlappungsfrei?
2. Wie entsteht der WPA2-PSK-Schlüssel?
3. Was bedeutet ein SNR von 8 dB bei einem Pegel von -62 dBm?
4. Wie viel Leistung brauchen die Geräte im Beispiel, und reicht ein 370-W-Switch?

### Modul 9: Security, Hardening und Zugriffskontrolle

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine ACL nach Reihenfolge, Wildcard-Maske und implizitem Deny auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende ein Paketfilter-Gegenstück mit Zählern lesen und eine Regel-Reihenfolge prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Port Security, DHCP Snooping und Dynamic ARP Inspection in ihrer Wirkung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Storm Control mit einem Schwellwert erklären.
  * Nach Abschluss dieses Moduls kann der Lernende SSH-Zugänge per Schlüssel absichern und AAA-Protokolle unterscheiden.
* **Voraussetzungen:** Modul 3, 5 und 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Lokale Benutzer, AAA, RADIUS und TACACS+ | 1,5 |
| 9.2 | ACL-Grundlagen: Reihenfolge, Wildcard, implizites Deny | 1,25 |
| 9.3 | Standard-, erweiterte und benannte ACLs | 1,5 |
| 9.4 | Port Security | 1,25 |
| 9.5 | DHCP Snooping und Dynamic ARP Inspection | 1,5 |
| 9.6 | Storm Control und RA Guard | 0,75 |
| 9.7 | Härtung der Verwaltungszugänge | 1,25 |
| 9.8 | Zugriffskontrolle auf die Verwaltungsebene | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **AAA und ACL-Auswertung (Einheiten 9.1 und 9.2):** Führe `bash sicherheit.sh` aus. Lies Schritt 6 (RADIUS und TACACS+) und nenne je einen Einsatz. Lies Schritt 2 (ACL-Auswertung): Prüfe die fünf Pakete der Tabelle von Hand, nenne die entscheidende Zeile und erkläre, was das implizite Deny am Ende bewirkt. Lies die vier Wildcard-Beispiele.
2. **Paketfilter und Port Security (Einheiten 9.3 und 9.4):** Lies Schritt 3 (nftables mit Zählern): Welche Anfragen kommen durch, welche nicht, und was zeigen die Zähler? Schreibe die ACL aus Schritt 2 als Cisco-Befehle (Fachwissen, nicht ausgeführt). Lies Schritt 4 (Port Security) und vergleiche die Modi protect, restrict und shutdown.
3. **Layer-2-Schutz (Einheiten 9.5 und 9.6):** Lies Schritt 5 (DHCP Snooping und DAI) und Schritt 5b (Storm Control): Erkläre, warum der Angreifer auf Fa0/5 verworfen wird und wann Storm Control eingreift. RA Guard ist nicht ausgeführt; beschreibe die Funktion in zwei Sätzen.
4. **SSH-Härtung und Verwaltungsebene (Einheiten 9.7 und 9.8):** Lies Schritt 1 (SSH mit Schlüssel, Passwort abgelehnt, `sshd -T`) und nenne fünf Härtungsmaßnahmen. Beschreibe, wie man den Zugang zur Verwaltung (VTY) auf ein Management-Netz beschränkt (Fachwissen, nicht ausgeführt).

#### Kontrollfragen

1. Warum steht am Ende jeder ACL ein implizites Deny, und welche Folge hat das?
2. Wie ist die Wildcard-Maske für ein /22 und für ein /27?
3. Was unterscheidet die Port-Security-Modi?
4. Wodurch erkennt DAI den Angreifer, der sich als 192.168.10.1 ausgibt?
5. Worin unterscheiden sich RADIUS und TACACS+?

### Modul 10: Betrieb, Monitoring, Logging und Troubleshooting

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SNMP-Objekte abfragen und die Versionen v2c und v3 unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen SNMP-Zähler in Auslastung umrechnen und den 32-Bit-Überlauf erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Syslog-Meldungen nach Schweregrad filtern und das Cisco-Format lesen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Konfiguration sichern, vergleichen und per SFTP/SCP ablegen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler schrittweise von der physischen Ebene bis zur Anwendung eingrenzen.
* **Voraussetzungen:** Modul 5, 6 und 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | SNMP: Abfragen, Versionen und Zugriff | 1,5 |
| 10.2 | Syslog: Schweregrade, Facility und zentrale Sammlung | 1,5 |
| 10.3 | Konfigurationssicherung mit SCP und SFTP | 1 |
| 10.4 | Baselines, Auslastung und Traps | 1 |
| 10.5 | Show-Befehle und Protokolle | 1,25 |
| 10.6 | Fehlersuche von unten nach oben | 1,5 |
| 10.7 | Dokumentation und Änderungsprotokoll | 0,75 |
| 10.8 | Fallübungen zur Fehlersuche | 0,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **SNMP und Syslog (Einheiten 10.1 und 10.2):** Führe `bash snmp-syslog.sh` aus. Lies Schritt 1 und 2 (SNMPv2c mit Community, SNMPv3 mit SHA und AES, falsche Zugangsdaten) und beschreibe die Unterschiede. Lies Schritt 5 (Schweregrade und Filter) und ordne die sechs Meldungen den Schweregraden zu.
2. **Sicherung, Auslastung und Traps (Einheiten 10.3 und 10.4):** Lies Schritt 6 (Sicherung, Prüfsumme, diff) und Schritt 7 (SCP und SFTP, Prüfsumme gleich). Lies Schritt 3 (Auslastung aus zwei Zählerwerten, 32-Bit-Überlauf) und Schritt 4 (Trap) und erkläre, wann ein Trap besser ist als Abfragen (Polling).
3. **Show-Befehle und Fehlersuche (Einheiten 10.5 und 10.6):** Ordne die Befehle `ip addr`, `ip route`, `ping`, `traceroute`, `ss`, `dig` den Cisco-Befehlen `show ip interface brief`, `show ip route`, `ping`, `traceroute`, `show tcp brief`, `nslookup` zu (Fachwissen, nicht ausgeführt). Führe `bash fehlersuche.sh` aus und lies die fünf Fehlerbilder samt Eingrenzung.
4. **Dokumentation und Fälle (Einheiten 10.7 und 10.8):** Schreibe für die Änderung zwischen den beiden Konfigurationsständen in Schritt 6 ein Änderungsprotokoll (System, Änderung, Rückfallplan, Prüfung). Lies Schritt 7 von `fehlersuche.sh` und nenne zu drei Symptomen die wahrscheinlichen Ursachen; beschreibe einen eigenen Fall mit dem Weg von der Meldung zur Ursache.

#### Kontrollfragen

1. Was ist beim Abruf mit falscher Community zu beobachten, was bei SNMPv3 mit falschem Kennwort?
2. Warum verwendet man bei schnellen Schnittstellen 64-Bit-Zähler?
3. Welche Meldungen sendet `logging trap warnings`?
4. Woran erkennt man, ob ein Dienst oder ein Filter schuld ist, wenn Ping klappt, aber TCP nicht?

### Modul 11: WAN, Virtualisierung, Cloud und SDN-Grundlagen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Hypervisor, VM und Container unterscheiden und die Kernel-Grundlage von Containern zeigen.
  * Nach Abschluss dieses Moduls kann der Lernende ein VXLAN im Mitschnitt in Außen- und Innenpaket zerlegen und den MTU-Mehraufwand berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende WAN-Topologien nach Leitungszahl und Ausfallverhalten vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Site-to-Site- und Remote-Access-VPN unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine Cloud-Adressplanung auf Überschneidung mit dem Standortnetz prüfen.
* **Voraussetzungen:** Modul 5, 6 und 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Hypervisor, virtuelle Maschine und Container | 1,5 |
| 11.2 | Overlay und VXLAN | 1,25 |
| 11.3 | WAN-Typen und Topologien | 1 |
| 11.4 | IPsec-VPN: Site-to-Site und Remote Access | 1,5 |
| 11.5 | Cloud-Modelle und Adressplanung | 1 |
| 11.6 | SDN und Controller | 1 |
| 11.7 | Verwaltungsansätze | 0,5 |
| 11.8 | MTU und Fehlersuche im Overlay | 0,25 |

#### Praxisaufgaben (Hands-on Lab)

1. **Virtualisierung und Overlay (Einheiten 11.1 und 11.2):** Führe `bash overlay-virt.sh` aus. Lies Schritt 3 (Prozesse im neuen PID-Namensraum, Hostname, Netzwerk-Namensraum) und beschreibe den Unterschied zwischen Container und VM. Lies Schritt 1: Zerlege den Mitschnitt in Außenpaket (Underlay) und Innenpaket (Overlay) und nenne VNI und UDP-Port.
2. **WAN und VPN (Einheiten 11.3 und 11.4):** Lies Schritt 4 (Hub-and-Spoke, teilvermascht, vollvermascht) und berechne die Leitungen für 12 Standorte. Lies Schritt 2 (IPsec und GRE im Container nicht ausführbar) und beschreibe in sechs Sätzen Site-to-Site- und Remote-Access-VPN, ESP, IKE und Transport- gegenüber Tunnelmodus (Fachwissen, nicht ausgeführt).
3. **Cloud und SDN (Einheiten 11.5 und 11.6):** Lies Schritt 5 (VPC-Subnetze und Überschneidung mit dem Standortnetz) und nenne eine Lösung bei Überschneidung. Beschreibe Controller, Southbound- und Northbound-Schnittstelle (Fachwissen) und vergleiche gerätebasierte, cloudbasierte, controllerbasierte und automatisierungsbasierte Verwaltung.
4. **Verwaltungsansätze und MTU (Einheiten 11.7 und 11.8):** Berechne den Mehraufwand von VXLAN und leite die größte Nutzlast bei MTU 1500 ab (siehe Schritt 1). Beschreibe, wie man ein Problem findet, bei dem nur große Pakete scheitern, und was beim Ausfall des Underlays mit dem Overlay geschieht.

#### Kontrollfragen

1. Wie groß ist der Mehraufwand von VXLAN, und welche MTU hat die Overlay-Schnittstelle bei Underlay-MTU 1500?
2. Welche Ping-Größe passt noch durch, welche nicht?
3. Worin unterscheidet sich ein Container von einer VM?
4. Welches Problem entsteht, wenn VPC- und Standortnetz überlappen?

### Modul 12: Automation, Programmability, Migration und BCDR

* **Priorität:** 3 (Vertiefung)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationen aus einem Datenmodell mit Jinja2 erzeugen und vor dem Erzeugen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende REST-Verben, Statuscodes und Token an einem lokalen Mock-Controller anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Ansible-Playbook im Trockenlauf und beim wiederholten Lauf (Idempotenz) lesen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Soll-Ist-Abweichung finden.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle agentischer KI mit Freigabe und Protokoll beschreiben und KI-Ausgaben vor dem Einsatz prüfen.
* **Voraussetzungen:** Modul 3, 6 und 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Agentische KI im Netzwerkbetrieb | 1,25 |
| 12.2 | Prompts für generative KI | 1,25 |
| 12.3 | Datenformate und REST-APIs | 1,5 |
| 12.4 | Vorlagen mit YAML und Jinja2 | 1 |
| 12.5 | Ansible | 1,5 |
| 12.6 | Abweichungsprüfung und Compliance | 0,75 |
| 12.7 | Migration und Wiederherstellung (BCDR) | 1,25 |
| 12.8 | Änderungsprozess und Dokumentation | 0,5 |

#### Praxisaufgaben (Hands-on Lab)

1. **KI im Netzwerkbetrieb (Einheiten 12.1 und 12.2):** Führe `bash automation.sh` aus. Lies Schritt 7 (Freigabeliste, Genehmigungsschritt, Protokoll) und Schritt 8 (Prüfung der Bausteine eines Prompts) und erkläre, welche Aktionen ein agentisches System ohne Freigabe ausführen darf. Lies in Schritt 6 die Prüfung des KI-Vorschlags und nenne die drei Befunde. Alles sind Spielzeugmodelle ohne generatives Modell.
2. **Datenformate, REST und Vorlagen (Einheiten 12.3 und 12.4):** Lies Schritt 3 (YAML, JSON, XML) und Schritt 4 (REST: 401, 200, 201, 204, 404, PATCH, jq). Lies Schritt 1: Datenmodell, Vorlage, erzeugte Datei und die Fehlerprüfung (VLAN 40 nicht definiert). Ergänze im Datenmodell einen vierten Switch und erzeuge die Konfiguration.
3. **Ansible und Abweichungen (Einheiten 12.5 und 12.6):** Lies Schritt 5: Trockenlauf (`--check --diff`), erster Lauf (changed=1), zweiter Lauf (changed=0), Lauf mit Fehler (Assertion). Lies Schritt 2 (Drift) und bewerte die drei zusätzlichen Zeilen im Ist-Stand.
4. **Migration, Wiederherstellung und Prozess (Einheiten 12.7 und 12.8):** Plane die Ablösung eines Switches in sieben Schritten (Bestandsaufnahme, Konfiguration sichern, Ersatz vorbereiten, Wartungsfenster, Wechsel, Prüfung, Rückfallplan) und nenne zu jedem Schritt eine Prüfung. Nenne RPO und RTO für die Konfigurationssicherung deines Labors. Beschreibe, wie ein Änderungsprozess mit Genehmigung und Protokoll aussieht (Lehrbuchwissen, kein Skript).

#### Kontrollfragen

1. Welche Statuscodes zeigen Erfolg, nicht angemeldet und nicht gefunden?
2. Was bedeutet changed=0 im zweiten Ansible-Lauf?
3. Warum prüft man KI-Ausgaben vor dem Einsatz?
4. Welche Bausteine gehören in einen Prompt für den Netzwerkbetrieb?
