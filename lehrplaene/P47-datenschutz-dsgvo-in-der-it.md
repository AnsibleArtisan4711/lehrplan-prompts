# Lehrplan: Datenschutz (DSGVO) in der IT

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 9 Module, 49 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | DSGVO und Datenschutz in der IT-Administration; Tabellenkalkulation und Textverarbeitung für Vorlagen; optional Python 3 für kleine Rechenhilfen |
| **Thematische Abgrenzung (Out of Scope)** | **Kein Rechtsrat:** Aussagen sind Kursannahmen und von Datenschutzbeauftragten oder Juristen zu prüfen. Kein technisches Labor. Technische Einzelthemen (Verschlüsselung, Backup, Logging-Werkzeuge, Härtung) werden nur kurz mit Verweis auf die eigenen Lehrpläne behandelt (z. B. P16 Kryptografie, Zertifikate und TLS; P12 IT-Sicherheitsgrundlagen; P19 Zentrales Logging; P35 Backup-Konzept). Keine Überschneidung mit P48 (NIS2) und P49 (ISO 27001) über kurze Verweise hinaus. Kein Arbeitsrecht im Detail. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundbegriffe und Grundsätze | 1 | 5 |
| 2 | Rechtsgrundlagen der Verarbeitung | 1 | 5 |
| 3 | Betroffenenrechte | 1 | 6 |
| 4 | Verzeichnis der Verarbeitungstätigkeiten | 1 | 5 |
| 5 | Auftragsverarbeitung und Übermittlung in Drittländer | 1 | 5 |
| 6 | Technische und organisatorische Maßnahmen | 1 | 6 |
| 7 | Datenpannen und Meldung | 1 | 5 |
| 8 | Protokollierung, Aufbewahrung und Praxisfälle aus der Administration | 1 | 8 |
| 9 | Datenschutz-Folgenabschätzung und Datenschutzbeauftragter | 2 | 4 |
| **Gesamt** | **8 Pflichtmodule, 1 Vertiefungsmodul** | | **49** |

*Hinweis zur Priorisierung: Modul 9 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 9 voraus.* 1 UE = 45 Minuten.

### 2. Quellen und Stand

* **Verordnung (EU) 2016/679 (DSGVO)**, Fundstelle EUR-Lex (CELEX 32016R0679). Die Artikelnummern in diesem Lehrplan (u. a. Art. 4, 5, 6, 7, 9, 12 bis 22, 24, 25, 28, 30, 32 bis 35, 37 bis 39, 44 ff.) sind aus dem Fachwissen des Verfassers übernommen. **Der Wortlaut wurde nicht abgerufen und nicht geprüft** (EUR-Lex war für die Recherche nicht erreichbar). Vor dem Kurs im aktuellen Gesetzestext nachlesen.
* **Datenschutzgesetz (DSG, Österreich)** mit dem Grundrecht auf Datenschutz in § 1 und den Regeln zur Bildverarbeitung: *Fundstelle und aktueller Stand im RIS nicht geprüft*.
* **WKO, „EU-DSGVO: Meldung von Datenschutzverletzungen“** (<https://www.wko.at/datenschutz/eu-dsgvo-meldung-von-datenschutzverletzungen>, Seite zeigt 23.10.2026, abgerufen am 13.11.2026): Meldung an die Datenschutzbehörde so früh wie möglich, bei Überschreitung von 72 Stunden mit Begründung der Verspätung; keine Meldung bei voraussichtlich fehlendem Risiko; Benachrichtigung der Betroffenen bei hohem Risiko; alle Verletzungen sind zu dokumentieren; Auftragsverarbeiter melden unverzüglich an den Verantwortlichen; die Datenschutzbehörde bietet ein freiwilliges Online- und PDF-Formular an.
* **Datenschutzbehörde (dsb.gv.at)** für Muster und Formulare: *nicht abgerufen, nicht geprüft*.
* **EDSA (Europäischer Datenschutzausschuss)**, Leitlinien (u. a. zu Datenpannen): *nicht geprüft*.
* **RFC 1918** (IETF, Februar 1996) für private Adressen und **RFC 2606** (IETF, Juni 1999, Datum nicht geprüft) für `example.com`.

### 3. Labor-Setup & Rahmenbedingungen

* **Kein technisches Labor.** Es genügen Textverarbeitung, Tabellenkalkulation und optional Python 3.
* **Fiktives Unternehmen:** Alpenblick Reisen GmbH (Wien), 45 Mitarbeitende, Domäne `alpenblick.example.com`, Netz `10.50.0.0/24`, Kundenportal, Buchungssystem, E-Mail, Dateiablage, Videoüberwachung am Eingang, Dienstleister für Newsletter und Backup. Alle Angaben sind frei erfunden.
* **Material des Dozenten:** (1) Systemliste mit Datenarten (Beispiel), (2) Szenarien für Betroffenenanfragen, (3) Beschreibung einer Datenpanne, (4) Protokollauszug mit personenbezogenen Daten. Beispiele liegen der Übungsreihe bei und sind erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Grundbegriffe und Grundsätze
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende personenbezogene Daten, Verarbeitung, Verantwortlicher und Auftragsverarbeiter definieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Grundsätze der Verarbeitung (u. a. Zweckbindung, Datenminimierung, Speicherbegrenzung, Integrität und Vertraulichkeit) auf Beispiele aus der IT anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum IP-Adressen, E-Mail-Adressen und Protokolleinträge personenbezogen sein können.
* **Voraussetzungen:** keine.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Begriffe: personenbezogene Daten, Verarbeitung, Verantwortlicher, Auftragsverarbeiter | 2 |
| 1.2 | Grundsätze der Verarbeitung und Rechenschaftspflicht | 2 |
| 1.3 | Personenbezug in der IT (IP-Adresse, Kennung, Protokolle); Grundrecht und Aufsicht in Österreich im Überblick | 1 |

#### Praxisaufgaben
1. **Begriffe:** Ordne zehn Datenfelder der Alpenblick Reisen GmbH (u. a. Name, E-Mail, IP-Adresse, Buchungsnummer, anonymisierter Umsatz) „personenbezogen“ oder „nicht personenbezogen“ zu und begründe.
2. **Grundsätze:** Beurteile drei Situationen (Test mit echten Kundendaten, unbegrenzte Aufbewahrung der Logdateien, Admin-Zugriff für alle) nach den Grundsätzen und schlage Verbesserungen vor.
3. **Rollen:** Bestimme für Newsletter-Versand, Buchungssystem und Backup-Dienstleister, wer Verantwortlicher und wer Auftragsverarbeiter ist (Annahme, begründen).

#### Kontrollfragen
1. Wann ist eine IP-Adresse personenbezogen?
2. Was bedeutet Datenminimierung für eine Testumgebung?
3. Wer trägt die Rechenschaftspflicht?

### Modul 2: Rechtsgrundlagen der Verarbeitung
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rechtsgrundlagen für die Verarbeitung nennen und Beispielen zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Anforderungen an eine wirksame Einwilligung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende besondere Kategorien von Daten erkennen und den erhöhten Schutzbedarf begründen.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Rechtsgrundlagen im Überblick (Vertrag, rechtliche Verpflichtung, berechtigtes Interesse, Einwilligung u. a.) | 2 |
| 2.2 | Einwilligung: Anforderungen, Widerruf, Nachweis | 2 |
| 2.3 | Besondere Kategorien von Daten und Daten über Beschäftigte (Überblick) | 1 |

#### Praxisaufgaben
1. **Zuordnung:** Ordne fünf Verarbeitungen (Buchungsabwicklung, Newsletter, Zeiterfassung, Videoüberwachung am Eingang, Bewerbungen) einer Rechtsgrundlage zu und begründe; markiere, wo die Zuordnung rechtlich zu klären ist.
2. **Einwilligung:** Prüfe einen fiktiven Text für die Newsletter-Anmeldung anhand einer Checkliste (freiwillig, informiert, konkret, widerrufbar, nachweisbar) und verbessere ihn.
3. **Besondere Daten:** Finde in einer Beispielliste Felder mit besonderem Schutzbedarf (z. B. Gesundheitsangaben für eine Reiseversicherung) und lege zusätzliche Schutzmaßnahmen fest.

#### Kontrollfragen
1. Warum ist eine Einwilligung nicht immer die beste Rechtsgrundlage?
2. Wie weist man eine Einwilligung nach?
3. Welche Angaben gelten als besondere Kategorien?

### Modul 3: Betroffenenrechte
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Rechte der Betroffenen (Information, Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit, Widerspruch) benennen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer Betroffenenanfrage von der Identitätsprüfung bis zur Antwort beschreiben und Fristen berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die technische Umsetzung von Auskunft und Löschung in IT-Systemen (inklusive Backups) planen.
* **Voraussetzungen:** Modul 1 und 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Überblick über die Rechte der Betroffenen | 2 |
| 3.2 | Ablauf einer Anfrage: Identität, Frist, Antwort, Dokumentation | 2 |
| 3.3 | Technische Umsetzung: Suchen, Exportieren, Löschen, Sperren; Backups | 2 |

#### Praxisaufgaben
1. **Rechte zuordnen:** Ordne fünf Betroffenenanfragen (z. B. „Welche Daten haben Sie über mich?“, „Bitte löschen Sie mein Konto“) dem passenden Recht zu.
2. **Fristen:** Berechne mit `anfrage_frist.py` die Antwortfrist für mehrere Eingangsdaten (Annahme: ein Monat ab Eingang, Verlängerung nur mit Begründung; Rechtsfrist im Gesetz nachlesen).
3. **Systemlandkarte:** Erstelle für eine Auskunft eine Tabelle: System, Datenart, Suchschlüssel, Zuständiger, Exportformat. Beschreibe, wie Backups bei der Löschung behandelt werden (Annahme, rechtlich zu klären).

#### Kontrollfragen
1. Wie prüft man die Identität, ohne neue Daten zu sammeln?
2. Was ist bei einer Löschanfrage mit Backups zu beachten?
3. Warum gehört die Anfrage in ein Verzeichnis (Dokumentation)?

### Modul 4: Verzeichnis der Verarbeitungstätigkeiten
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Pflichtangaben eines Verzeichnisses der Verarbeitungstätigkeiten benennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Verzeichnis für ein fiktives Unternehmen erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende das Verzeichnis aus einer Systemliste ableiten und aktuell halten.
* **Voraussetzungen:** Modul 1 bis 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Zweck, Pflichtangaben und Form des Verzeichnisses | 2 |
| 4.2 | Verzeichnis erstellen: Zwecke, Kategorien, Empfänger, Fristen | 2 |
| 4.3 | Ableitung aus der Systemliste und Pflege | 1 |

#### Praxisaufgaben
1. **Vorlage:** Erstelle eine Tabellenvorlage mit den Pflichtangaben (Muster der Behörde nachlesen, Fundstelle nicht geprüft).
2. **Verzeichnis:** Trage mindestens fünf Verarbeitungen der Alpenblick Reisen GmbH ein (Zweck, Betroffene, Datenkategorien, Empfänger, Löschfrist, Maßnahmen).
3. **Abgleich:** Vergleiche das Verzeichnis mit der Systemliste und finde Systeme ohne Eintrag.

#### Kontrollfragen
1. Wozu dient das Verzeichnis, wer kann es verlangen?
2. Wer pflegt es, und wann wird es aktualisiert?
3. Wo liegt die Verbindung zur Asset-Verwaltung?

### Modul 5: Auftragsverarbeitung und Übermittlung in Drittländer
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Auftragsverarbeitung von gemeinsamer Verantwortlichkeit und eigener Verantwortung abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Mindestinhalte eines Auftragsverarbeitungsvertrags prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Übermittlungen in Drittländer erkennen und den Prüfbedarf beschreiben.
* **Voraussetzungen:** Modul 1 und 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Rollen: Verantwortlicher, Auftragsverarbeiter, gemeinsam Verantwortliche | 2 |
| 5.2 | Auftragsverarbeitungsvertrag: Mindestinhalte und Prüfung | 2 |
| 5.3 | Drittländer, Cloud-Dienste und Unterauftragsverarbeiter | 1 |

#### Praxisaufgaben
1. **Rollen:** Beurteile vier Dienstleister (Newsletter, Backup, Steuerberatung, Hosting) als Auftragsverarbeiter oder nicht (Annahme, rechtlich zu klären).
2. **Vertragsprüfung:** Prüfe einen fiktiven Auftragsverarbeitungsvertrag mit einer Checkliste (Weisung, Vertraulichkeit, Sicherheit, Unterauftragnehmer, Unterstützung bei Betroffenenrechten, Rückgabe oder Löschung, Kontrollrechte).
3. **Cloud:** Beschreibe für einen US-Cloud-Dienst, welche Fragen vor dem Einsatz zu klären sind (Standort der Daten, Übermittlungsgrundlage, Unterauftragnehmer); aktuelle Rechtslage dazu im Gesetz und bei der Behörde nachlesen, nicht geprüft.

#### Kontrollfragen
1. Wann ist ein Dienstleister Auftragsverarbeiter?
2. Welche Pflichten hat der Verantwortliche bei der Auswahl?
3. Was ist ein Drittland?

### Modul 6: Technische und organisatorische Maßnahmen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen nach dem Stand der Technik für ein Szenario auswählen und begründen.
  * Nach Abschluss dieses Moduls kann der Lernende Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen erklären und anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen dokumentieren und ihre Wirksamkeit prüfen.
* **Voraussetzungen:** Modul 1 bis 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Sicherheit der Verarbeitung: Auswahl nach Risiko | 2 |
| 6.2 | Datenschutz durch Technik und durch Voreinstellung | 2 |
| 6.3 | Dokumentation und Wirksamkeitsprüfung | 2 |

#### Praxisaufgaben
1. **Maßnahmen:** Wähle für das Kundenportal Maßnahmen aus den Gruppen Zugriff, Verschlüsselung, Pseudonymisierung, Verfügbarkeit, Wiederherstellung und Überprüfung aus und begründe sie nach Risiko (Technikdetails nur kurz, Verweis auf P12 und P16).
2. **Voreinstellungen:** Prüfe ein fiktives Anmeldeformular auf Datensparsamkeit und lege datenschutzfreundliche Voreinstellungen fest.
3. **Dokumentation:** Fasse die Maßnahmen in einer Tabelle zusammen (Maßnahme, Zweck, Verantwortlicher, Prüfintervall, Nachweis).

#### Kontrollfragen
1. Was bedeutet „Stand der Technik“ in der Praxis?
2. Wie unterscheiden sich Pseudonymisierung und Anonymisierung?
3. Wie weist man die Wirksamkeit von Maßnahmen nach?

### Modul 7: Datenpannen und Meldung
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Verletzung des Schutzes personenbezogener Daten erkennen und einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Risiko und Meldepflicht an die Behörde sowie Benachrichtigung der Betroffenen beurteilen und die Frist berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Meldung entwerfen und die Datenpanne dokumentieren.
* **Voraussetzungen:** Modul 1 und 6.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Begriff und Beispiele für Datenpannen | 1 |
| 7.2 | Risikobewertung, Meldung an die Behörde, Benachrichtigung der Betroffenen | 2 |
| 7.3 | Meldung entwerfen, Dokumentation, Ablauf im Betrieb | 2 |

#### Praxisaufgaben
1. **Einordnen:** Beurteile fünf Vorfälle (Verlust eines Laptops, falscher E-Mail-Empfänger, Ransomware, Fehlkonfiguration einer Freigabe, Ausfall ohne Datenverlust) als Datenpanne oder nicht und begründe.
2. **Frist:** Berechne mit `meldefrist.py` für mehrere Zeitpunkte der Feststellung die 72-Stunden-Frist (Beginn laut Quelle „ab Kenntnis“, genaue Auslegung rechtlich zu klären).
3. **Meldung:** Entwirf mit den Inhalten laut Quelle (Art der Verletzung, Kategorien und ungefähre Zahl, wahrscheinliche Folgen, Maßnahmen, Kontaktperson) eine Meldung zur Datenpanne des Dozenten und lege fest, ob die Betroffenen zu benachrichtigen sind.

#### Kontrollfragen
1. Wann ist keine Meldung an die Behörde nötig?
2. Wann sind die Betroffenen zu benachrichtigen?
3. Welche Panne muss intern dokumentiert werden, auch wenn sie nicht gemeldet wird?

### Modul 8: Protokollierung, Aufbewahrung und Praxisfälle aus der Administration
* **Priorität:** 1 · **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Protokollierung begründen und Zweck, Umfang und Aufbewahrungsdauer festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Löschfristen in einem Löschkonzept zusammenfassen und Aufbewahrungspflichten aus anderen Gesetzen berücksichtigen.
  * Nach Abschluss dieses Moduls kann der Lernende Praxisfälle der Administration (Administratorrechte, Mitarbeiterkontrolle, Videoüberwachung, Fernwartung, Tests) datenschutzrechtlich einordnen.
* **Voraussetzungen:** Modul 1 bis 7.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Protokollierung: Zweck, Umfang, Zugriff, Aufbewahrungsdauer | 2 |
| 8.2 | Löschkonzept und gesetzliche Aufbewahrungspflichten | 2 |
| 8.3 | Praxisfälle: Administratorrechte, Mitarbeiter, Videoüberwachung | 2 |
| 8.4 | Praxisfälle: Fernwartung, Tests, Entsorgung von Geräten | 2 |

#### Praxisaufgaben
1. **Protokolle:** Prüfe einen Protokollauszug (fiktiv) mit `protokoll_pruefen.py` auf personenbezogene Angaben und lege je Protokollart Zweck, Zugriff und Aufbewahrungsdauer fest (Dauer als Annahme, begründen).
2. **Löschkonzept:** Erstelle eine Tabelle Datenart, Frist, Grundlage der Frist, Löschverfahren (Fristen aus anderen Gesetzen z. B. Steuerrecht: Fundstelle nachlesen, nicht geprüft).
3. **Administratorrechte und Mitarbeiter:** Beurteile den Zugriff von Administratoren auf Postfächer und die Auswertung von Protokollen über Mitarbeitende und nenne, wer vorher einzubinden ist (z. B. Betriebsrat, Datenschutzbeauftragter, Rechtsabteilung; Rechtslage nicht geprüft).
4. **Videoüberwachung:** Bewerte die Kamera am Eingang (Zweck, Speicherdauer, Kennzeichnung, Zugriff); Regeln des DSG zur Bildverarbeitung nachlesen, nicht geprüft.
5. **Fernwartung und Tests:** Lege Regeln für Fernwartung durch Dienstleister, Testdaten und die Entsorgung von Datenträgern fest.

#### Kontrollfragen
1. Welche Protokolle brauchen eine kurze Aufbewahrung, welche eine längere?
2. Warum können Löschfristen und Aufbewahrungspflichten kollidieren?
3. Was ist bei der Auswertung von Protokollen über Mitarbeitende zu beachten?

### Modul 9: Datenschutz-Folgenabschätzung und Datenschutzbeauftragter
* **Priorität:** 2 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, wann eine Datenschutz-Folgenabschätzung nötig sein kann, und den Ablauf skizzieren.
  * Nach Abschluss dieses Moduls kann der Lernende Aufgaben und Stellung des Datenschutzbeauftragten beschreiben.
* **Voraussetzungen:** Modul 6.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Datenschutz-Folgenabschätzung: Anlass, Ablauf, Ergebnis | 2 |
| 9.2 | Datenschutzbeauftragter: Benennung, Aufgaben, Zusammenarbeit mit der IT | 2 |

#### Praxisaufgaben
1. **DSFA:** Prüfe, ob für ein neues Kundenportal mit Profilbildung eine Folgenabschätzung nötig sein kann (Kriterienliste der Behörde nachlesen, nicht geprüft), und skizziere die Schritte (Beschreibung, Notwendigkeit, Risiken, Maßnahmen).
2. **Zusammenarbeit:** Beschreibe, bei welchen IT-Vorhaben der Datenschutzbeauftragte früh einzubinden ist (Beschaffung, neue Systeme, Dienstleisterwechsel).

#### Kontrollfragen
1. Wann kann eine Folgenabschätzung erforderlich sein?
2. Welche Rolle hat der Datenschutzbeauftragte gegenüber der Geschäftsleitung?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P47 erstellt (Annahmen: fiktive Alpenblick Reisen GmbH, kein Labor, Österreich und EU). Stunden: 5+5+6+5+5+6+5+8+4 = 49 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 8×1, 1×2.

**Nicht bestätigt:** Wortlaut aller DSGVO-Artikel und -Fristen (EUR-Lex nicht abrufbar), österreichisches DSG (RIS nicht geprüft), Muster und Kriterienlisten der Datenschutzbehörde, Aufbewahrungsfristen aus anderen Gesetzen, Rechtslage zu Drittlandübermittlungen, Videoüberwachung und Mitarbeiterkontrolle. Aus einer geprüften Sekundärquelle (WKO, Stand 23.10.2026) stammen nur die Angaben zur Meldung von Datenpannen. Kein Rechtsrat.

**Offen:** Zeitaufwand unerprobt; der Lehrplan wurde von Matija noch nicht geprüft.
