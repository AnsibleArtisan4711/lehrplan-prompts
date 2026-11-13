# Lehrplan: Lizenzmanagement

| Attribut | Beschreibung |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren / Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen; Grundkenntnisse im IT-Betrieb; Umgang mit einer Tabellenkalkulation |
| **Gesamtumfang** | 8 Module, 40 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Lizenzmodelle (Microsoft, Open Source, Cloud), Lizenzverwaltung in der Tabellenkalkulation; Python 3 für Rechenhilfen (optional) |
| **Thematische Abgrenzung (Out of Scope)** | Asset-Verwaltung und CMDB sind ein eigener Kurs (nur Verweise); **keine Rechtsberatung**: rechtliche Aussagen sind Kursannahmen und von Fachleuten (Rechtsabteilung, Hersteller, Lizenzberater) zu prüfen; keine Preislisten; kein technisches Labor; keine Zertifizierungsvorbereitung. |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundbegriffe und Lizenzarten | 1 | 5 |
| 2 | Microsoft-Lizenzierung im Überblick | 1 | 6 |
| 3 | Open-Source-Lizenzen und Pflichten | 1 | 5 |
| 4 | Cloud- und Subscription-Lizenzen | 1 | 5 |
| 5 | Lizenzinventur und Compliance | 1 | 6 |
| 6 | Audits und Nachweise | 2 | 4 |
| 7 | Optimierung und Beschaffung | 2 | 5 |
| 8 | Dokumentation und Prozess | 1 | 4 |
| **Gesamt** | **6 Pflichtmodule, 2 Vertiefungsmodule** | | **40** |

*Hinweis zur Priorisierung: Die Module 6 und 7 (Priorität 2) dienen der Vertiefung und können bei Zeitmangel gekürzt werden. Kein Pflichtmodul setzt ein Prio-2-Modul voraus.*

### 2. Quellen

* **Microsoft-Blog zum Lizenzmodell von Windows Server 2016** (archiviert, Microsoft Learn, 2016, abgerufen am 13.11.2026): Mindestens 8 Kernlizenzen je Prozessor und 16 je Server, Verkauf in 2er-Paketen, Zugriffslizenzen (CAL) je Benutzer oder Gerät. **Gilt für Windows Server 2016; der Stand für die aktuelle Version ist nicht geprüft** und vor dem Kurs in den aktuellen Microsoft-Lizenzbedingungen nachzulesen.
* **Microsoft 365, Cloud-Lizenzen, Preise:** *nicht geprüft*. Pläne, Bezeichnungen und Preise ändern sich; im Kurs keine Preise ohne Stand.
* **Open-Source-Lizenztexte** (GPL, LGPL, AGPL, MIT, BSD, Apache 2.0) liegen in den jeweiligen Projekten und bei den Lizenzgebern vor (z. B. gnu.org, opensource.org, apache.org). *Wortlaut nicht geprüft*; im Kurs nur Kernpflichten auf Begriffsebene, keine Rechtsauslegung.
* **ISO/IEC 19770** (Software Asset Management): nur als Hinweis genannt, Inhalt und Stand nicht geprüft.
* **DSGVO** (Verordnung (EU) 2016/679) nur als Rahmen bei Nutzerzahlen und Zuordnung; keine Rechtsberatung.

### 3. Labor-Setup & Rahmenbedingungen

* **Kein technisches Labor.** Gearbeitet wird mit einer Tabellenkalkulation (LibreOffice Calc oder Excel) und optional mit kleinen Python-Skripten.
* **Fiktives Unternehmen:** Bergfeld Maschinenbau GmbH, 60 Mitarbeitende an zwei Standorten, 4 physische Server, 12 virtuelle Maschinen, Microsoft 365, einige Open-Source-Komponenten. Alle Zahlen sind frei erfunden.
* **Material des Dozenten:** (1) Inventarliste mit Servern, VMs und Software (CSV), (2) Liste der erworbenen Lizenzen mit Nachweisen, (3) Beschreibung einer Audit-Anfrage. Die Beispiele liegen der Übungsreihe bei.

## B. Detaillierter Modulaufbau

### Modul 1: Grundbegriffe und Lizenzarten
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Lizenz, Nutzungsrecht, Metrik und Nachweis definieren.
  * Nach Abschluss dieses Moduls kann der Lernende Lizenzmodelle (Gerät, Benutzer, Subscription, Kern) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Lizenzmanagement von Asset-Verwaltung abgrenzen.
* **Voraussetzungen:** keine.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Lizenz, Nutzungsrecht, Metrik, Nachweis | 2 |
| 1.2 | Lizenzmodelle: Gerät, Benutzer, Subscription, Kern | 2 |
| 1.3 | Abgrenzung zur Asset-Verwaltung | 1 |

#### Praxisaufgaben
1. **Begriffe:** Ordne sechs Beispielprodukte (fiktiv) einer Metrik zu und begründe.
2. **Modelle:** Vergleiche in einer Tabelle Gerät-, Benutzer- und Subscription-Lizenz (Vorteil, Risiko, Beispiel).
3. **Abgrenzung:** Nenne je einen Fall für Asset-Verwaltung und Lizenzmanagement und zeige die gemeinsame Schnittmenge.

#### Kontrollfragen
1. Was ist der Unterschied zwischen Lizenz und Nutzungsrecht?
2. Warum ist die Metrik entscheidend für die Zählung?
3. Wann ist eine Benutzerlizenz günstiger als eine Gerätelizenz?

### Modul 2: Microsoft-Lizenzierung im Überblick
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Kernmodell für Windows Server nach der Beispielregel berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende Zugriffslizenzen (CAL) einordnen.
  * Nach Abschluss dieses Moduls kann der Lernende Aussagen zur Lizenzierung als „gilt laut Quelle mit Stand“ oder „nicht bestätigt“ kennzeichnen.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Server-Lizenzierung nach Kernen (Beispielregel) | 2 |
| 2.2 | Zugriffslizenzen (CAL) und Remote Desktop | 2 |
| 2.3 | Virtualisierung und Edition (Standard, Datacenter) im Überblick | 2 |

#### Praxisaufgaben
1. **Kerne:** Berechne mit `kernlizenzen.py` die benötigten Kernlizenzen für drei Server (Beispielregel: mindestens 8 je Prozessor, mindestens 16 je Server, 2er-Pakete). Kennzeichne die Regel als „Stand 2016, nicht bestätigt für die aktuelle Version“.
2. **CAL:** Ermittle für das Beispielunternehmen die Zahl der Benutzer- und Gerät-CALs und begründe die Wahl.
3. **Virtualisierung:** Beschreibe, wie sich die Lizenzierung bei zusätzlichen VMs ändert (Beispiel Standard: alle Kerne erneut lizenzieren, Stand 2016), und nenne offene Fragen für die aktuelle Version.

#### Kontrollfragen
1. Warum werden Kerne und nicht Sockel gezählt?
2. Wann braucht ein Benutzer eine zusätzliche RDS-CAL?
3. Warum darf man die Regel von 2016 nicht ungeprüft übernehmen?

### Modul 3: Open-Source-Lizenzen und Pflichten
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende permissive und Copyleft-Lizenzen unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Pflichten (Lizenztext, Quellcode, Hinweis) je Lizenzart benennen.
  * Nach Abschluss dieses Moduls kann der Lernende eine Komponentenliste nach Lizenz klassifizieren und Risiken markieren.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Permissive und Copyleft-Lizenzen (MIT, BSD, Apache, GPL, LGPL, AGPL) | 2 |
| 3.2 | Pflichten bei Nutzung, Weitergabe und Netzwerkdiensten | 2 |
| 3.3 | Komponentenliste und Risikobewertung | 1 |

#### Praxisaufgaben
1. **Vergleich:** Erstelle eine Tabelle mit Kernmerkmalen der genannten Lizenzen (Quellen: Lizenztexte der Projekte; im Zweifel „nicht bestätigt“).
2. **Klassifizieren:** Ordne zehn Beispielkomponenten mit `os_lizenzen.py` nach Lizenzfamilie und markiere solche mit Prüfbedarf.
3. **Szenario:** Beurteile intern genutzte Software gegenüber weitergegebener Software und notiere, was rechtlich zu klären ist.

#### Kontrollfragen
1. Was bedeutet Copyleft?
2. Was ändert sich bei Software, die nur intern genutzt wird?
3. Warum ist „Open Source“ nicht gleich „ohne Pflichten“?

### Modul 4: Cloud- und Subscription-Lizenzen
* **Priorität:** 1 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Subscription-Lizenzen und Kostenmodelle (je Benutzer, je Verbrauch) unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Kosten über Laufzeit und Nutzerzahl hochrechnen.
  * Nach Abschluss dieses Moduls kann der Lernende nicht genutzte Lizenzen erkennen.
* **Voraussetzungen:** Modul 1.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Subscription, Verbrauchsmodelle, Laufzeiten | 2 |
| 4.2 | Kostenhochrechnung (Beispielpreise, ohne Stand nicht verwendbar) | 2 |
| 4.3 | Zuweisung, Entzug und ungenutzte Lizenzen | 1 |

#### Praxisaufgaben
1. **Hochrechnung:** Berechne mit `kosten.py` die Jahreskosten für 60 Benutzer bei drei fiktiven Plänen (Preise sind **erfundene Beispielwerte**, keine echten Preise).
2. **Ungenutzte Lizenzen:** Finde in der Beispielliste Konten ohne Anmeldung seit 90 Tagen und leite Einsparungen ab.
3. **Prozess:** Beschreibe Zuweisung und Entzug beim Eintritt, Wechsel und Austritt.

#### Kontrollfragen
1. Warum steigen Subscription-Kosten schleichend?
2. Was ist beim Entzug einer Lizenz bei Austritt zu beachten?
3. Warum dürfen Preise nur mit Stand genannt werden?

### Modul 5: Lizenzinventur und Compliance
* **Priorität:** 1 · **Zeitaufwand:** 6 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende installierte Software und erworbene Lizenzen gegenüberstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Über- und Unterlizenzierung berechnen.
  * Nach Abschluss dieses Moduls kann der Lernende einen Lizenzstatus je Produkt ableiten.
* **Voraussetzungen:** Modul 2 bis 4.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Bestandsaufnahme: Installationen und Nutzer | 2 |
| 5.2 | Gegenüberstellung Bedarf und Bestand (Effective License Position) | 2 |
| 5.3 | Abweichungen bewerten und Maßnahmen ableiten | 2 |

#### Praxisaufgaben
1. **Bedarf:** Ermittle den Lizenzbedarf je Produkt aus der Inventarliste.
2. **Gegenüberstellung:** Vergleiche Bedarf und Bestand mit `lizenzbilanz.py` und weise Über- und Unterdeckung aus.
3. **Maßnahmen:** Lege je Abweichung eine Maßnahme fest (nachkaufen, deinstallieren, umverteilen, klären).

#### Kontrollfragen
1. Was bedeutet Unterlizenzierung, und welches Risiko entsteht?
2. Warum reicht eine Installationsliste allein nicht aus?
3. Wer entscheidet über Nachkauf oder Deinstallation?

### Modul 6: Audits und Nachweise
* **Priorität:** 2 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Ablauf eines Hersteller-Audits beschreiben.
  * Nach Abschluss dieses Moduls kann der Lernende Nachweise (Rechnung, Vertrag, Zertifikat) ordnen.
* **Voraussetzungen:** Modul 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Ablauf, Rechte und Pflichten bei Audits (Rahmen, ohne Rechtsberatung) | 2 |
| 6.2 | Nachweisarchiv aufbauen | 2 |

#### Praxisaufgaben
1. **Audit-Anfrage:** Lies die fiktive Anfrage, lege Ansprechpartner, Fristen und Schritte fest und markiere, was Rechtsabteilung oder Berater klären müssen.
2. **Nachweise:** Ordne zehn fiktive Belege einem Produkt zu und finde fehlende Nachweise.

#### Kontrollfragen
1. Warum sollte die Antwort auf eine Audit-Anfrage abgestimmt werden?
2. Welche Nachweise gelten für Abonnements?

### Modul 7: Optimierung und Beschaffung
* **Priorität:** 2 · **Zeitaufwand:** 5 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Optimierungsmöglichkeiten (Edition, Umverteilung, Laufzeit) bewerten.
  * Nach Abschluss dieses Moduls kann der Lernende einen Beschaffungsprozess mit Freigabe skizzieren.
* **Voraussetzungen:** Modul 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Optimierung: Edition, Umverteilung, Laufzeit | 3 |
| 7.2 | Beschaffungsprozess und Freigaben | 2 |

#### Praxisaufgaben
1. **Optimierung:** Bewerte drei Szenarien (Edition wechseln, Lizenzen umverteilen, Laufzeit verlängern) mit Beispielzahlen aus `kosten.py`.
2. **Beschaffung:** Zeichne den Ablauf von Bedarf bis Eingang des Nachweises mit Rollen.

#### Kontrollfragen
1. Wann lohnt sich eine längere Laufzeit nicht?
2. Warum gehört der Nachweis zum Beschaffungsprozess?

### Modul 8: Dokumentation und Prozess
* **Priorität:** 1 · **Zeitaufwand:** 4 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende ein Lizenzregister mit Pflichtfeldern aufbauen.
  * Nach Abschluss dieses Moduls kann der Lernende Rollen, Prüfrhythmus und Berichte festlegen.
* **Voraussetzungen:** Modul 5.

| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Lizenzregister: Felder und Pflege | 2 |
| 8.2 | Rollen, Rhythmus, Berichte | 2 |

#### Praxisaufgaben
1. **Register:** Baue ein Lizenzregister in der Tabellenkalkulation (Produkt, Metrik, Menge, Nachweis, Laufzeit, Verantwortlicher) und trage die Beispieldaten ein.
2. **Prozess:** Lege eine RACI-Tabelle und einen Prüfrhythmus fest (Annahme, begründen).

#### Kontrollfragen
1. Welche Felder braucht ein Lizenzregister mindestens?
2. Wie oft sollte das Register geprüft werden, und warum?

---

## C. Entstehung und Prüfvermerk (13.11.2026)

Dieser Lehrplan wurde direkt aus dem Prompt P70 erstellt (Annahmen: kein Labor, Tabellenkalkulation, fiktives Unternehmen). Stunden: 5+6+5+5+6+4+5+4 = 40 UE; jede Einheitentabelle summiert auf die Modulstunden; Prioritäten 6×1, 2×2.

**Nicht bestätigt:** Lizenzregeln für die aktuelle Windows-Server-Version, Microsoft-365-Pläne, alle Preise, Wortlaut und Auslegung der Open-Source-Lizenzen, Ablauf und Rechte bei Hersteller-Audits. Die Beispielregel zu Kernen stammt aus einer archivierten Quelle zu Windows Server 2016. Der Kurs gibt **keine Rechtsberatung**.

**Offen:** Der Zeitaufwand ist unerprobt. Der Lehrplan wurde von AnsibleArtisan4711 noch nicht geprüft.
