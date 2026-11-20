# Lehrplan: Intune und Autopilot

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen, Windows-11-Grundlagen und Entra-ID-Grundlagen (Benutzer, Gruppen, Bedingter Zugriff im Überblick) |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Microsoft Intune, Windows Autopilot, Windows 11: Geräteverwaltung (MDM und MAM), Registrierung und Einschränkungen, Windows Autopilot (Hardware-Hash-Datei, Profile, Modi), Konfigurationsprofile, Compliance-Richtlinien, App-Bereitstellung, Updates, Zuweisungen und Filter, Fehlersuche, Einordnung gegenüber Gruppenrichtlinien |
| **Thematische Abgrenzung (Out of Scope)** | Entra ID und Bedingter Zugriff im Kurs „Entra ID und Hybrid-Identität“, Azure-Ressourcen im Kurs „Azure Administration“. **Intune, Autopilot und Windows wurden nicht ausgeführt:** Es gab weder einen Mandanten noch ein Gerät noch eine Anmeldung. **Echt** sind nur (1) die Prüfung, ob Befehle und Parameter in der installierten **Azure CLI 2.93.0** existieren (`az … --help`, offline), (2) die **Prüfung der Autopilot-CSV** nach den in Microsoft Learn (Suchauszug) genannten Regeln, (3) **SHA-256-Prüfsummen** und (4) das Lesen von JSON-Dateien. Registrierung, Profile, Compliance, Zuweisungen und Filter sind ein **Lernmodell in Python** (`intunesim.py`). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Geräteverwaltung: MDM, MAM und Registrierungswege | 1 | 12 |
| 2 | Registrierung: Lizenz, MDM-Benutzerbereich, Einschränkungen und Limit | 1 | 14 |
| 3 | Windows Autopilot: Hardware-Hash-Datei, Profile und Modi | 1 | 14 |
| 4 | Konfigurationsprofile, Konflikte und Gruppenrichtlinien | 1 | 12 |
| 5 | Compliance-Richtlinien und Aktionen bei Nichtkonformität | 1 | 12 |
| 6 | App-Bereitstellung: Absichten, Erkennungsregeln und Prüfsumme | 1 | 14 |
| 7 | Windows-Updates: Ringe, Zurückstellung und Frist | 2 | 8 |
| 8 | Zuweisungen, Filter, Fehlersuche und Abschluss | 1 | 14 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Windows-Updates). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 92 UE. **Achtung:** Das Thema „Updates“ steckt ausschließlich in Modul 7; ohne dieses Modul fehlt es vollständig. Kein anderes Modul setzt Modul 7 voraus.

### 2. Quellen

**Gelesen (Microsoft Learn, Suchauszüge vom 20.11.2026, nicht ganze Seiten):** Lizenzen für Intune und Autopilot (u. a. Microsoft 365 Business Premium, F1/F3, E3/E5, EMS E3/E5, Intune for Education; Lizenzen müssen Benutzern zugewiesen sein), Regeln für die Autopilot-CSV (Kopfzeile `Device Serial Number,Windows Product ID,Hardware Hash,Group Tag,Assigned User`, keine zusätzlichen Spalten, keine Anführungszeichen, nur ANSI, Groß-/Kleinschreibung zählt, bis 500 Zeilen, Seriennummer und Hash erforderlich, ungültiger UPN kann das Gerät unbrauchbar machen), Autopilot: selbstbereitstellender Modus nicht für hybrid eingebundene Geräte, Nichtkonformitätsaktionen (Standard „als nicht konform markieren“ mit 0 Tagen, nicht entfernbar; weitere Aktionen; Zeitplan 0 bis 365 Tage), Zuweisungsfilter (Vorrang Exclude vor Kein Filter vor Include, ODER-Logik bei gleichem Modus, App-Absichten Verfügbar/Erforderlich/Deinstallieren, mehrere Absichten für dieselbe Gruppe nicht möglich) sowie Registrierungseinschränkungen und MDM-Benutzerbereich. **Lizenz- und Regelaussagen stützen sich nur auf diese Auszüge; Pläne ändern sich, vor der Anwendung prüfen.**

**Nicht gelesen und nicht bestätigt:** Verhalten bei widersprüchlichen Profilen im echten Intune, Erkennungsregeln und Verpacken von Win32-Apps, Einstellungen und Grenzen von Update-Ringen, Gerätelimit (der Wert 3 im Modell ist **erfunden**), die Wirkung der Aktionen im Detail, Gruppenrichtlinien-Vorrang bei Mischbetrieb. Portalmenüs sind **nicht bestätigt** (nicht geprüft, daher im Kurs nicht beschrieben).

**Getestet mit (Ubuntu 24.04, Cloud-Container):** Python 3.13, Azure CLI 2.93.0 (pip, nur Hilfetexte), Modell `intunesim.py`. **Nicht ausgeführt:** Intune-Mandant, Windows, Hyper-V, PowerShell, `Get-WindowsAutopilotInfo`.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Intune`, `10.91.0.0/24`; Name und Netz angenommen).

**VM 1:** `win11-1` (**erforderlich**, `10.91.0.21`): Windows-11-VM für Registrierung und Autopilot-Versuche (Name angenommen).

**Internetphase:** Registrierung und Anmeldung beim Mandanten brauchen Internetzugang.

**Test-Tenant:** zusätzlich ein Test-Tenant mit Intune-Lizenz (kein produktiver Tenant). Laufzeit und Kosten vorab prüfen; Lizenzpläne mit Stand prüfen.

**Prüfpunkt (Checkpoint):** Vor Modul 3 einen Prüfpunkt der VM anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux mit dem Modell `intunesim.py` und arbeiten unter `/tmp/p29`; sie brauchen weder VM noch Mandanten. Das Labor wurde **nicht** aufgebaut.

## B. Detaillierter Modulaufbau

### Modul 1: Geräteverwaltung: MDM, MAM und Registrierungswege

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende MDM und MAM unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende zu Betriebssystem, Besitz und Gerätezustand einen Registrierungsweg wählen.
  * Nach Abschluss dieses Moduls kann der Lernende Lizenzabhängigkeiten mit Stand nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Befehle für diese Aufgaben benennen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | MDM oder MAM | 4 |
| 1.2 | Registrierungsweg | 4 |
| 1.3 | Lizenzen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **MDM oder MAM (Einheit 1.1):** Führen Sie `bash enrollment.sh` aus. Erklären Sie Schritt 4: Wann wählt man MAM statt MDM?
2. **Registrierungsweg (Einheit 1.2):** Erklären Sie Schritt 3: Warum unterscheiden sich die Antworten für neue und vorhandene Firmengeräte?
3. **Lizenzen (Einheit 1.3):** Lesen Sie Schritt 2: Was muss trotz Microsoft-365-Abonnement zusätzlich geschehen?

#### Kontrollfragen

1. Was empfiehlt das Modell für ein neues Firmengerät mit Windows?
2. Und für ein vorhandenes Firmengerät?
3. Was gilt für ein privates Windows-Gerät?
4. Was muss bei Lizenzen beachtet werden?

### Modul 2: Registrierung: Lizenz, MDM-Benutzerbereich, Einschränkungen und Limit

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Ursachen fehlgeschlagener Registrierungen aus Lizenz, Bereich und Einschränkung ableiten.
  * Nach Abschluss dieses Moduls kann der Lernende private Windows-Geräte per Einschränkung sperren.
  * Nach Abschluss dieses Moduls kann der Lernende ein Gerätelimit einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Ursachen beheben und erneut prüfen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Fehlgeschlagene Registrierung | 6 |
| 2.2 | Einschränkung | 4 |
| 2.3 | Limit und Behebung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Fehlgeschlagene Registrierung (Einheit 2.1):** Führen Sie `bash einschraenkungen.sh` aus. Erklären Sie Schritt 2: Warum scheitern `ben` und `cem`, und warum gelingt `ana`?
2. **Einschränkung (Einheit 2.2):** Erklären Sie Schritt 3: Was ändert die Sperre privater Windows-Geräte?
3. **Limit und Behebung (Einheit 2.3):** Erklären Sie Schritt 4 und 5: Warum scheitert das dritte Firmengerät von `ana`, und wie werden `ben` und `cem` behoben?

#### Kontrollfragen

1. Warum scheitert `ben`?
2. Warum scheitert `cem`?
3. Was blockiert nach Schritt 3 das zweite private Gerät?
4. Ist das Limit von 3 Geräten ein echter Wert?

### Modul 3: Windows Autopilot: Hardware-Hash-Datei, Profile und Modi

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Hardware-Hash-Datei nach den dokumentierten Regeln prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Dateifehler erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Profile über Gruppen-Tags zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Einschränkungen von Modi nennen.
* **Voraussetzungen:** Modul 1; Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Gültige und fehlerhafte Dateien | 6 |
| 3.2 | Import und Profile | 4 |
| 3.3 | Modi | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Gültige und fehlerhafte Dateien (Einheit 3.1):** Führen Sie `bash autopilot.sh` aus. Erklären Sie die Schritte 2 und 3: Welche Regel verletzt jede der vier fehlerhaften Dateien?
2. **Import und Profile (Einheit 3.2):** Erklären Sie Schritt 4: Wie wird ein Gerät einem Profil zugeordnet, und was geschieht bei `SN-0003` und `SN-9999`?
3. **Modi (Einheit 3.3):** Erklären Sie Schritt 5: Warum wird das Profil `profil-hybrid` abgelehnt?

#### Kontrollfragen

1. Warum ist `falsch-kopf.csv` fehlerhaft?
2. Was ist an `falsch-bom.csv` falsch?
3. Was geschieht bei `SN-0003`?
4. Warum scheitert selbstbereitstellend mit hybrider Einbindung?

### Modul 4: Konfigurationsprofile, Konflikte und Gruppenrichtlinien

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Einstellungen aus mehreren Profilen zusammenführen.
  * Nach Abschluss dieses Moduls kann der Lernende Konflikte erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Intune-Profile und Gruppenrichtlinien einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen des Modells benennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Profile ohne Widerspruch | 4 |
| 4.2 | Konflikt | 4 |
| 4.3 | Einordnung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Profile ohne Widerspruch (Einheit 4.1):** Führen Sie `bash profile.sh` aus. Erklären Sie Schritt 2: Warum ist der gleiche Wert für die Bildschirmsperre kein Konflikt?
2. **Konflikt (Einheit 4.2):** Erklären Sie Schritt 3: Welche Einstellung ist im Konflikt, und was tut das Modell damit?
3. **Einordnung (Einheit 4.3):** Lesen Sie Schritt 4: Welche Unterschiede nennt die Tabelle zwischen Gruppenrichtlinien und Konfigurationsprofilen?

#### Kontrollfragen

1. Wie viele Einstellungen und Konflikte gibt es mit zwei Profilen?
2. Welche Einstellung ist im Konflikt?
3. Wird der Konfliktwert im Modell angewendet?
4. Wo liegt die Verwaltung bei Gruppenrichtlinien, wo bei Intune?

### Modul 5: Compliance-Richtlinien und Aktionen bei Nichtkonformität

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Geräte gegen eine Richtlinie auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Aktionen und Zeitplan lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Verbindung zum Bedingten Zugriff erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Karenzzeit wirken sehen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Auswertung | 4 |
| 5.2 | Bedingter Zugriff | 4 |
| 5.3 | Karenzzeit | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auswertung (Einheit 5.1):** Führen Sie `bash compliance.sh` aus. Erklären Sie Schritt 2: Welche Regeln verletzt `PC-ALT`?
2. **Bedingter Zugriff (Einheit 5.2):** Erklären Sie Schritt 3: Wann wird der Zugriff gesperrt?
3. **Karenzzeit (Einheit 5.3):** Erklären Sie Schritt 4: Was ändert die Karenzzeit von 3 Tagen?

#### Kontrollfragen

1. Ist `PC-GUT` konform?
2. Was verletzt `PC-ALT`?
3. Ab wann wird der Zugriff in Schritt 3 gesperrt?
4. Ab wann in Schritt 4?

### Modul 6: App-Bereitstellung: Absichten, Erkennungsregeln und Prüfsumme

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Integrität eines Pakets mit SHA-256 prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Absichten Verfügbar, Erforderlich und Deinstallieren zuweisen.
  * Nach Abschluss dieses Moduls kann der Lernende Erkennungsregeln auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Folgen fehlender Erkennung erklären.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Prüfsumme | 6 |
| 6.2 | Absichten | 4 |
| 6.3 | Erkennung | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prüfsumme (Einheit 6.1):** Führen Sie `bash apps.sh` aus. Erklären Sie Schritt 1: Warum weicht `paket2.bin` ab?
2. **Absichten (Einheit 6.2):** Erklären Sie Schritt 2: Warum wird die zweite Zuweisung an `technik` abgelehnt?
3. **Erkennung (Einheit 6.3):** Erklären Sie Schritt 3: Wann gilt die App als installiert?

#### Kontrollfragen

1. Was zeigt der SHA-256-Vergleich bei `paket.bin`?
2. Und bei `paket2.bin`?
3. Warum scheitert `technik:required` plus `technik:available`?
4. Wann gilt die App auf „Gerät alt“ als nicht installiert?

### Modul 7: Windows-Updates: Ringe, Zurückstellung und Frist

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zurückstellung und Frist unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Zeitpunkte für mehrere Ringe berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung einer Pause erklären.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Drei Ringe | 4 |
| 7.2 | Pause | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Drei Ringe (Einheit 7.1):** Führen Sie `bash updates.sh` aus. Erklären Sie Schritt 2: Wann wird jedem Ring das Update angeboten und wann spätestens installiert?
2. **Pause (Einheit 7.2):** Erklären Sie Schritt 3: Was ändert eine Pause von 10 Tagen?

#### Kontrollfragen

1. Wann gilt die Installation im Ring „Breit“ spätestens?
2. Was bewirkt eine Zurückstellung?
3. Was bewirkt die Frist?

### Modul 8: Zuweisungen, Filter, Fehlersuche und Abschluss

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zuweisungen mit Filtern auswerten (Vorrang, ODER-Logik).
  * Nach Abschluss dieses Moduls kann der Lernende Gruppenausschlüsse berücksichtigen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlersuche entlang der Kette durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende die Kette von Registrierung bis Wirkung zusammenfassen.
* **Voraussetzungen:** Module 2 bis 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Filter und Vorrang | 6 |
| 8.2 | Gruppenausschluss | 4 |
| 8.3 | Fehlersuche | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Filter und Vorrang (Einheit 8.1):** Führen Sie `bash zuweisungen.sh` aus. Erklären Sie die Schritte 2 bis 4: Wann wird die Richtlinie angewendet, und welcher Modus hat Vorrang?
2. **Gruppenausschluss (Einheit 8.2):** Erklären Sie Schritt 5: Warum wird `PC-B` ausgeschlossen, `PC-A` aber nicht?
3. **Fehlersuche (Einheit 8.3):** Erklären Sie Schritt 6: Was ist bei `PC-C`, `PC-D` und `PC-E` jeweils die erste Ursache?

#### Kontrollfragen

1. Wird die Richtlinie in Schritt 2 auf `PC-A` und `PC-B` angewendet?
2. Welcher Modus hat Vorrang?
3. Was gilt bei zwei Include-Filtern?
4. Was ist bei `PC-D` die erste Ursache?
