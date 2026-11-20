# Lehrplan: Google Cloud Grundlagen

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen; Cloud-Grundlagen |
| **Gesamtumfang** | 8 Module, 45 UE (zu 45 Minuten; 33,75 Stunden) |
| **Fokus-Technologien** | Google Cloud (Compute Engine, VPC, Cloud Storage, IAM), gcloud CLI; Organisation, Projekte und Abrechnung; IAM und Dienstkonten; Compute Engine; VPC und Firewall-Regeln; Cloud Storage; Cloud SQL im Überblick; Überwachung, Logging und Kosten; Vergleich mit AWS und Azure |
| **Thematische Abgrenzung (Out of Scope)** | AWS und Azure sind eigene Kurse; keine Spezialdienste (BigQuery, KI) außer als Ausblick |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Organisation, Projekte und Abrechnung | 1 | 5 |
| 2 | IAM und Dienstkonten | 1 | 6 |
| 3 | Compute Engine | 1 | 5 |
| 4 | VPC und Firewall-Regeln | 1 | 6 |
| 5 | Cloud Storage | 1 | 5 |
| 6 | Cloud SQL im Überblick | 2 | 4 |
| 7 | Überwachung, Logging und Kosten | 1 | 7 |
| 8 | Vergleich mit AWS und Azure | 1 | 7 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **45** |

**Priorität 1** (Pflicht) sind die Module 1 bis 5, 7 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 6 (Cloud SQL im Überblick). Fällt Modul 6 weg, verringert sich der Gesamtumfang auf 41 UE; kein Pflichtmodul setzt Modul 6 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Google Cloud (Projekte, IAM, Compute Engine, VPC, Cloud Storage, Cloud SQL, Monitoring, gcloud CLI) wurde **nicht** gelesen. Alle fachlichen Aussagen, Standardwerte und gcloud-Befehle stammen aus Fachwissen und sind **nicht bestätigt**; verbindlich ist die aktuelle Dokumentation von Google Cloud. **Preise, Gratis-Kontingente und Maschinentypen wurden nicht recherchiert**: Die Typen und Preise in den Modellen sind **erfunden**.

**Ausgeführt wurden ausschließlich die Python-Modelle** (Python 3 im Cloud-Container): reine Rechnungen mit erfundenen Werten, vereinfacht. **Nicht ausgeführt:** Google-Cloud-Konto, gcloud CLI. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Konto:** ein Google-Cloud-Testkonto **mit Budgetwarnung** (vor jeder Übung einrichten; Gratis-Kontingente und Kosten mit Stand prüfen). **Client:** eine Linux-VM `gcl01` mit installierter gcloud CLI (**keine** Schlüsseldateien von Dienstkonten in Repositories ablegen).

**Aufräumen:** Nach jeder Übung angelegte Ressourcen (Instanzen, Datenträger, Datenbanken, Adressen) löschen; viele verursachen Kosten, solange sie bestehen (Fachwissen, mit Stand prüfen).

**Skripte:** Die Python-Modelle laufen auf jedem Rechner mit Python 3, auch ohne Konto. Die CLI-Textdateien wurden **nicht** ausgeführt.

## B. Detaillierter Modulaufbau

### Modul 1: Organisation, Projekte und Abrechnung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Hierarchie Organisation, Ordner und Projekt erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Vererbung von Rollen nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle des Abrechnungskontos nennen.
* **Voraussetzungen:** Cloud-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Vererbung prüfen | 3 |
| 1.2 | Abrechnung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vererbung prüfen (Einheit 1.1):** Führen Sie `python3 hierarchie_modell.py` aus. Erklären Sie, welche Rolle jede Person in `projekt-web` hat.
2. **Abrechnung (Einheit 1.2):** Erklären Sie, warum `projekt-test` ohne Abrechnungskonto kostenpflichtige Dienste nicht nutzen kann, und lesen Sie `beispiel_cli.txt` (Befehle nicht geprüft).

#### Kontrollfragen

1. Wie wirken Rollen in der Hierarchie?
2. Was braucht ein Projekt für kostenpflichtige Dienste?
3. Welche Ebene ist die oberste im Modell?

### Modul 2: IAM und Dienstkonten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Dienstkonten einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende zu weite Rollen und alte Schlüssel erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende den Grundsatz der geringsten Rechte anwenden.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Dienstkonten prüfen | 2 |
| 2.2 | Ohne Schlüssel arbeiten | 2 |
| 2.3 | Befehle lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dienstkonten prüfen (Einheit 2.1):** Führen Sie `python3 dienstkonten_modell.py` aus. Erklären Sie jede Meldung.
2. **Ohne Schlüssel arbeiten (Einheit 2.2):** Begründen Sie, warum Schlüsseldateien vermieden werden sollten, und nennen Sie Alternativen (Fachwissen, nicht bestätigt).
3. **Befehle lesen (Einheit 2.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Was ist ein Dienstkonto?
2. Warum sind Schlüsseldateien riskant?
3. Welche Meldung erhält `sa-ci` im Modell?
4. Was bedeutet geringste Rechte?

### Modul 3: Compute Engine

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Maschinentyp passend zum Bedarf wählen.
  * Nach Abschluss dieses Moduls kann der Lernende laufende Kosten abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Instanzen mit der CLI verwalten.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Typ wählen | 3 |
| 3.2 | Befehle lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Typ wählen (Einheit 3.1):** Führen Sie `python3 maschinen_modell.py` aus. Erklären Sie die Wahl je Bedarf und die Monatskosten (erfundene Preise).
2. **Befehle lesen (Einheit 3.2):** Lesen Sie `beispiel_cli.txt` und erklären Sie Anlegen, Auflisten und Löschen. Kennzeichnen Sie, was Sie nicht geprüft haben, und nennen Sie, warum Löschen nach der Übung wichtig ist.

#### Kontrollfragen

1. Warum nimmt der Webserver den Typ klein?
2. Warum nimmt die Datenbank den Typ gross?
3. Warum Instanzen löschen?

### Modul 4: VPC und Firewall-Regeln

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Firewall-Regeln nach Priorität auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende das implizite Verbot eingehend erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Netzwerk mit Subnetz anlegen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Regeln auswerten | 2 |
| 4.2 | Prioritäten | 2 |
| 4.3 | Befehle lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regeln auswerten (Einheit 4.1):** Führen Sie `python3 firewall_modell.py` aus. Erklären Sie für jeden der vier Fälle die entscheidende Regel.
2. **Prioritäten (Einheit 4.2):** Erklären Sie, warum `verbiete-telnet` mit 900 vor den Regeln mit 1000 gilt.
3. **Befehle lesen (Einheit 4.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie Netzwerk, Subnetz und Regel. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Welche Regel hat bei kleinerer Zahl Vorrang?
2. Was gilt ohne passende Regel?
3. Warum SSH nur aus dem eigenen Netz?

### Modul 5: Cloud Storage

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Speicherklassen nach Zugriffshäufigkeit unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Kosten verschiedener Klassen vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Buckets mit der CLI anlegen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Klassen vergleichen | 3 |
| 5.2 | Befehle lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Klassen vergleichen (Einheit 5.1):** Führen Sie `python3 speicher_modell.py` aus. Erklären Sie Preis und Mindestlaufzeit und wann sich eine günstigere Klasse lohnt.
2. **Befehle lesen (Einheit 5.2):** Lesen Sie `beispiel_cli.txt` und erklären Sie Bucket, Kopieren und Lebenszyklus. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Was kostet 500 GB in Standard pro Monat im Modell?
2. Warum haben Archivklassen Mindestlaufzeiten?
3. Wozu dient eine Lebenszyklusregel?

### Modul 6: Cloud SQL im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Nutzen einer Reserve in einer zweiten Zone rechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherungen von Hochverfügbarkeit abgrenzen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Verfügbarkeit rechnen | 2 |
| 6.2 | Befehle lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verfügbarkeit rechnen (Einheit 6.1):** Führen Sie `python3 ha_modell.py` aus. Erklären Sie die Werte für eine und zwei Zonen und die Grenzen des Rechenmodells.
2. **Befehle lesen (Einheit 6.2):** Lesen Sie `beispiel_cli.txt` und erklären Sie Instanz und Sicherungsliste. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Welche Verfügbarkeit ergibt das Modell für zwei Zonen?
2. Warum ersetzt die Reserve keine Sicherung?
3. Was berücksichtigt das Modell nicht?

### Modul 7: Überwachung, Logging und Kosten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Budgetschwellen und Hochrechnung lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Protokolle abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende Kostenrisiken erkennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Budget prüfen | 3 |
| 7.2 | Warnungen planen | 2 |
| 7.3 | Befehle lesen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Budget prüfen (Einheit 7.1):** Führen Sie `python3 budget_modell.py` aus. Erklären Sie, wann die Prognose das Budget überschreitet und welche Schwellen ausgelöst werden.
2. **Warnungen planen (Einheit 7.2):** Planen Sie Budgetwarnungen und nennen Sie, wer wann reagiert.
3. **Befehle lesen (Einheit 7.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie Budget und Protokollabfrage. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Wann liegt die Prognose bei 30,00?
2. Welche Schwellen erreicht Tag 28?
3. Warum Budgetwarnung vor der ersten Übung?
4. Wozu dient eine Protokollabfrage?

### Modul 8: Vergleich mit AWS und Azure

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende häufige Begriffe der drei Anbieter zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzen solcher Zuordnungen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Auswahl begründet vorbereiten.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Begriffe zuordnen | 3 |
| 8.2 | Grenzen | 2 |
| 8.3 | Entscheidung vorbereiten | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe zuordnen (Einheit 8.1):** Führen Sie `python3 vergleich.py` aus. Erklären Sie die Zuordnung der fünf Zeilen.
2. **Grenzen (Einheit 8.2):** Beschreiben Sie an zwei Beispielen, warum eine Gleichsetzung nur grob ist.
3. **Entscheidung vorbereiten (Einheit 8.3):** Listen Sie auf, welche Kriterien (Kosten, Dienste, Standorte, Know-how) Sie bei einer Anbieterwahl prüfen und wie Sie die Aussagen belegen.

#### Kontrollfragen

1. Wie heißt der Objektspeicher bei den drei Anbietern?
2. Warum ist die Tabelle nur Orientierung?
3. Welchen Status haben die Zeilen?
