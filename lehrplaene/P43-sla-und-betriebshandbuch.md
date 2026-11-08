# Lehrplan: SLA und Betriebshandbuch

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 8 Module, 48 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Service Level Agreements (SLA, OLA, Underpinning Contract), Servicekatalog, Betriebshandbuch und Runbooks |
| **Thematische Abgrenzung (Out of Scope)** | Technische Dokumentation (Netzpläne, Systemdokumentation, Konfigurationsdokumentation) ist ein vorhandener Kurs und wird hier nur verwiesen. Gegenstand ist das Betriebsregelwerk: Wer betreibt was, wann, mit welchem Ziel und nach welcher Anleitung. Keine Rechtsberatung (Arbeits- und Vertragsrecht werden nur als Rahmen angesprochen). Keine Zertifizierungsvorbereitung. Keine Konfiguration von Monitoring- oder Ticketsystemen. Bezugsrahmen ist ITIL 4; ITIL Version 5 ist nicht Gegenstand (siehe Quellen). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Servicekatalog | 1 | 6 |
| 2 | SLA, OLA und Underpinning Contracts | 1 | 6 |
| 3 | Kennzahlen und Reporting | 1 | 6 |
| 4 | Verfügbarkeitsberechnung | 1 | 6 |
| 5 | Bereitschaft und Eskalation | 2 | 6 |
| 6 | Betriebshandbuch und Runbooks | 1 | 7 |
| 7 | Übergabe in den Betrieb | 1 | 6 |
| 8 | Qualität und Aktualität | 1 | 5 |
| **Gesamt** | **7 Pflichtmodule, 1 Vertiefungsmodul** | | **48** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln die erforderlichen Kernkompetenzen. Das Modul mit Priorität 2 (Bereitschaft und Eskalation) dient der Vertiefung und kann bei Zeitmangel gekürzt oder als Selbststudium ausgelagert werden. Kein Pflichtmodul setzt Modul 5 voraus: Die Eskalationsstufen werden in Modul 2 behandelt, der Beispiel-Bereitschaftsplan liegt als Material in A.3 vor.*

### 2. Quellen

* **ITIL Foundation, ITIL 4 Edition**
  * Herausgeber: AXELOS, inzwischen PeopleCert
  * Version/Datum: 2019 (Stand nicht geprüft)
  * URL: keine geprüfte Quelle
* **ITIL 4 Practice Guides „Service Level Management“ und „Service Catalogue Management“**
  * Herausgeber: AXELOS bzw. PeopleCert
  * Version/Datum: Stand nicht geprüft
  * URL: `https://axelos.com/resource-hub/practice/service-catalogue-management-itil-4-practice-guide` (nur als Suchtreffer gesehen; der Abruf lieferte keinen Seitentext, daher nicht geprüft)
* **Sekundärquelle zu ITIL 4 Service Level Management:** open-exam-prep.com, „7.2 Service Level Management“, [https://open-exam-prep.com/study-guides/itil-4-foundation/core-practices-ii/service-level-management](https://open-exam-prep.com/study-guides/itil-4-foundation/core-practices-ii/service-level-management) (abgerufen am 08.11.2026; Stand der Seite nicht angegeben). Daraus stammen: Zweck von Service Level Management, SLA als dokumentierte Vereinbarung zwischen Anbieter und Kunde, Watermelon-Effekt, Anforderungen an gute Service-Level-Ziele.
* **ITIL-Versionsstand:** Laut einer Sekundärquelle (Advised Skills, „ITIL version 5 in 2026: what is confirmed, what is available and what comes next“, 16.02.2026) führt PeopleCert ITIL Version 5 im Jahr 2026 schrittweise ein; ITIL 4 läuft dort parallel. Dieser Lehrplan bleibt bei ITIL 4. Ob Begriffe und Praktiken in Version 5 abweichen, ist nicht geprüft.
* **ISO/IEC 20000-1:2018 (Information technology — Service management — Part 1: Service management system requirements)**
  * Herausgeber: ISO (International Organization for Standardization)
  * Version/Datum: 2018 (Edition 3), laut ISO-Seite 2023 bestätigt, dazu Änderung 1:2024 („Climate action changes“); abgerufen am 08.11.2026
  * URL: [https://www.iso.org/standard/70636.html](https://www.iso.org/standard/70636.html)
* **Google, „Site Reliability Engineering“ (SRE-Buch), Kapitel 4 „Service Level Objectives“**, [https://sre.google/sre-book/service-level-objectives/](https://sre.google/sre-book/service-level-objectives/): Titel und Adresse über das Inhaltsverzeichnis bestätigt, der Kapiteltext war nicht abrufbar. Wird für die Begriffe SLI, SLO und SLA verwendet; die Definitionen sind vor dem Kurs im Kapitel nachzulesen.
* **Google, SRE-Buch, Kapitel 11 „Being On-Call“**, [https://sre.google/sre-book/being-on-call/](https://sre.google/sre-book/being-on-call/): Adresse über das Inhaltsverzeichnis bestätigt, der Kapiteltext war nicht abrufbar (nur eine Übersichtsseite).
* **Arbeitszeitgesetz (AZG), Österreich, § 20a „Rufbereitschaft“:** abgerufen über jusline.at, [https://www.jusline.at/gesetz/azg/paragraf/20a.pdf](https://www.jusline.at/gesetz/azg/paragraf/20a.pdf); die Seite nennt die Fassung „in Kraft seit 01.09.2018“, Stand der Seite 04.06.2025. Die Seite gab nur zwei Absätze wieder (Rufbereitschaft außerhalb der Arbeitszeit darf nur an zehn Tagen pro Monat vereinbart werden; Kollektivvertrag kann Abweichungen zulassen). Die amtliche Fassung im Rechtsinformationssystem des Bundes (RIS, `https://www.ris.bka.gv.at`) wurde nicht abgerufen und ist vor dem Kurs zu prüfen. Der Kollektivvertrag der jeweiligen Branche kann abweichen.
* **RFC 1918: Address Allocation for Private Internets** (IETF, Februar 1996), [https://datatracker.ietf.org/doc/html/rfc1918](https://datatracker.ietf.org/doc/html/rfc1918)
* **RFC 2606: Reserved Top Level DNS Names** (IETF, Juni 1999, Datum nicht geprüft), [https://www.rfc-editor.org/rfc/rfc2606](https://www.rfc-editor.org/rfc/rfc2606) (nur als Suchtreffer gesehen, nicht abgerufen). Reserviert unter anderem `example.com` für Beispiele und Dokumentation.
* **Runbooks (Praxisliteratur):** Es gibt keine einheitliche normative Quelle. Herstellerartikel (z. B. PagerDuty, „What is a Runbook?“, `https://pagerduty.com/resources/automation/learn/what-is-a-runbook`) wurden nur als Suchtreffer gesehen, nicht abgerufen. Die Aufbauregeln für Runbooks in Modul 6 sind deshalb didaktische Festlegungen dieses Lehrplans, keine zitierte Norm.
* **Verfügbarkeitsrechnung:** Die Formeln (Produkt bei Reihenschaltung, 1 − Π(1 − Aᵢ) bei Parallelschaltung unter Unabhängigkeitsannahme) sind Mathematik und im Lehrplan per Skript nachgerechnet; es wird keine externe Quelle zitiert.
* **Abgrenzung:** Der vorhandene Kurs „Technische Dokumentation“ wird nicht verlinkt, weil dem Lehrplan keine Adresse vorliegt.

### 3. Labor-Setup & Rahmenbedingungen

Für diesen Lehrplan ist **kein technisches Labor** (keine Hyper-V-Umgebung, keine VMs) erforderlich. Alle Praxisaufgaben sind Fallstudien, Rechen- und Dokumentationsaufgaben mit einem fiktiven Unternehmen.

**Erforderliche Rahmenbedingungen (ab Modul 1):**
* Ein PC mit Standard-Office-Software (Textverarbeitung, Tabellenkalkulation, z. B. LibreOffice) oder Papier und Taschenrechner. Alle Rechnungen sind mit einem Taschenrechner lösbar; eine Tabellenkalkulation spart Zeit.
* Vom Dozenten bereitgestelltes Material (siehe Tabelle unten). Soweit Daten fehlen, sind sie in diesem Lehrplan selbst enthalten (Tabellen in den Aufgaben).
* Die Fallstudien beruhen auf dem fiktiven Unternehmen **Nordwind Logistik GmbH** mit der Domain `nordwind.example.com` (nach RFC 2606 für Beispiele reserviert) und internen Adressen nach RFC 1918. Alle Zahlen, Namen und Verträge sind frei erfunden.

**Fallstudie Nordwind Logistik GmbH (gilt für alle Module):**

Die Nordwind Logistik GmbH betreibt ein Lager mit rund 90 Funkscannern und ein Büro mit rund 300 Arbeitsplätzen. Die IT-Abteilung („IT-Betrieb“) betreibt vier Services:

| Nr. | Service | Nutzer | Servicezeit | Server / Adresse |
| :--- | :--- | :--- | :--- | :--- |
| S1 | Lagerverwaltung (LVS) | Lager, Versand | Mo–So, 00:00–24:00 (24x7) | Anwendung `10.20.0.10`, Datenbank `10.20.0.11` |
| S2 | E-Mail und Kalender | Büro | Mo–Fr 07:00–19:00, ohne gesetzliche Feiertage | `10.20.0.20` |
| S3 | Dateiablage | Büro | Mo–Fr 07:00–19:00, ohne gesetzliche Feiertage | `10.20.0.30` |
| S4 | Service Desk (Anwenderunterstützung) | Alle | Mo–Fr 07:30–17:00 | – |

**Netzplan Nordwind Logistik GmbH (Annahme):**

| Bezeichnung | Adresse | Rolle | Verwendet in |
| :--- | :--- | :--- | :--- |
| Server-Netz | `10.20.0.0/24` (Gateway `10.20.0.1`) | Server der Services S1 bis S3 | Modul 1, 6 |
| Büro-Netz | `10.30.0.0/22` | Arbeitsplätze | Modul 1 |
| Scanner-WLAN | `10.40.0.0/25` | Funkscanner im Lager | Modul 1 |

**Zielwerte Service Desk (Annahme, gilt für Modul 2, 3 und 5):** Reaktions- und Lösungszeiten werden in Kalenderzeit gemessen (vereinfachend, ohne Servicezeit).

| Priorität | Beschreibung | Reaktionszeit | Lösungszeit |
| :--- | :--- | :--- | :--- |
| P1 | Service ausgefallen, kein Ersatz | 15 Minuten | 4 Stunden |
| P2 | Service eingeschränkt, Ersatz vorhanden | 60 Minuten | 8 Stunden |
| P3 | Einzelner Anwender betroffen, kein Ausfall | 240 Minuten | 48 Stunden |

**Lieferantenvertrag (Underpinning Contract, Annahme):** Der Hardwarelieferant „Muster-Hardware GmbH“ (fiktiv) tauscht defekte Serverkomponenten vor Ort innerhalb von 4 Stunden nach Störungsmeldung aus, **nur Mo–Fr 08:00–17:00**.

**Bereitschaftsplan September 2026 (Annahme, gilt für Modul 5 und 7):** Wechsel jeweils montags um 08:00 Uhr.

| Woche ab | Bereitschaft | Bis (Wechsel) |
| :--- | :--- | :--- |
| Mo 31.08.2026 | Huber | Mo 07.09.2026 |
| Mo 07.09.2026 | Maier | Mo 14.09.2026 |
| Mo 14.09.2026 | Gruber | Mo 21.09.2026 |
| Mo 21.09.2026 | Bauer | Mo 28.09.2026 |
| Mo 28.09.2026 | Huber | Mo 05.10.2026 |

**Material des Dozenten:**

| Material | Verwendet in | Inhalt |
| :--- | :--- | :--- |
| Vorlage Servicekatalog-Eintrag, Vorlage SLA, Vorlage OLA | Modul 1, 2 | Leere Formulare als PDF, DOCX oder ODT |
| Vorlage Runbook, Vorlage Betriebshandbuch-Inhaltsverzeichnis | Modul 6 | Leere Formulare |
| Vorlage Übergabe-Checkliste und Review-Protokoll | Modul 7, 8 | Leere Formulare |
| Zwei bis drei Beispiel-SLAs aus dem Netz oder aus eigenem Fundus (anonymisiert, ohne Urheberrechte Dritter) | Modul 2 | Optional als Vergleichsmaterial |

## B. Detaillierter Modulaufbau

### Modul 1: Servicekatalog
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Service von einer Komponente und von einem Server unterscheiden und Services aus Sicht der Nutzer beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Servicekatalog-Eintrag mit den Pflichtangaben (Beschreibung, Nutzer, Servicezeit, Verantwortlicher, Abhängigkeiten) erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Abhängigkeiten eines Services zu Servern und Netzsegmenten darstellen und die Größe von Subnetzen für Nutzergruppen abschätzen.
* **Voraussetzungen:** Keine.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Service, Servicekomponente, Server: Begriffe aus Nutzersicht; Zweck eines Servicekatalogs | 2 |
| 1.2 | Aufbau eines Servicekatalog-Eintrags (Beschreibung, Nutzer, Servicezeit, Verantwortlicher, Abhängigkeiten) | 2 |
| 1.3 | Abhängigkeiten: Service, Server, Netzsegment, Adressbedarf | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Begriffe abgrenzen (Lernziel 1):** Ordne für die vier Services der Nordwind Logistik GmbH (A.3) jeweils eine Komponente und einen Server zu und formuliere für jeden Service einen Satz aus Nutzersicht („Als Lagerarbeiter kann ich …“).
2. **Servicekatalog-Einträge (Lernziel 2):** Erstelle mit der Vorlage Einträge für S1 und S2 mit Beschreibung, Nutzergruppe, Servicezeit, Verantwortlichem (erfundener Name) und Abhängigkeiten. Begründe, welche Angaben für die Nutzer und welche nur für den IT-Betrieb gedacht sind.
3. **Abhängigkeiten und Adressbedarf (Lernziel 3):** Zeichne ein Abhängigkeitsdiagramm für S1 (Nutzer, Scanner-WLAN, Server-Netz, Anwendung, Datenbank) mit den Adressen aus dem Netzplan. Berechne, wie viele Endgeräte im Büro-Netz `10.30.0.0/22` und im Scanner-WLAN `10.40.0.0/25` jeweils adressierbar sind, und beurteile, ob 90 Scanner mit Reserve für Wachstum in `10.40.0.0/25` passen.

#### Kontrollfragen
1. Was unterscheidet einen Service von einem Server?
2. Welche Angaben gehören mindestens in einen Servicekatalog-Eintrag, und welche davon sind für die Nutzer wichtig?
3. Warum ist die Servicezeit eine Angabe des Servicekatalogs und nicht nur des SLA?
4. Wie viele Hostadressen hat ein `/22`-Netz und wie viele ein `/25`-Netz?

---

### Modul 2: SLA, OLA und Underpinning Contracts
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SLA, OLA und Underpinning Contract (UC) voneinander abgrenzen und den Zweck von Service Level Management benennen.
  * Nach Abschluss dieses Moduls kann der Lernende ein SLA mit den üblichen Bestandteilen (Servicebeschreibung, Servicezeit, Ziele, Messung, Ausschlüsse, Reporting, Eskalation, Review) entwerfen.
  * Nach Abschluss dieses Moduls kann der Lernende Eskalationsstufen (hierarchisch, funktional) festlegen und mit Reaktionszeiten verbinden.
  * Nach Abschluss dieses Moduls kann der Lernende prüfen, ob SLA, OLA und UC zueinander passen.
* **Voraussetzungen:** Modul 1

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Zweck von Service Level Management; SLA, OLA, UC (Abgrenzung) | 2 |
| 2.2 | Bestandteile eines SLA: Ziele, Messung, Ausschlüsse, Reporting, Review | 2 |
| 2.3 | Eskalation (hierarchisch, funktional) und Stimmigkeit der Vereinbarungen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Abgrenzung (Lernziel 1):** Ordne die folgenden Vereinbarungen der Nordwind Logistik GmbH jeweils SLA, OLA oder UC zu und begründe: (a) IT-Betrieb ↔ Fachabteilung Lager über S1; (b) Service Desk ↔ Netzwerkteam (beide intern) über Reaktion auf Netzstörungen; (c) IT-Betrieb ↔ Muster-Hardware GmbH.
2. **SLA entwerfen (Lernziel 2):** Entwirf mit der Vorlage ein SLA für S2 (E-Mail). Verwende die Servicezeit aus A.3 und lege ein Verfügbarkeitsziel (Vorschlag: 99 % je Monat bezogen auf die Servicezeit), die Zielwerte des Service Desk, die Ausschlüsse (geplante Wartung, angekündigt), die Messmethode, das Reporting (Zeitraum, Empfänger) und die Review-Frist fest. Begründe jedes Ziel in einem Satz.
3. **Eskalationsstufen (Lernziel 3):** Lege für P1-Störungen von S1 eine Eskalationskette fest: Service Desk → Betrieb → Teamleitung → Geschäftsführung. Gib je Stufe die maximale Wartezeit an, nach der automatisch weiter eskaliert wird. Weise nach, dass die Summe bis zur Information der Teamleitung die Reaktionszeit von 15 Minuten (A.3) nicht überschreitet.
4. **Stimmigkeit prüfen (Lernziel 4):** Der Lieferantenvertrag aus A.3 sichert 4 Stunden Austausch nur Mo–Fr 08:00–17:00 zu, das SLA für S1 verlangt eine Lösungszeit von 4 Stunden bei P1 rund um die Uhr. Beschreibe den Widerspruch für einen Serverausfall am Samstag um 03:00 Uhr und nenne zwei Möglichkeiten, ihn zu beheben (z. B. Ersatzteile vor Ort, anderer UC, angepasstes SLA).

#### Kontrollfragen
1. Was ist der Unterschied zwischen einem SLA und einem OLA?
2. Warum soll ein SLA mit dem Kunden gemeinsam vereinbart und nicht einseitig vorgegeben werden?
3. Was ist ein Ausschluss im SLA, und nenne zwei übliche Beispiele.
4. Welche Folgen hat ein UC, der schwächer ist als das SLA, das er stützen soll?
5. Worin unterscheiden sich hierarchische und funktionale Eskalation?

---

### Modul 3: Kennzahlen und Reporting
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Begriffe SLI, SLO und SLA unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Erfüllungsgrade für Reaktion und Lösung aus Ticketdaten berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, wenn ein SLA nach außen „grün“, für die Nutzer aber unbefriedigend ist (Watermelon-Effekt), und ergänzende Kennzahlen vorschlagen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Service-Report für einen Berichtszeitraum aufbauen.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | SLI, SLO, SLA; Auswahl sinnvoller Kennzahlen | 2 |
| 3.2 | Erfüllungsgrad berechnen; Messung und Datenqualität | 2 |
| 3.3 | Watermelon-Effekt, ergänzende Kennzahlen und Service-Report | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Begriffe (Lernziel 1):** Formuliere für den Service E-Mail (S2) je ein Beispiel für SLI (gemessene Größe), SLO (internes Ziel) und SLA (vereinbarte Zusage) und erkläre, warum SLO und SLA nicht dasselbe sein müssen.
2. **Erfüllungsgrad berechnen (Lernziel 2):** Der Service Desk hat im Berichtszeitraum zwölf Tickets bearbeitet. Reaktionszeiten und Lösungszeiten sind in Minuten angegeben (Zielwerte siehe A.3):

   | Ticket | Priorität | Reaktion (min) | Lösung (min) | Wiedereröffnet |
   | :--- | :--- | :--- | :--- | :--- |
   | T01 | P1 | 5 | 110 | nein |
   | T02 | P1 | 10 | 200 | ja |
   | T03 | P1 | 20 | 180 | ja |
   | T04 | P2 | 40 | 300 | nein |
   | T05 | P2 | 50 | 420 | ja |
   | T06 | P2 | 30 | 360 | nein |
   | T07 | P2 | 90 | 480 | nein |
   | T08 | P3 | 120 | 1500 | nein |
   | T09 | P3 | 200 | 2000 | ja |
   | T10 | P3 | 240 | 2600 | nein |
   | T11 | P3 | 60 | 1200 | nein |
   | T12 | P3 | 30 | 900 | nein |

   Berechne den Erfüllungsgrad der Reaktionszeit und der Lösungszeit insgesamt und je Priorität. Ein Ziel gilt als erfüllt, wenn der Wert kleiner oder gleich dem Zielwert ist.
3. **Watermelon-Effekt (Lernziel 3):** Die Vereinbarung lautet: Reaktion ≥ 90 %, Lösung ≥ 95 %. Beurteile anhand der Tabelle aus Aufgabe 2, ob das SLA erfüllt ist, und berechne die Quote der wiedereröffneten Tickets. Schlage zwei Kennzahlen vor, die die Sicht der Nutzer besser abbilden (z. B. Wiedereröffnungsquote, Kundenzufriedenheit), und begründe sie.
4. **Service-Report (Lernziel 4):** Erstelle einen einseitigen Report für den Berichtszeitraum mit Kennzahlen (aus Aufgabe 2 und 3), Ampelbewertung, Kurzkommentar je Abweichung und Maßnahme. Lege Empfänger und Versandrhythmus fest.

#### Kontrollfragen
1. Was misst ein SLI, und woran erkennt man eine brauchbare Kennzahl?
2. Warum kann ein SLA „grün“ sein, obwohl die Nutzer unzufrieden sind? Nenne ein Beispiel aus Aufgabe 3.
3. Warum ist ein Mittelwert allein für Reaktions- oder Lösungszeiten oft irreführend?
4. Was gehört in einen Service-Report, und wer sollte ihn erhalten?

---

### Modul 4: Verfügbarkeitsberechnung
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende aus einem Verfügbarkeitsziel die zulässige Ausfallzeit für einen Zeitraum berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die erreichte Verfügbarkeit aus Ausfalldaten ermitteln und dabei Servicezeit und geplante Wartung korrekt berücksichtigen.
  * Nach Abschluss dieses Moduls kann der Lernende die Gesamtverfügbarkeit einer Reihen- und einer Parallelschaltung berechnen und Verbesserungsmaßnahmen vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende MTTR und MTBF mit festgelegter Definition berechnen.
* **Voraussetzungen:** Modul 2, Modul 3

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Verfügbarkeit als Verhältnis; Servicezeit und geplante Wartung; zulässige Ausfallzeit | 2 |
| 4.2 | Erreichte Verfügbarkeit aus Ausfalldaten (Randfälle: Wartungsfenster, Monatsgrenze, Mitternacht) | 2 |
| 4.3 | Reihen- und Parallelschaltung; MTTR und MTBF | 2 |

**Definitionen für diesen Lehrplan:** Verfügbarkeit = (vereinbarte Servicezeit − geplante Wartung − Ausfallzeit) / (vereinbarte Servicezeit − geplante Wartung). Ausfallzeit zählt nur innerhalb der Servicezeit und nur außerhalb des angekündigten Wartungsfensters; überzieht eine Wartung, zählt die Überschreitung als Ausfall. Ausfälle über die Monatsgrenze werden auf die Monate aufgeteilt. MTTR = Gesamtausfallzeit / Anzahl der Ausfälle; MTBF = (Beobachtungszeit − Gesamtausfallzeit) / Anzahl der Ausfälle. Das Jahr hat 365 Tage. Diese Festlegungen sind Absprachen des Kurses; in der Praxis steht die Definition im SLA.

#### Praxisaufgaben (Hands-on Lab)
1. **Zulässige Ausfallzeit (Lernziel 1):** Berechne für Verfügbarkeitsziele von 99,0 %, 99,5 %, 99,9 %, 99,95 % und 99,99 % die zulässige Ausfallzeit pro Jahr (365 Tage, 24x7) in Minuten und Stunden sowie pro Monat mit 30 Tagen in Minuten. Berechne außerdem für S2 im Oktober 2026 (Mo–Fr 07:00–19:00, ohne Feiertage; der 26.10.2026 ist ein Montag und wird als arbeitsfrei angenommen) die Servicezeit in Minuten und die bei 99 % zulässige Ausfallzeit.
2. **Erreichte Verfügbarkeit S1 (Lernziel 2):** S1 hat Servicezeit 24x7, September 2026 (30 Tage). Geplante Wartung: Samstag 12.09.2026, 02:00–06:00 Uhr. Ausfälle:

   | Nr. | Beginn | Ende |
   | :--- | :--- | :--- |
   | 1 | 02.09.2026 14:10 | 02.09.2026 14:55 |
   | 2 | 12.09.2026 05:10 | 12.09.2026 07:25 |
   | 3 | 21.09.2026 09:00 | 21.09.2026 09:20 |
   | 4 | 24.09.2026 23:40 | 25.09.2026 00:35 |
   | 5 | 30.09.2026 23:30 | 01.10.2026 00:30 |

   Berechne die anrechenbare Ausfallzeit je Ausfall, die Verfügbarkeit und stelle fest, ob das Ziel 99,5 % erreicht wurde. Berechne zum Vergleich die Verfügbarkeit, wenn man die Wartung nicht berücksichtigt (Ausfall 2 vollständig, Basis 43 200 Minuten; Ausfall 5 nur mit dem Anteil im September), und erkläre den Unterschied.
3. **Erreichte Verfügbarkeit S2 (Lernziel 2):** Für Oktober 2026 (Servicezeit siehe Aufgabe 1; keine Wartung) sind folgende Ausfälle aufgetreten: Mo 05.10. 08:00–09:30; Mi 14.10. 18:30–19:45; Sa 17.10. 10:00–12:00; Mo 26.10. 08:00–10:00; Do 29.10. 06:15–07:45. Berechne die anrechenbare Ausfallzeit und die Verfügbarkeit und stelle fest, ob das Ziel von 99 % erreicht wurde.
4. **Reihen- und Parallelschaltung (Lernziel 3):** Die Verfügbarkeit von S1 hängt in Reihe von diesen Komponenten ab: Netzwerk 99,95 %, Server-Host 99,9 %, Datenbank 99,8 %, Anwendung 99,7 %. Berechne die Gesamtverfügbarkeit und die zu erwartende Ausfallzeit pro Jahr. Vergleiche danach (a) einen Host-Cluster aus zwei unabhängigen Hosts mit je 99,9 % und (b) einen Datenbank-Cluster aus zwei unabhängigen Datenbanken mit je 99,8 % und beantworte, welche Maßnahme das Ziel von 99,5 % erreichbar macht. Nenne zwei Gründe, warum die Rechnung für Parallelschaltungen die Wirklichkeit überschätzt.
5. **MTTR und MTBF (Lernziel 4):** Berechne aus den Daten von Aufgabe 2 (anrechenbare Ausfälle, Beobachtungszeit = Servicezeit abzüglich Wartung) MTTR und MTBF und erkläre, warum die beiden Kennzahlen allein kein SLA ersetzen.

#### Kontrollfragen
1. Wie viele Minuten Ausfall pro Jahr erlaubt eine Verfügbarkeit von 99,9 %?
2. Warum kann man Verfügbarkeitsziele nicht ohne Bezug auf die Servicezeit vergleichen?
3. Warum ist die Gesamtverfügbarkeit einer Reihenschaltung kleiner als die kleinste Einzelverfügbarkeit?
4. Welche Annahme steckt hinter der Formel für die Parallelschaltung?
5. Nenne zwei Gründe, warum MTTR in der Praxis unterschiedlich definiert wird.

---

### Modul 5: Bereitschaft und Eskalation
* **Priorität:** 2
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Bereitschaftsmodelle (Rufbereitschaft, Schichtdienst) beschreiben und von aktiver Arbeitszeit abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Bereitschaftsplan auf die Einhaltung einer vorgegebenen Höchstzahl an Bereitschaftstagen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Alarmierungs- und Eskalationskette so auslegen, dass die vereinbarten Reaktionszeiten erreichbar sind.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Bereitschaftsmodelle und rechtlicher Rahmen (Österreich), Übergabe der Bereitschaft | 2 |
| 5.2 | Bereitschaftsplan prüfen: Bereitschaftstage je Person, Vertretung | 2 |
| 5.3 | Alarmierungskette, Bestätigungsfristen und Reaktionszeit | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Modelle und Rahmen (Lernziel 1):** Lies § 20a AZG (siehe Quellen, im RIS nachprüfen). Stelle in einer Tabelle Rufbereitschaft und Schichtdienst gegenüber (Wo hält sich die Person auf? Wie schnell muss sie reagieren? Ab wann ist es Arbeitszeit?). Markiere, was du aus dem Gesetz belegen kannst und was nicht.
2. **Bereitschaftsplan prüfen (Lernziel 2):** Prüfe den Bereitschaftsplan September 2026 aus A.3: Zähle für jede Person die Kalendertage im September, an denen sie Bereitschaft hat (jeder angefangene Kalendertag zählt; die Zählweise ist eine Vereinfachung dieses Lehrplans, nicht bestätigt) und vergleiche mit der Höchstgrenze von zehn Tagen pro Monat. Frage: Was ändert sich, wenn Huber zusätzlich die Woche ab 14.09. für den erkrankten Gruber übernimmt?
3. **Alarmierungskette (Lernziel 3):** Lege fest: Stufe 1 Bereitschaftsperson, Stufe 2 Stellvertretung, Stufe 3 Teamleitung; Alarm um 00:00 Uhr. Bestimme die Bestätigungsfristen je Stufe so, dass die Teamleitung spätestens nach 10 Minuten alarmiert ist und die P1-Reaktionszeit von 15 Minuten (A.3) eingehalten werden kann. Zeige, dass Fristen von je 15 Minuten die Reaktionszeit verfehlen.

#### Kontrollfragen
1. Was unterscheidet Rufbereitschaft von Arbeitsbereitschaft? (Antwort mit Rechtsquelle belegen.)
2. Welche Höchstzahl an Bereitschaftstagen nennt § 20a AZG, und wer kann davon abweichen?
3. Wie viele Personen braucht ein Wochenrhythmus mindestens, damit niemand mehr als zehn Bereitschaftstage im Monat hat?
4. Warum muss die Bestätigungsfrist in der Alarmierungskette kürzer sein als die Reaktionszeit im SLA?

---

### Modul 6: Betriebshandbuch und Runbooks
* **Priorität:** 1
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Betriebshandbuch, Runbook und technische Dokumentation voneinander abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Betriebshandbuch gliedern.
  * Nach Abschluss dieses Moduls kann der Lernende ein Runbook so schreiben, dass eine nicht eingearbeitete Person es ausführen kann.
  * Nach Abschluss dieses Moduls kann der Lernende Mängel in einem vorhandenen Runbook finden und beheben.
* **Voraussetzungen:** Modul 1, Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Betriebshandbuch, Runbook, technische Dokumentation: Abgrenzung und Zielgruppen | 2 |
| 6.2 | Gliederung eines Betriebshandbuchs | 1 |
| 6.3 | Aufbau eines Runbooks: Auslöser, Voraussetzungen, Schritte, Prüfung, Rückfall, Eskalation | 2 |
| 6.4 | Warnhinweise, Freigaben und destruktive Schritte; Review eines Runbooks | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Abgrenzung (Lernziel 1):** Ordne diese Dokumente jeweils Betriebshandbuch, Runbook oder technischer Dokumentation (vorhandener Kurs) zu: (a) Netzplan mit VLAN-Liste; (b) Anleitung „Mail-Queue leeren“; (c) Regel „Wartungsfenster sind Samstag 02:00–06:00“; (d) Konfigurationsdatei-Beschreibung des Dateiservers. Begründe, wer jeweils die Zielgruppe ist.
2. **Betriebshandbuch gliedern (Lernziel 2):** Erstelle mit der Vorlage ein Inhaltsverzeichnis für das Betriebshandbuch der Nordwind Logistik GmbH (mindestens: Zweck und Geltungsbereich, Services und Servicezeiten, Rollen und Erreichbarkeit, Eskalation, Wartungsfenster und Änderungen, Runbook-Verzeichnis, Dokumentenpflege) und gib je Kapitel den Verantwortlichen an.
3. **Runbook schreiben (Lernziel 3):** Schreibe ein Runbook „S1 nicht erreichbar“ mit Titel, Version, Stand, Verantwortlichem, Auslöser, Voraussetzungen, Prüfschritten (Erreichbarkeit von `10.20.0.10` und `10.20.0.11` mit `ping`, Namensauflösung `lvs.nordwind.example.com` mit `nslookup`), Entscheidung („Netzproblem oder Serverproblem?“), Eskalation (Verweis auf Eskalationskette aus Modul 2), Erfolgsprüfung und Rückmeldung an den Service Desk. Verwende nur Befehle, die du kennst und im Kurs testen kannst; was du nicht prüfen kannst, markiere mit „nicht bestätigt“.
4. **Runbook prüfen (Lernziel 4):** Finde in diesem fehlerhaften Runbook mindestens acht Mängel und formuliere es neu:

   ```text
   Runbook: Dateiserver neu starten
   Stand: unbekannt
   1. Auf den Server verbinden.
   2. Dienst stoppen.
   3. Das Temp-Verzeichnis komplett löschen.
   4. Server neu starten.
   5. Prüfen, ob alles geht.
   Bei Problemen den Admin anrufen.
   ```

#### Kontrollfragen
1. Was unterscheidet ein Runbook von technischer Dokumentation?
2. Welche Angaben braucht jedes Runbook, damit es nachts von einer Vertretung ausgeführt werden kann?
3. Warum gehört vor einen destruktiven Schritt eine Sicherung und eine Freigabe?
4. Woran erkennt man eine messbare Erfolgsprüfung im Runbook?

---

### Modul 7: Übergabe in den Betrieb
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum ein neuer oder geänderter Service eine formale Übergabe in den Betrieb braucht.
  * Nach Abschluss dieses Moduls kann der Lernende Muss- und Soll-Kriterien für die Betriebsbereitschaft festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Übergabe-Checkliste auswerten und eine begründete Go/No-Go-Empfehlung abgeben.
  * Nach Abschluss dieses Moduls kann der Lernende ein Übergabeprotokoll mit offenen Punkten, Verantwortlichen und Fristen erstellen.
* **Voraussetzungen:** Modul 2, Modul 6

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Warum Übergabe? Rollen Projekt, Betrieb, Service Owner | 2 |
| 7.2 | Betriebsbereitschaftskriterien: Muss, Soll | 2 |
| 7.3 | Go/No-Go, bedingte Übernahme, Übergabeprotokoll | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Begründung (Lernziel 1):** Beschreibe an einem erfundenen Beispiel („Zeiterfassung“ geht ohne Übergabe in Betrieb), was am ersten Wochenende schiefgehen kann. Nenne mindestens drei Folgen (z. B. keine Bereitschaft, kein Runbook, kein Backup).
2. **Kriterien festlegen (Lernziel 2):** Leite aus den Modulen 1 bis 6 mindestens acht Kriterien ab und teile sie in Muss und Soll. Begründe, warum Backup und Wiederherstellungstest Muss-Kriterien sind.
3. **Checkliste auswerten (Lernziel 3):** Das Projekt „Zeiterfassung“ meldet:

   | Nr. | Kriterium | Art | Status |
   | :--- | :--- | :--- | :--- |
   | K1 | Servicekatalog-Eintrag vorhanden | Muss | erfüllt |
   | K2 | SLA und OLA abgestimmt | Muss | erfüllt |
   | K3 | Betriebshandbuch Version 1.0 | Muss | erfüllt |
   | K4 | Runbooks für mindestens drei Standardstörungen | Muss | 2 vorhanden |
   | K5 | Backup eingerichtet | Muss | erfüllt |
   | K6 | Wiederherstellungstest dokumentiert | Muss | nicht durchgeführt |
   | K7 | Überwachung und Alarmierung | Muss | erfüllt |
   | K8 | Bereitschaftsplan ergänzt | Muss | erfüllt |
   | K9 | Schulung Service Desk | Soll | geplant, nicht durchgeführt |
   | K10 | Support- und Lizenzvertrag dokumentiert | Soll | erfüllt |

   Zähle erfüllte und offene Muss-Kriterien und gib eine Go/No-Go-Empfehlung ab. Formuliere eine Variante „bedingte Übernahme“ mit Auflagen, Verantwortlichen und Fristen.
4. **Übergabeprotokoll (Lernziel 4):** Erstelle mit der Vorlage ein Übergabeprotokoll für „Zeiterfassung“ (Service, Übergebender, Übernehmender, Datum, Ergebnis, offene Punkte, Unterschriften).

#### Kontrollfragen
1. Wer entscheidet über die Übernahme in den Betrieb, und warum nicht das Projektteam allein?
2. Warum ist ein nicht getesteter Restore ein Muss-Kriterium?
3. Was ist der Unterschied zwischen „No-Go“ und „bedingter Übernahme“?
4. Was gehört in ein Übergabeprotokoll?

---

### Modul 8: Qualität und Aktualität
* **Priorität:** 1
* **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Qualitätsmerkmale für Betriebsdokumente benennen (vollständig, eindeutig, aktuell, auffindbar, verantwortet).
  * Nach Abschluss dieses Moduls kann der Lernende Review-Zyklen, Versionierung und Änderungshistorie festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende die Aktualität eines Dokumentenbestands anhand einer Kennzahl bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende Dokumentenpflege an Änderungen und Vorfälle koppeln.
* **Voraussetzungen:** Modul 6, Modul 7

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Qualitätsmerkmale und Review-Checkliste | 2 |
| 8.2 | Review-Zyklen, Versionierung, Verantwortliche | 1 |
| 8.3 | Aktualitätskennzahl; Pflege bei Änderung und Vorfall | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Review-Checkliste (Lernziele 1 und 2):** Erstelle eine Checkliste mit mindestens acht Prüfpunkten für ein Runbook und lege fest: Review-Zyklus (Vorschlag: 12 Monate), Versionsschema (z. B. 1.0, 1.1), Pflichtfelder der Änderungshistorie, Verantwortlicher je Dokument.
2. **Aktualität messen (Lernziel 3):** Stichtag ist der 30.11.2026. Ein Runbook gilt als überfällig, wenn der letzte Review mehr als 365 Tage zurückliegt:

   | Runbook | Letzter Review |
   | :--- | :--- |
   | RB-01 S1 nicht erreichbar | 15.06.2026 |
   | RB-02 S1 Datenbank neu starten | 30.11.2025 |
   | RB-03 S2 Mail-Queue hängt | 20.10.2025 |
   | RB-04 S3 Dateiablage voll | 02.03.2026 |
   | RB-05 S2 Postfach voll | 05.05.2025 |
   | RB-06 S1 Scanner-WLAN Ausfall | 01.09.2026 |
   | RB-07 S3 Berechtigung ändern | 12.12.2024 |
   | RB-08 Backup fehlgeschlagen | 20.01.2026 |
   | RB-09 S4 Kennwort zurücksetzen | 29.11.2025 |
   | RB-10 Zertifikat läuft ab | 10.10.2026 |

   Bestimme die überfälligen Runbooks, berechne die Aktualitätsquote (Anteil nicht überfälliger Runbooks) und schlage eine Reihenfolge für die Überarbeitung vor (Begründung nach Servicekritikalität).
3. **Pflege koppeln (Lernziel 4):** Beschreibe, wie jede Änderung am System („Datenbank wird auf einen neuen Server umgezogen“) und jeder Vorfall, bei dem ein Runbook falsch war, einen Pflegeauftrag auslöst. Verweise dabei auf die Prozesse Change und Incident (kein Gegenstand dieses Kurses).
4. **Abschlussarbeit (alle Lernziele):** Erstelle für den Service S2 ein Mini-Betriebspaket aus Servicekatalog-Eintrag, SLA-Kurzfassung, Runbook „Postfach voll“ und Review-Protokoll mit Mängelliste.

#### Kontrollfragen
1. Woran erkennt man ein veraltetes Runbook?
2. Warum braucht jedes Betriebsdokument einen Verantwortlichen und ein Datum?
3. Was spricht für und gegen einen fixen Review-Zyklus von 12 Monaten?
4. Wie verhindert man, dass nach einem Systemumzug das Runbook veraltet?

---

## C. Hinweise zur Entstehung und Prüfvermerk (08.11.2026)

Dieser Lehrplan wurde ohne Gem-Entwurf direkt aus dem Prompt P43 erstellt. Annahmen: Kein technisches Labor, fiktives Unternehmen Nordwind Logistik GmbH, Bezugsrahmen ITIL 4, Österreich als rechtlicher Rahmen für Bereitschaft. Alle Rechenwerte wurden per Skript berechnet.

**Kontrollwerte (Lösungsschlüssel für Dozenten):**

* **Modul 1, Aufgabe 3:** `/22` hat 1022, `/25` hat 126 nutzbare Hostadressen; 90 Scanner passen mit 36 Adressen Reserve.
* **Modul 3, Aufgabe 2:** Reaktion insgesamt 10 von 12 (83,3 %), Lösung 12 von 12 (100 %). Je Priorität Reaktion: P1 2 von 3 (66,7 %; T03 mit 20 min), P2 3 von 4 (75 %; T07 mit 90 min), P3 5 von 5; Lösung P1 bis P3 jeweils vollständig. Aufgabe 3: Wiedereröffnet sind T02, T03, T05, T09, also 4 von 12 (33,3 %). Lösung ≥ 95 % ist erfüllt, Reaktion ≥ 90 % verfehlt; damit ist das SLA nicht erfüllt, die Lösungsquote täuscht aber über Wiedereröffnungen hinweg.
* **Modul 4, Aufgabe 1:** 99,0 % → 5256 min = 87,6 h pro Jahr, 432 min pro Monat; 99,5 % → 2628 min = 43,8 h, 216 min; 99,9 % → 525,6 min = 8,76 h, 43,2 min; 99,95 % → 262,8 min = 4,38 h, 21,6 min; 99,99 % → 52,56 min = 0,876 h, 4,32 min. S2 im Oktober 2026: 21 Servicetage × 12 h = 252 h = 15 120 min; bei 99 % zulässig 151,2 min.
* **Modul 4, Aufgabe 2:** Servicezeit 43 200 min, Wartung 240 min, Basis 42 960 min. Anrechenbar: Ausfall 1: 45 min; Ausfall 2: 135 min gesamt, davon 50 min im Wartungsfenster (05:10–06:00), anrechenbar 85 min; Ausfall 3: 20 min; Ausfall 4: 55 min; Ausfall 5: 60 min gesamt, davon 30 min im September, anrechenbar 30 min. Summe 235 min. Verfügbarkeit = (42 960 − 235) / 42 960 = 99,453 %, zulässig wären 214,8 min; Ziel 99,5 % **nicht erreicht**. Naive Rechnung (Wartung ignoriert, Ausfall 5 nur im September, Basis 43 200 min): 285 min, 99,340 %.
* **Modul 4, Aufgabe 3:** Ausfall Mo 05.10.: 90 min; Mi 14.10.: 30 min (nur bis 19:00); Sa 17.10.: 0 (außerhalb der Servicezeit); Mo 26.10.: 0 (arbeitsfrei); Do 29.10.: 45 min (ab 07:00). Summe 165 min; Verfügbarkeit = (15 120 − 165) / 15 120 = 98,909 %; Ziel 99 % **nicht erreicht** (zulässig 151,2 min).
* **Modul 4, Aufgabe 4:** Reihe: 0,9995 × 0,999 × 0,998 × 0,997 = 99,351 %, entspricht rund 3409 min (56,8 h) Ausfall pro Jahr. (a) Host-Cluster: 1 − 0,001² = 99,9999 %, Gesamt 99,451 %. (b) Datenbank-Cluster: 1 − 0,002² = 99,9996 %, Gesamt 99,550 %. Nur (b) erreicht 99,5 %.
* **Modul 4, Aufgabe 5:** Beobachtungszeit 42 960 min, Ausfall 235 min, 5 Ausfälle: MTTR = 47 min; MTBF = (42 960 − 235) / 5 = 8545 min ≈ 142,4 h.
* **Modul 5, Aufgabe 2:** Bereitschaftstage im September: Huber 10 (1.–7.9. = 7 Tage und 28.–30.9. = 3 Tage), Maier 8 (7.–14.9.), Gruber 8 (14.–21.9.), Bauer 8 (21.–28.9.). Huber liegt genau an der Grenze von zehn Tagen. Übernimmt Huber zusätzlich 14.–21.9., hat er 18 Tage und überschreitet die Grenze. Aufgabe 3: Bei je 15 min Frist wird die Teamleitung erst nach 30 min alarmiert; Fristen von je 5 Minuten alarmieren die Teamleitung nach 10 min. Frage 3: Mindestens fünf Personen. Bei Wochenwechsel montags 08:00 berührt jede Woche acht Kalendertage; bei vier Personen kann eine Person in einem 31-Tage-Monat 8 + 3 = 11 Tage haben (per Skript über 140 Wochen: Maximum 11 bei vier, 8 bei fünf Personen, 16 bei drei).
* **Modul 6, Aufgabe 4, mögliche Mängel:** (1) kein Verantwortlicher, keine Version, Stand „unbekannt“; (2) kein Auslöser und keine Voraussetzung; (3) „den Server“ ohne Name oder Adresse; (4) „Dienst“ nicht benannt; (5) destruktiver Schritt „Temp-Verzeichnis komplett löschen“ ohne Sicherung, Freigabe oder Pfad; (6) keine Ankündigung an die Nutzer, kein Wartungsfenster; (7) „Prüfen, ob alles geht“ nicht messbar; (8) „den Admin“ ohne Name, Nummer oder Eskalationskette; (9) kein Rückfall bei Fehlschlag.
* **Modul 7, Aufgabe 3:** 8 Muss-Kriterien, 6 erfüllt (K1, K2, K3, K5, K7, K8), 2 offen (K4 mit 2 von 3 Runbooks, K6 ohne Restore-Test). Empfehlung: No-Go, oder bedingte Übernahme mit Auflagen (drittes Runbook und Restore-Test mit Verantwortlichem und Frist).
* **Modul 8, Aufgabe 2:** Stichtag 30.11.2026: RB-03 406 Tage, RB-05 574 Tage, RB-07 718 Tage und RB-09 366 Tage sind überfällig; RB-02 (30.11.2025) hat genau 365 Tage und ist nicht überfällig. 4 von 10 überfällig, Aktualitätsquote 60 %.

**Prüfvermerk (Grundanweisung, neun Punkte):**

1. **Stunden und Prioritäten:** 6+6+6+6+6+7+6+5 = 48 UE; 7× Priorität 1, 1× Priorität 2; jede Einheitentabelle summiert auf die Modulstunden (Skript über die Datei geprüft). Keine Fehler gefunden; Stichprobe: Modul 6 mit 2+1+2+2 = 7 UE.
2. **Labor-Setup:** Kein technisches Labor; alle Unterlagen sind aufgeführt oder im Lehrplan enthalten. Korrigiert: Die Spalte „Verwendet in“ im Netzplan nannte Modul 4, das keine Adressen benutzt; jetzt Modul 1 und 6. Stichprobe: Modul 4 und Modul 7 brauchen keine Zusatzdaten.
3. **Quellen:** Siehe A.2. Nicht abgerufen oder nicht bestätigt: Inhalt von SRE-Kapitel 4 und 11, Practice Guides, RFC 2606 (nur Suchtreffer), amtlicher Wortlaut § 20a AZG im RIS, Runbook-Literatur.
4. **Widerspruchsfreiheit und Zustände:** Zielwerte, Servicezeiten, Netzplan und Bereitschaftsplan sind einmal in A.3 festgelegt und werden nur verwendet. Der UC-Widerspruch in Modul 2, Aufgabe 4 ist beabsichtigt. Korrigiert: Die Vergleichsrechnung in Modul 4, Aufgabe 2 war mehrdeutig („Wartung und Monatsgrenze nicht beachtet“ ergibt 99,271 %, gemeint waren 99,340 %); die Aufgabe nennt jetzt eindeutig, was weggelassen wird. Alle Datums- und Wochentagsangaben (z. B. Sa 12.09.2026, Mo 26.10.2026, Mo 31.08.2026) per Skript geprüft.
5. **Lernziele, Lerneinheiten, Kontrollfragen:** Jedes Lernziel hat eine Aufgabe (im Text markiert); jede Lerneinheit hat mindestens eine Aufgabe oder Frage (Stichprobe Einheit 6.2: Aufgabe 2; Einheit 8.2: Aufgabe 1, Frage 2). Korrigiert: Kontrollfrage 3 in Modul 5 („wie viele Personen“) hatte keinen Lösungswert; ergänzt und per Skript über 140 Wochen geprüft.
6. **Einschränkungen und Rückbau:** Modul 5 ist Priorität 2; kein Pflichtmodul nennt es als Voraussetzung.
7. **Infrastruktur über eine VM hinaus:** Nicht relevant, kein Labor.
8. **Internet, Namen, Dateiwege:** Domain `nordwind.example.com`, Adressen `10.20.0.0/24`, `10.30.0.0/22`, `10.40.0.0/25` nach RFC 1918; keine Software, kein Download. Keine Fehler gefunden.
9. **Befehle und Sicherheit:** Nur `ping` und `nslookup` in Modul 6, beide hier nicht ausgeführt (es gibt kein Labor und die Adressen sind fiktiv); destruktive Schritte werden als Warnbeispiel in Modul 6, Aufgabe 4 behandelt, nicht ausgeführt.

**Offene Punkte:**

* Inhalte der Quellen mit „nicht abgerufen“ vor dem Kurs prüfen, besonders § 20a AZG im RIS und die Begriffe des SRE-Buchs.
* ITIL-4-Begriffe (Service Catalogue Management, SLM) gegen die Practice Guides prüfen.
* Der Zeitaufwand der Aufgaben ist unerprobt (kein Probelauf mit Lernenden).
* Überschneidung mit P40/P41 (SLA-Grundbegriffe, MTTR, MTBF) bleibt bewusst bestehen.
