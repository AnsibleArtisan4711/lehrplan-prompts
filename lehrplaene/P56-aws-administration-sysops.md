# Lehrplan: AWS Administration (SysOps)

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen; Cloud-Grundlagen (z. B. AWS Cloud Practitioner); Grundkenntnisse in Netzwerken |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | AWS (EC2, VPC, IAM, S3, CloudWatch, CloudFormation), AWS CLI; Konten und IAM; VPC; EC2, Auto Scaling und Load Balancing; Speicher (EBS, S3, EFS); Datenbanken im Betrieb (RDS); Überwachung mit CloudWatch; Automatisierung mit AWS CLI und CloudFormation; Sicherung, Kostenkontrolle, Sicherheit und Fehlersuche |
| **Thematische Abgrenzung (Out of Scope)** | AWS Cloud Practitioner ist ein eigener vorhandener Lehrplan dieses Repositories; Terraform ist ein eigener Kurs. Nicht behandelt: Container-Dienste (ECS/EKS), Serverless im Detail, Organisationen mit mehreren Konten |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Konten und IAM | 1 | 12 |
| 2 | VPC und Netzwerkaufbau | 1 | 14 |
| 3 | EC2, Auto Scaling und Load Balancing | 1 | 14 |
| 4 | Speicher: EBS, S3 und EFS | 1 | 12 |
| 5 | Datenbanken im Betrieb mit RDS | 2 | 10 |
| 6 | Überwachung mit CloudWatch | 1 | 12 |
| 7 | Automatisierung mit CLI und CloudFormation | 1 | 14 |
| 8 | Kostenkontrolle, Sicherheit und Fehlersuche | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 4 und 6 bis 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 5 (Datenbanken im Betrieb mit RDS). Fällt Modul 5 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 5 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von AWS (IAM, VPC, EC2, S3, RDS, CloudWatch, CloudFormation, AWS CLI) wurde **nicht** gelesen. Alle fachlichen Aussagen, Standardwerte und CLI-Befehle stammen aus Fachwissen und sind **nicht bestätigt**; verbindlich ist die aktuelle AWS-Dokumentation. **Kosten, Preise und Gratis-Kontingente wurden nicht recherchiert**: die Preise in den Modellen sind **erfunden**; echte Preise und Kontingente sind mit Stand zu prüfen.

**Ausgeführt wurden ausschließlich die Python-Modelle** (Python 3 im Cloud-Container): reine Rechnungen mit erfundenen Werten, vereinfacht (z. B. IAM nur mit Aktion und Ressource, kein Abkühlzeit-Verhalten beim Auto Scaling). **Nicht ausgeführt:** AWS-Konto, AWS CLI, CloudFormation. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Konto:** ein kostenloses oder budgetbegrenztes AWS-Konto **mit Budgetwarnung** (vor jeder Übung einrichten; Kostenmodelle und Gratis-Kontingente mit Stand prüfen). **Client:** eine Linux-VM `cli01` mit installierter AWS CLI und einem Benutzer mit Zugangsdaten (**keine** Zugangsschlüssel des Root-Benutzers; Schlüssel nie in Dateien eines Repositories speichern).

**Aufräumen:** Nach jeder Übung angelegte Ressourcen (Instanzen, Volumes, Elastic IPs, Datenbanken, Load Balancer, NAT-Gateways) löschen; viele davon verursachen Kosten, auch wenn sie nicht genutzt werden (Fachwissen, mit Stand prüfen).

**Skripte:** Die Python-Modelle laufen auf jedem Rechner mit Python 3, auch ohne AWS-Konto. Die CLI-Textdateien wurden **nicht** ausgeführt.

## B. Detaillierter Modulaufbau

### Modul 1: Konten und IAM

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Benutzer, Gruppen, Rollen und Richtlinien unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Auswertung von Allow und Deny nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende den Grundsatz der geringsten Rechte anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Zugangsdaten sicher behandeln.
* **Voraussetzungen:** Cloud-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Richtlinien auswerten | 3 |
| 1.2 | Deny schlägt Allow | 3 |
| 1.3 | Befehle lesen | 3 |
| 1.4 | Konzept der geringsten Rechte | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Richtlinien auswerten (Einheit 1.1):** Führen Sie `python3 iam_modell.py` aus. Erklären Sie für jeden der fünf Fälle, warum er erlaubt oder verboten ist.
2. **Deny schlägt Allow (Einheit 1.2):** Erklären Sie am Beispiel von `anna` und `s3:DeleteObject`, wie ein ausdrückliches Deny wirkt.
3. **Befehle lesen (Einheit 1.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Konzept der geringsten Rechte (Einheit 1.4):** Schreiben Sie eine Richtlinie in Worten für einen Benutzer, der nur Berichte lesen darf, und begründen Sie, was Sie weglassen.

#### Kontrollfragen

1. Was gilt ohne Allow-Regel?
2. Wie wirkt ein Deny?
3. Warum keine Zugangsschlüssel des Root-Benutzers?
4. Wozu dient eine Rolle (Fachwissen)?

### Modul 2: VPC und Netzwerkaufbau

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein VPC in öffentliche und private Subnetze aufteilen.
  * Nach Abschluss dieses Moduls kann der Lernende Routen nach dem längsten Präfix auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Adressen planen.
  * Nach Abschluss dieses Moduls kann der Lernende die Bausteine Internet-Gateway und Routentabelle erklären.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Adressplan | 5 |
| 2.2 | Routen | 3 |
| 2.3 | Befehle lesen | 3 |
| 2.4 | Eigenen Plan erstellen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Adressplan (Einheit 2.1):** Führen Sie `python3 vpc_plan.py` aus. Erklären Sie die Aufteilung von `10.56.0.0/16` in Subnetze.
2. **Routen (Einheit 2.2):** Erklären Sie, warum `10.57.1.1` über `pcx-1` und `8.8.8.8` über `igw-1` geht.
3. **Befehle lesen (Einheit 2.3):** Lesen Sie `beispiel_cli.txt` und ordnen Sie jeden Befehl einem Baustein des Plans zu. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Eigenen Plan erstellen (Einheit 2.4):** Planen Sie ein VPC mit zwei Zonen, je einem öffentlichen und privaten Subnetz, und begründen Sie die Größen.

#### Kontrollfragen

1. Wie viele /24-Subnetze passen in ein /16?
2. Welche Route gilt bei mehreren Treffern?
3. Warum sind nicht alle Adressen nutzbar?
4. Wozu dient ein Internet-Gateway?

### Modul 3: EC2, Auto Scaling und Load Balancing

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf des Target-Tracking-Scalings nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Minimum, Maximum und Ziel festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle eines Load Balancers beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Instanzen mit Vorlagen starten.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Scaling beobachten | 5 |
| 3.2 | Grenzen | 3 |
| 3.3 | Befehle lesen | 3 |
| 3.4 | Konzept | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Scaling beobachten (Einheit 3.1):** Führen Sie `python3 scaling_modell.py` aus. Erklären Sie, wie aus Last und Zielwert die gewünschte Anzahl entsteht.
2. **Grenzen (Einheit 3.2):** Erklären Sie, wann Minimum und Maximum die Rechnung begrenzen.
3. **Befehle lesen (Einheit 3.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Konzept (Einheit 3.4):** Skizzieren Sie eine Web-Anwendung mit Load Balancer, zwei Zonen und Auto Scaling und nennen Sie die Prüfungen (Health Checks).

#### Kontrollfragen

1. Wie viele Instanzen ergibt die Last 140 bei 2 Instanzen und Ziel 50 %?
2. Wozu dient das Maximum?
3. Was macht ein Load Balancer?
4. Welche Vereinfachung hat das Modell?

### Modul 4: Speicher: EBS, S3 und EFS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Block-, Objekt- und Dateispeicher unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Lebenszyklusregeln für Objekte beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Kosten mit und ohne Regel abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Snapshots einordnen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Lebenszyklus rechnen | 4 |
| 4.2 | Speicherarten | 4 |
| 4.3 | Befehle lesen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Lebenszyklus rechnen (Einheit 4.1):** Führen Sie `python3 speicher_modell.py` aus. Erklären Sie die Spalten und die Kosten mit und ohne Regel.
2. **Speicherarten (Einheit 4.2):** Beschreiben Sie, wofür EBS, S3 und EFS jeweils geeignet sind (Fachwissen) und kennzeichnen Sie die Unsicherheit.
3. **Befehle lesen (Einheit 4.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Wofür dient eine Lebenszyklusregel?
2. Warum sind die Preise im Modell erfunden?
3. Was unterscheidet Block- von Objektspeicher (Fachwissen)?

### Modul 5: Datenbanken im Betrieb mit RDS

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Aufbewahrungszeit von Sicherungen bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende punktgenaue Wiederherstellung einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Speicherwachstum planen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Aufbewahrung | 4 |
| 5.2 | Wachstum | 3 |
| 5.3 | Befehle lesen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbewahrung (Einheit 5.1):** Führen Sie `python3 rds_modell.py` aus. Erklären Sie, bei welchen Vorfällen die Wiederherstellung möglich ist.
2. **Wachstum (Einheit 5.2):** Rechnen Sie das Speicherwachstum auf 24 Monate hoch und nennen Sie, was Sie bei der Planung beachten.
3. **Befehle lesen (Einheit 5.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Wann ist die Wiederherstellung im Modell möglich?
2. Wie groß ist die Datenbank nach 12 Monaten?
3. Was ist ein Snapshot (Fachwissen)?

### Modul 6: Überwachung mit CloudWatch

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Alarm-Mechanismus „M von N Datenpunkten“ erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Schwellwerte sinnvoll setzen.
  * Nach Abschluss dieses Moduls kann der Lernende Alarmzustände lesen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Alarm auswerten | 3 |
| 6.2 | Parameter ändern | 3 |
| 6.3 | Befehle lesen | 3 |
| 6.4 | Überwachungskonzept | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Alarm auswerten (Einheit 6.1):** Führen Sie `python3 alarm_modell.py` aus. Erklären Sie, warum der Alarm bei Minute 3 beginnt und bei Minute 9 endet.
2. **Parameter ändern (Einheit 6.2):** Ändern Sie `m` auf 3 und beschreiben Sie, wie sich die Alarmzustände ändern.
3. **Befehle lesen (Einheit 6.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Überwachungskonzept (Einheit 6.4):** Planen Sie Alarme für CPU, Speicher und Fehlerrate einer Web-Anwendung.

#### Kontrollfragen

1. Was bedeutet „2 von 3“?
2. Warum nicht beim ersten Ausreißer alarmieren?
3. Wozu dient `describe-alarms`?
4. Was zeigt Minute 4 im Modell?

### Modul 7: Automatisierung mit CLI und CloudFormation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine CloudFormation-Vorlage strukturell lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Ref-Beziehungen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende CLI-Befehle zu einem Ablauf ordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Infrastruktur als Text beschreiben.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Vorlage prüfen | 5 |
| 7.2 | Vorlage lesen | 3 |
| 7.3 | Befehle lesen | 3 |
| 7.4 | Eigene Vorlage | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorlage prüfen (Einheit 7.1):** Führen Sie `python3 cfn_pruefen.py` aus. Erklären Sie die Befunde zur Vorlage „schlecht“.
2. **Vorlage lesen (Einheit 7.2):** Erklären Sie die Abschnitte Parameters, Resources und Outputs der Vorlage „gut“ im Skript.
3. **Befehle lesen (Einheit 7.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie `validate-template`, `create-stack` und `describe-stack-events`. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Eigene Vorlage (Einheit 7.4):** Schreiben Sie eine Vorlage für einen Bucket und prüfen Sie sie mit `validate-template`.

#### Kontrollfragen

1. Wozu dient CloudFormation?
2. Was meldet die Prüfung für „schlecht“?
3. Warum Infrastruktur als Text?
4. Ersetzt das Modell die Prüfung durch AWS?

### Modul 8: Kostenkontrolle, Sicherheit und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Budgetschwellen und Hochrechnung lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Kostenrisiken erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Sicherheits-Checkliste anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler systematisch eingrenzen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Budget prüfen | 3 |
| 8.2 | Kostenfallen | 3 |
| 8.3 | Befehle lesen | 3 |
| 8.4 | Ablaufplan | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Budget prüfen (Einheit 8.1):** Führen Sie `python3 kosten_modell.py` aus. Erklären Sie die Prognose und warum sie ab Tag 20 über dem Budget liegt, obwohl erst 75 % verbraucht sind.
2. **Kostenfallen (Einheit 8.2):** Listen Sie Ressourcen auf, die auch ungenutzt Kosten verursachen können, und kennzeichnen Sie die Unsicherheit.
3. **Befehle lesen (Einheit 8.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie `create-budget` und `lookup-events`. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Ablaufplan (Einheit 8.4):** Schreiben Sie einen Ablaufplan „Instanz ist nicht erreichbar“ (Status, Sicherheitsgruppe, Routen, Protokolle).

#### Kontrollfragen

1. Wie wird die Monatsprognose im Modell berechnet?
2. Warum Budgetwarnungen bei 50 %, 80 % und 100 %?
3. Warum Ressourcen nach der Übung löschen?
4. Wozu dient CloudTrail (Fachwissen)?
