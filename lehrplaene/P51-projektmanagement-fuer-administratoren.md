# Lehrplan: Projektmanagement für Administratoren

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in der Administration von Servern und Arbeitsplätzen |
| **Gesamtumfang** | 8 Module, 46 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Projektmanagement klassisch und agil für IT-Vorhaben (Server-Migration, Client-Rollout); Textverarbeitung und Tabellenkalkulation; optional Python 3 für kleine Rechenhilfen (kritischer Pfad, Dreipunktschätzung) |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen: Keine Zertifizierungsvorbereitung (z. B. für PMP, PRINCE2 oder Scrum-Rollen), keine Projektmanagement-Software, kein technisches Labor, keine Vertiefung von ITIL-Prozessen (Change-Management nur im Projektrahmen). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Projektgrundlagen und Projektphasen | 1 | 5 |
| 2 | Anforderungen erfassen und Projektauftrag schreiben | 1 | 6 |
| 3 | Planung: Strukturplan, Ablauf und kritischer Pfad | 1 | 7 |
| 4 | Aufwandsschätzung und Budget | 1 | 6 |
| 5 | Risiken und Änderungen steuern | 1 | 5 |
| 6 | Klassisch, agil und hybrid: Methoden im Überblick | 1 | 6 |
| 7 | Kommunikation, Abnahme, Übergabe und Dokumentation | 1 | 6 |
| 8 | Fallbeispiele: Server-Migration und Client-Rollout | 2 | 5 |
| **Gesamt** | **7 Pflichtmodule, 1 Vertiefungsmodul** | | **46** |

*Hinweis zur Priorisierung: Modul 8 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 8 voraus.* 1 UE = 45 Minuten.

### 2. Quellen und Stand

* **Projektmanagement-Methodik (Phasen, Netzplan, Dreipunktschätzung, Risikomatrix, Kanban):** Fachwissen des Verfassers, **nicht gegen Normen, Leitfäden oder Handbücher geprüft**. Vor dem Kurs mit der Methodik des Dozenten abgleichen.
* **Scrum Guide (2020)** (<https://www.scrumguides.org/scrum-guide.html>): in der Suche gefunden, **nicht abgerufen, Inhalt nicht geprüft**; die Beschreibung von Scrum in Modul 6 ist Fachwissen und vor dem Kurs am Scrum Guide zu prüfen.
* **Agiles Manifest, PMBOK, PRINCE2, ISO 21500/21502:** nicht abgerufen, nicht geprüft, nicht Grundlage dieses Lehrplans.
* **RFC 1918** (IETF, Februar 1996) für private Adressen und **RFC 2606** (IETF, Juni 1999, Datum nicht geprüft) für `example.com`.

### 3. Labor-Setup & Rahmenbedingungen

* **Kein technisches Labor.** Es genügen Textverarbeitung, Tabellenkalkulation und optional Python 3 (nur Standardbibliothek).
* **Fiktives Unternehmen:** Tannenhof Logistik GmbH (Linz), 60 Mitarbeitende, Domäne `tannenhof.example.com`, Netz `10.90.0.0/24`. Fall 1: Ersatz des Dateiservers (62 Freigaben), Fall 2: Rollout von 25 Arbeitsplätzen. Alle Angaben sind frei erfunden.
* **Aufgabenformen:** Fallstudien, Dokumentations- und Rechenaufgaben (Projektauftrag, Strukturplan, kritischer Pfad, Schätzung, Risikoregister, Abnahmeprotokoll).
* **Material des Dozenten:** Kurzbeschreibungen der Fälle, Vorgangsliste und Schätzwerte; Beispiele liegen der Übungsreihe bei und sind erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Projektgrundlagen und Projektphasen
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Projekt von laufendem Betrieb anhand von Merkmalen (einmalig, befristet, Ziel, Ressourcen) abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die typischen Projektphasen (Initiierung, Planung, Durchführung, Abschluss) und deren Ergebnisse nennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rollen in einem IT-Projekt (Auftraggeber, Projektleitung, Team, Anwender) beschreiben und das Zieldreieck (Zeit, Kosten, Leistung) auf ein Beispiel anwenden.
* **Voraussetzungen:** IT-Grundlagen.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Projekt und Betrieb: Merkmale und Abgrenzung | 1 |
| 1.2 | Projektphasen und ihre Ergebnisse | 2 |
| 1.3 | Rollen und Zieldreieck | 2 |

#### Praxisaufgaben
1. **Projekt oder Betrieb:** Ordne zehn Tätigkeiten der Tannenhof Logistik GmbH „Projekt“ oder „Betrieb“ zu und begründe.
2. **Phasenergebnisse:** Ordne den Phasen Ergebnisse zu und ergänze für den Fall Server-Migration je ein Ergebnis.
3. **Rollen und Zieldreieck:** Beschreibe die Rollen im Fall Client-Rollout und zeige am Zieldreieck, was ein verkürzter Termin bewirkt.

#### Kontrollfragen
1. Was unterscheidet ein Projekt vom Betrieb?
2. Welches Ergebnis schließt die Planungsphase ab?
3. Was zeigt das Zieldreieck?

### Modul 2: Anforderungen erfassen und Projektauftrag schreiben
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Anforderungen von Anwendern und Fachabteilungen erfassen, in funktionale und nichtfunktionale Anforderungen gliedern und priorisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Ziele nach dem SMART-Prinzip prüfbar formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende einen kurzen Projektauftrag mit Ziel, Umfang, Abgrenzung, Termin, Budgetrahmen und Beteiligten schreiben.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Anforderungen: sammeln, gliedern, priorisieren | 2 |
| 2.2 | Ziele prüfbar formulieren (SMART) | 1 |
| 2.3 | Projektauftrag und Abgrenzung | 3 |

#### Praxisaufgaben
1. **Anforderungen gliedern:** Gliedere zwölf Aussagen von Anwendern in funktionale und nichtfunktionale Anforderungen und priorisiere sie.
2. **SMART:** Prüfe vier Zielformulierungen nach SMART und verbessere zwei.
3. **Projektauftrag:** Schreibe einen Projektauftrag (eine Seite) für die Server-Migration.

#### Kontrollfragen
1. Was ist eine nichtfunktionale Anforderung?
2. Warum gehört die Abgrenzung in den Auftrag?
3. Was fehlt dem Ziel „schneller“?

### Modul 3: Planung: Strukturplan, Ablauf und kritischer Pfad
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Projekt in einem Projektstrukturplan in Arbeitspakete gliedern.
  * Nach Abschluss dieses Moduls kann der Lernende Abhängigkeiten zwischen Vorgängen darstellen und den kritischen Pfad sowie Pufferzeiten bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende einen einfachen Terminplan (Gantt-Darstellung als Tabelle) erstellen und Meilensteine festlegen.
* **Voraussetzungen:** Modul 1 und 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Projektstrukturplan und Arbeitspakete | 2 |
| 3.2 | Abhängigkeiten, kritischer Pfad und Puffer | 3 |
| 3.3 | Terminplan und Meilensteine | 2 |

#### Praxisaufgaben
1. **Projektstrukturplan:** Zerlege das Projekt Client-Rollout in mindestens zwölf Arbeitspakete auf zwei Ebenen.
2. **Kritischer Pfad:** Berechne mit `kritischer_pfad.py` den kritischen Pfad der Server-Migration und beantworte vier Fragen.
3. **Terminplan und Meilensteine:** Übertrage das Ergebnis in eine Terminplan-Tabelle und lege drei Meilensteine fest.

#### Kontrollfragen
1. Was ist der kritische Pfad?
2. Was bedeutet Puffer 0?
3. Wofür dienen Meilensteine?

### Modul 4: Aufwandsschätzung und Budget
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aufwand mit Dreipunktschätzung (optimistisch, wahrscheinlich, pessimistisch) berechnen und die Streuung einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Puffer begründen und von Schätzung und Zusage unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende ein einfaches Budget aus Personal-, Sach- und Lizenzkosten aufstellen.
* **Voraussetzungen:** Modul 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Schätzmethoden im Überblick und Schätzfehler | 2 |
| 4.2 | Dreipunktschätzung rechnen | 2 |
| 4.3 | Kosten und Budget | 2 |

#### Praxisaufgaben
1. **Schätzfehler:** Nenne fünf typische Schätzfehler und je eine Gegenmaßnahme.
2. **Dreipunktschätzung:** Rechne `aufwand.csv` von Hand für zwei Zeilen und mit `aufwand.py` für alle.
3. **Budget:** Stelle ein Budget für den Client-Rollout auf und trenne Schätzung, Puffer und Zusage.

#### Kontrollfragen
1. Was ist der Unterschied zwischen Schätzung und Zusage?
2. Warum wird die pessimistische Schätzung benötigt?
3. Was gehört in ein IT-Budget?

### Modul 5: Risiken und Änderungen steuern
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Risiken identifizieren, nach Eintrittswahrscheinlichkeit und Auswirkung bewerten und Gegenmaßnahmen zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Risikoregister mit Verantwortlichen und Beobachtungsdatum führen.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungswünsche (Change Requests) erfassen, bewerten und entscheiden lassen.
* **Voraussetzungen:** Modul 2 bis 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Risiken erkennen und bewerten | 2 |
| 5.2 | Risikoregister und Gegenmaßnahmen | 2 |
| 5.3 | Änderungen am Projekt steuern | 1 |

#### Praxisaufgaben
1. **Risiken sammeln:** Sammle zehn Risiken der Server-Migration und bewerte sie auf einer Skala von 1 bis 5.
2. **Risikoregister:** Lege für die drei größten Risiken Gegenmaßnahme, Verantwortlichen und Notfallplan fest.
3. **Change Request:** Bewerte zwei Änderungswünsche und erstelle eine Entscheidungsvorlage.

#### Kontrollfragen
1. Was heißt „Risiko akzeptieren“?
2. Warum braucht jedes Risiko einen Verantwortlichen?
3. Wer entscheidet über einen Change Request?

### Modul 6: Klassisch, agil und hybrid: Methoden im Überblick
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende klassisches (Wasserfall) und agiles Vorgehen anhand von Merkmalen vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende die Elemente von Scrum (Rollen, Ereignisse, Artefakte) und von Kanban in eigenen Worten beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende für ein gegebenes Vorhaben eine passende Vorgehensweise begründen.
* **Voraussetzungen:** Modul 1 bis 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Klassisches Vorgehen: Merkmale, Stärken, Grenzen | 1 |
| 6.2 | Scrum im Überblick | 2 |
| 6.3 | Kanban im Überblick | 1 |
| 6.4 | Auswahl und hybride Formen | 2 |

#### Praxisaufgaben
1. **Vergleich:** Vergleiche klassisches und agiles Vorgehen in einer Tabelle mit sechs Kriterien.
2. **Scrum und Kanban:** Beschreibe Scrum und Kanban jeweils in einem kurzen Absatz und nenne einen Unterschied.
3. **Passende Form:** Wähle für drei Vorhaben die Vorgehensweise und begründe.

#### Kontrollfragen
1. Wann ist klassisches Vorgehen sinnvoll?
2. Was begrenzt Kanban?
3. Was ist ein Sprint?

### Modul 7: Kommunikation, Abnahme, Übergabe und Dokumentation
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Kommunikationsplan mit Zielgruppen, Inhalten, Medien und Rhythmus aufstellen und einen Statusbericht schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Abnahmekriterien prüfbar formulieren und ein Abnahmeprotokoll aufbauen.
  * Nach Abschluss dieses Moduls kann der Lernende die Übergabe an den Betrieb vorbereiten (Betriebshandbuch, Einweisung) und einen Abschlussbericht mit gelernten Lehren verfassen.
* **Voraussetzungen:** Modul 2 bis 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Kommunikationsplan und Statusbericht | 2 |
| 7.2 | Abnahme: Kriterien, Test, Protokoll | 2 |
| 7.3 | Übergabe an den Betrieb und Projektabschluss | 2 |

#### Praxisaufgaben
1. **Kommunikationsplan:** Erstelle einen Kommunikationsplan für den Client-Rollout und schreibe einen Statusbericht.
2. **Abnahme:** Formuliere fünf Abnahmekriterien für die Server-Migration und baue ein Abnahmeprotokoll.
3. **Übergabe und Abschluss:** Plane die Übergabe an den Betrieb und fasse drei gelernte Lehren zusammen.

#### Kontrollfragen
1. Warum gehören Abnahmekriterien in den Auftrag?
2. Was gehört in einen Abschlussbericht?
3. Welche Rolle hat die Einweisung?

### Modul 8: Fallbeispiele: Server-Migration und Client-Rollout
* **Priorität:** 2 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Projekt (Server-Migration oder Client-Rollout) von der Anforderung bis zur Abnahme durchplanen.
  * Nach Abschluss dieses Moduls kann der Lernende den eigenen Projektplan gegen die Musterlösung abgleichen und Abweichungen begründen.
* **Voraussetzungen:** Module 1 bis 7.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Fallbeispiel Server-Migration | 3 |
| 8.2 | Fallbeispiel Client-Rollout | 2 |

#### Praxisaufgaben
1. **Server-Migration planen:** Erstelle aus einer Kurzbeschreibung Auftrag, Strukturplan, Risikoliste und Abnahmekriterien.
2. **Client-Rollout planen:** Plane den Rollout der 25 Arbeitsplätze mit Dreipunktschätzung und Budget.

#### Kontrollfragen
1. Woran erkennst du einen guten Projektplan?
2. Warum ist eine einzige richtige Lösung nicht zu erwarten?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P51 erstellt (Annahmen: Tannenhof Logistik GmbH, kein Labor, Fallbeispiele Server-Migration und Client-Rollout). Stunden: 5+6+7+6+5+6+6+5 = 46 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 7×1, 1×2.

**Nicht bestätigt:** Alle Methodenaussagen (Phasen, Formeln, Skalen) sind Fachwissen; Scrum Guide nicht abgerufen; keine Norm gelesen.

**Offen:** Zeitaufwand unerprobt; der Lehrplan wurde von Matija noch nicht geprüft.
