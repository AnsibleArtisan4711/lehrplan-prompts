# Lehrplan: Exchange Online Administration

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Microsoft-365-Grundlagen |
| **Gesamtumfang** | 10 Module, 110 UE (zu 45 Minuten; 82,5 Stunden) |
| **Fokus-Technologien** | Exchange Online in einem Microsoft-365-Test-Tenant (kein produktiver Tenant); Verwaltung über das Exchange Admin Center und PowerShell |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Microsoft-365-Governance und Entra ID in eigenen Kursen, SPF, DKIM und DMARC im Kurs „E-Mail-Authentifizierung: SPF, DKIM und DMARC“, Postfix und Dovecot im Kurs „Mailserver mit Postfix und Dovecot“. Nicht behandelt: Exchange Server (lokal) im Betrieb, Microsoft Defender for Office 365 über das Überblickswissen hinaus, Teams-Telefonie, Datenverlustprävention im Detail, eDiscovery, Rechtsfragen zur Aufbewahrung |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Überblick, Lizenzen und Grenzwerte | 1 | 10 |
| 2 | Postfachtypen und Massenanlage | 1 | 10 |
| 3 | Empfänger, Gruppen und Verteilerlisten | 1 | 12 |
| 4 | Mailfluss, akzeptierte Domains und Connectoren | 1 | 12 |
| 5 | Transportregeln (Mailflussregeln) | 1 | 12 |
| 6 | Schutz vor Spam und Schadsoftware (Exchange Online Protection) | 1 | 12 |
| 7 | Aufbewahrung und Compliance im Überblick | 1 | 10 |
| 8 | Migration und Hybrid im Überblick | 2 | 10 |
| 9 | Verwaltung mit PowerShell | 1 | 12 |
| 10 | Nachrichtenverfolgung und Fehlersuche | 1 | 10 |
| **Gesamt** | 10 Module | 9 × Priorität 1, 1 × Priorität 2 | **110** |

**Priorität 1** (Pflicht) sind die Module 1 bis 7, 9 und 10; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 8 (Migration und Hybrid im Überblick). Fällt Modul 8 weg, verringert sich der Gesamtumfang auf 100 UE; kein Pflichtmodul setzt Modul 8 voraus.

### 2. Quellen

**Gelesen (mit Abrufdatum 20.11.2026):** Seiten der Microsoft-Learn-Dokumentation zu den Grenzwerten von Exchange Online (Nachrichtengröße: Standard 35 MB laut Dokumentation, einstellbar 1 bis 150 MB, Zuschlag durch Codierung etwa ein Drittel; Postfachgrößen: Exchange Online Plan 1 bzw. Microsoft 365 E1 50 GB, Plan 2/E3/E5/Business 100 GB, F3/Kiosk 2 GB; Empfängerlimit je Nachricht einstellbar 1 bis 1000), zur Ankündigung zum Auslaufen der Basisauthentifizierung bei SMTP AUTH (Zeitplan **nicht bestätigt**; eine neuere Aktualisierung wurde nicht gelesen) sowie zu den Testmöglichkeiten (Microsoft 365 Developer Program: Sandbox nur für berechtigte Mitglieder; ein 30-Tage-Test von Microsoft 365 E3, danach kostenpflichtig). Lizenz- und Funktionsstand können sich ändern.

**Nicht gelesen:** die Dokumentation zu Exchange Online Protection, Mailfluss-Regeln, Aufbewahrung, Migration und PowerShell-Befehlen. Alle Skripte dieser Reihe sind **Python-Modelle mit erfundenen Daten**, die lokal im Container liefen; es wurde **kein** Exchange-Online-Tenant und **keine** PowerShell verwendet. Befehlsnamen, Portalmenüs und Standardwerte außerhalb der oben genannten Grenzwerte sind **nicht bestätigt**.

### 3. Labor-Setup & Rahmenbedingungen

**Testumgebung:** ein **Microsoft-365-Test-Tenant** (kein produktiver Tenant). Mögliche Zugänge laut Dokumentation (Stand 20.11.2026): das Microsoft 365 Developer Program (Sandbox mit E5-Lizenzen, nur für berechtigte Mitglieder, begrenzte Lizenzzahl und Laufzeit) oder eine Testversion von Microsoft 365 E3 (30 Tage, danach kostenpflichtig, wenn nicht gekündigt). **Laufzeit und mögliche Kosten sind vorab zu prüfen.** Es werden nur Test-Domains und Test-Konten verwendet.

**Arbeitsplatz:** ein Windows-11-Rechner mit Browser und PowerShell 7 (oder Windows PowerShell 5.1) sowie dem Modul `ExchangeOnlineManagement` (Installationsschritt: aus der Dokumentation prüfen, hier nicht bestätigt).

**Skripte:** Die Skripte dieser Reihe sind Python-Modelle und CSV-Auswertungen, die **ohne Verbindung zu Exchange Online** laufen (Python 3). Sie bilden Regeln, Rechnungen und Auswertungen nach; sie ersetzen den Test im Tenant nicht. Alle Adressen und Domains sind erfunden (`example.com`, `example.net`, `example.org`).

## B. Detaillierter Modulaufbau

### Modul 1: Überblick, Lizenzen und Grenzwerte

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau von Exchange Online als Teil von Microsoft 365 beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die wichtigsten Grenzwerte (Postfachgröße, Nachrichtengröße, Empfänger) nennen und anwenden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Test-Tenant mit Laufzeit und Kosten sachgerecht auswählen.
  * Nach Abschluss dieses Moduls kann der Lernende Verwaltungsrollen nach dem Prinzip der geringsten Rechte vergeben.
* **Voraussetzungen:** Microsoft-365-Grundlagen; IP-Adressen und Ports.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Exchange Online im Überblick: Dienst in Microsoft 365, Verwaltungsoberflächen (Admin Center, PowerShell) | 2 |
| 1.2 | Lizenzabhängigkeiten und Postfachgrößen; Grenzwerte für Nachrichten (`limits.py`) | 3 |
| 1.3 | Der Test-Tenant: Zugangsmöglichkeiten, Laufzeit, Kosten, Sicherheit des Testkontos | 3 |
| 1.4 | Rollen und Verwaltung: wer darf was; Grundsatz der geringsten Rechte | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tabelle lesen (Einheit 1.2):** Führen Sie `python3 limits.py` aus und notieren Sie für drei Lizenzarten die Postfachgröße. Prüfen Sie die Werte gegen die aktuelle Dokumentation (Stand und Quelle notieren).
2. **Anhang prüfen (Einheit 1.2):** Berechnen Sie, ob ein Anhang von 26 MB und einer von 30 MB bei der Standardgrenze von 35 MB noch zugestellt werden kann, und erklären Sie den Base64-Zuschlag.
3. **Test-Tenant auswählen (Einheit 1.3):** Vergleichen Sie zwei Zugänge (Developer-Programm, Testversion E3) nach Laufzeit, Kosten und Berechtigung und halten Sie fest, welchen Sie wählen und warum. Prüfen Sie vorab Laufzeit und mögliche Kosten.
4. **Rollen festlegen (Einheit 1.4):** Legen Sie fest, welche Rollen ein Hilfsdienst-Mitarbeiter für Postfächer und welche ein Administrator für Mailfluss braucht, ohne den Globalen Administrator zu vergeben.
5. **Dienst beschreiben (Einheit 1.1):** Beschreiben Sie in einem Absatz, was Exchange Online ist und über welche Wege es verwaltet wird (Fachwissen).

#### Kontrollfragen

1. Warum ist die Standardgrenze für Nachrichten wegen der Codierung kleiner als die Dateigröße des Anhangs?
2. Warum gehört ein Test-Tenant nicht in den produktiven Betrieb?
3. Was bedeutet „geringste Rechte“ bei der Vergabe von Administratorrollen?
4. Warum sind Lizenzgrenzen vor dem Einsatz zu prüfen?

### Modul 2: Postfachtypen und Massenanlage

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Postfachtypen unterscheiden und passend einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende Anforderungen an Lizenz und Anmeldung zuordnen.
  * Nach Abschluss dieses Moduls kann der Lernende eine CSV-Datei für die Massenanlage vor der Verarbeitung prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Postfachberechtigungen beschreiben.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Postfachtypen: Benutzerpostfach, freigegebenes Postfach, Raum- und Gerätepostfach | 3 |
| 2.2 | Lizenz und Anmeldung: wann ein Postfach eine Lizenz braucht (Fachwissen, prüfen) | 2 |
| 2.3 | Massenanlage: CSV-Datei vorbereiten und prüfen (`postfach_csv.py`) | 3 |
| 2.4 | Berechtigungen: Vollzugriff, Senden als, Senden im Auftrag (Überblick) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Typ wählen (Einheit 2.1):** Wählen Sie für fünf Fälle den Postfachtyp (Abteilungspostfach, Besprechungsraum, Beamer, neue Mitarbeiterin, Praktikant ohne Mail) und begründen Sie.
2. **Lizenzbedarf prüfen (Einheit 2.2):** Notieren Sie je Typ, ob nach Ihrer Kenntnis eine Lizenz nötig ist, und prüfen Sie die Angaben in der aktuellen Dokumentation (Ergebnis nicht bestätigt, solange nicht geprüft).
3. **CSV prüfen (Einheit 2.3):** Führen Sie `python3 postfach_csv.py postfaecher.csv` aus und beheben Sie jede gemeldete Zeile in einer korrigierten Kopie.
4. **Berechtigungen zuordnen (Einheit 2.4):** Erklären Sie den Unterschied zwischen Vollzugriff, „Senden als“ und „Senden im Auftrag“ an einem Beispiel.

#### Kontrollfragen

1. Wofür eignet sich ein freigegebenes Postfach?
2. Warum prüft man eine CSV-Datei vor der Massenanlage?
3. Was unterscheidet „Senden als“ von „Senden im Auftrag“?
4. Warum sollte die Anlage zuerst mit `-WhatIf` getestet werden (Modul 9)?

### Modul 3: Empfänger, Gruppen und Verteilerlisten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Empfängertypen und Gruppenarten unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende verschachtelte Gruppen auflösen und Schleifen erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende die Empfängergrenze je Nachricht berücksichtigen.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffsregeln für Verteilerlisten festlegen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Empfängertypen: Postfach, E-Mail-Kontakt, E-Mail-Benutzer, Gruppen | 3 |
| 3.2 | Gruppenarten: Verteilerliste, E-Mail-aktivierte Sicherheitsgruppe, Microsoft-365-Gruppe, dynamische Verteilerliste | 3 |
| 3.3 | Verschachtelung, Schleifen und Empfängergrenze (`verteiler_aufloesen.py`) | 3 |
| 3.4 | Verwaltung: wer darf an die Liste senden, Genehmigung, Besitzer | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Typen zuordnen (Einheit 3.1):** Ordnen Sie fünf Beispiele (externe Beraterin mit eigener Adresse, Abteilungsliste, Projektgruppe mit Teams, alle Mitarbeiter in Wien, Mailadresse eines Partners) dem passenden Empfänger- oder Gruppentyp zu.
2. **Gruppen wählen (Einheit 3.2):** Begründen Sie, wann eine dynamische Verteilerliste statt einer festen Liste sinnvoll ist (Fachwissen, prüfen).
3. **Liste auflösen (Einheit 3.3):** Führen Sie `python3 verteiler_aufloesen.py` aus. Zählen Sie Nennungen und verschiedene Empfänger und beschreiben Sie die Schleife.
4. **Regeln festlegen (Einheit 3.4):** Legen Sie für die Liste `alle@example.com` fest, wer senden darf, wer Besitzer ist und wie Antworten behandelt werden.

#### Kontrollfragen

1. Wie unterscheidet sich ein E-Mail-Kontakt von einem E-Mail-Benutzer?
2. Warum können Schleifen in verschachtelten Gruppen Probleme verursachen?
3. Was passiert, wenn die Empfängerzahl die Grenze überschreitet?
4. Warum sollte „alle“-Listen nicht für jeden zum Senden offen sein?

### Modul 4: Mailfluss, akzeptierte Domains und Connectoren

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Weg einer eingehenden und ausgehenden Nachricht beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende akzeptierte Domains und ihre Typen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Connectoren und ihre Bedingungen lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Grenzwerte im Mailfluss beachten.
* **Voraussetzungen:** Modul 3; DNS-Grundlagen (MX).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Mailfluss im Überblick: MX-Eintrag, Schutzprüfung, Zustellung ins Postfach | 3 |
| 4.2 | Akzeptierte Domains: autoritativ, interner Relay; Folgen für unbekannte Empfänger | 3 |
| 4.3 | Connectoren: eingehend von Partnern, ausgehend über Smarthost, TLS und Absenderprüfung (`mailfluss.py`) | 3 |
| 4.4 | Größe und Grenzwerte im Mailfluss: Nachrichtengröße, Empfängerzahl, Sendegrenzen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Weg zeichnen (Einheit 4.1):** Zeichnen Sie den Weg einer Nachricht von einem fremden Server zu einem Postfach (MX, Annahme, Schutzprüfung, Zustellung) und den Rückweg einer Antwort.
2. **Domaintyp wählen (Einheit 4.2):** Erklären Sie, wann eine Domain als „interner Relay“ statt „autoritativ“ eingetragen wird und was bei einem unbekannten Empfänger jeweils geschieht.
3. **Modell ausführen (Einheit 4.3):** Führen Sie `python3 mailfluss.py` aus und erklären Sie für jede Zeile, warum sie angenommen oder abgelehnt wird.
4. **Grenzwerte beachten (Einheit 4.4):** Nennen Sie je einen Fall, in dem die Nachrichtengröße, die Empfängerzahl oder die Sendegrenze zu einem Fehler führen kann.

#### Kontrollfragen

1. Wozu dient ein eingehender Connector für einen Partner?
2. Warum lehnt das Modell einen Absender mit falscher Domain am Partner-Connector ab?
3. Welche Rolle hat der MX-Eintrag beim Empfang?
4. Warum ist „kein Relay“ für nicht akzeptierte Domains wichtig?

### Modul 5: Transportregeln (Mailflussregeln)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer Transportregel erklären.
  * Nach Abschluss dieses Moduls kann der Lernende typische Regeln entwerfen.
  * Nach Abschluss dieses Moduls kann der Lernende die Reihenfolge der Auswertung nachvollziehen.
  * Nach Abschluss dieses Moduls kann der Lernende Regeln sicher testen und zurücknehmen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Aufbau einer Regel: Bedingungen, Aktionen, Ausnahmen, Priorität, Weiterverarbeitung | 3 |
| 5.2 | Typische Regeln: Haftungsausschluss, Kennzeichnung, Anhangsblockade, Kopie ans Archiv | 3 |
| 5.3 | Reihenfolge und Fehlerquellen: Priorität, „Verarbeitung beenden“ (`transportregeln.py`) | 3 |
| 5.4 | Test und Einführung: Testmodus, Überwachung, Rückfall | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Regel entwerfen (Einheit 5.2):** Entwerfen Sie auf Papier eine Regel „Externe Nachrichten mit Betreff ‚vertraulich‘ kennzeichnen“ mit Bedingung, Aktion und Ausnahme.
2. **Regelwerk auswerten (Einheit 5.3):** Führen Sie `python3 transportregeln.py` aus und notieren Sie je Nachricht, welche Regeln greifen und warum Regeln übersprungen werden.
3. **Reihenfolge ändern (Einheit 5.3):** Fügen Sie im Skript eine Nachricht 6 hinzu (ausgehend, extern, Anhang `setup.exe`). Setzen Sie dann die Priorität der Regel „Ausführbare Anhänge blockieren“ hinter den Haftungsausschluss und vergleichen Sie die Ausgabe für Nachricht 6. Warum ändert sich bei Nachricht 3 nichts?
4. **Einführung planen (Einheit 5.4):** Beschreiben Sie, wie Sie eine neue Regel mit geringem Risiko einführen (Testmodus, Beobachtung, Rückfall) und welche Angaben im Tenant zu prüfen sind (nicht bestätigt).
5. **Aufbau erklären (Einheit 5.1):** Erklären Sie Bedingung, Aktion, Ausnahme und Priorität einer Regel an einem Beispiel.

#### Kontrollfragen

1. Warum ist die Reihenfolge der Regeln wichtig?
2. Wozu dient die Option „weitere Regeln nicht verarbeiten“?
3. Welches Risiko hat eine Regel, die Nachrichten umleitet?
4. Warum sollten Regeln dokumentiert werden?

### Modul 6: Schutz vor Spam und Schadsoftware (Exchange Online Protection)

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Schutzschichten gegen unerwünschte Nachrichten benennen.
  * Nach Abschluss dieses Moduls kann der Lernende Quarantäne und Freigabe als Prozess beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Risiken von Erlaubnislisten erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlalarme systematisch behandeln.
* **Voraussetzungen:** Modul 5; Kurs „E-Mail-Authentifizierung: SPF, DKIM und DMARC“ (Überblick).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Schutzschichten: Verbindung, Authentifizierung (SPF, DKIM, DMARC), Inhalt, Anhänge | 3 |
| 6.2 | Richtlinien: Spam, Schadsoftware, Phishing; Quarantäne und Freigabe | 3 |
| 6.3 | Erlaubnis- und Sperrlisten: Wirkung und Risiko (`eop_modell.py`) | 3 |
| 6.4 | Berichte und Überwachung: was gefiltert wurde, Fehlalarme melden | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Schichten zuordnen (Einheit 6.1):** Ordnen Sie SPF/DKIM/DMARC, Inhaltsfilter, Anhangsscan und Absenderlisten den Schutzschichten zu.
2. **Modell auswerten (Einheit 6.3):** Führen Sie `python3 eop_modell.py` aus und erklären Sie, warum die Erlaubnisliste bei Schadsoftware nicht wirkt und warum die letzte Zeile (Erlaubnisliste, auffällig) problematisch ist.
3. **Quarantäne-Prozess (Einheit 6.2):** Beschreiben Sie den Ablauf, wenn ein Benutzer meldet, dass eine erwartete Nachricht fehlt (Nachrichtenverfolgung, Quarantäne prüfen, Freigabe, Ursache).
4. **Fehlalarme melden (Einheit 6.4):** Legen Sie fest, wie Fehlalarme gesammelt und ausgewertet werden (Meldeweg, Verantwortlicher, Ziel).

#### Kontrollfragen

1. Warum ersetzt eine Erlaubnisliste nicht die Prüfung auf Schadsoftware?
2. Warum ist ein bestandenes SPF allein kein Zustellgarant?
3. Was ist ein Fehlalarm und wie wird er behandelt?
4. Warum gehören Berichte zur Überwachung?

### Modul 7: Aufbewahrung und Compliance im Überblick

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Aufbewahrung, Archiv und Löschen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung einer Richtlinie auf Beispielnachrichten berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle einer Sperre (Hold) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Zuständigkeiten für Aufbewahrungsfristen benennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Aufbewahrung, Archiv und Löschen: Begriffe und Zusammenspiel | 3 |
| 7.2 | Aufbewahrungsrichtlinien: Archiv nach N Tagen, Löschen nach M Tagen (`aufbewahrung.py`) | 3 |
| 7.3 | Sperren (Hold) und Wiederherstellung gelöschter Elemente im Überblick | 2 |
| 7.4 | Zuständigkeiten und rechtliche Rahmenbedingungen (keine Rechtsberatung) | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Begriffe abgrenzen (Einheit 7.1):** Erklären Sie Aufbewahrung, Archivierung und Löschung an einem Beispiel einer Rechnungsmail.
2. **Wirkung berechnen (Einheit 7.2):** Führen Sie `python3 aufbewahrung.py` aus und erklären Sie jede Zeile (Alter, Hold, Wirkung).
3. **Hold verstehen (Einheit 7.3):** Beschreiben Sie, warum die Nachricht „Vertrag 2025 (Hold)“ bleibt, obwohl sie älter als 365 Tage ist, und wer eine Sperre anordnen sollte.
4. **Zuständigkeit festlegen (Einheit 7.4):** Legen Sie fest, wer die Fristen bestimmt (Fachabteilung, Datenschutz, Recht) und wie Änderungen dokumentiert werden.

#### Kontrollfragen

1. Warum ist „löschen nach N Tagen“ eine fachliche und keine technische Entscheidung?
2. Was bewirkt eine Sperre (Hold)?
3. Warum sollte man Fristen vor der Einführung abstimmen?
4. Warum ist hier keine Rechtsaussage möglich?

### Modul 8: Migration und Hybrid im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Migrationsarten und ihre Eignung nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Dauer und Wellen einer Migration abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende Koexistenz und Rückfall beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Nacharbeiten planen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Migrationsarten im Überblick: Umstellung auf einmal, in Etappen, Hybrid, IMAP | 3 |
| 8.2 | Planung: Postfachgrößen, Bandbreite, Wellen (`migration_planer.py`) | 3 |
| 8.3 | Koexistenz: gemeinsame Adressliste, Mailfluss, Rückfall | 2 |
| 8.4 | Nacharbeiten: Clients, Weiterleitungen, Altsysteme abschalten | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Art wählen (Einheit 8.1):** Wählen Sie für drei Szenarien (kleines Büro, mittlere Firma mit lokalem Server, viele Standorte) die Migrationsart und begründen Sie (Fachwissen, nicht bestätigt).
2. **Dauer berechnen (Einheit 8.2):** Führen Sie `python3 migration_planer.py` aus und ändern Sie Bandbreite und Anteil. Notieren Sie die Wirkung auf die Dauer.
3. **Wellen planen (Einheit 8.2):** Verteilen Sie die fünf Gruppen auf Wellen (Nächte oder Wochenenden) und begründen Sie die Reihenfolge.
4. **Rückfall beschreiben (Einheit 8.3):** Beschreiben Sie, wie Sie bei Problemen zum alten System zurückkehren (MX, Postfächer, Kommunikation).
5. **Nacharbeiten planen (Einheit 8.4):** Listen Sie fünf Nacharbeiten nach der Migration auf (Clients, Weiterleitungen, Altsystem) und ordnen Sie sie.

#### Kontrollfragen

1. Warum ist die Bandbreite allein kein verlässliches Maß für die Dauer?
2. Wozu dient Koexistenz?
3. Warum sollte der MX-Eintrag erst spät umgestellt werden?
4. Welche Nacharbeiten betreffen die Clients?

### Modul 9: Verwaltung mit PowerShell

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende sich mit einem Test-Tenant per PowerShell verbinden (beschreiben).
  * Nach Abschluss dieses Moduls kann der Lernende Postfächer lesen, filtern und exportieren.
  * Nach Abschluss dieses Moduls kann der Lernende ändernde Befehle mit `-WhatIf` und kleinen Mengen testen.
  * Nach Abschluss dieses Moduls kann der Lernende Skripte vor dem Einsatz auf riskante Muster prüfen.
* **Voraussetzungen:** Module 2 bis 4; PowerShell-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Verbindung, Modul und Rechte: `Connect-ExchangeOnline`, Moderne Authentifizierung (Fachwissen) | 3 |
| 9.2 | Lesen und Filtern: `Get-Mailbox`, `Select-Object`, `Where-Object`, Ausgabe in CSV | 3 |
| 9.3 | Sicher ändern: `-WhatIf`, `-Confirm`, kleine Mengen, Protokoll (`cmdlet_check.py`) | 3 |
| 9.4 | Massenverarbeitung aus CSV und Fehlerbehandlung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Verbindung beschreiben (Einheit 9.1):** Beschreiben Sie Schritte und Voraussetzungen für die Verbindung (Modul, Konto, Rolle, Anmeldung mit Mehrfaktor). Markieren Sie, was Sie nicht geprüft haben.
2. **Abfrage entwerfen (Einheit 9.2):** Schreiben Sie (ohne auszuführen) einen Befehl, der alle Postfächer eines Typs mit Name und Größe als CSV ausgibt.
3. **Skripte prüfen (Einheit 9.3):** Führen Sie `python3 cmdlet_check.py beispiel_gut.ps1 beispiel_riskant.ps1` aus und beheben Sie jede Meldung in einer Kopie von `beispiel_riskant.ps1`.
4. **Massenlauf planen (Einheit 9.4):** Planen Sie einen Massenlauf aus einer CSV (Testlauf mit `-WhatIf`, zehn Einträge, Protokolldatei, Rückfall).

#### Kontrollfragen

1. Warum soll ein Skript nie ein Kennwort im Klartext enthalten?
2. Wozu dient `-WhatIf`?
3. Warum prüft man zuerst mit wenigen Einträgen?
4. Was bedeutet es, dass die Prüfung nur eine Textprüfung ist?

### Modul 10: Nachrichtenverfolgung und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Nachrichtenverfolgung gezielt abfragen und auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende häufige Fehlercodes deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerquellen systematisch eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Störungsbericht schreiben.
* **Voraussetzungen:** Module 4 bis 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | Nachrichtenverfolgung: was gesucht wird, Statuswerte, Zeiträume | 3 |
| 10.2 | Fehlercodes lesen: 5.1.1, 5.7.1, 4.4.0, 4.4.7 (Fachwissen) (`nachrichtenverfolgung.py`) | 3 |
| 10.3 | Systematische Eingrenzung: Absender, Empfänger, Regel, Schutz, Connector | 2 |
| 10.4 | Abschlussübung und Selbstprüfung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auswertung ausführen (Einheit 10.2):** Führen Sie `python3 nachrichtenverfolgung.py beispiel_trace.csv` aus und zählen Sie die Status. Erklären Sie jede nicht zugestellte Nachricht.
2. **Fehler deuten (Einheit 10.2):** Erklären Sie die Codes 5.1.1, 5.7.1, 4.4.0 und 4.4.7 mit einer möglichen Ursache und Gegenmaßnahme. Kennzeichnen Sie, dass die Deutung nicht bestätigt ist.
3. **Eingrenzung beschreiben (Einheit 10.3):** Eine Mail an `partner@partner-b.example.net` kommt nicht an. Beschreiben Sie die Schritte (Verfolgung, Connector, Zielserver, Wiederholung, Absender informieren).
4. **Störungsbericht (Einheit 10.4):** Schreiben Sie einen Störungsbericht mit Zeitpunkt, Betroffenen, Meldung, Ursache, Maßnahme und Prüfung.
5. **Verfolgung abfragen (Einheit 10.1):** Beschreiben Sie, welche Angaben Sie für eine Nachrichtenverfolgung brauchen und welche Statuswerte vorkommen (Fachwissen, nicht bestätigt).

#### Kontrollfragen

1. Was bedeutet der Status „Pending“ im Unterschied zu „Failed“?
2. Wie unterscheiden Sie einen Fehler beim Empfänger von einem Fehler beim Absender?
3. Warum ist die Quarantäne kein Fehler?
4. Welche Angaben gehören in eine Verfolgung, um Treffer einzugrenzen?
