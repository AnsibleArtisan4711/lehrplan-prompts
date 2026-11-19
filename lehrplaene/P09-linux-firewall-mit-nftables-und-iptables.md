# Lehrplan: Linux-Firewall mit nftables und iptables

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Shell, Dateien, Pakete installieren, Dienste starten) |
| **Gesamtumfang** | 13 Module, 106 UE (zu 45 Minuten; 79,5 Stunden) |
| **Fokus-Technologien** | Debian/Ubuntu Linux, nftables, iptables |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise auf vorhandene Lehrpläne nur kurz. Nicht behandelt: OPNsense und andere Firewall-Appliances (eigener Kurs), VPN-Tunnel (Kurs „VPN mit WireGuard und OpenVPN“), Reverse Proxy und TLS (eigener Kurs), Hochverfügbarkeit (keepalived, conntrackd), eBPF/XDP |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Netfilter-Architektur und Laborumgebung | 1 | 7 |
| 2 | nftables: Tabellen, Ketten und Regeln | 1 | 9 |
| 3 | Host-Firewall für einen Server | 1 | 9 |
| 4 | Zustandsverfolgung (Connection Tracking) | 1 | 9 |
| 5 | Sets, Maps und Verdict-Maps | 2 | 8 |
| 6 | NAT: Masquerade, Port-Weiterleitung und Redirect | 1 | 9 |
| 7 | Router-Firewall mit Zonen (forward) | 1 | 9 |
| 8 | Rate Limiting und Protokollierung | 1 | 8 |
| 9 | Regelsätze sichern, laden und dauerhaft machen | 1 | 7 |
| 10 | iptables: Grundlagen und das Verhältnis zu nftables | 1 | 8 |
| 11 | Migration von iptables zu nftables | 1 | 8 |
| 12 | firewalld und ufw in Grundzügen | 2 | 6 |
| 13 | Fehlersuche und Abschlussprojekt | 1 | 9 |
| **Gesamt** | 13 Module | 11 × Priorität 1, 2 × Priorität 2 | **106** |

**Priorität 1** (Pflicht) sind die Module 1 bis 4, 6 bis 11 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) sind Modul 5 (Sets, Maps und Verdict-Maps) und Modul 12 (firewalld und ufw in Grundzügen). Fallen beide weg, verringert sich der Gesamtumfang auf 92 UE.

### 2. Quellen

**Keine Quelle wurde gegen das Original gelesen.** Alle Befehle und Ausgaben stammen aus Läufen im Labor-Container (Debian/Ubuntu-Umgebung, nftables 1.0.9, iptables 1.8.10 (nf_tables), conntrack-tools 1.4.8, firewalld 2.1.1, ufw 0.36.2, tcpdump) und aus Fachwissen. Die Handbuchseiten (`nft(8)`, `iptables(8)`, `iptables-extensions(8)`) und die Dokumentation von Netfilter sind **nicht** gelesen; wo eine Aussage über das Beobachtete hinausgeht, ist sie in der Übung mit „nicht bestätigt“ gekennzeichnet. Das Verhalten der Debian-12-Versionen (nftables 1.0.6, iptables 1.8.9) ist nicht geprüft.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switches:** zwei private Switches ohne Verbindung zum Heimnetz: `Lab-LAN-Net` (`10.0.1.0/24`) und `Lab-SRV-Net` (`10.0.2.0/24`); die Firewall-VM hängt an beiden.

**VMs:** `fw01` (Debian 12, 2 vCPU, 1 GB RAM, zwei Netzwerkkarten: `10.0.1.1` und `10.0.2.1`; Pakete `nftables`, `iptables`, `conntrack`, `tcpdump`, in Modul 12 zusätzlich `firewalld` und `ufw`), `cl01` (Debian oder Ubuntu, `10.0.1.2`, Standard-Gateway `10.0.1.1`) und `srv01` (Debian 12, `10.0.2.2`, Gateway `10.0.2.1`, Webserver oder `python3 -m http.server` auf den Ports 80 und 8080). Alle Adressen statisch, kein DHCP und kein DNS.

**Pakete** werden einmalig vor Kursbeginn mit Internetzugang (temporär eine zusätzliche NAT-Karte) installiert und die Karte danach entfernt. **Kontrollpunkt (Checkpoint):** Vor jedem Modul mit Änderungen an der Firewall einen Hyper-V-Prüfpunkt von `fw01` anlegen; wer sich aussperrt, kehrt dorthin zurück.

**Skripte:** Die Beispielskripte bauen dieses Labor als drei Netzwerk-Namespaces auf einer einzelnen Linux-Maschine nach (Schreibweise `on fw …` = „im Namespace der Firewall ausführen“). In den VMs entfallen das Präfix und die Hilfsfunktionen: Die `nft`- und `iptables`-Befehle sind dieselben.

## B. Detaillierter Modulaufbau

### Modul 1: Netfilter-Architektur und Laborumgebung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Weg eines Pakets durch die fünf Netfilter-Hooks beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie nftables, iptables, firewalld und ufw zusammenhängen.
  * Nach Abschluss dieses Moduls kann der Lernende das Drei-Rechner-Labor aufbauen und seine Erreichbarkeit prüfen.
* **Voraussetzungen:** Grundkenntnisse in IP-Netzen und in der Linux-Shell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Netfilter im Kernel: fünf Hooks (prerouting, input, forward, output, postrouting), Weg eines Pakets | 2 |
| 1.2 | Werkzeuge im Überblick: nftables (`nft`), iptables (`iptables-nft`, `iptables-legacy`), Frontends (firewalld, ufw) und ihr Verhältnis zueinander | 2 |
| 1.3 | Laborumgebung aufbauen und prüfen: Adressen, Routing, `ip_forward`, Prüfpunkte | 1 |
| 1.4 | Praxis: Pakete in den Hooks mitzählen (`pfad_zaehlen.sh`) und die Wege Durchgang, Eingang und Ausgang unterscheiden | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Labor aufbauen (Einheit 1.3):** Richten Sie `fw01`, `cl01` und `srv01` nach der Laborbeschreibung ein und prüfen Sie mit `ping` und `ip route`, dass `cl01` den Server über die Firewall erreicht. Prüfen Sie `sysctl net.ipv4.ip_forward`.
2. **Hooks mitzählen (Einheit 1.4):** Führen Sie `bash pfad_zaehlen.sh` aus (oder legen Sie in der Firewall-VM selbst fünf Ketten mit `counter` an). Notieren Sie für drei Pakete (Client zum Server, Client zur Firewall, Firewall zum Server), in welchen Hooks die Zähler steigen.
3. **Weg zeichnen (Einheit 1.1):** Zeichnen Sie für die drei Pakete den Weg durch die Hooks als Skizze und markieren Sie, wo Routing-Entscheidungen fallen.
4. **Werkzeuge zuordnen (Einheit 1.2):** Stellen Sie mit `iptables --version` und `nft list ruleset` fest, welche iptables-Variante im Labor läuft, und erklären Sie in zwei Sätzen, was „nf_tables“ in der Ausgabe bedeutet.

#### Kontrollfragen

1. In welchen Hooks taucht ein Paket auf, das ein Client durch die Firewall zu einem Server schickt?
2. Warum zählt bei einem Ping drei Hooks doppelt (Anfrage und Antwort)?
3. Was bedeutet „iptables v1.8.10 (nf_tables)“, und was ändert sich für die Regeln im Kern?
4. Was passiert mit Weiterleitung, wenn `net.ipv4.ip_forward` auf 0 steht?

### Modul 2: nftables: Tabellen, Ketten und Regeln

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Tabellen, Basis-Ketten und reguläre Ketten anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln einfügen, anhand des Handles löschen und die Reihenfolge steuern.
  * Nach Abschluss dieses Moduls kann der Lernende Familien und Prioritäten einordnen.
* **Voraussetzungen:** Modul 1; Zugriff auf `fw01` (root).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Objekte: Tabelle (Familie `ip`, `ip6`, `inet`), Kette (Basis-Kette und reguläre Kette), Regel; Prioritäten und Richtlinie (policy) | 3 |
| 2.2 | Regeln hinzufügen und ändern: `add`, `insert`, `replace`, `delete` (mit Handle), `flush`, `-a` | 3 |
| 2.3 | Praxis: Skript `nft_grundlagen.sh` ausführen und die Befehle nachvollziehen | 2 |
| 2.4 | Verzweigen mit `jump` und `goto`, Ketten aufräumen, typische Fehlermeldungen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tabelle und Kette (Einheit 2.1):** Legen Sie in `fw01` eine Tabelle `inet demo` mit Basis-Kette `input` (policy accept) an und zeigen Sie sie mit `nft -a list table inet demo`.
2. **Reihenfolge (Einheit 2.2):** Fügen Sie eine Regel für Port 22 an das Ende (`add`) und eine für das Loopback an den Anfang (`insert`) an. Erklären Sie, warum die Reihenfolge wirkt.
3. **Regel löschen (Einheit 2.2):** Löschen Sie die Regel für Port 23 anhand des Handles (aus `nft -a`).
4. **Skript lesen (Einheit 2.3):** Führen Sie `bash nft_grundlagen.sh` aus und erklären Sie jede Ausgabe in eigenen Worten.
5. **Sprung und Fehlermeldung (Einheit 2.4):** Legen Sie eine reguläre Kette `web` an, springen Sie mit `jump web` hinein und versuchen Sie, `web` zu löschen. Welche Meldung kommt, und warum?

#### Kontrollfragen

1. Was ist der Unterschied zwischen einer Basis-Kette und einer regulären Kette?
2. Wann ist die Familie `inet` sinnvoll?
3. Wie löscht man eine einzelne Regel gezielt?
4. Was bewirkt `policy drop` in einer Basis-Kette?

### Modul 3: Host-Firewall für einen Server

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine restriktive Eingangsfirewall für einen Server schreiben, prüfen und laden.
  * Nach Abschluss dieses Moduls kann der Lernende Dienste gezielt nach Quelladresse freigeben.
  * Nach Abschluss dieses Moduls kann der Lernende sich beim Testen nicht selbst aussperren.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Grundsatz „alles verbieten, was nicht erlaubt ist“: policy drop, Loopback, `ct state`, Dienste, ICMP | 3 |
| 3.2 | Regelwerk als Datei: `nft -c -f` (Prüfung), `nft -f` (Laden), Kommentare, Variablen mit `define` | 2 |
| 3.3 | Praxis: `host_firewall.nft` laden und aus dem Client testen (`host_firewall_test.sh`) | 3 |
| 3.4 | Zähler auswerten, Ausschluss durch Aussperren vermeiden (Prüfpunkt, zeitgesteuertes Zurücksetzen) | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regelwerk prüfen und laden (Einheit 3.2):** Prüfen Sie `host_firewall.nft` mit `nft -c -f` und laden Sie es auf `srv01`. Erklären Sie jede Regel mit einem Satz.
2. **Zugriffe testen (Einheit 3.3):** Führen Sie `bash host_firewall_test.sh` aus (oder testen Sie in den VMs: `ping`, `curl` auf Port 80 und 8080). Welche Zugriffe sind erlaubt, welche verworfen?
3. **Quelladresse (Einheit 3.1):** Sorgen Sie dafür, dass Port 8080 nur aus `10.0.1.0/24` erreichbar ist, und beweisen Sie es mit einer zweiten Quelladresse.
4. **Zähler (Einheit 3.4):** Lesen Sie den Zähler der letzten Regel. Welche Pakete zählt er, und was sagt er über Port-Scans?
5. **Aussperren vermeiden (Einheit 3.4):** Beschreiben Sie, wie Sie vor einer Änderung an der Firewall (per SSH) einen Rückweg sichern (Prüfpunkt, `at`-Job mit `nft flush ruleset`).

#### Kontrollfragen

1. Warum gehört `iif "lo" accept` an den Anfang der Eingangskette?
2. Was bewirkt `ct state established,related accept`, und was würde ohne diese Regel passieren?
3. Warum begrenzt man ICMP-Echo-Anfragen, statt ICMP ganz zu sperren?
4. Was zählt der Zähler in der letzten Regel einer Kette mit policy drop?

### Modul 4: Zustandsverfolgung (Connection Tracking)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Zustände einer Verbindung erklären und in Regeln verwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Einträge der Verbindungstabelle lesen.
  * Nach Abschluss dieses Moduls kann der Lernende verstehen, warum eine zustandslose Rückrichtung scheitert.
* **Voraussetzungen:** Modul 3; `conntrack` (Paket `conntrack`) installiert.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Verbindungszustände: new, established, related, invalid; auch UDP und ICMP haben Zustand | 3 |
| 4.2 | Tabelle der Verbindungen lesen: `conntrack -L`, `-E`, `-C`, Zeitlimits (sysctl) | 2 |
| 4.3 | Praxis: `conntrack_demo.sh` – TCP, UDP, ICMP und die Rückrichtung | 3 |
| 4.4 | Grenzen und Fallstricke: Tabellengröße, `invalid`, ICMP-Besonderheit, ct status | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verbindungen lesen (Einheit 4.2):** Führen Sie `bash conntrack_demo.sh` aus. Lesen Sie den TCP-Eintrag und nennen Sie Quelle, Ziel, Zustand und das Flag `[ASSURED]`.
2. **Zustände in Regeln (Einheit 4.1):** Erklären Sie anhand der Zähler im Skript, welche Regel die Antwortpakete durchlässt und welche nur das erste Paket.
3. **UDP und ICMP (Einheit 4.3):** Zeigen Sie, dass UDP-Antworten und ICMP-Antworten ohne eigene Regel durchkommen, und lesen Sie die Einträge.
4. **Rückrichtung (Einheit 4.3):** Zeigen Sie, dass der Server den Client nicht von sich aus erreichen kann, und begründen Sie das mit den Zuständen.
5. **Zeitlimits (Einheit 4.4):** Lesen Sie die sysctl-Zeitlimits für TCP, UDP und ICMP und erklären Sie die großen Unterschiede.

#### Kontrollfragen

1. Welche vier Zustände kennt `ct state`, und was bedeuten sie?
2. Warum kann auch eine UDP-„Verbindung“ als established gelten?
3. Wie lange bleibt eine beendete TCP-Verbindung in der Tabelle?
4. Was kann passieren, wenn die Verbindungstabelle voll ist?

### Modul 5: Sets, Maps und Verdict-Maps

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Sets mit Timeout und Intervallen anlegen und zur Laufzeit ändern.
  * Nach Abschluss dieses Moduls kann der Lernende eine Verdict-Map für Dienste einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Regelwerke mit Sets verkürzen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Sets: benannt, anonym, Intervalle, Timeout, dynamisch; Verkettung (Adresse . Port) | 3 |
| 5.2 | Maps und Verdict-Maps: Port oder Adresse einer Aktion zuordnen | 2 |
| 5.3 | Praxis: `sets_maps.nft` laden und Elemente zur Laufzeit ändern (`sets_demo.sh`) | 2 |
| 5.4 | Wann Sets besser sind als viele Einzelregeln | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Set mit Timeout (Einheit 5.1):** Laden Sie `sets_maps.nft` auf `srv01`. Sperren Sie den Client mit `nft add element … gesperrt { 10.0.1.2 timeout 5m }` und zeigen Sie die Wirkung und den Rest-Timeout.
2. **Intervall-Set (Einheit 5.1):** Entfernen Sie das Client-Netz aus dem Set `intern` und erklären Sie die Wirkung auf Port 8080.
3. **Verdict-Map (Einheit 5.2):** Fügen Sie der Map `dienste` den Port 443 mit `accept` hinzu und erklären Sie den Vorteil gegenüber drei Einzelregeln.
4. **Skript auswerten (Einheit 5.3):** Führen Sie `bash sets_demo.sh` aus und erklären Sie jede der sechs Ausgaben.
5. **Entscheidung (Einheit 5.4):** Nennen Sie zwei Fälle, in denen ein Set sinnvoll ist, und einen, in dem eine Einzelregel reicht.

#### Kontrollfragen

1. Wozu dient das Flag `timeout` bei einem Set?
2. Was ist eine Verkettung `ipv4_addr . inet_service`?
3. Was ist eine Verdict-Map?
4. Was gilt für Elemente, die Sie zur Laufzeit hinzufügen, nach einem Neuladen der Datei?

### Modul 6: NAT: Masquerade, Port-Weiterleitung und Redirect

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Masquerade und DNAT einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende am Server die gesehene Quelladresse vor und nach NAT bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende Filter- und NAT-Regeln zusammen richtig anordnen.
* **Voraussetzungen:** Module 3 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | SNAT, Masquerade, DNAT und Redirect; Ketten- und Hook-Typ `nat`; Zusammenspiel mit conntrack | 3 |
| 6.2 | Regeln: `masquerade`, `snat to`, `dnat to`, `redirect to` und die Priorität (srcnat/dstnat) | 2 |
| 6.3 | Praxis: `nat_demo.sh` ausführen und Quelladresse beim Server beobachten | 3 |
| 6.4 | NAT und Filter zusammen: `ct status dnat`, forward-Regeln für weitergeleitete Verbindungen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Quelladresse ohne NAT (Einheit 6.3):** Lassen Sie `cl01` auf `srv01` zugreifen, während der Server die Quelladresse ausgibt (`whoami.py`). Notieren Sie die Adresse.
2. **Masquerade (Einheit 6.2):** Aktivieren Sie `masquerade` für den Ausgang zum Server-Netz und wiederholen Sie den Test. Lesen Sie den Eintrag mit `conntrack -L`.
3. **Port-Weiterleitung (Einheit 6.2):** Leiten Sie Aufrufe an `10.0.1.1:8000` mit `dnat` zu `10.0.2.2:8080` um und testen Sie sie.
4. **Filter und DNAT (Einheit 6.4):** Setzen Sie in der Firewall policy drop in forward und erlauben Sie nur Verbindungen mit `ct status dnat`. Zeigen Sie, dass die direkte Verbindung zu 10.0.2.2:8080 danach verworfen wird.
5. **Redirect (Einheit 6.1):** Leiten Sie Port 9000 der Firewall auf den lokalen Port 3128 um und prüfen Sie den HTTP-Status.

#### Kontrollfragen

1. Wo im Weg eines Pakets findet DNAT statt, und wo SNAT?
2. Warum sieht der Server nach Masquerade die Adresse der Firewall?
3. Warum braucht man bei Masquerade keine Rückregel?
4. Was ist der Unterschied zwischen `dnat` und `redirect`?

### Modul 7: Router-Firewall mit Zonen (forward)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Zonenmodell mit Richtungsketten umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln pro Richtung messen und beweisen.
  * Nach Abschluss dieses Moduls kann der Lernende Eigen- und Durchgangsverkehr getrennt behandeln.
* **Voraussetzungen:** Module 3 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Zonenmodell: LAN und Server; Richtungen; Standard verwerfen; Ketten pro Richtung (`jump`) | 3 |
| 7.2 | Schnittstellen in Regeln: `iifname`, `oifname`, Variablen mit `define`, Port-Sets | 2 |
| 7.3 | Praxis: `zonen.nft` laden und in beide Richtungen testen (`zonen_test.sh`) | 3 |
| 7.4 | Eigenverkehr der Firewall (input/output) von Durchgangsverkehr (forward) trennen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regelwerk lesen (Einheit 7.1):** Laden Sie `zonen.nft` auf `fw01` und beschreiben Sie, welche Richtung welche Kette bekommt.
2. **Tests LAN zu Server (Einheit 7.3):** Führen Sie `bash zonen_test.sh` aus und prüfen Sie Ping, Port 80, Port 8080 und Port 22 vom Client.
3. **Rückrichtung (Einheit 7.3):** Zeigen Sie, dass der Server nichts ins LAN öffnen kann, und lesen Sie den Zähler der Kette `srv_zu_lan`.
4. **Schnittstellen und Sets (Einheit 7.2):** Ergänzen Sie den Port 443 im Set `web_ports` und erklären Sie, warum die Kette nicht geändert werden muss.
5. **Eigenverkehr (Einheit 7.4):** Erlauben Sie Ping an die Firewall nur aus dem LAN und beweisen Sie, dass er aus der Server-Zone verworfen wird.

#### Kontrollfragen

1. Warum zwei getrennte Richtungsketten statt einer langen forward-Kette?
2. Was ist der Unterschied zwischen den Hooks input und forward bei einer Firewall?
3. Warum ist `iifname` bei wechselnden Schnittstellen flexibler als `iif`?
4. Was zeigt der Zähler der letzten forward-Regel?

### Modul 8: Rate Limiting und Protokollierung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Pakete mit `limit rate` begrenzen und den Überschuss zählen.
  * Nach Abschluss dieses Moduls kann der Lernende neue Verbindungen je Quelladresse begrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Verworfene Pakete protokollieren und lesen.
* **Voraussetzungen:** Modul 3 (Modul 5 hilfreich).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Begrenzen: `limit rate`, `burst`, `over`; Zähler (`counter`, benannte Zähler) | 2 |
| 8.2 | Je Quelladresse begrenzen mit dynamischem Set (meter); Brute-Force-Schutz | 2 |
| 8.3 | Protokollieren: `log`, Präfix, `log group` (nflog), Auswertung mit tcpdump | 2 |
| 8.4 | Praxis: `limit_log.sh` ausführen und Ergebnisse deuten (inklusive der ICMP-Falle) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ping begrenzen (Einheit 8.1):** Führen Sie `bash limit_log.sh` aus. Wie viele der 40 Pakete kamen an, wie viele zählt der Zähler als Überschuss?
2. **Reihenfolge (Einheit 8.4):** Erklären Sie, warum die Limit-Regel vor `ct state established` stehen muss (siehe Hinweis zur ICMP-Falle).
3. **Verbindungen je Adresse (Einheit 8.2):** Prüfen Sie, dass von sechs Verbindungsversuchen auf Port 8080 die ersten drei durchgehen und die weiteren verworfen werden, und lesen Sie das dynamische Set.
4. **Protokoll lesen (Einheit 8.3):** Lesen Sie die Protokollpakete der Gruppen 1 und 2 mit `tcpdump -v -i nflog:1`. Was ist mit dem Präfix?
5. **Kernel-Log (Einheit 8.3):** Beschreiben Sie, wo ein `log`-Eintrag ohne `group` landet und wie man ihn liest (`journalctl -k`).

#### Kontrollfragen

1. Was bedeutet `limit rate 10/second burst 5 packets`?
2. Warum bringt eine einzige Regel `limit rate` ohne Quelladresse bei vielen Clients wenig Schutz?
3. Warum zählen wiederholte Pings im selben Aufruf nicht als neue Verbindungen?
4. Wie kommen Protokolleinträge in eine Datei, ohne dass der Kernel-Puffer überläuft?

### Modul 9: Regelsätze sichern, laden und dauerhaft machen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Regelwerk prüfen, sichern, laden und atomar austauschen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Konfiguration in Dateien mit include aufteilen.
  * Nach Abschluss dieses Moduls kann der Lernende die Falle bei relativen include-Pfaden erkennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Regelwerk als Datei: `nft list ruleset`, `nft -f`, `nft -c`, Transaktionen und Atomarität | 2 |
| 9.2 | Aufbau von `/etc/nftables.conf` mit `include` und Suchpfad; die Falle des leeren Glob | 2 |
| 9.3 | Praxis: `sichern_laden.sh` ausführen (fehlerhafte Datei, Austausch, Rückkehr zur Sicherung) | 2 |
| 9.4 | Dauerhaft: `nftables.service`, `reload`, Sicherung im Backup-Konzept | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **include ausprobieren (Einheit 9.2):** Führen Sie `bash sichern_laden.sh` aus. Warum bleibt das Regelwerk beim ersten Laden leer, obwohl kein Fehler gemeldet wird?
2. **Prüfen vor Laden (Einheit 9.1):** Prüfen Sie die Datei mit `nft -I . -c -f nftables.conf` und laden Sie sie danach.
3. **Fehlerhafte Datei (Einheit 9.1):** Zeigen Sie, dass eine Datei mit ungültigem Port das laufende Regelwerk unverändert lässt.
4. **Sichern und zurückspielen (Einheit 9.3):** Sichern Sie das laufende Regelwerk mit `nft list ruleset > sicherung.nft`, löschen Sie es (`flush ruleset`) und spielen Sie es zurück. Was gilt in der Zwischenzeit für den Server?
5. **Dauerhaft machen (Einheit 9.4):** Beschreiben Sie, wie `nftables.service` die Datei lädt, wie man neu lädt und wie die Datei in die Datensicherung kommt (Modul „Backup-Konzept“).

#### Kontrollfragen

1. Warum ist `nft -f` mit einer fehlerhaften Datei sicher?
2. Was bewirkt `flush ruleset` am Anfang einer Datei?
3. Warum findet `include "conf.d/*.nft"` ohne `-I` in dieser Umgebung nichts?
4. Was ist beim Zurückspielen aus einer Sicherung ein Zeitfenster-Risiko?

### Modul 10: iptables: Grundlagen und das Verhältnis zu nftables

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein einfaches Filter- und NAT-Regelwerk mit iptables schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln mit Nummern einfügen, ersetzen und löschen.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, dass iptables-nft Regeln als nftables-Objekte anlegt.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Tabellen und Ketten in iptables (filter, nat, mangle, raw), Ziele (ACCEPT, DROP, REJECT, LOG), Module (`-m conntrack`, `-m limit`) | 2 |
| 10.2 | Regeln verwalten: `-A`, `-I`, `-R`, `-D`, `-L -n -v --line-numbers`, `-S`, `-P` | 2 |
| 10.3 | iptables-nft und iptables-legacy: zwei Befehle, zwei Kernschnittstellen | 1 |
| 10.4 | Praxis: `iptables_grundlagen.sh` ausführen (Server-Eingang, Router mit NAT) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Server-Eingang (Einheit 10.2):** Setzen Sie auf `srv01` die policy von INPUT auf DROP und erlauben Sie Loopback, established/related, Port 80 und Ping (begrenzt). Testen Sie vom Client.
2. **Regeln verwalten (Einheit 10.2):** Fügen Sie mit `-I` eine Regel für Port 8080 an Position 3 ein, ersetzen Sie sie mit `-R` durch ein anderes Netz und löschen Sie sie mit `-D`. Zeigen Sie nach jedem Schritt den Zustand mit `-L -n -v --line-numbers`.
3. **Router mit NAT (Einheit 10.4):** Setzen Sie in `fw01` policy DROP für FORWARD, erlauben Sie established/related und Port 80 aus dem LAN und aktivieren Sie MASQUERADE.
4. **Zähler lesen (Einheit 10.1):** Lesen Sie die Zähler (`-v`) und erklären Sie die Spalten pkts, bytes, in, out.
5. **Sicht von nft (Einheit 10.3):** Zeigen Sie mit `nft list ruleset` die iptables-Regeln und erklären Sie den Warnhinweis „managed by iptables-nft“. Wie finden Sie heraus, ob `iptables-legacy` installiert ist (`update-alternatives`)?

#### Kontrollfragen

1. Wie unterscheiden sich die Ziele DROP und REJECT?
2. Wozu dient `-m conntrack --ctstate ESTABLISHED,RELATED`?
3. Was bedeutet der Warnhinweis „table ip filter is managed by iptables-nft, do not touch!“?
4. Welcher Unterschied besteht zwischen `-I INPUT` und `-A INPUT`?

### Modul 11: Migration von iptables zu nftables

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein bestehendes iptables-Regelwerk übersetzen und laden.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten vor und nach der Migration mit einem festen Testkatalog vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln erkennen, die nicht automatisch übersetzt werden.
* **Voraussetzungen:** Module 6 und 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Vorgehen: Bestand sichern (`iptables-save`), übersetzen, prüfen, laden, vergleichen | 2 |
| 11.2 | Werkzeuge: `iptables-restore-translate`, `iptables-translate`, `ip6tables-translate`; was nicht übersetzt wird | 2 |
| 11.3 | Praxis: `migration.sh` ausführen (Altbestand laden, übersetzen, Verhalten vergleichen) | 3 |
| 11.4 | Nacharbeit: Struktur verbessern (Sets, inet, Zonenketten), Übersetzung ist nur der erste Schritt | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bestand laden und sichern (Einheit 11.1):** Laden Sie `alt.rules` mit `iptables-restore` und führen Sie den Testkatalog aus (im Skript `matrix`). Sichern Sie den Bestand mit `iptables-save`.
2. **Übersetzen (Einheit 11.2):** Übersetzen Sie mit `iptables-restore-translate -f` und lesen Sie die Datei. Welche Regeln haben sich verändert (z. B. `multiport`)?
3. **Einzelregeln (Einheit 11.2):** Übersetzen Sie die drei Beispielregeln mit `iptables-translate`; was passiert mit dem Modul `recent`?
4. **Umschalten und vergleichen (Einheit 11.3):** Entfernen Sie den Altbestand, laden Sie `neu.nft` und vergleichen Sie die Testkataloge vorher/nachher mit `diff`.
5. **Aufräumen (Einheit 11.4):** Verbessern Sie die übersetzte Datei: Familie `inet`, ein Set für die Ports, sprechende Kettennamen. Wiederholen Sie den Vergleich.

#### Kontrollfragen

1. Warum ist der Vergleich mit einem festen Testkatalog wichtiger als der Vergleich der Regeltexte?
2. Welche Regel aus dem Beispiel kann `iptables-translate` nicht übersetzen?
3. Was ändert sich bei `multiport` in nftables?
4. Warum sollte man nach der automatischen Übersetzung noch nacharbeiten?

### Modul 12: firewalld und ufw in Grundzügen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende mit ufw einen Server absichern.
  * Nach Abschluss dieses Moduls kann der Lernende mit firewalld Zonen und Richtlinien einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Aufwand und Nutzen von Frontends einschätzen.
* **Voraussetzungen:** Module 10 und 6; `ufw`, `firewalld` installiert.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | ufw: Standardrichtlinien, `allow`, `limit`, `status`, Regeln aus Sicht von iptables | 2 |
| 12.2 | firewalld: Zonen, Dienste, Policies zwischen Zonen, rich rules, Laufzeit gegen dauerhaft | 2 |
| 12.3 | Praxis: `ufw_firewalld.sh` ausführen und die erzeugten Regeln (Tabellen, Ketten) betrachten | 1 |
| 12.4 | Wann ein Frontend, wann direkt nft/iptables; Zusammenspiel und Konflikte | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **ufw-Server (Einheit 12.1):** Richten Sie auf `srv01` mit ufw Port 80 für alle, Port 8080 nur aus `10.0.1.0/24` und `limit` für SSH ein und lesen Sie `ufw status numbered`.
2. **Darunterliegende Regeln (Einheit 12.3):** Finden Sie die ufw-Regeln für Port 80 und 8080 in `iptables -S` und benennen Sie die Kette.
3. **Zonen in firewalld (Einheit 12.2):** Weisen Sie die Schnittstellen dauerhaft den Zonen `internal` und `external` zu und beweisen Sie die Zuordnung mit `--get-active-zones`.
4. **Policy zwischen Zonen (Einheit 12.2):** Legen Sie die Policy `lan_zu_srv` an (nur Port 80 per rich rule) und erklären Sie, warum sie erst nach `--reload` wirkt.
5. **Entscheidung (Einheit 12.4):** Begründen Sie in einem Absatz, wann Sie firewalld oder ufw, wann direkt nftables einsetzen.

#### Kontrollfragen

1. Wie unterscheiden sich die Konzepte von ufw und firewalld im Kern?
2. Was heißt „Laufzeit“ gegenüber „permanent“ in firewalld?
3. Warum sollte man nftables-Regeln nicht neben firewalld von Hand ändern?
4. Welches Backend verwendet ufw, und woran erkennt man es?

### Modul 13: Fehlersuche und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Fehler im Regelwerk systematisch eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende mit Zählern, tcpdump und nft trace die Ursache belegen.
  * Nach Abschluss dieses Moduls kann der Lernende ein vollständiges Regelwerk dokumentieren und testen.
* **Voraussetzungen:** Module 3 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Systematik: Symptom, Hypothese, Messung (Zähler, tcpdump, trace), Änderung, Kontrolle | 2 |
| 13.2 | Werkzeuge: `nft list` mit Zählern, `nft monitor trace`, `tcpdump`, `ip -br link`, `sysctl` | 2 |
| 13.3 | Praxis: `fehlersuche.sh` – vier eingebaute Fehler diagnostizieren und beheben | 3 |
| 13.4 | Abschlussprojekt: Firewall für das komplette Labor mit Dokumentation und Testkatalog | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Reihenfolge (Einheit 13.3):** Führen Sie `bash fehlersuche.sh` aus. Erklären Sie bei Fehler 1, wie der Zähler die Ursache zeigt, und beheben Sie den Fehler selbst per Handle.
2. **Schnittstellenname (Einheit 13.2):** Erklären Sie bei Fehler 2, wie `ip -br link` die Ursache zeigt.
3. **Rückrichtung (Einheit 13.2):** Erklären Sie bei Fehler 3 die tcpdump-Zählung (SYN/SYN-ACK innen und außen).
4. **trace (Einheit 13.2):** Verfolgen Sie ein Paket mit `meta nftrace set 1` und `nft monitor trace` und beschreiben Sie den Weg durch die Ketten.
5. **Abschlussprojekt (Einheit 13.4):** Schreiben Sie die Firewall für `fw01` aus den Anforderungen: LAN zum Server nur Port 80 und 8080; Server zu LAN nichts; Ping zur Firewall nur aus dem LAN; Masquerade zum Server-Netz; Port-Weiterleitung 8000 zu 8080; begrenzte Neuverbindungen auf 8080; eine Datei mit `include`, dazu Testkatalog und Rückweg. Dokumentieren Sie in einer Seite.
6. **Vorgehen beschreiben (Einheit 13.1):** Beschreiben Sie Ihr Vorgehen bei einer Störung („Webserver nicht erreichbar“) in fünf Schritten.

#### Kontrollfragen

1. Welche drei Beobachtungen genügen oft, um Fehler 1, 2 und 4 zu unterscheiden?
2. Was zeigt tcpdump auf beiden Seiten einer Firewall, wenn die Rückrichtung fehlt?
3. Wann hilft `nft monitor trace`, wann reicht ein Zähler?
4. Warum ist es riskant, bei Störungen mehrere Regeln gleichzeitig zu ändern?
