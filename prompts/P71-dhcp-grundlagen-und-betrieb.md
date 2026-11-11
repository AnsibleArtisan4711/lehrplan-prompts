# P71 – DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea)

Priorität A, Netzwerkdienste und Firewall.

```text
Erstelle einen Lehrplan für den Kurs „DHCP-Grundlagen und -Betrieb (Windows-Server und ISC Kea)“.

Fokus-Technologien / Plattformen: Windows Server (DHCP-Rolle, PowerShell-Modul DhcpServer), Debian/Ubuntu Linux mit ISC Kea, DHCP-Relay unter Linux, DHCPv4 und DHCPv6
Spezifische Vorkenntnisse: IT-Grundlagen und Grundkenntnisse in Netzwerken (IPv4-Adressen, Subnetze, Standardgateway, Umgang mit Hyper-V)
Umfang: etwa 12 Module (10 bis 14), zusammen etwa 100 bis 120 Unterrichtsstunden (UE)
Kernthemen: DHCP-Grundlagen und DORA-Ablauf; Lease-Zeiten, Erneuerung und Rebinding; Scopes, Reservierungen und Ausschlüsse; Optionen, Klassen und Policies; DHCP-Relay und mehrere Subnetze; DHCP in Active Directory (Autorisierung, dynamische DNS-Updates); DHCP-Failover und Split-Scope; ISC Kea unter Linux; DHCPv6 und Router Advertisements; Überwachung, Sicherung und Migration; Rogue-DHCP und Härtung; Fehlersuche mit ipconfig, tcpdump und Protokollen
Thematische Abgrenzung (Out of Scope): DNS-Betrieb ist ein eigener Lehrplan (DNS-Grundlagen) und wird nur an der Schnittstelle der dynamischen Updates behandelt; DNSSEC, PXE-Netzwerkstart und Betriebssystem-Rollout, IPAM, 802.1X und DHCP-Funktionen von Heimroutern und Cloud-Diensten gehören nicht zum Kurs; DHCP Snooping nur konzeptionell
Spezifische Labor-Ressourcen: 1x Linux-Router-VM mit drei Netzen (Relay); 2x Windows-Server-VM (DHCP, Failover); 1x Windows-Server-VM als Domänencontroller (ab Modul 6); 1x Linux-Server-VM (Kea); 1 Windows-Client-VM; 1 Linux-Client-VM; drei private Hyper-V-Switches ohne Verbindung zum Heimnetz
Zusätzliche Hinweise: Versions- und Supportstände mit Stand nennen; kennzeichne Unsicherheit; Befehle, Parameter und Menünamen nicht erfinden. ISC DHCP wird nicht mehr als Server behandelt (Kea statt ISC DHCP).
```
