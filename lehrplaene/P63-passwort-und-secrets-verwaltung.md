# Lehrplan: Passwort- und Secrets-Verwaltung

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen; Linux-Grundlagen (Kommandozeile, Dateirechte); Grundbegriffe der Verschlüsselung; Git-Grundlagen |
| **Gesamtumfang** | 8 Module, 90 UE (zu 45 Minuten; 67,5 Stunden) |
| **Fokus-Technologien** | Passwortstärke und Entropie, Passwort-Hashing (PBKDF2, scrypt, bcrypt), Passwort-Richtlinien, Prinzip eines Passwortmanagers (verschlüsselter Tresor), Geheimnisse in Code und Git, Geheimnisse im Betrieb (Argumente, Umgebung, Dateien, Protokolle), verschlüsselte Geheimnisdateien (age, gpg), Geheimnisdienste im Überblick |
| **Thematische Abgrenzung (Out of Scope)** | Kryptografie und PKI sind eigene Kurse; Active-Directory-Kennwortrichtlinien nur kurz. Nicht behandelt: Betrieb eines Geheimnisdienstes (OpenBao oder HashiCorp Vault), Hardware-Schlüssel, Mehr-Faktor-Verfahren. Lizenzmodelle von OpenBao und HashiCorp Vault: mit Stand prüfen (nicht recherchiert) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Passwortstärke und Entropie | 1 | 12 |
| 2 | Passwort-Hashing | 1 | 12 |
| 3 | Passwort-Richtlinien und Passphrasen | 1 | 10 |
| 4 | Tresor und Passwortmanager | 1 | 12 |
| 5 | Geheimnisse in Code und Git | 1 | 12 |
| 6 | Geheimnisse im Betrieb | 1 | 12 |
| 7 | Verschlüsselte Geheimnisdateien mit age | 1 | 12 |
| 8 | Geheimnisdienste im Überblick | 2 | 8 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **90** |

**Priorität 1** (Pflicht) sind die Module 1 bis 7; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 8 (Geheimnisdienste im Überblick). Fällt Modul 8 weg, verringert sich der Gesamtumfang auf 82 UE; kein Pflichtmodul setzt Modul 8 voraus.

### 2. Quellen

**Nicht gelesen:** Empfehlungen zu Passwortrichtlinien (zum Beispiel von NIST oder BSI), die Dokumentation von OpenBao und HashiCorp Vault sowie die Handbücher von `age` und `gpg` wurden **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt. Zahlen, Namen und Werte sind erfundene Beispieldaten; alle Geheimnisse sind **erfunden**.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** Python 3 mit `hashlib`, `bcrypt`, `cryptography` und `secrets`, `openssl passwd`, `git`, `gpg`, `age 1.1.1`. **Nicht ausgeführt:** Passwortmanager-Programme, OpenBao und HashiCorp Vault, Mehr-Faktor-Verfahren, Active Directory.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Secrets`, `10.63.0.0/24`).

**VM:** `sec01` (**erforderlich**, `10.63.0.2`): Linux-Server (Debian oder Ubuntu) mit `git`, `gpg`, `age`, `openssl`, Python 3 und den Python-Paketen `bcrypt` und `cryptography`.

**Internetphase:** Für die Installation der Pakete braucht `sec01` vorübergehend Internetzugang; danach wird er entfernt. **Es werden nur erfundene Geheimnisse verwendet; echte Passwörter gehören nie in Übungsdateien.**

**Prüfpunkt (Checkpoint):** Vor Modul 5 von `sec01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte arbeiten unter `/tmp/p63`, brauchen keine Rechte außer dem Schreiben dort und räumen am Ende auf.

## B. Detaillierter Modulaufbau

### Modul 1: Passwortstärke und Entropie

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Entropie eines zufällig gewählten Passworts aus Zeichensatz und Länge berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende den Einfluss von Länge und Zeichensatz vergleichen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Muster die Stärke senken.
  * Nach Abschluss dieses Moduls kann der Lernende ein Rate-Zeit-Modell lesen und seine Annahmen nennen.
* **Voraussetzungen:** Logarithmus (Grundlagen).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Entropie rechnen | 3 |
| 1.2 | Länge gegen Zeichensatz | 3 |
| 1.3 | Rate-Zeit | 3 |
| 1.4 | Muster | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Entropie rechnen (Einheit 1.1):** Führen Sie `bash entropie.sh` aus. Erklären Sie die Tabelle in Schritt 1: Wie entsteht der Wert für 12 Kleinbuchstaben?
2. **Länge gegen Zeichensatz (Einheit 1.2):** Vergleichen Sie „8 Zeichen aus 94“ mit „12 Kleinbuchstaben“ und mit „4 Wörtern aus 7776“.
3. **Rate-Zeit (Einheit 1.3):** Lesen Sie Schritt 2: Wie ändert sich die Zeit mit dem Hash-Verfahren, und welche Annahmen stecken im Modell?
4. **Muster (Einheit 1.4):** Erklären Sie Schritt 3: Warum hat „Wort + 2 Ziffern“ nur rund 23 Bit?

#### Kontrollfragen

1. Wie berechnet man die Entropie eines zufälligen Passworts?
2. Warum sind lange Passphrasen oft besser als kurze komplizierte Passwörter?
3. Welche Annahmen stecken im Rate-Zeit-Modell?
4. Warum zählt ein Muster nicht als zufällig?

### Modul 2: Passwort-Hashing

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Passwörter gesalzen und mit langsamen Verfahren gehasht werden.
  * Nach Abschluss dieses Moduls kann der Lernende PBKDF2, scrypt und bcrypt unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Zeitkosten verschiedener Verfahren messen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende ein bcrypt-Ergebnis prüfen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Einfacher Hash | 3 |
| 2.2 | Salz | 3 |
| 2.3 | Kosten | 3 |
| 2.4 | bcrypt und crypt | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einfacher Hash (Einheit 2.1):** Führen Sie `bash hashing.sh` aus. Erklären Sie Schritt 1: Was verrät der gleiche Wert zweimal?
2. **Salz (Einheit 2.2):** Erklären Sie Schritt 2: Welche Angriffe erschwert das Salz?
3. **Kosten (Einheit 2.3):** Lesen Sie die Tabelle in Schritt 3: Wie unterscheiden sich die Verfahren in der Zeit, und warum wünscht man sich Langsamkeit?
4. **bcrypt und crypt (Einheit 2.4):** Erklären Sie Schritt 4 und 5: Was steht im bcrypt-Ergebnis, und warum ist der `openssl passwd`-Wert bei gleichem Salz gleich?

#### Kontrollfragen

1. Wozu dient das Salz?
2. Warum ist ein einfacher SHA-256 ungeeignet?
3. Was bedeutet „Kosten 10“ bei bcrypt?
4. Warum sind zwei bcrypt-Hashes desselben Passworts verschieden?

### Modul 3: Passwort-Richtlinien und Passphrasen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine einfache Richtlinie als Prüfprogramm umsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Sperrliste verwenden.
  * Nach Abschluss dieses Moduls kann der Lernende Passphrasen mit einem sicheren Zufallsgenerator erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen `random` und `secrets` erklären.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Prüfer lesen | 4 |
| 3.2 | Eigene Regeln | 2 |
| 3.3 | Passphrase | 2 |
| 3.4 | Zufall | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Prüfer lesen (Einheit 3.1):** Führen Sie `bash richtlinie.sh` aus. Erklären Sie für jedes der sechs Beispiele, warum es besteht oder nicht.
2. **Eigene Regeln (Einheit 3.2):** Ergänzen Sie den Prüfer um eine Regel Ihrer Wahl (zum Beispiel keine Jahreszahl) und prüfen Sie sie.
3. **Passphrase (Einheit 3.3):** Erklären Sie Schritt 2: Warum sind zehn Wörter in der Liste zu wenig, und wie viele Bit hat eine Liste mit 7776 Wörtern?
4. **Zufall (Einheit 3.4):** Erklären Sie Schritt 3: Warum darf man für Geheimnisse nicht `random` verwenden?

#### Kontrollfragen

1. Warum eine Sperrliste?
2. Warum fällt `Sommer2026!` durch?
3. Was ist an `random` unsicher?
4. Wie viele Bit haben vier Wörter aus 7776?

### Modul 4: Tresor und Passwortmanager

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip eines Passwortmanagers (Schlüsselableitung und Verschlüsselung) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum ein Tresor ohne Passphrase nicht lesbar ist.
  * Nach Abschluss dieses Moduls kann der Lernende Manipulation erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen gpg-symmetrischen Tresor mit dem Eigenbau vergleichen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Tresor lesen | 3 |
| 4.2 | Fehlversuch und Manipulation | 3 |
| 4.3 | Salz und Nonce | 3 |
| 4.4 | Vergleich | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Tresor lesen (Einheit 4.1):** Führen Sie `bash tresor.sh` aus. Erklären Sie Schritt 1: Wie entsteht der Schlüssel aus der Passphrase, und warum steht „Beispiel“ nicht in der Datei?
2. **Fehlversuch und Manipulation (Einheit 4.2):** Erklären Sie Schritt 2 und 3: Was passiert bei falscher Passphrase und bei einem geänderten Byte?
3. **Salz und Nonce (Einheit 4.3):** Erklären Sie Schritt 4: Warum sind zwei Tresore mit gleichem Inhalt verschieden?
4. **Vergleich (Einheit 4.4):** Vergleichen Sie Schritt 5 (gpg) mit dem Eigenbau: Was ist gleich, was anders, und warum sollte man in der Praxis kein Eigenbau-Verfahren einsetzen?

#### Kontrollfragen

1. Wozu dient die Schlüsselableitung (scrypt)?
2. Was erkennt die authentisierte Verschlüsselung?
3. Warum bleibt das Salz in der Datei?
4. Warum kein Eigenbau?

### Modul 5: Geheimnisse in Code und Git

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Geheimnisse in Dateien mit einem Scanner suchen und dessen Grenzen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Löschen im Git-Verlauf nichts entfernt.
  * Nach Abschluss dieses Moduls kann der Lernende Geheimnisse aus dem Code lösen (Umgebung, Vorlage, `.gitignore`).
  * Nach Abschluss dieses Moduls kann der Lernende einen `pre-commit`-Hook einsetzen.
* **Voraussetzungen:** Git-Grundlagen; Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Scanner | 3 |
| 5.2 | Verlauf | 3 |
| 5.3 | Saubere Lösung | 3 |
| 5.4 | Hook | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Scanner (Einheit 5.1):** Führen Sie `bash leckscan.sh` aus. Erklären Sie Schritt 1: Warum findet der Scanner `config.env` nicht, `grep` aber schon?
2. **Verlauf (Einheit 5.2):** Erklären Sie Schritt 2 und 4: Was bleibt nach „Datei löschen und committen“, und was folgt daraus?
3. **Saubere Lösung (Einheit 5.3):** Erklären Sie Schritt 3: Welche drei Maßnahmen trennen Geheimnis und Code?
4. **Hook (Einheit 5.4):** Erklären Sie Schritt 5: Wie verhindert der Hook den Commit, und was kann er nicht verhindern?

#### Kontrollfragen

1. Warum reicht das Löschen einer Datei nicht?
2. Was ist nach einem Leck zu tun?
3. Wozu `config.env.beispiel`?
4. Was kann ein Hook nicht verhindern?

### Modul 6: Geheimnisse im Betrieb

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, wer Geheimnisse in Argumenten, der Umgebung und Dateien sehen kann.
  * Nach Abschluss dieses Moduls kann der Lernende Dateirechte für Geheimnisdateien setzen.
  * Nach Abschluss dieses Moduls kann der Lernende das Risiko der späten Rechtevergabe (`chmod` nach dem Schreiben) nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Geheimnisse in Protokollen maskieren.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Argument | 3 |
| 6.2 | Umgebung | 3 |
| 6.3 | Datei | 3 |
| 6.4 | Protokolle | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Argument (Einheit 6.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1: Wer kann das Geheimnis im Argument sehen?
2. **Umgebung (Einheit 6.2):** Erklären Sie Schritt 2: Welche Rechte hat `/proc/PID/environ`, und was sehen Kindprozesse?
3. **Datei (Einheit 6.3):** Vergleichen Sie in Schritt 3 die drei Wege, eine Geheimnisdatei anzulegen.
4. **Protokolle (Einheit 6.4):** Erklären Sie Schritt 4 und 5: Wie vermeidet man das Argument, und wie maskiert man in Protokollen?

#### Kontrollfragen

1. Warum sind Geheimnisse in Argumenten riskant?
2. Warum `umask 077` vor dem Schreiben?
3. Was erbt ein Kindprozess?
4. Warum Protokolle maskieren?

### Modul 7: Verschlüsselte Geheimnisdateien mit age

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Dateien für mehrere Empfänger mit `age` verschlüsseln.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, was der Entzug eines Empfängers bewirkt und was nicht.
  * Nach Abschluss dieses Moduls kann der Lernende private Schlüssel schützen.
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf einer Rotation beschreiben.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Schlüssel | 3 |
| 7.2 | Mehrere Empfänger | 3 |
| 7.3 | Entzug | 3 |
| 7.4 | Ablauf planen | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Schlüssel (Einheit 7.1):** Führen Sie `bash age.sh` aus. Erklären Sie Schritt 1: Welcher Schlüssel ist öffentlich, welcher privat, und welche Rechte hat die private Datei?
2. **Mehrere Empfänger (Einheit 7.2):** Erklären Sie Schritt 2 bis 4: Wer kann die Datei lesen, wer nicht?
3. **Entzug (Einheit 7.3):** Erklären Sie Schritt 5: Warum kann `ben` die alte Datei weiter lesen, und was folgt daraus?
4. **Ablauf planen (Einheit 7.4):** Beschreiben Sie in sechs Schritten, wie Sie ein Datenbank-Passwort in einer age-Datei rotieren, wenn eine Person das Team verlässt.

#### Kontrollfragen

1. Wer kann entschlüsseln?
2. Was bewirkt der Entzug eines Empfängers?
3. Warum Rotation?
4. Wie schützt man private Schlüssel?

### Modul 8: Geheimnisdienste im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffsrichtlinien, befristete Ausleihen und Rotation an einem Modell erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Rolle eines Audit-Protokolls nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Vorteile gegenüber Dateien einordnen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Modell lesen | 4 |
| 8.2 | Rotation und Ausleihe | 2 |
| 8.3 | Audit und Befehle | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Modell lesen (Einheit 8.1):** Führen Sie `bash lauf.sh` aus. Erklären Sie Schritt 1: Warum bekommt `web` den Wert für `db/lesen`, aber nicht für `nas/lesen`?
2. **Rotation und Ausleihe (Einheit 8.2):** Erklären Sie Schritt 2 und 3: Was gilt für die alte Ausleihe nach der Rotation?
3. **Audit und Befehle (Einheit 8.3):** Lesen Sie Schritt 4 und `beispiel_cli.txt`. Kennzeichnen Sie, was nicht geprüft wurde, und listen Sie Fragen für eine Produktauswahl (Lizenz, Betrieb, Wiederherstellung).

#### Kontrollfragen

1. Wozu dient eine Zugriffsrichtlinie?
2. Was ist eine befristete Ausleihe?
3. Wozu dient das Audit-Protokoll?
4. Warum Lizenz und Version prüfen?
