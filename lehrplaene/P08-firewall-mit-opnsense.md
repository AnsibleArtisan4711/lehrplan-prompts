# Lehrplan: Firewall mit OPNsense

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen sind hilfreich |
| **Gesamtumfang** | 13 Module, 108 UE (zu 45 Minuten; 81 Stunden) |
| **Fokus-Technologien** | OPNsense |
| **Thematische Abgrenzung (Out of Scope)** | Unterschiede zu pfSense werden nur kurz erwähnt. Die Vertiefung von VPN (WireGuard, OpenVPN, IPsec) gehört in den Kurs „VPN“; hier nur der Überblick. Nicht behandelt: Multi-WAN-Lastverteilung, Captive Portal, Traffic Shaping, BGP/OSPF und die Weiterentwicklung der Plugins |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Konzept, Installation und Labor | 1 | 7 |
| 2 | Interfaces, VLANs und Zonen | 1 | 9 |
| 3 | Aliase | 1 | 8 |
| 4 | Firewall-Regeln und Reihenfolge | 1 | 10 |
| 5 | NAT: ausgehend, Portweiterleitung und 1:1 | 1 | 9 |
| 6 | DHCP und DNS auf der Firewall | 1 | 9 |
| 7 | Zertifikate und interne CA | 1 | 8 |
| 8 | VPN-Dienste: Überblick | 2 | 6 |
| 9 | IDS/IPS mit Suricata | 1 | 10 |
| 10 | Hochverfügbarkeit (CARP-Prinzip) | 2 | 8 |
| 11 | Sicherung der Konfiguration | 1 | 7 |
| 12 | Logging und Plugins | 1 | 8 |
| 13 | Fehlersuche und Abschlussprojekt | 1 | 9 |
| **Gesamt** | 13 Module | 11 × Priorität 1, 2 × Priorität 2 | **108** |

**Priorität 1** (Pflicht) sind die Module 1 bis 7, 9 und 11 bis 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) sind Modul 8 (VPN-Überblick) und Modul 10 (Hochverfügbarkeit). Fallen beide weg, verringert sich der Gesamtumfang auf 94 UE.

### 2. Quellen

**OPNsense selbst wurde nicht ausgeführt und keine Quelle gelesen.** Alle Aussagen über OPNsense (Menünamen, Oberfläche, Regelverarbeitung, Plugins, CARP, Suricata-Einbindung, Aufbau der Konfigurationsdatei, Installation unter Hyper-V) stammen aus Fachwissen und sind in den Modulen mit „nicht bestätigt“ gekennzeichnet. Geprüft wurde das **Verhalten der zugrunde liegenden Technik** in einem Namespace-Labor (Ubuntu 24.04): Regelreihenfolge, NAT, Aliase und Protokollierung mit nftables 1.0.9, DHCP/DNS mit dnsmasq, IDS mit Suricata 7.0.3 (Offline-Modus), Adressübernahme mit keepalived 2.2.8 (VRRP, nicht CARP), Zertifikate mit OpenSSL 3.0.13, Sicherungsablauf mit xmllint und openssl. OPNsense verwendet die Paketfilter-Technik von FreeBSD (pf); deren Regelauswertung weicht von nftables ab. Wo das Labor etwas nachbildet, steht das in der Übung.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switches:** drei private Switches ohne Verbindung zum Heimnetz: `Lab-LAN` (`10.8.1.0/24`), `Lab-DMZ` (`10.8.2.0/24`) und `Lab-WAN` (`10.8.9.0/24`).

**VMs:** `fw01` (OPNsense, drei Netzwerkkarten: LAN `10.8.1.1`, DMZ `10.8.2.1`, WAN `10.8.9.2`), `cl01` (Client im LAN, `10.8.1.2`, Debian 12 mit Desktop oder Konsole, `curl`, `dig`), `srv01` (Linux-Server in der DMZ, `10.8.2.2`, kleiner Webdienst auf den Ports 80 und 8080 sowie ein Dienst auf Port 22) und optional `wan01` (Linux im WAN-Netz `10.8.9.1`, steht für „das Internet“ und kennt keine Rückroute in die internen Netze). Ohne `wan01` lassen sich die NAT-Aufgaben nur eingeschränkt prüfen.

**OPNsense installieren:** Das Installationsabbild kommt vor Kursbeginn aus der offiziellen Quelle (Versionen und Prüfsummen dort lesen; im Kurs **nicht** geprüft). Unter Hyper-V sind Generation und Secure-Boot-Einstellung der VM zu beachten (nicht bestätigt). Vor jeder größeren Änderung einen Hyper-V-Prüfpunkt von `fw01` anlegen.

**Skripte:** Die Beispielskripte bilden dieses Labor als Namespaces auf einer einzelnen Linux-Maschine nach (`on fw …` = „im Namespace der Firewall“). **Die Firewall dort ist nicht OPNsense, sondern Linux mit nftables.** Die Skripte zeigen die Logik, nicht die Oberfläche von OPNsense.

## B. Detaillierter Modulaufbau

### Modul 1: Konzept, Installation und Labor

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aufgaben einer Firewall und der Zonen WAN, LAN und DMZ erklären.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor mit Adressplan aufbauen und die Erreichbarkeit prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Installation und Erstkonfiguration von OPNsense in Schritten beschreiben.
* **Voraussetzungen:** Kenntnisse zu IP-Adressen und Subnetzen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Was eine Firewall leistet: Paketfilter, zustandsbehaftet, Zonen; Aufgaben von OPNsense (Routing, NAT, DHCP, DNS, VPN, IDS); Unterschiede zu pfSense (kurz) | 2 |
| 1.2 | Aufbau des Labors: drei Netze, drei bis vier VMs, Adressplan; Hyper-V-Switches und Prüfpunkte | 2 |
| 1.3 | Installation und Erstkonfiguration (Konsole, Weboberfläche, Zuordnung der Schnittstellen WAN/LAN/DMZ); Zugriff und erste Absicherung | 2 |
| 1.4 | Praxis: Labor mit `labor_pruefen.sh` nachbilden und Erreichbarkeit ohne Regeln beschreiben | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Adressplan (Einheit 1.2):** Legen Sie für Labor und Firewall einen Adressplan an (Netz, Adresse der Firewall, Adresse der Geräte) und vergleichen Sie ihn mit `labor_pruefen.sh`.
2. **Labor prüfen (Einheit 1.4):** Führen Sie `bash labor_pruefen.sh` aus. Welche Verbindungen funktionieren ohne Regeln, und warum erreicht der Client das „Internet“ nicht?
3. **Zonen (Einheit 1.1):** Zeichnen Sie die drei Zonen mit Schnittstellen der Firewall und tragen Sie ein, welcher Verkehr später erlaubt werden soll.
4. **Installationsablauf (Einheit 1.3):** Beschreiben Sie in sechs Schritten, wie `fw01` installiert und für das Labor eingerichtet wird (Abbild, VM, Netzwerkkarten, Installation, Schnittstellenzuordnung, erster Aufruf der Weboberfläche). Kennzeichnen Sie Schritte, die Sie nicht geprüft haben.
5. **Erste Absicherung (Einheit 1.3):** Nennen Sie drei Maßnahmen nach der Installation (z. B. Standardkennwort ändern, Zugriff auf die Oberfläche nur aus dem LAN, Zeit und Name setzen).

#### Kontrollfragen

1. Was bedeutet „zustandsbehaftet“ bei einer Firewall?
2. Wozu dienen die Zonen WAN, LAN und DMZ?
3. Warum bekommt das Labor keine Verbindung zum Heimnetz?
4. Welche Schritte gehören zur Erstkonfiguration?

### Modul 2: Interfaces, VLANs und Zonen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zonen als eigene Schnittstellen mit eigener Adresse beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines 802.1Q-Rahmens erklären und im Mitschnitt lesen.
  * Nach Abschluss dieses Moduls kann der Lernende VLANs für eine kleine Netzaufteilung planen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Schnittstellen zuordnen und konfigurieren (statische Adresse, Beschreibung), Zonen; Weiterleitung zwischen Netzen | 3 |
| 2.2 | VLANs (IEEE 802.1Q): Tag, VLAN-ID, Trunk und Zugangsport; VLAN-Schnittstellen auf der Firewall | 3 |
| 2.3 | Praxis: `vlan_demo.sh` ausführen (Zonen, Weiterleitung, getaggter Rahmen im Mitschnitt) | 2 |
| 2.4 | Planung: Netzaufteilung (Büro, Gäste, Server), Adressplan, typische Fehler (VLAN-ID, nicht getaggt) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Schnittstellen lesen (Einheit 2.1):** Zeigen Sie mit dem Skript die Schnittstellen der Firewall und ordnen Sie jede einer Zone zu.
2. **Weiterleitung (Einheit 2.1):** Schalten Sie die Weiterleitung aus und wieder ein und beschreiben Sie, was sich im Test ändert.
3. **Getaggter Rahmen (Einheit 2.3):** Lesen Sie im Mitschnitt, in welchem Feld die VLAN-ID steht und welcher Ethernet-Typ den Rahmen kennzeichnet.
4. **Planung (Einheit 2.4):** Planen Sie VLAN 10 (Büro), 20 (Gäste) und 30 (Server) mit Netzen und Adressen der Firewall.
5. **Grenze des Labors (Einheit 2.2):** Erklären Sie, warum das Skript keine echte VLAN-Schnittstelle anlegt und was an der Stelle in einer VM zu tun wäre.

#### Kontrollfragen

1. Was enthält der VLAN-Tag eines Rahmens?
2. Wie unterscheiden sich Trunk und Zugangsport?
3. Warum trennt ein VLAN allein Netze noch nicht sicher?
4. Welche Rolle hat die Firewall zwischen zwei VLANs?

### Modul 3: Aliase

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aliase für Hosts, Netze und Ports planen und benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln über Aliase statt feste Adressen formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler in Aliasen erkennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Aliastypen: Hosts, Netze, Ports; Namen, Beschreibung, Verwendung in Regeln | 2 |
| 3.2 | Aliase pflegen: Einträge ergänzen und entfernen, Namenskonvention, verschachtelte Aliase (nicht bestätigt) | 2 |
| 3.3 | Praxis: `alias_demo.sh` ausführen (Sets als Nachbildung) | 3 |
| 3.4 | Fehlerquellen: Tippfehler, vergessene Verwendung, zu große Listen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aliase anlegen (Einheit 3.1):** Legen Sie die Aliase für Webserver, Web-Ports und Verwaltungsnetz an (Skript Schritt 1) und lesen Sie die Regel.
2. **Test (Einheit 3.3):** Rufen Sie Port 80, 8080 und 22 des Servers auf und erklären Sie das Ergebnis.
3. **Erweitern (Einheit 3.2):** Nehmen Sie Port 22 in den Port-Alias auf. Wird die Regel dafür geändert?
4. **Verkleinern (Einheit 3.2):** Entfernen Sie Port 8080 und prüfen Sie den Zugriff.
5. **Namenskonvention (Einheit 3.2):** Legen Sie eine Namenskonvention für Aliase fest (Präfix je Typ) und wenden Sie sie auf fünf Beispiele an.
6. **Fehlersuche (Einheit 3.4):** Ein Alias enthält `10.8.2.22` statt `10.8.2.2`. Wie fällt das auf?

#### Kontrollfragen

1. Welchen Vorteil haben Aliase gegenüber festen Adressen in Regeln?
2. Welche Typen von Aliasen gibt es?
3. Warum ändert sich beim Erweitern eines Aliases die Regel nicht?
4. Was ist bei verschachtelten Aliasen zu beachten?

### Modul 4: Firewall-Regeln und Reihenfolge

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Regeln nach Schnittstelle, Quelle, Ziel und Port formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung der Reihenfolge erklären und mit Zählern prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Block und Reject unterscheiden.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Regelaufbau: Schnittstelle, Richtung, Aktion (Pass, Block, Reject), Protokoll, Quelle, Ziel, Port, Protokollierung | 3 |
| 4.2 | Reihenfolge und Standardverhalten; Regeln je Schnittstelle, globale (floating) Regeln (nicht bestätigt); zustandsbehaftete Antworten | 3 |
| 4.3 | Praxis: `regeln_demo.sh` ausführen (falsche und richtige Reihenfolge, Zähler, Block und Reject) | 3 |
| 4.4 | Regelwerk dokumentieren: Beschreibungen, Aufräumen, Änderungsablauf (testen, speichern) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Standard (Einheit 4.2):** Prüfen Sie, dass ohne erlaubende Regel kein weitergeleiteter Verkehr durchkommt.
2. **Falsche Reihenfolge (Einheit 4.2):** Laden Sie die Regeln aus Schritt 2 (Erlaubnis vor Sperre) und erklären Sie, warum Port 22 erreichbar bleibt.
3. **Richtige Reihenfolge (Einheit 4.2):** Stellen Sie die Reihenfolge um (Sperre zuerst) und prüfen Sie Port 22 und 80.
4. **Richtung (Einheit 4.1):** Prüfen Sie, dass die DMZ das LAN nicht erreicht, obwohl das LAN die DMZ erreicht (Antworten sind zustandsbehaftet erlaubt).
5. **Block und Reject (Einheit 4.1):** Vergleichen Sie die Wartezeit der Aktionen und nennen Sie je einen Einsatz.
6. **Zähler (Einheit 4.3):** Lesen Sie in Schritt 6, welche Regeln Pakete getroffen haben, und erklären Sie die Zahlen.

#### Kontrollfragen

1. Warum bleibt eine Sperre unterhalb einer allgemeinen Erlaubnis wirkungslos?
2. Wie unterscheidet sich Reject von Block für den Client?
3. Warum braucht die Rückrichtung keine eigene Regel?
4. Woran erkennt man mit Zählern, welche Regel greift?

### Modul 5: NAT: ausgehend, Portweiterleitung und 1:1

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die drei NAT-Arten unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ausgehendes NAT und eine Portweiterleitung samt Filterregel einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung von Reihenfolge bei NAT-Regeln erklären.
* **Voraussetzungen:** Module 2 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Arten von NAT: ausgehend (Masquerade/SNAT), Portweiterleitung (DNAT), 1:1; Zusammenspiel mit Filterregeln | 3 |
| 5.2 | Ausgehendes NAT einrichten und prüfen (Verbindungstabelle); Portweiterleitung mit Filterregel | 3 |
| 5.3 | Praxis: `nat_demo.sh` ausführen (Quelladresse, Weiterleitung, Reihenfolge der NAT-Regeln) | 2 |
| 5.4 | Grenzen: Reflection (nicht bestätigt), Protokolle mit Adressen im Inhalt, Doppel-NAT | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ohne NAT (Einheit 5.2):** Prüfen Sie, dass der LAN-Client das „Internet“ ohne NAT nicht erreicht, und nennen Sie die Ursache.
2. **Ausgehendes NAT (Einheit 5.2):** Richten Sie die Masquerade-Regel am WAN ein und lesen Sie die Verbindungstabelle: Welche Adressen stehen in beiden Richtungen?
3. **Portweiterleitung (Einheit 5.2):** Leiten Sie WAN-Port 8080 auf den Server (Port 80) und prüfen Sie von `wan01` aus.
4. **Filterregel (Einheit 5.1):** Entfernen Sie die erlaubende Filterregel und zeigen Sie, dass die Weiterleitung allein nicht reicht.
5. **1:1-NAT (Einheit 5.3):** Binden Sie die externe Adresse `10.8.9.50` an den Server und prüfen Sie beide Richtungen. Was zeigt der Server als Quelladresse für ausgehenden Verkehr?
6. **Reihenfolge (Einheit 5.3):** Was passiert, wenn die Masquerade-Regel vor der 1:1-Regel steht?

#### Kontrollfragen

1. Wozu braucht ein privates Netz ausgehendes NAT?
2. Warum genügt eine Portweiterleitung allein nicht?
3. Was ändert sich beim 1:1-NAT gegenüber der Masquerade?
4. Welche Rolle spielt die Verbindungstabelle?

### Modul 6: DHCP und DNS auf der Firewall

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen DHCP-Bereich mit Optionen und statischer Zuordnung planen.
  * Nach Abschluss dieses Moduls kann der Lernende lokale DNS-Einträge und Weiterleitung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer Adressvergabe im Mitschnitt oder Protokoll lesen.
* **Voraussetzungen:** Module 2 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | DHCP-Dienst: Adressbereich, Laufzeit, Optionen (Gateway, DNS, Domain), statische Zuordnung; Ablauf Discover-Offer-Request-Ack | 3 |
| 6.2 | DNS auf der Firewall: Weiterleitung (Forwarder), lokale Einträge, Ausfall des Dienstes | 3 |
| 6.3 | Praxis: `dhcp_dns.sh` ausführen (dnsmasq als Stand-in, `dhclient`, `dig`) | 2 |
| 6.4 | Planung: Bereiche außerhalb statischer Adressen, Namensschema, Folgen eines Ausfalls | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration lesen (Einheit 6.1):** Lesen Sie `dnsmasq-lan.conf` und ordnen Sie jede Zeile dem Zweck zu (Bereich, Gateway, DNS, statische Zuordnung, lokaler Eintrag).
2. **Adresse beziehen (Einheit 6.3):** Führen Sie den Client-Test aus und notieren Sie die vier Schritte und die Optionen aus dem Hook.
3. **DNS testen (Einheit 6.2):** Fragen Sie `srv.lab.test`, `extern.test` und einen unbekannten Namen ab und erklären Sie die drei Ergebnisse.
4. **Statische Zuordnung (Einheit 6.1):** Zeigen Sie, dass das Gerät mit der MAC `02:00:00:aa:bb:01` immer `10.8.1.60` erhält.
5. **Ausfall (Einheit 6.4):** Beenden Sie den Dienst und beschreiben Sie, was ein Client noch kann.

#### Kontrollfragen

1. Wie heißen die vier Schritte der DHCP-Vergabe?
2. Warum sollte der DHCP-Bereich keine statischen Adressen enthalten?
3. Was bedeutet `REFUSED` bei einer DNS-Abfrage?
4. Welche Folgen hat ein DNS-Ausfall auf der Firewall?

### Modul 7: Zertifikate und interne CA

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine interne CA aufbauen und Zertifikate für Server und Clients ausstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Kette, Name und Laufzeit prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende widerrufene Zertifikate erkennen.
* **Voraussetzungen:** Modul 1; `openssl`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Zertifikate, Ketten, SAN und Rollen (Server, Client); CA der Firewall und eigene CA (nicht bestätigt) | 2 |
| 7.2 | Praxis: CA, Server- und Clientzertifikat mit `openssl` erzeugen und prüfen | 3 |
| 7.3 | Sperrliste (CRL) und Prüfung widerrufener Zertifikate | 1 |
| 7.4 | Verwendung: Weboberfläche der Firewall, VPN, Benutzeranmeldung; Laufzeiten und Erneuerung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **CA erzeugen (Einheit 7.2):** Erzeugen Sie die CA (30 Tage) und zeigen Sie Aussteller, Inhaber und `CA:TRUE`.
2. **Serverzertifikat (Einheit 7.2):** Stellen Sie ein Zertifikat für `fw.lab.test` und `10.8.1.1` aus und prüfen Sie Kette, Name und Adresse.
3. **Clientzertifikat (Einheit 7.2):** Stellen Sie ein Clientzertifikat aus. Welche Erweiterung unterscheidet es vom Serverzertifikat?
4. **Widerruf (Einheit 7.3):** Widerrufen Sie das Clientzertifikat, erstellen Sie die Sperrliste und prüfen Sie beide Zertifikate damit.
5. **TLS-Test (Einheit 7.2):** Starten Sie `s_server` und prüfen Sie mit `s_client` (a) mit passendem Namen, (b) mit falschem Namen, (c) ohne CA. Notieren Sie die Rückgabecodes.
6. **Planung (Einheit 7.4):** Planen Sie die Laufzeiten für CA, Server und Clients und wer sie erneuert.

#### Kontrollfragen

1. Wozu dient das SAN-Feld?
2. Welche Aufgabe hat die Sperrliste (CRL)?
3. Warum dürfen der CA-Schlüssel und der Serverschlüssel nicht gemeinsam gespeichert werden?
4. Wie unterscheiden sich Server- und Clientzertifikate?

### Modul 8: VPN-Dienste: Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende VPN-Arten unterscheiden und einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzungen einer VPN-Einrichtung an der Firewall nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Schlüssel und Konfiguration vorbereiten.
* **Voraussetzungen:** Module 4, 5 und 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | VPN-Arten im Überblick: Standort-zu-Standort, Fernzugang; WireGuard, OpenVPN, IPsec; Einordnung (Vertiefung im Kurs „VPN“) | 2 |
| 8.2 | Was die Firewall für ein VPN braucht: Schlüssel oder Zertifikate, Port am WAN, Regeln auf der Tunnelschnittstelle, NAT | 2 |
| 8.3 | Praxis: `vpn_schluessel.sh` ausführen (Schlüssel, Konfiguration, Syntaxprüfung; kein Tunnel) | 1 |
| 8.4 | Planung eines Fernzugangs: Adressbereiche, erlaubte Ziele, Benutzer | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Arten einordnen (Einheit 8.1):** Ordnen Sie WireGuard, OpenVPN und IPsec nach Zweck und Einsatz (Tabelle, drei Spalten).
2. **Voraussetzungen (Einheit 8.2):** Listen Sie fünf Dinge auf, die an der Firewall für einen Fernzugang nötig sind.
3. **Schlüssel (Einheit 8.3):** Führen Sie das Skript aus und prüfen Sie Länge und Format der Schlüssel. Warum wird der private Schlüssel nicht angezeigt?
4. **Konfiguration (Einheit 8.3):** Lesen Sie die Konfiguration der Firewall-Seite und erklären Sie `Address`, `ListenPort` und `AllowedIPs`.
5. **Planung (Einheit 8.4):** Planen Sie einen Fernzugang für eine Person: Adresse im Tunnel, erlaubte Ziele, Regeln.

#### Kontrollfragen

1. Wo liegt der Unterschied zwischen Standort-zu-Standort und Fernzugang?
2. Welcher Port muss für WireGuard am WAN erreichbar sein?
3. Warum bleibt ein privater Schlüssel auf dem Gerät?
4. Was bewirkt `AllowedIPs`?

### Modul 9: IDS/IPS mit Suricata

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende IDS und IPS unterscheiden und Einsatz begründen.
  * Nach Abschluss dieses Moduls kann der Lernende eigene Regeln schreiben und mit einem Mitschnitt testen.
  * Nach Abschluss dieses Moduls kann der Lernende Meldungen lesen und bewerten.
* **Voraussetzungen:** Module 4 und 5; Grundkenntnisse in HTTP.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | IDS und IPS: Erkennung, Verhinderung, Einsatzorte; Betriebsarten; Folgen (Falschmeldungen, Last) | 2 |
| 9.2 | Regeln lesen und schreiben (Aktion, Protokoll, Richtung, Inhalt, `sid`); Regelquellen und Aktualisierung (nicht bestätigt) | 3 |
| 9.3 | Praxis: Mitschnitt erzeugen und mit Suricata 7.0.3 im Offline-Modus auswerten (`ids_demo.sh`) | 3 |
| 9.4 | Meldungen auswerten (`fast.log`, `eve.json`), Aktion `drop` im Offline- und im Inline-Betrieb, Ausnahmen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verkehr und Mitschnitt (Einheit 9.3):** Führen Sie das Skript aus und erklären Sie, welcher Verkehr erzeugt und mitgeschnitten wird.
2. **Regeln lesen (Einheit 9.2):** Erklären Sie die vier Regeln aus `ids.rules` Zeile für Zeile.
3. **Meldungen (Einheit 9.4):** Ordnen Sie jede Meldung der Datei `fast.log` einer Regel und einem Request zu.
4. **drop (Einheit 9.4):** Wie erkennen Sie im Offline-Modus, dass eine Regel `drop` ist? Wie würde sie im Inline-Betrieb wirken?
5. **Eigene Regel (Einheit 9.2):** Schreiben Sie eine Regel, die den Aufruf von `/admin` meldet, und testen Sie sie mit einem neuen Mitschnitt.
6. **Falschmeldungen (Einheit 9.1):** Nennen Sie zwei Ursachen für Falschmeldungen und eine Gegenmaßnahme.

#### Kontrollfragen

1. Wie unterscheiden sich IDS und IPS?
2. Was bedeutet `[wDrop]` in der Meldungsdatei?
3. Warum wird `http.uri.raw` für `../` benötigt?
4. Welche Nachteile hat ein IPS im Datenpfad?

### Modul 10: Hochverfügbarkeit (CARP-Prinzip)

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip von Master, Backup und virtueller Adresse erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen Ausfall und die Rückkehr des Masters prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen ohne Zustandsabgleich benennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Prinzip: zwei Firewalls, gemeinsame virtuelle Adresse, Master und Backup; CARP und pfsync in OPNsense (nicht bestätigt) und VRRP als Vergleich | 2 |
| 10.2 | Planung: Adressen je Firewall und virtuelle Adressen, Prioritäten, Abgleich von Konfiguration und Zuständen | 2 |
| 10.3 | Praxis: Adressübernahme mit keepalived (VRRP) im Labor (`vrrp_demo.sh`) | 3 |
| 10.4 | Grenzen: laufende Verbindungen, gleiche Regeln auf beiden Geräten, Test des Ausfalls | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Adressplan (Einheit 10.2):** Planen Sie für LAN und DMZ je drei Adressen (zwei Firewalls, eine virtuelle).
2. **Start (Einheit 10.3):** Starten Sie das Skript und lesen Sie, welche Firewall nach dem Start welche virtuelle Adresse hält.
3. **Ausfall (Einheit 10.3):** Beenden Sie den Dienst auf dem Master und messen Sie die Dauer bis zur Übernahme. Wie hängt sie vom Meldeintervall ab?
4. **Rückkehr (Einheit 10.3):** Starten Sie den alten Master erneut. Was geschieht, und warum?
5. **Zustände (Einheit 10.4):** Prüfen Sie, auf welcher Firewall die Verbindungstabelle einen Eintrag hat, und erklären Sie die Folge für laufende Verbindungen.

#### Kontrollfragen

1. Welche Aufgabe hat die virtuelle Adresse?
2. Wer wird Master, wenn zwei Geräte laufen?
3. Warum genügt die virtuelle Adresse allein nicht für unterbrechungsfreie Umschaltung?
4. Was muss auf beiden Geräten gleich sein?

### Modul 11: Sicherung der Konfiguration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherungsstrategie für eine Firewall planen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherungen prüfen, vergleichen und verschlüsselt aufbewahren.
  * Nach Abschluss dieses Moduls kann der Lernende vor dem Weitergeben Geheimnisse entfernen.
* **Voraussetzungen:** Module 3 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Was gesichert werden muss: Konfiguration, Zertifikate, Schlüssel; Export und Import in OPNsense (nicht bestätigt) | 2 |
| 11.2 | Prüfen und Vergleichen: Wohlgeformtheit (`xmllint`), Unterschiede (`diff`), Prüfsummen | 2 |
| 11.3 | Praxis: `config_sicherung.sh` ausführen (Beispieldatei, verschlüsseln, schwärzen, Aufbewahrung) | 2 |
| 11.4 | Wiederherstellung üben: Ablauf, Reihenfolge, Test nach dem Einspielen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Strategie (Einheit 11.1):** Legen Sie fest, wann gesichert wird (vor jeder Änderung, täglich), wie viele Stände bleiben und wo sie liegen.
2. **Prüfen (Einheit 11.2):** Prüfen Sie die Beispieldatei mit `xmllint` und zeigen Sie, wie eine fehlerhafte Datei auffällt.
3. **Vergleichen (Einheit 11.2):** Vergleichen Sie zwei Stände mit `diff` und erklären Sie die Änderung.
4. **Schwärzen (Einheit 11.3):** Entfernen Sie Kennwort-Hash und Schlüssel aus einer Kopie, die Sie weitergeben wollen.
5. **Verschlüsseln (Einheit 11.3):** Verschlüsseln und entschlüsseln Sie eine Sicherung mit `openssl` und prüfen Sie die Gleichheit. Was passiert mit falschem Kennwort?
6. **Wiederherstellung (Einheit 11.4):** Beschreiben Sie den Ablauf einer Wiederherstellung auf einer neuen Firewall in sechs Schritten.

#### Kontrollfragen

1. Warum gehört eine Sicherung der Konfiguration nicht unverschlüsselt in ein gemeinsames Laufwerk?
2. Wie prüft man, ob eine XML-Datei wohlgeformt ist?
3. Warum zählt die Aufbewahrung der letzten Stände?
4. Was gehört zu einem Wiederherstellungstest?

### Modul 12: Logging und Plugins

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende gezielt protokollieren und die Protokollmenge steuern.
  * Nach Abschluss dieses Moduls kann der Lernende Ereignisse auswerten (Häufigkeit nach Port und Quelle).
  * Nach Abschluss dieses Moduls kann der Lernende Nutzen und Risiken von Plugins bewerten.
* **Voraussetzungen:** Module 4 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Protokollierung von Filterereignissen: welche Regel protokolliert, Menge steuern; Systemprotokolle; Weiterleitung an einen Protokollserver (nicht bestätigt) | 2 |
| 12.2 | Praxis: Regeln mit `log group` (nflog) und Mitschnitt mit tcpdump (`log_auswertung.sh`); Auswertung mit `awk` | 3 |
| 12.3 | Plugins: Aufgaben, Paketnamen `os-…` (nicht bestätigt), Installation, Aktualisierung; Risiken und Auswahl | 2 |
| 12.4 | Betrieb: Speicherplatz, Aufbewahrung, Datenschutz bei Protokollen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Gezielt protokollieren (Einheit 12.1):** Lesen Sie die Regeln und erklären Sie, welche Regeln protokollieren und warum die Erlaubnisregel für Port 80 nicht.
2. **Mitschnitt (Einheit 12.2):** Führen Sie das Skript aus. Wie viele Protokollzeilen entstehen und aus welchen Regeln?
3. **Auswertung (Einheit 12.2):** Werten Sie aus, welche Ziel-Ports wie oft blockiert wurden, und erklären Sie die Zahlen.
4. **Zähler und Protokoll (Einheit 12.2):** Vergleichen Sie die Paketzähler der Regeln mit den Protokollzeilen.
5. **Plugin-Auswahl (Einheit 12.3):** Legen Sie fünf Kriterien fest, nach denen Sie ein Plugin einsetzen (Pflege, Nutzen, Aufwand, Risiko, Alternativen).
6. **Datenschutz (Einheit 12.4):** Nennen Sie zwei Maßnahmen, die Menge personenbezogener Daten im Protokoll zu begrenzen.

#### Kontrollfragen

1. Warum protokolliert man nicht jeden erlaubten Verkehr?
2. Was zeigt ein Zähler, was das Protokoll?
3. Welche Risiken haben Plugins?
4. Welche Daten im Protokoll sind datenschutzrelevant?

### Modul 13: Fehlersuche und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Fehler an Zählern und Mitschnitten eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler erkennen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende ein vollständiges Regelwerk dokumentieren und gegen einen Testkatalog prüfen.
* **Voraussetzungen:** Module 2 bis 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Systematisches Vorgehen: Symptom, Schicht, Zähler, Mitschnitt, Änderung, Test; Diagnosewerkzeuge der Firewall | 2 |
| 13.2 | Typische Fehler: Reihenfolge, fehlendes NAT, Weiterleitung ohne Filterregel, falsches Gateway, Tippfehler im Alias | 2 |
| 13.3 | Praxis: `fehlersuche.sh` ausführen und jeden Fall zuordnen | 2 |
| 13.4 | Abschlussprojekt: komplettes Regelwerk für das Labor mit Testkatalog (`abschluss_loesung.nft`, `abschluss_test.sh`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fälle zuordnen (Einheit 13.3):** Führen Sie `bash fehlersuche.sh` aus und ordnen Sie jedem der fünf Fehler Symptom, Diagnose und Korrektur zu.
2. **Zähler lesen (Einheit 13.2):** Erklären Sie an Fehler 1 und Fehler 3, wie Zähler den Fehler zeigen.
3. **Mitschnitt lesen (Einheit 13.2):** Erklären Sie an Fehler 2 und Fehler 4, was der Mitschnitt zeigt.
4. **Vorgehen (Einheit 13.1):** Beschreiben Sie in fünf Schritten Ihr Vorgehen bei „kein Zugriff“.
5. **Abschlussprojekt (Einheit 13.4):** Bauen Sie das Regelwerk nach den Anforderungen (LAN → DMZ nur Web, SSH gesperrt mit Protokoll, LAN → Internet nur Web mit NAT, DMZ ohne Zugriff nach außen, Portweiterleitung WAN 8080 → Server 80, WAN nur dorthin, nur LAN darf die Firewall anpingen) und schreiben Sie einen Testkatalog.
6. **Abnahme (Einheit 13.4):** Führen Sie `abschluss_test.sh` mit Ihrer Lösung aus und dokumentieren Sie das Ergebnis.

#### Kontrollfragen

1. Welche Reihenfolge der Prüfung empfiehlt sich bei „kein Zugriff“?
2. Woran erkennt man eine Portweiterleitung ohne passende Filterregel?
3. Wie zeigt ein ARP-Mitschnitt ein falsches Gateway?
4. Warum gehört zu einem Regelwerk ein Testkatalog?
