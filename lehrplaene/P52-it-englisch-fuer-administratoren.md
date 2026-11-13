# Lehrplan: IT-Englisch für Administratoren

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Schulenglisch und IT-Grundlagen |
| **Gesamtumfang** | 8 Module, 46 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Fachenglisch für die IT-Administration: Fachwortschatz, Dokumentation und Fehlermeldungen lesen, E-Mails und Tickets, Telefon- und Support-Situationen, Berichte; optional Python 3 für kleine Glossar- und Meldungshilfen |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen: Kein allgemeiner Englischkurs, keine Prüfungsvorbereitung (z. B. Zertifikate), keine technischen Inhalte außer als Sprachanlass, keine Fachübersetzung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Fachwortschatz: Hardware, Software und Betriebssystem | 1 | 5 |
| 2 | Fachwortschatz: Netzwerk, Server und Betrieb | 1 | 5 |
| 3 | Dokumentation und Handbücher lesen | 1 | 7 |
| 4 | Fehlermeldungen und Logs auf Englisch lesen | 1 | 6 |
| 5 | E-Mails und Tickets auf Englisch schreiben | 1 | 7 |
| 6 | Telefon- und Support-Situationen | 1 | 6 |
| 7 | Berichte, Änderungs- und Vorfallsdokumentation auf Englisch | 1 | 6 |
| 8 | Übungsdialoge und Glossar Deutsch–Englisch | 2 | 4 |
| **Gesamt** | **7 Pflichtmodule, 1 Vertiefungsmodul** | | **46** |

*Hinweis zur Priorisierung: Modul 8 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 8 voraus.* 1 UE = 45 Minuten.

### 2. Quellen und Stand

* **Fachenglisch in der IT (Wortschatz, Aufbau von Dokumentation, E-Mails und Tickets):** Fachwissen des Verfassers, **nicht von einer Englischlehrkraft oder gegen ein Wörterbuch geprüft**.
* **Microsoft Writing Style Guide** (<https://learn.microsoft.com/style-guide/welcome/>): als Suchtreffer gefunden, **Inhalt nicht im Einzelnen geprüft**; nur als weiterführende Lektüre genannt.
* **RFC 2119** (IETF, <https://www.rfc-editor.org/rfc/rfc2119.html>): als Suchtreffer gefunden, **nicht abgerufen und nicht geprüft**; die Bedeutung von MUST, SHOULD und MAY ist aus dem Fachwissen beschrieben.
* **Alle englischen Texte, Dialoge und Meldungen** des Kurses sind vom Verfasser erfunden; keine Auszüge aus Handbüchern oder Programmen.

### 3. Labor-Setup & Rahmenbedingungen

* **Kein technisches Labor.** Es genügen Textverarbeitung, Tabellenkalkulation und optional Python 3 (nur Standardbibliothek).
* **Fiktives Unternehmen:** Bergfried Metallbau GmbH (Graz), 30 Mitarbeitende, Labornetz `10.80.0.0/24`, Namen unter `lab.internal`; englischsprachige Partner `Northwind Support Ltd.` und `Redfield Hosting Inc.` (fiktiv, `example.com`).
* **Aufgabenformen:** Zuordnungs-, Lücken-, Übersetzungs-, Schreib- und Rollenspielaufgaben; Rollenspiele werden paarweise geübt und vom Dozenten gehört.
* **Material des Dozenten:** Dialogszenarien und ein Glossar; Beispiele liegen der Übungsreihe bei und sind erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Fachwortschatz: Hardware, Software und Betriebssystem
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende gängige englische Fachbegriffe zu Hardware, Software und Betriebssystem verstehen und verwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Abkürzungen (RAM, SSD, PSU, OS, GUI, CLI) auflösen und aussprechen.
  * Nach Abschluss dieses Moduls kann der Lernende einfache Sachverhalte (Aufbau eines Arbeitsplatzes, Zustand eines Geräts) auf Englisch beschreiben.
* **Voraussetzungen:** Schulenglisch.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Hardware und Zubehör | 2 |
| 1.2 | Software, Updates und Betriebssystem | 2 |
| 1.3 | Abkürzungen und Aussprache | 1 |

#### Praxisaufgaben
1. **Begriffe zuordnen:** Ordne zwölf englische Begriffe den deutschen Entsprechungen zu.
2. **Software und Betriebssystem:** Fülle zehn Lücken in einem kurzen Text über Aktualisierungen aus und übersetze zwei Sätze.
3. **Abkürzungen:** Löse zehn Abkürzungen auf und übe die Aussprache der Buchstaben.

#### Kontrollfragen
1. Wie heißt „Arbeitsspeicher“ auf Englisch?
2. Was ist der Unterschied zwischen update und upgrade?
3. Wofür steht CLI?

### Modul 2: Fachwortschatz: Netzwerk, Server und Betrieb
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende englische Fachbegriffe zu Netzwerk, Servern und Betrieb (Backup, Incident, Maintenance) verstehen und verwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Zustände (up, down, available, reachable) und Handlungen (restart, restore, roll back) auf Englisch benennen.
  * Nach Abschluss dieses Moduls kann der Lernende einfache Handlungsanweisungen im Imperativ formulieren.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Netzwerk und Verbindung | 2 |
| 2.2 | Server, Dienste und Betrieb | 2 |
| 2.3 | Handlungsanweisungen formulieren | 1 |

#### Praxisaufgaben
1. **Netzwerkbegriffe:** Verbinde zehn englische Begriffe mit deutschen Erklärungen.
2. **Betriebsbegriffe:** Beschreibe in vier englischen Sätzen eine Wartung und die Rückkehr zum Normalbetrieb.
3. **Handlungsanweisungen:** Formuliere fünf Handlungsanweisungen für einen Kollegen im Imperativ.

#### Kontrollfragen
1. Was bedeutet „The server is down“?
2. Was ist ein maintenance window?
3. Wie bittest du höflich um Rückmeldung?

### Modul 3: Dokumentation und Handbücher lesen
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer englischen Anleitung (Requirements, Steps, Notes, Warnings) erkennen und gezielt Informationen suchen.
  * Nach Abschluss dieses Moduls kann der Lernende Modalverben und Signalwörter (must, should, may, do not, only if) in Anleitungen richtig deuten.
  * Nach Abschluss dieses Moduls kann der Lernende einen englischen Abschnitt einer Anleitung zusammenfassen und Schritte auf Deutsch wiedergeben.
* **Voraussetzungen:** Modul 1 und 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Aufbau von Anleitungen und Release Notes | 2 |
| 3.2 | Modalverben und Signalwörter | 2 |
| 3.3 | Lesestrategien und Zusammenfassung | 3 |

#### Praxisaufgaben
1. **Aufbau erkennen:** Markiere in einer erfundenen Anleitung die Abschnitte und beantworte Fragen.
2. **Modalverben:** Ordne Modalverben nach Verbindlichkeit und übersetze fünf Sätze.
3. **Zusammenfassung:** Fasse den Abschnitt „Restoring a file“ in fünf deutschen Sätzen zusammen.

#### Kontrollfragen
1. Was bedeutet „Do not“ in einer Anleitung?
2. Warum lohnt es sich, zuerst die Überschriften zu lesen?
3. Was ist der Unterschied zwischen note und warning?

### Modul 4: Fehlermeldungen und Logs auf Englisch lesen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende gängige englische Fehlermeldungen verstehen und deren Bedeutung auf Deutsch wiedergeben.
  * Nach Abschluss dieses Moduls kann der Lernende in englischen Logzeilen Zeit, Komponente, Stufe und Meldungstext unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende aus einer Fehlermeldung einen passenden Suchbegriff und einen Ticketsatz ableiten.
* **Voraussetzungen:** Modul 1 bis 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Aufbau von Fehlermeldungen | 2 |
| 4.2 | Logzeilen lesen | 2 |
| 4.3 | Meldungen auswerten und suchen | 2 |

#### Praxisaufgaben
1. **Meldungen deuten:** Übersetze und erkläre acht Fehlermeldungen.
2. **Logzeilen:** Zerlege fünf Logzeilen in Zeit, Komponente und Text und lies sie mit dem Skript `fehlermeldungen.py`.
3. **Suchbegriff und Ticketsatz:** Formuliere für zwei Meldungen einen Suchbegriff und einen englischen Ticketsatz.

#### Kontrollfragen
1. Warum keine internen Namen in die Suchmaschine?
2. Was ist der Unterschied zwischen „refused“ und „timed out“?
3. Wie liest man eine Logzeile?

### Modul 5: E-Mails und Tickets auf Englisch schreiben
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Störungsmeldung als englisches Ticket mit Betreff, Beschreibung, Auswirkung und Bitte schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende höfliche und präzise englische E-Mails an Kollegen, Kunden und Dienstleister verfassen (Anrede, Anliegen, Bitte, Schluss).
  * Nach Abschluss dieses Moduls kann der Lernende auf Rückfragen antworten, Termine bestätigen und eine Verzögerung höflich ankündigen.
* **Voraussetzungen:** Modul 1 bis 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Aufbau eines Tickets: Betreff, Beschreibung, Auswirkung | 2 |
| 5.2 | E-Mails: Anrede, Anliegen, Bitte, Schluss | 3 |
| 5.3 | Antworten, Bestätigen, Verzögerungen melden | 2 |

#### Praxisaufgaben
1. **Ticket:** Schreibe ein englisches Ticket für die Störung „Intranet nicht erreichbar“.
2. **E-Mail an den Hoster:** Schreibe eine E-Mail an `Redfield Hosting Inc.` mit Bitte um ein Wartungsfenster.
3. **Verzögerung melden:** Melde auf Englisch eine Verzögerung und bestätige einen neuen Termin.

#### Kontrollfragen
1. Was gehört in einen guten Ticketbetreff?
2. Welche Schlussformeln sind höflich?
3. Wie bittest du höflich um Bestätigung?

### Modul 6: Telefon- und Support-Situationen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Support-Telefonat auf Englisch eröffnen, strukturieren und beenden.
  * Nach Abschluss dieses Moduls kann der Lernende Rückfragen stellen, Aussagen wiederholen und Nichtverstehen höflich anzeigen.
  * Nach Abschluss dieses Moduls kann der Lernende Schritte am Telefon einfach und eindeutig erklären.
* **Voraussetzungen:** Modul 1 bis 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Begrüßung, Anliegen aufnehmen, Rückfragen | 2 |
| 6.2 | Schritte erklären, Verständnis sichern | 2 |
| 6.3 | Schwierige Situationen: Wartezeit, Eskalation, Abschluss | 2 |

#### Praxisaufgaben
1. **Dialog ordnen:** Bringe die Sätze eines Support-Dialogs in die richtige Reihenfolge.
2. **Schritte erklären:** Erkläre am Telefon einem Anwender in fünf Sätzen, wie er den Browser neu startet und die Seite erneut öffnet.
3. **Schwierige Situationen:** Formuliere höfliche Antworten für vier schwierige Situationen am Telefon.

#### Kontrollfragen
1. Wie bittest du um Wiederholung?
2. Warum wiederholst du wichtige Angaben?
3. Was sagst du, wenn du eskalierst?

### Modul 7: Berichte, Änderungs- und Vorfallsdokumentation auf Englisch
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen kurzen englischen Vorfallsbericht (Summary, Timeline, Cause, Actions) schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Änderung (Change) mit Zweck, Zeitfenster, Auswirkung und Rückfallplan auf Englisch beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Zeitangaben, Zahlen und Verlaufsformen (was geschah wann) korrekt ausdrücken.
* **Voraussetzungen:** Modul 3 bis 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Vorfallsbericht: Aufbau und Sprache | 2 |
| 7.2 | Änderungsbeschreibung und Rückfallplan | 2 |
| 7.3 | Zeit, Zahlen und Vergangenheitsformen | 2 |

#### Praxisaufgaben
1. **Vorfallsbericht:** Schreibe einen kurzen Vorfallsbericht zum Fall „DNS-Dienst beendet“.
2. **Change-Beschreibung:** Beschreibe eine Änderung (Update des Dateiservers) auf Englisch mit Rückfallplan.
3. **Zeitformen:** Verbessere fünf Sätze mit Fehlern in Zeitformen und Zahlen.

#### Kontrollfragen
1. Was gehört in eine Timeline?
2. Warum trennt der Bericht Ursache und Vermutung?
3. Was ist ein rollback plan?

### Modul 8: Übungsdialoge und Glossar Deutsch–Englisch
* **Priorität:** 2 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Support-Dialog mit Partner frei sprechen und die eigene Leistung nach Kriterien bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende ein eigenes Glossar Deutsch–Englisch aufbauen, prüfen und pflegen.
* **Voraussetzungen:** Modul 1 bis 7.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Übungsdialoge im Rollenspiel | 2 |
| 8.2 | Glossar aufbauen und prüfen | 2 |

#### Praxisaufgaben
1. **Rollenspiel:** Spielt zu zweit ein Support-Telefonat und bewertet es nach vier Kriterien.
2. **Glossar:** Erweitere `glossar.csv` um 20 eigene Einträge und prüfe mit `glossar_pruefen.py`.

#### Kontrollfragen
1. Woran erkennt man ein gutes Glossar?
2. Wie gehst du mit Wörtern um, die mehrere Übersetzungen haben?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P52 erstellt (Annahmen: Bergfried Metallbau GmbH, kein Labor, Vorkenntnisse Schulenglisch). Stunden: 5+5+7+6+7+6+6+4 = 46 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 7×1, 1×2.

**Nicht bestätigt:** Wortschatz und Beispielsätze sind Fachwissen und nicht von einer Englischlehrkraft geprüft; Stilleitfaden und RFC 2119 nicht gelesen.

**Offen:** Zeitaufwand unerprobt; der Lehrplan wurde von AnsibleArtisan4711 noch nicht geprüft.
