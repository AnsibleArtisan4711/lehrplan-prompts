# Lehrplan: VPN mit WireGuard und OpenVPN

| Kategorie | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger, angehende Systemadministratoren / Systemtechniker |
| **Vorkenntnisse** | IT-Grundlagen, Grundkenntnisse Netzwerke (IPv4, Subnetze, Routing) |
| **Gesamtumfang** | 12 Module, 110 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | WireGuard, OpenVPN, Debian 12 Linux, EasyRSA, nftables |
| **Thematische Abgrenzung (Out of Scope)** | OPNsense-Konfiguration, tiefergehende PKI- und Zertifikatsgrundlagen (TLS-Handshake-Details) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | VPN-Konzepte und technologische Grundlagen | 1 | 8 |
| 2 | Vorbereitung der Laborumgebung und Linux-Routing | 1 | 8 |
| 3 | WireGuard – Grundlagen und Architektur | 1 | 8 |
| 4 | WireGuard – Road-Warrior-Konzepte und Split Tunneling | 1 | 10 |
| 5 | WireGuard – Site-to-Site-Verbindungen | 2 | 8 |
| 6 | OpenVPN – Grundlagen und PKI-Vorbereitung (EasyRSA) | 1 | 8 |
| 7 | OpenVPN – Server-Konfiguration und Basisbetrieb | 1 | 10 |
| 8 | OpenVPN – Road-Warrior-Clients und Inline-Profile | 1 | 10 |
| 9 | OpenVPN – Fortgeschrittenes Routing (ccd, iroute) | 2 | 10 |
| 10 | OpenVPN – Site-to-Site-Verbindungen | 2 | 10 |
| 11 | Firewalling, NAT und Sicherheit für VPN-Gateways | 1 | 10 |
| 12 | Troubleshooting, Logging und Fehlerbehebung | 1 | 10 |
| **Gesamt**| **9x Pri 1, 3x Pri 2** | | **110 UE** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln zwingende Kernkompetenzen für den sicheren Betrieb eines VPN. Module mit Priorität 2 dienen der Vertiefung spezifischer Topologien (wie komplexe Site-to-Site-Setups) und können bei Zeitmangel gekürzt werden.*

### 2. Quellen

* **WireGuard: Next Generation Kernel Network Tunnel**, Jason A. Donenfeld, NDSS 2017. URL: https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/wireguard-next-generation-kernel-network-tunnel/ (über Suche gefunden, nicht abgerufen). Das Dokument wird laufend überarbeitet, die aktuelle Fassung liegt unter https://www.wireguard.com/papers/wireguard.pdf (nicht abgerufen); die frühere Jahresangabe „2021“ ist nicht bestätigt.
* **OpenVPN 2.6 Reference Manual:** OpenVPN Inc. URL: https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/ (URL und Stand nicht geprüft). Die in Debian 12 paketierte OpenVPN-Version ist nicht bestätigt.
* **EasyRSA 3 Documentation:** OpenVPN Inc. URL: https://easy-rsa.readthedocs.io/en/latest/ (URL und Stand nicht geprüft). Die EasyRSA-Befehle aus Modul 6 wurden mit EasyRSA aus dem GitHub-Repository `OpenVPN/easy-rsa` durchgespielt; die in Debian 12 paketierte Version kann abweichen (nicht bestätigt).
* **RFC 1918:** Address Allocation for Private Internets, Y. Rekhter et al., 1996. URL: https://datatracker.ietf.org/doc/html/rfc1918
* **The Debian Administrator's Handbook, Debian Bullseye from Discovery to Mastery** (Debian 11), R. Hertzog, R. Mas. URL: https://debian-handbook.info/ (laut https://www.debian.org/doc/books.en.html, abgerufen am 08.11.2026). Eine Ausgabe für Debian 12 ist nicht bestätigt; Pfade und Paketnamen für Debian 12 stützen sich auf die Handbuchseiten der Pakete (nicht geprüft).
* **RFC 4301** (Security Architecture for the Internet Protocol), **RFC 4303** (IP Encapsulating Security Payload, ESP) und **RFC 7296** (Internet Key Exchange Protocol Version 2, IKEv2). URLs: https://datatracker.ietf.org/doc/html/rfc4301, https://datatracker.ietf.org/doc/html/rfc4303, https://datatracker.ietf.org/doc/html/rfc7296 (nicht abgerufen). Grundlage für den IPsec-Vergleich in Modul 1.
* **The Noise Protocol Framework**, Trevor Perrin. URL: https://noiseprotocol.org/noise.html (nicht abgerufen). Grundlage des WireGuard-Handshakes.
* **RFC 8446** (The Transport Layer Security Protocol Version 1.3) und **RFC 7748** (Elliptic Curves for Security, Curve25519). URLs: https://datatracker.ietf.org/doc/html/rfc8446, https://datatracker.ietf.org/doc/html/rfc7748 (nicht abgerufen). Welche TLS-Version OpenVPN in Debian 12 aushandelt, ist nicht bestätigt.
* **Handbuchseiten `wg(8)` und `wg-quick(8)`** (WireGuard) sowie **nftables-Wiki**. URLs: https://man7.org/linux/man-pages/man8/wg-quick.8.html, https://wiki.nftables.org/ (nicht abgerufen). Das Verhalten von `wg-quick` bei Standardrouten und von `wg syncconf` bei Routen ist in Modul 4 und 5 als „nicht bestätigt“ gekennzeichnet.
* Diffie-Hellman-Schlüsselaustausch, Curve25519 und ChaCha20-Poly1305 werden nur als Begriffe genannt; eine eigene Quelle ist über die obigen Dokumente hinaus nicht geprüft.

### 3. Labor-Setup & Rahmenbedingungen

Alle Praxisaufgaben finden in einer isolierten Hyper-V-Umgebung ohne physische Verbindung zum Heim- oder Firmennetz (privater virtueller Switch) statt, mit Ausnahme der Internet-Phase in Modul 2. Cloud-Dienste kommen nicht zum Einsatz. Die Befehle wurden nicht auf Debian 12 ausgeführt; der EasyRSA-Ablauf (Modul 6) und die nftables-Syntax (Modul 11) wurden in einer Testumgebung geprüft, alles Übrige ist nicht ausgeführt und die Hinweise „nicht bestätigt“ sind zu beachten.

**Benötigte Systeme (Erforderlich ab Modul 2):**
* **Hyper-V-Host:** Windows 10/11 Pro oder Enterprise mit aktiviertem Hyper-V, mindestens 8 GB freier Arbeitsspeicher und 60 GB freier Speicherplatz für zwei VMs mit je 2 GB RAM, 1 vCPU und 20 GB Festplatte (Richtwerte, nicht erprobt).
* **Netzwerk:** Privater vSwitch `VPN-Lab-WAN` (Subnetz `10.0.0.0/24`, ohne Host-Adapter). Für Installation und Internet-Phase zusätzlich der vorhandene Hyper-V-Switch `Default Switch` (NAT, DHCP). Jede VM hat genau einen Netzwerkadapter; er wird in Modul 2 vom `Default Switch` auf `VPN-Lab-WAN` umgestellt. Vom Host aus ist im isolierten Zustand keine SSH-Verbindung zu den VMs möglich; Eingaben erfolgen in der Hyper-V-Konsole (Verbinden). Zwischen den beiden VMs ist SSH möglich.
* **Betriebssystem beider VMs:** Debian 12 (netinst-ISO von debian.org, Download am Host, nicht geprüft), Generation-2-VM mit der Secure-Boot-Vorlage „Microsoft UEFI Certificate Authority“ (Vorlage für Linux laut Microsoft Learn), ohne Desktop. Bei der Softwareauswahl „SSH-Server“ und „Standard-Systemwerkzeuge“ wählen. Das Root-Kennwort leer lassen, damit das Installationsprogramm für den Benutzer `labadmin` sudo einrichtet (Verhalten nicht bestätigt). Die Installation erfolgt vor Modul 2 mit Internet über den `Default Switch` und ist nicht in den Unterrichtseinheiten enthalten; danach wird je VM ein Hyper-V-Prüfpunkt `Basis` erstellt.
* **VM 1 (VPN-Server, Gateway Site A):** Hostname `vpn-a`; WAN-Adapter `10.0.0.1/24`; simuliertes LAN Site A als Interface `dummy0` mit `192.168.10.1/24` (wird in Modul 2 mit einem Skript erzeugt, in Modul 11 durch einen simulierten LAN-Host ersetzt).
* **VM 2 (Client, Gateway Site B):** Hostname `vpn-b`; WAN-Adapter `10.0.0.100/24`; simuliertes LAN Site B als Interface `dummy0` mit `192.168.20.1/24` (wird in Modul 2 mit einem Skript erzeugt).
* **Adressplan:** `10.0.0.0/24` WAN (`VPN-Lab-WAN`); `10.8.0.0/24` WireGuard (Server `.1`, Client `.100`); `10.9.0.0/24` OpenVPN (Server `.1`, `client1` ab Modul 9 fest `.50`); `192.168.10.0/24` Site A; `192.168.20.0/24` Site B; ab Modul 11 der simulierte LAN-Host `lan-a` mit `192.168.10.10` auf VM 1.
* **Regel für das gesamte Labor:** WireGuard und OpenVPN laufen nie gleichzeitig, weil beide Routen in `192.168.10.0/24` und `192.168.20.0/24` setzen (Routenkonflikt). Jede Aufgabe nennt, welcher Tunnel läuft. Die Namen der Netzwerkadapter (hier `eth0`) sind nicht bestätigt und mit `ip -br a` zu prüfen.
* **CA-Hinweis:** Aus Vereinfachung liegt die Certificate Authority (Modul 6) auf VM 1; in der Praxis liegt sie auf einem getrennten, geschützten System.
* **Software-Pakete (Download in Modul 2 nötig):** `wireguard`, `openvpn`, `easy-rsa`, `nftables`, `tcpdump`.

---

## B. Detaillierter Modulaufbau

### Modul 1: VPN-Konzepte und technologische Grundlagen
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Unterschiede zwischen IPsec, OpenVPN und WireGuard erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Topologien (Road-Warrior vs. Site-to-Site) skizzieren.
* **Voraussetzungen:** Keine.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Schutzziele in der Kommunikation (Vertraulichkeit, Integrität, Authentizität) | 2 |
| 1.2 | Topologien: Road-Warrior, Site-to-Site, Split Tunneling vs. Full Tunneling; Adressplanung (RFC 1918, Überschneidungen) | 3 |
| 1.3 | Protokollvergleich: IPsec (IKE/ESP), OpenVPN (TLS), WireGuard (Noise Protocol) | 3 |
#### Praxisaufgaben (Hands-on Lab)
*Da dieses Modul rein konzeptionell ist, ist kein technisches Labor erforderlich. Die Aufgaben bestehen aus Fallstudien.*
1. **Fallstudie Topologie-Wahl:** Entwerfen Sie auf dem Papier (oder Whiteboard) eine VPN-Struktur für ein fiktives Unternehmen (`example.com`) mit einer Zentrale und 50 Außendienstmitarbeitern. Skizzieren Sie die IP-Bereiche nach RFC 1918.
2. **Protokoll-Entscheidung:** Formulieren Sie eine kurze Empfehlung (Vor- und Nachteile), ob für die Verbindung zweier Rechenzentren IPsec oder WireGuard eingesetzt werden sollte.
#### Kontrollfragen
1. Nennen Sie drei wesentliche Unterschiede zwischen WireGuard und OpenVPN.
2. Was ist der Unterschied zwischen einem Road-Warrior-Setup und einer Site-to-Site-Verbindung?
3. Warum verwendet man für die Adressen im VPN und in den dahinterliegenden Netzen üblicherweise private Adressen nach RFC 1918, und welches Problem entsteht, wenn sich die Netze beider Standorte überschneiden?
4. Ordnen Sie die Schutzziele Vertraulichkeit, Integrität und Authentizität je einem Mechanismus zu, der in einem VPN dafür sorgt.

---

### Modul 2: Vorbereitung der Laborumgebung und Linux-Routing
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende IPv4-Forwarding unter Linux temporär und persistent aktivieren.
  * Nach Abschluss dieses Moduls kann der Lernende virtuelle Dummy-Schnittstellen anlegen.
* **Voraussetzungen:** Beide VMs sind mit Debian 12 installiert (Prüfpunkt `Basis`) und am `Default Switch` mit Internetzugang (DHCP). Alle Befehle werden mit `sudo` als Benutzer `labadmin` ausgeführt.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Softwarebereitstellung (Internet-Phase) und anschließende Lab-Isolation | 2 |
| 2.2 | IP-Grundkonfiguration und IPv4-Forwarding (`sysctl`) | 3 |
| 2.3 | Simulation lokaler Netze via `dummy`-Kernelmodul | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Paketinstallation (Internet-Phase):** Prüfen Sie auf beiden VMs mit `ip -br a`, dass der Adapter eine Adresse vom `Default Switch` hat. Installieren Sie die Pakete: `sudo apt update && sudo apt install -y wireguard openvpn easy-rsa nftables tcpdump`. Ändern Sie danach in den Hyper-V-Einstellungen den Adapter beider VMs auf den isolierten Switch `VPN-Lab-WAN`.
2. **Statische IPs vergeben:** Ermitteln Sie den Adapternamen mit `ip -br a`. Tragen Sie in `/etc/network/interfaces` für diesen Adapter (hier `eth0`) statt `dhcp` die Zeilen `iface eth0 inet static` und `address 10.0.0.1/24` ein (VM 2: `address 10.0.0.100/24`, jeweils ohne Gateway) und laden Sie die Konfiguration mit `sudo systemctl restart networking` (Datei und Verfahren für Debian 12 nicht bestätigt). Testen Sie die Erreichbarkeit mit `ping -c 3` zwischen den VMs.
3. **Routing aktivieren:** Aktivieren Sie auf `VM 1` und `VM 2` das IP-Forwarding zuerst temporär (`sudo sysctl -w net.ipv4.ip_forward=1`) und prüfen Sie es mit `sysctl net.ipv4.ip_forward`. Aktivieren Sie es danach persistent: Entfernen Sie in `/etc/sysctl.conf` das Kommentarzeichen vor `net.ipv4.ip_forward=1` (oder fügen Sie die Zeile hinzu) und wenden Sie die Datei mit `sudo sysctl -p` an. Das Ergebnis nach einem Neustart ist im Prüfpunkt der Aufgabe 5 zu bestätigen.
4. **Dummy-Interfaces anlegen:** Legen Sie auf `VM 1` das Skript `/usr/local/sbin/lab-dummy.sh` (ausführbar) mit diesem Inhalt an und führen Sie es mit `sudo` aus; auf `VM 2` verwenden Sie `192.168.20.1/24`:
   ```sh
   #!/bin/sh
   modprobe dummy
   ip link show dummy0 >/dev/null 2>&1 || ip link add dummy0 type dummy
   ip addr replace 192.168.10.1/24 dev dummy0
   ip link set dummy0 up
   ```
   Prüfen Sie mit `ip -br a show dummy0`. Die Schnittstelle bleibt nach einem Neustart nicht erhalten; das Skript wird dann erneut ausgeführt.
5. **Prüfpunkt:** Starten Sie beide VMs neu, prüfen Sie `sysctl net.ipv4.ip_forward` und führen Sie `lab-dummy.sh` aus. Erstellen Sie danach auf beiden VMs den Hyper-V-Prüfpunkt `M2-fertig`.
#### Kontrollfragen
1. Welcher Parameter in der `sysctl.conf` ist zwingend nötig, damit ein Linux-Server als VPN-Router fungieren kann?
2. Welchem Zweck dient das Modul `dummy` in unserem spezifischen isolierten Labor-Setup?
3. Warum müssen die Hyper-V VMs nach Aufgabe 1 zwingend in einen rein privaten virtuellen Switch verschoben werden?

---

### Modul 3: WireGuard – Grundlagen und Architektur
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende asymmetrische WireGuard-Schlüsselpaare generieren.
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache WireGuard-Schnittstelle konfigurieren und starten.
* **Voraussetzungen:** Modul 2 abgeschlossen (Pakete installiert).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Cryptokey-Routing: Private und Public Keys in WireGuard | 2 |
| 3.2 | Struktur der `wg0.conf` (Interface vs. Peer) | 3 |
| 3.3 | Befehlssatz: `wg`, `wg-quick` und Diensteverwaltung | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Schlüsselgenerierung:** Wechseln Sie mit `sudo -i` zu root und setzen Sie `umask 077`. Generieren Sie auf `VM 1` (Server) einen Private Key (`wg genkey`) und leiten Sie daraus den Public Key ab (`wg pubkey`), zum Beispiel mit `wg genkey | tee /etc/wireguard/server.key | wg pubkey > /etc/wireguard/server.pub`. Wiederholen Sie den Vorgang auf `VM 2` (Client) mit den Dateinamen `client.key` und `client.pub`.
2. **Basis-Konfiguration Server:** Erstellen Sie auf `VM 1` die Datei `/etc/wireguard/wg0.conf`. Konfigurieren Sie den Block `[Interface]` mit der VPN-IP (`Address = 10.8.0.1/24`), dem Private Key (`PrivateKey`) und `ListenPort = 51820`. Setzen Sie die Rechte mit `chmod 600 /etc/wireguard/wg0.conf`.
3. **Dienststart:** Starten Sie das Interface auf dem Server mit `wg-quick up wg0`. Prüfen Sie die Schnittstelle mit `ip a` und dem Befehl `wg`. Stoppen Sie es mit `wg-quick down wg0` und starten Sie es einmal über den Dienst (`systemctl start wg-quick@wg0`, Status mit `systemctl status wg-quick@wg0`, danach `systemctl stop wg-quick@wg0`). Aktivieren Sie den Autostart nicht (`systemctl enable` wird in diesem Labor nicht verwendet), damit WireGuard und OpenVPN nie gleichzeitig laufen. Starten Sie das Interface mit `wg-quick up wg0` erneut für Modul 4.
#### Kontrollfragen
1. Welche mathematische Abhängigkeit besteht zwischen dem Private Key und dem Public Key bei WireGuard?
2. Wozu dient der Befehl `wg-quick` im Gegensatz zum reinen `wg` Befehl?
3. Welche Informationen zeigt die Ausgabe des Befehls `wg` an, wenn noch keine Peers verbunden sind?

---

### Modul 4: WireGuard – Road-Warrior-Konzepte und Split Tunneling
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen WireGuard-Client für den Fernzugriff einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip "AllowedIPs" gezielt für Split- und Full-Tunneling anwenden.
* **Voraussetzungen:** Modul 3 (laufendes `wg0` Interface auf dem Server).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Die Bedeutung von `AllowedIPs` (Routing und Sicherheit) | 3 |
| 4.2 | Road-Warrior Client-Konfiguration | 4 |
| 4.3 | Split Tunneling vs. Full Tunneling in der Praxis | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Peer am Server eintragen:** Ergänzen Sie auf `VM 1` in der `wg0.conf` den Block `[Peer]` für `VM 2`. Nutzen Sie den Public Key von VM 2 (`/etc/wireguard/client.pub`) und `AllowedIPs = 10.8.0.100/32`. Übernehmen Sie die Änderung mit `wg-quick down wg0` und `wg-quick up wg0`.
2. **Client-Konfiguration (Split Tunnel):** Erstellen Sie auf `VM 2` die `wg0.conf` (Rechte `600`). Setzen Sie im `[Interface]` den Private Key von VM 2 und die IP `10.8.0.100/24`. Fügen Sie den Server als `[Peer]` hinzu (Public Key des Servers, `Endpoint = 10.0.0.1:51820`). Setzen Sie `AllowedIPs = 10.8.0.0/24, 192.168.10.0/24`. Starten Sie das Interface mit `wg-quick up wg0`.
3. **Verbindungstest:** Pingen Sie von `VM 2` die Tunnel-IP des Servers (`10.8.0.1`) und dessen LAN-IP (`192.168.10.1`). Prüfen Sie mit `wg` auf beiden VMs die Zeile `latest handshake` und die Zähler `transfer`.
4. **Full Tunnel Umbau:** Ändern Sie auf `VM 2` in der `wg0.conf` die `AllowedIPs` auf `0.0.0.0/0` und übernehmen Sie die Änderung mit `wg-quick down wg0` und `wg-quick up wg0` (eine Änderung der Datei wirkt nicht auf ein laufendes Interface). Prüfen Sie `ip rule`, `ip route show table 51820` und `ip route get 8.8.8.8`. `wg-quick` legt die Standardroute laut Handbuch in eine eigene Routingtabelle und eine Regel an, die Tabellennummer 51820 ist nicht bestätigt, und `ip route` allein zeigt sie nicht. Ein Internetzugriff ist im isolierten Labor nicht möglich. Setzen Sie die `AllowedIPs` anschließend auf den Wert aus Aufgabe 2 zurück, starten Sie das Interface neu und wiederholen Sie die Pings aus Aufgabe 3. Der Zustand nach Modul 4: `wg0` läuft auf beiden VMs.
#### Kontrollfragen
1. Welche zwei Funktionen übernimmt der Parameter `AllowedIPs` in WireGuard gleichzeitig?
2. Warum erfordert ein Full-Tunnel (`0.0.0.0/0`) am Server in der Regel den Einsatz von NAT (Masquerading)?
3. Welche Route wird auf dem Client automatisch gesetzt, wenn `AllowedIPs = 192.168.10.0/24` konfiguriert ist?

---

### Modul 5: WireGuard – Site-to-Site-Verbindungen
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende zwei Subnetze bidirektional über WireGuard routen.
* **Voraussetzungen:** Modul 4 (`wg0` läuft auf beiden VMs); die Dummy-Interfaces sind angelegt (nach einem Neustart `lab-dummy.sh` ausführen).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Site-to-Site Architektur und Subnetz-Routing | 3 |
| 5.2 | Anpassung von AllowedIPs für Netzsegmente | 2 |
| 5.3 | Bidirektionale Erreichbarkeitsprüfung | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Routing für Site B bekanntgeben:** Bearbeiten Sie auf `VM 1` (Server) den `[Peer]`-Eintrag für VM 2. Ändern Sie `AllowedIPs = 10.8.0.100/32, 192.168.20.0/24`. Übernehmen Sie die Änderung mit `wg-quick down wg0` und `wg-quick up wg0`. Prüfen Sie mit `ip route show dev wg0`, dass die Route `192.168.20.0/24` vorhanden ist.
2. **Verhalten von `wg syncconf` beobachten:** Entfernen Sie `192.168.20.0/24` aus den `AllowedIPs`, laden Sie mit `wg syncconf wg0 <(wg-quick strip wg0)` neu (in `bash`) und prüfen Sie `wg show wg0 allowed-ips` und `ip route show dev wg0`. Tragen Sie den Eintrag wieder ein, laden Sie erneut mit `wg syncconf` und prüfen Sie, ob die Route `192.168.20.0/24` wieder erscheint (erwartet: nein, weil `wg-quick` die Routen beim Start setzt und `wg syncconf` nur die Schnittstelle abgleicht; nicht bestätigt). Stellen Sie den Zustand mit `wg-quick down wg0` und `wg-quick up wg0` wieder her.
3. **Ping-Test zwischen LANs:** Pingen Sie von `VM 1` mit `ping -c 3 -I 192.168.10.1 192.168.20.1` und von `VM 2` mit `ping -c 3 -I 192.168.20.1 192.168.10.1` (die Quelladresse stammt jeweils aus dem eigenen Site-Netz). Beide Pings müssen über den Tunnel (`10.8.0.x`) laufen. Führen Sie parallel auf `VM 2` den Befehl `tcpdump -i wg0 -n icmp` aus, um den Tunnel-Traffic nachzuweisen.
4. **Rückbau:** Stoppen Sie am Ende des Moduls auf beiden Systemen WireGuard mit `wg-quick down wg0`, um Routenkonflikte mit OpenVPN (ab Modul 6, beide setzen Routen in die Netze `192.168.10.0/24` und `192.168.20.0/24`) zu vermeiden.
#### Kontrollfragen
1. Warum muss das Subnetz von Site B in den `AllowedIPs` auf Site A zwingend eingetragen werden?
2. Welchen Vorteil bietet der Befehl `wg syncconf` gegenüber einem Neustart des Interfaces mit `wg-quick down/up`, und was setzt er (laut Aufgabe 2) nicht um?
3. Warum reicht die WireGuard-Konfiguration allein nicht aus, wenn das IP-Forwarding im Kernel deaktiviert ist?

---

### Modul 6: OpenVPN – Grundlagen und PKI-Vorbereitung (EasyRSA)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache Certificate Authority (CA) mit EasyRSA initialisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Server- und Client-Zertifikate generieren und signieren.
* **Voraussetzungen:** Modul 2 (installierte Pakete, Prüfpunkt `M2-fertig`).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Funktionsweise von OpenVPN (TLS, tun/tap, UDP/TCP und Ports) | 3 |
| 6.2 | Einführung in EasyRSA (Infrastruktur aufbauen) | 2 |
| 6.3 | Erstellung von CA, Server- und Client-Zertifikaten | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Zustand herstellen und EasyRSA initialisieren:** Stoppen Sie WireGuard auf beiden VMs (`wg-quick down wg0`; läuft das Interface nicht mehr, ist die Meldung zu ignorieren). Wechseln Sie auf `VM 1` mit `sudo -i` zu root, erstellen Sie das Verzeichnis `/etc/openvpn/easy-rsa` und wechseln Sie hinein. Kopieren Sie die EasyRSA-Vorlagen dorthin (`cp -r /usr/share/easy-rsa/* .`). Führen Sie `./easyrsa init-pki` aus.
2. **CA erstellen:** Bauen Sie die Certificate Authority mit `./easyrsa build-ca nopass` (Common Name: `VPN-Lab-CA`).
3. **Server-Zertifikat:** Generieren Sie das Server-Zertifikat und den Schlüssel mit `./easyrsa gen-req server nopass` und signieren Sie es mit `./easyrsa sign-req server server` (Rückfrage mit `yes` bestätigen).
4. **Diffie-Hellman Parameter:** Generieren Sie die DH-Parameter mittels `./easyrsa gen-dh`.
5. **Client-Zertifikat:** Generieren Sie für `VM 2` (Common Name: `client1`) die Anforderung mit `./easyrsa gen-req client1 nopass` und signieren Sie sie mit `./easyrsa sign-req client client1` (Typ `client`, nicht `server`).
6. **Ergebnis prüfen:** Listen Sie mit `find pki -type f` die erzeugten Dateien. Erwartet werden unter `pki/` unter anderem `ca.crt`, `dh.pem`, `issued/server.crt`, `issued/client1.crt`, `private/server.key` und `private/client1.key`. Prüfen Sie mit `openssl x509 -in pki/issued/client1.crt -noout -subject -issuer`, dass der Aussteller `VPN-Lab-CA` ist.
#### Kontrollfragen
1. Welchen kryptografischen Zweck erfüllen die Diffie-Hellman-Parameter (DH) beim TLS-Verbindungsaufbau von OpenVPN?
2. Warum ist der Common Name (CN) eines Zertifikats für das spätere OpenVPN-Routing wichtig?
3. Worin liegt das Sicherheitsrisiko, wenn man den Parameter `nopass` beim Erstellen der CA verwendet?

---

### Modul 7: OpenVPN – Server-Konfiguration und Basisbetrieb
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine funktionale `server.conf` für OpenVPN erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende den OpenVPN-Dienst als Systemd-Service verwalten.
* **Voraussetzungen:** Modul 6 (CA, Server-Cert, Server-Key, DH-Parameter vorhanden).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Die Direktiven der `server.conf` (port, proto, dev, topology) | 4 |
| 7.2 | TLS-Authentifizierung (`tls-auth` / `tls-crypt`) | 3 |
| 7.3 | Dienststart und Socket-Analyse | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Zertifikate kopieren:** Kopieren Sie auf `VM 1` aus `/etc/openvpn/easy-rsa` die Dateien `pki/ca.crt`, `pki/issued/server.crt`, `pki/private/server.key` und `pki/dh.pem` nach `/etc/openvpn/server/`. Generieren Sie zusätzlich einen statischen TLS-Schlüssel: `openvpn --genkey secret /etc/openvpn/server/ta.key`.
2. **Server-Konfiguration anlegen:** Erstellen Sie `/etc/openvpn/server/server.conf`. Parameter: `port 1194`, `proto udp`, `dev tun`, `topology subnet`, `server 10.9.0.0 255.255.255.0`, `tls-crypt ta.key`, `push "route 192.168.10.0 255.255.255.0"`. Referenzieren Sie die Zertifikate mit `ca ca.crt`, `cert server.crt`, `key server.key` und `dh dh.pem` (relative Pfade, da der Dienst im Verzeichnis `/etc/openvpn/server` startet; nicht bestätigt).
3. **Dienst starten:** Aktivieren und starten Sie den Dienst mit `systemctl enable --now openvpn-server@server`. Prüfen Sie ihn mit `systemctl status openvpn-server@server` und `journalctl -u openvpn-server@server -n 20`, starten Sie ihn mit `systemctl restart openvpn-server@server` neu und stellen Sie sicher, dass er danach läuft.
4. **Verifikation:** Prüfen Sie mit `ss -uln`, ob Port 1194 (UDP) lauscht. Prüfen Sie mit `ip a`, ob das `tun0` Interface existiert und die IP `10.9.0.1` hat.
#### Kontrollfragen
1. Was bewirkt die Direktive `topology subnet` im Vergleich zur älteren `topology net30`?
2. Welchen Schutzmechanismus bietet die Option `tls-crypt` gegenüber der älteren `tls-auth` Direktive?
3. Warum verwendet OpenVPN standardmäßig UDP statt TCP als Transportprotokoll?

---

### Modul 8: OpenVPN – Road-Warrior-Clients und Inline-Profile
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende `.ovpn` Inline-Profile erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende OpenVPN-Clients konfigurieren und verbinden.
* **Voraussetzungen:** Modul 7 (laufender OpenVPN-Server). Modul 6 (Client-Zertifikate).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Struktur der Client-Konfiguration (`client.conf` / `.ovpn`), Direktiven `client` und `remote-cert-tls` | 3 |
| 8.2 | Inline-Certs (Zusammenfassen in einer Datei) | 4 |
| 8.3 | Verbindungsaufbau und Routing-Prüfung auf Client-Seite | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Zertifikats-Transfer:** Die Schlüsseldateien sind nur für root lesbar, und ein SSH-Login als root ist unter Debian meist gesperrt (nicht bestätigt). Kopieren Sie daher auf `VM 1` mit `sudo` die Dateien `pki/ca.crt`, `pki/issued/client1.crt` und `pki/private/client1.key` aus `/etc/openvpn/easy-rsa` sowie `/etc/openvpn/server/ta.key` in das Verzeichnis `/tmp/ovpn-client` und setzen Sie `sudo chown -R labadmin /tmp/ovpn-client`. Übertragen Sie es mit `scp -r /tmp/ovpn-client labadmin@10.0.0.100:/tmp/` nach `VM 2` und verschieben Sie die Dateien dort mit `sudo` nach `/etc/openvpn/client/` (`sudo chmod 600` für `client1.key` und `ta.key`). Löschen Sie danach `/tmp/ovpn-client` auf beiden VMs mit `rm -r /tmp/ovpn-client`.
2. **Profil erstellen (Inline):** Erstellen Sie auf `VM 2` die Datei `/etc/openvpn/client/client1.ovpn`. Konfigurieren Sie `client`, `dev tun`, `proto udp`, `remote 10.0.0.1 1194`, `remote-cert-tls server`. Binden Sie die vier übertragenen Schlüsseldateien inline als XML-ähnliche Tags ein (`<ca>...</ca>`, `<cert>...</cert>`, `<key>...</key>`, `<tls-crypt>...</tls-crypt>`). Legen Sie eine Sicherungskopie `client1.ovpn.bak` an.
3. **Verbindung herstellen:** Der Tunnel ist WireGuard-frei (`wg0` ist gestoppt). Starten Sie auf `VM 1` den Dienst (`systemctl start openvpn-server@server`, falls er nicht läuft) und auf `VM 2` den OpenVPN-Prozess im Vordergrund: `sudo openvpn --config /etc/openvpn/client/client1.ovpn`.
4. **Verifikation:** Öffnen Sie auf `VM 2` ein zweites Terminal (zweites Konsolenfenster oder `ssh labadmin@10.0.0.100` von `VM 1` aus) und prüfen Sie das neue Interface `tun0` (`ip a`), die gepushte Route mit `ip route` (erwartet: `192.168.10.0/24` über `tun0`) und pingen Sie die Server-LAN IP `192.168.10.1`. Beenden Sie den Client danach mit Strg+C.
#### Kontrollfragen
1. Welchen großen administrativen Vorteil bieten `.ovpn` Dateien mit Inline-Zertifikaten (insbesondere für Windows/Mobile Clients)?
2. Welche Direktive in `client` sorgt dafür, dass der Client die vom Server gepushten Routen übernimmt, und womit lassen sich gepushte Optionen auf dem Client unterdrücken (`route-nopull`)?
3. Was geschieht, wenn der Parameter `remote-cert-tls server` auf dem Client vergessen wird?

---

### Modul 9: OpenVPN – Fortgeschrittenes Routing (ccd, iroute)
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende client-spezifische Konfigurationen (`client-config-dir`) anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen `route` und `iroute` erklären (die praktische Anwendung folgt in Modul 10).
* **Voraussetzungen:** Modul 8 (erfolgreiche Client-Verbindung).
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Konzept des Client-Config-Dir (CCD) | 3 |
| 9.2 | Statische IP-Zuweisung für bestimmte Clients | 3 |
| 9.3 | Internes Routing (`iroute`) vs. Kernel-Routing (`route`) | 4 |
#### Praxisaufgaben (Hands-on Lab)
1. **CCD vorbereiten:** Erstellen Sie auf `VM 1` das Verzeichnis `/etc/openvpn/server/ccd/`. Fügen Sie der `server.conf` die Direktive `client-config-dir /etc/openvpn/server/ccd` hinzu und starten Sie den Dienst neu.
2. **Statische IP vergeben:** Erstellen Sie im CCD-Verzeichnis eine Datei mit dem Namen `client1` (exakt der Common Name des Client-Zertifikats). Fügen Sie die Zeile `ifconfig-push 10.9.0.50 255.255.255.0` ein.
3. **Test:** Beenden Sie den Client auf `VM 2` (Strg+C) und verbinden Sie neu (`sudo openvpn --config /etc/openvpn/client/client1.ovpn`). Prüfen Sie mit `ip a`, ob der Client nun zuverlässig die IP `10.9.0.50` erhält. Beenden Sie den Client danach mit Strg+C.
#### Kontrollfragen
1. Warum muss der Dateiname im `ccd`-Verzeichnis exakt mit dem Common Name (CN) des Zertifikats übereinstimmen?
2. Warum reicht ein normaler `route` Befehl im Kernel nicht aus, um ein Subnetz hinter einem spezifischen VPN-Client zu erreichen, und warum braucht OpenVPN stattdessen `iroute`?
3. Wo (in welcher Datei) wird der Parameter `ifconfig-push` definiert?

---

### Modul 10: OpenVPN – Site-to-Site-Verbindungen
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine TLS-basierte Site-to-Site-Verbindung mit OpenVPN aufbauen.
* **Voraussetzungen:** Modul 9.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Site-to-Site mit OpenVPN: Architektur | 3 |
| 10.2 | Konfiguration von `iroute` im CCD | 4 |
| 10.3 | Kernel-Routing für Client-Subnetze | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Kernel-Route am Server:** Ergänzen Sie die `server.conf` auf `VM 1` um die Direktive `route 192.168.20.0 255.255.255.0`.
2. **Interne Route (iroute) am Server:** Ergänzen Sie die CCD-Datei `/etc/openvpn/server/ccd/client1` um die Direktive `iroute 192.168.20.0 255.255.255.0`. Starten Sie den OpenVPN-Server neu.
3. **Bidirektionaler Ping-Test:** Starten Sie den Server (`systemctl start openvpn-server@server`, falls nötig) und verbinden Sie `VM 2` (`sudo openvpn --config /etc/openvpn/client/client1.ovpn`). Prüfen Sie auf `VM 1` mit `ip route get 192.168.20.1`, dass der Weg über `tun0` führt. Pingen Sie von `VM 1` auf das Dummy-Interface von Site B (`ping -c 3 192.168.20.1`) und von `VM 2` in einem zweiten Terminal mit `ping -c 3 -I 192.168.20.1 192.168.10.1`.
4. **Rückbau / Trennung:** Beenden Sie den OpenVPN-Client-Prozess auf `VM 2` (Strg+C) und den Dienst auf `VM 1` mit `systemctl disable --now openvpn-server@server`. Spätere Module starten den Dienst bei Bedarf selbst.
#### Kontrollfragen
1. Erklären Sie das Zusammenspiel zwischen `route` (in der server.conf) und `iroute` (in der CCD-Datei) bei einem Site-to-Site Setup in OpenVPN.
2. Warum ist bei Site-to-Site-Verbindungen das IP-Forwarding auf beiden Seiten zwingend erforderlich?
3. Welcher Fehler tritt im Ping-Test auf, wenn das `iroute` fehlt, aber das `route` gesetzt ist?

---

### Modul 11: Firewalling, NAT und Sicherheit für VPN-Gateways
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den VPN-Verkehr mit `nftables` absichern und maskieren (NAT).
  * Nach Abschluss dieses Moduls kann der Lernende das Gateway gegen unbefugte Zugriffe härten.
* **Voraussetzungen:** Modul 2, Modul 3 und 4 (WireGuard-Konfiguration) sowie Modul 7 und 8 (OpenVPN-Konfiguration). Die Tunnel werden in den Aufgaben nacheinander gestartet, nie gleichzeitig.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Grundlagen `nftables` (Tabellen, Ketten, Regeln) | 3 |
| 11.2 | Masquerading (NAT) für VPN-Clients | 4 |
| 11.3 | Absicherung der Input- und Forward-Chain (Ports 51820, 1194, 22) | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Prüfpunkt und LAN-Host simulieren:** Erstellen Sie auf `VM 1` den Hyper-V-Prüfpunkt `M11-Start` und stoppen Sie alle Tunnel (`wg-quick down wg0`, `systemctl stop openvpn-server@server`). Weiterleitung lässt sich mit den bisherigen Dummy-Interfaces nicht zeigen, weil die LAN-Adresse auf dem Gateway selbst liegt. Legen Sie daher das Skript `/usr/local/sbin/lab-lan-a.sh` an (ausführbar) und führen Sie es mit `sudo` aus; es ersetzt `dummy0` durch einen simulierten Rechner `lan-a` (`192.168.10.10`) in einem Netzwerk-Namespace:
   ```sh
   #!/bin/sh
   ip addr flush dev dummy0
   ip netns add lan-a
   ip link add veth-gw type veth peer name veth-host
   ip link set veth-host netns lan-a
   ip addr add 192.168.10.1/24 dev veth-gw
   ip link set veth-gw up
   ip netns exec lan-a ip addr add 192.168.10.10/24 dev veth-host
   ip netns exec lan-a ip link set veth-host up
   ip netns exec lan-a ip link set lo up
   ip netns exec lan-a ip route add default via 192.168.10.1
   ```
   Prüfen Sie mit `ping -c 2 192.168.10.10`. Nach einem Neustart wird das Skript erneut ausgeführt (zuvor `ip netns del lan-a`, falls der Namespace noch existiert). Das Skript wurde nicht ausgeführt (nicht bestätigt).
2. **Basis-Regelwerk anlegen:** Erstellen Sie auf `VM 1` die Datei `/etc/nftables.conf` mit folgendem Inhalt. Die `input`-Kette verwirft standardmäßig alles (Policy `drop`), erlaubt aber `lo`, bestehende Verbindungen, Ping, `SSH (TCP 22)`, `WireGuard (UDP 51820)` und `OpenVPN (UDP 1194)`. Die `forward`-Kette lässt nur Verkehr aus den VPN-Schnittstellen zum LAN und dessen Antworten durch:
   ```nft
   #!/usr/sbin/nft -f
   flush ruleset
   table inet filter {
       chain input {
           type filter hook input priority filter; policy drop;
           iif lo accept
           ct state established,related accept
           ct state invalid drop
           icmp type echo-request accept
           tcp dport 22 accept
           udp dport { 51820, 1194 } accept
       }
       chain forward {
           type filter hook forward priority filter; policy drop;
           ct state established,related accept
           iifname { "wg0", "tun0" } oifname "veth-gw" accept
       }
   }
   ```
   Die Syntax wurde mit `nft -c` geprüft (nftables 1.0.9, nicht auf Debian 12).
3. **NAT konfigurieren:** Ergänzen Sie in `/etc/nftables.conf` die Tabelle `table ip nat` mit der Kette `postrouting` (`type nat hook postrouting priority srcnat; policy accept;`) und der Regel `ip saddr { 10.8.0.0/24, 10.9.0.0/24 } oifname "veth-gw" masquerade`. Im isolierten Labor gibt es keinen Internetausgang; die Maskierung wird daher am simulierten LAN-Host `lan-a` gezeigt. In der Praxis steht in `oifname` das WAN-Interface (Name mit `ip -br a` prüfen).
4. **Regelwerk aktivieren:** Prüfen Sie die Datei mit `sudo nft -c -f /etc/nftables.conf` und laden Sie sie mit `sudo nft -f /etc/nftables.conf`. Prüfen Sie mit `sudo nft list ruleset`, ob die Regeln aktiv sind, und öffnen Sie von `VM 2` eine neue SSH-Verbindung (`ssh labadmin@10.0.0.1`). Als Ersatzzugang dient die Hyper-V-Konsole von `VM 1`; mit `sudo nft flush ruleset` heben Sie die Regeln im Notfall auf. Aktivieren Sie den Dienst `nftables` nicht für den Autostart.
5. **WireGuard unter Schutz testen:** Starten Sie `wg-quick up wg0` auf beiden VMs (OpenVPN läuft nicht). Pingen Sie von `VM 2` die Adressen `192.168.10.1` (Eingabekette) und `192.168.10.10` (Weiterleitung). Beobachten Sie auf `VM 1` mit `sudo ip netns exec lan-a tcpdump -i veth-host -n icmp`, dass der Host die Pakete von `192.168.10.1` (maskiert) und nicht von `10.8.0.100` sieht. Stoppen Sie danach `wg0` auf beiden VMs.
6. **OpenVPN unter Schutz testen:** Starten Sie `systemctl start openvpn-server@server` auf `VM 1` und `sudo openvpn --config /etc/openvpn/client/client1.ovpn` auf `VM 2`. Wiederholen Sie die Pings aus Aufgabe 5 und die Beobachtung mit `tcpdump`. Beenden Sie den Client (Strg+C) und den Dienst (`systemctl stop openvpn-server@server`).
#### Kontrollfragen
1. Warum ist `masquerade` (Source NAT) erforderlich, wenn VPN-Clients über das Gateway ins Internet surfen sollen?
2. Was passiert mit einer bestehenden SSH-Sitzung, wenn Sie in `nftables` die Input-Policy auf `drop` setzen, ohne vorher eine Regel für `state established` oder `tcp dport 22` anzulegen?
3. Welche Kette (Chain) in der Tabelle `filter` ist zuständig für Pakete, die von der VPN-Schnittstelle in die LAN-Schnittstelle geroutet werden sollen?

---

### Modul 12: Troubleshooting, Logging und Fehlerbehebung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende VPN-Verkehr auf Paket-Ebene analysieren.
  * Nach Abschluss dieses Moduls kann der Lernende Logfiles auswerten und Konfigurationsfehler lokalisieren.
* **Voraussetzungen:** Alle vorherigen Pflichtmodule, insbesondere Modul 11 (Regelwerk geladen, Namespace `lan-a` vorhanden). Die Aufgaben nennen, welcher Tunnel läuft; beide laufen nie gleichzeitig.
#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Paketanalyse mit `tcpdump` am physischen und virtuellen Interface | 4 |
| 12.2 | Log-Analyse von OpenVPN und WireGuard (`journalctl`, `dmesg`) | 3 |
| 12.3 | Typische Fehlerquellen (MTU, Zertifikate, Routing, Firewall) | 3 |
#### Praxisaufgaben (Hands-on Lab)
1. **Paketfluss analysieren (WireGuard):** Starten Sie `wg-quick up wg0` auf beiden VMs. Lassen Sie auf `VM 1` den Befehl `sudo tcpdump -i wg0 -n` laufen. Senden Sie von `VM 2` Pings an den Server. Identifizieren Sie Source- und Destination-IP in der Ausgabe. Wiederholen Sie den Test auf dem WAN-Interface (Name mit `ip -br a`, hier `eth0`: `sudo tcpdump -i eth0 udp port 51820 -n -X`) und vergleichen Sie den sichtbaren Payload (verschlüsselt).
2. **Fehler-Simulation OpenVPN:** Stoppen Sie `wg0` auf beiden VMs und starten Sie `systemctl start openvpn-server@server`. Sichern Sie `client1.ovpn` (`cp client1.ovpn client1.ovpn.bak`). Ersetzen Sie auf `VM 2` zuerst den Inhalt von `<tls-crypt>` durch einen neu erzeugten Schlüssel (`openvpn --genkey secret /tmp/falsch.key`), starten Sie den Client und beobachten Sie die Meldung am Client (erwartet nach etwa 60 Sekunden `TLS Error: TLS key negotiation failed to occur within 60 seconds`) und im Server-Log (`journalctl -u openvpn-server@server -f`, Meldung nicht bestätigt). Stellen Sie danach das Profil aus der Sicherung wieder her. Verfälschen Sie anschließend ein Zeichen im Block `<cert>` und beschreiben Sie, welche Meldung am Client und am Server erscheint (je nach geändertem Zeichen Ladefehler am Client oder Verifikationsfehler am Server; nicht bestätigt). Beheben Sie den Fehler mit der Sicherung.
3. **Fehler-Simulation Firewall:** Starten Sie `wg-quick up wg0` auf beiden VMs (OpenVPN gestoppt). Leeren Sie auf `VM 1` die Weiterleitungskette: `sudo nft flush chain inet filter forward` (die Policy `drop` bleibt). Pingen Sie von `VM 2` die Adressen `192.168.10.1` (funktioniert, Eingabekette) und `192.168.10.10` (schlägt fehl). Fügen Sie mit `sudo nft add rule inet filter forward counter` einen Zähler ein, wiederholen Sie den Ping und prüfen Sie mit `sudo nft list chain inet filter forward` und mit `tcpdump` auf `wg0` und `veth-host`, wo das Paket verworfen wird. Beheben Sie den Fehler mit `sudo nft -f /etc/nftables.conf`.
4. **MTU prüfen:** Prüfen Sie auf `VM 2` mit `ip link show wg0` die MTU (erwartet: 1420, nicht bestätigt) und testen Sie mit `ping -M do -s 1392 -c 2 10.8.0.1` (erwartet: Antwort) und `ping -M do -s 1393 -c 2 10.8.0.1` (erwartet: Fehlermeldung `message too long`, nicht bestätigt; 1420 minus 28 Byte Header ergibt 1392).
5. **WireGuard-Debugmeldungen:** Aktivieren Sie auf `VM 1` die Debugmeldungen des Moduls mit `echo 'module wireguard +p' | sudo tee /sys/kernel/debug/dynamic_debug/control` (ist `/sys/kernel/debug` leer, zuvor `sudo mount -t debugfs none /sys/kernel/debug`; Verfügbarkeit im Debian-Kernel nicht bestätigt). Senden Sie Pings von `VM 2` und lesen Sie die Meldungen mit `sudo dmesg | tail -n 20` oder `sudo journalctl -k -n 20`. Schalten Sie die Meldungen danach mit `echo 'module wireguard -p' | sudo tee /sys/kernel/debug/dynamic_debug/control` wieder aus.
6. **Rückbau:** Stoppen Sie `wg0` auf beiden VMs (`wg-quick down wg0`) und den OpenVPN-Dienst (`systemctl stop openvpn-server@server`). Leeren Sie auf `VM 1` die Regeln mit `sudo nft flush ruleset`, löschen Sie den Namespace mit `sudo ip netns del lan-a` und stellen Sie `dummy0` mit `sudo /usr/local/sbin/lab-dummy.sh` wieder her.
#### Kontrollfragen
1. Welchen entscheidenden Vorteil hat das Sniffen (`tcpdump`) auf der virtuellen Schnittstelle (`tun0` / `wg0`) im Vergleich zur physischen Schnittstelle (z.B. `eth0`) bei VPN-Fehlersuche?
2. Worauf deutet im OpenVPN-Log der Fehler `TLS Error: TLS key negotiation failed to occur within 60 seconds` primär hin?
3. Warum ist WireGuard im Logging besonders "leise" (stealthy), wenn fehlerhafte Pakete empfangen werden, und wo (welches Log) findet man dennoch Debug-Meldungen des Moduls?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (110 UE), Prioritäten (9x P1, 3x P2), Module und Lerneinheiten blieben unverändert (nachgerechnet). Aufgaben kamen hinzu; ob die Stunden dafür reichen, ist unerprobt (besonders Modul 2, 11 und 12). Die Befehle wurden nicht auf Debian 12 ausgeführt. Nur der EasyRSA-Ablauf (Modul 6, mit EasyRSA aus GitHub) und die nftables-Syntax (Modul 11, `nft -c`) wurden in einer Testumgebung geprüft. Das Verhalten von `wg-quick`, `wg syncconf`, Namespaces und OpenVPN-Meldungen ist nicht geprüft und im Text als „nicht bestätigt“ gekennzeichnet.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| A.2 | WireGuard-Paper auf NDSS 2017 korrigiert, Debian-Handbuch auf die Ausgabe für Debian 11 korrigiert, Quellen für IPsec (RFC 4301, 4303, 7296), Noise, TLS 1.3, Curve25519, `wg`/`wg-quick` und nftables ergänzt | „Alle Quellen existieren real“ war nicht geprüft; die Ausgabe „Debian 12“ des Handbuchs ist nicht belegt (die Seite nennt Debian 11); IPsec, Noise und TLS wurden im Text genannt und hatten keine Quelle |
| A.3 | Debian-Installation, SSH-Server, Benutzer, zweiter Switch für die Internet-Phase, Adressplan mit Tunnelnetzen, Hostnamen, Regel „nie beide Tunnel gleichzeitig“, `iperf3` entfernt, `wireguard-tools` und `wireguard` vereinheitlicht, Fokus „Ubuntu“ gestrichen | Die Installation, das zweite Netz, `10.8.0.0/24` und `10.9.0.0/24` und ein SSH-Zugang waren nirgends geplant; `iperf3` wurde nie benutzt; „Ubuntu“ kam im Labor nicht vor |
| Modul 1 | Einheit 1.2, Frage 3, neue Frage 4 | Die Aussage, RFC-1918-Adressen im Tunnel seien „zwingend erforderlich“, ist falsch; die Schutzziele aus Einheit 1.1 hatten keine Frage |
| Modul 2 | Voraussetzungen, Aufgaben 1 bis 5 | Statische IP ohne Dateiangabe, Forwarding nur persistent (Lernziel „temporär“), das als „Skript“ angekündigte Dummy-Interface war eine Handeingabe und nach Neustart verloren, kein Prüfpunkt |
| Modul 3 | Aufgaben 1 bis 3 | Schlüsselrechte (`umask`, `chmod 600`), Diensteverwaltung (Einheit 3.3) ohne Aufgabe, Autostart würde später mit OpenVPN kollidieren |
| Modul 4 | Aufgaben 1 bis 4 | Der Client-Private-Key fehlte in der Aufgabe; Änderung der Konfigurationsdatei wirkt nicht ohne Neustart des Interfaces; `ip route` zeigt die Full-Tunnel-Route von `wg-quick` nicht (eigene Tabelle) |
| Modul 5 | Voraussetzungen, Aufgaben 1 bis 4, Frage 2 | `wg syncconf` setzt keine Routen (laut `wg-quick`-Handbuch nicht bestätigt, daher als Beobachtungsaufgabe), der Ping zwischen Gateways prüfte keine Subnetz-Quelladressen und nur eine Richtung; die Begründung „Portkonflikt“ war falsch (UDP 51820 gegen 1194), richtig ist der Routenkonflikt |
| Modul 6 | Voraussetzungen, Einheit 6.1, Aufgaben 1 bis 6 | Der Rückbau von WireGuard stand nur im optionalen Modul 5, Pflichtmodul 6 verlangte ihn als Voraussetzung; Client-Zertifikat „analog zu Aufgabe 3“ hätte den Typ `server` benutzt; UDP/TCP aus Frage 3 in Modul 7 fehlte in der Einheit; Dateipfade der PKI nicht genannt |
| Modul 7 | Aufgaben 1 bis 3 | Dateipfade der EasyRSA-Ausgaben nicht genannt; Zertifikatsdirektiven nicht ausgeschrieben; Dienstverwaltung (Lernziel 2) nur als `enable --now` |
| Modul 8 | Einheit 8.1, Aufgaben 1 bis 4, Frage 2 | Schlüsseldateien sind nur für root lesbar und ein SSH-Login als root ist gesperrt (Übertragungsweg unlösbar); `remote-cert-tls server` stand in Frage 3, aber nicht im Profil; Frage 2 hatte keine Entsprechung in den Einheiten |
| Modul 9 | Lernziel 2, Aufgabe 3 | `iroute` wurde im Lernziel „beibringen“, aber erst in Modul 10 angewendet |
| Modul 10 | Aufgaben 3 und 4 | „Bidirektional“ prüfte nur eine Richtung; der Rückbau stoppte nur den Client, der Server und seine Route `192.168.20.0` blieben und hätten in Modul 11 den WireGuard-Start (Routenkonflikt) gestört |
| Modul 11 | Einheit 11.3, Aufgaben 1 bis 6, Voraussetzungen | Das Regelwerk ohne `ct state established`, ohne ICMP und ohne Freigabe der VPN-Schnittstellen hätte die Pings der Aufgabe 4 verworfen; es gab keine `forward`-Kette; Weiterleitung und NAT waren im Labor nicht testbar, weil jede LAN-Adresse auf dem Gateway selbst liegt (neuer Namespace `lan-a`); die NAT-Regel über `eth0` hätte keinen Verkehr gesehen; kein Prüfpunkt vor dem Sperren; OpenVPN wurde nicht getestet |
| Modul 12 | Voraussetzungen, Aufgaben 1 bis 6 | Ein verfälschtes Zertifikat erzeugt keine Meldung im Server-Log, die Frage 2 passt zu einem falschen `tls-crypt`-Schlüssel; die `forward`-Sperre hätte nichts bewirkt (kein weitergeleiteter Verkehr); MTU (Einheit 12.3) und `dmesg` (Einheit 12.2) hatten keine Aufgabe; kein Rückbau; Sicherungskopie vor dem Verfälschen fehlte |

**Bewertung des Prüfvermerks der ersten Fassung:** Punkt 1 stimmt in den Summen, enthält aber eine Entwurfsnotiz („ursprünglich 100 gezählt“), die nicht in einen Prüfvermerk gehört. Punkt 2 ist nicht erfüllt: Installation, Switch für die Internet-Phase, Netze und SSH-Zugang fehlten, `iperf3` blieb ungenutzt. Punkt 3 ist nicht erfüllt: Die Behauptung „existieren real“ wurde nicht geprüft, Jahr und Ausgabe zweier Quellen waren falsch bzw. nicht belegt, IPsec, Noise und TLS hatten keine Quelle. Punkt 4 ist nicht erfüllt: Der Routenkonflikt der beiden Tunnel (Modul 5, 10, 11) und der fehlende Rückbau des OpenVPN-Servers wurden nicht erkannt. Punkt 5 ist nicht erfüllt (Modul 3, 8, 9, 11, 12 und eine falsche Kontrollfrage in Modul 1). Punkt 6 ist teilweise erfüllt: Der Rückbau von WireGuard hing am optionalen Modul 5. Punkt 7 ist nicht erfüllt: Das Site-to-Site-Szenario bestand nur aus Gateway-Adressen, Weiterleitung und NAT waren nicht testbar. Punkt 8 ist nicht erfüllt (Dateiübertragung, Rechte, SSH-Server, Namen). Punkt 9 ist nicht erfüllt: Das Firewall-Regelwerk hätte die Aufgaben selbst blockiert; `sysctl -w` im Vermerk steht nicht im Text, und „keine destruktiven Befehle“ ignoriert das Verfälschen des Zertifikats ohne Sicherung.

**Hinweise und offene Punkte:**

* **Nicht bestätigt, vor Kursstart auf Debian 12 prüfen:** Adaptername `eth0`; Konfiguration über `/etc/network/interfaces`; sudo für `labadmin` bei leerem Root-Kennwort; Standardrouten und Tabelle 51820 bei `wg-quick`; Verhalten von `wg syncconf` bei Routen; MTU 1420; Debugmeldungen über `dynamic_debug`; relative Pfade in `server.conf`; Meldungen von OpenVPN bei falschem Schlüssel oder Zertifikat; Namespace-Skript in Modul 11; Passwort-Login von root per SSH.
* Mit dem Namespace `lan-a` ist die Zeit in Modul 11 und 12 knapp; wer sie kürzen muss, lässt Aufgabe 6 (Modul 11) und Aufgaben 4 und 5 (Modul 12) weg.