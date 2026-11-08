# Lehrplan: Incident-, Problem- und Change-Management

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 8 Module, 48 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | ITIL 4, Incident-, Problem- und Change-Management |
| **Thematische Abgrenzung (Out of Scope)** | Keine tiefgehende Konfiguration von Ticketsystemen; keine Überschneidung mit bestehenden Netzwerk- oder Server-Lehrplänen. Verweise darauf bleiben rein theoretisch. Keine Zertifizierungsvorbereitung (Prüfungsfragen, Braindumps). Bezugsrahmen ist ITIL 4; ITIL Version 5 ist nicht Gegenstand (siehe Quellen). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen des IT Service Managements (ITIL 4) | 1 | 6 |
| 2 | Incident Management – Lebenszyklus und Klassifizierung | 1 | 6 |
| 3 | Incident Management – Eskalation und Kommunikation | 1 | 6 |
| 4 | Problem Management – Grundlagen und reaktive Analyse | 1 | 6 |
| 5 | Problem Management – Proaktive Analyse und RCA | 2 | 6 |
| 6 | Change Enablement – Grundlagen und Change-Typen | 1 | 6 |
| 7 | Change Enablement – Evaluierung und Wartungsfenster | 1 | 6 |
| 8 | Post-Incident-Review und Service-Metriken | 2 | 6 |
| **Gesamt** | **6 Pflichtmodule, 2 Vertiefungsmodule** | | **48** |

*Hinweis zur Priorisierung: Module mit Priorität 1 vermitteln die zwingend erforderlichen Kernkompetenzen. Module mit Priorität 2 dienen der Vertiefung und können bei Zeitmangel gekürzt oder als Selbststudium ausgelagert werden. Kein Pflichtmodul setzt ein Modul mit Priorität 2 voraus.*

### 2. Quellen

* **ITIL Foundation, ITIL 4 Edition**
  * Herausgeber: AXELOS, inzwischen PeopleCert
  * Version/Datum: 2019 (Stand nicht geprüft)
  * URL: `https://www.axelos.com/certifications/itil-service-management/itil-4-foundation` (nicht geprüft, Seite des früheren Herausgebers; der Abruf war nicht möglich)
* **ITIL 4 Practice Guides (Incident Management, Problem Management, Change Enablement)**
  * Herausgeber: AXELOS bzw. PeopleCert
  * Version/Datum: Stand nicht geprüft
  * URL: keine geprüfte Quelle
* **ITIL-Versionsstand:** Laut einer Sekundärquelle (Advised Skills, „ITIL version 5 in 2026: what is confirmed, what is available and what comes next“, 16.02.2026, URL: `https://www.advisedskills.com/blog/it-service-management/itil-version-5-in-2026-what-is-confirmed-what-is-available-and-what-comes-next.md`) führt PeopleCert ITIL Version 5 im Jahr 2026 schrittweise ein; ITIL 4 läuft dort parallel. Dieser Lehrplan bleibt bei ITIL 4. Ob Begriffe und Praktiken in Version 5 abweichen, ist nicht geprüft.
* **ISO/IEC 20000-1:2018 (Information technology — Service management — Part 1: Service management system requirements)**
  * Herausgeber: ISO (International Organization for Standardization)
  * Version/Datum: 2018 (Edition 3), laut ISO-Seite 2023 bestätigt, dazu Änderung 1:2024 („Climate action changes“); abgerufen am 08.11.2026
  * URL: [https://www.iso.org/standard/70636.html](https://www.iso.org/standard/70636.html)
* **RFC 1918: Address Allocation for Private Internets**
  * Herausgeber: IETF
  * Version/Datum: Februar 1996
  * URL: [https://datatracker.ietf.org/doc/html/rfc1918](https://datatracker.ietf.org/doc/html/rfc1918)
* **RFC 2606: Reserved Top Level DNS Names** (reserviert unter anderem `example.com` für Beispiele und Dokumentation)
  * Herausgeber: IETF
  * Version/Datum: Juni 1999 (Datum nicht geprüft)
  * URL: [https://www.rfc-editor.org/rfc/rfc2606](https://www.rfc-editor.org/rfc/rfc2606) (nur als Suchtreffer gesehen, nicht abgerufen)
* **Hilfsmittel der Problemanalyse und Auswertung** (Sekundärquellen, nur als Suchtreffer gesehen, nicht abgerufen):
  * Ishikawa-Diagramm: Wikipedia, „Ishikawa diagram“, [https://en.wikipedia.org/wiki/Ishikawa_diagram](https://en.wikipedia.org/wiki/Ishikawa_diagram)
  * 5-Why-Methode: Wikipedia, „Five whys“, [https://en.wikipedia.org/wiki/Five_whys](https://en.wikipedia.org/wiki/Five_whys)
  * Post-Incident-Review im Vergleich (Postmortem): Google, „Site Reliability Engineering“, Kapitel „Postmortem Culture: Learning from Failure“, [https://sre.google/sre-book/postmortem-culture/](https://sre.google/sre-book/postmortem-culture/)
  * MTTR und MTBF: keine einheitliche Quelle; MTTR wird in der Praxis unterschiedlich definiert (Repair, Restore, Recovery, Respond, Resolve). Dieser Lehrplan legt in Modul 8 eine Definition fest.

### 3. Labor-Setup & Rahmenbedingungen

Für diesen Lehrplan ist **kein technisches Labor** (keine Hyper-V-Umgebung, keine VMs) erforderlich. Alle Praxisaufgaben werden als analytische Fallstudien, Rechen- oder Dokumentationsaufgaben durchgeführt. 

**Erforderliche Rahmenbedingungen (ab Modul 1):**
* Ein PC mit Standard-Office-Software (Textverarbeitung, Tabellenkalkulation) und einem Zeichenwerkzeug für Diagramme (z. B. LibreOffice Draw) oder Papier und Stift.
* Vom Dozenten bereitgestelltes Material (siehe Tabelle unten).
* Die Fallstudien basieren auf dem fiktiven Unternehmen `example.com` (Domain nach RFC 2606 für Beispiele reserviert) unter Verwendung von internen IP-Bereichen nach RFC 1918.

**Material des Dozenten:**

| Material | Verwendet in | Inhalt |
| :--- | :--- | :--- |
| Architekturbeschreibung `example.com` | Modul 1 | Kurze Beschreibung des Unternehmens mit mindestens drei Services (z. B. E-Mail, ERP, File-Sharing) und dem Netzplan unten |
| Vorlagen: Ticket, Change Request (RFC), KEDB-Eintrag, Post-Incident-Review | Modul 2, 4, 6, 8 | Leere Formulare als PDF, DOCX oder ODT |
| Szenarien zur Change-Klassifizierung | Modul 6 | Fünf Szenarien (siehe Modul 6, Aufgabe 1) |
| Liste von 15 Ticket-Überschriften | Modul 4 | Fiktive Tickets mit mindestens zwei erkennbaren Mustern (z. B. wiederholte Verbindungsabbrüche im Subnetz `10.2.0.0/24`) und einigen Einzelfällen |

**Netzplan `example.com` (Annahme, gilt für alle Fallstudien):**

| Bezeichnung | Adresse | Rolle | Verwendet in |
| :--- | :--- | :--- | :--- |
| Gateway / Core-Router | `10.0.0.1` | Übergang ins Internet, Firewall | Modul 2, 7 |
| Büro-Netz | `10.1.0.0/16` | Arbeitsplätze | Modul 1 |
| WLAN-Netz Konferenzräume | `10.2.0.0/24` | WLAN der Konferenzräume | Modul 4, 5 |
| Datenbankserver | `10.5.5.10` | Datenbank | Modul 5 |
| ERP-System | `10.10.10.50` | Zentrales ERP-System | Modul 3 |

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen des IT Service Managements (ITIL 4)
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen einem Service, einem Incident, einem Problem, einem Change und einem Service Request erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Grundgedanken der ITIL-4-Wertschöpfungskette benennen.
* **Voraussetzungen:** Keine.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Einführung in das IT Service Management und ITIL 4 (Service-Wertschöpfungskette) | 2 |
| 1.2 | Grundbegriffe: Service, Wert, Benutzer, Kunde, Sponsor | 2 |
| 1.3 | Abgrenzung der Practices: Incident, Problem, Change (und Service Request) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Fallstudie "Die IT der example.com":** Lies die vom Dozenten bereitgestellte Architekturbeschreibung des fiktiven Unternehmens `example.com`. Identifiziere in der Beschreibung drei angebotene Services (z. B. E-Mail, ERP, File-Sharing) und ordne die abhängigen Netzwerkkomponenten (z. B. das Subnetz `10.1.0.0/16`) grob zu.
2. **Begriffsabgrenzung:** Erstelle ein Dokument und beschreibe anhand von vier fiktiven Alltags-IT-Szenarien (z. B. "Drucker druckt nicht", "Neue Software wird benötigt", "Der Mailserver stürzt jeden Montag ab", "Der Server-Raum bekommt eine neue Klimaanlage") jeweils, ob es sich um einen Incident, ein Problem, einen Change oder einen Service Request handelt. Begründe die Entscheidung.

#### Kontrollfragen
1. Was ist nach ITIL 4 die Definition eines "Services"?
2. Warum ist die Unterscheidung zwischen einem Incident und einem Change im IT-Alltag wichtig?
3. Welche Rolle spielt der Endnutzer im Vergleich zum Kunden (Customer) bei der Definition von Anforderungen?
4. Nenne die Aktivitäten der ITIL-4-Wertschöpfungskette und ordne ihnen Incident Management und Change Enablement grob zu.

---

### Modul 2: Incident Management – Lebenszyklus und Klassifizierung
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den vollständigen Lebenszyklus eines Incidents dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende Störungen anhand von Auswirkung (Impact) und Dringlichkeit (Urgency) priorisieren.
* **Voraussetzungen:** Modul 1

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Der Incident-Lebenszyklus: Erfassung, Diagnose, Behebung, Schließung | 2 |
| 2.2 | Kategorisierung und Priorisierung (Impact & Urgency) | 2 |
| 2.3 | Initialdiagnose und Dokumentation von Tickets | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Priorisierungs-Matrix erstellen:** Erstelle eine 3x3-Matrix für Auswirkung (Hoch, Mittel, Gering) und Dringlichkeit (Hoch, Mittel, Gering). Definiere die resultierenden Prioritäten (z. B. P1 bis P5) und lege fiktive Reaktionszeiten fest.
2. **Ticket-Erfassung und Lebenszyklus:** Nimm drei fiktive Störungsmeldungen (z. B. "Ausfall des Core-Routers 10.0.0.1", "Passwort vergessen") und überführe sie in eine strukturierte Ticket-Vorlage. Weise Kategorien und Prioritäten basierend auf deiner Matrix zu und notiere eine Initialdiagnose. Führe das Ticket mit der höchsten Priorität durch den gesamten Lebenszyklus (Erfassung, Diagnose, Behebung, Schließung) und dokumentiere dabei Status und Zeitstempel jeder Phase.

#### Kontrollfragen
1. Aus welchen Hauptphasen besteht der Incident-Lebenszyklus?
2. Wie unterscheiden sich Auswirkung (Impact) und Dringlichkeit (Urgency)?
3. Warum ist eine saubere Kategorisierung bei der Ticketerfassung wichtig für die spätere Trendanalyse und das Problem Management (Modul 4)?

---

### Modul 3: Incident Management – Eskalation und Kommunikation
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende zwischen hierarchischer und funktionaler Eskalation unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Kommunikationsplan für einen Major Incident entwerfen.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Eskalationsarten: Hierarchisch vs. Funktional (Tier 1-3) | 2 |
| 3.2 | Major Incident Management: Definition und Sonderprozesse | 2 |
| 3.3 | Kommunikationstechnik und SLA-Überwachung | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Major Incident Kommunikation:** Das zentrale ERP-System von `example.com` (IP: `10.10.10.50`) ist ausgefallen (P1). Lege zuerst eine kurze Ereignis-Zeitleiste mit mindestens fünf Zeitpunkten fest (Beginn, Meldung, Eskalation, Ursache gefunden, Behebung). Entwirf dann einen Kommunikationsplan (Empfänger, Kanal, Aktualisierungsintervall, Verantwortlicher) und schreibe drei standardisierte Kommunikationsvorlagen: 1. Initiale Meldung an alle Nutzer, 2. Update nach 2 Stunden, 3. Entwarnung nach Behebung. Hebe Zeitleiste und Vorlagen für Modul 8 auf.
2. **Eskalationspfad zeichnen:** Zeichne ein Ablaufdiagramm für ein Ticket, das vom 1st-Level-Support wegen fehlender Rechte (funktionale Eskalation) an den 2nd-Level-Netzwerk-Support übergeben wird und aufgrund drohender SLA-Verletzung hierarchisch an den IT-Leiter eskaliert wird.

#### Kontrollfragen
1. Wann kommt eine hierarchische Eskalation im Incident Management zum Einsatz?
2. Was unterscheidet einen "Major Incident" von einem regulären "High Priority Incident"?
3. Welche Angaben gehören typischerweise in ein SLA (Service Level Agreement) bezüglich Incident-Reaktionszeiten?

---

### Modul 4: Problem Management – Grundlagen und reaktive Analyse
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Beziehung zwischen wiederkehrenden Incidents und einem Problem erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Workarounds dokumentieren und in eine Known Error Database (KEDB) überführen.
* **Voraussetzungen:** Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Problem vs. Incident und Definition von Known Errors | 2 |
| 4.2 | Reaktives Problem Management: Aus Incidents lernen | 2 |
| 4.3 | Workarounds und die Known Error Database (KEDB) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Incident-Trend-Analyse:** Analysiere die vom Dozenten bereitgestellte Liste von 15 fiktiven Ticket-Überschriften. Identifiziere Muster (z. B. wiederholte Verbindungsabbrüche im Subnetz `10.2.0.0/24`) und formuliere daraus zwei Problem-Tickets.
2. **KEDB-Eintrag verfassen:** Schreibe einen detaillierten Eintrag für die Known Error Database. Beschreibe das Symptom, die fehlerhafte Komponente und formuliere einen konkreten, sicheren Workaround für den 1st-Level-Support.

#### Kontrollfragen
1. Ab welchem Zeitpunkt wird ein "Problem" offiziell zu einem "Known Error"?
2. Warum löst ein Workaround zwar den Incident, aber nicht das Problem?
3. Welche Auswirkung hat eine gut gepflegte KEDB auf die Lösungszeiten im Incident Management?

---

### Modul 5: Problem Management – Proaktive Analyse und RCA
* **Priorität:** 2
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Root Cause Analysis (RCA) Methoden anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Ishikawa-Diagramme und die 5-Why-Methode für IT-Störungen erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende reaktive und proaktive Problemidentifikation unterscheiden.
* **Voraussetzungen:** Modul 4

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Root Cause Analysis (RCA): Grundprinzipien und proaktive Problemidentifikation | 2 |
| 5.2 | Die 5-Why-Methode in der Praxis | 2 |
| 5.3 | Das Ishikawa-Diagramm (Fischgrätendiagramm) für IT-Systeme | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **5-Why-Analyse:** Ein fiktiver Datenbankserver (`10.5.5.10`) ist aufgrund einer vollen Festplatte abgestürzt. Ausgangslage: Die Platte war durch Logdateien gefüllt; ein Alarm bei 90 % Füllstand wurde ausgelöst, ging aber an eine nicht mehr gelesene Gruppenadresse; wer die Logdateien aufräumt, war nie festgelegt. Führe eine schriftliche 5-Why-Analyse durch, bis du eine prozessuale oder organisatorische Ursache (Root Cause) findest, nicht nur eine technische. Die Zahl fünf ist eine Faustregel: Höre auf, wenn eine Ursache gefunden ist, die du beeinflussen kannst.
2. **Ishikawa-Diagramm:** Zeichne ein Ishikawa-Diagramm für das Problem "Häufige WLAN-Verbindungsabbrüche im Konferenzraum" (Netz `10.2.0.0/24`). Nutze die Kategorien Mensch, Maschine, Methode und Material (optional Messung und Umgebung). Trage in mindestens drei Kategorien Ursachen ein.

#### Kontrollfragen
1. Was ist das Ziel einer Root Cause Analysis (RCA)?
2. Welche Gefahr besteht, wenn man bei der 5-Why-Methode zu früh aufhört, Fragen zu stellen?
3. Wofür stehen die "4 M" (oder "6 M") im Ishikawa-Diagramm und wie lassen sie sich auf die IT übertragen?
4. Wie unterscheiden sich reaktive und proaktive Problemidentifikation? Nenne je ein Beispiel.

---

### Modul 6: Change Enablement – Grundlagen und Change-Typen
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Standard, Normal und Emergency Changes unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen vollständigen Change Request (RFC) ausfüllen.
* **Voraussetzungen:** Modul 1, Modul 2

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Definition und Ziel des Change Enablements | 2 |
| 6.2 | Change-Typen: Standard, Normal, Emergency | 2 |
| 6.3 | Erstellung eines Request for Change (RFC) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Change-Klassifizierung:** Ordne fünf gegebene IT-Szenarien den drei Change-Typen zu und begründe deine Wahl: "Sicherheits-Patch für Zero-Day-Lücke", "Monatliches Einspielen der Betriebssystem-Updates nach festem, vorab genehmigtem Verfahren", "Austausch des Core-Switches", "Umstellung des ERP-Systems auf eine neue Hauptversion" und "Anlage eines neuen Benutzers". Eines der Szenarien ist kein Change, sondern ein Service Request: Erkenne es und begründe.
2. **RFC Erstellung:** Fülle eine RFC-Vorlage für einen Normal Change ("Migration des lokalen File-Servers nach SharePoint") aus. Benenne den Sponsor, die technischen Abhängigkeiten und die geplante Dauer.

#### Kontrollfragen
1. Was ist das Hauptmerkmal eines "Standard Changes" im Vergleich zu einem "Normal Change"?
2. Warum benötigt ein Emergency Change einen anderen Genehmigungsweg als ein Normal Change?
3. Welche Informationen sollte ein RFC mindestens enthalten?
4. Was ist das Ziel von Change Enablement nach ITIL 4?

---

### Modul 7: Change Enablement – Evaluierung und Wartungsfenster
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Risikoanalyse für einen Change durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Wartungsfenster planen und Rückfallpläne (Rollbacks) definieren.
* **Voraussetzungen:** Modul 6 (das Ergebnis aus Modul 6, Aufgabe 2, liegt vor)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Evaluierung, Risikoanalyse, Change Authority und das CAB (Change Advisory Board) | 2 |
| 7.2 | Planung: Wartungsfenster, Downtime und Kommunikation | 2 |
| 7.3 | Remediation: Erstellung von Rückfall- und Rollback-Plänen | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Risikoanalyse:** Nimm den RFC aus Modul 6 (Migration File-Server). Führe eine Risikoanalyse durch. Benenne drei mögliche Risiken während der Umsetzung und formuliere Gegenmaßnahmen zur Risikominderung.
2. **Rollback-Planung:** Ein Change beinhaltet das Update der Firewall-Regeln auf dem Gateway `10.0.0.1`. Dokumentiere einen exakten, schrittweisen Rollback-Plan, um bei einem Fehler den alten Zustand wiederherzustellen; beginne mit der Sicherung der aktuellen Konfiguration. Definiere den "Point of no Return".
3. **Wartungsfenster planen:** Plane für den File-Server-Umzug aus Modul 6 ein Wartungsfenster: Zeitpunkt mit Begründung, erwartete Downtime, betroffene Nutzer, Ankündigung (wann und auf welchem Weg) und ein Abbruchkriterium, ab dem der Rollback aus Aufgabe 2 gestartet wird.

#### Kontrollfragen
1. Welche Aufgabe hat das Change Advisory Board (CAB), und wie unterscheidet es sich von der Change Authority nach ITIL 4?
2. Was bedeutet der "Point of no Return" in einem Change-Plan?
3. Warum wird für einen Normal Change in der Regel ein dokumentierter Rückfallplan (Rollback) verlangt?
4. Welche Faktoren bestimmen die Wahl eines Wartungsfensters?

---

### Modul 8: Post-Incident-Review und Service-Metriken
* **Priorität:** 2
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Kennzahlen MTTR und MTBF berechnen und interpretieren.
  * Nach Abschluss dieses Moduls kann der Lernende einen Post-Incident-Review (PIR) durchführen und dokumentieren.
* **Voraussetzungen:** Modul 3, Modul 7 (die Ergebnisse aus Modul 3, Aufgabe 1, liegen vor)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Das Post-Incident-Review (PIR) / Post-Implementation Review | 2 |
| 8.2 | Wichtige Kennzahlen: MTTR, MTBF, First-Time-Fix-Rate | 2 |
| 8.3 | Continual Service Improvement (CSI) in der Praxis | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Kennzahlen berechnen:** Für einen Webserver wurden in einem Beobachtungszeitraum von 30 Tagen (720 Stunden) zehn Ausfälle erfasst:

   | Nr. | Ausfallbeginn | Wiederherstellung |
   | :--- | :--- | :--- |
   | 1 | Tag 3, 08:10 | Tag 3, 09:40 |
   | 2 | Tag 5, 14:00 | Tag 5, 14:30 |
   | 3 | Tag 9, 22:15 | Tag 10, 02:15 |
   | 4 | Tag 12, 10:00 | Tag 12, 10:45 |
   | 5 | Tag 15, 03:30 | Tag 15, 05:30 |
   | 6 | Tag 18, 16:20 | Tag 18, 17:20 |
   | 7 | Tag 21, 07:00 | Tag 21, 07:30 |
   | 8 | Tag 24, 11:10 | Tag 24, 13:40 |
   | 9 | Tag 27, 19:00 | Tag 27, 19:45 |
   | 10 | Tag 30, 09:00 | Tag 30, 10:00 |

   Berechne die Mean Time To Repair (MTTR = Gesamtausfallzeit / Anzahl der Ausfälle) und die Mean Time Between Failures (MTBF = (Beobachtungszeitraum − Gesamtausfallzeit) / Anzahl der Ausfälle) in Stunden. Halte fest, welche Definition du verwendet hast: MTTR wird in der Literatur unterschiedlich definiert.
2. **PIR-Dokumentation:** Basierend auf dem Major Incident und der Zeitleiste aus Modul 3, Aufgabe 1, erstelle einen formalen Post-Incident-Review-Bericht. Beantworte darin: Was ist passiert? Warum ist es passiert? Wie wurde reagiert? Was wird getan, damit es nicht wieder passiert (CSI)?

#### Kontrollfragen
1. Was ist der Hauptzweck eines Post-Incident-Reviews (PIR)?
2. Wie unterscheidet sich die MTTR (Mean Time To Repair) von der Reaktionszeit?
3. Warum kann eine hohe First-Time-Fix-Rate auf eine gut gepflegte KEDB und gut geschulten 1st-Level-Support hindeuten, und welche anderen Ursachen sind denkbar?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (8 × 3 × 2 = 48 UE), Prioritäten (6x P1, 2x P2) und die Zahl der Module blieben unverändert. Aufgaben und Fragen kamen hinzu; ob 6 UE je Modul dafür reichen, ist unerprobt. Es gibt kein technisches Labor; die Aufgaben wurden nur gelesen und fachlich geprüft, nicht durchgespielt. Die Berechnung in Modul 8 wurde per Skript nachgerechnet.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf | Out-of-Scope um „keine Zertifizierungsvorbereitung“ und „ITIL 5 nicht Gegenstand“ ergänzt | Wie bei P40; Version und Stand sollen genannt werden |
| A.1 | Hinweis: kein Pflichtmodul setzt ein Prio-2-Modul voraus | Die Regel stand nirgends; geprüft: kein Modul nennt Modul 5 oder 8 als Voraussetzung |
| A.2 | ITIL-Herausgeber PeopleCert, Stand nicht geprüft; Practice Guides, ITIL-Versionsstand, RFC 2606 und Hilfsmittel (Ishikawa, 5 Whys, SRE-Postmortem, MTTR) ergänzt; ISO-Änderung 1:2024 genannt | 5-Why, Ishikawa, MTTR, PIR und die Practices hatten keine Quelle; AXELOS ist laut P40-Prüfung nicht mehr Herausgeber; die ISO-Seite nennt Änderung 1:2024; `example.com` kommt aus RFC 2606, nicht aus RFC 1918 |
| A.3 | Zeichenwerkzeug ergänzt; Tabelle „Material des Dozenten“ und „Netzplan“ neu; „Priorisierungs-Matrizen“ aus den Vorlagen entfernt | Architekturbeschreibung (Modul 1), Ticketliste (Modul 4) und Szenarien (Modul 6) wurden verlangt, aber nicht aufgeführt; die Matrix wird in Modul 2 selbst erstellt; die IP-Adressen (`10.0.0.0/8`, `10.0.0.1`, `10.10.10.50`, `10.5.5.10`, `10.1.0.0/16`, `10.2.0.0/24`) hatten keinen gemeinsamen Netzplan |
| Modul 1 | Lernziel 1, Einheit 1.1 und 1.3, Aufgabe 2, Frage 4 | Das Lernziel „Wertschöpfungskette“ hatte keine Einheit, Aufgabe oder Frage; „Neue Software wird benötigt“ ist nach ITIL 4 ein Service Request, aber nur Incident, Problem und Change standen zur Wahl; Szenario für ein Problem fehlte |
| Modul 2 | Aufgabe 2, Frage 3 | Das Lernziel „vollständigen Lebenszyklus dokumentieren“ wurde nur bis zur Erfassung geübt; „Core-Router für 10.0.0.0/8“ war kein sinnvolles Ziel (ganzer privater Adressraum); Frage 3 griff auf Modul 4 vor, ohne es zu nennen |
| Modul 3 | Aufgabe 1, Frage 3 | Das Lernziel „Kommunikationsplan“ wurde nur mit Vorlagen geübt; Modul 8 braucht eine Zeitleiste, die Modul 3 nicht lieferte; „zwingend“ im SLA ist eine absolute Behauptung |
| Modul 4 | Aufgabe 1 | Verweist auf die Ticketliste des Dozenten (Material fehlte) |
| Modul 5 | Lernziel 3, Einheit 5.1, Aufgaben 1 und 2, Frage 4 | Der Titel nennt „Proaktive Analyse“, kein Lernziel, keine Einheit und keine Aufgabe behandelte sie; die 5-Why-Aufgabe hatte keine Ausgangslage; „Material“ passt schlecht zur IT, daher optional Messung und Umgebung |
| Modul 6 | Aufgabe 1, Fragen 3 und 4 | „Anlage eines neuen Benutzers“ ist nach ITIL 4 in der Regel ein Service Request; nur drei Szenarien waren genannt (gefordert: fünf); Einheit 6.1 hatte keine Frage; „zwingend“ im RFC ist eine absolute Behauptung (ITIL schreibt keine Pflichtfelder vor, nicht bestätigt) |
| Modul 7 | Voraussetzungen, Einheit 7.1, Aufgaben 2 und 3, Fragen 1, 3 und 4 | Das Lernziel „Wartungsfenster planen“ und Einheit 7.2 hatten keine Aufgabe und keine Frage; in ITIL 4 entscheidet die Change Authority, das CAB ist nicht für jeden Change vorgesehen; „ist Voraussetzung“ zu absolut; die Firewall-Änderung begann nicht mit einer Sicherung |
| Modul 8 | Voraussetzungen, Aufgaben 1 und 2, Frage 3 | „Du erhältst die Rohdaten“: Daten und Definitionen fehlten (MTBF-Variante, Beobachtungszeitraum); der PIR brauchte Material aus Modul 3; Frage 3 setzte ein Ergebnis voraus („ist ein Indikator“) |

**Kontrollwerte Modul 8, Aufgabe 1:** Gesamtausfallzeit 14,5 h; MTTR = 14,5 h / 10 = 1,45 h; Betriebszeit = 720 h − 14,5 h = 705,5 h; MTBF = 705,5 h / 10 = 70,55 h. Die zehn Ausfalldauern sind 1,5; 0,5; 4,0; 0,75; 2,0; 1,0; 0,5; 2,5; 0,75 und 1,0 Stunden. Die Daten sind frei erfunden.

**Bewertung des Prüfvermerks der ersten Fassung:** Das Format wurde eingehalten (Stichprobe je Punkt). Die Bewertung ist trotzdem zu gut ausgefallen. Punkt 1 ist korrekt (48 UE, 6x P1, 2x P2). Punkt 2 ist teilweise erfüllt (Architekturbeschreibung, Ticketliste, Szenarien und Zeichenwerkzeug fehlten; die „Matrix in Modul 2“ wurde als Vorlage gelistet, obwohl sie selbst zu erstellen ist). Punkt 3 ist nicht erfüllt (geprüft wurde nur, ob Herausgeber und URL „existieren“; AXELOS ist veraltet, ISO-Änderung 2024 fehlte, RCA, 5 Whys, Ishikawa, MTTR und PIR hatten keine Quelle; „alle IPs beziehen sich auf RFC 1918“ ist keine Quellenprüfung). Punkt 4 ist teilweise erfüllt (der Prüfvermerk behauptet, Modul 3, Aufgabe 2, simuliere ein Ticket aus Modul 2: das stimmt nicht, die Aufgabe ist allgemein; Modul 8 brauchte eine Zeitleiste, die Modul 3 nicht lieferte; die IP-Adressen hatten keinen Netzplan). Punkt 5 ist nicht erfüllt (geprüft wurde nur Modul 5; Lernziele ohne Aufgabe oder Frage in Modul 1, 2, 3, 5 und 7, Einheit 6.1 ohne Frage). Punkt 6 ist erfüllt; der Prüfvermerk nennt „Aufgabe 7.2“, gemeint ist Aufgabe 2 bzw. Einheit 7.3, und die Sicherung vor der Änderung fehlte. Punkt 7 ist erfüllt. Punkt 8 ist teilweise erfüllt (Namen und Adressen ohne Definition, RFC 2606 fehlte). Punkt 9 ist erfüllt.

**Hinweise und offene Punkte:**

* **Bestätigt (Sekundärquellen, Suchtreffer abgerufen):** Known Error = „ein Problem, das analysiert, aber noch nicht gelöst ist“ und KEDB (open-exam-prep.com); Change-Typen Standard, Normal, Emergency, Change Authority statt CAB für jeden Change (itsm.tools); ISO/IEC 20000-1:2018 mit Änderung 1:2024 (iso.org). Reaktive und proaktive Problemidentifikation laut open-exam-prep.com.
* **Nicht bestätigt:** Die Aktivitäten der Wertschöpfungskette (Modul 1, Frage 4), die Aussage „Anlage eines neuen Benutzers ist ein Service Request“ (itsm.tools behandelt Service Requests nicht), die Practice-Guide-Namen, das Datum von RFC 2606, die Hilfsmittel-Quellen (nur Suchtreffer) und die AXELOS-Adresse (Abruf war nicht möglich). Vor dem Kurs gegen das ITIL-4-Foundation-Buch und die Practice Guides prüfen.
* **ITIL Version 5:** Der Lehrplan bleibt bei ITIL 4. Bei einer Umstellung sind Begriffe und Praktiken neu zu prüfen.
* **Überschneidung mit P40 (ITIL 4 Grundlagen):** Modul 1 und Einheit 8.2 (MTTR, MTBF) kommen auch in P40 vor. Ob P41 darauf aufbaut und Modul 1 kürzer wird, ist offen.
* **Optionales Ticketsystem:** Der Kursdatensatz nennt „optional ein Open-Source-Ticketsystem“; die erste Fassung übernahm das nicht. Es bleibt weg, die Aufgaben laufen mit Vorlagen.
* **Zeitaufwand:** Modul 7 hat jetzt drei Aufgaben. Ob 6 UE reichen, ist unerprobt.
