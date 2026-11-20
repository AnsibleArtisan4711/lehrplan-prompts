# Lehrplan: Kubernetes-Grundlagen

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Docker-Grundlagen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Architektur von Kubernetes, Pods, Deployments und Services, ConfigMaps und Secrets, Volumes, Ingress, Namespaces und Rechte (RBAC), Updates und Rollbacks, lokale Umgebung (kubeadm, k3s, kind, minikube), Fehlersuche, Einordnung gegenüber Docker Compose |
| **Thematische Abgrenzung (Out of Scope)** | **Kubernetes wurde nicht ausgeführt:** Im Cloud-Container gibt es weder `kubectl` noch `kubeadm`, `k3s`, `kind` oder `minikube`. **Echt ausgeführt** sind nur (1) die **Prüfung der Manifeste mit `kubernetes-validate` 1.37.0 gegen das Schema von Kubernetes 1.31 (streng)**, (2) die Docker-Nachstellung eines Pods mit gemeinsamem Netz-Namespace (Modul 1), (3) `base64` und Abfragen des Rechners. **Der Cluster ist ein Lernmodell in Python** (`k8ssim.py`: Planung, Deployments mit Rolling Update, Dienste, Ingress-Regeln, einfaches RBAC); es bildet das echte Verhalten nur vereinfacht ab und wurde nicht gegen einen echten Cluster geprüft. Die Kubernetes-Dokumentation wurde nicht gelesen; Aussagen dazu sind Fachwissen. Helm, Operatoren, StatefulSets, Netzwerkrichtlinien und Cloud-Dienste sind nicht Teil dieses Kurses. Docker und Compose stehen im Kurs P25. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Architektur und Konzepte | 1 | 12 |
| 2 | Pods, ReplicaSets und Deployments | 1 | 14 |
| 3 | Services und Netzwerk | 1 | 12 |
| 4 | ConfigMaps, Secrets und Volumes | 1 | 12 |
| 5 | Namespaces und Ingress | 1 | 12 |
| 6 | Rechte mit RBAC | 1 | 12 |
| 7 | Lokale Umgebung: kubeadm, k3s, kind, minikube | 2 | 8 |
| 8 | Updates, Rollbacks, Fehlersuche, Einordnung und Abschlussprojekt | 1 | 18 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (lokale Umgebung: kubeadm, k3s, kind, minikube). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 92 UE; kein Pflichtmodul setzt Modul 7 voraus, die Übungen laufen mit dem Modell. Im Hyper-V-Labor wird Modul 7 jedoch gebraucht, wenn ein echter Cluster entstehen soll.

### 2. Quellen

**Quellen:** Es wurden **keine** Seiten der Kubernetes-Dokumentation gelesen. Alle Aussagen zu Architektur und Verhalten sind Fachwissen und im Text als solches gekennzeichnet. Die Schemaprüfung stützt sich auf `kubernetes-validate` 1.37.0 (pip) mit dem Schema 1.31; sie prüft die Form eines Manifests, nicht den Betrieb.

**Getestet mit (Ubuntu 24.04, Cloud-Container):** Python 3.13 mit PyYAML und kubernetes-validate 1.37.0, Docker Engine 29.9.2 (nur Modul 1 und Teil von Modul 8), Modell `k8ssim.py`. **Nicht ausgeführt:** Kubernetes selbst, kubectl, kubeadm, k3s, kind, minikube, ein Ingress-Controller, Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-K8s`, `10.80.0.0/24`).

**VM 1:** `cp1` (**erforderlich**, `10.80.0.10`): Linux, Control-Plane-Knoten (Annahme: mindestens 2 CPU und 2 GiB RAM).

**VM 2:** `w1` (**erforderlich**, `10.80.0.11`): Linux, Arbeitsknoten.

**VM 3:** `w2` (**optional**, `10.80.0.12`): zweiter Arbeitsknoten.

**Internetphase:** Zum Installieren und zum Laden von Images brauchen die VMs vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 7 und Modul 8 von allen VMs einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux mit dem Modell `k8ssim.py` und arbeiten unter `/tmp/p26`; sie brauchen die VMs nicht. Im Labor ersetzt man die Modell-Befehle durch `kubectl` (nicht geprüft).

## B. Detaillierter Modulaufbau

### Modul 1: Architektur und Konzepte

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Bausteine von Control Plane und Knoten nennen.
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip „Sollzustand beschreiben, Controller stellen ihn her“ erklären.
  * Nach Abschluss dieses Moduls kann der Lernende zeigen, dass Container eines Pods ein Netz teilen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Manifest mit dem Schema prüfen.
* **Voraussetzungen:** Docker-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Bausteine | 4 |
| 1.2 | Pod und Netz | 4 |
| 1.3 | Schema | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bausteine (Einheit 1.1):** Führen Sie `bash architektur.sh` aus. Nennen Sie anhand von Schritt 1 und 2 die Bausteine und die Knoten des Modell-Clusters.
2. **Pod und Netz (Einheit 1.2):** Erklären Sie Schritt 3: Was zeigt die Docker-Nachstellung über einen Pod?
3. **Schema (Einheit 1.3):** Erklären Sie Schritt 4: Warum wird `pod-fehler.yaml` abgelehnt?

#### Kontrollfragen

1. Welche Knoten hat das Modell?
2. Was zeigt Schritt 3?
3. Warum ist `pod-fehler.yaml` ungültig?
4. Was ist die Grundidee von Kubernetes?

### Modul 2: Pods, ReplicaSets und Deployments

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Kette Deployment, ReplicaSet, Pod erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Selbstheilung und Skalierung beobachten.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten bei Knotenausfall beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Ressourcenanforderungen (requests) und ihre Wirkung auf die Planung deuten.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Kette | 6 |
| 2.2 | Heilen und skalieren | 4 |
| 2.3 | Planung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kette (Einheit 2.1):** Führen Sie `bash deployments.sh` aus. Erklären Sie Schritt 1 und 2: Welche Objekte entstehen, und wie sind die Pods verteilt?
2. **Heilen und skalieren (Einheit 2.2):** Erklären Sie Schritt 3 bis 5: Was geschieht beim Löschen eines Pods, beim Skalieren und beim Ausfall von `w1`?
3. **Planung (Einheit 2.3):** Erklären Sie Schritt 6: Warum bleibt der Pod „Unschedulable“?

#### Kontrollfragen

1. Wie erkennt man den Schemafehler `replicas: "drei"`?
2. Warum steht kein Pod auf `cp1`?
3. Was geschieht bei Ausfall von `w1`?
4. Wie lautet die Meldung bei zu großer Anforderung?

### Modul 3: Services und Netzwerk

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wie ein Service Pods über Labels auswählt.
  * Nach Abschluss dieses Moduls kann der Lernende Endpunkte lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler durch falsche Selektoren erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Dienst-Typen unterscheiden.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Auswahl | 4 |
| 3.2 | Skalierung | 4 |
| 3.3 | Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auswahl (Einheit 3.1):** Führen Sie `bash services.sh` aus. Erklären Sie Schritt 1 und 2: Wie wählt der Service Pods, und wie werden Anfragen verteilt?
2. **Skalierung (Einheit 3.2):** Erklären Sie Schritt 3: Wie ändern sich die Endpunkte?
3. **Fehler (Einheit 3.3):** Erklären Sie Schritt 4 und 5: Warum findet das Schema den Selektor-Fehler nicht?

#### Kontrollfragen

1. Wie viele Endpunkte hat `web` anfangs?
2. Wie werden Anfragen verteilt?
3. Was meldet ein Dienst ohne passenden Pod?
4. Wie unterscheidet sich ein Headless-Service?

### Modul 4: ConfigMaps, Secrets und Volumes

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ConfigMap und Secret unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende zeigen, dass base64 keine Verschlüsselung ist.
  * Nach Abschluss dieses Moduls kann der Lernende Verweise auf Konfiguration in Umgebungsvariablen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Volume-Arten im Schema erkennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Secret | 4 |
| 4.2 | Umgebung | 4 |
| 4.3 | Fehlender Verweis | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Secret (Einheit 4.1):** Führen Sie `bash konfig.sh` aus. Erklären Sie Schritt 1: Warum schützt base64 das Secret nicht?
2. **Umgebung (Einheit 4.2):** Erklären Sie Schritt 3: Woher stammen die Werte der Umgebungsvariablen?
3. **Fehlender Verweis (Einheit 4.3):** Erklären Sie Schritt 4: Was findet das Schema, was nicht?

#### Kontrollfragen

1. Wie lautet der dekodierte Wert?
2. Welche Variablen sieht der Pod?
3. Was meldet das Modell bei einer fehlenden ConfigMap?
4. Welche Volume-Arten kommen vor?

### Modul 5: Namespaces und Ingress

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Namespaces zur Trennung von Namen einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Ingress-Regeln für Host und Pfad lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Pfadtypen Prefix und Exact unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende veraltete API-Versionen erkennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Namespaces | 4 |
| 5.2 | Ingress | 4 |
| 5.3 | Veraltet | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Namespaces (Einheit 5.1):** Führen Sie `bash ingress.sh` aus. Erklären Sie Schritt 1: Wie kann `web` in `dev` und `prod` verschieden sein?
2. **Ingress (Einheit 5.2):** Erklären Sie Schritt 2 bis 4: Wie wird jede Anfrage aufgelöst, und was bedeutet 404 und 503?
3. **Veraltet (Einheit 5.3):** Erklären Sie Schritt 5: Was meldet die Prüfung bei `extensions/v1beta1`?

#### Kontrollfragen

1. Wie viele Pods hat `web` in `dev` und in `prod`?
2. Wohin geht `/api/benutzer`?
3. Was geschieht mit `/status/x`?
4. Was meldet die Prüfung bei der alten API-Version?

### Modul 6: Rechte mit RBAC

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Role, ClusterRole und die zugehörigen Bindungen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Berechtigungen mit `can-i` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip „ohne Regel verboten“ erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen der Schemaprüfung bei Rechten benennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Rollen | 4 |
| 6.2 | Rechte prüfen | 4 |
| 6.3 | Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rollen (Einheit 6.1):** Führen Sie `bash rbac.sh` aus. Erklären Sie Schritt 1: Welche Objekte entstehen?
2. **Rechte prüfen (Einheit 6.2):** Erklären Sie Schritt 2: Warum darf `alice` Pods lesen, aber nicht in `prod` und keine Secrets?
3. **Fehler (Einheit 6.3):** Erklären Sie Schritt 3: Welcher Fehler fällt dem Schema auf, welcher nicht?

#### Kontrollfragen

1. Welche Rechte hat `alice`?
2. Warum darf `bob` Knoten lesen, aber keine Pods?
3. Was ist der Standard ohne Regel?
4. Welchen Fehler findet das Schema nicht?

### Modul 7: Lokale Umgebung: kubeadm, k3s, kind, minikube

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Möglichkeiten für einen lokalen Cluster unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen eines Rechners abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende den Laborplan mit zwei bis drei VMs beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Nichtgeprüftes als solches benennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Werkzeuge | 4 |
| 7.2 | Vergleich | 2 |
| 7.3 | Plan | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Werkzeuge (Einheit 7.1):** Führen Sie `bash umgebung.sh` aus. Erklären Sie Schritt 1 und 2: Was ist vorhanden, was nicht, und was gilt nur für diesen Rechner?
2. **Vergleich (Einheit 7.2):** Geben Sie Schritt 3 in eigenen Worten wieder.
3. **Plan (Einheit 7.3):** Beschreiben Sie anhand von Schritt 4 das Labor.

#### Kontrollfragen

1. Welche Kubernetes-Werkzeuge sind auf dem Rechner vorhanden?
2. Welche Voraussetzungen wurden abgefragt?
3. Wofür eignet sich kind?
4. Wie sieht der Laborplan aus?

### Modul 8: Updates, Rollbacks, Fehlersuche, Einordnung und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 18 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Rolling Update und seine Schritte beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Fehlstart (ImagePullBackOff) erkennen und die Ursache aus den Ereignissen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Rollback durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Kubernetes und Docker Compose einordnen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Update | 6 |
| 8.2 | Fehlersuche und Rollback | 6 |
| 8.3 | Einordnung und Abschluss | 6 |

#### Praxisaufgaben (Hands-on Lab)

1. **Update (Einheit 8.1):** Führen Sie `bash updates.sh` aus. Erklären Sie Schritt 1 und 2: Warum bleiben beim Update auf ein nicht vorhandenes Image drei alte Pods laufen?
2. **Fehlersuche und Rollback (Einheit 8.2):** Erklären Sie Schritt 3 und 4: Welche Ereignisse zeigt der fehlerhafte Pod, und wie ändert der Rollback die Versionsliste?
3. **Einordnung und Abschluss (Einheit 8.3):** Führen Sie `bash vergleich.sh` und `bash abschluss.sh` aus. Vergleichen Sie Compose und Kubernetes, und erklären Sie die Abnahme des Shops.

#### Kontrollfragen

1. Wie viele Pods sind beim fehlgeschlagenen Update bereit?
2. Was zeigt `describe` des fehlerhaften Pods?
3. Wie lautet die Versionsliste nach dem Rollback?
4. Wann genügt Compose?
