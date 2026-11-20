# Lehrplan: Failover-Clustering und Hochverfügbarkeit

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Windows-Server-Grundlagen und Active-Directory-Grundlagen; Hyper-V-Grundlagen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Windows Server (Failover Clustering), Hyper-V; Verfügbarkeit und Ausfallkonzepte; Clusteraufbau; Quorum und Zeugen; gemeinsamer Speicher und Cluster Shared Volumes; hochverfügbare VMs und Live-Migration; Hyper-V Replica; Cluster-aware Updating; Überwachung; Fehlersuche; Ausfalltests |
| **Thematische Abgrenzung (Out of Scope)** | Hyper-V Administration ist ein eigener Kurs; Backup und Notfallplanung sind eigene Kurse (Hochverfügbarkeit ersetzt keine Datensicherung). Nicht behandelt: Speicherplätze Direkt (Storage Spaces Direct), Stretch-Cluster, SQL-Always-On, Azure-Stack-HCI |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Hochverfügbarkeit und Ausfallkonzepte | 1 | 12 |
| 2 | Failover-Cluster aufbauen | 1 | 14 |
| 3 | Quorum und Zeugen | 1 | 14 |
| 4 | Gemeinsamer Speicher und Cluster Shared Volumes | 1 | 12 |
| 5 | Hochverfügbare VMs und Live-Migration | 1 | 14 |
| 6 | Hyper-V Replica | 2 | 10 |
| 7 | Cluster-aware Updating und Überwachung | 1 | 12 |
| 8 | Fehlersuche und Ausfalltests | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 5, 7 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 6 (Hyper-V Replica). Fällt Modul 6 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 6 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Windows Server, Failover Clustering und Hyper-V wurde **nicht** gelesen. Alle fachlichen Aussagen und alle PowerShell-Beispiele stammen aus Fachwissen und sind **nicht bestätigt**; verbindlich ist die Dokumentation der eingesetzten Windows-Server-Version (Versions-, Lizenz- und Supportstände mit Stand prüfen).

**Ausgeführt wurden ausschließlich die Python-Modelle** (Python 3 im Cloud-Container): reine Rechnungen mit erfundenen Werten. **Nicht ausgeführt:** Windows Server, Failover-Cluster, Hyper-V, PowerShell. Die Modelle bilden die Technik **vereinfacht** nach (z. B. einfaches Mehrheitsquorum ohne dynamisches Quorum, RAM als einziger Engpass). Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V (physisch oder geschachtelt). **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Cluster`, `10.60.0.0/24`).

**VMs bzw. Hosts:** zwei Hyper-V-Hosts `hv01` (`10.60.0.11`) und `hv02` (`10.60.0.12`) mit Windows Server (Failover-Clustering-Feature, Hyper-V-Rolle); `dc01` (`10.60.0.5`): Domänencontroller; `san01` (`10.60.0.20`): Speicher-VM oder iSCSI-Ziel für gemeinsamen Speicher. **Hardware- und RAM-Bedarf:** bei geschachtelter Virtualisierung braucht der physische Host genug RAM für zwei Hyper-V-Hosts samt ihrer VMs (Richtwert in der Dokumentation prüfen; nicht bestätigt).

**Prüfpunkt (Checkpoint):** Vor Modul 3 und vor Modul 5 von allen VMs je einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Python-Modelle laufen auf jedem Rechner mit Python 3, auch ohne Labor. Die PowerShell-Textdateien sind für die Hosts gedacht und wurden **nicht** ausgeführt.

## B. Detaillierter Modulaufbau

### Modul 1: Hochverfügbarkeit und Ausfallkonzepte

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Verfügbarkeit in Prozent in erlaubte Ausfallzeit umrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Reihen- und Parallelschaltung berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Hochverfügbarkeit von Backup abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende einzelne Ausfallstellen (Single Points of Failure) finden.
* **Voraussetzungen:** Hyper-V-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Verfügbarkeit berechnen | 3 |
| 1.2 | Reihen- und Parallelschaltung | 3 |
| 1.3 | Single Points of Failure | 3 |
| 1.4 | Abgrenzung zu Backup | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verfügbarkeit berechnen (Einheit 1.1):** Führen Sie `python3 verfuegbarkeit.py` aus. Erklären Sie die Tabelle der erlaubten Ausfallzeiten.
2. **Reihen- und Parallelschaltung (Einheit 1.2):** Erklären Sie, warum die Parallelschaltung die Verfügbarkeit erhöht und die Reihenschaltung senkt, und was der einzelne Switch in der Kette bewirkt.
3. **Single Points of Failure (Einheit 1.3):** Listen Sie für eine Umgebung mit zwei Hosts, einem Speicher und einem Switch die Einzelausfallstellen auf.
4. **Abgrenzung zu Backup (Einheit 1.4):** Erklären Sie in fünf Sätzen, warum ein Cluster ein Backup nicht ersetzt.

#### Kontrollfragen

1. Wie viele Minuten Ausfall pro Jahr erlaubt 99,9 %?
2. Wie berechnet man die Verfügbarkeit zweier paralleler Teile?
3. Was ist ein Single Point of Failure?
4. Warum ersetzt ein Cluster kein Backup?

### Modul 2: Failover-Cluster aufbauen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzungen für einen Failovercluster nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Bestandsliste gegen Voraussetzungen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Schritte zum Anlegen eines Clusters beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende das Labor aufbauen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Voraussetzungen prüfen | 5 |
| 2.2 | Schritte lesen | 3 |
| 2.3 | Netzwerke planen | 3 |
| 2.4 | Labor aufbauen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Voraussetzungen prüfen (Einheit 2.1):** Führen Sie `python3 voraussetzungen.py` aus. Erklären Sie jede Meldung für `hv03` und was Sie ändern müssten.
2. **Schritte lesen (Einheit 2.2):** Lesen Sie `beispiel_powershell.txt` und erklären Sie `Install-WindowsFeature`, `Test-Cluster` und `New-Cluster`. Kennzeichnen Sie, was Sie nicht geprüft haben.
3. **Netzwerke planen (Einheit 2.3):** Planen Sie die Netzwerke der Knoten (Verwaltung, Cluster, Speicher) mit Adressen aus `10.60.0.0/24` und begründen Sie die Trennung.
4. **Labor aufbauen (Einheit 2.4):** Bauen Sie `hv01`, `hv02`, `dc01` und `san01` am Switch `Lab-Cluster` auf und führen Sie `Test-Cluster` aus; tragen Sie das Ergebnis ein.

#### Kontrollfragen

1. Warum müssen die Knoten in derselben Domäne sein (Fachwissen)?
2. Wozu dient `Test-Cluster`?
3. Warum werden mehrere Netzwerkkarten empfohlen?
4. Welche Meldungen erhält `hv03` im Modell?

### Modul 3: Quorum und Zeugen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Quorum nach Mehrheit der Stimmen berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle eines Zeugen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende für 2, 3, 4 und 5 Knoten die überstehbaren Ausfälle bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen des Modells nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Quorum berechnen | 5 |
| 3.2 | Zeugen einsetzen | 3 |
| 3.3 | Gerade und ungerade Knotenzahl | 3 |
| 3.4 | Zeugenart wählen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Quorum berechnen (Einheit 3.1):** Führen Sie `python3 quorum.py` aus. Erklären Sie die Spalten Stimmen, Mehrheit und die Ausfallfälle.
2. **Zeugen einsetzen (Einheit 3.2):** Erklären Sie, warum ein Zwei-Knoten-Cluster mit Zeuge einen Knotenausfall übersteht, ohne Zeuge nicht.
3. **Gerade und ungerade Knotenzahl (Einheit 3.3):** Vergleichen Sie 4 Knoten ohne Zeuge mit 4 Knoten mit Zeuge und 5 Knoten.
4. **Zeugenart wählen (Einheit 3.4):** Lesen Sie `beispiel_powershell.txt` und entscheiden Sie für ein Zwei-Knoten-Labor und eine Zweigstelle, welche Zeugenart passt; nennen Sie, was Sie noch prüfen müssten.

#### Kontrollfragen

1. Wann hat ein Cluster Quorum (Modell)?
2. Wie viele Knotenausfälle übersteht ein Zwei-Knoten-Cluster mit Zeuge?
3. Warum bringt bei 4 Knoten ein Zeuge Vorteile?
4. Was bildet das Modell nicht nach?

### Modul 4: Gemeinsamer Speicher und Cluster Shared Volumes

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck gemeinsamen Speichers im Cluster erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Cluster Shared Volume (CSV) einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende den Platzbedarf mit Reserve planen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle des Koordinators beschreiben.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Platz planen | 4 |
| 4.2 | Koordinator | 4 |
| 4.3 | Befehle lesen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Platz planen (Einheit 4.1):** Führen Sie `python3 csv_modell.py` aus. Erklären Sie die Platzrechnung mit 20 % Reserve.
2. **Koordinator (Einheit 4.2):** Erklären Sie, was beim Ausfall von `hv01` mit dem Koordinator geschieht und was gleich bleibt.
3. **Befehle lesen (Einheit 4.3):** Lesen Sie `beispiel_powershell.txt` und erklären Sie, wie ein Datenträger zum CSV wird. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Wozu dient ein CSV?
2. Warum eine Reserve einplanen?
3. Was ändert sich beim Ausfall des Koordinators?

### Modul 5: Hochverfügbare VMs und Live-Migration

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine VM als Clusterrolle hochverfügbar machen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf bei Knotenausfall erklären.
  * Nach Abschluss dieses Moduls kann der Lernende N+1-Kapazität berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Live-Migration und Neustart nach Ausfall unterscheiden.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Ausfall simulieren | 5 |
| 5.2 | Priorität | 3 |
| 5.3 | Kapazität planen | 3 |
| 5.4 | Befehle lesen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ausfall simulieren (Einheit 5.1):** Führen Sie `python3 failover_sim.py` aus. Erklären Sie, welche VMs bei `hv01` und `hv02` neu gestartet werden und welche nicht.
2. **Priorität (Einheit 5.2):** Erklären Sie, warum `db1` nicht startet und welche Rolle die Priorität spielt.
3. **Kapazität planen (Einheit 5.3):** Berechnen Sie für drei Knoten mit je 64 GB, wie viel RAM insgesamt belegt sein darf, damit der Ausfall eines Knotens verkraftet wird (N+1).
4. **Befehle lesen (Einheit 5.4):** Lesen Sie `beispiel_powershell.txt` und erklären Sie, wie eine VM hochverfügbar wird und wie die Live-Migration angestoßen wird. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Was geschieht mit einer VM beim Knotenausfall?
2. Worin unterscheidet sich Live-Migration vom Neustart nach Ausfall?
3. Warum startet `db1` im Modell nicht?
4. Wie hoch darf die Gesamtbelegung bei drei Knoten zu je 64 GB sein?

### Modul 6: Hyper-V Replica

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Hyper-V Replica nennen.
  * Nach Abschluss dieses Moduls kann der Lernende RPO aus Intervall und Datenmenge abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Replikation von Cluster-Failover abgrenzen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | RPO abschätzen | 4 |
| 6.2 | Rückstand erkennen | 3 |
| 6.3 | Befehle lesen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **RPO abschätzen (Einheit 6.1):** Führen Sie `python3 replica_rpo.py` aus. Erklären Sie die Spalten und den schlimmsten Datenverlust.
2. **Rückstand erkennen (Einheit 6.2):** Erklären Sie, wann die Replikation in Rückstand gerät.
3. **Befehle lesen (Einheit 6.3):** Lesen Sie `beispiel_powershell.txt` und beschreiben Sie, wie die Replikation eingerichtet und geprüft wird. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Was bedeutet RPO?
2. Was bestimmt den Datenverlust bei Replikation?
3. Wie unterscheidet sich Replica vom Cluster?

### Modul 7: Cluster-aware Updating und Überwachung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer rollierenden Aktualisierung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende vor dem Leeren eines Knotens die Kapazität prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Überwachungspunkte eines Clusters nennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Rolling Update prüfen | 3 |
| 7.2 | Kapazität | 3 |
| 7.3 | Befehle lesen | 3 |
| 7.4 | Überwachung planen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rolling Update prüfen (Einheit 7.1):** Führen Sie `python3 cau_plan.py` aus. Erklären Sie, wie das Modell für jeden Knoten entscheidet.
2. **Kapazität (Einheit 7.2):** Erklären Sie die N+1-Aussage am Ende der Ausgabe und warum die Gesamtbelegung von 106 GB unproblematisch ist.
3. **Befehle lesen (Einheit 7.3):** Lesen Sie `beispiel_powershell.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Überwachung planen (Einheit 7.4):** Listen Sie auf, welche Zustände (Knoten, Rollen, Speicher, Netzwerke, Zeuge) Sie überwachen und wie Sie alarmieren.

#### Kontrollfragen

1. Was geschieht bei Cluster-aware Updating mit den VMs eines Knotens?
2. Wann bricht das Modell ab?
3. Wie viel Belegung erlaubt N+1 bei drei Knoten zu 64 GB?
4. Was sollte überwacht werden?

### Modul 8: Fehlersuche und Ausfalltests

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Testplan für Ausfälle aufstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Lücken im Testplan erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine systematische Fehlersuche im Cluster beschreiben.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Abdeckung prüfen | 3 |
| 8.2 | Tests ergänzen | 3 |
| 8.3 | Fehlersuche | 3 |
| 8.4 | Dokumentation | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Abdeckung prüfen (Einheit 8.1):** Führen Sie `python3 ausfalltest_plan.py` aus. Erklären Sie die Lücken im Testplan.
2. **Tests ergänzen (Einheit 8.2):** Ergänzen Sie für jede Lücke einen Test mit erwartetem Ergebnis und Rückfallweg.
3. **Fehlersuche (Einheit 8.3):** Lesen Sie `beispiel_powershell.txt` und schreiben Sie einen Ablaufplan „Rolle startet nicht auf dem Zielknoten“.
4. **Dokumentation (Einheit 8.4):** Beschreiben Sie, wie Sie Ausfalltests und Ergebnisse dokumentieren, damit sie wiederholbar sind.

#### Kontrollfragen

1. Welche Ausfallarten deckt der Testplan nicht ab?
2. Warum Ausfalltests vor dem Betrieb?
3. Wozu dient das Clusterprotokoll?
4. Warum einen Rückfallweg planen?
