# Änderungen

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
