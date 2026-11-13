# Lehrplan: NIS2 für Administratoren

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 8 Module, 46 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | NIS-2-Richtlinie und österreichische Umsetzung (NISG 2026), Informationssicherheit im Betrieb; Tabellenkalkulation und Textverarbeitung für Vorlagen; optional Python 3 für Fristrechnungen |
| **Thematische Abgrenzung (Out of Scope)** | **Kein Rechtsrat:** Aussagen sind Kursannahmen und von Juristen oder Fachstellen zu prüfen. Kein technisches Labor. Technische Maßnahmen (Härtung, Backup, Monitoring, Kryptografie) werden nur in ihrem Bezug zu den Pflichten behandelt, mit Verweis auf die eigenen Lehrpläne (P12 IT-Sicherheitsgrundlagen, P13 Windows-Server-Härtung, P14 Linux-Server-Härtung, P15 Schwachstellenmanagement, P16 Kryptografie, P17 Monitoring mit Zabbix, P19 Zentrales Logging, P35 Backup-Konzept, P36 Notfallplanung). Keine Überschneidung mit P47 (Datenschutz) und P49 (ISO 27001) über kurze Verweise hinaus. Keine Zertifizierungsvorbereitung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen und Rechtsrahmen | 1 | 5 |
| 2 | Anwendungsbereich und Einstufung | 1 | 6 |
| 3 | Pflichten im Überblick und Leitungsorgane | 1 | 5 |
| 4 | Risikomanagementmaßnahmen, Teil 1: Risiko, Vorfälle, Betriebskontinuität | 1 | 7 |
| 5 | Risikomanagementmaßnahmen, Teil 2: Härtung, Zugriff, Schwachstellen, Kryptografie | 1 | 6 |
| 6 | Meldepflichten bei erheblichen Vorfällen | 1 | 6 |
| 7 | Lieferkette und Dienstleister | 1 | 5 |
| 8 | Nachweise, Aufsicht und Umsetzungsplan | 2 | 6 |
| **Gesamt** | **7 Pflichtmodule, 1 Vertiefungsmodul** | | **46** |

*Hinweis zur Priorisierung: Modul 8 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 8 voraus.* 1 UE = 45 Minuten.

### 2. Quellen und Stand (13.11.2026)

* **Richtlinie (EU) 2022/2555 (NIS-2-Richtlinie)**, EUR-Lex (CELEX 32022L2555). Der Wortlaut war auf EUR-Lex nicht abrufbar. Für Art. 21 Abs. 2 (Risikomanagementmaßnahmen a bis j) und Art. 23 (Meldepflichten) wurden Wiedergaben auf den Seiten gesetze.legal (<https://gesetze.legal/eu/rl_2022_2555_eu/21>) und gesetzefinden.at (<https://gesetzefinden.at/eu-recht/richtlinien/nis-2-rl/artikel-23>) gelesen (abgerufen am 13.11.2026). **Die Fassung auf EUR-Lex ist maßgeblich und wurde nicht verglichen.**
* **Österreichisches Netz- und Informationssystemsicherheitsgesetz 2026 (NISG 2026)**, laut RIS-Link BGBl. I Nr. 94/2025 (<https://ris.bka.gv.at/eli/bgbl/i/2025/94/P0/NOR40277627>). **Der Gesetzestext konnte nicht abgerufen werden** (RIS sperrt den automatischen Abruf). Die Angaben zu Stand und Fristen stammen aus der Sekundärquelle **Austrian Standards, „NIS-2 und NISG 2026“** (<https://www.austrian-standards.at/de/standardisierung/aktuelle-themen/technologie-innovation/nis-2>, ohne Datum der Seite, abgerufen am 13.11.2026):
  * Kundmachung am 23.12.2025, Inkrafttreten am 01.10.2026 (neun Monate danach), das NISG 2018 gilt bis 30.09.2026.
  * Ab 01.10.2026: Risikomanagementmaßnahmen, Lieferkettensicherheit und Meldepflichten; Leitungsorgane haben bis dahin eine Cybersicherheitsschulung zu absolvieren.
  * Registrierung: im Fließtext 31.12.2026, in der Fristenübersicht 01.01.2027 (**Widerspruch in der Quelle, nicht geklärt**). Selbstdeklaration: 30.09.2027 bzw. 01.10.2027 (ebenfalls uneinheitlich).
  * Nachweise durch unabhängige Prüfung auf Aufforderung frühestens ab 01.10.2028.
  * Betroffene: mittlere und große Unternehmen (Schwelle laut Quelle ab 50 Beschäftigten oder mehr als 10 Mio. EUR Umsatz oder Bilanzsumme, Formulierung uneinheitlich) in Sektoren der Anlagen 1 (hohe Kritikalität) und 2 (sonstige kritische Sektoren); wesentliche und wichtige Einrichtungen; Sanktionen bis 10 Mio. EUR oder 2 % (wesentlich) bzw. bis 7 Mio. EUR oder 1,4 % (wichtig) des weltweiten Jahresumsatzes.
* **Abweichung bei der Frist des Abschlussberichts:** Austrian Standards nennt „einen Monat nach der Frühwarnung“, die Wiedergabe von Art. 23 nennt „einen Monat nach der Meldung (72 Stunden)“. Im Kurs gilt die Frist **laut Richtlinie** mit dem Hinweis, den Gesetzestext zu prüfen.
* **Durchführungsverordnung (EU) 2024/2690** (technische und methodische Anforderungen für bestimmte digitale Dienste): nur als Hinweis genannt, *nicht geprüft*.
* **ENISA, NIS-Kooperationsgruppe, Leitfäden des Bundeskanzleramts oder des Computer-Notfallteams** (u. a. CERT.at, GovCERT): *nicht geprüft*.
* **RFC 1918** (IETF, Februar 1996) und **RFC 2606** (IETF, Juni 1999, Datum nicht geprüft) für Adressen und `example.com`.

### 3. Labor-Setup & Rahmenbedingungen

* **Kein technisches Labor.** Es genügen Textverarbeitung, Tabellenkalkulation und optional Python 3.
* **Fiktives Unternehmen:** Donauwerk Fertigungs GmbH (Linz), 120 Mitarbeitende, Umsatz 28 Mio. EUR (erfunden), Produktion von Maschinenteilen (Sektor „Produktion“ als Annahme), Domäne `donauwerk.example.com`, Netz `10.60.0.0/22`, ERP, Fertigungsnetz, Fernwartung durch Maschinenlieferanten, Cloud-Backup, zwei Dienstleister. Alle Angaben sind frei erfunden.
* **Material des Dozenten:** (1) Firmenprofil für die Einstufung, (2) Systemliste mit Kritikalität, (3) Vorfallbeschreibung mit Zeitstempeln, (4) Lieferantenliste. Beispiele liegen der Übungsreihe bei und sind erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen und Rechtsrahmen
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ziel und Aufbau der NIS-2-Richtlinie und ihrer österreichischen Umsetzung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Richtlinie, nationales Gesetz und Verordnungen unterscheiden und den Stand der Umsetzung mit Datum nennen.
  * Nach Abschluss dieses Moduls kann der Lernende NIS2 von DSGVO und ISO 27001 abgrenzen.
* **Voraussetzungen:** keine.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Ziel und Aufbau der NIS-2-Richtlinie | 2 |
| 1.2 | Umsetzung in Österreich: NISG 2026, Stand und Fristen | 2 |
| 1.3 | Abgrenzung zu DSGVO und ISO 27001 | 1 |

#### Praxisaufgaben
1. **Rechtsakte:** Erstelle eine Tabelle Rechtsakt, Ebene (EU/Österreich), Wirkung, Fundstelle, Stand. Trage mindestens NIS-2-Richtlinie und NISG 2026 ein und kennzeichne, was nicht geprüft ist.
2. **Zeitleiste:** Zeichne die Fristen laut Austrian Standards auf einer Zeitleiste (23.12.2025, 01.10.2026, Registrierung, Selbstdeklaration, 01.10.2028) und markiere die Widersprüche der Quelle.
3. **Abgrenzung:** Nenne für einen Vorfall (Angriff auf das ERP mit Kundendaten) die Pflichten nach NIS2, nach DSGVO und die Rolle einer ISO-27001-Zertifizierung.

#### Kontrollfragen
1. Warum braucht eine EU-Richtlinie ein nationales Gesetz?
2. Seit wann gelten die Pflichten laut Quelle, und welche Quelle wäre maßgeblich?
3. Was unterscheidet NIS2 von der DSGVO?

### Modul 2: Anwendungsbereich und Einstufung
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende prüfen, ob ein Unternehmen nach Größe und Sektor in den Anwendungsbereich fällt.
  * Nach Abschluss dieses Moduls kann der Lernende zwischen wesentlichen und wichtigen Einrichtungen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Registrierung und Selbstdeklaration als Aufgaben beschreiben und Unsicherheiten der Einstufung dokumentieren.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Größenkriterien und Sektoren (Anlagen 1 und 2) | 2 |
| 2.2 | Wesentliche und wichtige Einrichtungen | 2 |
| 2.3 | Registrierung, Selbstdeklaration und Sonderfälle (kleine Unternehmen, Lieferkette) | 2 |

#### Praxisaufgaben
1. **Prüfung:** Prüfe mit `einstufung.py` drei fiktive Unternehmen (Größe, Umsatz, Sektor) nach der **Kursregel** (aus der Sekundärquelle abgeleitet, rechtlich zu prüfen).
2. **Einstufung Donauwerk:** Stufe die Donauwerk Fertigungs GmbH ein, begründe jeden Schritt und markiere Unsicherheiten (Sektorzuordnung, Konzernbezug, Zählweise der Beschäftigten).
3. **Registrierung:** Lege fest, welche Angaben für die Registrierung zusammenzustellen sind (Annahme, Fristen siehe Quelle mit Widerspruch) und wer im Unternehmen zuständig ist.

#### Kontrollfragen
1. Wann kann auch ein kleines Unternehmen betroffen sein?
2. Welche Rolle spielt der Sektor?
3. Warum ist die Einstufung zu dokumentieren?

### Modul 3: Pflichten im Überblick und Leitungsorgane
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Pflichten (Risikomanagement, Meldung, Registrierung, Nachweis) im Überblick benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Verantwortung und Schulungspflicht der Leitungsorgane beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Pflichten Rollen im Unternehmen zuordnen.
* **Voraussetzungen:** Modul 1 und 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Pflichten im Überblick | 2 |
| 3.2 | Verantwortung und Schulung der Leitungsorgane | 2 |
| 3.3 | Rollen und Zuständigkeiten im Unternehmen | 1 |

#### Praxisaufgaben
1. **Pflichtenliste:** Erstelle eine Tabelle Pflicht, Quelle, Frist, Verantwortlicher für die Donauwerk Fertigungs GmbH.
2. **Leitungsorgan:** Entwirf ein Briefing für die Geschäftsführung (eine Seite: Pflichten, Haftungsrisiko laut Quelle, Schulungsbedarf, Entscheidungen) ohne Rechtsberatung.
3. **RACI:** Ordne die Pflichten Geschäftsführung, IT-Leitung, Administration und Einkauf zu.

#### Kontrollfragen
1. Welche Pflichten betreffen die Leitung unmittelbar?
2. Was bedeutet die Schulungspflicht in der Praxis?
3. Wer in der IT arbeitet an welchen Pflichten mit?

### Modul 4: Risikomanagementmaßnahmen, Teil 1: Risiko, Vorfälle, Betriebskontinuität
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Maßnahmenliste der Richtlinie (Art. 21 Abs. 2) in eigenen Worten wiedergeben.
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache Risikoanalyse für Systeme durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Vorfallbehandlung und Betriebskontinuität (Backup, Notfallwiederherstellung, Krisenmanagement) mit den Pflichten verknüpfen.
* **Voraussetzungen:** Modul 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Maßnahmenliste nach Art. 21 Abs. 2 im Überblick | 2 |
| 4.2 | Risikoanalyse: Werte, Bedrohungen, Eintritt und Auswirkung | 3 |
| 4.3 | Vorfallbehandlung und Betriebskontinuität (Backup, Wiederherstellung, Krise) | 2 |

#### Praxisaufgaben
1. **Maßnahmenliste:** Gib die zehn Gruppen der Maßnahmen sinngemäß wieder (Risikoanalyse, Vorfälle, Betriebskontinuität, Lieferkette, Beschaffung und Schwachstellen, Wirksamkeitsprüfung, IT-Hygiene und Schulung, Kryptografie, Personal und Zugriff, Authentifizierung und Kommunikation) und ordne je Gruppe eine Frage für die Donauwerk Fertigungs GmbH zu.
2. **Risikoanalyse:** Bewerte mit `risikomatrix.py` zehn Systeme nach Eintritt und Auswirkung (Skalen 1 bis 5, Annahme) und priorisiere.
3. **Kontinuität:** Beschreibe für das ERP Ziel für Wiederanlauf und Datenverlust (Annahmen) und nenne, welche Maßnahmen dafür nötig sind (Verweis auf P35 und P36, nur kurz).

#### Kontrollfragen
1. Welche Maßnahmen betreffen die Betriebskontinuität?
2. Warum sind Skalen und Annahmen der Risikoanalyse zu dokumentieren?
3. Wie hängt die Vorfallbehandlung mit der Meldepflicht zusammen?

### Modul 5: Risikomanagementmaßnahmen, Teil 2: Härtung, Zugriff, Schwachstellen, Kryptografie
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Härtung, Schwachstellenmanagement und IT-Hygiene den Maßnahmen der Richtlinie zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffskontrolle, Anlagenverwaltung und Mehr-Faktor-Authentifizierung als Pflichtbestandteile beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Kryptografie-Konzepte und Wirksamkeitsprüfungen planen und dokumentieren.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Härtung, Patch- und Schwachstellenmanagement, IT-Hygiene | 2 |
| 5.2 | Zugriffskontrolle, Anlagenverwaltung, Mehr-Faktor-Authentifizierung | 2 |
| 5.3 | Kryptografie-Konzept und Wirksamkeitsprüfung | 2 |

#### Praxisaufgaben
1. **Lückenanalyse:** Prüfe mit einer Checkliste die Donauwerk-Fertigungs-Maßnahmen (fiktive Antworten) auf Lücken bei Härtung, Patchen und Schwachstellen und leite Maßnahmen ab (technische Details nur Verweis auf P13, P14, P15).
2. **Zugriff:** Erstelle ein Zugriffs- und Anlagenverzeichnis (System, Verantwortlicher, Kritikalität, Authentifizierung) und markiere Systeme ohne Mehr-Faktor-Authentifizierung.
3. **Wirksamkeit:** Lege für fünf Maßnahmen fest, wie ihre Wirksamkeit geprüft wird (Kennzahl, Intervall, Nachweis).

#### Kontrollfragen
1. Warum gehört die Anlagenverwaltung zur Cybersicherheit?
2. Wann ist Mehr-Faktor-Authentifizierung besonders wichtig?
3. Wie weist man die Wirksamkeit einer Maßnahme nach?

### Modul 6: Meldepflichten bei erheblichen Vorfällen
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen erheblichen Vorfall nach den Kriterien beurteilen (Annahme: Kriterien laut Gesetz nachlesen).
  * Nach Abschluss dieses Moduls kann der Lernende die gestuften Fristen (Frühwarnung, Meldung, Abschlussbericht) berechnen und Zeitleisten erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Meldeinhalte entwerfen und den internen Meldeprozess festlegen.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Erheblicher Vorfall: Kriterien und Beispiele | 2 |
| 6.2 | Gestufte Meldung: Fristen und Inhalte | 2 |
| 6.3 | Interner Meldeprozess und Abgrenzung zur Meldung nach DSGVO | 2 |

#### Praxisaufgaben
1. **Beurteilung:** Beurteile fünf Vorfälle (Ransomware im ERP, Ausfall der Fertigung, Phishing ohne Folge, Datenabfluss, Störung beim Lieferanten) als erheblich oder nicht, mit Begründung und markierter Unsicherheit.
2. **Fristen:** Berechne mit `meldefristen.py` für mehrere Zeitpunkte der Kenntnis die Frist der Frühwarnung (24 Stunden), der Meldung (72 Stunden) und des Abschlussberichts (ein Monat nach der Meldung laut Richtlinie, siehe Quellenhinweis).
3. **Prozess:** Entwirf ein Ablaufdiagramm von der Entdeckung bis zum Abschlussbericht (Rollen, Entscheidungen, Vorlagen) und nenne, welche Meldung zusätzlich an die Datenschutzbehörde nach DSGVO zu prüfen ist (Verweis auf P47).

#### Kontrollfragen
1. Welche Inhalte hat die Frühwarnung, welche die Meldung?
2. Was passiert, wenn der Vorfall beim Abschlussbericht noch andauert?
3. Warum sind Meldungen nach NIS2 und DSGVO getrennt zu prüfen?

### Modul 7: Lieferkette und Dienstleister
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Risiken durch Lieferanten und Dienstleister erkennen und einstufen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherheitsanforderungen in Verträgen und Bewertungen festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Lieferantenverzeichnis führen.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Lieferkettenrisiken und Kritikalität von Dienstleistern | 2 |
| 7.2 | Sicherheitsanforderungen in Verträgen und Bewertungen | 2 |
| 7.3 | Lieferantenverzeichnis und laufende Überwachung | 1 |

#### Praxisaufgaben
1. **Einstufung:** Stufe die Lieferanten der Donauwerk Fertigungs GmbH (Fernwartung, Cloud-Backup, Hosting, Software) nach Kritikalität ein.
2. **Anforderungen:** Erstelle eine Anforderungsliste für Verträge (Meldung von Vorfällen, Zugriffsrechte, Fernwartung, Unterauftragnehmer, Nachweise) ohne Rechtsberatung.
3. **Verzeichnis:** Lege ein Lieferantenverzeichnis an (Dienst, Kritikalität, Ansprechpartner, Nachweise, Überprüfungsdatum).

#### Kontrollfragen
1. Warum betrifft NIS2 auch Unternehmen, die selbst nicht erfasst sind?
2. Welche Anforderungen gehören in jeden Vertrag mit Fernwartung?
3. Wie oft ist ein Lieferant zu überprüfen?

### Modul 8: Nachweise, Aufsicht und Umsetzungsplan
* **Priorität:** 2 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aufsicht, Nachweispflichten und Sanktionsrahmen laut Quelle beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle von Protokollierung und Überwachung als Nachweis beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Lückenanalyse und einen Umsetzungsplan erstellen.
* **Voraussetzungen:** Modul 4 bis 7.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Aufsicht, Nachweise und Sanktionsrahmen | 2 |
| 8.2 | Protokollierung, Überwachung und Nachweise im Betrieb (Verweis auf P17, P19) | 2 |
| 8.3 | Lückenanalyse und Umsetzungsplan | 2 |

#### Praxisaufgaben
1. **Nachweise:** Liste für jede Pflicht den Nachweis (Dokument, Protokoll, Bericht) und die Aufbewahrung auf; Fristen der Prüfung laut Quelle (frühestens 01.10.2028 auf Aufforderung) vermerken.
2. **Überwachung:** Lege fest, welche Ereignisse protokolliert und welche Meldungen überwacht werden (nur Konzept, Werkzeuge siehe P17 und P19).
3. **Plan:** Erstelle eine Lückenanalyse mit Reifegrad je Maßnahme (0 bis 3, Annahme) und einen Umsetzungsplan mit Verantwortlichen, Terminen und Prioritäten; markiere die Registrierungs- und Meldefristen.

#### Kontrollfragen
1. Welche Folgen können Verstöße haben (Rahmen laut Quelle)?
2. Warum sind Protokolle ein Nachweis?
3. Wie priorisiert man Lücken?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P48 erstellt (Annahmen: fiktive Donauwerk Fertigungs GmbH, kein Labor, Österreich und EU). Stunden: 5+6+5+7+6+6+5+6 = 46 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 7×1, 1×2.

**Umsetzungsstand in Österreich mit Datum:** Laut der Sekundärquelle Austrian Standards (abgerufen am 13.11.2026, Seite ohne Datum) ist das NISG 2026 am 01.10.2026 in Kraft getreten; Registrierung, Selbstdeklaration und Nachweise haben spätere Fristen (siehe Quellen, mit Widersprüchen der Quelle). **Der Gesetzestext im RIS wurde nicht gelesen.** Der aktuelle Stand ist vor dem Kurs im RIS und bei der zuständigen Behörde zu prüfen.

**Nicht bestätigt:** Wortlaut von Richtlinie und Gesetz, genaue Schwellen und Sektorlisten, Kriterien des erheblichen Vorfalls, Fristen der Registrierung und Selbstdeklaration, Frist des Abschlussberichts im österreichischen Gesetz, Sanktionsrahmen. Kein Rechtsrat.

**Offen:** Zeitaufwand unerprobt; der Lehrplan wurde von AnsibleArtisan4711 noch nicht geprüft.
