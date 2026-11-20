# Lehrplan: Azure Administration

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze) |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Microsoft Azure: Abonnements, Verwaltungsgruppen und Ressourcengruppen, Tags und Sperren, Rollen und Bereiche (RBAC), virtuelle Netzwerke, virtuelle Maschinen und ARM-Vorlagen, Speicher, Sicherung und Überwachung, App Service und Container im Überblick, Azure Policy, Kosten und Budgets, Azure CLI |
| **Thematische Abgrenzung (Out of Scope)** | Der vorhandene Kurs „M365 Governance“ behandelt die Microsoft-365-Seite; AWS ist ein eigener Lehrplan; Azure-Netzwerk und Azure-Sicherheit im Detail sind im Kurs „Azure-Netzwerk und Azure-Sicherheit“, Entra ID im Kurs „Entra ID und Hybrid-Identität“. **Azure wurde nicht ausgeführt:** Es gab weder ein Abonnement noch einen Mandanten noch eine Anmeldung. **Echt ausgeführt** sind nur (1) die Prüfung, ob Befehle und Parameter in der installierten **Azure CLI 2.93.0** existieren (`az … --help`, offline), (2) Rechnungen und JSON-Verarbeitung in Python (CIDR, HMAC, JSON). Azure selbst ist ein **Lernmodell in Python** (`azsim.py`) mit **erfundenen** Größen, Preisen und Kontingenten. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Abonnements, Verwaltungsgruppen und Ressourcengruppen | 1 | 12 |
| 2 | Identitäten und rollenbasierte Zugriffssteuerung (RBAC) | 1 | 14 |
| 3 | Virtuelle Netzwerke, Subnetze und Peering | 1 | 14 |
| 4 | Virtuelle Maschinen und ARM-Vorlagen | 1 | 14 |
| 5 | Speicher: Konten, Redundanz, Zugriff und Lebenszyklus | 1 | 12 |
| 6 | Sicherung und Überwachung | 1 | 12 |
| 7 | App Service und Container im Überblick | 2 | 8 |
| 8 | Azure Policy, Kosten und Abschlussprojekt | 1 | 14 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (App Service und Container im Überblick). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 92 UE. **Achtung:** Das Thema „App Service und Container“ aus dem Lehrplan steckt ausschließlich in Modul 7; ohne dieses Modul fehlt es vollständig (bei einer Ausrichtung an AZ-104 kein Weglassen empfohlen). Kein anderes Modul setzt Modul 7 voraus.

### 2. Quellen

**Gelesen (Microsoft Learn, Suchauszug vom 20.11.2026):** Seite „Study guide for Exam AZ-104: Microsoft Azure Administrator“. Der Auszug nennt die Prüfungsbereiche (Identitäten und Governance 20–25 %, Speicher 15–20 %, Compute 20–25 %, virtuelle Netzwerke 15–20 %, Überwachung und Wiederherstellung 10–15 %) mit dem Vermerk „Skills measured as of October 26, 2023“. **Ob es inzwischen eine neuere Fassung gibt, wurde nicht geprüft**; die Seite wurde nicht vollständig gelesen. Die Module orientieren sich sinngemäß an diesen Bereichen; **es wurden keine Prüfungsfragen übernommen**.

**Nicht gelesen:** Alle weiteren Azure-Dokumentationsseiten. Aussagen zu Rollen, Redundanz, Subnetz-Reservierung, Sperren, Richtlinien und Preisen sind Fachwissen, stark vereinfacht und **nicht bestätigt**. Portalmenüs sind **nicht bestätigt** (nicht geprüft, daher im Kurs nicht beschrieben). **Preise, Kontingente und Grenzwerte im Modell sind erfunden.**

**Getestet mit (Ubuntu 24.04, Cloud-Container):** Python 3.13, Azure CLI 2.93.0 (pip, nur Hilfetexte), Modell `azsim.py`. **Nicht ausgeführt:** Azure-Abonnement, `az login`, Portal, Bicep (nicht installierbar im Cloud-Container), PowerShell.

### 3. Labor-Setup & Rahmenbedingungen

**Azure-Zugang:** Ein **Test-Tenant** (Microsoft-365-Entwickler- oder Testzugang), **kein produktiver Tenant**. Laufzeit und mögliche Kosten vorab prüfen (nicht geprüft). **Kostenlimit und Budgetwarnung einrichten**, Ressourcen nach jeder Übung löschen (Ressourcengruppe löschen).

**Arbeitsplatz:** Ein Rechner mit Azure CLI (`pip install azure-cli` oder Installer) und einem Browser. Das Labor wurde **nicht** aufgebaut.

**Skripte:** Die Skripte laufen unter Linux mit dem Modell `azsim.py` und arbeiten unter `/tmp/p27`; sie brauchen keinen Azure-Zugang. Die Prüfung der Befehle nutzt `az … --help` und braucht keine Anmeldung. Im Test-Tenant ersetzt man die Modell-Befehle durch `az` (nicht geprüft).

## B. Detaillierter Modulaufbau

### Modul 1: Abonnements, Verwaltungsgruppen und Ressourcengruppen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Hierarchie Mandant, Verwaltungsgruppe, Abonnement, Ressourcengruppe beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Ressourcengruppen mit Tags anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung einer Sperre beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Azure-CLI-Befehle für diese Aufgaben benennen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Hierarchie | 4 |
| 1.2 | Gruppen und Tags | 4 |
| 1.3 | Sperre | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Hierarchie (Einheit 1.1):** Führen Sie `bash hierarchie.sh` aus. Zeichnen Sie anhand von Schritt 2 die Hierarchie auf, und erklären Sie, wo das Abonnement hängt.
2. **Gruppen und Tags (Einheit 1.2):** Erklären Sie Schritt 3 und 4: Wozu dienen Tags, und welche Grenze meldet das Modell?
3. **Sperre (Einheit 1.3):** Erklären Sie Schritt 5: Warum scheitert das Löschen, und was ändert sich nach dem Entfernen der Sperre?

#### Kontrollfragen

1. Wo liegt das Abonnement nach Schritt 2?
2. Welche Meldung kommt bei einer doppelten Verwaltungsgruppe?
3. Was verhindert die Sperre `CanNotDelete`?
4. Was bedeutet „az … -> --name:ok“?

### Modul 2: Identitäten und rollenbasierte Zugriffssteuerung (RBAC)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rollenzuweisungen auf verschiedenen Bereichen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Vererbung und Gruppenmitgliedschaft in die Beurteilung einbeziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Steuerungsebene und Datenebene unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum eine Sperre eine Rolle übersteuert.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Zuweisungen | 6 |
| 2.2 | Zugriff prüfen | 4 |
| 2.3 | Ebenen und Sperre | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zuweisungen (Einheit 2.1):** Führen Sie `bash rbac.sh` aus. Erklären Sie Schritt 3 und 4: Welche Zuweisungen gelten für `rg-web` und `rg-daten`, und was ist geerbt?
2. **Zugriff prüfen (Einheit 2.2):** Erklären Sie Schritt 5 und 6: Warum darf `ana` VMs ändern, `ben` nicht, und warum darf `ana` keine Zuweisungen schreiben?
3. **Ebenen und Sperre (Einheit 2.3):** Erklären Sie Schritt 7 und 8: Wie unterscheiden sich Steuerungs- und Datenebene, und was bewirkt die Sperre?

#### Kontrollfragen

1. Woher hat `ana` ihre Rechte?
2. Warum darf `ben` keine VM ändern?
3. Warum darf `ana` die Blobs nicht lesen?
4. Was zeigt Schritt 8?

### Modul 3: Virtuelle Netzwerke, Subnetze und Peering

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Adressräume und Subnetze rechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehler bei Überlappung und falscher Lage erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Bedingung für Peering nennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Reihenfolge der NSG-Regeln erklären.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Adressen rechnen | 6 |
| 3.2 | Fehler und Peering | 4 |
| 3.3 | NSG | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Adressen rechnen (Einheit 3.1):** Führen Sie `bash vnet.sh` aus. Erklären Sie Schritt 2 bis 4: Wie viele Adressen hat ein /27, und wie groß muss ein Subnetz für 60 Server sein?
2. **Fehler und Peering (Einheit 3.2):** Erklären Sie Schritt 3 und 5: Warum werden `falsch` und `ueber` abgelehnt, und warum scheitert das Peering `hub` mit `alt`?
3. **NSG (Einheit 3.3):** Erklären Sie Schritt 6: Welche Regel trifft bei Port 443 und Port 22, und was gilt ohne eigene Regeln?

#### Kontrollfragen

1. Wie viele Adressen hat `10.10.2.0/27`, und wie viele sind nutzbar?
2. Wie groß ist das Subnetz für 60 Server?
3. Warum scheitert das Peering `hub` mit `alt`?
4. Was gilt für Port 22 aus dem Internet ohne eigene Regeln?

### Modul 4: Virtuelle Maschinen und ARM-Vorlagen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine VM mit Größe, Zone und Subnetz beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Kontingent und Kosten abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende eine ARM-Vorlage lesen und Strukturfehler finden.
  * Nach Abschluss dieses Moduls kann der Lernende JSON-Fehler lesen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | VMs und Kontingent | 6 |
| 4.2 | Größe und Kosten | 4 |
| 4.3 | Vorlage | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **VMs und Kontingent (Einheit 4.1):** Führen Sie `bash vm.sh` aus. Erklären Sie Schritt 3: Warum scheitern `gross` und `falsch`?
2. **Größe und Kosten (Einheit 4.2):** Erklären Sie Schritt 4: Wie ändern sich die Kosten nach dem Verkleinern von `web2`? (Preise sind erfunden.)
3. **Vorlage (Einheit 4.3):** Erklären Sie Schritt 5 bis 7: Welche Fehler findet die Strukturprüfung, und was meldet Python bei kaputtem JSON?

#### Kontrollfragen

1. Warum scheitert `gross`?
2. Warum scheitert `falsch`?
3. Wie hoch sind die Kosten nach dem Verkleinern?
4. Was findet die Prüfung in `fehler.json`?

### Modul 5: Speicher: Konten, Redundanz, Zugriff und Lebenszyklus

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Namensregeln für Speicherkonten anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Redundanzstufen nach Ausfallbereich einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende ein zeitlich begrenztes Zugriffstoken im Prinzip erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Lebenszyklusregeln lesen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Konten und Redundanz | 4 |
| 5.2 | Token | 4 |
| 5.3 | Lebenszyklus | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Konten und Redundanz (Einheit 5.1):** Führen Sie `bash speicher.sh` aus. Erklären Sie Schritt 2 und 3: Welche Redundanzstufe übersteht welchen Ausfall, und warum scheitern vier der Namen?
2. **Token (Einheit 5.2):** Erklären Sie Schritt 4: Warum wird der Zugriff abgelehnt, und was bewirkt der andere Schlüssel? Beachten Sie: Das Token ist nur ein Modell.
3. **Lebenszyklus (Einheit 5.3):** Erklären Sie Schritt 5 und 6: In welcher Stufe liegt ein Blob nach 5, 40, 120 und 400 Tagen?

#### Kontrollfragen

1. Welche Stufe übersteht den Ausfall eines Rechenzentrums, aber nicht den der Region?
2. Warum scheitert `LabDaten`?
3. Warum wird der Zugriff bei Zeit 1001 abgelehnt?
4. Welche Stufe hat ein Blob mit 120 Tagen?

### Modul 6: Sicherung und Überwachung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aufbewahrung und Wiederherstellungspunkte berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum eine Wiederherstellung auf einen bestimmten Tag nicht immer möglich ist.
  * Nach Abschluss dieses Moduls kann der Lernende einen Metrik-Alarm mit Fenster und Schwellwert beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende kurze Spitzen von dauerhaften Problemen unterscheiden.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Aufbewahrung | 4 |
| 6.2 | Alarm | 4 |
| 6.3 | Schwelle nach unten | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Aufbewahrung (Einheit 6.1):** Führen Sie `bash sicherung.sh` aus. Erklären Sie Schritt 2: Wie viele Wiederherstellungspunkte entstehen, und warum geht „vor 20 Tagen“ nicht?
2. **Alarm (Einheit 6.2):** Erklären Sie Schritt 4 und 5: Wann löst der Alarm mit Fenster 3, 2 und 1 aus?
3. **Schwelle nach unten (Einheit 6.3):** Erklären Sie Schritt 6: Wann löst der Alarm bei zu wenig freiem Speicher aus?

#### Kontrollfragen

1. Wie viele Punkte gibt es bei 7/4/3 nach 100 Tagen?
2. Warum geht „vor 20 Tagen“ nicht?
3. Wann löst die Reihe mit Fenster 3 aus?
4. Warum löst die Reihe mit Spitzen und Fenster 3 nicht aus?

### Modul 7: App Service und Container im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Regeln der Autoskalierung nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende den Slot-Tausch und haftende Einstellungen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Größe einer Container-Gruppe festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Befehle für App Service und Container nennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Autoskalierung | 4 |
| 7.2 | Slot-Tausch | 2 |
| 7.3 | Container | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Autoskalierung (Einheit 7.1):** Führen Sie `bash app.sh` aus. Erklären Sie Schritt 2: Wie verläuft die Instanzzahl, wenn die CPU steigt und fällt?
2. **Slot-Tausch (Einheit 7.2):** Erklären Sie Schritt 3: Was ändert die Markierung `--sticky DB`?
3. **Container (Einheit 7.3):** Erklären Sie Schritt 4: Wie setzt sich der (erfundene) Preis der Container-Gruppe zusammen?

#### Kontrollfragen

1. Wann steigt die Instanzzahl?
2. Wann sinkt sie?
3. Was bewirkt `--sticky DB`?
4. Wie hoch ist der Preis für 2 vCPU und 4 GiB?

### Modul 8: Azure Policy, Kosten und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Richtlinien mit Wirkung deny und audit unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine Ausnahme (notScopes) anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende ein Budget mit Schwellen auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende ein kleines Vorhaben kostenmäßig abschätzen und aufräumen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Richtlinien | 6 |
| 8.2 | Ausnahme und Budget | 4 |
| 8.3 | Abschluss | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Richtlinien (Einheit 8.1):** Führen Sie `bash abschluss.sh` aus. Erklären Sie Schritt 3: Welche Ressource wird bei welcher Richtlinie abgelehnt, und was bewirkt `audit`?
2. **Ausnahme und Budget (Einheit 8.2):** Erklären Sie Schritt 4 und 5: Was bewirkt `notScopes`, und bei welchen Tagen löst das Budget Warnungen aus?
3. **Abschluss (Einheit 8.3):** Erklären Sie Schritt 6 und 7: Wie hoch sind die geschätzten Kosten, und warum löscht man die Ressourcengruppe?

#### Kontrollfragen

1. Welche Ressource lehnt `nur-westeuropa` ab?
2. Was macht `tag-audit` mit `vm-notag`?
3. An welchen Tagen warnt das Budget?
4. Warum stoppt die Budgetwarnung die Kosten nicht?
