# E05 – Backup auf NAS mit Veeam

- Thema: Homelab und Betrieb
- Repository: [storage-backup-uebungen/veeam-nas](https://github.com/AnsibleArtisan4711/storage-backup-uebungen/tree/main/veeam-nas)
- Umfang: 2 Module, davon 2 mit Material; 2 Einheiten

## Modul 1: Backup und Restore

### 01.1 Backup auf NAS mit Veeam

- Stufe: Aufbau; geschätzte Zeit: 8 bis 10 Stunden (Schätzung), auf mehrere Tage verteilbar
- Teile: 0 Testumgebung aufbauen (6 Schritte); 1 Backup einrichten (8 Schritte); 2 Wiederherstellung (2 Schritte); 3 Betrieb (4 Schritte)
- Lernziele: 6, Kontrollfragen: 8
- Skripte: `01.1-nas-einrichten.sh`, `01.1-testdaten-fileserver.ps1`, `01.1-testdaten-ad.ps1`, `01.1-backup-bericht.ps1`, `01.1-offsite-kopie.sh`

## Modul 2: Monitoring mit PRTG

### 02.1 Monitoring der Backup-Umgebung mit PRTG

- Stufe: Aufbau; geschätzte Zeit: 4 bis 5 Stunden (Schätzung)
- Teile: 1 Server und Struktur (4 Schritte); 2 Geräte anbinden (4 Schritte); 3 Eigener Sensor, Ausfälle, Betrieb (4 Schritte)
- Lernziele: 6, Kontrollfragen: 6
- Skripte: `02.1-monitoring-benutzer.ps1`, `02.1-snmp-auf-nas.sh`, `02.1-prtg-backup-alter.sh`, `02.1-prtg-backup-alter.ps1`, `02.1-ausfall-test.ps1`

Aufbau gelesen aus den Dateien des Repositories (`python tools/uebungen_einlesen.py`).
Umsetzungsordner anlegen: `python tools/umsetzung_anlegen.py E05`
