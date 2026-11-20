# Lehrplan: E-Mail-Authentifizierung: SPF, DKIM und DMARC

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); DNS-Grundlagen |
| **Gesamtumfang** | 11 Module, 110 UE (zu 45 Minuten; 82,5 Stunden) |
| **Fokus-Technologien** | SPF, DKIM, DMARC, DNS (TXT-Einträge); Postfix als Beispiel-Mailserver; Exchange Online nur als Hinweis |
| **Thematische Abgrenzung (Out of Scope)** | Keine Überschneidung mit vorhandenen Lehrplänen; Verweise nur kurz: Aufbau und Betrieb eines Mailservers im Kurs „Mailserver mit Postfix und Dovecot“, Exchange Online im Kurs „Exchange Online Administration“, DNS-Grundlagen im Kurs über DNS. Nicht behandelt: Betrieb eines öffentlich erreichbaren Mailservers (Reputation, Reverse-DNS, Blocklisten), MTA-STS und DANE, Einrichtung eines Signatur-Dienstes (OpenDKIM als Milter), Betrieb eines Berichts-Auswertungsdienstes, juristische Fragen zu Absenderfälschung |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Warum Absender gefälscht werden können | 1 | 10 |
| 2 | DNS-TXT-Einträge für E-Mail | 1 | 8 |
| 3 | SPF: Aufbau und Auswertung | 1 | 12 |
| 4 | SPF in der Praxis: Grenze von zehn Abfragen | 1 | 10 |
| 5 | DKIM: Signieren und Prüfen | 1 | 12 |
| 6 | DKIM im Betrieb: Selektoren und Schlüsselwechsel | 1 | 10 |
| 7 | DMARC: Richtlinie und Ausrichtung | 1 | 12 |
| 8 | DMARC-Berichte auswerten | 1 | 10 |
| 9 | Schrittweise Einführung und typische Fehler | 1 | 10 |
| 10 | ARC und BIMI im Überblick | 2 | 6 |
| 11 | Gesamtprüfung und Fehlersuche | 1 | 10 |
| **Gesamt** | 11 Module | 10 × Priorität 1, 1 × Priorität 2 | **110** |

**Priorität 1** (Pflicht) sind die Module 1 bis 9 und 11; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 10 (ARC und BIMI im Überblick). Fällt Modul 10 weg, verringert sich der Gesamtumfang auf 104 UE; kein Pflichtmodul setzt Modul 10 voraus.

### 2. Quellen

**Nicht gelesen:** Die Standards zu SPF (RFC 7208), DKIM (RFC 6376), DMARC (RFC 7489), ARC (RFC 8617) und BIMI sowie die Dokumentation von Postfix, OpenDKIM und Exchange Online wurden **nicht** gelesen. Alle Aussagen stammen aus Fachwissen und wurden, soweit möglich, durch die Läufe im Labor bestätigt (pyspf 2.0.14 für SPF, dkimpy 1.1.8 für DKIM, `opendkim-genkey` für Schlüssel). Der Aufbau des DMARC-Berichtsformats in Modul 8 stammt aus Fachwissen und ist **nicht** gegen den Standard geprüft. Angaben zu Exchange Online (z. B. Einrichtung von DKIM im Portal) sind **nicht bestätigt**.

**Getestet mit:** Postfix 3.8.6, dnsmasq, OpenDKIM-Werkzeuge (`opendkim-genkey`), pyspf, dkimpy, dnspython, swaks, Python 3 (Ubuntu 24.04). Die Beispieldaten (Domains, Adressen, Berichte, Mengen) sind **frei erfunden**; es wird ausschließlich `example.com` (reservierte Beispiel-Domain) mit `example.net` und `example.org` verwendet.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Auth`, `10.38.0.0/24`).

**VMs:** `dns01` (**erforderlich**, `10.38.0.2`): Linux mit einem DNS-Server (z. B. BIND 9 oder dnsmasq) für die Zonen `example.com` und `example.org`, in denen die TXT-Einträge gepflegt werden. `mail01` (**erforderlich**, `10.38.0.3`): Ubuntu Server 24.04 oder Debian 12 mit `postfix`, `swaks`, `opendkim-tools`, Python 3 mit den Paketen `pyspf`, `dkimpy` und `dnspython`; als DNS-Server `dns01` eintragen. Kein Windows nötig.

**Internetphase:** Für die Paketinstallation braucht `mail01` vorübergehend Internetzugang (zweite Netzwerkkarte an einem externen Switch); danach wird sie entfernt. Es wird **keine** echte Domain verändert und kein Mail an fremde Server gesendet.

**Prüfpunkt (Checkpoint):** Vor Modul 3 und vor Modul 7 von `dns01` und `mail01` je einen Prüfpunkt anlegen.

**Skripte:** Die Beispielskripte liefen **nicht** in Hyper-V, sondern in einem Cloud-Container mit einer **privaten Instanz** (`lab.sh`): dnsmasq als DNS auf `127.0.0.1:5353` (Python-Skripte fragen ihn über `dnsconf.py`), Postfix auf `127.0.0.1:2525`, Arbeitsordner `/tmp/p38`, Test-Konten `t38alice` und `t38bob`. Auf `dns01`/`mail01` gelten die Standardports.

## B. Detaillierter Modulaufbau

### Modul 1: Warum Absender gefälscht werden können

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, warum Absenderangaben in E-Mails ohne Zusatzverfahren frei wählbar sind.
  * Nach Abschluss dieses Moduls kann der Lernende Umschlag-Absender und Header-From unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende eine gefälschte Nachricht im Labor erzeugen und im Postfach erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Aufgabe und Prüfgegenstand von SPF, DKIM und DMARC nennen.
* **Voraussetzungen:** IP-Adressen und Ports; Grundlagen des E-Mail-Versands (Kurs „Mailserver mit Postfix und Dovecot“, Modul 1).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | SMTP kennt keinen Absendernachweis: Umschlag-Absender (MAIL FROM) und Header-From | 3 |
| 1.2 | Praxis: gefälschte Nachricht an ein lokales Postfach senden (`faelschung.sh`) | 3 |
| 1.3 | Angriffsarten: Phishing, Chef-Betrug, Missbrauch der eigenen Domain; Folgen für die Zustellbarkeit | 2 |
| 1.4 | Überblick der drei Verfahren: SPF, DKIM, DMARC und was jedes prüft | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Zwei Absender unterscheiden (Einheit 1.1):** Erklären Sie, wo in einer Nachricht der Umschlag-Absender (`MAIL FROM`, später `Return-Path`) und wo der Header-From steht und welcher von beiden das Mailprogramm anzeigt.
2. **Fälschung erzeugen (Einheit 1.2):** Senden Sie im Labor mit `swaks` eine Nachricht mit `--from zufall@example.org` und `--h-From "Chef <chef@example.com>"` an ein lokales Postfach (`faelschung.sh`). Lesen Sie danach `Return-Path` und `From` im Postfach.
3. **Folgen beschreiben (Einheit 1.3):** Beschreiben Sie in je zwei Sätzen, was ein Angreifer mit einer gefälschten Absenderadresse der eigenen Firma erreichen kann (Phishing gegen Kunden, Chef-Betrug) und was das für die Zustellbarkeit eigener Mails bedeutet.
4. **Verfahren zuordnen (Einheit 1.4):** Ordnen Sie SPF, DKIM und DMARC je einer Frage zu: „Darf dieser Server für die Domain senden?“, „Wurde die Nachricht unterwegs verändert?“, „Was soll der Empfänger tun, wenn die Prüfung scheitert?“

#### Kontrollfragen

1. Warum prüft ein normaler Mailserver nicht, ob der Absender „echt“ ist?
2. Welche der beiden Absenderangaben sieht der Benutzer im Mailprogramm?
3. Warum reicht SPF allein nicht, um eine gefälschte From-Zeile zu erkennen?
4. Was bedeutet „Authentifizierung“ hier: Benutzer oder Domain?

### Modul 2: DNS-TXT-Einträge für E-Mail

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines TXT-Eintrags und die Begrenzung von 255 Zeichen je Abschnitt erklären.
  * Nach Abschluss dieses Moduls kann der Lernende lange Werte in Abschnitte teilen und wieder zusammensetzen.
  * Nach Abschluss dieses Moduls kann der Lernende TXT-Einträge mit `dig` abfragen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Formatfehler erkennen.
* **Voraussetzungen:** Modul 1; DNS-Grundlagen (Eintragstypen).

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | TXT-Einträge: Aufbau, Zeichenkettenabschnitte (höchstens 255 Zeichen), Anführungszeichen | 3 |
| 2.2 | Praxis: kurzen SPF-Eintrag und langen DKIM-Schlüssel anlegen und abfragen (`dns_txt.sh`, `txt_split.py`) | 3 |
| 2.3 | Typische Fehler: fehlendes Semikolon, Leerzeichen im Schlüssel, doppelte Einträge | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eintrag lesen (Einheit 2.1):** Fragen Sie mit `dig TXT example.com` den SPF-Eintrag ab und erklären Sie Anfang (`v=spf1`) und Ende (`-all`).
2. **Langen Wert teilen (Einheit 2.2):** Erzeugen Sie mit `openssl` einen 2048-Bit-Schlüssel, bilden Sie den öffentlichen Teil als Base64-Text und teilen Sie `v=DKIM1; k=rsa; p=…` mit `txt_split.py` in Abschnitte. Legen Sie ihn im DNS an (`dns_txt.sh`).
3. **Abfrage vergleichen (Einheit 2.2):** Fragen Sie den Eintrag mit `dig` ab (mehrere Abschnitte) und mit Python (ein zusammengesetzter Wert). Prüfen Sie, dass beide denselben Text ergeben.
4. **Fehler finden (Einheit 2.3):** Prüfen Sie die drei Beispielwerte im Skript (richtig, ohne Semikolon, Leerzeichen im Schlüssel) und erklären Sie, wie ein empfangender Server auf die fehlerhaften Werte reagieren würde.

#### Kontrollfragen

1. Warum werden lange TXT-Werte in Abschnitte geteilt?
2. Wie setzt ein Empfänger die Abschnitte zusammen?
3. Warum ist ein Leerzeichen mitten im Schlüssel ein Fehler?
4. Warum sollte es pro Name nur einen SPF-Eintrag geben?

### Modul 3: SPF: Aufbau und Auswertung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von SPF und den Prüfgegenstand erklären.
  * Nach Abschluss dieses Moduls kann der Lernende einen SPF-Eintrag mit Mechanismen und Qualifizierern lesen und schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende die sieben Ergebnisse unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Grenzen von SPF nennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Idee: eine Domain nennt die Server, die für sie senden dürfen; geprüft wird die Domain des Umschlag-Absenders (und HELO) | 3 |
| 3.2 | Syntax: `v=spf1`, Mechanismen (`ip4`, `a`, `mx`, `include`, `all`) und Qualifizierer (`+`, `-`, `~`, `?`) | 3 |
| 3.3 | Ergebnisse: pass, fail, softfail, neutral, none, permerror, temperror (`spf.sh`, `spf_pruefen.py`) | 3 |
| 3.4 | Grenzen: Weiterleitung, Mailinglisten, Header-From wird nicht geprüft | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eintrag lesen (Einheit 3.2):** Erklären Sie den Eintrag `v=spf1 ip4:192.0.2.0/28 mx -all` Wort für Wort.
2. **Eintrag schreiben (Einheit 3.2):** Schreiben Sie einen SPF-Eintrag für eine Domain, die nur über ihren MX und einen externen Dienst (`include:dienst-a.example.com`) sendet und alles andere ablehnt.
3. **Ergebnisse prüfen (Einheit 3.3):** Führen Sie `spf.sh` aus (oder `python3 spf_pruefen.py`) und ordnen Sie jedem Ergebnis der Tabelle den Grund zu (z. B. `softfail` bei `~all`).
4. **Grenzen erklären (Einheit 3.4):** Erklären Sie, warum eine weitergeleitete Nachricht SPF verletzt und warum SPF die From-Zeile nicht schützt.
5. **Idee erklären (Einheit 3.1):** Erklären Sie in drei Sätzen, wer bei SPF welche Domain prüft und was der Eintrag der Domain angibt.

#### Kontrollfragen

1. Was ist der Unterschied zwischen `-all`, `~all` und `?all`?
2. Welches Ergebnis liefert die Prüfung bei zwei SPF-Einträgen einer Domain?
3. Warum scheitert SPF bei weitergeleiteten Nachrichten?
4. Welche Domain prüft SPF: die im Header-From oder die im Umschlag?

### Modul 4: SPF in der Praxis: Grenze von zehn Abfragen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende `include` für externe Absender einsetzen.
  * Nach Abschluss dieses Moduls kann der Lernende erklären, welche Mechanismen zur Grenze von zehn Abfragen zählen.
  * Nach Abschluss dieses Moduls kann der Lernende die Abfragen eines Eintrags zählen und die Grenze testen.
  * Nach Abschluss dieses Moduls kann der Lernende Maßnahmen gegen ein Überschreiten nennen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Dienstleister einbinden: `include`, Reihenfolge, Pflegeaufwand | 2 |
| 4.2 | Die Grenze von zehn Abfragen: was zählt und was nicht | 3 |
| 4.3 | Praxis: Abfragen zählen und Ketten testen (`spf_limit.sh`, `spf_lookups.py`) | 3 |
| 4.4 | Abhilfe: direkte IP-Angaben, weniger Dienste, getrennte Subdomains | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Dienstleister einbinden (Einheit 4.1):** Schreiben Sie einen Eintrag, der zwei Dienstleister per `include` und den eigenen MX erlaubt. Zählen Sie die Abfragen.
2. **Grenze testen (Einheit 4.3):** Führen Sie `spf_limit.sh` aus und lesen Sie, bei welcher Kettenlänge `permerror` entsteht.
3. **Zähler prüfen (Einheit 4.3):** Rufen Sie `python3 spf_lookups.py kurz.example.com kette1.example.com flach.example.com` auf und vergleichen Sie Zähler und Ergebnis von pyspf.
4. **Abhilfe wählen (Einheit 4.4):** Ein Eintrag überschreitet die Grenze. Schlagen Sie drei Maßnahmen vor und nennen Sie je einen Nachteil (z. B. feste IP-Adressen veralten).
5. **Zählregel erklären (Einheit 4.2):** Erklären Sie, welche Mechanismen auf die Grenze von zehn Abfragen zählen und welche nicht (teils am Skript geprüft).

#### Kontrollfragen

1. Welche Mechanismen zählen zur Grenze, welche nicht?
2. Warum gibt es die Grenze?
3. Was ist ein Nachteil, Dienstleister durch feste `ip4`-Angaben zu ersetzen?
4. Warum ist die Prüfung nach dem Überschreiten nicht „weniger streng“, sondern fehlerhaft?

### Modul 5: DKIM: Signieren und Prüfen

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf von DKIM beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende ein Schlüsselpaar erzeugen und den öffentlichen Teil veröffentlichen.
  * Nach Abschluss dieses Moduls kann der Lernende die Felder der Kopfzeile `DKIM-Signature` deuten.
  * Nach Abschluss dieses Moduls kann der Lernende Veränderungen erkennen, die die Signatur ungültig machen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | Idee: der sendende Server signiert ausgewählte Kopfzeilen und den Text; der öffentliche Schlüssel steht im DNS | 3 |
| 5.2 | Schlüsselpaar erzeugen (`opendkim-genkey`) und veröffentlichen; Aufbau des Eintrags `selektor._domainkey.domain` | 3 |
| 5.3 | Signieren und Prüfen mit Python (`dkim_signieren.py`); Aufbau der Kopfzeile `DKIM-Signature` | 3 |
| 5.4 | Was eine Signatur bricht: Änderungen am Text, am Betreff, an Fußzeilen; was sie nicht bricht | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Ablauf zeichnen (Einheit 5.1):** Zeichnen Sie den Ablauf: Server signiert, Nachricht läuft, Empfänger holt den Schlüssel per DNS, berechnet den Hash und vergleicht.
2. **Schlüssel erzeugen (Einheit 5.2):** Erzeugen Sie mit `opendkim-genkey -b 2048 -d example.com -s sel1` ein Schlüsselpaar und veröffentlichen Sie den öffentlichen Teil als TXT-Eintrag (`dkim.sh`).
3. **Signieren und prüfen (Einheit 5.3):** Signieren Sie eine Nachricht mit `dkim_signieren.py` und lesen Sie die Felder `d`, `s`, `a`, `c`, `h`, `bh` und `b`. Notieren Sie, was jedes Feld bedeutet.
4. **Veränderungen testen (Einheit 5.4):** Werten Sie die fünf Testfälle der Tabelle aus (unverändert, Text, Betreff, Zusatzzeile, Fußzeile) und begründen Sie je Ergebnis.

#### Kontrollfragen

1. Warum steht der öffentliche Schlüssel im DNS und der private nicht?
2. Was bedeutet das Feld `h=` in der Signatur?
3. Warum bricht eine angehängte Fußzeile einer Mailingliste die Signatur?
4. Warum besteht die Prüfung, wenn eine nicht signierte Kopfzeile hinzugefügt wird?

### Modul 6: DKIM im Betrieb: Selektoren und Schlüsselwechsel

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von Selektoren erklären.
  * Nach Abschluss dieses Moduls kann der Lernende eine Signatur auf Mindestanforderungen prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Schlüsselwechsel mit Überlappung durchführen.
  * Nach Abschluss dieses Moduls kann der Lernende die Folgen des zu frühen Entfernens eines Schlüssels beschreiben.
* **Voraussetzungen:** Modul 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Selektoren: mehrere Schlüssel nebeneinander (Dienste, Zeiträume) | 2 |
| 6.2 | Qualität einer Signatur prüfen: `h=` mit From, Algorithmus, `d=` passend zur From-Domain (`dkim_tags.py`) | 3 |
| 6.3 | Schlüsselwechsel mit Überlappung (`dkim_rotation.sh`) | 3 |
| 6.4 | Folgen eines zu frühen Löschens und Aufbewahrung alter Schlüssel | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Selektoren planen (Einheit 6.1):** Legen Sie für eine Firma Selektoren fest (eigener Mailserver, Newsletter-Dienst, Rechnungssystem) und für den Schlüsselwechsel (Jahr/Buchstabe).
2. **Signatur prüfen (Einheit 6.2):** Lesen Sie mit `dkim_tags.py` die Signatur einer Nachricht und bewerten Sie die fünf Prüfpunkte.
3. **Schlüssel wechseln (Einheit 6.3):** Führen Sie `dkim_rotation.sh` aus: neuen Selektor veröffentlichen, neue Nachrichten damit signieren, beide Schlüssel parallel gültig lassen.
4. **Fehlbedienung auswerten (Einheit 6.4):** Erklären Sie das Ergebnis, wenn der alte Schlüssel entfernt wird, bevor alle alten Nachrichten geprüft sind (z. B. Nachrichten im Postfach, die später weitergeleitet werden).

#### Kontrollfragen

1. Warum wird beim Wechsel nicht einfach der Schlüssel unter demselben Selektor ersetzt?
2. Wie lange sollte der alte Schlüssel im DNS bleiben?
3. Welche Prüfpunkte machen eine Signatur für DMARC brauchbar?
4. Warum signiert man mit rsa-sha256 und nicht mit sha1?

### Modul 7: DMARC: Richtlinie und Ausrichtung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende erklären, was DMARC zusätzlich zu SPF und DKIM leistet.
  * Nach Abschluss dieses Moduls kann der Lernende einen DMARC-Eintrag lesen und schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Ausrichtung relaxed und strict unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende das DMARC-Ergebnis aus SPF- und DKIM-Ergebnissen herleiten.
* **Voraussetzungen:** Module 3 und 5.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Idee: DMARC verknüpft SPF und DKIM mit der From-Domain und legt die Richtlinie fest | 3 |
| 7.2 | Der Eintrag `_dmarc`: `p`, `sp`, `pct`, `rua`, `adkim`, `aspf` | 3 |
| 7.3 | Ausrichtung (Alignment): relaxed und strict; Suche nach Organisationsdomain (`dmarc.sh`, `dmarc_pruefen.py`) | 3 |
| 7.4 | Bestehen: SPF **oder** DKIM ausgerichtet; Richtlinien none, quarantine, reject | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Eintrag lesen (Einheit 7.2):** Erklären Sie `v=DMARC1; p=quarantine; sp=reject; pct=100; rua=mailto:dmarc-berichte@example.com; adkim=r; aspf=r`.
2. **Eintrag schreiben (Einheit 7.2):** Schreiben Sie einen Eintrag für die Domain `example.com`: Richtlinie nur beobachten, Berichte an eine Adresse, strenge Ausrichtung für SPF.
3. **Fälle auswerten (Einheit 7.3):** Führen Sie `dmarc.sh` aus und erklären Sie für jeden der neun Fälle das Ergebnis (z. B. „SPF besteht, aber andere Domain“).
4. **Regel formulieren (Einheit 7.4):** Formulieren Sie die DMARC-Bestehensregel in einem Satz und nennen Sie, warum sie bei weitergeleiteten Nachrichten oft über DKIM erfüllt wird.
5. **Idee erklären (Einheit 7.1):** Erklären Sie in drei Sätzen, wie DMARC SPF und DKIM mit der From-Domain verknüpft und was die Richtlinie festlegt.

#### Kontrollfragen

1. Welche zwei Bedingungen müssen für ein DMARC-pass zusammenkommen?
2. Was ändert `adkim=s` im Vergleich zu `adkim=r`?
3. Was gilt für eine Subdomain, die keinen eigenen DMARC-Eintrag hat?
4. Warum sollte man mit `p=none` beginnen?

### Modul 8: DMARC-Berichte auswerten

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau eines Aggregatberichts beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende einen Bericht mit Python auswerten.
  * Nach Abschluss dieses Moduls kann der Lernende Quellen als eigen, beauftragt oder unbekannt einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Handlungsbedarf aus einem Bericht ableiten.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Aggregatberichte (`rua`): Aufbau, Inhalte, was sie nicht enthalten | 3 |
| 8.2 | Praxis: Bericht (XML) mit Python auswerten (`dmarc_bericht.py`) | 3 |
| 8.3 | Quellen zuordnen: eigene Server, beauftragte Dienste, Fälschungen | 2 |
| 8.4 | Datenschutz und Aufbewahrung der Berichte | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Struktur lesen (Einheit 8.1):** Öffnen Sie `beispiel_bericht.xml` und markieren Sie Berichtskopf, veröffentlichte Richtlinie und die Datensätze.
2. **Bericht auswerten (Einheit 8.2):** Führen Sie `python3 dmarc_bericht.py beispiel_bericht.xml` aus und notieren Sie Gesamtzahl, Anteil pass und die Quellen mit fail.
3. **Quellen zuordnen (Einheit 8.3):** Ordnen Sie jede Quelle zu (eigener Server, beauftragter Dienst, unbekannt) und begründen Sie, warum die Zeile mit SPF-pass und DKIM-fail dennoch DMARC-pass ergibt.
4. **Datenschutz bedenken (Einheit 8.4):** Nennen Sie zwei Datenschutzfragen beim Sammeln der Berichte (z. B. IP-Adressen, Aufbewahrungsdauer) ohne Rechtsaussage.

#### Kontrollfragen

1. Wozu dient der Aggregatbericht im Unterschied zu einem Einzelfallbericht?
2. Warum gehört die zweite Zeile der eigenen IP (SPF pass, DKIM fail) nicht zu den Fehlern?
3. Warum ist eine unbekannte Quelle nicht automatisch eine Fälschung?
4. Warum genügt ein einziger Bericht nicht für eine Entscheidung?

### Modul 9: Schrittweise Einführung und typische Fehler

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Phasenplan für die Einführung von DMARC aufstellen.
  * Nach Abschluss dieses Moduls kann der Lernende die Wirkung einer Richtlinie auf legitime und gefälschte Mails abschätzen.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehler benennen und vermeiden.
  * Nach Abschluss dieses Moduls kann der Lernende einen Rückfallplan formulieren.
* **Voraussetzungen:** Module 7 und 8.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 9.1 | Phasenplan: Bestandsaufnahme, p=none, Quellen beheben, quarantine mit wachsendem pct, reject | 3 |
| 9.2 | Wirkung abschätzen: wie viele legitime Mails wären betroffen (`einfuehrung.py`) | 3 |
| 9.3 | Typische Fehler: vergessene Dienstleister, Weiterleitungen, Mailinglisten, zu schneller Wechsel auf reject | 2 |
| 9.4 | Ausnahmen und Kommunikation: Dienstleister, Fachabteilungen, Rückfallplan | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Quellen sammeln (Einheit 9.1):** Erstellen Sie eine Liste aller Systeme, die für Ihre Domain E-Mails senden (Mailserver, Newsletter, Rechnungen, Drucker, Webformulare, Dienstleister) mit Verantwortlichem.
2. **Wirkung berechnen (Einheit 9.2):** Führen Sie `python3 einfuehrung.py` aus und lesen Sie, wie viele legitime Mails bei `quarantine` und `reject` betroffen wären und welche Quellen zu beheben sind.
3. **Phasenplan schreiben (Einheit 9.1):** Schreiben Sie einen Plan mit Phasen, Dauer (Annahmen kennzeichnen) und Kriterien für den Wechsel (z. B. „legitime Fehlerquote unter 1 %“).
4. **Rückfallplan (Einheit 9.4):** Beschreiben Sie, was Sie tun, wenn nach dem Wechsel auf `reject` ein wichtiger Absender abgewiesen wird (Meldeweg, DNS-Änderung, Zeit bis zur Wirkung).
5. **Typische Fehler sammeln (Einheit 9.3):** Nennen Sie vier typische Fehler bei der Einführung von DMARC und je eine Gegenmaßnahme.

#### Kontrollfragen

1. Warum beginnt man mit `p=none` und nicht gleich mit `reject`?
2. Wozu dient `pct` beim Wechsel auf `quarantine`?
3. Warum verursachen Mailinglisten und Weiterleitungen besondere Probleme?
4. Warum braucht man einen Rückfallplan?

### Modul 10: ARC und BIMI im Überblick

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Problem nennen, das ARC lösen soll.
  * Nach Abschluss dieses Moduls kann der Lernende den Aufbau einer ARC-Kette lesen.
  * Nach Abschluss dieses Moduls kann der Lernende den Zweck von BIMI beschreiben und die Voraussetzungen nennen.
* **Voraussetzungen:** Modul 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 10.1 | ARC: Problem bei Weiterleitungen und Mailinglisten; Kette aus Siegel, Signatur und Ergebnis je Station | 3 |
| 10.2 | Praxis: Aufbau einer ARC-Kette prüfen (`arc_header.py`, ohne kryptografische Prüfung) | 2 |
| 10.3 | BIMI: Logo im Postfach als Zusatz; Voraussetzungen im Überblick | 1 |

#### Praxisaufgaben (Hands-on Lab)

1. **Problem beschreiben (Einheit 10.1):** Beschreiben Sie, warum eine Mailingliste die DKIM-Signatur bricht und wie ARC dem nächsten Empfänger den ursprünglichen Zustand mitteilt.
2. **Kette prüfen (Einheit 10.2):** Führen Sie `arc_header.py` an der Beispielnachricht aus und erklären Sie `i=`, `cv=` und die drei Zeilen je Station.
3. **BIMI bewerten (Einheit 10.3):** Beurteilen Sie die drei BIMI-Beispieleinträge der Ausgabe und nennen Sie, was fehlt.

#### Kontrollfragen

1. Wofür steht `i=` in den ARC-Zeilen?
2. Was sagt `cv=` aus?
3. Warum garantiert ARC allein nicht die Zustellung?

### Modul 11: Gesamtprüfung und Fehlersuche

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SPF, DKIM und DMARC gemeinsam einrichten und prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Ergebnisse einer Prüfung deuten.
  * Nach Abschluss dieses Moduls kann der Lernende typische Fehlerbilder systematisch eingrenzen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Prüfliste für die eigene Domain schreiben.
* **Voraussetzungen:** Module 1 bis 9.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 11.1 | Alles zusammen: DNS-Einträge, signierter Versand, Zustellung und Prüfung (`gesamt.sh`) | 3 |
| 11.2 | Ergebnisse lesen im Stil von `Authentication-Results`: spf, dkim, dmarc | 2 |
| 11.3 | Fehlersuche: Checkliste von DNS über Selektor bis Ausrichtung; Prüfwerkzeuge | 3 |
| 11.4 | Abschlussübung und Selbstprüfung | 2 |

#### Praxisaufgaben (Hands-on Lab)

1. **Gesamtlauf ausführen (Einheit 11.1):** Führen Sie `gesamt.sh` aus: SPF, DKIM-Schlüssel und DMARC einrichten, drei Nachrichten senden (echt, gefälscht, über Mailingliste verändert) und prüfen.
2. **Ergebnisse deuten (Einheit 11.2):** Erklären Sie für jede der drei Nachrichten, warum SPF, DKIM und DMARC so ausfallen und welche Maßnahme der Empfänger trifft.
3. **Fehler eingrenzen (Einheit 11.3):** Eine Nachricht von Ihrer Domain landet beim Empfänger im Spam. Beschreiben Sie in Schritten die Suche (Header lesen, DNS prüfen, Selektor, Ausrichtung, Berichte).
4. **Prüfliste schreiben (Einheit 11.4):** Schreiben Sie eine Prüfliste mit mindestens zehn Punkten für die Einführung von SPF, DKIM und DMARC (Einträge, Tests, Berichte, Rückfall).

#### Kontrollfragen

1. Warum besteht DMARC bei der über die Mailingliste veränderten Nachricht trotz ungültiger DKIM-Signatur?
2. Warum wird die gefälschte Nachricht trotz bestandenem SPF abgelehnt?
3. Welche Zeile im Header zeigt, welche Prüfungen der Empfänger durchgeführt hat?
4. Welche zwei Dinge prüft man bei „dkim=fail“ zuerst?
