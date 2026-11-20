# Lehrplan: Penetrationstest-Grundlagen

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | Netzwerkgrundlagen (TCP/IP, Ports, HTTP); Linux-Grundlagen (Kommandozeile); Grundbegriffe der IT-Sicherheit |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | rechtlicher Rahmen und Scope, Vorgehen und Dokumentation, Aufklärung eigener Systeme, Portscans mit nmap, Fehlkonfigurationen und einfache Schwachstellen, Prüfung einer Webanwendung ohne Ausnutzung, Anmeldeschutz, Bericht und Bewertung |
| **Thematische Abgrenzung (Out of Scope)** | Keine Exploits, keine Passwortlisten, keine Angriffe auf Fremdsysteme. Nicht behandelt: Metasploit, Exploit-Entwicklung, Social Engineering, Active-Directory-Angriffe, drahtlose Netze. Rechtliche Aussagen sind keine Rechtsberatung (nicht rechtlich geprüft) |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Recht, Ethik und Scope | 1 | 10 |
| 2 | Vorgehen und Dokumentation | 1 | 10 |
| 3 | Aufklärung eigener Systeme | 1 | 12 |
| 4 | Portscans mit nmap | 1 | 16 |
| 5 | Fehlkonfigurationen finden | 1 | 14 |
| 6 | Webanwendung prüfen | 1 | 16 |
| 7 | Anmeldeschutz prüfen | 2 | 10 |
| 8 | Bericht und Abschlussprojekt | 1 | 12 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 6 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 7 (Anmeldeschutz prüfen). Fällt Modul 7 weg, verringert sich der Gesamtumfang auf 90 UE; Modul 8 benötigt die Befunde der Module 5 und 6, nicht aber Modul 7.

### 2. Quellen

**Nicht gelesen:** Die Dokumentation von nmap, Rechtsvorschriften zum Thema (zum Beispiel zum Ausspähen von Daten) und Vorgehensmodelle für Penetrationstests wurden **nicht** gelesen. Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch Läufe im Test-Container bestätigt. Namen, Adressen und Daten sind erfunden.

**Getestet mit (Ubuntu 24.04.5, Cloud-Container):** nmap 7.94SVN (Verbindungsscan `-sT`, Skripte `banner`, `http-*`), curl, Python 3 (`http.server` als Beispielanwendung). **Nicht ausgeführt:** Metasploit, Burp Suite, Nessus oder OpenVAS, Scans über ein Netz, andere nmap-Versionen.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Pentest`, `10.64.0.0/24`).

**VM 1:** `pt01` (**erforderlich**, `10.64.0.2`): Prüfsystem mit Linux, `nmap`, `curl` und Python 3.

**VM 2:** `ziel01` (**erforderlich**, `10.64.0.10`): eigenes Zielsystem mit der Beispielanwendung `app.py` aus der Übungsreihe. **Es werden ausschließlich eigene Systeme im isolierten Labor geprüft.**

**Internetphase:** Für die Installation der Pakete braucht `pt01` vorübergehend Internetzugang; danach wird er entfernt.

**Prüfpunkt (Checkpoint):** Vor Modul 4 von beiden VMs Prüfpunkte anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte starten die Beispielanwendung selbst auf `127.0.0.1` (Ports 8080, 8081, 2121 und 2222) und brauchen keine Rechte.

## B. Detaillierter Modulaufbau

### Modul 1: Recht, Ethik und Scope

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum ein Test eine schriftliche Beauftragung braucht.
  * Nach Abschluss dieses Moduls kann der Lernende die Pflichtangaben eines Auftrags nennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Geltungsbereich (Scope) prüfbar festhalten.
  * Nach Abschluss dieses Moduls kann der Lernende Ziele außerhalb des Scopes zuverlässig ausschließen.
* **Voraussetzungen:** Netzwerkgrundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Auftrag lesen | 4 |
| 1.2 | Scope prüfen | 2 |
| 1.3 | Lücken finden | 2 |
| 1.4 | Eigene Regeln | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Auftrag lesen (Einheit 1.1):** Führen Sie `bash recht.sh` aus. Erklären Sie, wozu jedes Feld der Auftragsdatei in Schritt 1 dient.
2. **Scope prüfen (Einheit 1.2):** Erklären Sie Schritt 2: Warum gilt `10.64.0.99` nicht als im Scope, obwohl es im Netz `10.64.0.0/24` liegt?
3. **Lücken finden (Einheit 1.3):** Erklären Sie Schritt 3: Welche Folgen hätte ein Test ohne Notfallkontakt und ohne Liste der ausgeschlossenen Systeme?
4. **Eigene Regeln (Einheit 1.4):** Entwerfen Sie je drei erlaubte und drei verbotene Tätigkeiten für einen Test Ihrer eigenen Heimlabor-Umgebung.

#### Kontrollfragen

1. Warum reicht mündliches Einverständnis nicht?
2. Was ist der Scope?
3. Warum eine Liste „außerhalb“?
4. Wozu ein Notfallkontakt?

### Modul 2: Vorgehen und Dokumentation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Phasen eines Tests nennen und ihre Ergebnisse beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Befunde nachvollziehbar mit Beleg notieren.
  * Nach Abschluss dieses Moduls kann der Lernende erkennen, wann ein Beleg wiederholbar ist.
  * Nach Abschluss dieses Moduls kann der Lernende Rohdaten und Zeitpunkte sichern.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Phasen | 4 |
| 2.2 | Notizfunktion | 2 |
| 2.3 | Wiederholbarkeit | 2 |
| 2.4 | Eigener Befund | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Phasen (Einheit 2.1):** Führen Sie `bash vorgehen.sh` aus. Ordnen Sie jeder der sechs Phasen aus Schritt 1 eine Tätigkeit aus Ihrem Alltag zu.
2. **Notizfunktion (Einheit 2.2):** Erklären Sie Schritt 2: Was enthält ein Eintrag, und wozu dient die Prüfsumme?
3. **Wiederholbarkeit (Einheit 2.3):** Erklären Sie Schritt 3 und 4: Warum sind die Prüfsummen im einen Fall gleich und im anderen nicht?
4. **Eigener Befund (Einheit 2.4):** Ergänzen Sie einen vierten Befund (zum Beispiel TRACE in den erlaubten Methoden) und notieren Sie ihn.

#### Kontrollfragen

1. Wozu dient ein Beleg?
2. Warum Zeitstempel und Rohdatei?
3. Warum ist die Prüfsumme in Schritt 3 gleich?
4. Was gehört zu einem Befund?

### Modul 3: Aufklärung eigener Systeme

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende lauschende Ports von innen und von außen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Banner lesen und deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Kopfzeilen und `robots.txt` auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende beschreiben, was ein Dienst über sich verrät.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Lauschende Ports | 3 |
| 3.2 | Banner | 3 |
| 3.3 | Kopfzeilen und robots.txt | 3 |
| 3.4 | Zusammenfassung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Lauschende Ports (Einheit 3.1):** Führen Sie `bash aufklaerung.sh` aus. Erklären Sie Schritt 1: Was zeigt `ss -ltn`, und was zeigt es nicht?
2. **Banner (Einheit 3.2):** Erklären Sie Schritt 2: Was verrät der Banner, und wie könnte ein Betreiber das ändern?
3. **Kopfzeilen und robots.txt (Einheit 3.3):** Erklären Sie Schritt 3 bis 5: Welche Informationen liefern diese Quellen, und warum ist `robots.txt` kein Schutz?
4. **Zusammenfassung (Einheit 3.4):** Schreiben Sie eine Liste aller Informationen, die der Dienst im Skript ohne Anmeldung preisgibt.

#### Kontrollfragen

1. Wozu dient `ss -ltn`?
2. Was verrät ein Banner?
3. Ist robots.txt ein Zugriffsschutz?
4. Warum liefert `/backup/` den Status 404, obwohl die Datei darunter existiert?

### Modul 4: Portscans mit nmap

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 16 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende mit nmap offene, geschlossene und gefilterte Ports unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Portbereiche und `--open` einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende die Ausgabe mit `--reason` deuten.
  * Nach Abschluss dieses Moduls kann der Lernende grepbaren Export auswerten und die Grenzen der Dienstnamen nennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Einzelne Ports | 4 |
| 4.2 | Gründe | 4 |
| 4.3 | Bereiche und Export | 4 |
| 4.4 | Dienstnamen und Banner | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Einzelne Ports (Einheit 4.1):** Führen Sie `bash portscan.sh` aus. Erklären Sie Schritt 1: Welche Ports sind offen, welcher ist geschlossen?
2. **Gründe (Einheit 4.2):** Erklären Sie Schritt 2: Was bedeuten `syn-ack` und `conn-refused`?
3. **Bereiche und Export (Einheit 4.3):** Erklären Sie Schritt 3 und 4: Wie verändert `--open` die Ausgabe, und wie wertet man `-oG` aus?
4. **Dienstnamen und Banner (Einheit 4.4):** Erklären Sie Schritt 5 und 6: Warum ist der Dienstname `ccproxy-ftp` irreführend, und was zeigt das Skript `banner`?

#### Kontrollfragen

1. Was bedeutet „open“?
2. Was bedeutet „closed“?
3. Woher stammt der Dienstname?
4. Warum ist `-sV` mit Vorsicht einzusetzen?

### Modul 5: Fehlkonfigurationen finden

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende nmap-Skripte der Kategorie `safe` einsetzen und prüfen, was sie tun.
  * Nach Abschluss dieses Moduls kann der Lernende Sicherheits-Kopfzeilen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende riskante Methoden und verbose Fehlerseiten erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Befunde knapp formulieren.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | nmap-Skripte | 5 |
| 5.2 | Sicherheits-Kopfzeilen | 3 |
| 5.3 | Methoden und Fehlerseite | 3 |
| 5.4 | Skriptauswahl | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **nmap-Skripte (Einheit 5.1):** Führen Sie `bash konfiguration.sh` aus. Erklären Sie Schritt 1: Was meldet jedes der vier Skripte?
2. **Sicherheits-Kopfzeilen (Einheit 5.2):** Erklären Sie Schritt 2 und 3: Welche Kopfzeilen fehlen, und wozu dient jede?
3. **Methoden und Fehlerseite (Einheit 5.3):** Erklären Sie den Befund zu TRACE und die Fehlerseite aus Schritt 4.
4. **Skriptauswahl (Einheit 5.4):** Erklären Sie Schritt 6: Wie prüft man vor dem Einsatz, ob ein nmap-Skript sicher ist?

#### Kontrollfragen

1. Wozu `X-Content-Type-Options`?
2. Was ist an TRACE kritisch?
3. Warum zeigt die Fehlerseite ein Problem?
4. Wie erkennt man den Skripttyp?

### Modul 6: Webanwendung prüfen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 16 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ungeprüfte Ausgabe von Eingaben mit einem harmlosen Marker erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende öffentlich erreichbare Sicherungsdateien finden.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerseiten und Zugriffsschutz bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende Befunde ohne Ausnutzung belegen.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Eingabe-Echo | 4 |
| 6.2 | Pfade | 4 |
| 6.3 | Sicherung bewerten | 4 |
| 6.4 | Fehlerseite und Admin | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eingabe-Echo (Einheit 6.1):** Führen Sie `bash webpruefung.sh` aus. Erklären Sie Schritt 1: Woran sieht man den Unterschied zwischen `/suche` und `/suche-sicher`?
2. **Pfade (Einheit 6.2):** Erklären Sie Schritt 2: Welche Pfade liefern welchen Status, und was folgt daraus?
3. **Sicherung bewerten (Einheit 6.3):** Erklären Sie Schritt 3: Warum wird das Kennwort maskiert, und warum darf man es nicht weiterverwenden?
4. **Fehlerseite und Admin (Einheit 6.4):** Erklären Sie Schritt 4 und 5 und formulieren Sie die Befundliste (Schritt 6) in eigenen Worten.

#### Kontrollfragen

1. Warum ein Marker statt Schadcode?
2. Was bedeutet Status 401?
3. Was bedeutet Status 500?
4. Warum ist die Sicherung ein hoher Befund?

### Modul 7: Anmeldeschutz prüfen

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende prüfen, ob ein Dienst Fehlversuche begrenzt.
  * Nach Abschluss dieses Moduls kann der Lernende Vor- und Nachteile einer Kontosperre nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Gegenmaßnahmen vorschlagen.
* **Voraussetzungen:** Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Dienst ohne Sperre | 4 |
| 7.2 | Dienst mit Sperre | 3 |
| 7.3 | Bewertung | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dienst ohne Sperre (Einheit 7.1):** Führen Sie `bash anmeldung.sh` aus. Erklären Sie Schritt 1: Was bedeutet es, dass nach sechs Fehlversuchen noch eine Anmeldung klappt?
2. **Dienst mit Sperre (Einheit 7.2):** Erklären Sie Schritt 2 und 3: Ab welchem Versuch greift die Sperre, und wen trifft sie?
3. **Bewertung (Einheit 7.3):** Beschreiben Sie anhand von Schritt 4 eine bessere Lösung und ihre Nachteile.

#### Kontrollfragen

1. Was bedeutet Status 429?
2. Welches Risiko bringt eine Kontosperre?
3. Was ist besser als eine harte Sperre?
4. Warum nur wenige Fehlversuche testen?

### Modul 8: Bericht und Abschlussprojekt

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Befunde nach Wahrscheinlichkeit und Auswirkung bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende einen Bericht mit Zusammenfassung und Maßnahmenliste erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Vollständigkeit des Berichts prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende ein Abschlussprojekt auf eigenen Systemen planen.
* **Voraussetzungen:** Modul 5; Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Befunde sammeln | 3 |
| 8.2 | Bewertung | 3 |
| 8.3 | Bericht | 3 |
| 8.4 | Abschlussprojekt | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Befunde sammeln (Einheit 8.1):** Führen Sie `bash bericht.sh` aus. Erklären Sie Schritt 1: Woher stammen die Befunde, und was bedeuten W und A?
2. **Bewertung (Einheit 8.2):** Erklären Sie Schritt 2: Wie entsteht das Risiko, und warum liegen B-2 und B-4 gleich?
3. **Bericht (Einheit 8.3):** Lesen Sie Schritt 3 und 4 und formulieren Sie die Zusammenfassung für eine Leitung ohne Fachkenntnisse.
4. **Abschlussprojekt (Einheit 8.4):** Planen Sie einen eigenen Test: Auftragsdatei, Scope, Prüfschritte, Bericht. Führen Sie ihn auf dem eigenen Labor aus.

#### Kontrollfragen

1. Wie wird das Risiko berechnet?
2. Welcher Befund ist am wichtigsten?
3. Warum die Zusammenfassung getrennt?
4. Was prüft Schritt 4?
