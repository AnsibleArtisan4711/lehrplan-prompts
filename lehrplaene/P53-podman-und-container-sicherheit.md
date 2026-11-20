# Lehrplan: Podman und Container-Sicherheit

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen; Grundlagen von Docker oder Containern |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Podman, Buildah, Skopeo auf Debian/Ubuntu oder Fedora/RHEL-Derivaten; Rootless-Container; Pods; Images bauen und prüfen; Volumes und Netzwerke; systemd-Einbindung mit Quadlet; Kubernetes-YAML und Compose; Sicherheit (Capabilities, seccomp, Richtlinien für Image-Signaturen); Ressourcenlimits; Fehlersuche |
| **Thematische Abgrenzung (Out of Scope)** | Docker und Docker Compose sind ein eigener Kurs; Kubernetes nur als Ausblick (Erzeugen und Abspielen von Pod-YAML). Nicht behandelt: Betrieb einer eigenen Registry, SELinux- und AppArmor-Profile im Detail, Schwachstellenscanner im Betrieb, Orchestrierung über mehrere Hosts |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Podman im Überblick: erste Container | 1 | 12 |
| 2 | Rootless-Container | 1 | 12 |
| 3 | Pods, Volumes und Netzwerke | 1 | 14 |
| 4 | Images bauen und prüfen: Containerfile, Buildah, Skopeo | 1 | 14 |
| 5 | systemd-Einbindung mit Quadlet | 1 | 12 |
| 6 | Mehrere Container: Kubernetes-YAML und Compose | 2 | 10 |
| 7 | Container-Sicherheit | 1 | 14 |
| 8 | Ressourcenlimits und Fehlersuche | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 5, 7 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 6 (Kubernetes-YAML und Compose). Fällt Modul 6 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 6 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Podman, Buildah, Skopeo und Quadlet wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt; verbindlich ist die Dokumentation der eingesetzten Version. Zahlen und Namen sind erfundene Beispieldaten.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container, Kernel 6.18.44, cgroup v1, kein systemd):** Podman 4.9.3 (Laufzeit `runc`, Speichertreiber `overlay`), Buildah 1.33.7, Skopeo 1.13.3, ein selbst aus der statischen `busybox` gebautes Image `localhost/bb:1` (kein Zugriff auf eine Registry). Rootless-Container liefen nur ohne Netzwerk (`--network=none`). **Nicht ausgeführt:** Zugriff auf Registries (`pull`, `push`, `login`), Image-Signaturen, SELinux und AppArmor, Schwachstellenscanner, systemd-Dienste (bei Quadlet nur der Probelauf des Generators), Podman Compose, Rootless-Netzwerk. Diese Teile sind Textdateien mit der Kennzeichnung „nicht ausgeführt“ und **nicht bestätigt**. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Container`, `10.53.0.0/24`).

**VM:** `pod01` (**erforderlich**, `10.53.0.2`): Linux-Server (Debian, Ubuntu oder Fedora/RHEL-Derivat) mit den Paketen `podman`, `buildah`, `skopeo`, `uidmap`; ein normaler Benutzer für die Rootless-Übungen.

**Internetphase:** Für die Installation der Pakete und für `podman pull` braucht `pod01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es werden nur erfundene Beispieldaten verwendet.

**Prüfpunkt (Checkpoint):** Vor Modul 5 und vor Modul 7 von `pod01` je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte bauen ein winziges Image `localhost/bb:1` aus der statischen `busybox` (Paket `busybox-static` oder vorhandenes `busybox`; `lab.sh`), brauchen keine Registry, legen den Benutzer `rl1` an und räumen am Ende alles auf. Auf `pod01` verwenden Sie stattdessen Images aus einer Registry.

## B. Detaillierter Modulaufbau

### Modul 1: Podman im Überblick: erste Container

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Container starten, auflisten, darin Befehle ausführen und sein Protokoll lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Exitcodes wie 137 deuten.
  * Nach Abschluss dieses Moduls kann der Lernende die Befehle `run`, `ps`, `exec`, `logs`, `stop`, `rm` erklären.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor `pod01` aufbauen.
* **Voraussetzungen:** Grundlagen von Docker oder Containern.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Container starten, auflisten, `exec` und `logs` (`grundlagen.sh`) | 4 |
| 1.2 | Beenden, Exitcodes und Entfernen (`grundlagen.sh`) | 3 |
| 1.3 | Unterschiede zu Docker: kein Dienst im Hintergrund (Fachwissen) | 2 |
| 1.4 | Labor aufbauen: `pod01`, privater Switch | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Container starten (Einheit 1.1):** Führen Sie `bash grundlagen.sh` aus. Erklären Sie die Befehle der Schritte 2 bis 4 und den Unterschied zwischen `run --rm` und `run -d`.
2. **Exitcodes (Einheit 1.2):** Erklären Sie Schritt 5: Warum endet der Container mit dem Exitcode 137, obwohl `podman stop` ihn beenden sollte? Was bedeutet 137?
3. **Programm-Exitcode (Einheit 1.3):** Erklären Sie Schritt 6: Wie gelangt der Exitcode des Programms zum Host?
4. **Labor aufbauen (Einheit 1.4):** Bauen Sie `pod01` mit Podman auf und führen Sie `podman run --rm` mit einem Image Ihrer Wahl aus (Internetphase).

#### Kontrollfragen

1. Was bedeutet `--rm`?
2. Wie sieht man das Protokoll eines Containers?
3. Was besagt der Exitcode 137 (Fachwissen)?
4. Worin unterscheidet sich Podman von Docker beim Hintergrunddienst (Fachwissen)?

### Modul 2: Rootless-Container

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Container-root auf einen normalen Benutzer abgebildet wird.
  * Nach Abschluss dieses Moduls kann der Lernende die Zuordnung in `/proc/self/uid_map` lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Vorteile und Grenzen von Rootless-Betrieb nennen.
  * Nach Abschluss dieses Moduls kann der Lernende den Speicherort der Images eines Benutzers finden.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Untergeordnete Nummern (`subuid`) und Benutzer-Namensraum (`rootless.sh`) | 4 |
| 2.2 | Container als normaler Benutzer starten, `uid_map` lesen (`rootless.sh`) | 3 |
| 2.3 | Speicherort und Eigenständigkeit des Benutzers (`rootless.sh`) | 2 |
| 2.4 | Rootless-Netzwerk: Einschränkungen im Container (`rootless.sh`) | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zuordnung lesen (Einheit 2.1):** Führen Sie `bash rootless.sh` aus. Erklären Sie die zwei Zeilen von `uid_map` aus Schritt 3.
2. **Host-Sicht (Einheit 2.2):** Erklären Sie Schritt 4: Unter welchem Benutzer läuft der Container-Prozess auf dem Host, obwohl er im Container `root` ist?
3. **Speicher (Einheit 2.3):** Erklären Sie Schritt 5: Warum hat jeder Benutzer eigene Images?
4. **Netzwerk (Einheit 2.4):** Erklären Sie Schritt 6: Welche Rolle spielt `slirp4netns`, und was scheiterte im Container?

#### Kontrollfragen

1. Was ist ein Benutzer-Namensraum?
2. Warum ist Rootless sicherer als ein Container als root (Fachwissen)?
3. Was steht in `/etc/subuid`?
4. Welche Einschränkungen hat Rootless (Fachwissen)?

### Modul 3: Pods, Volumes und Netzwerke

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Pod anlegen und das gemeinsame Netzwerk erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Volumes und Bind-Mounts unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Netzwerk anlegen und Container über den Namen verbinden.
  * Nach Abschluss dieses Moduls kann der Lernende Persistenz für einen Dienst planen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Pod: gemeinsames Netzwerk zweier Container (`pods_volumes_netze.sh`) | 4 |
| 3.2 | Volumes und Bind-Mounts, Nur-Lesen (`pods_volumes_netze.sh`) | 4 |
| 3.3 | Eigenes Netzwerk und Namensauflösung (`pods_volumes_netze.sh`) | 3 |
| 3.4 | Persistenz und Netz für ein Beispieldienst planen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Pod (Einheit 3.1):** Führen Sie `bash pods_volumes_netze.sh` aus. Erklären Sie Schritt 1: Warum erreicht der Client den Server über `localhost`? Warum zeigt der Pod 2 Container, obwohl nur einer gestartet wurde?
2. **Volume und Bind-Mount (Einheit 3.2):** Erklären Sie die Schritte 2 und 3: Wo liegen die Daten, und was bewirkt `:ro`?
3. **Netzwerk (Einheit 3.3):** Erklären Sie Schritt 4: Wie findet der Client den Server `srv` über den Namen?
4. **Planen (Einheit 3.4):** Planen Sie für einen Dienst mit Datenbank und Webanwendung Volumes, Netzwerk und Ports und begründen Sie die Wahl.

#### Kontrollfragen

1. Was teilen sich Container eines Pods?
2. Worin unterscheiden sich Volume und Bind-Mount?
3. Wozu dient `:ro`?
4. Wie sprechen Container in einem eigenen Netzwerk einander an?

### Modul 4: Images bauen und prüfen: Containerfile, Buildah, Skopeo

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Image mit einem Containerfile bauen und seine Ebenen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende dasselbe Ziel mit Buildah schrittweise erreichen.
  * Nach Abschluss dieses Moduls kann der Lernende Images mit Skopeo kopieren und inspizieren.
  * Nach Abschluss dieses Moduls kann der Lernende Registry-Befehle nennen und ihre Voraussetzungen beschreiben.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Image mit `Containerfile` bauen, Ebenen lesen (`images_bauen.sh`) | 4 |
| 4.2 | Mit `buildah` ein Image schrittweise erzeugen (`images_bauen.sh`) | 3 |
| 4.3 | Mit `skopeo` Images ohne Registry kopieren und prüfen (`images_bauen.sh`) | 3 |
| 4.4 | Registries, Anmeldung und `pull`/`push`: Befehle (Fachwissen, nicht ausgeführt) | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Containerfile (Einheit 4.1):** Führen Sie `bash images_bauen.sh` aus. Erklären Sie jede Zeile des Containerfiles und die Ausgabe von `podman history` in Schritt 2.
2. **Buildah (Einheit 4.2):** Erklären Sie Schritt 4: Welche Schritte entsprechen `FROM`, `RUN` und dem Abschluss des Builds?
3. **Skopeo (Einheit 4.3):** Erklären Sie Schritt 5: Was sind die Transporte `dir:` und `oci:`, und was zeigt die Ausgabe zu Architektur und Ebenen?
4. **Registry (Einheit 4.4):** Schreiben Sie die Befehle für Anmelden, Markieren, Hochladen und Herunterladen eines Images auf; kennzeichnen Sie, was Sie nicht geprüft haben, und führen Sie sie auf `pod01` aus.

#### Kontrollfragen

1. Wie viele Ebenen entstehen durch `COPY` und `RUN` (Fachwissen)?
2. Wozu dient `skopeo copy`?
3. Was ist ein OCI-Layout?
4. Warum sollte ein Image nicht mit `latest` referenziert werden (Fachwissen)?

### Modul 5: systemd-Einbindung mit Quadlet

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Quadlet-Dateien für Container, Volume und Netzwerk schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die vom Generator erzeugten systemd-Units lesen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie Abhängigkeiten zwischen den Units entstehen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Quadlet-Dateien (`.container`, `.volume`, `.network`) schreiben (`quadlet.sh`) | 4 |
| 5.2 | Probelauf des Generators lesen: erzeugte Units (`quadlet.sh`) | 4 |
| 5.3 | Dienste mit `systemctl` steuern (Fachwissen, nicht ausgeführt) | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dateien lesen (Einheit 5.1):** Führen Sie `bash quadlet.sh` aus. Erklären Sie jede Zeile der drei Quadlet-Dateien.
2. **Units lesen (Einheit 5.2):** Erklären Sie die Auszüge der Schritte 2 und 3: Woher stammen `Requires`/`After`, und welcher Befehl wird zum Starten verwendet?
3. **Betrieb (Einheit 5.3):** Beschreiben Sie, wie Sie auf `pod01` die Dateien installieren, `systemctl daemon-reload` ausführen und den Dienst starten. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Wozu dient Quadlet?
2. Wie heißt die erzeugte Unit zu `web.container`?
3. Was bewirkt `WantedBy=multi-user.target`?
4. Wo liegen Quadlet-Dateien für Rootless (Fachwissen)?

### Modul 6: Mehrere Container: Kubernetes-YAML und Compose

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende aus einem Pod eine YAML-Datei erzeugen und daraus neu starten.
  * Nach Abschluss dieses Moduls kann der Lernende eine Compose-Datei lesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Zusammenhang zu Kubernetes beschreiben.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Pod als YAML erzeugen und abspielen (`kube.sh`) | 4 |
| 6.2 | Compose-Datei lesen (`compose.yaml`, nicht ausgeführt) | 3 |
| 6.3 | Kubernetes als Ausblick | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **YAML erzeugen (Einheit 6.1):** Führen Sie `bash kube.sh` aus. Erklären Sie die Auszüge der YAML-Datei und was `kube play` bzw. `kube down` bewirken.
2. **Compose lesen (Einheit 6.2):** Lesen Sie `compose.yaml` und `beispiel_compose.txt` und beschreiben Sie, welche Podman-Befehle den Einträgen entsprechen.
3. **Ausblick (Einheit 6.3):** Beschreiben Sie in fünf Sätzen, was Kubernetes über Podman hinaus leistet (Fachwissen) und welche Grenzen `kube play` hat.

#### Kontrollfragen

1. Wozu dient `podman generate kube`?
2. Welche Rolle hat `kube play`?
3. Worin unterscheidet sich Compose von einer Pod-YAML (Fachwissen)?

### Modul 7: Container-Sicherheit

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Capabilities eines Containers lesen und gezielt entfernen.
  * Nach Abschluss dieses Moduls kann der Lernende Nur-Lesen, `no-new-privileges` und `--user` einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende seccomp-Filter erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Image-Signaturen, SELinux/AppArmor und Schwachstellenscans einordnen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Capabilities entfernen und Wirkung beobachten (`sicherheit.sh`) | 3 |
| 7.2 | Nur-Lesen-Dateisystem, `no-new-privileges`, Benutzer (`sicherheit.sh`) | 3 |
| 7.3 | seccomp: Standardprofil gegen `unconfined` (`sicherheit.sh`) | 3 |
| 7.4 | Richtlinie für Signaturen, SELinux/AppArmor, Schwachstellenscan: Überblick (Fachwissen, nicht ausgeführt) | 5 |

#### Praxisaufgaben (Hands-on Lab)

1. **Capabilities (Einheit 7.1):** Führen Sie `bash sicherheit.sh` aus. Erklären Sie Schritt 1 und 2: Was zeigt `CapEff`, und warum scheitert `chown` ohne `CAP_CHOWN`?
2. **Härtung (Einheit 7.2):** Erklären Sie die Schritte 3, 4 und 6: Was bewirken `--read-only`, `no-new-privileges` und `--user`?
3. **seccomp (Einheit 7.3):** Erklären Sie Schritt 5: Was bedeutet `Seccomp=2` gegenüber `Seccomp=0`?
4. **Konzept (Einheit 7.4):** Schreiben Sie ein Sicherheitskonzept für einen Container (Benutzer, Capabilities, Dateisystem, Images, Signaturen). Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Was ist eine Capability?
2. Warum sollte ein Container nicht als root laufen?
3. Was macht ein seccomp-Filter?
4. Wozu dient eine Richtlinie in `policy.json`?

### Modul 8: Ressourcenlimits und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Speicher- und Prozesslimits für einen Container setzen und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende das Überschreiten eines Limits erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehlermeldungen zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine systematische Fehlersuche durchführen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Speicher- und Prozesslimits (`limits_fehler.sh`) | 4 |
| 8.2 | Überschreiten des Speicherlimits beobachten (`limits_fehler.sh`) | 2 |
| 8.3 | Typische Fehlermeldungen lesen (`limits_fehler.sh`) | 4 |
| 8.4 | Ablaufplan für die Fehlersuche | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Limits (Einheit 8.1):** Führen Sie `bash limits_fehler.sh` aus. Erklären Sie die Schritte 1 und 2: Woher stammt der Wert 67108864, und was meldet `sh` bei `--pids-limit`?
2. **OOM (Einheit 8.2):** Erklären Sie Schritt 3: Warum endet der Container mit 137, und was fällt an `OOMKilled=false` auf?
3. **Fehlermeldungen (Einheit 8.3):** Ordnen Sie die Fehler aus Schritt 4 den Ursachen zu und nennen Sie jeweils die Abhilfe.
4. **Ablaufplan (Einheit 8.4):** Schreiben Sie einen Ablaufplan „Container startet nicht“ mit der Reihenfolge der Prüfungen (`ps -a`, `logs`, `inspect`, Image, Ports).

#### Kontrollfragen

1. Welcher Wert entspricht `--memory 64m` in Byte?
2. Was bewirkt `--pids-limit`?
3. Welcher Exitcode zeigt einen nicht gefundenen Befehl?
4. Wie lässt sich ein belegter Name vermeiden?
