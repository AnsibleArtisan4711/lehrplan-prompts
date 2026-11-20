# Lehrplan: Windows-Server-Härtung

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Active-Directory- und Gruppenrichtlinien-Grundlagen |
| **Gesamtumfang** | 13 Module, 111 UE (zu 45 Minuten; 83,25 Stunden) |
| **Fokus-Technologien** | Windows Server (2022 oder 2025), Gruppenrichtlinien, PowerShell; Windows 11 als Client |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Active-Directory-Grundlagen im AD-Kurs, Härtung von Linux-Servern im Kurs „Linux-Server-Härtung“, Schwachstellenscans im Kurs „Schwachstellenmanagement“, Grundbegriffe im Kurs „IT-Sicherheitsgrundlagen“. Nicht behandelt: Härtung von Exchange, SQL Server und IIS im Detail, Microsoft Intune und Entra-ID-Verwaltung über Hinweise hinaus, Azure-Härtung, Active-Directory-Wiederherstellung (Forest Recovery), Zertifikatsdienste |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Härtungskonzept und Sicherheitsbaselines | 1 | 8 |
| 2 | Tier-Modell und Administrationskonten | 1 | 9 |
| 3 | Lokale Richtlinien und Gruppenrichtlinien | 1 | 10 |
| 4 | Konten, Kennwort- und Sperrrichtlinien | 1 | 8 |
| 5 | Dienste und Rollen reduzieren | 1 | 8 |
| 6 | Microsoft Defender und Windows-Firewall | 1 | 9 |
| 7 | Anmeldeschutz: Windows LAPS und lokale Konten | 1 | 9 |
| 8 | Überwachungsrichtlinie und Protokollierung | 1 | 9 |
| 9 | Ereignisse auswerten und Angriffe erkennen | 1 | 8 |
| 10 | Patch-Management | 1 | 8 |
| 11 | Fernzugriff und Protokolle: RDP, SMB, NTLM, WinRM | 1 | 8 |
| 12 | Zusatzschutz: Credential Guard, Anwendungskontrolle, Secure Boot | 2 | 7 |
| 13 | Härtung prüfen, dokumentieren und Fehlersuche | 1 | 10 |
| **Gesamt** | 13 Module | 12 × Priorität 1, 1 × Priorität 2 | **111** |

**Priorität 1** (Pflicht) sind die Module 1 bis 11 und 13; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 12 (Zusatzschutz: Credential Guard, Anwendungskontrolle, Secure Boot). Fällt Modul 12 weg, verringert sich der Gesamtumfang auf 104 UE; kein Pflichtmodul setzt Modul 12 voraus.

### 2. Quellen

**Gelesen über das Microsoft-Learn-Werkzeug am 20.11.2026 (nur Suchauszüge, nicht die vollständigen Seiten):** (1) „What is Windows LAPS?“, „Key concepts in Windows LAPS“, „Overview of Windows LAPS PowerShell Cmdlets“ (Windows LAPS ab Windows Server 2019; Sicherung nach Active Directory oder Entra ID; Kennwortverschlüsselung in AD verlangt Domänenfunktionsebene 2016; Erkennung zurückgesetzter Abbilder ab Windows Server 2025 / Windows 11 24H2; Cmdlets). (2) „Credential Guard“, „Considerations and known issues“, „Configure Credential Guard“ (Standardaktivierung ab Windows 11 22H2 und Windows Server 2025 auf domänenverbundenen Nicht-Domänencontrollern; blockiert u. a. NTLMv1-SSO, MS-CHAP, WDigest-SSO, unbeschränkte Kerberos-Delegierung). (3) „Microsoft Security Compliance Toolkit“ und „Security baselines“ (Baselines für Windows Server 2016 bis 2025, Policy Analyzer, LGPO, Formate `.pol`, `.inf`, `.csv`; Microsoft-Baselines sind nicht gleich CIS-konform). (4) „Tier model for Active Directory Domain Services“ und „Enterprise access model“ (Tier 0/1/2, privilegierte Arbeitsstationen). (5) „Advanced Audit Policy Configuration“, „Monitoring Active Directory for Signs of Compromise“, „System audit policy recommendations“ (`auditpol`-Syntax, Ereignis-Kennungen 4624, 4625, 4720, 4688). Der Stand der Dokumentation ändert sich; Versionsnummern vor dem Einsatz prüfen.

**Nicht gelesen:** die **CIS Benchmarks** (nach Registrierung frei verfügbar; Nummerierung und Maßnahmen werden hier **nicht** übernommen, die Kursmaßnahmen sind eigene Formulierungen); die Dokumentation zu Microsoft Defender Antivirus, Windows-Firewall mit erweiterter Sicherheit, Windows Update for Business und WSUS; die Handbuchseiten der PowerShell-Cmdlets (außer den Namen der LAPS-Cmdlets aus (1)). Aussagen dazu sind **Fachwissen und nicht bestätigt**. Alle Beispieldaten (Vorlagen, Konten, Dienste, Regeln, Ereignisse, Patchstände) sind **frei erfunden**.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-WinHaertung`, `10.13.0.0/24`).

**VMs:** `srv01` (**erforderlich**, `10.13.0.10`): Windows Server 2022 oder 2025 (Testversion), Domänencontroller und Dateiserver einer Testdomäne (nur im Labor in dieser Doppelrolle), 2 vCPU, 4 GB RAM, 40 GB Platte. `cl01` (**erforderlich**, `10.13.0.20`): Windows 11 (Testversion) als Domänenmitglied und Verwaltungs-Arbeitsstation.

**Internetphase:** Für Testversionen, Updates und die Microsoft Security Compliance Toolkit-Downloads brauchen die VMs vorübergehend eine zweite Netzwerkkarte an einem externen Switch; danach wird sie entfernt. Heruntergeladene Dateien vor dem Einsatz prüfen (Herkunft, Prüfsumme).

**Prüfpunkt (Checkpoint):** Vor Modulen mit Richtlinienänderungen einen Hyper-V-Prüfpunkt anlegen. **Achtung:** Das Zurücksetzen eines Domänencontrollers auf einen Prüfpunkt kann die Domäne beschädigen (USN-Rollback); Windows LAPS erkennt zurückgesetzte Abbilder erst ab Windows Server 2025 (laut Dokumentation). Im Labor Prüfpunkte nur auf `cl01` und mit Bedacht auf `srv01` einsetzen, sonst Sicherung des Systemzustands verwenden.

**Skripte:** Die Beispielskripte sind **Python-Prüfwerkzeuge** für Exportdateien (CSV, INF) mit erfundenen Daten; sie liefen in einem Linux-Container, **nicht** unter Windows. Die PowerShell- und Windows-Befehle im Text sind in der Übung als „nicht bestätigt“ gekennzeichnet, soweit sie nicht in der gelesenen Dokumentation stehen.

## B. Detaillierter Modulaufbau

### Modul 1: Härtungskonzept und Sicherheitsbaselines

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Härtungsziele und Prinzipien an Windows-Beispielen erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Microsoft-Baselines und CIS Benchmarks unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine exportierte Sicherheitsvorlage mit einer Baseline vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Härtungsprotokoll führen.
* **Voraussetzungen:** IT-Grundlagen; AD- und Gruppenrichtlinien-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Ziele der Härtung, Angriffsfläche, Least Privilege, Defense in Depth | 2 |
| 1.2 | Baselines: Microsoft Security Baselines und Security Compliance Toolkit, CIS Benchmarks (Profilstufen) | 2 |
| 1.3 | Praxis: Sicherheitsvorlage gegen eine Baseline-Tabelle vergleichen (`baseline_vergleich.py`) | 2 |
| 1.4 | Härtungsprotokoll: Soll, Ist, Ausnahme, Begründung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prinzipien zuordnen (Einheit 1.1):** Ordnen Sie fünf Maßnahmen (z. B. Spooler abschalten, Administratorkonten trennen, SMB-Signierung verlangen, Überwachung einschalten, Updates einspielen) den Prinzipien Angriffsfläche, Least Privilege und Defense in Depth zu und begründen Sie je einen Satz.
2. **Baseline wählen (Einheit 1.2):** Laden Sie in der Internetphase die Security Compliance Toolkit-Baseline für Ihre Windows-Server-Version herunter, prüfen Sie Herkunft und Prüfsumme und beschreiben Sie, welche Dateien (GPO-Sicherungen, Berichte, Tabellen) sie enthält. Begründen Sie, warum Sie nicht die gesamte Baseline ungeprüft anwenden.
3. **Vorlage vergleichen (Einheit 1.3):** Führen Sie `python3 baseline_vergleich.py sicherheit.inf baseline.csv` aus und ordnen Sie jede Abweichung einer Auswirkung zu. Ergänzen Sie `baseline.csv` um eine eigene Zeile (z. B. `PasswordHistorySize >= 12`).
4. **Protokoll anlegen (Einheit 1.4):** Legen Sie ein Härtungsprotokoll mit den Spalten Maßnahme, Soll, Ist, Datum, Ausnahme und Begründung an und tragen Sie die Ergebnisse aus Aufgabe 3 ein.

#### Kontrollfragen

1. Warum ist eine Microsoft-Baseline nicht automatisch CIS-konform?
2. Warum wird eine Baseline vor dem Einsatz getestet und angepasst?
3. Was kann der Policy Analyzer, was ein einfacher Vergleich in `baseline_vergleich.py` nicht kann?
4. Welche Angaben gehören in die Begründung einer Ausnahme?

### Modul 2: Tier-Modell und Administrationskonten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die drei Tiers des Active-Directory-Tier-Modells beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum sich ein Administrator nicht an einer niedrigeren Stufe anmelden soll.
  * Nach Abschluss dieses Moduls kann der Lernende Anmeldeprotokolle auf Verletzungen der Stufentrennung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Kontenkonzept mit getrennten Administrationskonten entwerfen.
* **Voraussetzungen:** Modul 1; AD-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Tier 0, Tier 1, Tier 2: Identitätsebene, Server, Arbeitsplätze | 2 |
| 2.2 | Privilegierte Arbeitsstationen (PAW), „saubere Tastatur“, Rückgriff (Reach-back) | 2 |
| 2.3 | Praxis: Anmeldungen gegen das Tier-Modell prüfen (`tier_pruefung.py`) | 2 |
| 2.4 | Konten und Gruppen trennen: Admin-Konten je Stufe, Domänen-Admins klein halten | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Systeme einstufen (Einheit 2.1):** Ordnen Sie `srv01` (Domänencontroller), einen Dateiserver, einen Anwendungsserver, `cl01` und ein Helpdesk-Konto den Tiers 0, 1 und 2 zu und begründen Sie je einen Satz.
2. **PAW beschreiben (Einheit 2.2):** Beschreiben Sie in fünf Sätzen, was eine privilegierte Arbeitsstation ausmacht (nur für Administration, keine E-Mail, keine unverwalteten Programme) und warum sie zur Stufe passen muss.
3. **Anmeldungen prüfen (Einheit 2.3):** Führen Sie `python3 tier_pruefung.py anmeldungen.csv` aus. Erklären Sie die fünf Verletzungen und geben Sie je eine Gegenmaßnahme an.
4. **Kontenkonzept (Einheit 2.4):** Entwerfen Sie für Ihr Labor Konten und Gruppen (persönliches Konto, Admin-Konto je Stufe, Dienstkonto) und legen Sie fest, wo sie sich anmelden dürfen. Nennen Sie, wie viele Personen Domänen-Admins sein sollen und warum so wenige.

#### Kontrollfragen

1. Wofür steht Tier 0 im Tier-Modell?
2. Warum bleibt ein Hilfsserver (Sprungserver), der zu Tier 0 verwaltet, ein Tier-0-System?
3. Warum ist die Anmeldung eines Tier-0-Kontos an einem Arbeitsplatz gefährlich?
4. Was bedeutet „keine gemeinsamen Zugangsdaten über Stufen hinweg“?

### Modul 3: Lokale Richtlinien und Gruppenrichtlinien

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Verarbeitungsreihenfolge von Gruppenrichtlinien erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Erzwingen und „Vererbung blockieren“ in ihrer Wirkung unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende mit dem Modell den wirksamen Wert einer Einstellung bestimmen.
  * Nach Abschluss dieses Moduls kann der Lernende wirksame Richtlinien auf einem Rechner diagnostizieren.
* **Voraussetzungen:** Modul 1; GPO-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Lokale Richtlinie und Gruppenrichtlinien: Verarbeitungsreihenfolge LSDOU, Vererbung, Erzwingen | 3 |
| 3.2 | Sicherheitsfilterung, WMI-Filter, Loopback: Wirkung eingrenzen | 2 |
| 3.3 | Praxis: Vorrang an Beispielen nachvollziehen (`gpo_vorrang.py`) | 2 |
| 3.4 | Diagnose: `gpresult`, `gpupdate`, Ergebnissatz der Richtlinien (RSoP), Ereignisprotokoll | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Reihenfolge erklären (Einheit 3.1):** Erklären Sie die Reihenfolge lokal, Standort, Domäne, Organisationseinheit und geben Sie an, welche Einstellung bei Konflikt gewinnt. Stellen Sie die Reihenfolge als Skizze dar.
2. **Filter einsetzen (Einheit 3.2):** Beschreiben Sie, wie Sie eine GPO nur auf eine Gruppe von Servern wirken lassen (Sicherheitsfilterung, WMI-Filter) und wann welches Mittel passt.
3. **Modell ausführen (Einheit 3.3):** Führen Sie `python3 gpo_vorrang.py` aus. Notieren Sie je Szenario, welche Einstellung aus welcher GPO kommt, und erklären Sie, warum im zweiten Szenario die Webserver-Ausnahme nicht mehr greift.
4. **Diagnose planen (Einheit 3.4):** Beschreiben Sie, wie Sie in `cl01` herausfinden, warum eine Einstellung nicht wirkt: Befehle, Ort der Ergebnisse, Ereignisprotokoll. Kennzeichnen Sie, was Sie nicht ausgeführt haben.

#### Kontrollfragen

1. Welche Einstellung gewinnt, wenn Domäne und OU denselben Wert unterschiedlich setzen?
2. Was bewirkt „Erzwingen“ gegenüber „Vererbung blockieren“?
3. Warum sollte „Vererbung blockieren“ sparsam eingesetzt werden?
4. Wozu dient die Ausgabe von `gpresult`?

### Modul 4: Konten, Kennwort- und Sperrrichtlinien

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende sinnvolle Kennwort- und Sperrrichtlinien begründen.
  * Nach Abschluss dieses Moduls kann der Lernende auffällige Konten in einem Export erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Dienstkonten mit möglichst geringen Rechten und verwalteten Kennwörtern planen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf der Konten bereinigen.
* **Voraussetzungen:** Modul 1; Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Kennwortrichtlinien: Länge, Komplexität, Ablauf, Verlauf; detaillierte Richtlinien (PSO) | 2 |
| 4.2 | Kontosperrung und Anmeldeoptionen: Schwellwert, Dauer, Gastkonto, integriertes Administratorkonto | 2 |
| 4.3 | Praxis: Konten-Export prüfen (`konten_pruefen.py`) | 2 |
| 4.4 | Dienstkonten: gMSA statt Kennwörter, minimale Rechte | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Richtlinie festlegen (Einheit 4.1):** Legen Sie für Benutzer und für Administratoren je eine Kennwort- und Sperrrichtlinie fest (Länge, Ablauf, Sperrschwelle, Dauer) und begründen Sie die Unterschiede. Kennzeichnen Sie Werte, die Ihre Annahme sind.
2. **Sperrung abwägen (Einheit 4.2):** Beschreiben Sie, warum eine Sperrschwelle von 1 Fehlversuch problematisch ist (Aussperren durch Dritte), und schlagen Sie einen Wert samt Dauer vor.
3. **Konten prüfen (Einheit 4.3):** Führen Sie `python3 konten_pruefen.py konten_export.csv` aus. Erklären Sie die Auffälligkeiten und die Maßnahme zu jedem Konto.
4. **Dienstkonto planen (Einheit 4.4):** Planen Sie für ein Dienstkonto `svc-sql` den Wechsel auf ein gruppenverwaltetes Dienstkonto (gMSA) mit minimalen Rechten. Kennzeichnen Sie die PowerShell-Schritte als nicht bestätigt.

#### Kontrollfragen

1. Warum ist ein Administratorkonto mit nie ablaufendem Kennwort ein Risiko?
2. Was ist der Vorteil eines gMSA gegenüber einem normalen Dienstkonto?
3. Warum sollen ungenutzte Konten deaktiviert werden?
4. Welche Rolle hat das integrierte Administratorkonto in einer Domäne, und warum wird es kaum benutzt?

### Modul 5: Dienste und Rollen reduzieren

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Rollen und Features begründet auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende Dienste gegen eine Positivliste prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende abhängige Dienste bei einer Abschaltung berücksichtigen.
  * Nach Abschluss dieses Moduls kann der Lernende Änderungen mit Rückweg durchführen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Rollen und Features: nur installieren, was gebraucht wird; Server Core | 2 |
| 5.2 | Dienste: Starttypen, Konten, abhängige Dienste, Positivliste je Rolle | 2 |
| 5.3 | Praxis: Dienste-Export gegen eine Rolle prüfen (`dienste_pruefen.py`) | 2 |
| 5.4 | Änderungen sicher durchführen: testen, Rückweg, dokumentieren | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Rolle festlegen (Einheit 5.1):** Legen Sie für `srv01` fest, welche Rollen und Features installiert sein dürfen, und welche Alternative Server Core für einen Dateiserver bietet.
2. **Positivliste erstellen (Einheit 5.2):** Erstellen Sie eine Positivliste für die Rolle Dateiserver mit Dienstname, erlaubt, Begründung. Übernehmen Sie `rolle_dateiserver.csv` als Vorlage und ergänzen Sie zwei Zeilen.
3. **Dienste prüfen (Einheit 5.3):** Führen Sie `python3 dienste_pruefen.py dienste_export.csv rolle_dateiserver.csv` aus und erklären Sie jede Meldung. Nennen Sie die Auswirkung, wenn der Dienst abgeschaltet wird.
4. **Änderungsplan (Einheit 5.4):** Schreiben Sie einen Änderungsplan für das Abschalten von Spooler und RemoteRegistry: Vorprüfung, Änderung, Test, Rückweg.

#### Kontrollfragen

1. Warum ist der Druckdienst auf einem Dateiserver ein Risiko?
2. Was ist der Unterschied zwischen „Beenden“ und „Starttyp Deaktiviert“?
3. Warum eine Positivliste statt einer Negativliste?
4. Was ist bei abhängigen Diensten zu prüfen?

### Modul 6: Microsoft Defender und Windows-Firewall

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Schutzfunktionen von Defender beschreiben und Ausschlüsse kritisch beurteilen.
  * Nach Abschluss dieses Moduls kann der Lernende Firewall-Profile und Regeln erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Regelliste auf zu offene Regeln prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln zentral verteilen.
* **Voraussetzungen:** Modul 3; Netzwerk-Grundkenntnisse.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Microsoft Defender Antivirus: Echtzeitschutz, Signaturen, Ausschlüsse, Manipulationsschutz | 2 |
| 6.2 | Windows-Firewall mit erweiterter Sicherheit: Profile, Regeln, Standardrichtung | 2 |
| 6.3 | Praxis: Firewall-Regelliste prüfen (`firewall_pruefen.py`) | 2 |
| 6.4 | Regeln per Gruppenrichtlinie verteilen und überwachen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Defender prüfen (Einheit 6.1):** Beschreiben Sie, wie Sie auf `srv01` den Status von Defender prüfen, wo Signaturen aktualisiert werden und welche Ausschlüsse für den Dateiserver sinnvoll wären. Kennzeichnen Sie, was nicht bestätigt ist.
2. **Profile verstehen (Einheit 6.2):** Erklären Sie die drei Firewall-Profile (Domäne, Privat, Öffentlich) und warum ein Server im Domänenprofil laufen sollte.
3. **Regeln prüfen (Einheit 6.3):** Führen Sie `python3 firewall_pruefen.py firewall_regeln.csv` aus. Erklären Sie die drei Auffälligkeiten und formulieren Sie je eine bessere Regel.
4. **Verteilung planen (Einheit 6.4):** Planen Sie die Verteilung der Firewall-Regeln per Gruppenrichtlinie für die OU der Server inklusive Test und Überwachung der Regeländerungen.

#### Kontrollfragen

1. Warum ist „Test alles erlaubt“ gefährlich?
2. Warum begrenzt man RDP und WinRM auf das Verwaltungsnetz?
3. Warum sind Defender-Ausschlüsse ein Risiko?
4. Wozu dient der Manipulationsschutz?

### Modul 7: Anmeldeschutz: Windows LAPS und lokale Konten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Windows LAPS erklären und von der alten LAPS-Version abgrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Einrichtung in Active Directory beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende abgelaufene oder fehlende LAPS-Kennwörter erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Abruf und Rotation mit Berechtigungen und Protokollierung planen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Das Problem gleicher lokaler Administratorkennwörter; Windows LAPS: Funktionsweise | 2 |
| 7.2 | Einrichtung in Active Directory: Schema, Berechtigungen, Richtlinie, Verschlüsselung | 3 |
| 7.3 | Praxis: Ablauf der LAPS-Kennwörter prüfen (`laps_pruefen.py`) | 2 |
| 7.4 | Kennwörter abrufen und rotieren: Berechtigungen, Protokollierung, Notfall | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Risiko erklären (Einheit 7.1):** Erklären Sie in fünf Sätzen, warum ein gleiches lokales Administratorkennwort auf vielen Rechnern ein Risiko ist (seitliche Bewegung) und wie LAPS es mindert.
2. **Einrichtung beschreiben (Einheit 7.2):** Beschreiben Sie die Schritte zur Einrichtung in Ihrer Testdomäne: Schema erweitern, Rechner dürfen ihr Kennwort schreiben, wer darf lesen, Richtlinie, Verschlüsselung. Nennen Sie die Cmdlets aus der Dokumentation und kennzeichnen Sie, dass Sie sie nicht ausgeführt haben.
3. **Ablauf prüfen (Einheit 7.3):** Führen Sie `python3 laps_pruefen.py computer_export.csv` aus. Erklären Sie die Auffälligkeiten; rechnen Sie ein FILETIME-Beispiel von Hand in ein Datum um (Hinweis: 100-Nanosekunden-Schritte seit 1601).
4. **Abruf regeln (Einheit 7.4):** Legen Sie fest, wer Kennwörter lesen darf, wie der Abruf protokolliert wird und wann nach Gebrauch rotiert wird. Beschreiben Sie, was nach einem Zurücksetzen einer VM auf einen Prüfpunkt passiert.

#### Kontrollfragen

1. Wo speichert Windows LAPS das Kennwort bei Active Directory?
2. Was verlangt die Verschlüsselung der Kennwörter in AD?
3. Warum kann das Zurücksetzen einer VM auf einen Prüfpunkt LAPS stören?
4. Warum soll einem Rechner nie erlaubt sein, Kennwörter zu entschlüsseln?

### Modul 8: Überwachungsrichtlinie und Protokollierung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 9 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende wichtige Unterkategorien der Überwachung nennen.
  * Nach Abschluss dieses Moduls kann der Lernende die wirksame Überwachungsrichtlinie auslesen und bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende Lücken zwischen Soll und Ist erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende zentrale Sammlung als Konzept beschreiben.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Erweiterte Überwachungsrichtlinie: Kategorien, Unterkategorien, Erfolg und Fehler | 2 |
| 8.2 | `auditpol`, Gruppenrichtlinie und wirksame Richtlinie; Ereignisprotokoll: Größe, Aufbewahrung | 3 |
| 8.3 | Praxis: Soll-Ist der Überwachung (`audit_vergleich.py`) | 2 |
| 8.4 | Weiterleitung und zentrale Sammlung: Windows Event Forwarding, Konzept | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Unterkategorien auswählen (Einheit 8.1):** Wählen Sie zehn Unterkategorien (z. B. Anmeldung, Kontosperrung, Benutzerkontenverwaltung, Prozesserstellung) für einen Dateiserver und begründen Sie, ob Erfolg, Fehler oder beides.
2. **Richtlinie auslesen (Einheit 8.2):** Beschreiben Sie, wie Sie die wirksame Richtlinie mit `auditpol /get /category:*` auslesen und wie Sie eine Unterkategorie mit `auditpol /set` einschalten (Syntax laut Dokumentation, nicht ausgeführt).
3. **Lücken finden (Einheit 8.3):** Führen Sie `python3 audit_vergleich.py audit_ist.csv audit_soll.csv` aus. Erklären Sie die fünf Lücken und welche Ereignisse dadurch fehlen.
4. **Sammlung planen (Einheit 8.4):** Skizzieren Sie, wie die Ereignisse von `srv01` und `cl01` zentral gesammelt würden, und legen Sie Größe und Aufbewahrung der Protokolle fest.

#### Kontrollfragen

1. Warum reicht die Überwachung „Anmelden“ allein nicht aus?
2. Warum ist `auditpol` für die wirksame Richtlinie verlässlicher als die Gruppenrichtlinien-Oberfläche?
3. Welche Ereignis-Kennung steht für eine fehlgeschlagene Anmeldung?
4. Warum müssen Ereignisprotokolle geschützt aufbewahrt werden?

### Modul 9: Ereignisse auswerten und Angriffe erkennen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende wichtige Sicherheitsereignisse benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Angriffsmuster in Ereignissen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende einfache Regeln mit Schwellwerten umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlalarme und Meldeweg bedenken.
* **Voraussetzungen:** Modul 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Wichtige Ereignisse: Anmeldungen, Konten, Gruppen, Protokolllöschung | 2 |
| 9.2 | Muster erkennen: Kennwortraten, neue Konten, Rechteausweitung, Spurenverwischung | 2 |
| 9.3 | Praxis: einfache Regeln auf einen Ereignis-Export (`ereignisse_auswerten.py`) | 2 |
| 9.4 | Von der Regel zum Alarm: Schwellwerte, Fehlalarme, Meldeweg | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ereignisse sammeln (Einheit 9.1):** Stellen Sie eine Tabelle mit Ereignis-Kennung, Bedeutung und Verdachtsfall für zehn Ereignisse zusammen und kennzeichnen Sie, welche Kennungen aus der Dokumentation stammen und welche aus Fachwissen.
2. **Muster beschreiben (Einheit 9.2):** Beschreiben Sie für Kennwortraten, Hintertür-Konto und Protokolllöschung je die Ereignisfolge, an der Sie das Muster erkennen.
3. **Regeln anwenden (Einheit 9.3):** Führen Sie `python3 ereignisse_auswerten.py ereignisse.csv` aus. Erklären Sie die drei Treffer und wie Sie jeden prüfen würden.
4. **Alarm entwerfen (Einheit 9.4):** Legen Sie für Regel 1 Schwellwert, Zeitfenster, Ausnahmen (z. B. Dienstkonto mit falschem Kennwort) und Meldeweg fest.

#### Kontrollfragen

1. Warum ist ein Erfolg direkt nach vielen Fehlversuchen verdächtig?
2. Warum ist das Löschen des Überwachungsprotokolls ein starkes Warnsignal?
3. Warum entstehen bei festen Schwellwerten Fehlalarme?
4. Warum ist die Quelladresse wichtiger als der Kontoname?

### Modul 10: Patch-Management

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Update-Wege und ihre Eigenschaften vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Ringplan mit Testgruppe und Wartungsfenstern erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende den Patchstand gegen Fristen auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Ausnahmen und Notfälle regeln.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Update-Quellen und -Wege: Windows Update, WSUS, Windows Update for Business im Überblick | 2 |
| 10.2 | Ringe, Testgruppen, Wartungsfenster, Neustarts | 2 |
| 10.3 | Praxis: Patchstand gegen Fristen prüfen (`patch_stand.py`) | 2 |
| 10.4 | Ausnahmen, Notfall-Patches, Außerbetriebnahme veralteter Systeme | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Wege vergleichen (Einheit 10.1):** Vergleichen Sie Windows Update direkt, WSUS und Windows Update for Business nach Kontrolle, Aufwand und Eignung für das Labor. Kennzeichnen Sie, dass Sie die Dokumentation nicht gelesen haben.
2. **Ringplan (Einheit 10.2):** Entwerfen Sie einen Ringplan (Test, Pilot, Breite) für drei Servergruppen mit Fristen und Wartungsfenstern.
3. **Stand prüfen (Einheit 10.3):** Führen Sie `python3 patch_stand.py patchstand.csv` aus. Erklären Sie die Überfälligkeiten und den ausstehenden Neustart.
4. **Ausnahmen regeln (Einheit 10.4):** Schreiben Sie eine Regel für nicht patchbare Altsysteme (Isolierung, Begründung, Befristung, Freigabe).

#### Kontrollfragen

1. Warum ist ein Patch ohne Neustart manchmal nicht wirksam?
2. Wozu dient eine Testgruppe?
3. Warum haben Domänencontroller und Clients unterschiedliche Fristen?
4. Wie geht man mit einem System um, das keine Updates mehr erhält?

### Modul 11: Fernzugriff und Protokolle: RDP, SMB, NTLM, WinRM

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende RDP, SMB und WinRM sicher konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Folgen von SMB1 und NTLMv1 beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Rechner auf Abweichungen bei Fernzugriff und Protokollen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Verwaltungswege auf das Verwaltungsnetz begrenzen.
* **Voraussetzungen:** Modul 6; Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | RDP mit Netzwerkebenen-Authentifizierung, Gateway, Begrenzung auf das Verwaltungsnetz | 2 |
| 11.2 | SMB: SMB1 abschalten, Signierung, Verschlüsselung; NTLM zurückdrängen (LmCompatibilityLevel) | 3 |
| 11.3 | Praxis: Einstellungen je Rechner prüfen (`remote_pruefen.py`) | 1 |
| 11.4 | WinRM und PowerShell-Remoting: HTTPS, Berechtigungen, protokollierte Sitzungen | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **RDP absichern (Einheit 11.1):** Beschreiben Sie, wie Sie RDP auf `srv01` mit NLA, Beschränkung auf das Verwaltungsnetz und einer eigenen Benutzergruppe absichern.
2. **SMB und NTLM planen (Einheit 11.2):** Legen Sie fest, wie Sie SMB1 abschalten, SMB-Signierung verlangen und NTLM zurückdrängen, und welche alten Anwendungen dabei ausfallen können (Test mit Überwachung).
3. **Einstellungen prüfen (Einheit 11.3):** Führen Sie `python3 remote_pruefen.py remote_einstellungen.csv` aus. Ordnen Sie jeder Abweichung eine Maßnahme zu.
4. **WinRM planen (Einheit 11.4):** Beschreiben Sie, wie WinRM nur über HTTPS und für eine Verwaltungsgruppe erreichbar wird und wie die Sitzungen protokolliert werden (Konzept, nicht ausgeführt).

#### Kontrollfragen

1. Was verhindert die Netzwerkebenen-Authentifizierung bei RDP?
2. Warum ist SMB1 gefährlich?
3. Was bewirkt eine höhere NTLM-Stufe?
4. Warum kann Credential Guard SSO mit NTLMv1 blockieren?

### Modul 12: Zusatzschutz: Credential Guard, Anwendungskontrolle, Secure Boot

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 7 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Credential Guard, seine Voraussetzungen und bekannte Einschränkungen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Anwendungskontrolle als Konzept erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Secure Boot, TPM und BitLocker einordnen.
* **Voraussetzungen:** Module 7 und 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 12.1 | Credential Guard in Grundzügen: Voraussetzungen, Standardaktivierung, Auswirkungen | 3 |
| 12.2 | Anwendungskontrolle (AppLocker, App Control) im Überblick | 2 |
| 12.3 | Secure Boot, TPM, BitLocker im Überblick; Wiederherstellung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Credential Guard bewerten (Einheit 12.1):** Beschreiben Sie, ab welcher Version Credential Guard standardmäßig aktiv ist und welche Auswirkungen auf NTLMv1, MS-CHAP, WDigest und unbeschränkte Delegierung möglich sind. Entscheiden Sie für Ihr Labor, ob Sie es aktivieren, und begründen Sie die Entscheidung.
2. **Anwendungskontrolle beschreiben (Einheit 12.2):** Beschreiben Sie in fünf Sätzen, wie eine Anwendungskontrolle nur freigegebene Programme zulässt, und nennen Sie zwei Betriebsrisiken (Fehlkonfiguration).
3. **Schutzkette skizzieren (Einheit 12.3):** Skizzieren Sie die Kette Secure Boot, TPM, BitLocker und beschreiben Sie, wo der Wiederherstellungsschlüssel aufbewahrt wird.

#### Kontrollfragen

1. Ab welchen Versionen ist Credential Guard laut Dokumentation standardmäßig aktiv?
2. Warum ist Credential Guard auf Domänencontrollern nicht standardmäßig aktiv?
3. Welche Folge kann Credential Guard für Live Migration mit CredSSP haben?
4. Wozu dient der Wiederherstellungsschlüssel von BitLocker?

### Modul 13: Härtung prüfen, dokumentieren und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Ergebnisse mehrerer Prüfungen zu einem Härtungsbericht zusammenfassen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler nach einer Härtung eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende Diagnosewerkzeuge gezielt einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Abschlussdokumentation mit Ausnahmen und Restrisiko schreiben.
* **Voraussetzungen:** Module 1 bis 11.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 13.1 | Gesamtprüfung: Prüfungen zu einem Bericht zusammenfassen (`haertung_bericht.py`) | 3 |
| 13.2 | Fehlersuche: Richtlinie wirkt nicht, Anmeldung nicht möglich, Dienst fällt aus, Firewall blockiert | 3 |
| 13.3 | Diagnosewerkzeuge: Ereignisanzeige, `gpresult`, `Test-NetConnection`, Netzwerkmitschnitt | 2 |
| 13.4 | Abschlussdokumentation und Übergabe | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bericht erzeugen (Einheit 13.1):** Führen Sie `python3 haertung_bericht.py` aus und ergänzen Sie für jeden Bereich Maßnahme, Verantwortlichen und Frist oder begründete Ausnahme.
2. **Fehler eingrenzen (Einheit 13.2):** Nach einer Härtung kann sich `cl01` nicht mehr per RDP an `srv01` anmelden. Beschreiben Sie in Schritten, wie Sie die Ursache eingrenzen (Netz, Firewall, NLA, Gruppe, Richtlinie, Ereignisprotokoll).
3. **Diagnose üben (Einheit 13.3):** Legen Sie fest, mit welchem Werkzeug Sie welche Frage klären (Erreichbarkeit, Richtlinie, Ereignis, Dienststatus). Kennzeichnen Sie, welche Werkzeuge Sie nicht ausgeführt haben.
4. **Abschlussdokument (Einheit 13.4):** Schreiben Sie eine Abschlussdokumentation von höchstens zwei Seiten: Umfang, Baseline, Abweichungen und Ausnahmen, Prüfungen, Restrisiko, nächste Schritte.

#### Kontrollfragen

1. Warum ist ein Bericht ohne Maßnahmen, Verantwortliche und Fristen wenig wert?
2. Warum prüft man nach einer Härtung die Anmeldung von einem zweiten Rechner aus?
3. Welche Rolle hat der Rückweg bei Änderungen an Richtlinien?
4. Was gehört in den Abschnitt „Restrisiko“?
