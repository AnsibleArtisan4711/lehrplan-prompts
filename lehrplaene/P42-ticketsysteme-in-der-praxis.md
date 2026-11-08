# Lehrplan: Ticketsysteme in der Praxis

| Kriterium | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemtechniker/Systemadministratoren (Raum Österreich/EU). |
| **Vorkenntnisse** | IT-Grundlagen, Netzwerk-Grundlagen (IP-Adressen, Subnetze, DNS), grundlegende Linux-Befehle (Shell, Paketverwaltung, Dateisystem). |
| **Gesamtumfang** | 8 Module, 45 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Zammad (Open Source, laut Dokumentation Version 7.x; genaue Version nicht geprüft), Ubuntu Linux, Nginx, PostgreSQL, Elasticsearch, Mailpit (lokales Mail-Testing). |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidungen mit reinen Linux-Admin-Kursen; tiefe Datenbankadministration (SQL-Tuning) oder ITIL-Theorieprüfungen sind nicht Teil dieses Kurses. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen und Vorbereitung des Labors | 1 | 4 |
| 2 | Installation und Grundkonfiguration von Zammad | 1 | 6 |
| 3 | Kategorien, Gruppen und Berechtigungskonzepte | 1 | 6 |
| 4 | SLAs, Eskalationen und Prioritäten | 1 | 6 |
| 5 | Wissensdatenbank (Knowledge Base) und Textbausteine | 2 | 4 |
| 6 | E-Mail-Anbindung und Kommunikationswege | 1 | 7 |
| 7 | Automatisierung (Trigger, Scheduler, Makros) | 2 | 6 |
| 8 | Reporting, Monitoring-Anbindung und Troubleshooting | 1 | 6 |
| **Gesamt** | **Summe der Einheiten: 6x Prio 1, 2x Prio 2** | | **45** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln zwingend erforderliche Kernkompetenzen. Module mit Priorität 2 dienen der Vertiefung und können bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt ein Modul mit Priorität 2 voraus.*

### 2. Quellen

* **Zammad Admin Documentation**, Zammad GmbH, abgerufen am 08.11.2026 (Version „latest“), URL: https://admin-docs.zammad.org/ (verwendet: Calendars, SLAs, Knowledge Base, Group Permissions, Scheduler, Trigger, Text Modules)
* **Zammad Dokumentation: Software-Voraussetzungen und Hardware**, Zammad GmbH, abgerufen am 08.11.2026, URLs: https://docs.zammad.org/en/latest/prerequisites-software.html und https://docs.zammad.org/en/latest/prerequisites/hardware.html
* **Zammad Package Installation**, Zammad GmbH, abgerufen am 08.11.2026, URL: https://next.zammad.org/en/get-started/installation/package.html
* **Zammad User Documentation: Ticket Basics**, Zammad GmbH, abgerufen am 08.11.2026, URL: https://user-docs.zammad.org/en/latest/basics/ticket-basics.html
* **Zammad REST API (Einführung und Ticketstatus)**, Zammad GmbH, abgerufen am 08.11.2026 (die Einführungsseite nur teilweise), URLs: https://docs.zammad.org/en/latest/api/intro.html und https://next.zammad.org/en/reference/rest-api/states.html
* **Mailpit**, Mailpit Projekt, Version 1.33.1 (Programm am 08.11.2026 heruntergeladen, Hilfetext ausgewertet und getestet), Download: https://github.com/axllent/mailpit/releases (Datei `mailpit-linux-amd64.tar.gz`); Dokumentation: https://mailpit.axllent.org/docs/ (nicht abgerufen)
* **Ubuntu Server 24.04 LTS Documentation**, Canonical Ltd., Stand nicht geprüft, URL: https://ubuntu.com/server/docs
* **Elasticsearch-Installation** (Anleitung von Elastic bzw. Zammad-Tutorial zu Elasticsearch 9, auf das die Zammad-Installationsseite verweist): keine geprüfte URL
* **Microsoft Learn, Hyper-V und Linux-VMs der Generation 2** (Secure-Boot-Vorlage „Microsoft UEFI Certificate Authority“): bei der Prüfung von P01 bestätigt, URL hier nicht erneut geprüft
* **RFC 1918: Address Allocation for Private Internets**, Internet Engineering Task Force (IETF), Stand: Februar 1996, URL: https://datatracker.ietf.org/doc/html/rfc1918
* **Top-Level-Domain `.internal`:** laut ICANN-Beschluss von 2024 für private Nutzung reserviert (nicht bestätigt, keine geprüfte URL)

### 3. Labor-Setup & Rahmenbedingungen

* **Hypervisor:** Hyper-V (Windows Client oder Server). Der Host braucht mindestens 16 GB RAM (Annahme: 10 GB für die Server-VM plus 4 GB für die Client-VM plus Host). Beide VMs sind Generation 2. Für die Ubuntu-VM ist als Secure-Boot-Vorlage „Microsoft UEFI Certificate Authority“ zu wählen (sonst startet sie nicht); die Windows-11-VM braucht ein virtuelles TPM.
* **Netzwerk:**
  * Ein privater virtueller Switch (`Private-Switch`) für die isolierte Kommunikation.
  * Für Modul 1 und 2 wird temporär ein Switch mit Internetzugang für die Server-VM benötigt: der `Default Switch` (nur unter Windows Client, NAT) oder ein externer Switch (`External-Switch`, z. B. unter Windows Server).
* **Server-VM (erforderlich ab Modul 1):** 1x Ubuntu 24.04 LTS Server. IP-Adresse (isoliert): `192.168.100.10/24`. Hostname: `zammad-srv`. Ressourcen: 4 vCPU, 10 GB RAM (feste Zuweisung, ohne Dynamic Memory), 40 GB Festplatte (Zammad verlangt laut Dokumentation mindestens 2 Kerne und 6 GB RAM, dazu 4 GB, wenn Elasticsearch auf demselben Server läuft; die Plattengröße ist eine Annahme). Benutzer `labadmin` mit `sudo`, OpenSSH-Server installiert.
* **Client-VM (erforderlich ab Modul 1):** 1x Windows 11 Evaluation (oder Linux Desktop). IP-Adresse: `192.168.100.20/24`. Hostname: `client-pc`. 4 GB RAM, lokales Administratorkonto.
* **Vorbereitung vor Modul 1 (nicht Teil der UE):** Beide VMs sind installiert und starten. Die Installation der Betriebssysteme ist nicht Gegenstand dieses Lehrplans.
* **Namensauflösung:** Da kein Active Directory vorhanden ist, erfolgt die Namensauflösung im isolierten Netz über lokale `/etc/hosts` bzw. `hosts`-Dateien (unter Windows `C:\Windows\System32\drivers\etc\hosts`, Bearbeitung nur als Administrator). Zieldomäne: `zammad.example.internal`.
* **Zusatzsoftware (erforderlich ab Modul 2):**
  * Zammad aus der Zammad-Paketquelle (PostgreSQL ab Version 15 und Nginx installiert das Paket laut Dokumentation selbst, sofern nicht vorhanden).
  * Elasticsearch aus der Paketquelle von Elastic (laut Dokumentation für aktuelle Zammad-Versionen ab 8.15 und unter 10; für Zammad „optional, aber dringend empfohlen“, in diesem Lehrplan Pflicht).
  * Mailpit als Binary von GitHub (für Modul 6).
  * Voraussetzungspakete für die Zammad-Paketquelle: `curl`, `apt-transport-https`, `gnupg`.
* **Mailpit im Lehrplan (zwei Instanzen):** Mailpit stellt einen SMTP-Server und eine Weboberfläche bereit; einen POP3-Server nur, wenn eine Passwortdatei angegeben wird (`--pop3-auth-file`); IMAP gibt es nicht. Würde Zammad seine ausgehenden Mails in dasselbe Postfach schreiben, aus dem es eingehende Mails abruft, holte es seine eigenen Nachrichten zurück (im Test erschienen ausgehende Mails in der POP3-Liste). Deshalb laufen zwei Instanzen:

| Dienst | Zweck | SMTP | Weboberfläche | POP3 |
| :--- | :--- | :--- | :--- | :--- |
| `mailpit-out` | Empfängt die **ausgehenden** Mails von Zammad | `127.0.0.1:1025` | `0.0.0.0:8025` | aus |
| `mailpit-in` | Postfach für **eingehende** Mails, das Zammad per POP3 abruft | `127.0.0.1:2025` | `0.0.0.0:8026` | `127.0.0.1:1110`, Benutzer `zammad`, Passwort `Lab-Passwort-1` (nur für das Labor) |

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen und Vorbereitung des Labors
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den grundlegenden Zweck eines Ticketsystems erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Labor-VMs netzwerktechnisch für die Installation vorbereiten.
* **Voraussetzungen:** Beide VMs sind laut Abschnitt A.3 installiert und starten (Vorbereitung, nicht Teil der UE).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | ITSM-Grundlagen und Zweck eines Ticketsystems (Incident/Service Request) | 1 |
| 1.2 | Architektur von Zammad (Applikationsserver, Datenbank, Suchmaschine, Webserver) | 1 |
| 1.3 | Netzwerkkonfiguration und Betriebssystem-Updates | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **IP-Konfiguration:** Konfiguriere die Server-VM auf die IP `192.168.100.10/24` und die Client-VM auf `192.168.100.20/24` auf dem privaten Hyper-V-Switch. Unter Ubuntu ermittelst du den Schnittstellennamen mit `ip a`, bearbeitest die Datei in `/etc/netplan/` (Dateiname mit `ls /etc/netplan` nachsehen) und wendest sie mit `sudo netplan apply` an; Beispiel (Schnittstellenname anpassen, Einrückung nur mit Leerzeichen):

   ```yaml
   network:
     version: 2
     ethernets:
       eth0:
         addresses: [192.168.100.10/24]
   ```

   Unter Windows setzt du die Adresse in den Netzwerkeinstellungen.
2. **Namensauflösung:** Trage `192.168.100.10 zammad.example.internal` in die `hosts`-Datei der Client-VM und der Server-VM ein. Teste die Verbindung mittels `ping zammad.example.internal` von der Client-VM aus. Ein Ping von der Server-VM zur Windows-Client-VM schlägt standardmäßig fehl, weil die Windows-Firewall Echo-Anfragen blockiert; erkläre, warum das kein Netzwerkfehler ist.
3. **Temporärer Internetzugang:** Füge der Server-VM eine zweite Netzwerkschnittstelle mit Internetzugang (Default Switch bzw. externer Switch) hinzu. Ubuntu konfiguriert die neue Schnittstelle nicht von selbst: Ergänze sie in Netplan mit `dhcp4: true`, wende die Konfiguration an und prüfe mit `ip route`, ob eine Default-Route vorhanden ist. Führe dann `sudo apt update` und `sudo apt upgrade` durch.

#### Kontrollfragen
1. Worin unterscheidet sich ein Incident von einem Service Request im Kontext von Ticketsystemen?
2. Welche Hauptkomponenten (Dienste) werden für den Betrieb von Zammad typischerweise auf Linux benötigt?
3. Warum wird in einer Active-Directory-freien Umgebung die `hosts`-Datei für die Namensauflösung benötigt?


### Modul 2: Installation und Grundkonfiguration von Zammad
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zammad inklusive aller Abhängigkeiten installieren.
  * Nach Abschluss dieses Moduls kann der Lernende das System in einer komplett isolierten Umgebung betreiben.
* **Voraussetzungen:** Abgeschlossenes Modul 1 (funktionierendes Netzwerk und temporärer Internetzugang).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Installation der Abhängigkeiten (PostgreSQL, Elasticsearch, Nginx) | 2 |
| 2.2 | Installation von Zammad über die Paketquelle und von Mailpit als Binary | 2 |
| 2.3 | Web-Setup, System-Init und Netzwerk-Rückbau | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Paketinstallation:** Installiere Elasticsearch und Zammad nach der offiziellen Dokumentation via `apt`. Reihenfolge laut Zammad-Installationsseite: zuerst Elasticsearch (Anleitung von Elastic bzw. das Zammad-Tutorial zu Elasticsearch 9), dann `sudo apt install curl apt-transport-https gnupg`, Schlüssel und Paketquellen-Datei für Ubuntu 24.04 aus der Zammad-Dokumentation einrichten, `sudo apt update` und `sudo apt install zammad`. PostgreSQL und Nginx werden dabei laut Dokumentation automatisch mitinstalliert. Lade zusätzlich die Datei `mailpit-linux-amd64.tar.gz` von den GitHub-Releases des Mailpit-Projekts herunter, entpacke sie (`tar xzf mailpit-linux-amd64.tar.gz mailpit`) und installiere die Binary mit `sudo install -m 755 mailpit /usr/local/bin/mailpit`. Prüfe mit `mailpit version`; ohne Internet meldet das Programm zusätzlich einen Fehler bei der Update-Suche, die Versionszeile erscheint trotzdem.
2. **Web-Setup:** Öffne auf der Client-VM den Browser unter `http://zammad.example.internal`. Durchlaufe den Initial-Wizard. Lege einen initialen Administrator an (z. B. `admin@example.internal`) und trage als System-URL `http://zammad.example.internal` ein. Überspringe die E-Mail-Konfiguration im Wizard.
3. **Rückbau der Internetverbindung:** Entferne die Konfiguration der zweiten Schnittstelle aus Netplan, fahre die Server-VM herunter, entferne die zweite Netzwerkschnittstelle (Internetzugang) in Hyper-V und starte die VM neu. Verifiziere, dass Zammad vom Client aus weiterhin erreichbar ist, dass `ip route` keine Default-Route zeigt und dass `ping -c 3 8.8.8.8` auf dem Server fehlschlägt (erfolgreiche Isolation). Erstelle danach einen Hyper-V-Checkpoint `nach-Modul-2` der Server-VM als Rückkehrpunkt für die Folgemodule.

#### Kontrollfragen
1. Welche Aufgabe übernimmt Elasticsearch in der Zammad-Architektur?
2. Warum wird ein Webserver wie Nginx vor den eigentlichen Zammad-Applikationsserver geschaltet?
3. Welcher Port wird standardmäßig für unverschlüsselte HTTP-Verbindungen genutzt, die vom Client zum Nginx-Server aufgebaut werden?


### Modul 3: Kategorien, Gruppen und Berechtigungskonzepte
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Gruppen (Queues) für verschiedene IT-Teams anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Agenten und Kunden mit passenden Berechtigungen konfigurieren.
* **Voraussetzungen:** Abgeschlossenes Modul 2 (funktionierendes Zammad).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Rollenkonzept in Zammad (Admin, Agent, Kunde) | 2 |
| 3.2 | Erstellung und Verwaltung von Gruppen (Queues) | 2 |
| 3.3 | Anlage von Benutzern und Zuweisung von Berechtigungen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Gruppen anlegen:** Erstelle in der Zammad-Admin-Oberfläche zwei neue Gruppen: `1st-Level-Support` und `Infrastruktur`.
2. **Benutzer anlegen:** Erstelle den Benutzer `Agent Müller` (E-Mail `mueller@example.internal`, Rolle: Agent, Passwort setzen; Gruppenrecht „Full“ auf `1st-Level-Support`, „Read“ auf `Infrastruktur`). Erstelle den Benutzer `Kunde Schmidt` (E-Mail `schmidt@example.internal`, Rolle: Customer, Passwort setzen).
3. **Ticket-Testlauf:** Melde dich als `Kunde Schmidt` am Webinterface an und erstelle ein Ticket in der Gruppe `1st-Level-Support`. Kann der Kunde die Gruppe im Formular nicht wählen, lege das Ticket als Admin für `Kunde Schmidt` an. Melde dich als `Agent Müller` an und übernimm das Ticket (Besitzer setzen).

#### Kontrollfragen
1. Was ist der funktionale Unterschied zwischen einer "Rolle" und einer "Gruppe" in Zammad?
2. Darf ein Benutzer in Zammad gleichzeitig die Rolle "Agent" und "Customer" besitzen? Begründe die Antwort.
3. Welches Gruppenrecht (Read, Change, Create) benötigt ein Agent mindestens in der Zielgruppe, um ein Ticket von einer Gruppe in eine andere zu verschieben?


### Modul 4: SLAs, Eskalationen und Prioritäten
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Service Level Agreements (SLAs) definieren und auf Gruppen anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Geschäftszeiten (Calendars) konfigurieren.
* **Voraussetzungen:** Abgeschlossenes Modul 3 (Vorhandene Gruppen und Agenten).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Konzept von SLAs (Reaktionszeit, Lösungszeit) | 2 |
| 4.2 | Konfiguration von Geschäftszeiten (Kalender) | 2 |
| 4.3 | SLA-Regeln in Zammad anlegen und testen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Kalender konfigurieren:** Erstelle unter Manage > Calendars einen Kalender "Standard-Geschäftszeiten" (Mo-Fr, 08:00 - 17:00 Uhr, Zeitzone Europe/Vienna).
2. **SLA definieren:** Erstelle unter Manage > SLAs ein SLA namens "Kritische Störung". Verknüpfe es mit dem Kalender. Setze als Bedingungen: `Gruppe = 1st-Level-Support` und `Priorität = 3 (hoch)`. Definiere eine Erstreaktionszeit (First Response) von 2 Stunden.
3. **Eskalation testen:** Erstelle ein Ticket in der Gruppe `1st-Level-Support` mit Priorität 3 (hoch), als Kunde oder, falls der Kunde die Priorität nicht wählen kann, als Agent im Namen von `Kunde Schmidt`. Prüfe als Agent in der Ticket-Ansicht den angezeigten Eskalationszeitpunkt (beim Darüberfahren erscheinen alle anstehenden Zeiten). Beachte: Laut Dokumentation zählen nur die Geschäftszeiten des Kalenders; läuft der Test außerhalb von Mo-Fr 08:00 - 17:00 Uhr, beginnt die Frist erst zur nächsten Geschäftszeit. Erkläre, warum der Zeitpunkt dann nicht „jetzt plus 2 Stunden“ ist.

#### Kontrollfragen
1. Warum ist es wichtig, SLAs an einen spezifischen Arbeitszeiten-Kalender zu binden?
2. Was passiert typischerweise im Ticketsystem, wenn die Erstreaktionszeit eines SLAs überschritten wird?
3. Worin unterscheiden sich Erstreaktionszeit und Lösungszeit?


### Modul 5: Wissensdatenbank (Knowledge Base) und Textbausteine
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Wissensdatenbank aktivieren und befüllen.
  * Nach Abschluss dieses Moduls kann der Lernende Textbausteine zur Effizienzsteigerung einrichten.
* **Voraussetzungen:** Abgeschlossenes Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Struktur und Sichtbarkeiten der Wissensdatenbank | 2 |
| 5.2 | Erstellung von internen und externen Artikeln | 1 |
| 5.3 | Konfiguration von Textbausteinen (Snippets) | 1 |

#### Praxisaufgaben (Hands-on Lab)
1. **Knowledge Base aktivieren:** Aktiviere unter Manage > Knowledge Base den Schalter, wähle die Sprache und lege die Wissensdatenbank mit „Create Knowledge Base“ an. Erstelle eine Kategorie "Netzwerk".
2. **Artikel anlegen:** Erstelle einen Artikel "VPN-Einrichtung" (Sichtbarkeit: öffentlich) und einen Artikel "Router-Wartung" (Sichtbarkeit: nur Mitarbeitende; ohne echte Passwörter oder Zugangsdaten). Teste die Sichtbarkeit, indem du auf der Client-VM abgemeldet `http://zammad.example.internal/help` öffnest: Nur der öffentliche Artikel darf erscheinen.
3. **Textbausteine:** Erstelle unter Manage > Text modules einen Textbaustein mit dem Namen "Passwort zurücksetzen", dem Keyword `pwd` und dem Inhalt "Bitte teilen Sie uns Ihren Benutzernamen mit, wir setzen Ihr Passwort zurück.". Teste den Baustein in einer Ticket-Antwort: Tippe `::` und suche den Baustein über Name oder Keyword.

#### Kontrollfragen
1. Warum sollte strikt zwischen internen und öffentlichen Wissensartikeln getrennt werden?
2. Wie ruft ein Agent einen Textbaustein während der Ticketbearbeitung auf?
3. Welche Berechtigung muss ein Benutzer haben, um Artikel in der Knowledge Base erstellen und bearbeiten zu dürfen, und wer hat sie standardmäßig?


### Modul 6: E-Mail-Anbindung und Kommunikationswege
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Mailpit als lokalen SMTP/POP3-Simulator konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende eingehende und ausgehende E-Mail-Kanäle im Ticketsystem einrichten.
* **Voraussetzungen:** Abgeschlossenes Modul 2 und Modul 3 (Gruppen `1st-Level-Support` und `Infrastruktur`, `Kunde Schmidt`). (Unabhängig von Modul 4 und 5).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Funktionsweise von E-Mail-Integration (SMTP vs. POP3/IMAP) | 2 |
| 6.2 | Einrichtung des lokalen Simulators (Mailpit, zwei Instanzen) als Dienste | 2 |
| 6.3 | Anbindung des Simulators an Zammad und Funktionstests | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Mailpit starten:** Richte auf der Server-VM zwei Mailpit-Dienste laut Tabelle in Abschnitt A.3 ein (`mailpit-out`, `mailpit-in`). Vorbereitung (Befehle nicht auf Ubuntu ausgeführt):

   ```bash
   sudo useradd --system --no-create-home --shell /usr/sbin/nologin mailpit
   sudo mkdir -p /etc/mailpit
   echo 'zammad:Lab-Passwort-1' | sudo tee /etc/mailpit/pop3users.txt
   sudo chown root:mailpit /etc/mailpit/pop3users.txt
   sudo chmod 640 /etc/mailpit/pop3users.txt
   ```

   Lege `/etc/systemd/system/mailpit-out.service` an (Unit-Syntax mit `systemd-analyze verify` geprüft, Dienst unter Ubuntu nicht gestartet):

   ```ini
   [Unit]
   Description=Mailpit - ausgehende Mails von Zammad
   After=network.target

   [Service]
   User=mailpit
   StateDirectory=mailpit-out
   ExecStart=/usr/local/bin/mailpit --database /var/lib/mailpit-out/mailpit.db --listen 0.0.0.0:8025 --smtp 127.0.0.1:1025
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

   Die Datei `mailpit-in.service` unterscheidet sich in `Description`, `StateDirectory=mailpit-in` und in dieser Zeile:

   ```ini
   ExecStart=/usr/local/bin/mailpit --database /var/lib/mailpit-in/mailpit.db --listen 0.0.0.0:8026 --smtp 127.0.0.1:2025 --pop3 127.0.0.1:1110 --pop3-auth-file /etc/mailpit/pop3users.txt
   ```

   Aktiviere beide mit `sudo systemctl daemon-reload` und `sudo systemctl enable --now mailpit-out mailpit-in`. Prüfe mit `ss -tlnp`, dass die Ports 1025, 2025, 1110, 8025 und 8026 lauschen, und rufe von der Client-VM `http://192.168.100.10:8025` und `http://192.168.100.10:8026` auf.
2. **Ausgehende Mails (SMTP):** Lege in Zammad die Absenderadresse `support@example.internal` an und ordne sie den Gruppen `1st-Level-Support` und `Infrastruktur` zu. Konfiguriere den E-Mail-Kanal so, dass ausgehende Mails über SMTP an `127.0.0.1` (Port 1025) ohne Verschlüsselung und ohne Authentifizierung gesendet werden. Teste den Versand, indem du in einem Ticket von `Kunde Schmidt` als Agent antwortest: Die Mail muss in der Weboberfläche von `mailpit-out` (Port 8025) auftauchen.
3. **Eingehende Mails (POP3):** Konfiguriere in Zammad den Abruf über POP3 von `127.0.0.1` (Port 1110, Benutzer `zammad`, Passwort `Lab-Passwort-1`, ohne Verschlüsselung), Zielgruppe `1st-Level-Support`. Simuliere einen externen E-Mail-Eingang an die Instanz `mailpit-in`, zum Beispiel auf der Server-VM mit einer Datei `mail.txt` (Zeilen `From: schmidt@example.internal`, `To: support@example.internal`, `Subject: Drucker defekt`, eine Leerzeile, dann der Text):

   ```bash
   curl --url smtp://127.0.0.1:2025 --mail-from schmidt@example.internal --mail-rcpt support@example.internal -T mail.txt
   ```

   Alternativ nutzt du die Send-API von Mailpit (`POST http://192.168.100.10:8026/api/v1/send`). Warte, bis Zammad das Postfach abgerufen hat, und prüfe, ob in der Gruppe `1st-Level-Support` ein neues Ticket entstanden ist.

#### Kontrollfragen
1. Warum benötigt ein Ticketsystem sowohl SMTP als auch IMAP/POP3?
2. Wieso ist der Einsatz eines Tools wie Mailpit in isolierten Testumgebungen Best-Practice?
3. Was passiert in Zammad standardmäßig, wenn ein Kunde auf eine Benachrichtigungs-E-Mail zu einem geschlossenen Ticket antwortet?
4. Warum laufen in diesem Lehrplan zwei getrennte Mailpit-Instanzen für ausgehende und eingehende Mails?


### Modul 7: Automatisierung (Trigger, Scheduler, Makros)
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ereignisgesteuerte Automatisierungen (Trigger) einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende zeitgesteuerte Automatisierungen (Scheduler) anlegen.
* **Voraussetzungen:** Abgeschlossenes Modul 3 und Modul 6 (Absenderadresse und funktionierender Postausgang).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Ereignisgesteuerte Trigger (z. B. Auto-Replies) | 2 |
| 7.2 | Zeitgesteuerte Aufgaben (Scheduler) | 2 |
| 7.3 | Manuelle Massenaktionen durch Makros | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Trigger anlegen:** Erstelle unter Manage > Trigger einen Trigger, der dem Kunden bei Ticketerstellung in der Gruppe `Infrastruktur` automatisch eine E-Mail sendet ("Wir haben Ihre Netzwerkanfrage erhalten"), mit den Bedingungen „Action is created“ und „Group is Infrastruktur“. Laut Dokumentation überspringt Zammad einen E-Mail-Trigger, wenn der Gruppe keine E-Mail-Adresse zugeordnet ist (erledigt in Modul 6, Aufgabe 2). Zammad bringt außerdem einen Standard-Trigger mit, der nach neuen Tickets eine Eingangsbestätigung sendet; deaktiviere ihn für den Test, sonst erhält der Kunde zwei Mails. Prüfe das Ergebnis in der Weboberfläche von `mailpit-out`.
2. **Scheduler anlegen:** Erstelle unter Manage > Scheduler einen Scheduler, der alle Tickets im Status `pending reminder` (der Standardstatus für „wartet auf Rückmeldung“; einen Status „Warten auf Kunde“ gibt es in Zammad nicht), die seit 7 Tagen nicht aktualisiert wurden, automatisch in den Status `closed` versetzt. Für den Labortest setzt du statt 7 Tagen eine kurze Frist (z. B. 10 Minuten) und die nächste Ausführungszeit des Schedulers, wartest ab und stellst danach auf 7 Tage zurück. Ist kein Zeitkriterium „seit letzter Aktualisierung“ verfügbar, wähle ein vorhandenes Zeitattribut des Tickets und halte fest, welches du genommen hast.
3. **Makro anlegen:** Lege zuerst die Gruppe `Trash` an und gib `Agent Müller` dort das Recht „Create“ (zum Verschieben von Tickets in die Gruppe nötig). Erstelle dann ein Makro "Spam aussortieren", das ein ausgewähltes Ticket dem aktuellen Agenten zuweist, den Status auf `closed` setzt und es in die Gruppe `Trash` verschiebt. Teste es als `Agent Müller` an einem Testticket.

#### Kontrollfragen
1. Was ist der wesentliche technische Unterschied zwischen einem Trigger und einem Scheduler?
2. In welchem Szenario ist ein Makro effizienter als eine manuelle Ticketbearbeitung?
3. Warum sollten Trigger, die automatische Antworten senden, Schleifen-Erkennungen (Loop-Prevention) besitzen?


### Modul 8: Reporting, Monitoring-Anbindung und Troubleshooting
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ticketsystem-Logfiles zur Fehlerdiagnose auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende eine Basis-API-Anbindung für Monitoring-Alarme konfigurieren.
* **Voraussetzungen:** Abgeschlossenes Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Auswertung von Reports und Dashboards | 2 |
| 8.2 | API-Tokens und Ticket-Erstellung per REST-API für externes Monitoring | 2 |
| 8.3 | System-Troubleshooting und Log-Analyse (`production.log`) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **API Token generieren:** Erstelle in den Profil-Einstellungen des Agenten ein persönliches Zugriffs-Token (API Token) mit Berechtigungen zum Erstellen von Tickets. Ist die Token-Anmeldung nicht möglich, ist sie laut Dokumentation auf manchen Systemen abgeschaltet und muss in den Zammad-Einstellungen aktiviert werden.
2. **API testen:** Sende vom Client-PC über die PowerShell (Cmdlet `Invoke-RestMethod`) oder `curl.exe` (in Windows PowerShell ist `curl` ein Alias für ein anderes Cmdlet) einen HTTP-POST-Request mit dem Token an die Zammad-API, um ein Ticket automatisiert zu erstellen (Simulation eines Monitoring-Alarms). Der Header lautet `Authorization: Token token=<TOKEN>`. Beispiel (nicht ausgeführt, Felder nicht gegen die Ticket-Endpunkt-Dokumentation geprüft):

   ```powershell
   $token = "<TOKEN>"
   $body = @{
     title    = "Monitoring: Festplatte voll auf srv01"
     group    = "1st-Level-Support"
     customer = "schmidt@example.internal"
     article  = @{ subject = "Disk-Alarm"; body = "Füllstand 91 %"; type = "note"; internal = $false }
   } | ConvertTo-Json -Depth 3
   Invoke-RestMethod -Method Post -Uri "http://zammad.example.internal/api/v1/tickets" `
     -Headers @{ Authorization = "Token token=$token" } -ContentType "application/json" -Body $body
   ```
3. **Log-Analyse:** Verbinde dich via SSH oder Konsole auf die Server-VM. Betrachte mittels `sudo tail -f /opt/zammad/log/production.log` die Logausgaben, während du im Webinterface das über die API erstellte Ticket öffnest und schließt. Identifiziere die entsprechenden HTTP-GET und POST-Einträge (im Rails-Log Zeilen mit `Started GET` bzw. `Started POST`).
4. **Report auswerten:** Öffne das Dashboard und, sofern dein Benutzer die Berechtigung hat, den Bereich für Berichte (Reporting; Menüführung nicht bestätigt). Ermittle die Anzahl der bisher erstellten Tickets je Gruppe und Status und vergleiche sie mit deinen Testtickets. Erkläre, welche Kennzahl für den Betrieb am wichtigsten ist.

#### Kontrollfragen
1. Welchen Sicherheitsvorteil bietet die Nutzung von API-Tokens gegenüber der Verwendung von regulären Benutzernamen und Passwörtern für externe Systeme?
2. Welcher Linux-Befehl eignet sich am besten, um eine Logdatei in Echtzeit zu überwachen, während man Aktionen im Webinterface durchführt?
3. Wo speichert Zammad auf Betriebssystemebene standardmäßig seine Applikationslogs ab?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (4+6+6+6+4+7+6+6 = 45 UE, jedes Modul entspricht der Summe seiner Einheiten), Prioritäten (6x P1, 2x P2) und die Zahl der Module blieben unverändert. Aufgaben und Fragen kamen hinzu; ob die Stunden dafür reichen (besonders Modul 2 und Modul 6), ist unerprobt. **Zammad selbst wurde nicht installiert:** Alle Schritte in der Zammad-Oberfläche wurden nur gegen die Dokumentation geprüft, nicht ausgeführt. Mailpit (Version 1.33.1) wurde im Sandkasten gestartet und getestet.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf | Zammad-Version 7.x ergänzt (nicht geprüft) | Version und Stand sollen genannt werden |
| A.1 | Hinweis: kein Pflichtmodul setzt ein Prio-2-Modul voraus | Die Regel stand nirgends; geprüft: Modul 6 und 8 verlangen nur Modul 2 und 3 |
| A.2 | Zammad-Quellen (Installation, Hardware, API, User Docs) ergänzt, „Stand: 2024“ durch Abrufdatum ersetzt; Mailpit-Version, Elasticsearch, Hyper-V, `.internal` ergänzt | Zammad-Docs mit „Stand 2024“ waren veraltet (aktuell Version 7.x); Installation, Hardware, Elasticsearch und Hyper-V hatten keine Quelle; „Stand nicht geprüft“ bei Mailpit |
| A.3 | VM-Ressourcen, Generation 2, Secure-Boot-Vorlage, TPM, Switch-Arten, Vorbereitung vor Modul 1, hosts-Pfad unter Windows, Benutzer `labadmin`, Zusatzsoftware und zwei Mailpit-Instanzen mit Port-Tabelle | Labor nannte weder RAM noch Plattenplatz (Zammad verlangt laut Dokumentation 2 Kerne und 6 GB, plus 4 GB mit Elasticsearch); die Installation der VMs fehlte; „Default Switch“ gibt es nur unter Windows Client; Mailpit-Download und Ports waren nicht beschrieben |
| Modul 1 | Voraussetzungen, Einheit 1.2, Aufgaben 1 bis 3, Frage 2 | „Voraussetzungen: Keine“ trotz erforderlicher VMs; der Webserver fehlte in der Architektur (Frage 2 nannte „drei“ Komponenten, Modul 2 braucht vier); Ubuntu konfiguriert eine nachträglich eingebaute zweite Schnittstelle nicht von selbst, daher wäre `apt update` gescheitert; die Windows-Firewall blockiert Ping zum Client |
| Modul 2 | Einheit 2.2, Aufgaben 1 bis 3 | „Mailpit über Paketquellen“ widersprach der Aufgabe (Mailpit ist keine Ubuntu-Paketquelle, sondern ein Download); Reihenfolge der Installation nach der Zammad-Seite; System-URL im Wizard; Rückbau ohne Netplan-Bereinigung und ohne Checkpoint |
| Modul 3 | Aufgaben 2 und 3, Frage 3 | Benutzer ohne E-Mail-Adresse und Passwort sind nicht anlegbar bzw. nicht anmeldbar; ob Kunden die Gruppe im Formular wählen können, ist nicht bestätigt (Ausweichweg ergänzt); Frage 3: laut Dokumentation entscheidet das Recht „Create“ in der Zielgruppe |
| Modul 4 | Aufgaben 1 bis 3 | „System > Kalender“ gibt es nicht, der Pfad lautet Manage > Calendars; das Lernziel „auf Gruppen anwenden“ wurde nur mit einer Prioritätsbedingung geübt; SLA-Zeiten zählen nur in Geschäftszeiten, der Test außerhalb ergäbe verwirrende Werte |
| Modul 5 | Aufgaben 1 bis 3, Frage 3 | Aktivierung unter Manage > Knowledge Base mit „Create Knowledge Base“; die öffentliche Wissensdatenbank liegt unter `/help` und braucht keine Anmeldung; der Artikel „Admin-Passwörter Router“ lud zum Ablegen von Passwörtern ein; `::pwd` ist kein Name, sondern Aufruf über das Keyword; das „Self-Service-Portal“ gibt es im Labor nicht; Frage 3 fragte nach einer Rolle, benötigt wird die Berechtigung `knowledge_base.editor` |
| Modul 6 | Lernziel 1, Voraussetzungen, Einheiten 6.1 und 6.2, Aufgaben 1 bis 3, Frage 4 | Mailpit hat keinen IMAP-Server; der POP3-Server ist standardmäßig aus und startet nur mit einer Passwortdatei, Aufgabe 3 wäre gescheitert; Modul 6 braucht Gruppen und Kunden aus Modul 3; Zammad würde seine eigenen ausgehenden Mails aus demselben Postfach zurückholen, daher zwei Instanzen |
| Modul 7 | Voraussetzungen, Aufgaben 1 bis 3 | Modul 7 braucht den Postausgang aus Modul 6; ein Trigger wird übersprungen, wenn die Gruppe keine E-Mail-Adresse hat; den Status „Warten auf Kunde“ gibt es nicht (Standardstatus: new, open, pending reminder, pending close, closed, merged, removed); die Gruppe `Trash` war nie angelegt; Standard-Trigger sendet bereits eine Eingangsbestätigung |
| Modul 8 | Einheit 8.2, Aufgaben 2 bis 4 | „Webhooks“ in 8.2 wurden nirgends geübt; Einheit 8.1 hatte keine Aufgabe und keine Frage; `curl` ist in Windows PowerShell ein Alias; `sudo` für das Log |

**Testergebnisse Mailpit 1.33.1 (Sandkasten, nicht Ubuntu in Hyper-V):**

* Ohne `--pop3-auth-file` ist Port 1110 geschlossen; mit Passwortdatei startet der POP3-Server und verlangt Benutzer und Passwort (falsches Passwort: `-ERR invalid password`).
* Zwei Instanzen (SMTP 1025/POP3 aus, SMTP 2025/POP3 1110) laufen parallel; eine Mail an Port 2025 (per `curl --url smtp://…` und per Send-API) erscheint im POP3-Postfach, eine Mail an Port 1025 nicht.
* Bei einer einzigen Instanz erscheinen ausgehende Mails in der POP3-Liste; das Löschen mit `DELE` entfernt sie auch in der Weboberfläche.
* Die Unit-Dateien bestehen `systemd-analyze verify` (mit Testpfad der Binary); gestartet wurden sie nicht.

**Bewertung des Prüfvermerks der ersten Fassung:** Das Format wurde eingehalten, die Bewertung ist trotzdem zu gut. Punkt 1 ist korrekt (45 UE, 6x P1, 2x P2). Punkt 2 ist nicht erfüllt (RAM und Platte, Betriebssysteminstallation, Generation 2 und Secure Boot, Netplan für die zweite Schnittstelle, Download-Quellen fehlten). Punkt 3 ist nicht erfüllt (der Prüfvermerk behauptet, RFC 1918 und die Zammad-Docs seien „im Text verankert“; im Modultext stehen keine Quellenverweise; „Stand 2024“ war veraltet; Installation, Elasticsearch, Hardware ohne Quelle). Punkt 4 ist teilweise erfüllt (die Rückbau-Aussage stimmt, aber Modul 6 braucht Modul 3, Modul 7 braucht Modul 6, die Gruppe `Trash` und den Status „Warten auf Kunde“ gab es nicht). Punkt 5 ist nicht erfüllt (der Prüfvermerk behauptet „Module 1 bis 8“, nannte aber nur Modul 6 als Stichprobe und bestätigte dort, Aufgabe 1 bis 3 führten die Mailpit-Konfiguration „exakt“ durch: der POP3-Server wäre nicht gestartet; das Lernziel nannte IMAP; „auf Gruppen anwenden“, Einheit 8.1 und 8.2 ohne Aufgabe). Punkt 6 ist teilweise erfüllt (der Ping-Test stimmt, aber kein Zustand zum Zurückkehren). Punkt 7 ist teilweise erfüllt (VMs genannt, ohne Ressourcen und Installation). Punkt 8 ist teilweise erfüllt (Mailpit-Download stimmt, aber Elasticsearch- und Zammad-Paketquelle, Mailpit-Quelle und Windows-hosts-Pfad fehlten). Punkt 9 ist teilweise erfüllt (die genannten Befehle sind harmlos, aber Passwörter im Wissensartikel und `curl`-Alias fehlten).

**Hinweise und offene Punkte:**

* **Bestätigt (Zammad-Dokumentation, abgerufen):** Ubuntu 24.04 wird für die Paketinstallation unterstützt; PostgreSQL ab 15; Elasticsearch ab 8.15 und unter 10 für Zammad ab 7.2 (für Zammad „optional, aber dringend empfohlen“); Hardwarerichtwerte (2 Kerne, 6 GB RAM, plus 4 GB mit Elasticsearch); Menüpfade Manage > Calendars, SLAs, Knowledge Base, Trigger, Scheduler, Text modules; Gruppenrechte Read, Create, Change, Overview, Full (Verschieben braucht Create in der Zielgruppe, Besitzer setzen braucht Full); Standardstatus und -prioritäten (low 1, normal 2, high 3); öffentliche Wissensdatenbank unter `/help`; Berechtigung `knowledge_base.editor`; Header `Authorization: Token token=…`.
* **Nicht bestätigt (Zammad nicht installiert):** Wizard-Schritte; der Dialog zum Anlegen von E-Mail-Kanälen, auch ob Zammad dabei eine Verifizierungsmail verlangt, die im Labor nicht zurückkommen würde (dann den Ablauf anpassen); ob Kunden Gruppe und Priorität im Formular wählen können; ob ein Benutzer zugleich Agent und Customer sein darf (Frage 2, Modul 3); ob der Scheduler ein Zeitkriterium „seit letzter Aktualisierung“ bietet; Menüführung für Berichte, Token-Verwaltung und die Token-Einstellung; die Felder der Ticket-API; was bei Antworten auf geschlossene Tickets geschieht (Frage 3, Modul 6); ob `ingest-attachment` bei der gewählten Elasticsearch-Version nötig ist (Elasticsearch-Installation nach der verlinkten Anleitung).
* **Nicht ausgeführt:** Hyper-V-Schritte, Netplan-Beispiel, Windows-Schritte, die systemd-Dienste unter Ubuntu und die PowerShell-Beispiele.
* **Mailpit-Passwort:** `Lab-Passwort-1` ist nur ein Laborwert und gehört in keine reale Umgebung.
