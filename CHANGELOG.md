# Änderungen

## 2026-11-08 (Bilder-Index)

- Neu: `tools/bilder_index.py`. Es liest alle Markdown-Dateien eines Ordners (Standard: `Umsetzung` neben dem Repository) und schreibt `bilder-index.md` mit allen verlinkten Bildern (Ordner, Datei, Abschnitt, Beschreibung, Größe, Link). Es meldet Bilder ohne Verlinkung, Links auf fehlende Bilder und Bilder über 1 MB. Bilder werden nicht verändert.

## 2026-11-08 (Umsetzungsordner)

- Neu: `tools/umsetzung_anlegen.py`. Es liest einen Lehrplan aus `lehrplaene/` und legt je Modul einen Ordner mit Checkliste (Voraussetzungen, Lerneinheiten, Praxisaufgaben, Lernziele, Kontrollfragen, Prüfpunkte), Protokollvorlage je Praxisaufgabe, Fehlerprotokoll und den Ablageordnern `screenshots/`, `notizen/`, `ausgaben/` an. Dazu eine Übersicht mit Fortschrittstabelle, `befehle-nicht-bestaetigt.md` (Stellen mit „nicht bestätigt“ in den Praxisaufgaben) und `99-abschluss/` mit Checkliste und Sammlung der Lehrplan-Korrekturen. Das Skript überschreibt nichts.
- Die Umsetzungsordner liegen bewusst außerhalb des Repositories (Standard: Ordner neben dem Repository), weil dort Screenshots und Notizen entstehen. Fertiges Material kommt später in ein eigenes Repository je Fach.

## 2026-11-08 (erste Lehrpläne im Repository)

- Neu: Ordner `lehrplaene/` mit den 16 geprüften Lehrplänen (P01–P05, P10, P12, P16, P30, P40–P46), unverändert aus der jeweiligen „Finalen Version“ übernommen, einschließlich Prüfvermerk und offener Punkte. Dateiname wie die Prompt-Datei (`PNN-<slug>.md`).
- Status von P41, P42, P43, P45 und P46 auf „Lehrplan erstellt“ gesetzt; damit stehen 16 von 52 Kursen auf „Lehrplan erstellt“.
- `tools/build_prompts.py`: Neue Spalte „Lehrplan“ in der Tabelle (Link, wenn die Datei in `lehrplaene/` liegt); das Skript bricht ab, wenn ein Kurs auf „Lehrplan erstellt“ steht, aber die Datei fehlt.
- `daten/rahmen.json`: Legende der Statuswerte angepasst. Ausarbeitungen zu Übungen kommen in eigene Repositories („aufbereitet“, „gepusht“).
- Lizenz: Die Lehrpläne stehen wie die Prompts unter CC BY 4.0 (`LICENSE-DOCS.md`, README). Die Frage zur Schutzfähigkeit der KI-erzeugten Tabellen „Lerneinheiten laut Lehrplan“ ist damit nicht rechtlich geklärt, nur die Lizenz des Repositories festgelegt.
- Hinweis: Befehle in den Lehrplänen, die als „nicht bestätigt“ markiert sind, wurden nicht ausgeführt. Das steht in den Prüfvermerken.

## 2026-11-08 (Status in der README erklärt)

- `tools/build_prompts.py` und `daten/rahmen.json`: Vor der Tabelle in der README stehen jetzt ein Zähler (Kurse je Status) und eine Legende zu den vier Statuswerten. Neu in `rahmen.json`: `status_legende`, das Skript bricht ab, wenn ein Statuswert keine Legende hat. Anlass: Aus der Tabelle ging nicht hervor, was „Lehrplan erstellt“ bedeutet und dass die fertigen Lehrpläne nicht im Repository liegen.

## 2026-11-08 (nach der Prüfung von P40 und P44)

- Prüfvermerk der Grundanweisung: Zu jedem der neun Punkte sind die gefundenen und korrigierten Fehler (Modul und Art) zu nennen, oder „keine gefunden“ mit einer konkreten Stichprobe. Ein Punkt ohne beides gilt als nicht geprüft. Anlass: Auch mit Denkaufwand „Hoch“ bewertete die Gem P16, P40 und P44 mit „erfüllt“, obwohl unter anderem Quellen fehlten, Lernziele keine Aufgabe hatten und die Windows-Installation im Labor nirgends geplant war.
- `tools/build_prompts.py`: Das Thema „Troubleshooting und Diagnosewerkzeuge“ wird nur noch bei Kursen mit technischem Labor an die Kernthemen angehängt. Betroffen und neu erzeugt: P40, P41, P43, P47, P48, P49, P51, P52 (Kurse mit „kein technisches Labor nötig“).
- ITIL bleibt bei Version 4 (P40).

## 2026-11-08 (nach den Prüfungen von P02, P03, P04 und P16)

- Selbstprüfung der Grundanweisung von sieben auf neun Punkte erweitert und als nummerierte Liste gesetzt. Der Prüfvermerk verlangt zu jedem Punkt die konkret geprüften Module; Fehler sind vor der Ausgabe zu korrigieren und nicht nur im Prüfvermerk zu nennen.
- Neu: Punkt 2 (jede genutzte Rolle, Software oder jedes Feature hat eine Installationsaufgabe); Punkt 3 (auch Algorithmen, Protokolle und Dateiformate stehen in den Quellen); Punkt 4 (Auswahlen aus frühen Modulen decken spätere Verwendungen ab, Voraussetzungen stehen vor der Aufgabe, die sie braucht); Punkt 5 (Lerneinheiten mit Praxistitel haben eine Aufgabe, Zahlen in Kontrollfragen passen zu den Einheiten); Punkt 6 (Pflichtmodule nennen kein optionales Modul als Voraussetzung); Punkt 8 (Internetphasen, Namen und Adressen im Labor-Setup, Übertragungsweg für Dateien); Punkt 9 (Befehle liefern das Ziel der Aufgabe, zerstörende Befehle stehen nach Zielprüfung und Prüfpunkt). Regel 1 verlangt, erwartete Ausgaben und Fehlercodes nur zu nennen, wenn sie sicher sind.
- Anlass: P02 bis P04 und P16 hatten alle Punkte mit „erfüllt“ bewertet. Gefunden wurden unter anderem ein Pflichtmodul, das von einem optionalen abhing, Software und Inhalte ohne Internet, undefinierte Hostnamen in URLs, ein Webserver, der erst nach seiner Verwendung entstand, eine Auswahl in Modul 3, die spätere Verwendungen nicht abdeckte, ein Zertifikat ohne SAN trotz SAN im CSR, ein falscher Fehlercode, Lerneinheiten ohne Aufgabe und eine Kontrollfrage mit drei statt vier Schutzzielen. P16 wurde mit Denkaufwand „Hoch“ erzeugt; das Fehlermuster blieb ähnlich.

## 2026-11-08 (nach dem Test mit P12)

- Selbstprüfung der Grundanweisung geschärft: Punkt 3 nennt auch Standards, Gesetze und Verordnungen (DSGVO, CVSS, CIS Benchmarks); Punkt 4 verlangt, dass erwartete Ergebnisse zu früheren Modulen passen und Zugangssperren vorher einen Ersatzzugang testen; Punkt 5 unterscheidet Praxisaufgabe (anwenden, konfigurieren) und Kontrollfrage (kennen, verstehen), verlangt Abdeckung jedes genannten Begriffs und verbietet, ein Pflichtlernziel nur in einem optionalen Modul zu prüfen; Punkt 7 nennt Software, die ohne Internet im isolierten Labor installiert werden muss. Anlass: Der Lehrplan P12 (IT-Sicherheit) hatte alle sieben Punkte mit „erfüllt“ bewertet, obwohl mehrere Lernziele ungeprüft waren (VPN, Patch-Management, Risikobewertung), DSGVO und CVSS in den Quellen fehlten, ein Webserver und die Software ohne Internet nie installiert wurden, SSH-Passwort-Login vor dem Schlüsseltest abgeschaltet wurde und der Nmap-Nachweis den Firewall-Regeln widersprach.

## 2026-11-08 (nach dem Test mit P05)

- Selbstprüfung der Grundanweisung: Punkt 6 um die Regel ergänzt, dass der Rückbau von Änderungen nie von einem optionalen Modul abhängt; neuer Punkt 7 (Voraussetzungen wie Domäne, Zertifikate, gemeinsamer Speicher oder zusätzliche Hosts müssen im Labor-Setup aufgebaut oder ausgeschlossen sein). Anlass: Der Hyper-V-Lehrplan (P05) nannte eine Domäne `lab.internal`, baute sie aber nie auf, verlangte aber eine Live-Migration, die ohne Domäne nicht möglich ist, und legte den Rückbau der Nested-Umgebung in ein optionales Modul. Der Prüfvermerk hatte dennoch alle Punkte mit „erfüllt“ bewertet.

## 2026-11-08 (nach dem Test mit P01)

- Selbstprüfung der Grundanweisung um Punkt 6 erweitert (einschränkende Einstellungen in späteren Modulen, angekündigte Szenarien vollständig, Lernziele im Labor machbar) und die Bewertung „teilweise erfüllt“ eingeführt. Anlass: Der zweite Test (P01) hatte alle Punkte mit „erfüllt“ bewertet, obwohl Modul 9 an früheren Lauschadressen und ACLs scheiterte und ein TSIG-Lernziel im Lab nicht machbar war.

## 2026-11-08 (Umbau auf Variablen-Form)

- Gem-Grundanweisung überarbeitet und als `gem/grundanweisung.md` ins Repository aufgenommen. Neu: Dokumentstruktur mit festen Überschriftsebenen, Zeile „Gesamt“ in der Master-Tabelle, Quellenregeln (Format, Verifikation, jede Norm und jeder RFC in der Liste), Labor-Setup mit „erforderlich“ und „optional“, Ausnahme für Cloud-Kurse (Test-Tenant) und für Kurse ohne technisches Labor, Hinweis, dass Scans nur gegen eigene Lab-VMs laufen, UE = 45 Minuten, Dateiname `lehrplan_<kursname>.md`, Selbstprüfung mit Prüfvermerk im Chat.
- Neue Vorlage `gem/vorlage-variablen.md`.
- Alle 52 Prompts auf die Variablen-Form umgebaut (Fokus-Technologien, Vorkenntnisse, Umfang, Kernthemen, Abgrenzung, Labor-Ressourcen, Zusätzliche Hinweise). Neue Felder `fokus` und `labor` in `daten/kurse.json`, das Feld `praxis` entfällt, `zielgruppe` steht nur noch in der Grundanweisung.

## 2026-11-08 (später am Tag)

- Repository öffentlich gestellt und im Profil verlinkt. `LICENSE` (MIT, Skript) und `LICENSE-DOCS.md` (CC BY 4.0, Texte) ergänzt, README um Abschnitte „Entstehung“ und „Lizenz“ erweitert.

## 2026-11-08

- Erste Fassung: 52 Prompts in 16 Themengebieten (Priorität A, B, C), erzeugt aus `daten/kurse.json`.
- Gemeinsamer Rahmen: Zielgruppe Auszubildende, Quereinsteiger und angehende Systemadministratoren/Systemtechniker (Österreich/EU); große Kurse etwa 12 Module und 100 bis 120 Stunden, kleine Kurse (Recht, IT-Betrieb, Zusatz, PC-Hardware) etwa 8 Module und 40 bis 60 Stunden.
- Gemeinsame Regeln in allen Prompts: keine erfundenen Fakten, Versionen oder Befehle; Unsicheres als „nicht bestätigt“; keine geschützten Texte oder Prüfungsfragen; eigene Szenarien mit `example.com`; Übungen nur in isolierten Umgebungen; Ausgabeformat gemäß Grundanweisung der Gem.
