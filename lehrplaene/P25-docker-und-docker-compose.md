# Lehrplan: Docker und Docker Compose

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Docker Engine unter Linux, Docker Compose, Container und Images, Dockerfile, Registries, Volumes und Netzwerke, Ressourcenlimits, Sicherheit, Aufräumen, Logging, Sicherung von Daten, Lizenz von Docker Desktop und Alternativen |
| **Thematische Abgrenzung (Out of Scope)** | **Im Cloud-Container echt ausgeführt:** Docker Engine 29.9.2 mit Compose 5.7.0 (BuildKit), eine lokale Registry (`registry` 2.8.2) und Podman 4.9.3. Der Docker-Daemon musste dort von Hand gestartet werden (kein systemd). **Docker Hub war nicht erreichbar**; die Übungen benutzen daher ein **selbst gebautes Basis-Image aus `busybox-static`** (`p25/busybox:lab`) statt offizieller Images. **Nicht ausgeführt:** Docker Desktop (nur Windows und macOS), Rootless-Docker, ein Schwachstellenscanner für Images, Docker Hub und andere Internet-Registries, AppArmor- und SELinux-Profile, Hyper-V. Kubernetes ist ein eigener Kurs (P26). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Container und Images | 1 | 12 |
| 2 | Dockerfile und Images bauen | 1 | 14 |
| 3 | Registries | 1 | 10 |
| 4 | Volumes und Netzwerke | 1 | 14 |
| 5 | Docker Compose | 1 | 14 |
| 6 | Ressourcengrenzen, Logging und Sicherheit | 1 | 14 |
| 7 | Docker Desktop, Lizenz und Alternativen | 2 | 8 |
| 8 | Betrieb, Aufräumen, Sicherung und Abschlussprojekt | 1 | 14 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Docker Desktop, Lizenz und Alternativen). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 92 UE. **Hinweis:** Der Lehrplan verlangt, die Lizenzbedingungen von Docker Desktop mit Stand zu nennen; das geschieht in Schritt 5 von Modul 7. Bei Wegfall des Moduls sollte zumindest dieser Schritt (etwa 1 UE) gelesen werden.

### 2. Quellen

**Stand der Lizenzbedingungen von Docker Desktop (20.11.2026, Unsicherheit gekennzeichnet):** Gelesen wurde nur die **Zusammenfassung einer Seite von docs.docker.com**, die als zuletzt aktualisiert den 28.09.2026 nannte; der **Wortlaut der Bedingungen wurde nicht gelesen**. Danach ist Docker Desktop kostenlos für kleine Unternehmen (weniger als 250 Beschäftigte und weniger als 10 Mio. USD Jahresumsatz), für den persönlichen Gebrauch, die Ausbildung und nichtkommerzielle Open-Source-Projekte; die berufliche Nutzung in größeren Organisationen und in Behörden braucht ein kostenpflichtiges Abonnement. **Vor jedem Einsatz die Originalseite lesen.** Die Lizenz von Docker Engine unter Linux wurde nicht geprüft.

**Getestet mit (Ubuntu 24.04, Cloud-Container):** Docker Engine 29.9.2, Compose 5.7.0, Registry 2.8.2, Podman 4.9.3. **Nicht ausgeführt:** Docker Desktop, Rootless-Docker, Image-Scanner, Docker Hub. Aussagen zu Konzepten (Namespaces, Schichten, 3-2-1-Regel) sind Fachwissen und nicht gegen die Dokumentation geprüft.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Docker`, `10.70.0.0/24`).

**VM 1:** `dock01` (**erforderlich**, `10.70.0.10`): Ubuntu Server mit Docker Engine (Compose-Plugin).

**Internetphase:** Zum Installieren von Docker und zum Laden von Images braucht `dock01` vorübergehend Internetzugang; danach wird er entfernt. Für die Übungen ohne Internet genügen die selbst gebauten Basis-Images der Skripte.

**Prüfpunkt (Checkpoint):** Vor Modul 6 und Modul 8 einen Prüfpunkt von `dock01` anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux mit einem laufenden Docker-Daemon und arbeiten unter `/tmp/p25`. Sie räumen am Ende ihre Container, Netze, Volumes und Images mit dem Label `p25` auf.

## B. Detaillierter Modulaufbau

### Modul 1: Container und Images

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Container als isolierten Prozess erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Lebenslauf eines Containers (create, start, stop, rm) nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Logs lesen und Befehle mit exec ausführen.
  * Nach Abschluss dieses Moduls kann der Lernende Image und Container unterscheiden.
* **Voraussetzungen:** Linux-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Isolation | 4 |
| 1.2 | Lebenslauf | 4 |
| 1.3 | Image und Container | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Isolation (Einheit 1.1):** Führen Sie `bash container.sh` aus. Erklären Sie Schritt 2 und 5: Woran erkennt man, dass der Container ein isolierter Prozess ist?
2. **Lebenslauf (Einheit 1.2):** Erklären Sie Schritt 3 und 6: Welche Zustände durchläuft der Container, und was bedeuten die Exit-Codes 137 und 3?
3. **Image und Container (Einheit 1.3):** Erklären Sie Schritt 7: Was ist der Unterschied?

#### Kontrollfragen

1. Welche Prozess-ID hat die Shell im Container?
2. Welche Namespaces hat der Container?
3. Was bedeutet Exit-Code 137?
4. Wie liest man die Ausgabe eines Containers?

### Modul 2: Dockerfile und Images bauen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Dockerfile mit FROM, COPY, RUN, ENV, ARG, USER und ENTRYPOINT/CMD lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Schichten und den Bau-Cache erklären.
  * Nach Abschluss dieses Moduls kann der Lernende .dockerignore einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen mehrstufigen Bau beschreiben.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Bauen | 6 |
| 2.2 | Schichten und Cache | 4 |
| 2.3 | Sauberkeit | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bauen (Einheit 2.1):** Führen Sie `bash dockerfile.sh` aus. Erklären Sie Schritt 1 und 2: Was bewirken ENTRYPOINT und CMD?
2. **Schichten und Cache (Einheit 2.2):** Erklären Sie Schritt 4 und 5: Warum werden nach der Änderung von `version.txt` zwei Schritte neu gebaut, `WORKDIR` aber nicht?
3. **Sauberkeit (Einheit 2.3):** Erklären Sie Schritt 3, 6 und 7: Was bewirken `.dockerignore`, ARG/ENV und der mehrstufige Bau?

#### Kontrollfragen

1. Wie viele Dateisystemschichten hat das Image?
2. Was geschieht im Cache nach Änderung einer kopierten Datei?
3. Warum fehlt `secret.txt` im Image?
4. Was bringt der mehrstufige Bau?

### Modul 3: Registries

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines Image-Namens (Registry/Pfad:Tag) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Image taggen, hochladen und wieder holen.
  * Nach Abschluss dieses Moduls kann der Lernende Katalog und Tags über die Registry-API abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende Digest und Tag unterscheiden.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Hochladen | 4 |
| 3.2 | Abfragen | 3 |
| 3.3 | Tag und Digest | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Hochladen (Einheit 3.1):** Führen Sie `bash registry.sh` aus. Erklären Sie Schritt 2: Wie ist der Name `localhost:5000/p25/basis:1.0` aufgebaut?
2. **Abfragen (Einheit 3.2):** Erklären Sie Schritt 1 und 3: Was liefert die Registry-API?
3. **Tag und Digest (Einheit 3.3):** Erklären Sie Schritt 5 und 6: Warum ist der Digest verlässlicher als der Tag?

#### Kontrollfragen

1. Welche Antwort liefert `GET /v2/`?
2. Welche Tags hat `p25/basis`?
3. Was zeigt Schritt 4?
4. Was meldet Docker bei einem unbekannten Image?

### Modul 4: Volumes und Netzwerke

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende benannte Volumes, Bind-Mounts und tmpfs unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende zeigen, dass Daten ohne Volume mit dem Container verschwinden.
  * Nach Abschluss dieses Moduls kann der Lernende Namensauflösung in eigenen Netzen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Ports veröffentlichen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Daten | 6 |
| 4.2 | Netze | 4 |
| 4.3 | Ports | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Daten (Einheit 4.1):** Führen Sie `bash netz.sh` aus. Erklären Sie Schritt 1 bis 3: Welche Daten überleben, welche nicht, und warum ist der Bind-Mount schreibgeschützt?
2. **Netze (Einheit 4.2):** Erklären Sie Schritt 4: Warum scheitert der Name `web0` im Standardnetz?
3. **Ports (Einheit 4.3):** Erklären Sie Schritt 5 und 6: Wie wird ein Dienst erreichbar, und was hat ein Container ohne Netz?

#### Kontrollfragen

1. Wie überleben Daten das Entfernen eines Containers?
2. Was bewirkt `ro` beim Bind-Mount?
3. Was unterscheidet das Standardnetz von einem eigenen Netz?
4. Was hat ein Container mit `--network none`?

### Modul 5: Docker Compose

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Compose-Datei lesen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Abhängigkeiten mit Gesundheitsprüfung (healthcheck) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Umgebungsvariablen mit Vorgabewert setzen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Projekt mit `up` und `down` betreiben.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Prüfen und starten | 6 |
| 5.2 | Abhängigkeit | 4 |
| 5.3 | Projekt | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prüfen und starten (Einheit 5.1):** Führen Sie `bash compose.sh` aus. Erklären Sie Schritt 1 und 2: Welche Dienste gibt es, und was zeigt der Zustand „healthy“?
2. **Abhängigkeit (Einheit 5.2):** Erklären Sie Schritt 3: Warum wartet `client` auf `web`?
3. **Projekt (Einheit 5.3):** Erklären Sie Schritt 4 bis 6: Wie entstehen die Namen der Netze und Container, und was entfernt `down`?

#### Kontrollfragen

1. Welche Dienste hat die Datei?
2. Wozu dient die Gesundheitsprüfung?
3. Wie wird die Vorgabe einer Variablen überschrieben?
4. Wie heißen Netz und Container?

### Modul 6: Ressourcengrenzen, Logging und Sicherheit

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Speicher-, Prozess- und CPU-Grenzen setzen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende die Rotation von Logs einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende Schreibschutz, Benutzer, Capabilities und no-new-privileges einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen der gezeigten Maßnahmen benennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Grenzen | 6 |
| 6.2 | Logs | 4 |
| 6.3 | Rechte | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Grenzen (Einheit 6.1):** Führen Sie `bash grenzen.sh` aus. Erklären Sie Schritt 1 und 2: Warum endet der Container mit Exit-Code 137 und `OOMKilled: true`?
2. **Logs (Einheit 6.2):** Erklären Sie Schritt 3: Wie viele Logdateien bleiben, und was steht darin?
3. **Rechte (Einheit 6.3):** Erklären Sie Schritt 4 bis 6: Was bewirken `--read-only`, `--user`, `--cap-drop ALL` und `no-new-privileges`?

#### Kontrollfragen

1. Was bedeutet `OOMKilled: true`?
2. Wie viele Logdateien bleiben bei `max-file=2`?
3. Welcher Benutzer läuft im Container?
4. Was zeigt `CapEff` nach `--cap-drop ALL`?

### Modul 7: Docker Desktop, Lizenz und Alternativen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Docker Engine unter Linux und Docker Desktop unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende den Lizenzstand von Docker Desktop mit Datum und Quelle wiedergeben und Unsicherheit benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Podman als Alternative mit denselben Images einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen der Gleichwertigkeit benennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Engine unter Linux | 4 |
| 7.2 | Podman | 2 |
| 7.3 | Lizenz | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Engine unter Linux (Einheit 7.1):** Führen Sie `bash alternativen.sh` aus. Erklären Sie Schritt 1 und 2: Was ist installiert, und was nicht?
2. **Podman (Einheit 7.2):** Erklären Sie Schritt 3 und 4: Was wurde übernommen, was nicht geprüft?
3. **Lizenz (Einheit 7.3):** Geben Sie Schritt 5 in eigenen Worten wieder: Wer zahlt, wer nicht, und was ist nicht gelesen?

#### Kontrollfragen

1. Wo läuft Docker Engine?
2. Wie kam das Image zu Podman?
3. Wer braucht ein Abonnement für Docker Desktop?
4. Welche Lizenz hat Docker Engine unter Linux?

### Modul 8: Betrieb, Aufräumen, Sicherung und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Belegung ansehen und Ungenutztes entfernen.
  * Nach Abschluss dieses Moduls kann der Lernende Daten eines Volumes sichern und wiederherstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Neustartrichtlinien beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende ein Compose-Projekt mit Sicherung abnehmen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Aufräumen | 6 |
| 8.2 | Sicherung | 4 |
| 8.3 | Abschluss | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufräumen (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1 und 2: Was entfernt `prune`, was nicht?
2. **Sicherung (Einheit 8.2):** Erklären Sie Schritt 3 und 4: Wie wird ein Volume gesichert und wiederhergestellt, und woran sieht man, dass die Daten gleich sind?
3. **Abschluss (Einheit 8.3):** Führen Sie `bash abschluss.sh` aus und erklären Sie Schritt 1 bis 5: Was geht verloren, was kommt zurück?

#### Kontrollfragen

1. Welche Volumes entfernt `volume prune`?
2. Wie weist man nach, dass die Wiederherstellung vollständig ist?
3. Was bewirkt `on-failure:2`?
4. Ist ein Volume auf demselben Rechner eine Sicherung?
