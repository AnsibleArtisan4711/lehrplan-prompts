# Lehrplan: Reverse Proxy, Lastverteilung und TLS

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Shell, Pakete installieren, Dienste starten); HTTP-Grundlagen sind hilfreich |
| **Gesamtumfang** | 13 Module, 110 UE (zu 45 Minuten; 82,5 Stunden) |
| **Fokus-Technologien** | nginx, HAProxy, Debian/Ubuntu Linux, TLS |
| **Thematische Abgrenzung (Out of Scope)** | Der vorhandene Kurs „Webserver“ behandelt Apache und nginx als Webserver; hier Fokus auf Proxy, Lastverteilung und TLS. Zertifikate ausschließlich mit einer internen CA und einem lokalen ACME-Testserver (Pebble), keine öffentlichen Zertifizierungsstellen und keine echten Domänen. Nicht behandelt: Web Application Firewalls, Service Mesh, Kubernetes-Ingress, CDN, HTTP/3 (QUIC), Hochverfügbarkeit des Proxys selbst (keepalived) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Reverse-Proxy-Konzept und Laborumgebung | 1 | 7 |
| 2 | nginx als Reverse Proxy | 1 | 9 |
| 3 | HAProxy als Reverse Proxy | 1 | 9 |
| 4 | TLS-Grundlagen und eine interne CA mit openssl | 1 | 9 |
| 5 | TLS-Terminierung mit nginx | 1 | 9 |
| 6 | TLS-Terminierung mit HAProxy und TLS-Durchleitung | 1 | 8 |
| 7 | Let’s Encrypt und ACME mit einem lokalen Testserver (Pebble) | 1 | 9 |
| 8 | Lastverteilung mit nginx | 1 | 9 |
| 9 | Lastverteilung und Health Checks mit HAProxy | 1 | 9 |
| 10 | Header, HSTS und das PROXY-Protokoll | 1 | 8 |
| 11 | WebSocket hinter dem Proxy | 2 | 7 |
| 12 | Caching im Reverse Proxy | 2 | 8 |
| 13 | Sicherheit, Fehlersuche und Abschlussprojekt | 1 | 9 |
| **Gesamt** | 13 Module | 11 × Priorität 1, 2 × Priorität 2 | **110** |

**Priorität 1** (Pflicht) sind die Module 1 bis 10 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) sind Modul 11 (WebSocket) und Modul 12 (Caching). Fallen beide weg, verringert sich der Gesamtumfang auf 95 UE.

### 2. Quellen

**Keine Quelle wurde gegen das Original gelesen.** Alle Befehle und Ausgaben stammen aus Läufen im Labor-Container (Ubuntu 24.04: nginx 1.24.0, HAProxy 2.8.30, OpenSSL 3.0.13, curl 8.5.0; Pebble v2.6.0, aus dem Quelltext mit Go 1.24.7 gebaut; certbot 5.10.0 mit Python 3.12) und aus Fachwissen. Die Dokumentation von nginx, HAProxy, Pebble, certbot und den Protokollen (HTTP, TLS, ACME, PROXY-Protokoll, WebSocket) ist **nicht** gelesen; wo eine Aussage über das Beobachtete hinausgeht, ist sie in der Übung mit „nicht bestätigt“ gekennzeichnet. Das Verhalten der Debian-12-Pakete (nginx 1.22, HAProxy 2.6) ist nicht geprüft; bekannte Unterschiede (z. B. `http2 on;` erst ab nginx 1.25.1) stehen in den Hinweisen.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switches:** zwei private Switches ohne Verbindung zum Heimnetz: `Lab-Front-Net` (`10.1.1.0/24`, Client und Proxy) und `Lab-Back-Net` (`10.1.2.0/24`, Proxy und Backends); der Proxy leitet **nicht** zwischen den Netzen (kein `ip_forward`).

**VMs:** `px01` (Proxy, Debian 12, 1 GB RAM, zwei Netzwerkkarten `10.1.1.1` und `10.1.2.1`; Pakete `nginx`, `haproxy`, `openssl`, `socat`, `curl`, `libnginx-mod-stream`; ab Modul 7 zusätzlich Pebble und certbot), `web01` (`10.1.2.11`) und `web02` (`10.1.2.12`) (Debian 12, je ein kleiner Webdienst auf Port 8080; im Kurs das mitgelieferte `backend.py` mit Python 3) und `cl01` (`10.1.1.2`, Standard-Gateway `10.1.1.1`, `curl`, `openssl`). Alle Adressen statisch, kein DHCP und kein DNS; die Namen `shop.lab.test` und `api.lab.test` stehen in `/etc/hosts` von `cl01` und `px01` und zeigen auf `10.1.1.1`.

**Pakete und Programme** werden einmalig vor Kursbeginn mit Internetzugang (temporär eine zusätzliche NAT-Karte) installiert und die Karte danach entfernt. Pebble und certbot sind **nicht** in den Debian-Paketquellen enthalten: Pebble wird aus dem Quelltext gebaut (`go build ./cmd/pebble`, Quelltext von GitHub) oder als fertiges Programm bereitgestellt; certbot lässt sich in einer Python-Umgebung per `pip` installieren. Die Beschaffung in der VM ist nicht geprüft.

**Prüfpunkte:** Vor Änderungen am Proxy einen Hyper-V-Prüfpunkt von `px01` anlegen.

**Skripte:** Die Beispielskripte bauen dieses Labor als vier Netzwerk-Namespaces auf einer einzelnen Linux-Maschine nach (Schreibweise `on px …` = „im Namespace des Proxys ausführen“). In den VMs entfallen das Präfix und die Hilfsfunktionen; die Konfigurationsdateien und Befehle sind dieselben.

## B. Detaillierter Modulaufbau

### Modul 1: Reverse-Proxy-Konzept und Laborumgebung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Reverse Proxy, Forward Proxy und Load Balancer unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende den Weg einer Anfrage über zwei getrennte TCP-Verbindungen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor aufbauen und die Isolation der Backends nachweisen.
* **Voraussetzungen:** Grundkenntnisse in IP-Netzen, HTTP und der Linux-Shell.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Forward Proxy, Reverse Proxy, Load Balancer, Gateway: Begriffe und Aufgaben; Schichten 4 und 7 | 2 |
| 1.2 | Warum ein Proxy? Entkopplung, TLS an einer Stelle, Verteilung, Schutz, Caching; Kosten und Risiken | 2 |
| 1.3 | Laborumgebung aufbauen und prüfen: zwei Netze, kein Routing zwischen Client und Backends | 1 |
| 1.4 | Praxis: minimalen nginx-Proxy starten und die zwei Verbindungen beobachten (`proxy_konzept.sh`) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Labor aufbauen (Einheit 1.3):** Richten Sie `px01`, `web01`, `web02` und `cl01` nach der Laborbeschreibung ein. Weisen Sie nach, dass `cl01` die Backends direkt nicht erreicht (Ping, `curl`), den Proxy aber schon.
2. **Minimaler Proxy (Einheit 1.4):** Starten Sie nginx mit `minimal.conf` (oder führen Sie `bash proxy_konzept.sh` aus) und rufen Sie den Proxy vom Client aus auf. Was meldet das Backend als Client-Adresse?
3. **Zwei Verbindungen (Einheit 1.4):** Zeigen Sie mit `ss -tn` auf dem Proxy während einer langsamen Anfrage die zwei TCP-Verbindungen und ordnen Sie sie Client und Backend zu.
4. **Begriffe abgrenzen (Einheit 1.1):** Stellen Sie in einer Tabelle Forward Proxy, Reverse Proxy und Load Balancer nach Standort, Auftraggeber und typischer Aufgabe gegenüber.
5. **Nutzen und Risiko (Einheit 1.2):** Nennen Sie drei Vorteile und zwei Risiken eines Reverse Proxys (z. B. Single Point of Failure, Verlust der Client-Adresse).

#### Kontrollfragen

1. Wo steht ein Reverse Proxy im Vergleich zu einem Forward Proxy, und wem dient er?
2. Warum sieht das Backend die Adresse des Proxys und nicht die des Clients?
3. Was ist der Unterschied zwischen einem Proxy auf Schicht 7 und einem auf Schicht 4?
4. Welche Risiken entstehen durch einen zentralen Proxy?

### Modul 2: nginx als Reverse Proxy

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen nginx-Reverse-Proxy mit mehreren Backends und Namen konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Header so setzen, dass das Backend Host, Client-Adresse und Protokoll kennt.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationsfehler mit `nginx -t` finden.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | `proxy_pass`, `location`, virtuelle Server (`server_name`), Upstream-Blöcke | 3 |
| 2.2 | Header richtig setzen: `Host`, `X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto`; Pfadumschreibung mit und ohne Schrägstrich | 2 |
| 2.3 | Zeitlimits und Fehlerbilder: `proxy_connect_timeout`, `proxy_read_timeout`, 502 und 504 | 1 |
| 2.4 | Praxis: `nginx_proxy.sh` ausführen, Konfiguration mit `nginx -t` prüfen, Ergebnisse deuten | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration prüfen (Einheit 2.4):** Prüfen Sie `proxy_defekt.conf` mit `nginx -t` und nennen Sie die Fehlermeldung. Beheben Sie den Fehler.
2. **Header (Einheit 2.2):** Vergleichen Sie die Ausgabe des Backends bei `location = /roh` (ohne Header) und `location /` (mit Header). Welche Header fehlen im ersten Fall?
3. **Pfad (Einheit 2.2):** Rufen Sie `/api/info` und `/voll/info` auf und erklären Sie den Unterschied zwischen `proxy_pass http://b2/;` und `proxy_pass http://b2;`.
4. **Virtuelle Server (Einheit 2.1):** Richten Sie für `api.lab.test` einen eigenen `server`-Block ein und beweisen Sie mit zwei Aufrufen, dass zwei Namen auf derselben Adresse zu verschiedenen Backends führen.
5. **Zeitlimit (Einheit 2.3):** Setzen Sie `proxy_read_timeout 5s` und rufen Sie `/slow?s=7` auf. Welcher Status kommt, und welche Zeile steht im Fehlerprotokoll?

#### Kontrollfragen

1. Welchen Host-Header sieht das Backend, wenn man `proxy_set_header Host` nicht setzt?
2. Wie unterscheiden sich `proxy_pass http://b2/;` und `proxy_pass http://b2;` bei `location /api/`?
3. Warum ist `$proxy_add_x_forwarded_for` allein nicht vertrauenswürdig?
4. Was bedeutet 502, was 504?

### Modul 3: HAProxy als Reverse Proxy

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen HAProxy-Reverse-Proxy mit Frontends, Backends und ACLs konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Betriebsarten http und tcp unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Konfigurationsfehler mit `haproxy -c` erkennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Aufbau der Konfiguration: `global`, `defaults`, `frontend`, `backend`; Modus `http` und `tcp` | 3 |
| 3.2 | Weiterleitung nach Host und Pfad mit ACLs (`use_backend`), Header (`forwardfor`, `set-header`), Pfad umschreiben | 3 |
| 3.3 | Konfiguration prüfen (`haproxy -c`) und Betrieb über die Laufzeit-Schnittstelle (Admin-Socket) | 1 |
| 3.4 | Praxis: `haproxy_proxy.sh` ausführen (Host, Pfad, TCP-Modus, Status) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konfiguration prüfen (Einheit 3.3):** Prüfen Sie `haproxy_defekt.cfg` mit `haproxy -c -f` und nennen Sie die Meldung. Beheben Sie den Fehler.
2. **Host und Pfad (Einheit 3.2):** Prüfen Sie, dass `shop.lab.test` zu `b1` und `api.lab.test` zu `b2` führt und dass `/api/…` auf `b2` landet (ohne Präfix).
3. **Header (Einheit 3.2):** Prüfen Sie, welche Header das Backend bei HTTP-Modus und bei TCP-Modus (Port 9000) sieht, und erklären Sie den Unterschied.
4. **Aufbau lesen (Einheit 3.1):** Ordnen Sie in `haproxy.cfg` jede Zeile einem Abschnitt (`global`, `defaults`, `frontend`, `backend`) zu und erklären Sie deren Aufgabe.
5. **Admin-Socket (Einheit 3.4):** Fragen Sie über den Socket die Version und den Zustand der Server ab (`show info`, `show stat`).

#### Kontrollfragen

1. Welche Aufgaben haben `frontend`, `backend` und `defaults`?
2. Warum gibt es im TCP-Modus kein `X-Forwarded-For`?
3. Wie wählt HAProxy mit ACLs das Backend aus?
4. Wozu dient `haproxy -c`?

### Modul 4: TLS-Grundlagen und eine interne CA mit openssl

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine interne CA aufbauen und ein Serverzertifikat mit SAN ausstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Kette und den Namen eines Zertifikats prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler (fehlende CA, falscher Name) erkennen.
* **Voraussetzungen:** Modul 1; `openssl` installiert.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | TLS-Grundlagen: Handshake, Zertifikat, Kette, Vertrauen, Namen (SAN); TLS 1.2 und 1.3 | 2 |
| 4.2 | Interne CA aufbauen: Root-Schlüssel und -Zertifikat, Serverschlüssel, CSR, Signatur mit SAN | 3 |
| 4.3 | Prüfen: `openssl verify`, `-checkhost`, `-checkend`, Schlüssel-Zertifikat-Paar | 2 |
| 4.4 | Praxis: `ca_aufbau.sh` ausführen und TLS-Verbindung mit `s_server` und `s_client` testen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Root-CA (Einheit 4.2):** Erzeugen Sie Schlüssel und selbstsigniertes Zertifikat der Lab-CA (30 Tage) und zeigen Sie Aussteller, Inhaber und Laufzeit.
2. **Serverzertifikat (Einheit 4.2):** Erzeugen Sie Schlüssel und CSR für `shop.lab.test` und signieren Sie ihn mit der CA mit SAN `shop.lab.test` und `api.lab.test`.
3. **Prüfen (Einheit 4.3):** Prüfen Sie mit `openssl verify`, `-checkhost` und `-checkend` die Kette, den Namen und die Restlaufzeit. Passt der Schlüssel zum Zertifikat?
4. **Verbindung testen (Einheit 4.4):** Starten Sie `openssl s_server` und verbinden Sie sich mit `s_client` (a) mit CA, (b) ohne CA, (c) mit falschem Namen. Notieren Sie die Rückgabecodes.
5. **Begriffe (Einheit 4.1):** Erklären Sie in je einem Satz: Vertrauensanker, Zwischenzertifikat, SAN, CSR.

#### Kontrollfragen

1. Warum genügt der Common Name allein nicht mehr?
2. Wozu dient der CSR?
3. Was bedeutet „unable to verify the first certificate“?
4. Warum dürfen Schlüssel der CA nicht auf dem Proxy liegen?

### Modul 5: TLS-Terminierung mit nginx

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende HTTPS am nginx-Proxy einrichten und HTTP zum Backend sprechen.
  * Nach Abschluss dieses Moduls kann der Lernende HTTP auf HTTPS umleiten und HSTS setzen.
  * Nach Abschluss dieses Moduls kann der Lernende Protokollversionen festlegen und das Ergebnis prüfen.
* **Voraussetzungen:** Module 2 und 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | HTTPS-Server: `ssl_certificate`, `ssl_certificate_key`, `ssl_protocols`, Sitzungs-Cache, HTTP/2 | 2 |
| 5.2 | Weiterleitung von HTTP auf HTTPS (301), HSTS, `X-Forwarded-Proto` | 2 |
| 5.3 | Praxis: `nginx_tls.sh` ausführen: curl mit und ohne CA, Zertifikat, Protokollversionen | 3 |
| 5.4 | Protokollversionen einschränken und prüfen (`s_client -tls1_2`/`-tls1_3`), Hinweise zu Verschlüsselungssammlungen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **HTTPS einrichten (Einheit 5.1):** Laden Sie `tls.conf` (Zertifikat aus Modul 4) und rufen Sie `https://shop.lab.test/` mit `--cacert` auf. Welche Header sieht das Backend?
2. **Umleitung und HSTS (Einheit 5.2):** Rufen Sie `http://shop.lab.test/foo` auf und lesen Sie Status und `Location`. Prüfen Sie den HSTS-Header der HTTPS-Antwort.
3. **Fehlerfälle (Einheit 5.3):** Rufen Sie HTTPS ohne `--cacert` auf und notieren Sie den Rückgabewert von curl. Erklären Sie die Ursache.
4. **Zertifikat anzeigen (Einheit 5.3):** Zeigen Sie mit `s_client` Subject, Aussteller und SAN des Serverzertifikats.
5. **Nur TLS 1.3 (Einheit 5.4):** Stellen Sie `ssl_protocols` auf `TLSv1.3` um, laden Sie neu und testen Sie `s_client -tls1_2` und `-tls1_3`.

#### Kontrollfragen

1. Warum spricht der Proxy zum Backend oft nur HTTP, und welches Risiko entsteht dadurch?
2. Wozu dient HSTS, und welches Risiko birgt ein zu langer `max-age` bei Fehlkonfiguration?
3. Wie sieht das Backend, dass der Client HTTPS verwendet hat?
4. Was ändert sich in nginx ab Version 1.25.1 bei HTTP/2?

### Modul 6: TLS-Terminierung mit HAProxy und TLS-Durchleitung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende TLS am HAProxy terminieren und mehrere Zertifikate nach Namen ausliefern.
  * Nach Abschluss dieses Moduls kann der Lernende zwischen Terminierung und Durchleitung unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Weiterleitung und HSTS konfigurieren.
* **Voraussetzungen:** Module 3 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | `bind … ssl crt …`, PEM-Datei aus Zertifikat und Schlüssel, mehrere Zertifikate (SNI), ALPN `h2` | 2 |
| 6.2 | Weiterleitung auf HTTPS, HSTS, `ssl_fc`, `ssl_fc_sni`, Mindestversion | 2 |
| 6.3 | Praxis: `haproxy_tls.sh` ausführen (SNI, HTTP/2, Header) | 2 |
| 6.4 | TLS-Durchleitung (Passthrough) im TCP-Modus: Unterschied zur Terminierung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zertifikate bereitstellen (Einheit 6.1):** Erzeugen Sie je ein Zertifikat für `shop.lab.test` und `api.lab.test` (PEM mit Zertifikat und Schlüssel) und binden Sie beide in HAProxy ein.
2. **Weiterleitung und HSTS (Einheit 6.2):** Prüfen Sie die Weiterleitung von HTTP auf HTTPS und den HSTS-Header.
3. **SNI testen (Einheit 6.3):** Fordern Sie mit `s_client -servername` beide Namen an und vergleichen Sie Zertifikat und Backend.
4. **HTTP/2 (Einheit 6.3):** Prüfen Sie mit `curl --http2`, welche HTTP-Version ausgehandelt wird.
5. **Passthrough (Einheit 6.4):** Rufen Sie Port 8443 auf und erklären Sie, warum das Zertifikat hier vom dahinterliegenden Server stammt und warum HAProxy keine HTTP-Header ändern kann.

#### Kontrollfragen

1. Warum braucht HAProxy Zertifikat und Schlüssel in einer Datei?
2. Was ist SNI, und wozu benötigt der Proxy ihn?
3. Welche Vor- und Nachteile hat die Durchleitung gegenüber der Terminierung?
4. Welche Rolle spielt ALPN?

### Modul 7: Let’s Encrypt und ACME mit einem lokalen Testserver (Pebble)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer ACME-Ausstellung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende mit certbot ein Zertifikat vom lokalen Testserver beziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Erneuerung und Neuladen des Proxys automatisieren.
* **Voraussetzungen:** Modul 5; Pebble und certbot auf `px01` bereitgestellt.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | ACME-Protokoll: Konto, Bestellung, Challenge (HTTP-01), Ausstellung, Erneuerung; Let’s Encrypt als Beispiel | 2 |
| 7.2 | Pebble als lokaler ACME-Testserver: Start, Verzeichnis, Wurzelzertifikat; Namensauflösung | 2 |
| 7.3 | Praxis: certbot mit `standalone` und `webroot`, Zertifikat in nginx einbinden (`acme_pebble.sh`) | 3 |
| 7.4 | Erneuerung mit Hook, Laufzeit und Erneuerungskonfiguration | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Pebble starten (Einheit 7.2):** Starten Sie Pebble mit der Konfiguration aus dem Skript (Prüfport 80) und rufen Sie das Verzeichnis `https://localhost:14000/dir` ab.
2. **standalone (Einheit 7.3):** Beziehen Sie mit `certbot certonly --standalone` ein Zertifikat für `shop.lab.test` und lesen Sie Aussteller und SAN.
3. **webroot (Einheit 7.3):** Beziehen Sie ein Zertifikat für `api.lab.test` mit `--webroot`, während nginx die Challenge-Datei ausliefert, und binden Sie es in nginx ein.
4. **Prüfung (Einheit 7.2):** Rufen Sie `https://api.lab.test/` mit dem Wurzelzertifikat von Pebble (`/roots/0`) auf.
5. **Erneuern (Einheit 7.4):** Führen Sie `certbot renew --force-renewal` mit einem Deploy-Hook aus, der nginx neu lädt, und beweisen Sie, dass nginx das neue Zertifikat ausliefert.
6. **Ablauf erklären (Einheit 7.1):** Beschreiben Sie in fünf Schritten, was bei einer HTTP-01-Challenge zwischen certbot, Pebble und dem Webserver passiert.

#### Kontrollfragen

1. Warum muss der Name beim HTTP-01-Verfahren vom ACME-Server aus erreichbar sein?
2. Worin unterscheiden sich `--standalone` und `--webroot`?
3. Warum laufen ausgestellte Zertifikate nur kurz (im Lauf 90 Tage), und wie hilft Automatisierung?
4. Wozu dient ein Deploy-Hook?

### Modul 8: Lastverteilung mit nginx

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Anfragen mit mehreren Verfahren verteilen und die Verteilung messen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ausfall eines Backends ohne Fehler für die Clients überbrücken.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen der passiven Prüfung benennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Upstream-Verfahren: Round Robin, `weight`, `least_conn`, `ip_hash`; Wahl nach Anwendung | 3 |
| 8.2 | Passive Gesundheitsprüfung: `max_fails`, `fail_timeout`, `proxy_next_upstream` | 2 |
| 8.3 | Praxis: `nginx_lb.sh` ausführen und Verteilung messen | 3 |
| 8.4 | Grenzen: keine aktive Prüfung in nginx (Open Source), Sitzungsbindung, Ausfallverhalten | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Round Robin (Einheit 8.1):** Verteilen Sie 20 Anfragen auf zwei Backends und zählen Sie die Treffer je Backend.
2. **Gewichte (Einheit 8.1):** Setzen Sie `weight=3` für ein Backend und messen Sie das Verhältnis.
3. **ip_hash (Einheit 8.1):** Zeigen Sie, dass `ip_hash` einen Client immer demselben Backend zuordnet, und nennen Sie einen Nachteil.
4. **least_conn (Einheit 8.3):** Halten Sie ein Backend mit einer langsamen Anfrage besetzt und zeigen Sie, dass `least_conn` kurze Anfragen überwiegend zum anderen schickt.
5. **Ausfall (Einheit 8.2):** Beenden Sie ein Backend, schicken Sie 20 Anfragen und lesen Sie das Fehlerprotokoll (`connect() failed`). Starten Sie das Backend wieder und messen Sie, wann es zurückkehrt.
6. **Grenzen (Einheit 8.4):** Beschreiben Sie, was passive Prüfung nicht erkennt (z. B. ein Backend, das 200 mit leerer Seite liefert).

#### Kontrollfragen

1. Wann ist `ip_hash` besser als Round Robin, wann schlechter?
2. Was bewirken `max_fails=2` und `fail_timeout=5s`?
3. Warum bekommen die Clients bei einem Ausfall trotzdem eine Antwort?
4. Warum ist eine aktive Prüfung zuverlässiger?

### Modul 9: Lastverteilung und Health Checks mit HAProxy

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Verfahren und Gewichte in HAProxy einsetzen und messen.
  * Nach Abschluss dieses Moduls kann der Lernende aktive Prüfungen konfigurieren und das Verhalten bei Ausfall und Rückkehr erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Server im laufenden Betrieb sanft herausnehmen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Verfahren: `roundrobin`, `leastconn`, `source`, Gewichte; Sitzungsbindung per Cookie | 3 |
| 9.2 | Aktive Gesundheitsprüfung: `option httpchk`, `check`, `inter`, `fall`, `rise`, `backup` | 3 |
| 9.3 | Praxis: `haproxy_lb.sh` ausführen (Verteilung, Cookie, Ausfall, Wiederkehr, Backup) | 2 |
| 9.4 | Laufzeit-Schnittstelle: `drain`, `disable`, Gewicht ändern, Zustand lesen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verteilung (Einheit 9.1):** Messen Sie Round Robin und Gewicht 3:1 mit je 20 Anfragen.
2. **Cookie (Einheit 9.1):** Zeigen Sie, dass mit `cookie SRV insert` ein Client mit Cookie-Datei beim selben Server bleibt, ohne Cookie aber wechselt.
3. **Aktive Prüfung (Einheit 9.2):** Lassen Sie `/health` von `b2` einen Fehler (503) liefern und zeigen Sie mit `show stat` den Status DOWN und das Prüfergebnis (`L7STS`). Messen Sie die Verteilung danach.
4. **Rückkehr und Backup (Einheit 9.2):** Beheben Sie den Fehler und zeigen Sie die Rückkehr (UP). Konfigurieren Sie `b2` als `backup` und zeigen Sie, dass er nur bei Ausfall von `b1` trägt.
5. **Laufzeit (Einheit 9.4):** Setzen Sie über den Socket `b2` auf `drain`, danach wieder auf `ready`, und ändern Sie die Gewichte im laufenden Betrieb.
6. **Skript lesen (Einheit 9.3):** Führen Sie `bash haproxy_lb.sh` aus und erklären Sie jede Ausgabe.

#### Kontrollfragen

1. Was bedeuten `inter 1s fall 2 rise 2`?
2. Wie unterscheiden sich `drain` und `disable`?
3. Wann ist `balance source` sinnvoll?
4. Warum ist eine Cookie-Bindung mit `insert indirect nocache` für Browser transparent?

### Modul 10: Header, HSTS und das PROXY-Protokoll

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende gefälschte X-Forwarded-For-Ketten erkennen und verhindern.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherheits-Header am Proxy setzen und Server-Angaben verbergen.
  * Nach Abschluss dieses Moduls kann der Lernende das PROXY-Protokoll zwischen zwei Proxys einsetzen.
* **Voraussetzungen:** Module 2 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Client-Adresse sicher weitergeben: `X-Forwarded-For` überschreiben statt anhängen, `X-Real-IP`, Vertrauensgrenzen | 2 |
| 10.2 | Sicherheits-Header: `X-Content-Type-Options`, `X-Frame-Options`, `Content-Security-Policy`, `Referrer-Policy`, HSTS; Server-Angaben verbergen | 2 |
| 10.3 | PROXY-Protokoll: HAProxy (`send-proxy`) und nginx (`proxy_protocol`, `real_ip_header`) | 2 |
| 10.4 | Praxis: `header_proxyprotocol.sh` ausführen und Ergebnisse auswerten | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fälschung zeigen (Einheit 10.1):** Senden Sie ein eigenes `X-Forwarded-For: 6.6.6.6` an den naiven Proxy und lesen Sie die Kette, die das Backend sieht.
2. **Härten (Einheit 10.1):** Überschreiben Sie die Kette mit `$remote_addr` und wiederholen Sie den Test.
3. **Sicherheits-Header (Einheit 10.2):** Vergleichen Sie die Antwort-Header beider Server (Port 80 und 81) und erklären Sie jeden Header in einem Satz.
4. **PROXY-Protokoll (Einheit 10.3):** Zeigen Sie, dass das Backend mit `send-proxy` die Adresse des Clients (`x-real-ip`) erfährt und dass nginx ohne `send-proxy` die Verbindung ablehnt.
5. **Auswerten (Einheit 10.4):** Führen Sie `bash header_proxyprotocol.sh` aus und erklären Sie, wo jeweils die Vertrauensgrenze liegt.

#### Kontrollfragen

1. Warum ist `$proxy_add_x_forwarded_for` am äußersten Proxy riskant?
2. Wozu dient `X-Frame-Options: DENY`?
3. Was überträgt das PROXY-Protokoll, und warum ist es besser als ein HTTP-Header?
4. Welche Gefahr besteht, wenn nginx `proxy_protocol` auf einem öffentlich erreichbaren Port erwartet?

### Modul 11: WebSocket hinter dem Proxy

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Verbindungsaufbau einer WebSocket-Verbindung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende WebSocket durch nginx und HAProxy leiten.
  * Nach Abschluss dieses Moduls kann der Lernende Leerlaufzeiten als Ursache getrennter Verbindungen erkennen.
* **Voraussetzungen:** Module 2 und 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | WebSocket-Handshake (Upgrade), langlebige Verbindungen, Unterschied zu HTTP-Anfragen | 2 |
| 11.2 | nginx: `proxy_http_version 1.1`, `Upgrade`, `Connection`, `proxy_read_timeout` | 2 |
| 11.3 | HAProxy: Upgrade und `timeout tunnel` | 1 |
| 11.4 | Praxis: `websocket.sh` mit `ws_client.py` ausführen (ohne Header, kurze und lange Leerlaufzeit) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fehlender Upgrade (Einheit 11.2):** Rufen Sie `/ohne` auf und lesen Sie den Status. Warum kommt der Upgrade nicht beim Backend an?
2. **Richtig konfigurieren (Einheit 11.2):** Konfigurieren Sie `proxy_http_version 1.1` sowie die Header `Upgrade` und `Connection` und zeigen Sie den Status 101 und eine Echo-Antwort.
3. **Leerlaufzeit nginx (Einheit 11.2):** Zeigen Sie, dass `proxy_read_timeout 3s` eine Verbindung nach 5 s Pause kappt und 60 s sie hält.
4. **HAProxy (Einheit 11.3):** Wiederholen Sie die Tests mit `timeout tunnel 3s` und `60s`.
5. **Handshake beschreiben (Einheit 11.1):** Beschreiben Sie die Header des Handshakes (`Upgrade`, `Connection`, `Sec-WebSocket-Key`, `Sec-WebSocket-Accept`).
6. **Skript lesen (Einheit 11.4):** Führen Sie `bash websocket.sh` aus und erklären Sie jede Ausgabe.

#### Kontrollfragen

1. Warum gibt nginx `Upgrade` und `Connection` nicht automatisch weiter?
2. Was passiert bei einer WebSocket-Verbindung, die längere Zeit nichts überträgt?
3. Wofür steht Status 101?
4. Wie können Anwendungen Leerlauf-Trennungen vermeiden?

### Modul 12: Caching im Reverse Proxy

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen nginx-Cache einrichten und seinen Zustand lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Gültigkeit aus Backend-Headern ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende bei Ausfall des Backends veraltete Antworten ausliefern.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Cache-Grundlagen: `Cache-Control`, `max-age`, Schlüssel, Gültigkeit; `proxy_cache_path`, `proxy_cache` | 2 |
| 12.2 | Statusanzeige `$upstream_cache_status`: MISS, HIT, EXPIRED, BYPASS, STALE | 2 |
| 12.3 | Praxis: `cache_demo.sh` ausführen (Treffer, Ablauf, Bypass, Ausfall des Backends) | 3 |
| 12.4 | Was man nicht cachen darf (personalisierte Inhalte, POST), `proxy_cache_lock`, `use_stale` | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Cache einrichten (Einheit 12.1):** Legen Sie `proxy_cache_path` und `proxy_cache` an und zeigen Sie MISS und HIT.
2. **Ohne Cache vergleichen (Einheit 12.3):** Rufen Sie denselben Inhalt ohne Cache auf und zeigen Sie, dass jede Anfrage das Backend erreicht.
3. **Bypass (Einheit 12.2):** Umgehen Sie den Cache mit einem Header (`proxy_cache_bypass`) und zeigen Sie, wie der Cache-Eintrag danach aussieht.
4. **Ablauf (Einheit 12.2):** Zeigen Sie EXPIRED nach Ablauf von `max-age=10` und erklären Sie, warum die Messung auf ganze Sekunden rundet.
5. **Ausfall (Einheit 12.3):** Beenden Sie das Backend nach dem Ablauf und zeigen Sie STALE bei `proxy_cache_use_stale` sowie den Fehler 502 ohne Cache.
6. **Risiken (Einheit 12.4):** Nennen Sie drei Inhalte, die nicht in den Cache gehören.

#### Kontrollfragen

1. Woher bezieht nginx die Gültigkeit, wenn das Backend `Cache-Control` sendet?
2. Wann liefert nginx STALE?
3. Warum ist `proxy_cache_lock` bei vielen gleichzeitigen Anfragen sinnvoll?
4. Welche Risiken entstehen, wenn personalisierte Inhalte im gemeinsamen Cache landen?

### Modul 13: Sicherheit, Fehlersuche und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische Proxy-Fehler an Status und Protokoll erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Schutzmaßnahmen (Begrenzung, Größen, Zeitlimits) einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende einen vollständigen Proxy dokumentieren und testen.
* **Voraussetzungen:** Module 2 bis 10.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Schutz am Proxy: `limit_req`, Größenbegrenzung, Zeitlimits, Standard-Server (444), Server-Angaben | 2 |
| 13.2 | Fehlerbilder: 502, 504, 413, 429, 503; Zugriffs- und Fehlerprotokoll lesen | 2 |
| 13.3 | Praxis: `fehlersuche.sh` ausführen und jeden Fall zuordnen | 2 |
| 13.4 | Abschlussprojekt: HTTPS-Proxy mit Lastverteilung, Schutz und Testkatalog (`abschluss.conf`, `abschluss_test.sh`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fälle zuordnen (Einheit 13.3):** Führen Sie `bash fehlersuche.sh` aus. Ordnen Sie jedem der Fälle (`/abgelehnt`, `/tot`, `/langsam`, `/upload`, unbekannter Host) Status, Ursache und Protokollzeile zu.
2. **Begrenzung (Einheit 13.1):** Erklären Sie, warum bei `rate=2r/s burst=2 nodelay` von 10 schnellen Anfragen genau drei durchgehen.
3. **Protokolle (Einheit 13.2):** Lesen Sie die Zeilen des Fehlerprotokolls zu 502 und 504 und erklären Sie den Unterschied.
4. **HAProxy 503 (Einheit 13.2):** Zeigen Sie, dass HAProxy bei ausgefallenen Servern 503 liefert, und begründen Sie, warum das nicht vom Backend stammt.
5. **Abschlussprojekt (Einheit 13.4):** Bauen Sie den Proxy aus den Anforderungen: HTTPS mit Lab-CA, Weiterleitung 80 zu 443, HSTS, zwei Backends mit Ausfalltoleranz, Begrenzung, überschriebenes `X-Forwarded-For`, keine Server-Version, unbekannte Namen ohne Antwort. Schreiben Sie dazu einen Testkatalog.
6. **Vorgehen (Einheit 13.2):** Beschreiben Sie in fünf Schritten Ihr Vorgehen bei „Seite nicht erreichbar“ (Client, Proxy, Backend, Protokolle, Änderung).

#### Kontrollfragen

1. Woran erkennt man im Fehlerprotokoll den Unterschied zwischen einem abgelehnten und einem zu langsamen Backend?
2. Was bedeutet `burst` bei `limit_req`?
3. Warum ist HTTP 444 in nginx kein echter HTTP-Statuscode?
4. Warum sollte ein Testkatalog vor jeder Änderung der Konfiguration laufen?
