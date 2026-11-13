# Lehrplan: ISO 27001 Grundlagen

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 9 Module, 49 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | ISO/IEC 27001 und Informationssicherheits-Managementsystem (ISMS); Tabellenkalkulation und Textverarbeitung für Vorlagen; optional Python 3 für kleine Rechenhilfen |
| **Thematische Abgrenzung (Out of Scope)** | **Kein Normtext:** Die Norm ist urheberrechtlich geschützt. Der Kurs gibt Inhalte nur sinngemäß und mit eigenen Beispielen wieder; die Lernenden beschaffen die Norm selbst. **Kein Rechtsrat.** Kein technisches Labor. Technische Maßnahmen werden nur im Bezug zum ISMS behandelt, mit kurzem Verweis auf die eigenen Lehrpläne (P12 IT-Sicherheitsgrundlagen, P16 Kryptografie, P35 Backup-Konzept, P40 ITIL 4). Keine Überschneidung mit P47 (Datenschutz) und P48 (NIS2) über kurze Verweise hinaus. Keine Vorbereitung auf eine Prüfung zum Auditor oder Manager. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Informationssicherheit, ISMS und Normfamilie | 1 | 5 |
| 2 | Kontext, interessierte Parteien und Geltungsbereich | 1 | 5 |
| 3 | Führung, Politik, Rollen und Verantwortung | 1 | 5 |
| 4 | Risikomanagement: Bewertung und Behandlung | 1 | 7 |
| 5 | Maßnahmen im Überblick und Erklärung zur Anwendbarkeit | 1 | 7 |
| 6 | Unterstützung und dokumentierte Information | 1 | 5 |
| 7 | Betrieb, Überwachung, interne Audits und Managementbewertung | 1 | 6 |
| 8 | Verbesserung und Zertifizierung | 1 | 5 |
| 9 | Bezug zum Betrieb: ISMS im IT-Alltag | 2 | 4 |
| **Gesamt** | **8 Pflichtmodule, 1 Vertiefungsmodul** | | **49** |

*Hinweis zur Priorisierung: Modul 9 (Priorität 2) dient der Vertiefung und kann bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt Modul 9 voraus.* 1 UE = 45 Minuten.

### 2. Quellen und Stand (13.11.2026)

* **ISO/IEC 27001:2022** („Information security, cybersecurity and privacy protection, Information security management systems, Requirements“) mit **Amendment 1:2024 „Climate action changes“**, veröffentlicht Februar 2024 (iso.org, <https://www.iso.org/standard/88435.html>, abgerufen am 13.11.2026). Laut dieser Seite ist die Ausgabe 2022 die Basisnorm und die Änderung von 2024 gilt für sie. **Inhalt der Änderung ist nicht bekannt**; die Seite nennt keine Einzelheiten. Die **Norm selbst wurde nicht gelesen.**
* **Aufbau der Norm (Klauseln 4 bis 10, Anhang A):** Die Gliederung ist aus dem Fachwissen des Verfassers übernommen und **nicht an der Norm geprüft**. Dasselbe gilt für die Anzahl der Maßnahmen in Anhang A (laut Fachwissen 93 Maßnahmen in vier Themen: organisatorisch, personenbezogen, physisch, technologisch).
* **ISO/IEC 27002** (Leitfaden zu Maßnahmen) und **ISO/IEC 27005** (Informationssicherheits-Risikomanagement): nur als Hinweis genannt, *nicht geprüft*.
* **Österreichische Normenausgabe (ÖNORM EN ISO/IEC 27001)** und Auswahl akkreditierter Zertifizierungsstellen: *nicht geprüft*; vor dem Kurs beim Normungsinstitut bzw. bei der Akkreditierungsstelle nachlesen.
* **Richtlinie (EU) 2022/2555 (NIS 2)** und **DSGVO**: nur als Bezug (siehe P48, P47), *nicht geprüft*.
* **RFC 1918** (IETF, Februar 1996) und **RFC 2606** (IETF, Juni 1999, Datum nicht geprüft) für Adressen und `example.com`.

### 3. Labor-Setup & Rahmenbedingungen

* **Kein technisches Labor.** Es genügen Textverarbeitung, Tabellenkalkulation und optional Python 3.
* **Fiktives Unternehmen:** Silbersee Software GmbH (Graz), 80 Mitarbeitende, Entwicklung und Betrieb einer Branchenlösung als Software-as-a-Service, Domäne `silbersee.example.com`, Netz `10.70.0.0/23`, zwei Standorte, Cloud-Hosting durch einen Dienstleister. Alle Angaben sind frei erfunden.
* **Material des Dozenten:** (1) Beschreibung des Unternehmens und seiner Interessenträger, (2) Liste von Werten (Assets) mit Eigentümern, (3) Auditfeststellungen aus einem fiktiven internen Audit, (4) Zertifizierungsablauf als Fallbeispiel. Beispiele liegen der Übungsreihe bei und sind erfunden.

## B. Detaillierter Modulaufbau

### Modul 1: Informationssicherheit, ISMS und Normfamilie
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Vertraulichkeit, Integrität und Verfügbarkeit mit Beispielen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Informationssicherheits-Managementsystem (ISMS) beschreiben und von einzelnen technischen Maßnahmen abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Normfamilie (27001, 27002, 27005) einordnen und die Ausgabe mit Stand nennen.
* **Voraussetzungen:** keine.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Schutzziele: Vertraulichkeit, Integrität, Verfügbarkeit | 2 |
| 1.2 | Was ist ein ISMS? Nutzen, Aufbau, Abgrenzung | 2 |
| 1.3 | Normfamilie und Ausgabe mit Stand | 1 |

#### Praxisaufgaben
1. **Schutzziele:** Ordne zehn Vorfälle der Silbersee Software GmbH (z. B. Datenabfluss, Ransomware, Ausfall des Hostings, Manipulation von Quellcode) dem verletzten Schutzziel zu.
2. **ISMS:** Beschreibe den Unterschied zwischen einer Firewall und einem ISMS in eigenen Worten und nenne drei Aufgaben, die nur ein Managementsystem erfüllt.
3. **Normfamilie:** Erstelle eine Tabelle Norm, Zweck, zertifizierbar ja/nein (Annahme, nicht an der Norm geprüft), Stand der Ausgabe.

#### Kontrollfragen
1. Welches Schutzziel verletzt ein Datenabfluss?
2. Warum reicht eine technische Maßnahme allein nicht für ein ISMS?
3. Welche Ausgabe der Norm gilt, und woher weiß man das?

### Modul 2: Kontext, interessierte Parteien und Geltungsbereich
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende interne und externe Themen des Kontexts analysieren.
  * Nach Abschluss dieses Moduls kann der Lernende interessierte Parteien mit ihren Anforderungen erfassen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Geltungsbereich mit Schnittstellen und Ausschlüssen festlegen und begründen.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Kontextanalyse: interne und externe Themen | 2 |
| 2.2 | Interessierte Parteien und ihre Anforderungen | 1 |
| 2.3 | Geltungsbereich: Grenzen, Schnittstellen, Ausschlüsse | 2 |

#### Praxisaufgaben
1. **Kontext:** Erstelle für die Silbersee Software GmbH eine Tabelle interner und externer Themen (z. B. Fachkräfte, Kundenvorgaben, Gesetze, Cloud-Abhängigkeit).
2. **Parteien:** Liste Kunden, Mitarbeitende, Behörden und Dienstleister mit ihren Anforderungen an die Informationssicherheit.
3. **Geltungsbereich:** Formuliere einen Geltungsbereich (Standorte, Prozesse, Systeme) und begründe, was ausgeschlossen wird und welche Schnittstellen zu Dritten bestehen.

#### Kontrollfragen
1. Warum beginnt das ISMS mit dem Kontext?
2. Welche Folgen hat ein zu eng gewählter Geltungsbereich?
3. Wie geht man mit Dienstleistern am Rand des Geltungsbereichs um?

### Modul 3: Führung, Politik, Rollen und Verantwortung
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Verantwortung der obersten Leitung für das ISMS beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Informationssicherheitspolitik mit Zielen entwerfen.
  * Nach Abschluss dieses Moduls kann der Lernende Rollen, Befugnisse und Berichtswege festlegen.
* **Voraussetzungen:** Modul 2.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Verantwortung und Engagement der Leitung | 1 |
| 3.2 | Informationssicherheitspolitik und Ziele | 2 |
| 3.3 | Rollen, Befugnisse und Berichtswege | 2 |

#### Praxisaufgaben
1. **Leitung:** Beschreibe fünf Aufgaben der Geschäftsführung im ISMS (Ressourcen, Politik, Rollen, Bewertung, Förderung) mit je einem Beispiel.
2. **Politik:** Entwirf eine einseitige Informationssicherheitspolitik (Zweck, Geltungsbereich, Grundsätze, Verantwortliche) und drei messbare Ziele.
3. **Rollen:** Lege Rollen (Geschäftsführung, Informationssicherheitsbeauftragter, Systemverantwortliche, Mitarbeitende) in einer RACI-Tabelle fest.

#### Kontrollfragen
1. Warum darf die Leitung die Verantwortung nicht delegieren?
2. Was macht ein Sicherheitsziel messbar?
3. Wer berichtet an wen?

### Modul 4: Risikomanagement: Bewertung und Behandlung
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Methode zur Risikobewertung mit Skalen und Akzeptanzkriterien festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken für Werte identifizieren, bewerten und priorisieren.
  * Nach Abschluss dieses Moduls kann der Lernende Risikobehandlungsoptionen auswählen und einen Risikobehandlungsplan erstellen.
* **Voraussetzungen:** Modul 2 und 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Methode: Skalen, Akzeptanzkriterien, Wiederholbarkeit | 2 |
| 4.2 | Risikoidentifikation und -bewertung | 3 |
| 4.3 | Risikobehandlung, Restrisiko und Risikobehandlungsplan | 2 |

#### Praxisaufgaben
1. **Methode:** Definiere Skalen für Eintritt und Auswirkung (1 bis 5), eine Risikomatrix und ein Akzeptanzkriterium (Annahme, begründen).
2. **Bewertung:** Bewerte mit `risikoregister.py` zehn Risiken der Silbersee Software GmbH nach der Methode und sortiere sie.
3. **Behandlung:** Wähle je Risiko eine Option (vermeiden, verringern, teilen, akzeptieren), ergänze den Risikoeigner und das Restrisiko und fasse alles in einem Risikobehandlungsplan zusammen.

#### Kontrollfragen
1. Warum muss die Methode wiederholbar sein?
2. Wer entscheidet über die Akzeptanz des Restrisikos?
3. Was unterscheidet „verringern“ von „teilen“?

### Modul 5: Maßnahmen im Überblick und Erklärung zur Anwendbarkeit
* **Priorität:** 1 · **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Themenbereiche der Maßnahmen im Anhang A (organisatorisch, personenbezogen, physisch, technologisch) mit eigenen Beispielen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen aus dem Risikobehandlungsplan ableiten und begründen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Erklärung zur Anwendbarkeit (Statement of Applicability) erstellen.
* **Voraussetzungen:** Modul 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Themenbereiche der Maßnahmen im Überblick | 3 |
| 5.2 | Maßnahmen aus Risiken ableiten und begründen | 2 |
| 5.3 | Erklärung zur Anwendbarkeit: Aufbau und Pflege | 2 |

#### Praxisaufgaben
1. **Themen:** Beschreibe je Themenbereich drei Maßnahmen in eigenen Worten mit einem Beispiel aus der Silbersee Software GmbH (die Maßnahmentexte der Norm nicht abschreiben).
2. **Ableitung:** Ordne den fünf höchsten Risiken aus Modul 4 passende Maßnahmen zu.
3. **Anwendbarkeit:** Erstelle eine Tabelle Maßnahme, anwendbar ja/nein, Begründung, Umsetzungsstand, Nachweis für mindestens 20 Maßnahmen (Auswahl eigene Beispiele, Verweis auf Norm und Leitfaden).

#### Kontrollfragen
1. Warum ist die Erklärung zur Anwendbarkeit nötig?
2. Darf eine Maßnahme als „nicht anwendbar“ gelten, und wie ist das zu begründen?
3. Wie hängen Risiko, Maßnahme und Nachweis zusammen?

### Modul 6: Unterstützung und dokumentierte Information
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ressourcen, Kompetenz, Bewusstsein und Kommunikation als Unterstützungsanforderungen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende zwischen Dokumenten und Aufzeichnungen unterscheiden und eine Dokumentenlenkung festlegen.
* **Voraussetzungen:** Modul 3.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Ressourcen, Kompetenz, Bewusstsein, Kommunikation | 2 |
| 6.2 | Dokumentierte Information: Erstellen, Lenken, Aufbewahren | 3 |

#### Praxisaufgaben
1. **Schulung:** Plane ein Schulungs- und Sensibilisierungskonzept (Zielgruppen, Inhalte, Nachweis, Wiederholung).
2. **Dokumentenlenkung:** Erstelle eine Dokumentenlandkarte (Politik, Verfahren, Arbeitsanweisungen, Aufzeichnungen) mit Eigentümer, Version, Freigabe und Aufbewahrung.

#### Kontrollfragen
1. Was ist der Unterschied zwischen einem Dokument und einer Aufzeichnung?
2. Wie sorgt man dafür, dass nur gültige Versionen im Umlauf sind?

### Modul 7: Betrieb, Überwachung, interne Audits und Managementbewertung
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Betriebsplanung und Kennzahlen zur Überwachung des ISMS festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende ein internes Audit planen, durchführen und Feststellungen formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende Eingaben und Ergebnisse einer Managementbewertung beschreiben.
* **Voraussetzungen:** Modul 4 bis 6.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Betriebliche Planung und Steuerung; Kennzahlen | 2 |
| 7.2 | Internes Audit: Programm, Durchführung, Feststellungen | 2 |
| 7.3 | Managementbewertung | 2 |

#### Praxisaufgaben
1. **Kennzahlen:** Lege fünf Kennzahlen mit Zielwert, Quelle und Intervall fest (z. B. Anteil geschulter Mitarbeitender, Dauer bis zum Einspielen kritischer Updates) und berechne zwei davon mit `kennzahlen.py`.
2. **Audit:** Plane ein internes Audit für einen Bereich (Ziel, Kriterien, Fragen, Nachweise) und formuliere aus den Material-Feststellungen drei Abweichungen mit Ursache und Maßnahme.
3. **Bewertung:** Erstelle eine Gliederung für die Managementbewertung (Eingaben, Ergebnisse, Beschlüsse) und fülle sie mit Beispieldaten.

#### Kontrollfragen
1. Warum muss ein internes Audit unabhängig sein?
2. Wie unterscheiden sich Abweichung und Verbesserungshinweis?
3. Welche Entscheidungen gehören in die Managementbewertung?

### Modul 8: Verbesserung und Zertifizierung
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Korrekturmaßnahmen und kontinuierliche Verbesserung im ISMS beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer Zertifizierung (Vorbereitung, Audits, Zertifikat, Überwachung) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende eine Zertifizierungsstelle nach Kriterien auswählen.
* **Voraussetzungen:** Modul 7.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Abweichungen, Korrekturmaßnahmen, Verbesserung | 2 |
| 8.2 | Zertifizierungsablauf und Überwachungsaudits (Annahme, vor dem Kurs prüfen) | 2 |
| 8.3 | Auswahl einer Zertifizierungsstelle und Kosten-Nutzen | 1 |

#### Praxisaufgaben
1. **Korrekturmaßnahmen:** Bearbeite zwei Abweichungen aus Modul 7 mit Ursachenanalyse, Maßnahme, Verantwortlichem, Frist und Wirksamkeitsprüfung.
2. **Ablauf:** Zeichne den Weg zur Zertifizierung als Zeitplan (Annahmen zu Dauer und Abschnitten, Ablauf mit der Zertifizierungsstelle klären, nicht geprüft).
3. **Auswahl:** Erstelle eine Entscheidungstabelle für drei fiktive Zertifizierungsstellen (Akkreditierung, Branchenerfahrung, Kosten, Sprache) und begründe die Wahl.

#### Kontrollfragen
1. Was gehört zu einer wirksamen Korrekturmaßnahme?
2. Warum ist ein Zertifikat keine Garantie für Sicherheit?
3. Welche Rolle spielt die Akkreditierung?

### Modul 9: Bezug zum Betrieb: ISMS im IT-Alltag
* **Priorität:** 2 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Anforderungen des ISMS in Betriebsprozessen (Change, Backup, Zugriff, Lieferanten, Vorfälle) verorten.
  * Nach Abschluss dieses Moduls kann der Lernende Nachweise aus dem Betrieb für Audits sammeln und ordnen.
* **Voraussetzungen:** Modul 5 und 7.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Betriebsprozesse und ISMS-Anforderungen (Verweise auf P35, P40) | 2 |
| 9.2 | Nachweise aus dem Betrieb sammeln und ordnen | 2 |

#### Praxisaufgaben
1. **Prozesskarte:** Ordne den Prozessen Change, Backup, Zugriffsverwaltung, Lieferantenmanagement und Vorfallbehandlung je zwei ISMS-Anforderungen und eine Maßnahme zu.
2. **Nachweise:** Erstelle ein Nachweisverzeichnis (Anforderung, Nachweis, Ablageort, Verantwortlicher, Aktualität) mit zehn Einträgen.

#### Kontrollfragen
1. Welche Betriebsnachweise sind für ein Audit besonders wichtig?
2. Wie vermeidet man doppelte Dokumentation zwischen ITIL-Prozessen und ISMS?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P49 erstellt (Annahmen: fiktive Silbersee Software GmbH, kein Labor, Österreich und EU, Normtexte nur sinngemäß). Stunden: 5+5+5+7+7+5+6+5+4 = 49 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 8×1, 1×2.

**Ausgabe der Norm mit Stand:** ISO/IEC 27001:2022 mit Amendment 1:2024 (Klimaschutz-Änderungen), laut iso.org veröffentlicht Februar 2024 (Seite am 13.11.2026 abgerufen). Die Norm selbst, ihr Inhalt, die Klauselnummern und die Zahl der Maßnahmen wurden nicht an der Norm geprüft.

**Nicht bestätigt:** Inhalt der Änderung von 2024, Gliederung und Maßnahmenzahl von Anhang A, Zertifizierungsablauf und Fristen, österreichische Normenausgabe und Zertifizierungsstellen. Kein Rechtsrat.

**Offen:** Zeitaufwand unerprobt; der Lehrplan wurde von AnsibleArtisan4711 noch nicht geprüft.
