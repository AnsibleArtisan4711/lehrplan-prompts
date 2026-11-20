# Lehrplan: Schwachstellenmanagement

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 13 Module, 113 UE (zu 45 Minuten; 84,75 Stunden) |
| **Fokus-Technologien** | OpenVAS/Greenbone oder Nessus Essentials; Nmap; Windows und Linux als Scan-Ziele |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Härtung von Linux-Servern im Kurs „Linux-Server-Härtung“, von Windows-Servern im Kurs „Windows-Server-Härtung“, Grundbegriffe im Kurs „IT-Sicherheitsgrundlagen“, Zertifikate und TLS im Kurs „Kryptografie, Zertifikate und TLS“. Nicht behandelt: Penetrationstests mit Angriffswerkzeugen, Web-Anwendungs-Scans (DAST) über das Konzept hinaus, Container-Scanner, Cloud-Konfigurationsprüfung, Patch-Verteilung mit WSUS, Intune oder Configuration Manager im Detail |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Prozess und Grundbegriffe | 1 | 8 |
| 2 | Rechtliche und organisatorische Rahmenbedingungen | 1 | 8 |
| 3 | Labor und Entdeckung von Hosts und Diensten | 1 | 9 |
| 4 | Nmap-Skripte und Befunde nach Regeln | 1 | 9 |
| 5 | CVE und CVSS | 1 | 9 |
| 6 | Schwachstellenscanner: Greenbone/OpenVAS und Nessus Essentials | 1 | 10 |
| 7 | Authentifizierte Scans und Paketprüfung | 1 | 9 |
| 8 | Berichte erstellen und auswerten | 1 | 8 |
| 9 | Priorisierung nach Risiko | 1 | 9 |
| 10 | Beheben, Gegenmaßnahmen und Nachweis | 1 | 9 |
| 11 | Ausnahmen dokumentieren und Kennzahlen | 1 | 8 |
| 12 | Windows-Ziele und Besonderheiten | 2 | 7 |
| 13 | Abschlussrunde und Fehlersuche | 1 | 10 |
| **Gesamt** | 13 Module | 12 × Priorität 1, 1 × Priorität 2 | **113** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 12 (Windows-Ziele und Besonderheiten). Fällt Modul 12 weg, verringert sich der Gesamtumfang auf 106 UE; kein Pflichtmodul setzt Modul 12 voraus.

### 2. Quellen

**Gelesen (mit Abrufdatum 20.11.2026):** (1) Dokumentation „Greenbone Community Containers 22.4“ (greenbone.github.io/docs/latest/22.4/container): Betrieb mit Docker Compose, Feed-Version `24.10`, Standardkonto `admin`/`admin` (die Dokumentation nennt es unsicher), Mindestanforderung 2 CPU-Kerne, 4 GB RAM, 20 GB Speicher; die Anleitung ist laut Dokumentation zum Lernen und Testen gedacht, **nicht für den Produktivbetrieb**. (2) Seite „License Utilization“ der Tenable-Dokumentation zu Nessus 10.10: Nessus Essentials erlaubt 16 Hosts; ein Host zählt nach 90 Tagen ohne Scan nicht mehr; nur durch Host-Erkennung gefundene Hosts zählen nicht. Lizenzbedingungen und Funktionsumfang können sich ändern; vor dem Einsatz bei Tenable prüfen.

**Nicht gelesen:** das CVSS-3.1-Regelwerk (Spezifikation und Formeln) im Original; die Formeln im Skript `cvss_rechner.py` stammen aus Fachwissen und wurden mit sechs Vektoren geprüft (darunter zwei Beispielwerte aus dem Benutzerhandbuch des FIRST, soweit aus dem Gedächtnis bekannt, **nicht gegen das Dokument geprüft**). Der Wortlaut von **§ 118a StGB** (Österreich) und der entsprechenden Vorschriften anderer Staaten wurde nicht gelesen; die Rechtsaussagen in Modul 2 sind **nicht geprüft** und keine Rechtsberatung. Nmap, Greenbone und Nessus wurden nicht gegen ihre Handbücher gelesen; die Skripte wurden mit Nmap 7.94SVN im Container ausgeführt. Die Beispieldaten (Funde, Hinweise, Ausnahmen, Verläufe) sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Scan`, `10.15.0.0/24`).

**VMs:** `scan01` (**erforderlich**, `10.15.0.2`): Scanner-VM, Linux (Debian 12 oder Ubuntu 24.04) mit Nmap; für Modul 6 zusätzlich Greenbone Community Containers (Docker Compose; 2 vCPU, 4 GB RAM, 20 GB Speicher laut Dokumentation Mindestwert, besser 4 vCPU, 8 GB RAM) **oder** Nessus Essentials. `lx01` (**erforderlich**, `10.15.0.11`): Linux-Ziel, Debian 12 oder Ubuntu 24.04 mit `openssh-server` und einem Webserver. `win01` (**erforderlich ab Modul 7**, `10.15.0.12`): Windows-Server (Testversion) oder Windows 11 als Ziel mit einem lokalen Konto für authentifizierte Scans.

**Internetphase:** Für die Scanner-Einrichtung und die Schwachstellen-Feeds braucht `scan01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt und die Scans laufen im privaten Switch. Scans nur gegen die eigenen Lab-VMs.

**Prüfpunkt (Checkpoint):** Vor Modul 10 von `lx01` und `win01` je einen Prüfpunkt anlegen (Behebung rückgängig machen können).

**Skripte:** Die Beispielskripte liefen in einem Container mit zwei Netzwerk-Namespaces (`lab.sh`: Scanner `sc`, Ziel `lx`), nicht in Hyper-V und ohne Windows. Das Ziel wird dort zuerst absichtlich schwach konfiguriert und später gehärtet. **Nie gegen fremde Systeme richten.**

## B. Detaillierter Modulaufbau

### Modul 1: Prozess und Grundbegriffe

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Schwachstelle, Bedrohung und Risiko unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die vier Prozessschritte Erfassen, Bewerten, Beheben und Prüfen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Lebenszyklus eines Befunds mit erlaubten und verbotenen Übergängen darstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Rollen für Bewertung, Behebung und Prüfung benennen.
* **Voraussetzungen:** IT-Grundlagen; Netzwerk-Grundkenntnisse.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Begriffe: Schwachstelle, Bedrohung, Risiko, Exploit, Patch, Fehlkonfiguration | 2 |
| 1.2 | Der Prozess: Erfassen, Bewerten, Beheben, Prüfen und wieder von vorn | 2 |
| 1.3 | Lebenszyklus eines Befunds als Zustandsautomat (`lebenszyklus.py`) | 2 |
| 1.4 | Rollen und Verantwortung: wer entscheidet, wer behebt, wer prüft | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe abgrenzen (Einheit 1.1):** Beschreiben Sie anhand eines ungepatchten Webservers in je einem Satz Schwachstelle, Bedrohung, Exploit und Risiko.
2. **Prozess zeichnen (Einheit 1.2):** Zeichnen Sie den Kreislauf Erfassen, Bewerten, Beheben, Prüfen und tragen Sie bei jedem Schritt Eingabe und Ergebnis ein (z. B. Eingabe: Scan-Bericht; Ergebnis: priorisierte Liste).
3. **Zustandsautomaten ausführen (Einheit 1.3):** Führen Sie `python3 lebenszyklus.py` aus. Notieren Sie zwei erlaubte und zwei verbotene Übergänge und begründen Sie, warum der Sprung von „zugewiesen“ direkt auf „geschlossen“ verboten ist.
4. **Rollen festlegen (Einheit 1.4):** Legen Sie für ein kleines Unternehmen fest, wer Befunde bewertet, wer sie behebt und wer die Behebung prüft, und begründen Sie, warum Behebender und Prüfender nicht dieselbe Person sein sollten.

#### Kontrollfragen

1. Warum ist eine Schwachstelle allein noch kein Risiko?
2. Warum endet der Prozess nicht mit dem Beheben, sondern mit dem Prüfen?
3. Was ist der Unterschied zwischen einem falsch-positiven Befund und einer akzeptierten Ausnahme?
4. Warum ist ein einmaliger Scan nicht ausreichend?

### Modul 2: Rechtliche und organisatorische Rahmenbedingungen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende begründen, warum Scans nur mit schriftlicher Erlaubnis zulässig sind.
  * Nach Abschluss dieses Moduls kann der Lernende eine Scan-Freigabe mit allen nötigen Angaben formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende Ziele automatisch gegen eine Freigabe prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken eines Scans (Last, Datenschutz) benennen und abfedern.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Warum Scans eine Erlaubnis brauchen: Zustimmung des Eigentümers, Geltungsbereich, Haftung | 2 |
| 2.2 | Scan-Freigabe schriftlich: Ziele, Zeitraum, Ausschlüsse, Ansprechpartner, Werkzeuge | 2 |
| 2.3 | Praxis: Zielliste gegen eine Freigabe prüfen (`scan_freigabe.py`) | 2 |
| 2.4 | Datenschutz, Lastrisiko und Notfallkontakt beim Scannen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Freigabe entwerfen (Einheit 2.2):** Entwerfen Sie eine Scan-Freigabe für das Labornetz `10.15.0.0/24` mit Ziele, Zeitraum, Ausschlüssen, Ansprechpartner und erlaubten Werkzeugen. Schließen Sie den Router `10.15.0.1` aus.
2. **Zielliste prüfen (Einheit 2.3):** Führen Sie `python3 scan_freigabe.py freigabe.csv` aus. Erklären Sie für jede abgelehnte Adresse den Grund.
3. **Erweiterung (Einheit 2.3):** Ergänzen Sie in `scan_freigabe.py` eine Ablehnung für Adressen aus dem Bereich `169.254.0.0/16` und testen Sie sie.
4. **Risiken abwägen (Einheit 2.4):** Listen Sie je drei Risiken eines Scans für den laufenden Betrieb und für personenbezogene Daten (z. B. Anmeldeversuche, Absturz alter Geräte, Lesen von Dateinamen) mit je einer Gegenmaßnahme.
5. **Rechtslage klären (Einheit 2.1):** Formulieren Sie in drei Sätzen, was Sie vor dem ersten Scan einer fremden Umgebung klären müssen. Kennzeichnen Sie ausdrücklich, dass das keine Rechtsberatung ist.

#### Kontrollfragen

1. Warum genügt mündliche Zustimmung nicht?
2. Wozu dient eine Ausschlussliste in der Freigabe?
3. Warum sollte der Scan-Zeitraum begrenzt sein?
4. Wer sollte im Notfall erreichbar sein, wenn ein Scan ein System lahmlegt?

### Modul 3: Labor und Entdeckung von Hosts und Diensten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Labornetz mit Scanner und Zielen aufbauen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Hosts, Ports und Dienste mit Nmap entdecken.
  * Nach Abschluss dieses Moduls kann der Lernende die Ausgaben von Nmap in eine Bestandsliste überführen.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen offenem, geschlossenem und gefiltertem Port erklären.
* **Voraussetzungen:** Modul 1; Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Aufbau des Labors: privater Switch, Scanner, Linux-Ziel, Windows-Ziel; Adressplan | 2 |
| 3.2 | Hosts finden: Ping-Scan, ARP, Ausschlüsse (`nmap -sn`, `--exclude`) | 2 |
| 3.3 | Ports und Dienste: SYN-Scan, Dienst- und Versionserkennung (`nmap -sS`, `-sV`) | 3 |
| 3.4 | Bestandsliste aus dem Scan erstellen (`discovery.sh`, `nmap_nach_csv.py`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Labor aufbauen (Einheit 3.1):** Bauen Sie das Labor nach der Laborbeschreibung auf (privater Switch `Lab-Scan`, `scan01`, `lx01`, `win01`) und prüfen Sie mit `ping` die Verbindung vom Scanner zu beiden Zielen. Prüfen Sie, dass `scan01` im Scan-Zeitraum keine Verbindung zum Heimnetz hat.
2. **Hosts finden (Einheit 3.2):** Führen Sie einen Ping-Scan des Netzes aus und nehmen Sie den Scanner selbst mit `--exclude` aus. Notieren Sie, wie viele Hosts antworten.
3. **Ports und Dienste (Einheit 3.3):** Scannen Sie `lx01` mit `nmap -sS -p-` und danach die offenen Ports mit `-sV`. Notieren Sie je Port Dienst und Version und den Unterschied zwischen `open`, `closed` und `filtered`.
4. **Bestandsliste (Einheit 3.4):** Führen Sie `bash discovery.sh` aus (im Labor) oder erzeugen Sie die XML-Ausgabe mit `-oX` und wandeln Sie sie mit `nmap_nach_csv.py` in eine CSV-Datei um. Ergänzen Sie die Spalten Verantwortlicher und Kritikalität von Hand.

#### Kontrollfragen

1. Warum findet ein Ping-Scan nicht alle Hosts?
2. Was bedeutet der Port-Zustand „filtered“?
3. Warum liefert `-sV` genauere Aussagen als der Portname aus der Portnummer?
4. Warum gehört der Scanner selbst nicht in die Bestandsliste der Ziele?

### Modul 4: Nmap-Skripte und Befunde nach Regeln

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende NSE-Skripte gezielt auswählen und sicher einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende TLS-Protokolle, SSH-Anmeldearten und HTTP-Header mit Nmap prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Scan-Ausgaben nach festen Regeln in Befunde überführen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen einer Regelprüfung gegenüber einem Schwachstellenscanner nennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Die Nmap-Skript-Engine (NSE): Kategorien, Auswahl, sicherer Einsatz | 2 |
| 4.2 | TLS, SSH, HTTP und Banner prüfen (`ssl-enum-ciphers`, `ssh-auth-methods`, `http-headers`, `banner`) | 3 |
| 4.3 | Befunde nach Regeln auswerten (`nmap_skripte.sh`, `nmap_befunde.py`) | 2 |
| 4.4 | Grenzen der Skript-Prüfung: Falsch-positive und Falsch-negative | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Skripte auswählen (Einheit 4.1):** Listen Sie mit `nmap --script-help` oder `ls /usr/share/nmap/scripts` die Skripte der Kategorien `safe` und `default` auf und wählen Sie fünf für das Labor aus. Begründen Sie, warum Sie Skripte der Kategorie `intrusive` zunächst weglassen.
2. **TLS und SSH prüfen (Einheit 4.2):** Prüfen Sie `lx01` mit `ssl-enum-ciphers` und `ssh-auth-methods`. Notieren Sie angebotene Protokolle, die schwächste Chiffre und die erlaubten Anmeldearten.
3. **Regeln anwenden (Einheit 4.3):** Führen Sie `bash nmap_skripte.sh` aus. Ordnen Sie jeden der sechs Befunde in `beispiele/nmap_skripte.ausgabe.txt` einer Regel R1 bis R6 aus `nmap_befunde.py` zu.
4. **Regel ergänzen (Einheit 4.3):** Ergänzen Sie in `nmap_befunde.py` eine Regel R7 „SSH-Server meldet Versionsbanner mit Produktname“ und testen Sie sie. Beschreiben Sie, wann sie falsch-positiv wäre.
5. **Grenzen benennen (Einheit 4.4):** Nennen Sie drei Dinge, die ein Schwachstellenscanner findet und die Ihre sechs Regeln nicht finden (z. B. fehlende Patches, schwache Passwörter).

#### Kontrollfragen

1. Was kennzeichnet NSE-Skripte der Kategorie `intrusive`?
2. Warum ist „TLS 1.0 angeboten“ ein Befund, auch wenn TLS 1.3 ebenfalls angeboten wird?
3. Warum ist die Regelprüfung kein Ersatz für einen Schwachstellenscanner?
4. Wie entsteht ein falsch-negativer Befund?

### Modul 5: CVE und CVSS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer CVE-Kennung erklären und Einträge in Schwachstellenlisten finden.
  * Nach Abschluss dieses Moduls kann der Lernende einen CVSS-3.1-Vektor lesen und den Basiswert berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Aussagegrenzen des Basiswerts benennen.
  * Nach Abschluss dieses Moduls kann der Lernende EPSS und die KEV-Liste als Zusatzinformation einordnen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | CVE-Kennungen, Schwachstellenlisten, Hersteller-Hinweise (Advisories) | 2 |
| 5.2 | CVSS v3.1: Basismetriken (Angriffsvektor, Komplexität, Rechte, Interaktion, Auswirkung) | 3 |
| 5.3 | Praxis: Basiswert berechnen (`cvss_rechner.py`, `cvss_demo.sh`) | 2 |
| 5.4 | Grenzen von CVSS: Basiswert ist kein Risiko; Zeit- und Umgebungsmetriken, EPSS, KEV | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **CVE lesen (Einheit 5.1):** Nehmen Sie eine CVE-Kennung Ihrer Wahl aus einem Hersteller-Hinweis oder aus der Nationalen Schwachstellendatenbank und halten Sie fest: Kennung, betroffene Produkte und Versionen, Basiswert, Vektor, behobene Version.
2. **Vektor entschlüsseln (Einheit 5.2):** Entschlüsseln Sie den Vektor `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` in Worten und sagen Sie, warum der Basiswert so hoch ausfällt.
3. **Basiswert rechnen (Einheit 5.3):** Führen Sie `python3 cvss_rechner.py --selbsttest` und `bash cvss_demo.sh` aus. Berechnen Sie danach den Basiswert für zwei eigene Vektoren (einen lokalen, einen aus dem Netz erreichbaren) und erklären Sie den Unterschied.
4. **Grenzen erklären (Einheit 5.4):** Erklären Sie an einem Beispiel, warum ein Befund mit Basiswert 9,8 auf einem isolierten Testsystem weniger dringend sein kann als einer mit 6,5 auf einem Webserver im Internet.

#### Kontrollfragen

1. Wofür steht die Kennung CVE-JJJJ-NNNN?
2. Welche Metriken gehören zum Basiswert?
3. Warum kann der Basiswert desselben CVE bei zwei Organisationen verschieden relevant sein?
4. Was sagt der EPSS-Wert aus, was die KEV-Liste?

### Modul 6: Schwachstellenscanner: Greenbone/OpenVAS und Nessus Essentials

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines Schwachstellenscanners beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Greenbone oder Nessus Essentials im Labor einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Ziele, Scan-Konfigurationen und Zeitpläne anlegen und Lastgrenzen setzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Bericht lesen und Falsch-positive erkennen.
* **Voraussetzungen:** Module 1 bis 5; Docker-Grundkenntnisse (Container starten) oder Bereitschaft, sie zu erwerben.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Aufbau eines Scanners: Scan-Engine, Prüfungen (Feed), Manager, Weboberfläche, Datenbank | 2 |
| 6.2 | Greenbone Community Containers einrichten (Docker Compose), Feed laden, Konto und Passwort ändern | 3 |
| 6.3 | Scan-Konfigurationen, Ziele, Zeitpläne und Lastgrenzen; Nessus Essentials als Alternative (16 Hosts) | 3 |
| 6.4 | Erste Scans auswerten und Falsch-positive erkennen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Komponenten benennen (Einheit 6.1):** Zeichnen Sie die Komponenten von Greenbone Community Containers (Scan-Dienst, Manager, Datenbank, Weboberfläche, Feed) und beschreiben Sie je einen Satz Aufgabe.
2. **Greenbone einrichten (Einheit 6.2):** Richten Sie Greenbone Community Containers auf `scan01` nach der Dokumentation ein (Internetphase). Ändern Sie sofort das Standardpasswort. Warten Sie, bis der Feed vollständig geladen ist, und dokumentieren Sie Versionen und Dauer.
3. **Ziel und Scan anlegen (Einheit 6.3):** Legen Sie ein Ziel `lx01` mit Zugangsdaten an (zunächst ohne), wählen Sie eine Scan-Konfiguration, begrenzen Sie die gleichzeitigen Prüfungen und starten Sie den Scan. Notieren Sie Dauer und Ergebnis. Alternativ: dasselbe mit Nessus Essentials.
4. **Bericht prüfen (Einheit 6.4):** Wählen Sie fünf Befunde aus dem Bericht und prüfen Sie jeden von Hand (z. B. mit Nmap oder dem Dienst selbst). Vermerken Sie, welche falsch-positiv sind und warum.

#### Kontrollfragen

1. Warum ist der Feed-Stand für die Qualität eines Scans entscheidend?
2. Warum muss das Standardpasswort nach der Einrichtung sofort geändert werden?
3. Wozu dienen Lastgrenzen (Zahl gleichzeitiger Prüfungen und Hosts)?
4. Welche Einschränkung hat Nessus Essentials?

### Modul 7: Authentifizierte Scans und Paketprüfung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen authentifizierten und unauthentifizierten Scans erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Scan-Konto mit minimalen Rechten einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende installierte Paketversionen gegen Hersteller-Hinweise prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Ursachen einer fehlgeschlagenen Scan-Anmeldung eingrenzen.
* **Voraussetzungen:** Modul 5; Modul 6 (für den Einsatz im Scanner).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Unauthentifiziert und authentifiziert: was jeweils sichtbar ist | 2 |
| 7.2 | Zugangsdaten für Scans: eigene Konten mit geringsten Rechten, Schlüssel, Aufbewahrung | 2 |
| 7.3 | Praxis: installierte Pakete gegen Hinweise prüfen (`paketpruefung.py`, `paketpruefung.sh`) | 3 |
| 7.4 | Linux und Windows: SSH und WinRM/SMB als Zugang; Fehlerbilder bei fehlgeschlagener Anmeldung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Sichtbarkeit vergleichen (Einheit 7.1):** Vergleichen Sie in einer Tabelle, welche Befundarten ein Scan ohne und mit Anmeldung findet (fehlende Patches, Konfiguration, installierte Software, Dienste von außen).
2. **Scan-Konto anlegen (Einheit 7.2):** Legen Sie auf `lx01` ein Konto `scan` ohne Anmeldung per Passwort an (Schlüssel), das nur lesen darf. Legen Sie auf `win01` ein lokales Konto mit den nötigen Rechten an und notieren Sie, welche Rechte Sie bewusst nicht vergeben.
3. **Pakete prüfen (Einheit 7.3):** Führen Sie `bash paketpruefung.sh` aus. Erklären Sie, wie `dpkg --compare-versions` die Ergebnisse „verwundbar“, „behoben“ und „nicht installiert“ bestimmt, und warum die Hinweise in `beispiel_hinweise.csv` frei erfunden sind.
4. **Anmeldefehler suchen (Einheit 7.4):** Beschreiben Sie je drei mögliche Ursachen, wenn der authentifizierte Scan auf Linux (SSH) und auf Windows (SMB/WinRM) meldet „Anmeldung fehlgeschlagen“, und wie Sie jede prüfen.

#### Kontrollfragen

1. Warum findet ein authentifizierter Scan mehr fehlende Patches?
2. Warum soll das Scan-Konto kein Administrator-Konto sein, wenn es sich vermeiden lässt?
3. Warum genügt ein Vergleich von Versionstexten als Zeichenketten nicht?
4. Wo werden die Zugangsdaten des Scan-Kontos im Scanner aufbewahrt, und wer darf sie lesen?

### Modul 8: Berichte erstellen und auswerten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Schwachstellenbericht aufbauen und an die Zielgruppe anpassen.
  * Nach Abschluss dieses Moduls kann der Lernende Berichtsdaten mit einem Skript nach Schwere und Host zusammenfassen.
  * Nach Abschluss dieses Moduls kann der Lernende unsichere und unplausible Befunde erkennen und kennzeichnen.
  * Nach Abschluss dieses Moduls kann der Lernende den Umgang mit Berichten (Vertraulichkeit) festlegen.
* **Voraussetzungen:** Modul 4; Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Aufbau eines Schwachstellenberichts: Zusammenfassung, Methode, Befunde, Maßnahmen | 2 |
| 8.2 | Zielgruppen: Technik, Management; Kennzahlen und Darstellung | 2 |
| 8.3 | Praxis: Bericht (CSV) auswerten (`bericht_auswerten.py`) | 2 |
| 8.4 | Unsichere Befunde kennzeichnen, Plausibilität prüfen, Berichte schützen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Gliederung entwerfen (Einheit 8.1):** Entwerfen Sie die Gliederung eines Berichts für die Geschäftsführung (eine Seite) und für die Technik (Details je Befund).
2. **Management-Zusammenfassung (Einheit 8.2):** Schreiben Sie auf Grundlage der Auswertung eine Zusammenfassung von fünf Sätzen ohne Fachbegriffe: Lage, wichtigste drei Maßnahmen, Frist.
3. **Bericht auswerten (Einheit 8.3):** Führen Sie `python3 bericht_auswerten.py beispiel_bericht.csv` aus. Notieren Sie Anzahl je Schwere, Befunde je Host und die gekennzeichneten unsicheren Befunde.
4. **Plausibilität prüfen (Einheit 8.4):** Erklären Sie, warum ein Befund mit CVSS 0,0 und Schwere „hoch“ auffällt, und beschreiben Sie, wie Sie ihn klären.

#### Kontrollfragen

1. Wozu braucht ein Bericht eine Beschreibung der Methode und des Scan-Zeitpunkts?
2. Warum genügt für die Geschäftsführung nicht die Liste aller Befunde?
3. Was bedeutet „unsicher“ bei einem Befund?
4. Warum ist ein Bericht vertraulich zu behandeln?

### Modul 9: Priorisierung nach Risiko

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende begründen, warum Priorisierung den Kontext berücksichtigen muss.
  * Nach Abschluss dieses Moduls kann der Lernende einen eigenen, nachvollziehbaren Risikowert festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Prioritätsklassen mit Fristen zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Wartungsfenster und Ausnahmen in die Planung einbeziehen.
* **Voraussetzungen:** Modul 5; Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Warum nach Basiswert allein sortieren zu kurz greift | 2 |
| 9.2 | Kontext: Kritikalität des Systems, Exposition, bekannte Ausnutzung (KEV), EPSS | 2 |
| 9.3 | Praxis: Risikowert berechnen und Fristen zuordnen (`priorisieren.py`) | 3 |
| 9.4 | Prioritätsklassen und Fristen (SLA), Wartungsfenster | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Basiswert-Rangfolge (Einheit 9.1):** Sortieren Sie die Befunde in `befunde.csv` nur nach CVSS-Basiswert und notieren Sie die Rangfolge.
2. **Kontext sammeln (Einheit 9.2):** Pflegen Sie `assets.csv` für Ihr Labor (Kritikalität 1 bis 5, Exposition intern/dmz/internet) und begründen Sie jeden Wert in einem Satz.
3. **Risikowert berechnen (Einheit 9.3):** Führen Sie `python3 priorisieren.py` aus und vergleichen Sie die Rangfolge mit Aufgabe 1. Erklären Sie die zwei größten Unterschiede.
4. **Gewichte ändern (Einheit 9.3):** Ändern Sie in `priorisieren.py` einen Gewichtungsfaktor (z. B. den Aufschlag für KEV) und beschreiben Sie, wie sich Prioritäten verschieben. Begründen Sie Ihre endgültige Wahl.
5. **Fristen festlegen (Einheit 9.4):** Legen Sie für die Klassen P1 bis P4 Fristen fest (Standard: 7, 30, 90 Tage, Wartungsfenster) und beschreiben Sie, wer eine Verlängerung genehmigt.

#### Kontrollfragen

1. Warum steht ein Befund auf einem Testsystem trotz hohem Basiswert niedriger als ein mittlerer auf dem Webserver in der DMZ?
2. Warum sind die Gewichte in `priorisieren.py` keine Norm?
3. Was ist ein Wartungsfenster, und wie beeinflusst es Fristen?
4. Wer sollte Prioritäten nachträglich ändern dürfen?

### Modul 10: Beheben, Gegenmaßnahmen und Nachweis

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende für einen Befund die passende Maßnahmenart wählen.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungen mit Prüfpunkt und Rückweg durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende die Behebung durch einen Nachscan belegen.
  * Nach Abschluss dieses Moduls kann der Lernende unvollständige Behebung im Vergleich erkennen.
* **Voraussetzungen:** Modul 4; Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Maßnahmenarten: Patch, Konfiguration, Abschalten, Absichern (Filter), Ersatz | 2 |
| 10.2 | Änderungen sicher durchführen: Prüfpunkt, Reihenfolge, Rückweg, Wartungsfenster | 2 |
| 10.3 | Praxis: Scan vorher, Maßnahme, Scan nachher, Vergleich (`behebung_nachweis.sh`, `scan_vergleich.py`) | 3 |
| 10.4 | Teilweise Behebung erkennen und Befunde wieder öffnen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Maßnahmen zuordnen (Einheit 10.1):** Ordnen Sie den sechs Befunden aus Modul 4 je eine Maßnahmenart zu (Patch, Konfiguration, Abschalten, Filter, Ersatz) und begründen Sie die Wahl.
2. **Änderungsplan schreiben (Einheit 10.2):** Schreiben Sie einen Plan für die Behebung auf `lx01` und `win01` mit Reihenfolge, Prüfpunkt (Checkpoint), Rückweg und Zeitfenster.
3. **Nachweis führen (Einheit 10.3):** Führen Sie `bash behebung_nachweis.sh` aus. Erklären Sie anhand der Ausgabe, wie `scan_vergleich.py` zwischen behoben, neu und unverändert unterscheidet und was der Rückgabewert bedeutet.
4. **Gegenprobe auswerten (Einheit 10.4):** Betrachten Sie die Gegenprobe (nur TLS gehärtet). Nennen Sie die drei offenen Befunde und die Maßnahme zu jedem.

#### Kontrollfragen

1. Warum ist „Abschalten“ oft besser als „Patchen“?
2. Wozu dient der Prüfpunkt vor der Änderung?
3. Was bedeutet ein „neuer“ Befund im Vergleich nach einer Behebung?
4. Warum muss die Prüfung mit demselben Scan-Profil wie die erste Messung erfolgen?

### Modul 11: Ausnahmen dokumentieren und Kennzahlen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Ausnahme vollständig und befristet dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende ein Ausnahmeregister auf fehlende Angaben und Fristen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Kennzahlen zur Schwachstellenbehebung berechnen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Kennzahlen für die Berichterstattung auswählen.
* **Voraussetzungen:** Modul 9; Modul 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Wann eine Ausnahme zulässig ist: Begründung, Ausgleichsmaßnahme, Befristung, Freigabe | 2 |
| 11.2 | Ausnahmeregister führen und prüfen (`ausnahmen_pruefen.py`) | 2 |
| 11.3 | Kennzahlen: Behebungsdauer (MTTR), Fristeinhaltung, offene und überfällige Befunde (`kennzahlen.py`) | 2 |
| 11.4 | Berichten an die Leitung und kontinuierliche Verbesserung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ausnahme formulieren (Einheit 11.1):** Formulieren Sie eine Ausnahme für ein Altsystem (veraltetes TLS, Hersteller liefert kein Update) mit Begründung, Ausgleichsmaßnahme, Verantwortlichem, Gültigkeit und Freigabe.
2. **Register prüfen (Einheit 11.2):** Führen Sie `python3 ausnahmen_pruefen.py ausnahmen.csv` aus. Nennen Sie je Eintrag das Problem (abgelaufen, bald ablaufend, Pflichtfelder leer) und was zu tun ist.
3. **Kennzahlen berechnen (Einheit 11.3):** Führen Sie `python3 kennzahlen.py befunde_verlauf.csv` aus. Deuten Sie MTTR je Priorität und Fristeinhaltung und nennen Sie zwei mögliche Ursachen für Überschreitungen.
4. **Kennzahlen auswählen (Einheit 11.4):** Wählen Sie drei Kennzahlen für einen monatlichen Bericht an die Leitung und begründen Sie die Auswahl; nennen Sie eine Kennzahl, die irreführen kann.

#### Kontrollfragen

1. Warum muss jede Ausnahme befristet sein?
2. Wer sollte eine Ausnahme genehmigen, und warum nicht der Verursachende?
3. Was bedeutet MTTR, und was sagt sie nicht aus?
4. Warum ist die reine Anzahl offener Befunde als Kennzahl allein irreführend?

### Modul 12: Windows-Ziele und Besonderheiten

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische Windows-Ports und ihre Bedeutung nennen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum der Portname aus der Portnummer nur eine Vermutung ist.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen für authentifizierte Windows-Scans beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende typische Windows-Befunde mit Gegenmaßnahmen verknüpfen.
* **Voraussetzungen:** Modul 3; Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Typische Windows-Ports und -Dienste: RPC, NetBIOS, SMB, RDP, WinRM | 2 |
| 12.2 | Port-Namen sind Vermutungen: Diensterkennung statt Raten (`windows_ports.sh`) | 2 |
| 12.3 | Authentifizierte Windows-Scans: Rechte, Remote-UAC, Firewall, Updatestand | 2 |
| 12.4 | Typische Windows-Befunde und Gegenmaßnahmen: SMB, RDP, Updates | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ports zuordnen (Einheit 12.1):** Ordnen Sie die Ports 135, 139, 445, 3389 und 5985 je einem Dienst zu und beschreiben Sie, welche nicht aus dem Internet erreichbar sein sollten.
2. **Namen und Wirklichkeit (Einheit 12.2):** Führen Sie `bash windows_ports.sh` aus (Platzhalter-Dienste, kein Windows). Erklären Sie den Unterschied zwischen Schritt 1 (ohne Diensterkennung) und Schritt 2 (mit `-sV`).
3. **Scan-Voraussetzungen (Einheit 12.3):** Listen Sie fünf Voraussetzungen auf, damit ein authentifizierter Scan auf `win01` gelingt (Konto, Firewall-Regel, Dienste, Rechte, Remote-UAC).
4. **Befunde zuordnen (Einheit 12.4):** Ordnen Sie drei typischen Windows-Befunden (SMBv1 aktiv, RDP ohne Netzwerkebenen-Authentifizierung, fehlende Updates) je eine Maßnahme zu.

#### Kontrollfragen

1. Warum kann Port 3389 trotz Namen „ms-wbt-server“ etwas anderes anbieten?
2. Warum soll SMB nicht aus dem Internet erreichbar sein?
3. Was bewirkt die Remote-UAC bei lokalen Konten?
4. Welche Rolle spielt der Updatestand bei Windows-Befunden?

### Modul 13: Abschlussrunde und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine vollständige Schwachstellenmanagement-Runde im Labor durchführen und dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler bei Scans eingrenzen und beheben.
  * Nach Abschluss dieses Moduls kann der Lernende Diagnosewerkzeuge gezielt einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Abschlussbericht mit Befunden, Maßnahmen und Restrisiken schreiben.
* **Voraussetzungen:** Module 1 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Eine vollständige Runde: Freigabe, Scan, Bewertung, Behebung, Nachscan (`abschluss_runde.sh`) | 3 |
| 13.2 | Fehlersuche bei Scans: Zeitüberschreitung, gefilterte Ports, Last, Feed, Anmeldung | 3 |
| 13.3 | Diagnosewerkzeuge: `ping`, `traceroute`, `ss`, `tcpdump`, Scanner-Protokolle | 2 |
| 13.4 | Abschlussbericht und Selbstprüfung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Runde durchführen (Einheit 13.1):** Führen Sie die Runde auf `scan01` gegen `lx01` durch (oder `bash abschluss_runde.sh` im Labor): Freigabe prüfen, scannen, priorisieren, beheben, nachscannen, vergleichen. Dokumentieren Sie jeden Schritt mit Zeitpunkt.
2. **Fehler suchen (Einheit 13.2):** Der Scan von `win01` liefert „alle Ports gefiltert“. Beschreiben Sie in Schritten, wie Sie die Ursache eingrenzen (Erreichbarkeit, Firewall, Adresse, Scan-Profil, Last).
3. **Diagnose üben (Einheit 13.3):** Prüfen Sie mit `ss -ltn` auf `lx01`, welche Dienste lauschen, und vergleichen Sie das mit den Ergebnissen von Nmap von `scan01`. Erklären Sie jede Abweichung.
4. **Abschlussbericht schreiben (Einheit 13.4):** Schreiben Sie einen Abschlussbericht von höchstens zwei Seiten: Umfang, Methode, Befunde (vorher/nachher), Maßnahmen, Ausnahmen, Restrisiko, Empfehlung für die nächste Runde.

#### Kontrollfragen

1. Warum wird vor der Behebung ein Ausgangsstand gesichert?
2. Wie unterscheiden Sie „Ziel nicht erreichbar“ von „Ports gefiltert“?
3. Welche Abweichungen zwischen `ss` auf dem Ziel und Nmap von außen sind erwartbar?
4. Was gehört in den Abschnitt „Restrisiko“?
