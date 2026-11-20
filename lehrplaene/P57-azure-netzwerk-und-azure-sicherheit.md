# Lehrplan: Azure-Netzwerk und Azure-Sicherheit

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Azure-Grundlagen (siehe Kurs „Azure Administration“); Grundkenntnisse in Netzwerken |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Microsoft Azure (VNet, NSG, Azure Firewall, Key Vault, Defender for Cloud), Azure CLI und PowerShell; virtuelle Netzwerke und Subnetze; Peering; NSG und ASG; Routen, Azure Firewall und Bastion; VPN Gateway; Private Endpoints; DNS in Azure; Key Vault; RBAC und Azure Policy; Defender for Cloud; Protokollierung und Überwachung; Fehlersuche |
| **Thematische Abgrenzung (Out of Scope)** | Azure Administration und Entra ID sind eigene Kurse; Zertifikatsgrundlagen im Kurs „Kryptografie, Zertifikate und TLS“. Nicht behandelt: ExpressRoute im Detail, Azure Virtual WAN, Front Door/Application Gateway |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Virtuelle Netzwerke, Subnetze und Peering | 1 | 14 |
| 2 | Netzwerksicherheitsgruppen und Anwendungssicherheitsgruppen | 1 | 14 |
| 3 | Routen, Azure Firewall, Bastion und VPN Gateway | 1 | 12 |
| 4 | Private Endpoints und DNS | 1 | 12 |
| 5 | Key Vault | 2 | 10 |
| 6 | RBAC und Azure Policy | 1 | 14 |
| 7 | Defender for Cloud, Protokollierung und Überwachung | 1 | 12 |
| 8 | Fehlersuche im Azure-Netzwerk | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 4 und 6 bis 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 5 (Key Vault). Fällt Modul 5 weg, verringert sich der Gesamtumfang auf 90 UE; kein Pflichtmodul setzt Modul 5 voraus.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von Microsoft Azure (VNet, NSG, Azure Firewall, Private Link, Key Vault, RBAC, Policy, Defender for Cloud, Azure CLI) wurde **nicht** gelesen. Alle fachlichen Aussagen, Standardwerte und CLI-Befehle stammen aus Fachwissen und sind **nicht bestätigt**; verbindlich ist die aktuelle Microsoft-Dokumentation. **Preise, Kontingente und Lizenz-/Supportstände wurden nicht recherchiert** und sind mit Stand zu prüfen.

**Ausgeführt wurden ausschließlich die Python-Modelle** (Python 3 im Cloud-Container): reine Rechnungen mit erfundenen Werten, **stark vereinfacht** (z. B. NSG nur eingehend und TCP, Rollen mit erfundenen Namen). **Nicht ausgeführt:** Azure-Abonnement, Azure CLI, PowerShell. Alle Namen und Daten sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Abonnement:** ein Azure-Abonnement (Testkonto oder Visual-Studio-Guthaben) **mit Budgetwarnung** (vor jeder Übung einrichten; Preise und Gratis-Kontingente mit Stand prüfen). **Client:** `win11` (Windows-11-Client) mit Azure CLI und PowerShell.

**Aufräumen:** Nach jeder Übung Ressourcengruppen löschen; manche Ressourcen (z. B. Azure Firewall, VPN Gateway, Bastion) verursachen laufend erhebliche Kosten, solange sie bestehen (Fachwissen, mit Stand prüfen).

**Skripte:** Die Python-Modelle laufen auf jedem Rechner mit Python 3, auch ohne Abonnement. Die CLI-Textdateien wurden **nicht** ausgeführt.

## B. Detaillierter Modulaufbau

### Modul 1: Virtuelle Netzwerke, Subnetze und Peering

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Adressräume und Subnetze für virtuelle Netzwerke planen.
  * Nach Abschluss dieses Moduls kann der Lernende Überlappungen von Adressräumen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Voraussetzung für Peering nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Subnetzgrößen mit reservierten Adressen berechnen.
* **Voraussetzungen:** Azure-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Subnetze planen | 5 |
| 1.2 | Peering prüfen | 3 |
| 1.3 | Befehle lesen | 3 |
| 1.4 | Eigener Plan | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Subnetze planen (Einheit 1.1):** Führen Sie `python3 vnet_plan.py` aus. Erklären Sie die Aufteilung des Hub-Netzwerks und die nutzbaren Adressen.
2. **Peering prüfen (Einheit 1.2):** Erklären Sie, warum `app` und `test` nicht gepeert werden können.
3. **Befehle lesen (Einheit 1.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie `vnet create` und `peering create`. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Eigener Plan (Einheit 1.4):** Planen Sie drei Netzwerke (Hub, Anwendung, Test) überlappungsfrei und begründen Sie die Größen.

#### Kontrollfragen

1. Warum dürfen sich Adressräume beim Peering nicht überlappen?
2. Wie viele Adressen sind in einem /27 nutzbar?
3. Welche Netzwerke überlappen im Modell?
4. Wozu dient das Peering?

### Modul 2: Netzwerksicherheitsgruppen und Anwendungssicherheitsgruppen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Regelauswertung nach Priorität erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Standardregeln lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln für einen Webserver und Verwaltungszugriff entwerfen.
  * Nach Abschluss dieses Moduls kann der Lernende ASGs einordnen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Regeln auswerten | 5 |
| 2.2 | Prioritäten | 3 |
| 2.3 | Befehle lesen | 3 |
| 2.4 | Regelwerk entwerfen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regeln auswerten (Einheit 2.1):** Führen Sie `python3 nsg_modell.py` aus. Erklären Sie für jeden der fünf Fälle, welche Regel entscheidet und warum.
2. **Prioritäten (Einheit 2.2):** Erklären Sie, was passiert, wenn `verbiete-ssh` die Priorität 50 statt 300 hätte.
3. **Befehle lesen (Einheit 2.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Regelwerk entwerfen (Einheit 2.4):** Entwerfen Sie Regeln für einen Webserver (HTTPS aus dem Internet, SSH nur aus dem Verwaltungsnetz) und nennen Sie, wo ASGs helfen.

#### Kontrollfragen

1. Welche Regel gilt bei mehreren Treffern?
2. Was geschieht ohne passende eigene Regel?
3. Wozu dienen ASGs (Fachwissen)?
4. Warum SSH nur intern erlauben?

### Modul 3: Routen, Azure Firewall, Bastion und VPN Gateway

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Routenauswahl mit eigenen Routen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck einer zentralen Firewall im Hub beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Bastion und VPN Gateway einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Kostenrisiken dieser Dienste benennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Routen auswerten | 3 |
| 3.2 | Eigene Routen | 3 |
| 3.3 | Befehle lesen | 3 |
| 3.4 | Einordnen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Routen auswerten (Einheit 3.1):** Führen Sie `python3 routen_modell.py` aus. Erklären Sie, warum Ziele außerhalb des VNets zur Firewall gehen.
2. **Eigene Routen (Einheit 3.2):** Erklären Sie, was bei gleichem Präfix gilt und warum das für eine zentrale Firewall wichtig ist.
3. **Befehle lesen (Einheit 3.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie Routentabelle, Route und Firewall. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Einordnen (Einheit 3.4):** Beschreiben Sie in fünf Sätzen, wozu Bastion und VPN Gateway dienen (Fachwissen) und nennen Sie, was Sie zu Kosten noch prüfen müssten.

#### Kontrollfragen

1. Welche Route gewinnt im Modell für 10.60.1.1?
2. Warum werden 8.8.8.8 und der Internetverkehr zur Firewall geleitet?
3. Wozu dient Bastion (Fachwissen)?
4. Warum Kosten prüfen?

### Modul 4: Private Endpoints und DNS

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Private Endpoints erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Namensauflösung mit privatelink-Zonen nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, warum eine fehlende Zonenverknüpfung zur öffentlichen Adresse führt.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Auflösung prüfen | 4 |
| 4.2 | Fehlerbild | 4 |
| 4.3 | Befehle lesen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auflösung prüfen (Einheit 4.1):** Führen Sie `python3 dns_modell.py` aus. Erklären Sie beide Ergebnisse.
2. **Fehlerbild (Einheit 4.2):** Beschreiben Sie, welche Folgen es hat, wenn ein Dienst nur über die private Adresse erreichbar sein soll, die Zone aber nicht verknüpft ist.
3. **Befehle lesen (Einheit 4.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie Endpoint, Zone und Verknüpfung. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Was bewirkt ein Private Endpoint?
2. Warum liefert das zweite Netz die öffentliche Adresse?
3. Welche Zone gehört zu Blob-Speicher im Modell?

### Modul 5: Key Vault

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck eines Key Vaults nennen.
  * Nach Abschluss dieses Moduls kann der Lernende rollenbasierten Zugriff auf Geheimnisse planen.
  * Nach Abschluss dieses Moduls kann der Lernende Umgang mit Geheimnissen beschreiben.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Zugriff auswerten | 4 |
| 5.2 | Geheimnisse sicher behandeln | 3 |
| 5.3 | Befehle lesen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zugriff auswerten (Einheit 5.1):** Führen Sie `python3 keyvault_zugriff.py` aus. Erklären Sie die Ergebnisse je Rolle.
2. **Geheimnisse sicher behandeln (Einheit 5.2):** Beschreiben Sie, warum Geheimnisse nicht in Dateien oder Repositories gehören und wie ein Vault das löst.
3. **Befehle lesen (Einheit 5.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie jeden Befehl. Kennzeichnen Sie, was Sie nicht geprüft haben.

#### Kontrollfragen

1. Wozu dient ein Key Vault?
2. Warum rollenbasierter Zugriff?
3. Wie behandelt man ein Geheimnis im Befehl?

### Modul 6: RBAC und Azure Policy

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Vererbung von Rollenzuweisungen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Rolle und Richtlinie unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Effekte Deny und Audit unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Rechte nach dem Grundsatz der geringsten Rechte vergeben.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Vererbung | 5 |
| 6.2 | Richtlinien | 3 |
| 6.3 | Befehle lesen | 3 |
| 6.4 | Konzept | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vererbung (Einheit 6.1):** Führen Sie `python3 rbac_policy_modell.py` aus. Erklären Sie, welche Rolle jede Person auf welcher Ebene hat.
2. **Richtlinien (Einheit 6.2):** Erklären Sie die Richtlinie „erlaubte Regionen“ (Deny) und „Pflicht-Tag“ (Audit).
3. **Befehle lesen (Einheit 6.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie Rollenzuweisung und Richtlinienzuweisung. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Konzept (Einheit 6.4):** Entwerfen Sie Rollenzuweisungen und eine Richtlinie für ein Entwicklungsabonnement und begründen Sie die Ebenen.

#### Kontrollfragen

1. Wie wirken Rollenzuweisungen nach unten?
2. Worin unterscheiden sich RBAC und Policy?
3. Was bewirkt Deny, was Audit?
4. Warum hat `cara` auf `rg-db` keine Rolle?

### Modul 7: Defender for Cloud, Protokollierung und Überwachung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aufgabe von Defender for Cloud einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Flow-Protokolle auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Schwellen für Alarme festlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Kosten der Protokollierung bedenken.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Protokolle auswerten | 3 |
| 7.2 | Schwelle | 3 |
| 7.3 | Befehle lesen | 3 |
| 7.4 | Konzept | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Protokolle auswerten (Einheit 7.1):** Führen Sie `python3 log_modell.py` aus. Erklären Sie das Ergebnis je Quelle.
2. **Schwelle (Einheit 7.2):** Erklären Sie, wie Sie die Schwelle 3 begründen und welche Fehlalarme entstehen können.
3. **Befehle lesen (Einheit 7.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie Diagnose-Einstellungen und Defender-Pläne. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Konzept (Einheit 7.4):** Planen Sie, welche Protokolle Sie sammeln, wie lange Sie sie aufbewahren und wer alarmiert wird (Kosten mit Stand prüfen).

#### Kontrollfragen

1. Wie viele Zeilen wurden abgelehnt?
2. Welche Quelle löst den Alarm aus?
3. Wozu dient Defender for Cloud (Fachwissen)?
4. Warum Aufbewahrungsdauer festlegen?

### Modul 8: Fehlersuche im Azure-Netzwerk

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Verbindung entlang der Kette Namensauflösung, Route und Sicherheitsgruppe prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende das blockierende Glied eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende passende Diagnosebefehle nennen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Kette prüfen | 3 |
| 8.2 | Reihenfolge | 3 |
| 8.3 | Befehle lesen | 3 |
| 8.4 | Ablaufplan | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Kette prüfen (Einheit 8.1):** Führen Sie `python3 diagnose_modell.py` aus. Erklären Sie, wo die vier Fälle jeweils blockieren.
2. **Reihenfolge (Einheit 8.2):** Begründen Sie die Reihenfolge der Prüfungen (Namensauflösung, Route, Sicherheitsgruppe).
3. **Befehle lesen (Einheit 8.3):** Lesen Sie `beispiel_cli.txt` und erklären Sie `test-connectivity`, `show-effective-route-table` und `list-effective-nsg`. Kennzeichnen Sie, was Sie nicht geprüft haben.
4. **Ablaufplan (Einheit 8.4):** Schreiben Sie einen Ablaufplan „VM erreicht Speicherkonto nicht“ mit den Prüfungen aus den Modulen 2 bis 4.

#### Kontrollfragen

1. Wo blockiert `vm1 -> db1`?
2. Warum zuerst die Namensauflösung prüfen?
3. Welche Befehle zeigen die wirksamen Routen und Regeln (Fachwissen)?
4. Warum Ergebnisse dokumentieren?
