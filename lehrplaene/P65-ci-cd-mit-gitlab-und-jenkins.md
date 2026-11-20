# Lehrplan: CI/CD mit GitLab und Jenkins

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Linux-Grundlagen (Kommandozeile, Bash); Git-Grundlagen (Commit, Push, Zweige); Grundlagen der Softwareentwicklung (Tests, Build) |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Pipelines und Stufen, Git-Abläufe und serverseitige Hooks, Aufbau einer `.gitlab-ci.yml`, Variablen, Artefakte und Cache, Jenkinsfile im Überblick, Tests und Qualitätstore, Auslieferung mit Rückfall, Betrieb und Kennzahlen |
| **Thematische Abgrenzung (Out of Scope)** | GitLab und Jenkins werden **nicht** betrieben: Die Übungen nutzen Bash, Git und einen eigenen kleinen Läufer als Modell. Nicht behandelt: Container-Builds in Pipelines, Kubernetes-Deployments, Cloud-Dienste, Runner-Verwaltung, Plugin-Entwicklung. Lizenzen und Versionen von GitLab und Jenkins: mit Stand prüfen (nicht recherchiert) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Pipeline-Grundlagen | 1 | 10 |
| 2 | Git-Abläufe und Hooks | 1 | 14 |
| 3 | Die Datei .gitlab-ci.yml | 1 | 14 |
| 4 | Variablen, Artefakte und Cache | 1 | 12 |
| 5 | Jenkinsfile im Überblick | 2 | 12 |
| 6 | Tests und Qualitätstore | 1 | 14 |
| 7 | Auslieferung und Rückfall | 1 | 12 |
| 8 | Betrieb und Abschlussprojekt | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 4 und 6 bis 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 5 (Jenkinsfile im Überblick). Fällt Modul 5 weg, verringert sich der Gesamtumfang auf 88 UE; kein Pflichtmodul setzt Modul 5 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von GitLab CI/CD und Jenkins wurde **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt. Namen, Zahlen und Werte sind erfunden.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** Bash, Git (zentrales Repository mit Hooks), Python 3 mit PyYAML (Läufer-Modell, `unittest`). **Nicht ausgeführt:** GitLab, GitLab Runner, Jenkins, Docker-Builds, Plugins.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-CICD`, `10.65.0.0/24`).

**VM 1:** `ci01` (**erforderlich**, `10.65.0.2`): Linux-Server mit `git`, `bash` und Python 3 (PyYAML).

**VM 2 (optional):** `gitlab01` (`10.65.0.10`): eigene GitLab-Installation; **nicht** Teil der geprüften Übungen. Ebenso optional: `jenkins01` (`10.65.0.11`) für Modul 5.

**Internetphase:** Für die Installation der Pakete braucht `ci01` vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 2 von `ci01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Alles läuft unter `/tmp/p65`; Git nutzt eine eigene Konfigurationsdatei dort und verändert `~/.gitconfig` nicht.

## B. Detaillierter Modulaufbau

### Modul 1: Pipeline-Grundlagen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Stufen, Rückgabecodes und Abbruch bei Fehlern erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine kleine Pipeline in Bash schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende unkritische Stufen mit erlaubtem Fehler behandeln.
  * Nach Abschluss dieses Moduls kann der Lernende Protokolle je Stufe ablegen.
* **Voraussetzungen:** Bash-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Pipeline lesen | 4 |
| 1.2 | Fehlerfall | 2 |
| 1.3 | Erlaubter Fehler | 2 |
| 1.4 | Protokolle | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Pipeline lesen (Einheit 1.1):** Führen Sie `bash pipeline.sh` aus. Erklären Sie, wie die Funktion `lauf` die Rückgabecodes auswertet.
2. **Fehlerfall (Einheit 1.2):** Erklären Sie Schritt 2: Welche Stufen laufen nicht mehr, und welchen Rückgabecode hat die Pipeline?
3. **Erlaubter Fehler (Einheit 1.3):** Erklären Sie Schritt 3: Warum darf `lint` scheitern, `test` aber nicht?
4. **Protokolle (Einheit 1.4):** Ergänzen Sie eine Stufe `doku`, die immer läuft, und legen Sie ihr Protokoll ab.

#### Kontrollfragen

1. Was bedeutet Rückgabecode 0?
2. Warum bricht eine Pipeline bei einem Fehler ab?
3. Wozu `allow_failure`?
4. Warum Protokolle je Stufe?

### Modul 2: Git-Abläufe und Hooks

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein zentrales (bare) Repository und eine Arbeitskopie einrichten.
  * Nach Abschluss dieses Moduls kann der Lernende mit `pre-receive` Regeln auf dem Server durchsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende mit `post-receive` einen Lauf anstoßen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Zweig mit Merge nachvollziehen.
* **Voraussetzungen:** Modul 1; Git-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Zentrales Repository | 5 |
| 2.2 | pre-receive | 3 |
| 2.3 | post-receive | 3 |
| 2.4 | Zweige | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zentrales Repository (Einheit 2.1):** Führen Sie `bash git_hooks.sh` aus. Erklären Sie Schritt 1: Was ist ein „bare“-Repository, und warum gibt es keine Arbeitsdateien?
2. **pre-receive (Einheit 2.2):** Erklären Sie Schritt 2 und 3: Warum wird der erste Push abgelehnt, und wie korrigiert man den Commit?
3. **post-receive (Einheit 2.3):** Erklären Sie Schritt 4: Was passiert nach einem erfolgreichen Push?
4. **Zweige (Einheit 2.4):** Beschreiben Sie anhand von Schritt 5, was `--no-ff` am Verlauf ändert.

#### Kontrollfragen

1. Wo laufen serverseitige Hooks?
2. Warum reicht ein clientseitiger Hook nicht?
3. Was bewirkt `git commit --amend`?
4. Was bewirkt `--no-ff`?

### Modul 3: Die Datei .gitlab-ci.yml

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Stufen und Jobs einer `.gitlab-ci.yml` lesen und schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler wie unbekannte Stufen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende das Verhalten bei Fehlern (Abbruch, `when: always`) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Modell und echtes GitLab unterscheiden.
* **Voraussetzungen:** Modul 1; Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Datei lesen | 5 |
| 3.2 | Prüfung | 3 |
| 3.3 | Fehlerfall | 3 |
| 3.4 | Eigene Pipeline | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Datei lesen (Einheit 3.1):** Führen Sie `bash gitlab_ci.sh` aus. Erklären Sie die drei Jobs und ihre Stufen in Schritt 1 und 2.
2. **Prüfung (Einheit 3.2):** Erklären Sie Schritt 3: Welche zwei Fehler findet der Läufer, und welcher Rückgabecode zeigt einen Fehler in der Datei?
3. **Fehlerfall (Einheit 3.3):** Erklären Sie Schritt 4: Warum läuft `bauen` nicht, `aufraeumen` aber doch?
4. **Eigene Pipeline (Einheit 3.4):** Schreiben Sie eine `ci.yml` mit Stufen `pruefen` und `paket` für ein eigenes Beispiel und führen Sie sie mit `runner.py` aus.

#### Kontrollfragen

1. Was ist eine Stufe (stage)?
2. Was bewirkt `when: always`?
3. Ist `runner.py` ein GitLab Runner?
4. Woran erkennt man eine fehlerhafte Datei?

### Modul 4: Variablen, Artefakte und Cache

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende globale und Job-Variablen einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Artefakte zwischen Jobs weitergeben.
  * Nach Abschluss dieses Moduls kann der Lernende Cache-Schlüssel aus einer Sperrdatei bilden.
  * Nach Abschluss dieses Moduls kann der Lernende Artefakt und Cache unterscheiden.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Variablen | 3 |
| 4.2 | Artefakt | 3 |
| 4.3 | Cache | 3 |
| 4.4 | Vergleich | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Variablen (Einheit 4.1):** Führen Sie `bash variablen_artefakte.sh` aus. Erklären Sie, warum der Job `pruefen` die Umgebung `abnahme` meldet.
2. **Artefakt (Einheit 4.2):** Erklären Sie, wie die Datei `dist/paket.txt` zum zweiten Job kommt.
3. **Cache (Einheit 4.3):** Erklären Sie Schritt 2 bis 4: Wann trifft der Cache, wann nicht?
4. **Vergleich (Einheit 4.4):** Erklären Sie Schritt 5 und nennen Sie ein Beispiel, bei dem ein Cache ohne Gefahr fehlen darf.

#### Kontrollfragen

1. Welche Variable gilt, wenn sie global und im Job gesetzt ist?
2. Was ist ein Artefakt?
3. Woraus entsteht der Cache-Schlüssel?
4. Warum darf ein Cache fehlen?

### Modul 5: Jenkinsfile im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines deklarativen Jenkinsfiles lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Pflichtblöcke und Stufen formal prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende GitLab CI und Jenkins gegenüberstellen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Aufbau | 4 |
| 5.2 | Prüfung | 4 |
| 5.3 | Gegenüberstellung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbau (Einheit 5.1):** Führen Sie `bash jenkins.sh` aus. Beschreiben Sie anhand von Schritt 1 die Blöcke `pipeline`, `agent`, `stages`, `stage`, `steps` und `post`.
2. **Prüfung (Einheit 5.2):** Erklären Sie Schritt 2 und 3: Welche drei Fehler findet das Lernwerkzeug in der kaputten Fassung?
3. **Gegenüberstellung (Einheit 5.3):** Ergänzen Sie die Gegenüberstellung aus Schritt 4 um zwei weitere Unterschiede aus eigener Recherche und kennzeichnen Sie sie als nicht geprüft.

#### Kontrollfragen

1. Wozu dient `agent`?
2. Was bewirkt `post { failure { … } }`?
3. Wie viele Fehler findet das Lernwerkzeug in der kaputten Fassung?
4. Warum ist ein Klartext-Zugangswert im Jenkinsfile ein Fehler?

### Modul 6: Tests und Qualitätstore

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Syntax- und Unittests in einer Pipeline ausführen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Testfehler lesen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Qualitätstor vor dem Bauen einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Mindestanzahl Tests prüfen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Syntax | 5 |
| 6.2 | Unittests | 3 |
| 6.3 | Fehlerfall | 3 |
| 6.4 | Mindestanzahl | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Syntax (Einheit 6.1):** Führen Sie `bash tests.sh` aus. Erklären Sie Schritt 1: Was prüfen die Python-Syntaxprüfung und `bash -n`, und was nicht?
2. **Unittests (Einheit 6.2):** Erklären Sie Schritt 2: Welche vier Tests laufen, und was zeigt „OK“?
3. **Fehlerfall (Einheit 6.3):** Erklären Sie Schritt 3 und 4: Welche Tests schlagen fehl, warum nicht alle, und warum entsteht kein Paket?
4. **Mindestanzahl (Einheit 6.4):** Schreiben Sie einen fünften Test für Prozent 50 und prüfen Sie die Mindestanzahl neu.

#### Kontrollfragen

1. Was prüft `bash -n`?
2. Was bedeutet `FAILED (failures=2)`?
3. Warum schlägt `test_null` nicht fehl?
4. Wozu ein Qualitätstor?

### Modul 7: Auslieferung und Rückfall

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Releases in Ordnern ablegen und per Symlink umschalten.
  * Nach Abschluss dieses Moduls kann der Lernende eine Gesundheitsprüfung mit Rückfall (Rollback) verbinden.
  * Nach Abschluss dieses Moduls kann der Lernende alte Releases aufräumen.
  * Nach Abschluss dieses Moduls kann der Lernende Geheimnisse in Protokollen maskieren.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Umschalten | 3 |
| 7.2 | Rückfall | 3 |
| 7.3 | Aufräumen | 3 |
| 7.4 | Verbesserung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Umschalten (Einheit 7.1):** Führen Sie `bash deployment.sh` aus. Erklären Sie, warum `mv -T` das Umschalten atomar macht.
2. **Rückfall (Einheit 7.2):** Erklären Sie Schritt 3: Wie erkennt das Skript das fehlerhafte Release, und was passiert?
3. **Aufräumen (Einheit 7.3):** Erklären Sie Schritt 5: Warum bleibt Release 3 erhalten, obwohl es fehlerhaft war?
4. **Verbesserung (Einheit 7.4):** Schlagen Sie vor, wie man fehlerhafte Releases beim Aufräumen zuerst entfernt, und beschreiben Sie die Änderung.

#### Kontrollfragen

1. Warum Release-Ordner?
2. Was ist ein Symlink-Wechsel?
3. Warum eine Gesundheitsprüfung?
4. Warum darf das aktive Release nie gelöscht werden?

### Modul 8: Betrieb und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Verlauf einer Pipeline auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Kennzahlen wie Erfolgsquote und Abstand bis zur Behebung berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler der fehlgeschlagenen Stufe zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abschlussprojekt planen.
* **Voraussetzungen:** Modul 2; Modul 6; Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Läufe | 3 |
| 8.2 | Kennzahlen | 3 |
| 8.3 | Fehleranalyse | 3 |
| 8.4 | Abschlussprojekt | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Läufe (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1: Welche Läufe sind fehlgeschlagen, und in welcher Stufe?
2. **Kennzahlen (Einheit 8.2):** Erklären Sie Schritt 2: Wie sind Erfolgsquote und Abstand definiert?
3. **Fehleranalyse (Einheit 8.3):** Erklären Sie Schritt 3: Warum werden `paket` und `ausliefern` übersprungen?
4. **Abschlussprojekt (Einheit 8.4):** Setzen Sie die Aufgabenliste aus Schritt 4 auf Ihrem Labor um und schreiben Sie einen Kurzbericht mit offenen Punkten.

#### Kontrollfragen

1. Wie berechnet man die Erfolgsquote?
2. Wozu die Fehler je Stufe?
3. Warum werden Folgestufen übersprungen?
4. Was gehört in den Kurzbericht?
