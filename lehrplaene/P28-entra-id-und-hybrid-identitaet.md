# Lehrplan: Entra ID und Hybrid-Identität

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Active-Directory-Grundlagen |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Microsoft Entra ID, Entra Connect, Windows Server Active Directory: Aufbau von Mandant und Domänen, Benutzer, Gruppen, Geräte und Rollen, Synchronisation (Passwort-Hash-Synchronisation, Pass-through, Federation im Überblick), Hybrid Join, Mehrfaktor-Authentifizierung, Bedingter Zugriff (Lizenzabhängigkeit), Privileged Identity Management im Überblick, Anwendungsregistrierungen und Token |
| **Thematische Abgrenzung (Out of Scope)** | M365 Governance und Active Directory sind vorhandene Lehrpläne; Azure-Ressourcen im Kurs „Azure Administration“, Geräteverwaltung im Kurs „Intune und Autopilot“. **Entra ID, Entra Connect und Active Directory wurden nicht ausgeführt:** Es gab weder einen Mandanten noch einen Domänencontroller noch eine Anmeldung. **Echt gerechnet** sind nur (1) die Prüfung, ob Befehle und Parameter in der installierten **Azure CLI 2.93.0** existieren (`az … --help`, offline), (2) die **Einmalkennwörter (TOTP) nach RFC 6238**, geprüft gegen die sechs Testwerte der RFC, und (3) **Token mit RS256-Signatur** (PyJWT 2.15.0, cryptography 50.0.1). Mandant, Synchronisation, Geräte, Bedingter Zugriff und PIM sind ein **Lernmodell in Python** (`entrasim.py`). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Aufbau von Entra ID: Mandant, Domänen und Benutzer | 1 | 12 |
| 2 | Gruppen, dynamische Mitgliedschaft und Verwaltungsrollen | 1 | 14 |
| 3 | Entra Connect: Synchronisation und Anmeldemethoden | 1 | 14 |
| 4 | Geräte: Registrierung, Einbindung und Hybrid Join | 1 | 12 |
| 5 | Mehrfaktor-Authentifizierung und Einmalkennwörter | 1 | 12 |
| 6 | Bedingter Zugriff | 1 | 14 |
| 7 | Privileged Identity Management im Überblick | 2 | 8 |
| 8 | Anwendungsregistrierungen, Token und Abschlussprojekt | 1 | 14 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Privileged Identity Management im Überblick). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 92 UE. **Achtung:** Das Thema „Privileged Identity Management im Überblick“ steckt ausschließlich in Modul 7; ohne dieses Modul fehlt es vollständig. Kein anderes Modul setzt Modul 7 voraus.

### 2. Quellen

**Gelesen (Microsoft Learn, Suchauszüge vom 20.11.2026, nicht ganze Seiten):** „Microsoft Entra licensing“ (Free, P1, P2, Governance, Suite; Entra Connect kostenlos und im Azure-Abonnement enthalten; Connect Health erfordert P1), „What is Conditional Access?“ und „Plan a Conditional Access deployment“ (Bedingter Zugriff erfordert P1; risikobasierte Richtlinien erfordern P2; Sicherheitsstandards für alle Kunden verfügbar), „Features and licenses for Microsoft Entra multifactor authentication“, „Microsoft Entra ID Governance licensing fundamentals“ (PIM in P2, Governance und Suite) und eine Seite zu Windows Autopilot (selbstbereitstellender Modus nicht für hybrid eingebundene Geräte). **Lizenzaussagen in den Übungen stützen sich nur auf diese Auszüge; Pläne ändern sich, vor der Anwendung prüfen.** Weitere Seiten der Entra-Dokumentation wurden **nicht** gelesen.

**Nicht gelesen und nicht bestätigt:** Verhalten von Entra Connect (Filter, UPN-Rückfall auf die Standarddomäne, Quellanker), die Auswertung dynamischer Gruppen, Einbindungsarten und `dsregcmd`, Rollenberechtigungen (die Zuordnung im Modell ist **erfunden**), Grenzen im Modell (Aktivierungsdauer 480 Minuten, Geheimnis 730 Tage) und die Gestaltung der Token von Entra ID. Portalmenüs sind **nicht bestätigt** (nicht geprüft, daher im Kurs nicht beschrieben).

**Getestet mit (Ubuntu 24.04, Cloud-Container):** Python 3.13, PyJWT 2.15.0, cryptography 50.0.1, Azure CLI 2.93.0 (pip, nur Hilfetexte), Modell `entrasim.py`. **Nicht ausgeführt:** Entra-Mandant, Entra Connect, Windows Server, Active Directory, `dsregcmd`, PowerShell, Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Entra`, `10.90.0.0/24`).

**VM 1:** `dc1` (**erforderlich**, `10.90.0.10`): Windows Server mit Active Directory (Domäne `firma.lab`).

**VM 2:** `client1` (**erforderlich**, `10.90.0.21`): Windows-Client für die hybride Einbindung.

**Internetphase:** Entra Connect und die Anmeldung beim Mandanten brauchen vorübergehend Internetzugang; danach wird er entfernt.

**Test-Tenant:** zusätzlich ein Test-Tenant (Microsoft-365-Entwickler- oder Testzugang), **kein produktiver Tenant**. Laufzeit und mögliche Kosten vorab prüfen (nicht geprüft). Lizenzabhängigkeit der Funktionen (Free, P1, P2) mit Stand prüfen.

**Prüfpunkt (Checkpoint):** Vor Modul 3 und Modul 4 von beiden VMs einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte laufen unter Linux mit dem Modell `entrasim.py` und arbeiten unter `/tmp/p28`; sie brauchen weder VMs noch Mandanten. Im Labor ersetzt man die Modell-Befehle durch die echten Werkzeuge (nicht geprüft).

## B. Detaillierter Modulaufbau

### Modul 1: Aufbau von Entra ID: Mandant, Domänen und Benutzer

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Mandanten und seine Domänen beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum nur verifizierte Domänen als UPN-Suffix taugen.
  * Nach Abschluss dieses Moduls kann der Lernende Benutzer anlegen und die Quelle (Cloud oder Synchronisation) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Befehle für diese Aufgaben benennen.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Mandant und Domänen | 4 |
| 1.2 | Domäne verifizieren | 4 |
| 1.3 | Benutzerliste | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Mandant und Domänen (Einheit 1.1):** Führen Sie `bash aufbau.sh` aus. Erklären Sie Schritt 2 und 3: Welche Domänen hat der Mandant, und warum scheitert `cem@muster-lab.example`?
2. **Domäne verifizieren (Einheit 1.2):** Erklären Sie Schritt 4: Warum scheitert die erste Verifizierung, und was ändert sich danach?
3. **Benutzerliste (Einheit 1.3):** Lesen Sie Schritt 5: Welche Angaben zeigt die Liste, und was bedeutet „Quelle Cloud“?

#### Kontrollfragen

1. Welche Domänen gibt es anfangs?
2. Warum scheitert `cem@muster-lab.example` zuerst?
3. Was zeigt der falsche TXT-Eintrag?
4. Was bedeutet „Quelle Cloud“?

### Modul 2: Gruppen, dynamische Mitgliedschaft und Verwaltungsrollen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende zugewiesene und dynamische Gruppen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine Regel für dynamische Gruppen lesen und auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Rollen mit kleinster Berechtigung vergeben.
  * Nach Abschluss dieses Moduls kann der Lernende Regelfehler erkennen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Zugewiesen oder dynamisch | 6 |
| 2.2 | Regeln | 4 |
| 2.3 | Rollen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zugewiesen oder dynamisch (Einheit 2.1):** Führen Sie `bash gruppen.sh` aus. Erklären Sie Schritt 3: Warum kann man zu `vertrieb-dynamisch` niemanden von Hand hinzufügen?
2. **Regeln (Einheit 2.2):** Erklären Sie Schritt 4: Welche Mitglieder haben die drei Regeln, und was zeigt der Tippfehler?
3. **Rollen (Einheit 2.3):** Erklären Sie Schritt 5: Was darf `ben` mit der Rolle „Helpdesk Administrator“, und warum darf `ana` nichts verwalten?

#### Kontrollfragen

1. Wer ist in `vertrieb-dynamisch`?
2. Welche Mitglieder hat `ana-oder-technik`?
3. Was meldet die Regel `user.department = Vertrieb`?
4. Was darf `ben` als Helpdesk Administrator?

### Modul 3: Entra Connect: Synchronisation und Anmeldemethoden

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Synchronisationsbereich (OUs) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende den Rückfall bei nicht verifiziertem UPN-Suffix erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Delta-Synchronisation und Löschen nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende PHS, PTA und Federation bei Ausfall der lokalen Umgebung vergleichen.
* **Voraussetzungen:** Modul 1; Active-Directory-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Bereich und UPN | 6 |
| 3.2 | Änderungen | 4 |
| 3.3 | Anmeldemethoden | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bereich und UPN (Einheit 3.1):** Führen Sie `bash connect.sh` aus. Erklären Sie Schritt 2 und 3: Welche Benutzer werden synchronisiert, und was geschieht mit den UPN-Suffixen `firma.local` und `muster-lab.example`?
2. **Änderungen (Einheit 3.2):** Erklären Sie Schritt 4 und 5: Was passiert nach der Verifizierung und der Änderung im AD, und warum verschwindet `ana`?
3. **Anmeldemethoden (Einheit 3.3):** Erklären Sie Schritt 6: Welche Methode funktioniert bei Ausfall der lokalen Umgebung, und warum?

#### Kontrollfragen

1. Welche Benutzer sind außerhalb des Bereichs?
2. Welcher Cloud-UPN entsteht für `ben@firma.local`?
3. Was bewirkt `ad del ana` bei der nächsten Synchronisation?
4. Welche Methode überlebt den Ausfall der lokalen Umgebung?

### Modul 4: Geräte: Registrierung, Einbindung und Hybrid Join

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Einbindungsarten unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Ausgabe von `dsregcmd /status` einordnen (hier nachgebildet).
  * Nach Abschluss dieses Moduls kann der Lernende Voraussetzungen der hybriden Einbindung nennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Einschränkung zu Autopilot benennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Einbindungsarten | 4 |
| 4.2 | Voraussetzungen | 4 |
| 4.3 | Autopilot | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einbindungsarten (Einheit 4.1):** Führen Sie `bash hybrid.sh` aus. Erklären Sie Schritt 2: Welche Einbindung ergibt sich aus den vier Beispielen?
2. **Voraussetzungen (Einheit 4.2):** Erklären Sie Schritt 3: Was fehlt jeweils bei den beiden fehlgeschlagenen Fällen?
3. **Autopilot (Einheit 4.3):** Erklären Sie Schritt 4: Welche Aussage stammt aus gelesener Dokumentation, und welche nicht?

#### Kontrollfragen

1. Wann ist ein Gerät „Entra hybrid eingebunden“?
2. Was bedeutet `AzureAdJoined=NO` und `DomainJoined=YES`?
3. Was fehlt bei `--connect no`?
4. Wofür gilt der selbstbereitstellende Modus von Autopilot nicht?

### Modul 5: Mehrfaktor-Authentifizierung und Einmalkennwörter

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip zeitbasierter Einmalkennwörter (TOTP) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen Code mit Toleranzfenster prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherheitsstandards und Bedingten Zugriff nach Lizenz einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rechnung gegen die Testwerte der RFC nachvollziehen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Testwerte | 4 |
| 5.2 | Codes und Zeit | 4 |
| 5.3 | Toleranz | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Testwerte (Einheit 5.1):** Führen Sie `bash mfa.sh` aus. Erklären Sie Schritt 2: Was beweist die Übereinstimmung mit den RFC-Werten?
2. **Codes und Zeit (Einheit 5.2):** Erklären Sie Schritt 3: Warum ändern sich die Codes alle 30 Sekunden?
3. **Toleranz (Einheit 5.3):** Erklären Sie Schritt 4: Warum wird derselbe Code bei Zeit 1030 mit und ohne Fenster unterschiedlich beurteilt?

#### Kontrollfragen

1. Was beweist Schritt 2?
2. Wann ändert sich der Code?
3. Warum wird der Code bei Zeit 1030 ohne Fenster abgelehnt?
4. Welche Lizenz braucht Bedingter Zugriff für MFA nach Bedarf?

### Modul 6: Bedingter Zugriff

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zuweisungen, Bedingungen und Zugriffssteuerung einer Richtlinie lesen.
  * Nach Abschluss dieses Moduls kann der Lernende die Auswertung mehrerer Richtlinien erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Ausnahmen für Notfallkonten begründen.
  * Nach Abschluss dieses Moduls kann der Lernende die Lizenzabhängigkeit (P1, P2) nennen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Richtlinien lesen | 6 |
| 6.2 | Sperre und Ausnahme | 4 |
| 6.3 | Lizenz | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Richtlinien lesen (Einheit 6.1):** Führen Sie `bash bedingter-zugriff.sh` aus. Erklären Sie Schritt 2 und 3: Welche Richtlinien greifen für `ana` und für `dora` als Mitglied von `admins`?
2. **Sperre und Ausnahme (Einheit 6.2):** Erklären Sie Schritt 4: Warum ist der Zugriff unter Linux gesperrt, und warum hat `notfall` Zugriff?
3. **Lizenz (Einheit 6.3):** Erklären Sie Schritt 5 und 6: Was ändert sich mit P1, P2 und ohne Lizenz?

#### Kontrollfragen

1. Welche Richtlinie sperrt Linux?
2. Was bedeutet „nur Bericht“?
3. Warum greift für `notfall` nichts Wirksames?
4. Was braucht die Risikobedingung?

### Modul 7: Privileged Identity Management im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende berechtigte (eligible) und aktive Zuweisungen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Aktivierung mit Begründung und begrenzter Dauer erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Genehmigung bei Aktivierung beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die Lizenzabhängigkeit (P2) nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Eligible und aktiv | 4 |
| 7.2 | Aktivierung | 2 |
| 7.3 | Genehmigung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eligible und aktiv (Einheit 7.1):** Führen Sie `bash pim.sh` aus. Erklären Sie Schritt 3: Was unterscheidet `ana` und `ben`?
2. **Aktivierung (Einheit 7.2):** Erklären Sie Schritt 4 und 5: Wie lange ist die Rolle aktiv, und warum scheitern die drei Fehlerfälle?
3. **Genehmigung (Einheit 7.3):** Erklären Sie Schritt 6: Was ändert die Genehmigung?

#### Kontrollfragen

1. Wann ist die Rolle von `ana` aktiv?
2. Warum scheitert die Aktivierung für 600 Minuten?
3. Warum scheitert die Aktivierung von `ben`?
4. Welche Lizenz braucht PIM?

### Modul 8: Anwendungsregistrierungen, Token und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Registrierung einer Anwendung (Umleitung, Geheimnis, Rechte) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende delegierte Rechte und Anwendungsrechte unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Teile eines Tokens und die Prüfung (Signatur, Aussteller, Zielgruppe, Zeit) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Kette von Registrierung bis Prüfung zusammenfassen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Registrierung | 6 |
| 8.2 | Rechte | 4 |
| 8.3 | Token | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Registrierung (Einheit 8.1):** Führen Sie `bash anwendungen.sh` aus. Erklären Sie Schritt 2: Warum werden `unsicher` und `langlebig` abgelehnt?
2. **Rechte (Einheit 8.2):** Erklären Sie Schritt 3: Wann wirkt das Anwendungsrecht `Mail.Read`?
3. **Token (Einheit 8.3):** Erklären Sie Schritt 4: Warum ist jede der sechs Prüfungen nötig, und was ist an den Nutzdaten nicht geschützt?

#### Kontrollfragen

1. Warum wird `http://berichte.example.test/…` abgelehnt?
2. Wann wirkt `Mail.Read` als Anwendungsrecht?
3. Warum ist die veränderte Nutzlast ungültig?
4. Sind die Nutzdaten des Tokens verschlüsselt?
