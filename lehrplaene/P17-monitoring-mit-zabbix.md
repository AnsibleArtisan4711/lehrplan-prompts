# Lehrplan: Monitoring mit Zabbix

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen, Subnetze); Linux-Grundlagen (Shell, Dienste, Textdateien); Grundkenntnisse in Datenbanken sind hilfreich |
| **Gesamtumfang** | 8 Module, 100 UE (zu 45 Minuten; 75 Stunden) |
| **Fokus-Technologien** | Architektur (Server, Proxy, Agent), Installation, Hosts, Items und Trigger, Vorlagen, SNMP und Agent, Auto-Discovery, Benachrichtigungen, Dashboards, Wartungsfenster, Leistung und Betrieb, Sicherung |
| **Thematische Abgrenzung (Out of Scope)** | Zabbix-Server, Zabbix-Agent, `zabbix_get`, `zabbix_sender`, Frontend-API (PHP) und PostgreSQL laufen in den Übungen **wirklich**; Zabbix **7.0.32** wurde dafür **aus dem Quellcode** gebaut (Ubuntu 24.04 hat keine Zabbix-Pakete). Die **Installation aus den Paketen von zabbix.com**, der **Windows-Agent**, der **Proxy**, SNMPv3 und SNMP-Traps sowie die **Darstellung im Browser** wurden **nicht** ausgeführt (nur als Text oder nicht behandelt). Messwerte stammen vom Container (Last, Prozesse) oder sind erfunden. Nicht behandelt: Hochverfügbarkeit, verschlüsselte Verbindungen (TLS), Benutzerverwaltung im Detail, Prometheus (siehe P18), Logs (siehe P19). |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
|---|---|---|---|
| 1 | Architektur und Datenmodell | 1 | 12 |
| 2 | Installation | 1 | 12 |
| 3 | Hosts, Items und Trigger | 1 | 16 |
| 4 | Vorlagen und Agent | 1 | 12 |
| 5 | SNMP | 1 | 14 |
| 6 | Auto-Discovery | 2 | 12 |
| 7 | Benachrichtigungen, Dashboards und Wartungsfenster | 1 | 12 |
| 8 | Leistung, Betrieb und Sicherung | 1 | 10 |
| **Gesamt** | 8 Module | 7 × Priorität 1, 1 × Priorität 2 | **100** |

**Priorität 1** (Pflicht) sind die Module 1 bis 5, 7 und 8; **Priorität 2** (Vertiefung, bei Zeitmangel entfallbar) ist Modul 6 (Auto-Discovery). Fällt Modul 6 weg, verringert sich der Gesamtumfang auf 88 UE; kein Pflichtmodul setzt Modul 6 voraus.

### 2. Quellen

**Gelesen:** Für diese Übungsreihe wurden **keine** Seiten der Zabbix-Dokumentation vollständig gelesen. Aufbau, Befehle und API-Aufrufe stammen aus Fachwissen und wurden durch Ausführen gegen den selbst gebauten Zabbix 7.0.32 geprüft. **Standardports** (10050, 10051, 80/443), Paketnamen, Dateipfade der Pakete, Menünamen des Frontends sowie das Verhalten von Proxy, SNMPv3 und Windows-Agent sind **nicht bestätigt**. Zahlen zu Vorlagen und Datenbank (356 Vorlagen, 203 Tabellen) gelten für **7.0.32** und ändern sich mit der Version.

**Getestet mit (Ubuntu 24.04, Cloud-Container, kein systemd):** Zabbix 7.0.32 (Server, Agent, `zabbix_get`, `zabbix_sender`, Frontend/API mit PHP 8.3, aus dem Quellcode gebaut), PostgreSQL 16, `snmpd`/`snmpget`/`snmpwalk` (net-snmp 5.9.4), `jq`, `curl`, Python 3. **Nicht ausgeführt:** Pakete von zabbix.com, Windows-Agent, Proxy, Browser-Frontend, SNMPv3, SNMP-Traps, E-Mail-Versand, systemd, Hyper-V.

### 3. Labor-Setup & Rahmenbedingungen

**Hypervisor:** Hyper-V. **Switch:** ein privater Switch ohne Verbindung zum Heimnetz (`Lab-Zabbix`, `10.17.0.0/24`).

**VM 1:** `zbx01` (**erforderlich**, `10.17.0.10`): Ubuntu Server (LTS) mit Zabbix-Server, Frontend und Datenbank; Rechte: `sudo`.

**VM 2:** `lin01` (**erforderlich**, `10.17.0.21`): Ubuntu Server als überwachter Host mit Zabbix-Agent und `snmpd`.

**VM 3:** `win01` (**erforderlich**, `10.17.0.31`): Windows als überwachter Host mit Zabbix-Agent (Module 3 und 4, nur als Beschreibung).

**Internetphase:** Für die Installation der Pakete brauchen `zbx01` und `lin01` vorübergehend Internetzugang; danach wird der Zugang entfernt. Lizenzen für Windows sind selbst zu beschaffen.

**Prüfpunkt (Checkpoint):** Vor Modul 5 und vor Modul 8 von `zbx01` einen Prüfpunkt anlegen. Prüfpunkte sind **keine** Datensicherung.

**Skripte:** Die Skripte erwarten den selbst gebauten Zabbix unter `/opt/zbx` (siehe `aufbau-container.sh`) und starten ihre eigenen Prozesse auf `127.0.0.1` (Ports 11050, 11051, 11161, 15432, 18080); sie arbeiten unter `/tmp/p17` und sind im Labor **nicht** ohne Anpassung der Pfade lauffähig.

## B. Detaillierter Modulaufbau

### Modul 1: Architektur und Datenmodell

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Server, Agent, Datenbank und Frontend sowie ihre Wege benennen.
  * Nach Abschluss dieses Moduls kann der Lernende passive und aktive Agentenprüfungen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende die Prozesse des Servers und ihre Anzahl lesen.
  * Nach Abschluss dieses Moduls kann der Lernende Aufbau der Datenbank und mitgelieferte Objekte erkunden.
* **Voraussetzungen:** IT-Grundlagen.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 1.1 | Bausteine und Prozesse | 4 |
| 1.2 | Passiv und aktiv | 4 |
| 1.3 | Datenmodell | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Bausteine und Prozesse (Einheit 1.1):** Führen Sie `bash architektur.sh` aus. Erklären Sie Schritt 1 und 2: Welche Versionen laufen, und wofür stehen Poller, History Syncer und Housekeeper?
2. **Passiv und aktiv (Einheit 1.2):** Erklären Sie Schritt 3 und 4: Wer fragt wen, und warum wird der unbekannte Host in Schritt 4 abgelehnt?
3. **Datenmodell (Einheit 1.3):** Erklären Sie Schritt 5 und 6: Was enthalten `hosts`, `items`, `triggers`, und warum gibt es 356 „Hosts“ mit Status 3?

#### Kontrollfragen

1. Wer fragt bei einer passiven Prüfung?
2. Wer fragt bei einer aktiven Prüfung?
3. Was bedeutet `ZBX_NOTSUPPORTED`?
4. Warum stehen in `hosts` auch Vorlagen?

### Modul 2: Installation

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Datenbank anlegen und Schema in der richtigen Reihenfolge einspielen.
  * Nach Abschluss dieses Moduls kann der Lernende Server und Agent konfigurieren und starten.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerbilder (falscher Datenbankanschluss) im Protokoll erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Standardkennwort ändern und Laufzeitbefehle (`-R`) nutzen.
* **Voraussetzungen:** Modul 1.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 2.1 | Datenbank und Server | 4 |
| 2.2 | Agent und Frontend | 4 |
| 2.3 | Laufzeitbefehle und Pakete | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Datenbank und Server (Einheit 2.1):** Führen Sie `bash installation.sh` aus. Erklären Sie Schritt 1 bis 3: In welcher Reihenfolge werden die SQL-Dateien eingespielt, und was zeigt das Protokoll beim falschen und beim richtigen Start?
2. **Agent und Frontend (Einheit 2.2):** Erklären Sie Schritt 4 und 5: Was prüft `zabbix_agentd -t`, welche PHP-Module sind nötig, und warum muss das Standardkennwort sofort geändert werden?
3. **Laufzeitbefehle und Pakete (Einheit 2.3):** Erklären Sie Schritt 6 und 7: Was bewirken die `-R`-Befehle, und was ist am Paketweg **nicht** bestätigt?

#### Kontrollfragen

1. In welcher Reihenfolge werden die SQL-Dateien eingespielt?
2. Woran erkennt man den falschen Datenbankanschluss?
3. Was tut `zabbix_agentd -t`?
4. Wurde die Paketinstallation ausgeführt?

### Modul 3: Hosts, Items und Trigger

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 16 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Host-Gruppe, Host und Schnittstelle über die API anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Items mit Schlüssel, Datentyp und Intervall definieren.
  * Nach Abschluss dieses Moduls kann der Lernende Trigger mit Ausdruck und Wiederherstellungsausdruck (Hysterese) schreiben.
  * Nach Abschluss dieses Moduls kann der Lernende nicht unterstützte Items und fehlerhafte Ausdrücke erkennen.
* **Voraussetzungen:** Modul 2.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 3.1 | Host und Items | 4 |
| 3.2 | Unterstützt oder nicht | 4 |
| 3.3 | Trigger und Hysterese | 4 |
| 3.4 | Ereignisse | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Host und Items (Einheit 3.1):** Führen Sie `bash hosts.sh` aus. Erklären Sie Schritt 1 und 2: Was legen die API-Aufrufe an, und welche Datentypen haben die vier Items?
2. **Unterstützt oder nicht (Einheit 3.2):** Erklären Sie Schritt 3: Warum wird `kein.schluessel` „nicht unterstützt“, und woran sieht man das in der Datenbank?
3. **Trigger und Hysterese (Einheit 3.3):** Erklären Sie Schritt 4 und 5: Warum bleibt das Problem bei Wert 70 bestehen, und was zeigen die beiden Fehlermeldungen bei falschen Ausdrücken?
4. **Ereignisse (Einheit 3.4):** Erklären Sie Schritt 6: Welche Ereignisse entstehen, und wann ist das Problem geschlossen?

#### Kontrollfragen

1. Was bedeutet `state=1` beim Item?
2. Warum bleibt der Trigger bei 70 im Problem?
3. Was meldet die API bei unbekanntem Schlüssel im Ausdruck?
4. Welche Ereignisse entstehen im Ablauf?

### Modul 4: Vorlagen und Agent

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Vorlage mit Item, Makro und Trigger anlegen und verknüpfen.
  * Nach Abschluss dieses Moduls kann der Lernende Makros auf Host-Ebene überschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Vorverarbeitung (Multiplikator) nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende aktive Prüfungen und `zabbix_sender` mit Trapper-Items einsetzen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 4.1 | Vorlage und Vererbung | 4 |
| 4.2 | Vorverarbeitung und Makros | 4 |
| 4.3 | Aktiv, Sender und mitgelieferte Vorlagen | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Vorlage und Vererbung (Einheit 4.1):** Führen Sie `bash vorlagen.sh` aus. Erklären Sie Schritt 1 und 2: Was erbt der Host von der Vorlage?
2. **Vorverarbeitung und Makros (Einheit 4.2):** Erklären Sie Schritt 3 und 4: Wie wird aus 2048 der Wert 2097152, und warum löst derselbe Messwert 50 erst mit dem Host-Makro 30 ein Problem aus?
3. **Aktiv, Sender und mitgelieferte Vorlagen (Einheit 4.3):** Erklären Sie Schritt 5 bis 8: Was ist an der aktiven Prüfung anders, was meldet `zabbix_sender` bei falschem Host, und was wurde bei Windows **nicht** ausgeführt?

#### Kontrollfragen

1. Wozu dienen Makros?
2. Was bewirkt der Multiplikator 1024?
3. Was meldet `zabbix_sender` bei unbekanntem Host?
4. Wie viele Items hat „Linux by Zabbix agent“ in 7.0.32?

### Modul 5: SNMP

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 14 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SNMP vor dem Einsatz in Zabbix mit `snmpget`/`snmpwalk` prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Host mit SNMP-Schnittstelle (v2c, Gemeinschaft als Makro) anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende SNMP-Items mit OID und Vorverarbeitung („Änderung je Sekunde“) anlegen.
  * Nach Abschluss dieses Moduls kann der Lernende Fehlerbilder (falsche Gemeinschaft, fehlende OID) deuten.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 5.1 | SNMP von Hand | 6 |
| 5.2 | Host und Items | 4 |
| 5.3 | Fehlerbilder und Vorlage | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **SNMP von Hand (Einheit 5.1):** Führen Sie `bash snmp.sh` aus. Erklären Sie Schritt 1: Was liefern die Abfragen, und warum antwortet der Agent bei falscher Gemeinschaft nicht?
2. **Host und Items (Einheit 5.2):** Erklären Sie Schritt 2 und 3: Wie ist die Schnittstelle angelegt, und was berechnet die Vorverarbeitung „Änderung je Sekunde“ bei Zählern?
3. **Fehlerbilder und Vorlage (Einheit 5.3):** Erklären Sie Schritt 4 bis 6: Woran erkennt man die Fehler, was bedeutet Verfügbarkeit 2, und was wurde bei SNMPv3 **nicht** geprüft?

#### Kontrollfragen

1. Warum erst `snmpget`, dann Zabbix?
2. Was meldet Zabbix bei falscher Gemeinschaft?
3. Was bedeutet „No Such Object available on this agent at this OID“?
4. Warum „Änderung je Sekunde“ bei Zählern?

### Modul 6: Auto-Discovery

* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Entdeckungsregeln mit JSON und Makros (`{#QUEUE}`) beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Filter einsetzen und Item- und Trigger-Prototypen nutzen.
  * Nach Abschluss dieses Moduls kann der Lernende das Verschwinden entdeckter Objekte steuern.
  * Nach Abschluss dieses Moduls kann der Lernende fehlerhafte Entdeckungsdaten erkennen.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 6.1 | Entdeckungsskript | 4 |
| 6.2 | Entdeckung läuft | 4 |
| 6.3 | Verschwinden und Fehler | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Entdeckungsskript (Einheit 6.1):** Führen Sie `bash discovery.sh` aus. Erklären Sie Schritt 1 und 2: Welches JSON liefert das Skript, und was bewirkt der Filter?
2. **Entdeckung läuft (Einheit 6.2):** Erklären Sie Schritt 3 und 4: Welche Items und Trigger entstehen, und was geschieht, wenn eine neue Warteschlange auftaucht?
3. **Verschwinden und Fehler (Einheit 6.3):** Erklären Sie Schritt 5 und 6: Wann werden Items gelöscht, und was geschieht bei ungültigem JSON?

#### Kontrollfragen

1. Wie liefert ein Skript Entdeckungsdaten?
2. Was bewirkt der Filter `^archiv$` (passt nicht auf)?
3. Wann verschwindet ein Item?
4. Was geschieht bei ungültigem JSON?

### Modul 7: Benachrichtigungen, Dashboards und Wartungsfenster

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Medientyp, Benutzer-Medium und Aktion konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Problem- und Wiederherstellungsnachrichten prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende Wartungsfenster nutzen und ihre Wirkung erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Dashboard über die API anlegen und Fehlerbilder deuten.
* **Voraussetzungen:** Modul 3; Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 7.1 | Medientyp und Aktion | 4 |
| 7.2 | Nachrichten und Wartung | 4 |
| 7.3 | Fehlerbild und Dashboard | 4 |

#### Praxisaufgaben (Hands-on Lab)

1. **Medientyp und Aktion (Einheit 7.1):** Führen Sie `bash benachrichtigung.sh` aus. Erklären Sie Schritt 1 und 2: Welche Bausteine sind nötig, damit ein Problem eine Nachricht auslöst?
2. **Nachrichten und Wartung (Einheit 7.2):** Erklären Sie Schritt 3 und 4: Welche Nachrichten entstehen, und warum bleibt es im Wartungsfenster ruhig?
3. **Fehlerbild und Dashboard (Einheit 7.3):** Erklären Sie Schritt 5 und 6: Wie zeigt sich ein fehlendes Skript, und was lehnt die API beim Dashboard ab?

#### Kontrollfragen

1. Welche Bausteine braucht eine Benachrichtigung?
2. Was bewirkt ein Wartungsfenster mit Datensammlung?
3. Woran erkennt man ein fehlendes Skript?
4. Wurde ein Dashboard im Browser angesehen?

### Modul 8: Leistung, Betrieb und Sicherung

* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Server über interne Items überwachen.
  * Nach Abschluss dieses Moduls kann der Lernende die erwartete Last (NVPS) berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Housekeeping einstellen und ungültige Angaben erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Konfiguration sichern, wiederherstellen und prüfen.
* **Voraussetzungen:** Modul 3.

#### Tabelle „Lerneinheiten laut Lehrplan“

| Einheit | Inhalt | Stunden |
|---|---|---|
| 8.1 | Selbstüberwachung und NVPS | 4 |
| 8.2 | Housekeeping | 3 |
| 8.3 | Sicherung, Wiederherstellung und Abnahme | 3 |

#### Praxisaufgaben (Hands-on Lab)

1. **Selbstüberwachung und NVPS (Einheit 8.1):** Führen Sie `bash betrieb.sh` aus. Erklären Sie Schritt 1 und 2: Welche internen Items zeigen die Gesundheit des Servers, und wie wird die Last (NVPS) berechnet?
2. **Housekeeping (Einheit 8.2):** Erklären Sie Schritt 3: Was ändert sich bei den Aufbewahrungszeiten, und was meldet die API bei ungültiger Angabe?
3. **Sicherung, Wiederherstellung und Abnahme (Einheit 8.3):** Erklären Sie Schritt 4 bis 7: Was wird gesichert (und was nicht), wie wird die Wiederherstellung belegt, und welcher Prüfpunkt ist absichtlich ein FEHLER?

#### Kontrollfragen

1. Was ist NVPS?
2. Was macht das Housekeeping?
3. Warum enthält die Sicherung keine Messwerte?
4. Wie belegt man eine gelungene Wiederherstellung?
