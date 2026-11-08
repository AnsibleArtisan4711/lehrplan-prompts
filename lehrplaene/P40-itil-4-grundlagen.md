# Lehrplan: ITIL 4 Grundlagen

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU). |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze). |
| **Gesamtumfang** | 8 Module, 48 Unterrichtseinheiten (UE). |
| **Fokus-Technologien** | ITIL 4 (Service-Wertschöpfungssystem, Praktiken, Leitprinzipien). |
| **Thematische Abgrenzung (Out of Scope)** | Keine technische Konfiguration und kein Labor; keine Überschneidung mit den vorhandenen Technik-Lehrplänen (Verweise nur kurz); keine Zertifizierungsvorbereitung (Prüfungsfragen, Braindumps). Bezugsrahmen ist ITIL 4; ITIL Version 5 ist nicht Gegenstand (siehe Quellen). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Einführung in IT-Servicemanagement und ITIL 4 | 1 | 6 |
| 2 | Die 7 Leitprinzipien (Guiding Principles) | 1 | 6 |
| 3 | Das Service-Wertschöpfungssystem (SVS) und die Vier Dimensionen | 1 | 6 |
| 4 | ITIL-Praktiken: Incident Management & Troubleshooting | 1 | 8 |
| 5 | ITIL-Praktiken: Problem & Change Enablement | 1 | 6 |
| 6 | ITIL-Praktiken: Service Desk, Request Fulfilment & Monitoring | 1 | 6 |
| 7 | Rollen, Kennzahlen (KPIs) und SLAs im IT-Betrieb | 2 | 4 |
| 8 | Continual Improvement (KVP) im System-Alltag | 2 | 6 |
| **Gesamt** | **Summe: 6x Pri 1, 2x Pri 2** | | **48** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (Pflicht) bilden die Kernkompetenz ab. Module mit Priorität 2 (Vertiefung) sind Ergänzungen für ein erweitertes Verständnis im Systembetrieb.*

### 2. Quellen

* ITIL Foundation: ITIL 4 Edition. Herausgeber: AXELOS, inzwischen PeopleCert. Datum: 2019 (Stand nicht geprüft). URL: `https://www.axelos.com/certifications/itil-service-management/itil-4-foundation` (nicht geprüft, Seite des früheren Herausgebers).
* ITIL 4 Practice Guides (Incident Management, Problem Management, Change Enablement, Service Desk, Service Request Management, Monitoring and Event Management, Service Level Management, Continual Improvement). Herausgeber: AXELOS bzw. PeopleCert. Datum: Stand nicht geprüft. URL: Keine geprüfte Quelle.
* Versionsstand: Laut einer Sekundärquelle (Advised Skills, „ITIL version 5 in 2026: what is confirmed, what is available and what comes next“, 16.02.2026, abgerufen am 08.11.2026, URL: `https://www.advisedskills.com/blog/it-service-management/itil-version-5-in-2026-what-is-confirmed-what-is-available-and-what-comes-next.md`) führt PeopleCert ITIL Version 5 im Jahr 2026 schrittweise ein; ITIL 4 läuft dort parallel, ein Enddatum von ITIL 4 ist in der Quelle nicht genannt. Dieser Lehrplan bleibt bei ITIL 4. Ob Begriffe und Praktiken in Version 5 abweichen, ist nicht geprüft.
* Hilfsmittel ohne eigene Norm (PDCA-Zyklus nach Deming, 5-Why- und Ishikawa-Methode, MTTR und MTBF, RACI-Matrix, PESTLE): Keine geprüfte Quelle. Die Begriffe werden im Kurs mit einer festen Definition verwendet (Definition von MTTR und MTBF in Modul 7).
* RFC 1918 - Address Allocation for Private Internets. Herausgeber: IETF. Datum: Februar 1996. URL: `https://datatracker.ietf.org/doc/html/rfc1918`
* RFC 2606 - Reserved Top Level DNS Names (für example.com). Herausgeber: IETF. Datum: Juni 1999. URL: `https://datatracker.ietf.org/doc/html/rfc2606`

### 3. Labor-Setup & Rahmenbedingungen

* **Technisches Labor:** Nicht erforderlich (Out of Scope).
* **Praxiskonzept:** Alle Übungen basieren auf Dokumentationsaufgaben und Fallstudien. Es kommt das fiktive Unternehmen „Example Corp“ mit der reservierten Domäne `example.com` zum Einsatz (RFC 2606). Das fiktive interne Netz ist `192.168.10.0/24` (RFC 1918) mit den Systemen `fileserver01` (Dateiserver), `erp01` (ERP-System), `www.example.com` (Webserver) und dem VPN-Dienst `vpn.example.com`. Es wird nichts installiert oder ausgeführt; Konsolenausgaben in Tickets sind frei erfunden, aber in sich stimmig.
* **Werkzeuge (erforderlich ab Modul 1):** Textverarbeitungsprogramm (z. B. Word, LibreOffice) oder Tabellenkalkulation für die Dokumentationsübungen.
* **Vom Kursleiter bereitzustellen:** (1) eine Ticket-Vorlage mit den Feldern Ticket-ID, Melder, Kategorie, Auswirkung, Dringlichkeit, Priorität, Beschreibung, Diagnose, Workaround, Status (erforderlich ab Modul 1, genutzt in Modul 4); (2) ein Logauszug mit etwa zehn fiktiven Einträgen von `www.example.com` (erforderlich für Modul 6); (3) eine Fallstudien-Vorlage mit den Abschnitten Ausgangslage, Analyse, Ergebnis (erforderlich ab Modul 1).

---

## B. Detaillierter Modulaufbau

### Modul 1: Einführung in IT-Servicemanagement und ITIL 4
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Kernbegriffe des IT-Servicemanagements (Service, Wert, Co-Creation) eigenständig definieren.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen Outputs und Outcomes im IT-Umfeld erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Relevanz von ITIL 4 für den Alltag eines Systemadministrators aufzeigen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Bedeutung von Services und Co-Creation of Value | 2 |
| 1.2 | Kernbegriffe: Utility (Zweckmäßigkeit) vs. Warranty (Garantie) | 2 |
| 1.3 | Outputs, Outcomes, Kosten und Risiken im IT-Betrieb | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Definition eines IT-Services.** Analysieren Sie den Service „Unternehmensweites File-Sharing“ für die Example Corp. Dokumentieren Sie in einer Fallstudien-Vorlage die *Utility* (Welchen Zweck erfüllt der Speicher?) und die *Warranty* (Welche Verfügbarkeit und Sicherheit muss garantiert sein?).
2. **Titel: Output vs. Outcome.** Beschreiben Sie für ein geplantes Server-Update den technischen Output (z. B. System läuft auf Version X) und den geschäftlichen Outcome (z. B. Fachabteilung hat schnellere Ladezeiten).
3. **Titel: ITIL im eigenen Alltag.** Wählen Sie drei typische Aufgaben eines Systemadministrators (z. B. ein Passwort zurücksetzen, einen Server patchen, eine Störung beheben). Notieren Sie je Aufgabe, welchen Outcome sie für den Kunden bringt, welches Risiko oder welche Kosten der Kunde dadurch nicht selbst tragen muss und wo ohne Struktur Probleme entstehen würden.

#### Kontrollfragen
1. Wie definieren Sie den Begriff „Co-Creation of Value“ im Kontext eines IT-Dienstleisters und seines Kunden?
2. Warum reicht Utility allein nicht aus, um einen erfolgreichen Service bereitzustellen?
3. Erklären Sie den Unterschied zwischen Kosten und Risiken, die der Kunde durch den Service nicht mehr selbst tragen muss, und solchen, die der Service ihm auferlegt. Nennen Sie je ein Beispiel.
4. Definieren Sie in eigenen Worten „Service“ und „Wert“ und nennen Sie ein Beispiel aus dem Alltag eines Administrators.

### Modul 2: Die 7 Leitprinzipien (Guiding Principles)
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die 7 Leitprinzipien von ITIL 4 aufzählen und ihre Bedeutung erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Prinzipien auf reale Sysadmin-Szenarien anwenden (z. B. Migrationen, Skript-Automatisierung).
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Prinzipien 1-3: Focus on value, Start where you are, Progress iteratively | 2 |
| 2.2 | Prinzipien 4-5: Collaborate and promote visibility, Think and work holistically | 2 |
| 2.3 | Prinzipien 6-7: Keep it simple and practical, Optimize and automate | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Anwendung der Leitprinzipien auf ein Projekt.** Die Example Corp plant den Austausch der Kern-Switches im Rechenzentrum. Wenden Sie die Prinzipien „Start where you are“ und „Progress iteratively“ auf die Planung an. Erstellen Sie ein kurzes Konzept (max. 1 Seite), wie der Ist-Zustand erfasst und der Austausch in sicheren Phasen durchgeführt wird.
2. **Titel: Automatisierungspotenziale bewerten.** Sie verwalten 50 Linux-Server. Wenden Sie das Prinzip „Optimize and automate“ an, um darzulegen, welche manuellen administrativen Prozesse (z. B. Benutzeranlage, Updates) in welcher Reihenfolge automatisiert werden sollten.

#### Kontrollfragen
1. Warum sollte laut ITIL 4 vor jeder Automatisierung eine Optimierung des Prozesses stattfinden?
2. Wie hilft das Prinzip „Think and work holistically“ bei der Behebung eines Netzwerkfehlers?
3. Erklären Sie den Ansatz „Start where you are“ im Gegensatz zu einem kompletten „Greenfield-Ansatz“ bei der Systemablöse.
4. Nennen Sie alle sieben Leitprinzipien und erklären Sie zwei davon an je einem Beispiel aus dem Administratorenalltag.

### Modul 3: Das Service-Wertschöpfungssystem (SVS) und die Vier Dimensionen
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Komponenten des SVS (Service Value System) skizzieren.
  * Nach Abschluss dieses Moduls kann der Lernende die vier Dimensionen des Servicemanagements auf einen neuen IT-Dienst anwenden.
* **Voraussetzungen:** Modul 1 und 2.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Aufbau des SVS (fünf Komponenten: Leitprinzipien, Governance, Service Value Chain, Praktiken, Continual Improvement; Eingang Chance/Nachfrage, Ausgang Wert) | 2 |
| 3.2 | Dimension 1 & 2: Organisationen/Menschen, Informationen/Technologie | 2 |
| 3.3 | Dimension 3 & 4: Partner/Lieferanten, Wertströme/Prozesse; externe Faktoren (PESTLE) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Vier-Dimensionen-Modellierung.** Die Example Corp führt einen neuen VPN-Dienst (`vpn.example.com`) für Homeoffice-Mitarbeiter ein. Modellieren Sie diesen Dienst tabellarisch anhand der vier Dimensionen. Berücksichtigen Sie z. B. Authentifizierungstechnologie (Dim 2) und Internet-Provider-Abhängigkeiten (Dim 3).
2. **Titel: Value Chain Mapping.** Ordnen Sie die Tätigkeit „Server-Hardware bestellen und ins Rack einbauen“ in die passenden Aktivitäten der Service Value Chain (Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support) ein.
3. **Titel: SVS skizzieren.** Zeichnen Sie das Service-Wertschöpfungssystem mit seinen fünf Komponenten (Chance/Nachfrage links, Wert rechts) und tragen Sie ein, wo der VPN-Dienst aus Aufgabe 1 jeweils vorkommt (z. B. welches Leitprinzip, welche Praktik, welche Verbesserung).

#### Kontrollfragen
1. Was passiert, wenn beim Design eines neuen Dienstes die Dimension „Partner und Lieferanten“ ignoriert wird?
2. Welche Rolle spielen externe Einflüsse (PESTLE-Faktoren) auf die vier Dimensionen?
3. Wofür steht die Aktivität „Obtain/Build“ in der Service Value Chain im Kontext der Systemadministration?

### Modul 4: ITIL-Praktiken: Incident Management & Troubleshooting
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Lebenszyklus eines Incidents beschreiben und dokumentieren.
  * Nach Abschluss dieses Moduls kann der Lernende Tickets richtig priorisieren und strukturierte Troubleshooting-Informationen eintragen.
  * Nach Abschluss dieses Moduls kann der Lernende Konzepte wie Swarming zur schnellen Fehlerbehebung erklären.
* **Voraussetzungen:** Modul 1, technisches Grundwissen in Netzwerken (IP-Adressen, Subnetze).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Definition Incident vs. Workaround, Ticket-Lebenszyklus | 2 |
| 4.2 | Priorisierung (Auswirkung und Dringlichkeit, Prioritätsmatrix), Kategorisierung | 2 |
| 4.3 | Troubleshooting-Prozesse, Diagnose-Outputs und Swarming | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Incident-Erfassung und Dokumentation.** In der Example Corp (internes Netz `192.168.10.0/24`) meldet eine Abteilung einen IP-Adresskonflikt, der den Zugriff auf das ERP-System `erp01` blockiert. Erfassen Sie in der Ticket-Vorlage ein vollständiges Ticket: Vergeben Sie eine Kategorie, schätzen Sie Dringlichkeit und Auswirkung ein, leiten Sie die Priorität mit einer selbst definierten Prioritätsmatrix ab und formulieren Sie die Problembeschreibung aus technischer Sicht. Dokumentieren Sie zusätzlich den Statusverlauf des Tickets von „Neu“ bis „Geschlossen“ (mindestens fünf Status mit fiktiven Zeitstempeln).
2. **Titel: Diagnose-Dokumentation im Ticket.** Fügen Sie dem Ticket aus Aufgabe 1 selbst erstellte, in sich stimmige Konsolenausgaben in Textform hinzu: `ipconfig /all` und `arp -a` (Windows) bzw. `ip neigh` (Linux) zeigen den Konflikt (z. B. dieselbe IP-Adresse mit zwei verschiedenen MAC-Adressen im Netz `192.168.10.0/24`), `ping` bestätigt die Erreichbarkeit. Gliedern Sie das Vorgehen in Troubleshooting-Schritte (Symptom, Hypothese, Test, Ergebnis) und formulieren Sie einen temporären Workaround (z. B. eine neue feste Adresse für den betroffenen Client), um den Betrieb wiederherzustellen. Die Ausgaben sind fiktiv; es wird nichts ausgeführt.

#### Kontrollfragen
1. Wie ergibt sich in der Regel die Priorität eines Incidents aus Auswirkung und Dringlichkeit?
2. Was unterscheidet das Konzept „Swarming“ vom klassischen hierarchischen Eskalationsmodell (Tier 1/2/3)?
3. Warum ist die schnelle Identifikation eines Workarounds im Incident Management oft wichtiger als die sofortige Ursachenfindung?

### Modul 5: ITIL-Praktiken: Problem & Change Enablement
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen Incident und Problem erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache Root Cause Analysis (RCA) strukturiert durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Change-Typen (Standard, Normal, Emergency) in der Systemadministration anwenden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Problem Management: Known Errors, Root Cause Analysis (RCA) | 2 |
| 5.2 | Change Enablement: Definition und Abgrenzung zu Incidents | 2 |
| 5.3 | Change-Modelle: Standard, Normal und Emergency Changes; Change Authority (z. B. CAB) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Root Cause Analysis (RCA).** Die Example Corp leidet seit Wochen unter sporadischen DNS-Timeouts, die als mehrere Incidents gemeldet wurden. Erstellen Sie einen Problem Record. Führen Sie eine RCA in Textform (z. B. nach der 5-Why-Methode oder per Ishikawa/Fischgräten-Dokumentation) durch und definieren Sie den Known Error.
2. **Titel: Change-Klassifizierung.** Klassifizieren Sie folgende drei Szenarien als Standard, Normal oder Emergency Change und begründen Sie Ihre Wahl schriftlich. Halten Sie Ihre Annahmen fest (z. B. ob für das Szenario ein vorab genehmigtes Verfahren existiert):
   * Einspielen eines kritischen Zero-Day-Patches auf der Firewall.
   * Austausch einer defekten Festplatte in einem RAID1-Verbund.
   * Upgrade des vCenter-Servers auf eine neue Major-Release-Version.

#### Kontrollfragen
1. Warum sollte ein Problem nicht durch den Service Desk in erster Instanz geschlossen werden?
2. Welche Kriterien müssen erfüllt sein, damit ein Change als „Standard Change“ gilt?
3. Was ist der Zweck eines Change Advisory Boards (CAB) bzw. einer Change Authority?
4. Worin unterscheiden sich Incident und Problem, und wann wird aus mehreren Incidents ein Problem?

### Modul 6: ITIL-Praktiken: Service Desk, Request Fulfilment & Monitoring
* **Priorität:** 1
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Service Requests von Incidents abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wichtigkeit eines zentralen Service Desks (SPOC) für Anwender beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Event Management und Monitoring-Kategorien anwenden.
* **Voraussetzungen:** Modul 4 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Die Rolle des Service Desks (Single Point of Contact - SPOC) | 2 |
| 6.2 | Service Request Management: Standardisierung und Automatisierung | 2 |
| 6.3 | Monitoring und Event Management (Info, Warnung, Ausnahme) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Service Request Modellierung.** Entwerfen Sie ein Bestellformular (als Dokumentvorlage) für eine neue virtuelle Maschine (VM) für Software-Entwickler bei der Example Corp. Definieren Sie, welche technischen Parameter abgefragt werden müssen und wer den Request genehmigen muss.
2. **Titel: Event-Klassifizierung.** Der Kursleiter stellt einen Logauszug mit etwa zehn fiktiven Einträgen von `www.example.com` bereit. Kategorisieren Sie die Einträge in Information, Warnung oder Ausnahme (Exception) und definieren Sie, welches Event automatisch einen Incident auslösen sollte.
3. **Titel: Request oder Incident?** Ordnen Sie sechs Meldungen jeweils einem Service Request oder einem Incident zu und begründen Sie Ihre Wahl: „Passwort vergessen“, „Drucker druckt nicht“, „neuer Mitarbeiter braucht ein Konto“, „Webseite liefert Fehler 500“, „Zugriff auf einen Ordner beantragen“, „Software-Lizenz verlängern“.

#### Kontrollfragen
1. Warum werden Service Requests in der Regel in einem eigenen Workflow bearbeitet und nicht wie Incidents?
2. Was ist der Hauptunterschied zwischen einer Warnung und einer Ausnahme (Exception) im Monitoring?
3. Welche Fähigkeiten benötigt ein moderner Service-Desk-Mitarbeiter neben reinem IT-Wissen?
4. Welche Vorteile hat ein zentraler Service Desk als Single Point of Contact für die Anwender und für den IT-Betrieb?

### Modul 7: Rollen, Kennzahlen (KPIs) und SLAs im IT-Betrieb
* **Priorität:** 2
* **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau und Zweck eines Service Level Agreements (SLA) erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende technische KPIs (wie MTTR, MTBF) berechnen und interpretieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Verantwortlichkeiten typischer Rollen im Servicebetrieb benennen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | SLAs, OLAs (Operational Level Agreements) und Underpinning Contracts; typische Rollen im Betrieb (z. B. Service Owner, Prozessverantwortliche, Service-Desk-Mitarbeiter) | 2 |
| 7.2 | Metriken und KPIs: MTTR (Mean Time to Repair), MTBF; aussagekräftige Berichte (Praxisbegriff „Wassermelonen-Effekt“) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: MTTR und MTBF Berechnung.** Ein zentraler Dateiserver (`fileserver01`) der Example Corp ist in einer Woche (168 Stunden) dreimal ausgefallen. Ausfalldauer: 2 Stunden, 1 Stunde, 3 Stunden. Verwenden Sie MTTR = Gesamtausfallzeit / Anzahl der Ausfälle und MTBF = Betriebszeit ohne Ausfall / Anzahl der Ausfälle. Berechnen Sie MTTR, MTBF und die Verfügbarkeit der Woche in Prozent und diskutieren Sie in einem kurzen Absatz, wie aussagekräftig diese KPIs für den Endnutzer sind.
2. **Titel: OLA Definition.** Formulieren Sie ein kurzes Operational Level Agreement (OLA) zwischen dem Service Desk (Tier 1) und der Netzwerk-Administration (Tier 2) bezüglich der Reaktionszeiten bei Netzwerkausfällen.
3. **Titel: Rollen und Verantwortung (RACI).** Erstellen Sie eine RACI-Tabelle für die Bearbeitung eines Incidents mit den Rollen Service-Desk-Mitarbeiter, Techniker der zweiten Ebene und Service Owner und den Tätigkeiten Ticket erfassen, priorisieren, diagnostizieren, Kunde informieren und schließen.

#### Kontrollfragen
1. Was ist der konzeptionelle Unterschied zwischen einem SLA und einem OLA?
2. Was sagt der sogenannte „Wassermelonen-Effekt“ bei SLAs aus?
3. In welchen Fällen zieht ein IT-Dienstleister einen Underpinning Contract (UC) heran?
4. Nennen Sie drei typische Rollen im Servicebetrieb und je eine Verantwortung.

### Modul 8: Continual Improvement (KVP) im System-Alltag
* **Priorität:** 2
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Continual Improvement Model von ITIL auf technische Infrastrukturen anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Verbesserungsplan (PDCA-Zyklus) für ein wiederkehrendes Sysadmin-Problem erstellen.
* **Voraussetzungen:** Module 1 bis 7.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Das Continual Improvement Model (Schritte 1 bis 7) | 2 |
| 8.2 | Der PDCA-Zyklus (Deming-Kreis) im Systembetrieb | 2 |
| 8.3 | Einbindung von Verbesserungen in den täglichen Betriebsablauf | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Titel: Verbesserungsplan (Continual Improvement Model).** Der Service Desk der Example Corp wird täglich mit über 50 Passwort-Reset-Tickets blockiert. Nutzen Sie das Continual Improvement Model ("What is the vision?", "Where are we now?", etc.), um einen strategischen Plan zu entwerfen, der dieses Ticketvolumen durch technische Maßnahmen (z. B. Self-Service-Portal) senkt.
2. **Titel: PDCA im Patch-Management.** Dokumentieren Sie einen PDCA-Zyklus (Plan, Do, Check, Act) zur Verbesserung des monatlichen Windows-Server-Patchdays, da dieser zuletzt zu Ausfällen geführt hat.

#### Kontrollfragen
1. Welchen Zweck erfüllt die Phase „Where are we now?“ im Continual Improvement Model?
2. Warum ist die letzte Frage des Modells („How do we keep the momentum going?“) entscheidend für den IT-Betrieb?
3. Wie können Systemadministratoren kleine Verbesserungen im Alltag festhalten (Stichwort: Continual Improvement Register)?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (48 UE), Prioritäten (6x P1, 2x P2) und die Zahl der Module blieben unverändert. Acht Module entsprechen der Vorgabe des Prompts („etwa 8 Module, 6 bis 10“, kleiner Kurs). Aufgaben kamen hinzu; ob die Stunden dafür reichen, ist unerprobt. Es gibt kein technisches Labor, die Aufgaben wurden nur gelesen und fachlich geprüft, nicht ausgeführt.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf | Out-of-Scope präzisiert (kein Labor, keine Zertifizierungsvorbereitung, ITIL 5 nicht Gegenstand) | Der Satz über „Netzwerk-Zertifizierungen“ war unklar |
| A.2 | Practice Guides, Versionsstand ITIL 5, Hilfsmittel (PDCA, 5-Why, MTTR, RACI, PESTLE) ergänzt; Herausgeber PeopleCert genannt | Der Prompt verlangt „Version und Stand nennen“; ITIL Version 5 wird laut Sekundärquelle 2026 schrittweise eingeführt; Praktiken hatten keine Quelle |
| A.3 | Netz und Systeme der Example Corp benannt; Vorlagen und Logauszug als Material des Kursleiters aufgeführt | Aufgaben nutzten „Vorlage“ und „erhalten Log-Einträge“, ohne dass das Material beschrieben oder bereitgestellt war; `erp01`, `fileserver01` kamen ohne Definition vor |
| Modul 1 | Aufgabe 3, Frage 3 präzisiert, Frage 4 | Lernziel „Relevanz für den Administratoralltag“ und „Service und Wert definieren“ hatten keine Aufgabe bzw. Frage; Frage 3 beschrieb „Risiko, das von einem Service entfernt wird“ ungenau |
| Modul 2 | Frage 4 | Lernziel „sieben Leitprinzipien aufzählen“ hatte keine Frage |
| Modul 3 | Einheit 3.1 (fünf SVS-Komponenten), Einheit 3.3 (PESTLE), Aufgabe 3 (SVS skizzieren) | Das Lernziel „SVS skizzieren“ hatte keine Aufgabe; Governance und Continual Improvement fehlten in Einheit 3.1; PESTLE kam nur in einer Frage vor |
| Modul 4 | Einheit 4.2, Aufgaben 1 und 2, Frage 1 | Bei einem IP-Adresskonflikt zeigen `ping` und `tracert` den Konflikt nicht; ersetzt durch `ipconfig /all`, `arp -a` bzw. `ip neigh` mit Troubleshooting-Schritten; der Statusverlauf des Lernziels „Lebenszyklus“ war nicht gefordert; „Dringlichkeit x Auswirkung“ suggerierte eine Multiplikation statt einer Matrix |
| Modul 5 | Einheit 5.3 (Change Authority), Aufgabe 2 (Annahmen), Frage 3 und 4 | CAB kam nur in einer Frage vor; die Einstufung der Festplatte im RAID hängt von Annahmen ab; Incident und Problem hatten keine eigene Frage |
| Modul 6 | Aufgabe 2 (Logauszug vom Kursleiter), Aufgabe 3 (Request oder Incident), Fragen 1 und 4 | Lernziele „Requests abgrenzen“ und „SPOC beschreiben“ hatten keine Aufgabe bzw. Frage; Frage 1 behauptete „dürfen nicht“, ITIL schreibt das nicht so vor |
| Modul 7 | Lernziel „typische Rollen“, Einheiten 7.1 und 7.2, Aufgabe 1 (MTBF und Verfügbarkeit mit Definition), Aufgabe 3 (RACI), Frage 4 | MTBF sollte berechnet werden, wurde aber nicht verlangt; Rollen standen im Titel und Lernziel, aber in keiner Einheit; „Wassermelonen-Effekt“ kam nur in einer Frage vor |
| Modul 8 | Frage 3: „Continual Improvement Register“ | „CSI Register“ ist ein Begriff aus der Vorgängerversion ITIL v3 (nicht bestätigt, bitte prüfen) |

**Kontrollwerte Modul 7, Aufgabe 1:** Gesamtausfallzeit 6 h, MTTR = 6 h / 3 = 2 h, Betriebszeit 162 h, MTBF = 162 h / 3 = 54 h, Verfügbarkeit = 162 / 168 ≈ 96,4 %.

**Bewertung des Prüfvermerks der ersten Fassung:** Punkt 1 ist korrekt. Punkt 2 ist teilweise erfüllt (Vorlagen und Logauszug als Material fehlten). Punkt 3 ist nicht erfüllt (Praktiken, PDCA, MTTR, PESTLE ohne Quelle; Versionsstand fehlte). Punkt 4 ist teilweise erfüllt (die Diagnosewerkzeuge passten nicht zum Szenario). Punkt 5 ist nicht erfüllt (Lernziele in Modul 1, 2, 3, 6 und 7 ohne Aufgabe oder Frage). Punkt 6 ist erfüllt, es gibt keinen Rückbau. Punkt 7 ist erfüllt. Punkt 8 ist teilweise erfüllt (Systemnamen undefiniert). Punkt 9 ist erfüllt. Die Begründung „Geprüft in M1-M8“ stand bei fast jedem Punkt, ohne dass die Fehler gefunden wurden.

**Hinweise und offene Punkte:**

* **Nicht bestätigt:** Alle ITIL-4-Begriffe (sieben Leitprinzipien, fünf SVS-Komponenten, sechs Aktivitäten der Service Value Chain, sieben Schritte des Continual Improvement Model, Change-Typen) stammen aus dem Wissensstand, nicht aus dem geprüften Buch. Ebenso der Begriff „Continual Improvement Register“ und die Namen der Practice Guides. Vor dem Kurs gegen das ITIL-4-Foundation-Buch prüfen.
* **ITIL Version 5:** Der Lehrplan bleibt bei ITIL 4. Falls der Kurs auf Version 5 umgestellt werden soll, sind Leitprinzipien, SVS und Praktiken neu zu prüfen.
* Die Rollen in Modul 7 sind typische Rollen im Betrieb. Ob ITIL 4 feste Rollen vorgibt, wurde nicht geprüft.