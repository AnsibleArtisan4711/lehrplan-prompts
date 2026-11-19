# Lehrplan: Notfallplanung und Disaster Recovery

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Backup-Grundlagen (Lehrplan P35 oder gleichwertig), Grundkenntnisse in Linux und Windows Server; Active-Directory-Grundlagen für Modul 8 |
| **Gesamtumfang** | 13 Module, 111 UE (zu 45 Minuten; 83,25 Stunden) |
| **Fokus-Technologien** | Business-Impact-Analyse, Risikoanalyse, Wiederanlauf-Reihenfolge, DR-Strategien und Standorte, Alarmierung und Kommunikation, Wiederherstellung (Linux praktisch, Windows/Active Directory nach Dokumentation), Notfallhandbuch, Notfallübung, Maßnahmenverfolgung, Vorgehen bei Cyberangriff, Gesamtprüfung eines DR-Plans |
| **Thematische Abgrenzung (Out of Scope)** | Keine Details zu Backup-Verfahren (siehe Lehrplan P35), keine juristische Beratung zu Melde- und Aufbewahrungspflichten, keine IT-Forensik, keine Produkt-Schulung (Veeam, Azure Site Recovery u. a.), keine Hochverfügbarkeits-Cluster |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Grundlagen: Notfallmanagement, Business Continuity und Disaster Recovery | 1 | 6 |
| 2 | Business-Impact-Analyse (BIA) | 1 | 9 |
| 3 | Risikoanalyse für den IT-Betrieb | 1 | 8 |
| 4 | Wiederanlauf-Reihenfolge und Abhängigkeiten | 1 | 9 |
| 5 | DR-Strategien und Standorte: kalt, warm, heiß, Cloud | 1 | 8 |
| 6 | Alarmierung, Rollen und Kommunikation | 1 | 8 |
| 7 | Wiederherstellung unter Linux mit Zeitmessung | 1 | 10 |
| 8 | Wiederherstellung unter Windows und Active Directory | 1 | 10 |
| 9 | Das Notfallhandbuch: Aufbau, Prüfung und Pflege | 1 | 9 |
| 10 | Notfallübung planen, durchführen und auswerten | 1 | 10 |
| 11 | Lessons Learned und Maßnahmenverfolgung | 2 | 6 |
| 12 | Szenario Cyberangriff: Reihenfolge der Schritte | 2 | 8 |
| 13 | Abschlussprojekt: DR-Plan prüfen und zusammenführen | 1 | 10 |
| **Gesamt** | 13 Module | 11 × Priorität 1, 2 × Priorität 2 | **111** |

**Priorität 1** (Pflicht) sind die Module 1 bis 10 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) sind Modul 11 (Maßnahmenverfolgung) und Modul 12 (Cyberangriff-Szenario). Fallen beide weg, verringert sich der Gesamtumfang auf 97 UE.

### 2. Quellen

Geprüft (auf Microsoft Learn am 19.11.2026 gelesen): Befehlsreferenz `wbadmin` mit den Unterbefehlen `start recovery`, `start systemstaterecovery` (Option `-authsysvol`), `start sysrecovery` (nur in der Windows-Wiederherstellungsumgebung; Option `-recreateDisks` zerstört Daten). Die Linux-Befehle (`restic`, `bc`, Python 3 mit `graphlib`) wurden im Labor ausgeführt (restic 0.16.4, Python 3.13), nicht gegen Handbücher gelesen. Für Normen und Standards zum Notfallmanagement (z. B. ISO 22301, BSI-Standard 200-4) gibt es **keine geprüfte Quelle**: Sie wurden nicht gelesen, und alle Aussagen dazu sind Fachwissen und mit „nicht bestätigt“ gekennzeichnet. Meldepflichten und Fristen (Datenschutz, NIS2) sind nicht Teil dieser Übung.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V (Windows Server oder Windows 11 Pro); die Module 2 bis 7, 9 bis 13 benötigen nur eine Linux-Maschine mit Python 3.

**VMs:** `srv-lin01` (Debian 12, 2 GB RAM; Python 3, restic, bc), `srv-win01` (Windows Server mit Active-Directory-Domänendienste, 4 GB RAM, nur für Modul 8) und optional `srv-lin02` als Ziel für Restore-Übungen.

**Netz:** privater Switch `Lab-Internal-Net`, Adressbereich `192.168.10.0/24` (statisch, ohne DHCP und DNS), Domäne bzw. Zone `labor.example.internal`; alle Kontakte, Telefonnummern (`+43 000 …`) und Firmen sind frei erfunden.

**Internetphase:** Vor Kursbeginn einmalig: `restic`, `bc`, `python3` auf `srv-lin01` installieren; auf `srv-win01` die Windows-Features für Domänendienste und (nach Bedarf) Windows Server Backup. Danach Internet trennen. Der genaue Name des Windows-Features für Windows Server Backup ist nicht bestätigt.

**Zugangsdaten:** Laborkennwörter vergibt der Lernende selbst. **Ausgangszustand je Modul:** Hyper-V-Prüfpunkt; **Rückbau:** Prüfpunkt wiederherstellen und Arbeitsordner `~/dr/mNN` löschen.

**Hinweis zur Testumgebung der Ausarbeitung:** Das Labor wurde nicht in Hyper-V aufgebaut; die Skripte wurden in einem Cloud-Container ausgeführt; Windows und Active Directory wurden nicht ausgeführt.

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen: Notfallmanagement, Business Continuity und Disaster Recovery

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Notfall, Krise, Business Continuity und Disaster Recovery abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Phasen des Notfallmanagements nennen und in der richtigen Reihenfolge anordnen.
  * Nach Abschluss dieses Moduls kann der Lernende in einer Fallstudie Versäumnisse benennen.
* **Voraussetzungen:** Grundlagen von Backup, RPO und RTO.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Begriffe: Notfall, Krise, Business Continuity, Disaster Recovery, Wiederanlauf, Ausfallzeit | 2 |
| 1.2 | Ablauf eines Notfallmanagements: analysieren, planen, umsetzen, üben, verbessern (PDCA-Gedanke) | 2 |
| 1.3 | Fallstudie: Ausfall des Serverraums und typische Versäumnisse | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe abgrenzen (Einheit 1.1):** Erklären Sie in je einem Satz Notfall, Krise, Business Continuity und Disaster Recovery und nennen Sie ein Beispiel aus der IT.
2. **Phasen ordnen (Einheit 1.2):** Ordnen Sie die Schritte „üben“, „Gefährdung analysieren“, „Maßnahmen planen“, „verbessern“, „umsetzen“ in eine sinnvolle Reihenfolge und begründen Sie, warum der Ablauf ein Kreislauf ist.
3. **Fallstudie (Einheit 1.3):** Lesen Sie die Fallstudie in den Hinweisen. Nennen Sie vier Versäumnisse und je eine Maßnahme, die später in diesem Kurs behandelt wird.

#### Kontrollfragen

1. Wodurch unterscheidet sich Disaster Recovery von Business Continuity?
2. Warum gehört das Üben zum Notfallmanagement?
3. Was ist der Unterschied zwischen Notfall und Krise?
4. Welche Rolle spielt die Geschäftsführung im Notfallmanagement?

### Modul 2: Business-Impact-Analyse (BIA)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende aus Prozessen die Größen MTPD, RTO und RPO ableiten und deren Beziehung erklären.
  * Nach Abschluss dieses Moduls kann der Lernende mit `bia.py` Prozesse nach Dringlichkeit ordnen und Unstimmigkeiten finden.
  * Nach Abschluss dieses Moduls kann der Lernende Zielwerte begründen.
* **Voraussetzungen:** Modul 1; Python 3 auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Ziel der BIA, Prozesse und ihre IT-Systeme, Größen MTPD, RTO, RPO | 3 |
| 2.2 | Schaden bis zum RTO und Prioritätsklassen A bis D | 2 |
| 2.3 | Praxis: `bia.py` mit Beispielprozessen, Plausibilitätsprüfung | 3 |
| 2.4 | Typische Fehler: zu eng gesetzte Ziele, fehlende Abstimmung mit den Fachbereichen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Skript ausführen (Einheit 2.3):** Führen Sie `python3 bia.py prozesse.csv` aus. Nennen Sie die Reihenfolge der Systeme, die Klassen und den Prozess mit dem höchsten Schaden bis zum RTO.
2. **Hinweis deuten (Einheit 2.4):** Das Skript meldet einen Hinweis zur Lohnabrechnung. Erklären Sie, was „kritisch ab 72 h“ bei RTO 48 h bedeutet, und schlagen Sie eine Änderung vor.
3. **Fehler provozieren (Einheit 2.3):** Setzen Sie bei einem Prozess den RTO größer als den MTPD und beschreiben Sie die Reaktion des Skripts (Warnung und Rückgabewert).
4. **Eigene Prozesse (Einheit 2.1):** Ergänzen Sie drei eigene Prozesse für die fiktive Firma mit begründeten Werten.

#### Kontrollfragen

1. Warum muss der RTO kleiner sein als die MTPD?
2. Wie berechnet das Skript den „Schaden bis RTO“, und welche Folgekosten fehlen darin?
3. Wer legt die Zielwerte fest, die IT oder die Fachbereiche?
4. Warum können zwei Prozesse dasselbe System betreffen und unterschiedliche RTO haben?

### Modul 3: Risikoanalyse für den IT-Betrieb

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Szenarien mit Wahrscheinlichkeit und Schaden bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende Brutto- und Nettorisiko vergleichen und die Wirkung von Maßnahmen beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen einer Produkt-Bewertung erklären.
* **Voraussetzungen:** Module 1 und 2; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Gefährdungen und Szenarien; Eintrittswahrscheinlichkeit und Schadenshöhe | 2 |
| 3.2 | Risiko = Wahrscheinlichkeit x Schaden; Matrix, Brutto- und Nettorisiko | 2 |
| 3.3 | Praxis: `risiko.py` mit Risikotabelle | 3 |
| 3.4 | Grenzen des Produkts und seltene Großschäden | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Skript ausführen (Einheit 3.3):** Führen Sie `python3 risiko.py risiken.csv` aus. Welches Risiko ist brutto am höchsten und wie ändert sich die Einstufung durch die Maßnahme?
2. **Matrix lesen (Einheit 3.3):** Lesen Sie die Netto-Matrix. Welche Szenarien liegen im Bereich „Schaden 4 oder 5“?
3. **Grenzen (Einheit 3.4):** Das Szenario „Brand im Serverraum“ wird brutto als „niedrig“ eingestuft. Begründen Sie, warum das trotzdem nicht ausreicht, und nennen Sie eine zusätzliche Bewertungsregel.
4. **Neues Szenario (Einheit 3.1):** Ergänzen Sie ein Szenario mit Maßnahme und bewerten Sie vorher und nachher.

#### Kontrollfragen

1. Warum ist das Produkt aus Wahrscheinlichkeit und Schaden allein nicht ausreichend?
2. Was bedeutet Nettorisiko?
3. Wann ist eine Maßnahme als „fraglich“ markiert?
4. Welche Rolle spielt die Risikobereitschaft der Geschäftsführung?

### Modul 4: Wiederanlauf-Reihenfolge und Abhängigkeiten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende aus einer Abhängigkeitsliste die Wiederanlauf-Reihenfolge in Stufen ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende die Gesamtdauer bei einem und mehreren Helfern bestimmen und mit dem RTO vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen gegen verfehlte RTO benennen.
* **Voraussetzungen:** Module 2 und 3; Python 3.9 oder neuer.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Abhängigkeiten zwischen Systemen und Diensten (Netz, Speicher, Verzeichnisdienst, Datenbank, Anwendung) | 2 |
| 4.2 | Topologische Sortierung: Stufen, parallele Arbeit, kritischer Pfad | 2 |
| 4.3 | Praxis: `wiederanlauf.py` mit einem und zwei Helfern | 3 |
| 4.4 | RTO-Verletzungen und Maßnahmen (Parallelisieren, Vorbereiten) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Reihenfolge ablesen (Einheit 4.3):** Führen Sie `python3 wiederanlauf.py abhaengigkeiten.csv 1` aus und beschreiben Sie die fünf Stufen.
2. **Zwei Helfer (Einheit 4.3):** Wiederholen Sie mit 2 Helfern und vergleichen Sie Gesamtdauer und Zahl der verfehlten RTO.
3. **Maßnahme planen (Einheit 4.4):** Das System „Speicher“ verfehlt den RTO. Nennen Sie zwei Maßnahmen und ändern Sie die CSV entsprechend; wiederholen Sie den Lauf.
4. **Zyklus (Einheit 4.1):** Tragen Sie eine Abhängigkeit ein, die einen Kreis bildet, und beschreiben Sie die Reaktion des Skripts.

#### Kontrollfragen

1. Warum kann man Netzwerk und Speicher nicht gleichzeitig mit DC01 starten?
2. Wie wirkt sich ein zweiter Helfer auf die Dauer aus, und was begrenzt die Zeitersparnis?
3. Was ist ein Zyklus in den Abhängigkeiten, und wie löst man ihn praktisch?
4. Warum verfehlt WEB01 den RTO, obwohl seine eigene Wiederherstellung nur 40 Minuten dauert?

### Modul 5: DR-Strategien und Standorte: kalt, warm, heiß, Cloud

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Varianten nach Wiederanlaufzeit, Datenverlust, Kosten und Betriebsaufwand vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende die günstigste Variante bestimmen, die die Ziele erfüllt.
  * Nach Abschluss dieses Moduls kann der Lernende die Ergebnisse als Entscheidungsvorlage formulieren.
* **Voraussetzungen:** Module 2 und 4; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Varianten: kalter, warmer, heißer Standort und Wiederherstellung in der Cloud; Kosten und Aufwand | 3 |
| 5.2 | Auswahl nach RTO, RPO und Budget; Schaden je Ereignis gegen laufende Kosten | 3 |
| 5.3 | Praxis: `standortvergleich.py` mit Vorgaben | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auswahl (Einheit 5.3):** Führen Sie `python3 standortvergleich.py standorte.csv 8 4 2500` aus. Welche Varianten erfüllen RTO 8 h und RPO 4 h?
2. **Ziele ändern (Einheit 5.2):** Setzen Sie RTO 1 h und RPO 1 h und führen Sie erneut aus. Welche Variante bleibt?
3. **Wirtschaftlichkeit (Einheit 5.2):** Vergleichen Sie Kosten pro Jahr und erwarteten Schaden pro Ereignis; ab wie vielen Ereignissen in zehn Jahren lohnt sich die teurere Variante?
4. **Vorlage (Einheit 5.2):** Formulieren Sie in fünf Sätzen eine Entscheidungsvorlage für die Geschäftsführung.

#### Kontrollfragen

1. Warum erfüllt die Variante „Warm“ in den Beispieldaten das RPO nicht?
2. Welche Kosten fehlen im Vergleich (Lizenzen, Personal, Tests)?
3. Welche Risiken bringt die Cloud-Wiederherstellung (Bandbreite, Zugangsdaten, Verfügbarkeit)?
4. Warum ist die „heiße“ Variante nicht automatisch die beste?

### Modul 6: Alarmierung, Rollen und Kommunikation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Alarmkette mit Vertretungen entwerfen und auf Lücken prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Kommunikationswege nennen, die ohne die eigene IT funktionieren.
  * Nach Abschluss dieses Moduls kann der Lernende Rollen und Entscheidungsbefugnisse im Notfall festlegen.
* **Voraussetzungen:** Module 1 und 4; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Alarmkette, Rollen (Bereitschaft, Leitung, Krisenstab, Kommunikation), Vertretungen | 3 |
| 6.2 | Kommunikationswege bei Ausfall der IT (Telefon, Papier, getrennter Kanal) | 2 |
| 6.3 | Praxis: `alarmkette.py` mit Nichterreichbarkeit | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kette lesen (Einheit 6.3):** Führen Sie `python3 alarmkette.py kontakte.csv` aus und notieren Sie Dauer und Reihenfolge.
2. **Lücken finden (Einheit 6.3):** Führen Sie `python3 alarmkette.py kontakte.csv "Clara Muster,Daniel Probe,Gerda Muster"` aus. Welche Stufen bleiben ohne Ergebnis, und welche Folge hat das?
3. **Kette verbessern (Einheit 6.1):** Ergänzen Sie Vertretungen und prüfen Sie erneut.
4. **Kommunikation ohne IT (Einheit 6.2):** Legen Sie fest, wie Mitarbeiter und Kunden informiert werden, wenn E-Mail und Telefonanlage ausgefallen sind.

#### Kontrollfragen

1. Warum braucht jede Rolle eine Vertretung?
2. Warum darf die Kontaktliste nicht nur im Intranet liegen?
3. Was ist die Aufgabe des Krisenstabs im Unterschied zur IT-Bereitschaft?
4. Wann ist ein Zeitaufwand von 5 Minuten je Versuch in der Simulation zu knapp?

### Modul 7: Wiederherstellung unter Linux mit Zeitmessung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Wiederherstellung mit restic durchführen und die Dauer messen.
  * Nach Abschluss dieses Moduls kann der Lernende die Dauer auf eine größere Datenmenge hochrechnen und die Unsicherheit benennen.
  * Nach Abschluss dieses Moduls kann der Lernende das Ergebnis mit dem RTO vergleichen.
* **Voraussetzungen:** Backup-Grundlagen und restic (P35 Modul 7); `bc` auf `srv-lin01`.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Ablauf einer Wiederherstellung: Entscheidung, Ersatz bereitstellen, Daten zurückspielen, prüfen | 3 |
| 7.2 | Zeit messen und auf reale Datenmengen hochrechnen; Grenzen linearer Hochrechnung | 3 |
| 7.3 | Praxis: `restore_zeit.sh` mit restic | 3 |
| 7.4 | Vergleich mit dem RTO und Ableitung von Maßnahmen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Messlauf (Einheit 7.2):** Führen Sie `bash restore_zeit.sh ./lab 5` aus. Notieren Sie Dauer, Durchsatz und die Hochrechnung auf 500 GB.
2. **Wiederholen (Einheit 7.2):** Wiederholen Sie den Lauf dreimal und notieren Sie die Streuung der Zeit.
3. **Hochrechnung bewerten (Einheit 7.2):** Nennen Sie drei Gründe, warum die lineare Hochrechnung von 40 MB auf 500 GB unzuverlässig ist, und planen Sie einen realistischeren Test.
4. **Ziel vergleichen (Einheit 7.4):** Vergleichen Sie die Hochrechnung mit dem RTO für FS01 (12 Stunden) aus Modul 4.

#### Kontrollfragen

1. Warum ist die gemessene Zeit im Labor nur eine untere Schranke?
2. Welche Schritte gehören zur Wiederherstellung außer dem Kopieren?
3. Warum soll man die Wiederherstellung auf eine frische Maschine üben?
4. Wann wäre eine Wiederherstellung per Image-Verfahren schneller als dateibasiert?

### Modul 8: Wiederherstellung unter Windows und Active Directory

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die wbadmin-Wiederherstellungsbefehle ihrem Zweck zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Besonderheiten der Wiederherstellung eines Domänencontrollers beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken (Datenverlust durch `-recreateDisks`, Replikationsfolgen) benennen.
* **Voraussetzungen:** P35 Modul 6; Active-Directory-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Wiederherstellungswege mit `wbadmin`: Dateien und Volumes (`start recovery`), Systemstatus (`start systemstaterecovery`), Systemabbild (`start sysrecovery`) | 4 |
| 8.2 | Active Directory: Systemstatus-Sicherung, nicht-autoritative und autoritative Wiederherstellung, Option `-authsysvol` (nach Dokumentation) | 4 |
| 8.3 | Planung: Reihenfolge, Voraussetzungen und Risiken (Daten überschreiben) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Befehle zuordnen (Einheit 8.1):** Ordnen Sie `wbadmin start recovery`, `start systemstaterecovery` und `start sysrecovery` je einem Szenario zu (einzelne Dateien, Systemstatus eines Servers, kompletter Server auf neuer Hardware).
2. **Risiko erkennen (Einheit 8.1):** Beschreiben Sie, was die Option `-recreateDisks` bewirkt, und warum man sie nur nach Bestätigung des Ziels einsetzt.
3. **DC-Wiederherstellung planen (Einheit 8.2):** Schreiben Sie eine Ablaufliste für den Ausfall eines von zwei Domänencontrollern (nicht-autoritativ) und für das Löschen einer OU (autoritativ); begründen Sie, wann welche nötig ist.
4. **Prüfliste (Einheit 8.3):** Erstellen Sie eine Prüfliste vor einer Wiederherstellung (Zielvolume, Sicherungsversion, Netzwerk, Berechtigungen).

#### Kontrollfragen

1. Wozu dient der Systemstatus eines Domänencontrollers?
2. Wann ist eine autoritative Wiederherstellung erforderlich?
3. Warum gilt `start sysrecovery` nur in der Windows-Wiederherstellungsumgebung?
4. Welche Folgen hat eine unbeabsichtigte Wiederherstellung eines veralteten Domänencontrollers?

### Modul 9: Das Notfallhandbuch: Aufbau, Prüfung und Pflege

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Notfallhandbuch aufbauen und mit einer Prüfliste auf Lücken testen.
  * Nach Abschluss dieses Moduls kann der Lernende Schritte mit Prüfkriterien formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Pflege (Stand, Verantwortliche, Ablage) regeln.
* **Voraussetzungen:** Module 4 bis 8; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Pflichtabschnitte, Verständlichkeit unter Stress, Schritte mit Prüfkriterium | 3 |
| 9.2 | Verfügbarkeit des Handbuchs im Notfall (Offline-Kopie, Papier, getrennte Ablage) | 2 |
| 9.3 | Praxis: `handbuch_pruefen.py` auf ein lückenhaftes Beispiel anwenden und verbessern | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prüfung ausführen (Einheit 9.3):** Führen Sie `python3 handbuch_pruefen.py handbuch.md 2026-11-19` aus und listen Sie die sieben Befunde.
2. **Handbuch verbessern (Einheit 9.3):** Ergänzen Sie `handbuch.md` so, dass die Prüfung weniger Befunde meldet (Abschnitte, Telefonnummern als Beispielwerte, Prüfkriterien); führen Sie erneut aus.
3. **Verfügbarkeit (Einheit 9.2):** Legen Sie fest, wo Kopien des Handbuchs liegen (mindestens drei Orte) und wer sie aktuell hält.
4. **Schritte formulieren (Einheit 9.1):** Formulieren Sie die zwei Schritte „Neue VM aus Vorlage erstellen“ und „Daten mit restic zurückspielen“ mit Prüfkriterium neu.

#### Kontrollfragen

1. Warum ist „siehe Aushang“ im Handbuch ein Befund?
2. Was ist ein Prüfkriterium und warum gehört es zu jedem Schritt?
3. Wer ist für die Pflege verantwortlich, und wann wird sie ausgelöst?
4. Warum soll ein Notfallhandbuch kurze Schritte statt Fließtext enthalten?

### Modul 10: Notfallübung planen, durchführen und auswerten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Notfallübung mit Zielen und Regeln planen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Übungsprotokoll mit Soll und Ist auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende aus den Abweichungen Maßnahmen ableiten.
* **Voraussetzungen:** Module 6 und 9; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Übungsarten: Planbesprechung (Tabletop), Funktionstest, Vollübung; Ziele, Regeln, Abbruchkriterien | 3 |
| 10.2 | Protokoll: Soll- und Istzeiten, Abweichungen, Bemerkungen | 3 |
| 10.3 | Praxis: `uebung_protokoll.py` auswerten | 3 |
| 10.4 | Ableitung von Maßnahmen | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Übung planen (Einheit 10.1):** Planen Sie eine Tabletop-Übung für den Ausfall des Serverraums: Ziel, Teilnehmer, Ablauf, Regeln, Abbruchkriterien.
2. **Protokoll auswerten (Einheit 10.3):** Führen Sie `python3 uebung_protokoll.py uebung.csv` aus. Welche Schritte sind auffällig und warum?
3. **Toleranz ändern (Einheit 10.3):** Setzen Sie die Toleranz auf 100 Prozent und erklären Sie, was sich ändert und warum das kein Fortschritt wäre.
4. **Maßnahmen (Einheit 10.4):** Formulieren Sie zu jedem auffälligen Schritt eine konkrete Maßnahme mit Verantwortlichem.

#### Kontrollfragen

1. Wozu dient eine Tabletop-Übung, wenn nichts technisch ausgeführt wird?
2. Warum ist ein nicht durchgeführter Schritt ein Befund?
3. Was sind sinnvolle Abbruchkriterien einer Vollübung?
4. Wie sorgt man dafür, dass die Übung kein Risiko für den Betrieb wird?

### Modul 11: Lessons Learned und Maßnahmenverfolgung

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Nachbesprechung strukturiert durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen verfolgbar formulieren.
  * Nach Abschluss dieses Moduls kann der Lernende überfällige Maßnahmen erkennen und eskalieren.
* **Voraussetzungen:** Modul 10; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Nachbesprechung (Lessons Learned): Ablauf, Fragen, Dokumentation | 2 |
| 11.2 | Maßnahmen mit Verantwortlichem, Termin, Priorität; Status und Überfälligkeit | 2 |
| 11.3 | Praxis: `massnahmen.py` auf eine Maßnahmenliste anwenden | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Liste auswerten (Einheit 11.3):** Führen Sie `python3 massnahmen.py massnahmen.csv 2026-11-19` aus. Welche Maßnahme ist überfällig?
2. **Termin ändern (Einheit 11.3):** Ändern Sie Stichtag auf `2027-01-05` und beschreiben Sie die Änderungen.
3. **Formulieren (Einheit 11.2):** Formulieren Sie drei Maßnahmen aus Modul 10 so, dass sie messbar sind (Ergebnis, Verantwortlicher, Termin).
4. **Eskalation (Einheit 11.2):** Legen Sie fest, ab wann und an wen eine überfällige Maßnahme eskaliert wird.

#### Kontrollfragen

1. Warum braucht jede Maßnahme einen Verantwortlichen und einen Termin?
2. Was unterscheidet „Wir sollten“ von einer messbaren Maßnahme?
3. Warum ist Rückgabewert 1 bei überfälligen Punkten nützlich?
4. Wie vermeidet man, dass Maßnahmen im Alltag versanden?

### Modul 12: Szenario Cyberangriff: Reihenfolge der Schritte

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Reihenfolge der Schritte bei einem Angriff aus dem Lagebild ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum eine einfache Wiederherstellung bei aktivem Angriff gefährlich ist.
  * Nach Abschluss dieses Moduls kann der Lernende ein einfaches Playbook formulieren.
* **Voraussetzungen:** Module 4, 6 und 8; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Besonderheiten bei Angriff: Eindämmen, Beweise, saubere Wiederherstellung, Kommunikation | 3 |
| 12.2 | Entscheidungshilfe `szenario_entscheid.py` (Lage Angriff, Backup, Active Directory) | 3 |
| 12.3 | Planungsaufgabe: Playbook für Ransomware im Lab | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Lagebild eingeben (Einheit 12.2):** Führen Sie das Skript mit `aktiv backup_unklar ad_betroffen` und mit `abgeschlossen backup_sauber ad_ok` aus; vergleichen Sie die Schritte.
2. **Dritte Lage (Einheit 12.2):** Testen Sie `aktiv backup_verschluesselt ad_betroffen` und beschreiben Sie, was sich ändert.
3. **Playbook (Einheit 12.3):** Schreiben Sie ein Playbook (eine Seite) für den Fall „Ransomware auf der Dateiablage im Lab“.
4. **Beurteilung (Einheit 12.1):** Beurteilen Sie, wo die Entscheidungshilfe zu einfach ist.

#### Kontrollfragen

1. Warum soll bei aktivem Angriff nicht sofort wiederhergestellt werden?
2. Wozu dient die Beweissicherung vor der Wiederherstellung?
3. Warum behandelt man ein betroffenes Active Directory als kompromittiert?
4. Wer entscheidet über Meldungen an Behörden?

### Modul 13: Abschlussprojekt: DR-Plan prüfen und zusammenführen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Ergebnisse der Module zu einem DR-Plan zusammenführen.
  * Nach Abschluss dieses Moduls kann der Lernende Widersprüche zwischen BIA, Abhängigkeiten, Kontakten und Maßnahmen finden.
  * Nach Abschluss dieses Moduls kann der Lernende einen DR-Plan der Geschäftsführung vorstellen.
* **Voraussetzungen:** Module 2 bis 10; Python 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Zusammenführung der Bausteine (BIA, Risiko, Wiederanlauf, Standort, Alarmierung, Handbuch, Übung, Maßnahmen) | 3 |
| 13.2 | Konsistenzprüfung mit `dr_gesamtcheck.py`: Widersprüche zwischen den Dateien finden | 3 |
| 13.3 | Abschlussprojekt: DR-Plan für die fiktive Firma „Alpenwerk Beispiel“ | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Gesamtprüfung (Einheit 13.2):** Führen Sie `python3 dr_gesamtcheck.py 2026-11-19` aus und nennen Sie die vier Befunde mit der Datei, in der sie zu beheben sind.
2. **Befunde beheben (Einheit 13.2):** Beheben Sie die Befunde (Systemnamen vereinheitlichen, Vertretungen ergänzen, überfällige Maßnahme klären) und führen Sie die Prüfung erneut aus.
3. **DR-Plan schreiben (Einheit 13.3):** Schreiben Sie einen DR-Plan auf zwei bis drei Seiten mit Zielen, Reihenfolge, Standort, Alarmierung, Wiederherstellung, Übungsplan.
4. **Präsentation (Einheit 13.3):** Fassen Sie den Plan in fünf Sätzen für die Geschäftsführung zusammen.

#### Kontrollfragen

1. Warum entstehen Widersprüche zwischen den Dateien, wenn mehrere Personen sie pflegen?
2. Welche Prüfung ersetzt die manuelle Durchsicht, welche nicht?
3. Wie häufig sollte der Plan geprüft werden?
4. Was gehört in die Zusammenfassung für die Geschäftsführung?
