# Änderungen

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
