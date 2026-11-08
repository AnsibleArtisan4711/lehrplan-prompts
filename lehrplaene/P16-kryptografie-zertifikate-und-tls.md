# Lehrplan: Kryptografie, Zertifikate und TLS

| Eigenschaft | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen und Grundkenntnisse in Netzwerken (IP-Adressen nach RFC 1918, Subnetze), sicherer Umgang mit der Linux-CLI (Navigieren, `sudo`, Texteditor wie `nano`), grundlegende Bedienung von Windows 11 (Explorer, Datenträgerverwaltung, PowerShell) |
| **Gesamtumfang** | 12 Module, 110 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | OpenSSL, TLS, Debian/Ubuntu Linux, Windows 11 |
| **Thematische Abgrenzung (Out of Scope)** | Die AD-CS-Praxis steht im Kurs „Zertifikatsdienste und PKI“; keine Kryptoanalyse und keine mathematischen Beweise (Überblick genügt); BitLocker nur für Datenlaufwerke, nicht für das Systemlaufwerk mit TPM |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen der Kryptografie | 1 | 8 |
| 2 | Symmetrische Verschlüsselung | 1 | 10 |
| 3 | Asymmetrische Verschlüsselung | 1 | 10 |
| 4 | Hashes und Message Authentication Codes | 1 | 8 |
| 5 | Digitale Signaturen | 1 | 8 |
| 6 | Zertifikate und Vertrauenskette (PKI) | 1 | 10 |
| 7 | OpenSSL in der Praxis (lokale CA) | 1 | 12 |
| 8 | Der TLS-Handshake | 1 | 10 |
| 9 | Zertifikatsprüfung und Fehlersuche in TLS | 1 | 10 |
| 10 | Verschlüsselung ruhender Daten: LUKS | 2 | 8 |
| 11 | Verschlüsselung ruhender Daten: BitLocker | 2 | 8 |
| 12 | Passwörter und Hashing | 1 | 8 |
| **Gesamt** | **12 Module (10x Prio 1, 2x Prio 2)** | | **110** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (Pflicht) bilden die essenzielle Kernkompetenz. Module mit Priorität 2 (Vertiefung) sind optionale Themen zur inhaltlichen Abrundung.*

### 2. Quellen

* RFC 1918 (Address Allocation for Private Internets), IETF, 1996, URL: https://datatracker.ietf.org/doc/html/rfc1918
* RFC 5280 (Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List Profile), IETF, 2008, URL: https://datatracker.ietf.org/doc/html/rfc5280
* RFC 5246 (The Transport Layer Security (TLS) Protocol Version 1.2), IETF, 2008, URL: https://datatracker.ietf.org/doc/html/rfc5246
* RFC 8446 (The Transport Layer Security (TLS) Protocol Version 1.3), IETF, 2018, URL: https://datatracker.ietf.org/doc/html/rfc8446
* RFC 7468 (Textual Encodings of PKIX, PKCS, and CMS Structures - PEM), IETF, 2015, URL: https://datatracker.ietf.org/doc/html/rfc7468
* BSI TR-02102-1 (Kryptographische Verfahren: Empfehlungen und Schlüssellängen), BSI, Stand nicht geprüft, URL: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf
* OpenSSL Documentation, OpenSSL Software Foundation, URL: https://www.openssl.org/docs/
* RFC 2104 (HMAC: Keyed-Hashing for Message Authentication), IETF, 1997, URL: https://datatracker.ietf.org/doc/html/rfc2104
* RFC 6960 (X.509 Internet PKI Online Certificate Status Protocol - OCSP), IETF, 2013, URL: https://datatracker.ietf.org/doc/html/rfc6960
* RFC 8017 (PKCS #1: RSA Cryptography Specifications Version 2.2), IETF, 2016, URL: https://datatracker.ietf.org/doc/html/rfc8017
* RFC 8018 (PKCS #5: Password-Based Cryptography Specification Version 2.1; PBKDF2), IETF, 2017, URL: https://datatracker.ietf.org/doc/html/rfc8018
* RFC 8439 (ChaCha20 and Poly1305 for IETF Protocols), IETF, 2018, URL: https://datatracker.ietf.org/doc/html/rfc8439
* RFC 9106 (Argon2 Memory-Hard Function for Password Hashing), IETF, 2021, URL: https://datatracker.ietf.org/doc/html/rfc9106
* FIPS 197 (Advanced Encryption Standard), NIST, URL: https://csrc.nist.gov/pubs/fips/197/final (Aufruf nicht geprüft)
* FIPS 180-4 (Secure Hash Standard, SHA-2) und FIPS 202 (SHA-3), NIST, URLs: https://csrc.nist.gov/pubs/fips/180-4/upd1/final und https://csrc.nist.gov/pubs/fips/202/final (Aufruf nicht geprüft)
* NIST SP 800-38A (Betriebsmodi von Blockchiffren) und SP 800-38D (GCM), NIST, URLs: https://csrc.nist.gov/pubs/sp/800/38/a/final und https://csrc.nist.gov/pubs/sp/800/38/d/final (Aufruf nicht geprüft)
* cryptsetup und LUKS2 On-Disk Format Specification, Projekt cryptsetup, URL: https://gitlab.com/cryptsetup/cryptsetup (Aufruf nicht geprüft)
* BitLocker overview und manage-bde (Befehlsreferenz), Microsoft Corporation, abgerufen am 08.11.2026, URLs: https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/ und https://learn.microsoft.com/windows-server/administration/windows-commands/manage-bde

### 3. Labor-Setup & Rahmenbedingungen

* **Virtuelles Netzwerk:** Ein privater Hyper-V-Switch (z. B. `Lab-Internal-Net`) ohne Verbindung zum Heimnetz oder physischen Router. Subnetz: `192.168.10.0/24` (gemäß RFC 1918). Alle Adressen sind statisch, es gibt weder DHCP noch DNS. (Erforderlich ab Modul 2)
* **VM1 (Server `linux01`):** 1x Linux-Server-VM (Debian 12 oder Ubuntu Server 22.04 LTS bzw. neuer, damit OpenSSL 3.x vorhanden ist; die Befehle wurden mit OpenSSL 3.0.13 getestet), statische IP `192.168.10.10`. Erforderliche Pakete: `openssl`, `ca-certificates`, `cryptsetup`, `tshark`, `openssh-server`. Wireshark mit grafischer Oberfläche wird nicht benötigt, die Mitschnitte werden mit `tshark` ausgewertet. (Erforderlich ab Modul 2). Eine zusätzliche leere virtuelle Festplatte (VHDX, ca. 5 GB) am Linux-System (Erforderlich ab Modul 10).
* **VM2 (Client `win11-01`):** 1x Windows-11-VM der Edition Pro, Enterprise oder Education (Workgroup, keine Domäne; die BitLocker-Verwaltung ist laut Microsoft für diese Editionen dokumentiert), statische IP `192.168.10.20`. `curl.exe` und der OpenSSH-Client (`scp`) sind unter Windows 11 enthalten; fehlt `scp`, wird das optionale Feature „OpenSSH-Client“ nachinstalliert. (Erforderlich ab Modul 8). Eine zusätzliche leere virtuelle Festplatte (VHDX, ca. 5 GB) ohne TPM-Zwang (Erforderlich ab Modul 11).
* **Vorbereitung vor Kursbeginn (einmalig, mit Internet):** Der private Switch hat keinen Internetzugang. Die Pakete aus der Liste oben werden deshalb vor Kursbeginn installiert, indem die Linux-VM vorübergehend an einen Switch mit Internetzugang (z. B. den Hyper-V-„Default Switch“) angeschlossen wird; danach wird sie auf `Lab-Internal-Net` umgestellt. Im Kurs selbst gibt es keine Aktion, die Internet braucht.
* **Arbeitsverzeichnis und Dateien:** Auf `linux01` arbeitet jedes Modul im Ordner `~/krypto/mNN/` (z. B. `~/krypto/m07/`). Spätere Module greifen auf diese Ordner zu (Modul 5 auf die Schlüssel aus Modul 3, Modul 8 und 9 auf CA und Server-Zertifikat aus Modul 7). Der Ordner `~/krypto/` wird nicht gelöscht.
* **Dateiübertragung:** Das Root-Zertifikat `ca.crt` wird von der Windows-VM per `scp` von `linux01` geholt (Modul 9). Der Linux-Benutzer braucht ein Kennwort für SSH. Der Schlüssel `ca.key` wird nie übertragen.
* **Zeit und Namen:** Die Hyper-V-Zeitsynchronisierung bleibt aktiviert, weil Zertifikate zeitabhängig sind. Der Dienstname `server.example.internal` ist fiktiv und nur über einen Eintrag in der `hosts`-Datei der Windows-VM auflösbar (Modul 9).
* **Hyper-V-Prüfpunkte:** Je ein Prüfpunkt von `linux01` vor Modul 10 und von `win11-01` vor Modul 11.

*Hinweis: Da Modul 1 theoretisch ist, wird dafür kein technisches Labor benötigt.*

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen der Kryptografie
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Grundprinzipien der Informationssicherheit (Schutzziele) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen symmetrischen und asymmetrischen Verfahren in der Theorie zusammenfassen.
  * Nach Abschluss dieses Moduls kann der Lernende historische Verschlüsselungsmethoden und das Kerckhoffs'sche Prinzip beschreiben.
* **Voraussetzungen:** IT-Grundkenntnisse

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Schutzziele (Vertraulichkeit, Integrität, Authentizität, Verbindlichkeit) | 2 |
| 1.2 | Historische Kryptografie (Caesar, Vigenère) und das Kerckhoffs'sche Prinzip | 2 |
| 1.3 | Einordnung der kryptografischen Verfahren (Symmetrisch vs. Asymmetrisch vs. Hashing) | 2 |
| 1.4 | Standards und Vorgaben (BSI TR-02102-1) | 2 |

#### Praxisaufgaben (Hands-on Lab)
*Da kein technisches Labor benötigt wird, basieren die Aufgaben auf Fallstudien.*
1. **Fallstudie zur Algorithmensicherheit:** Recherchieren Sie in der BSI TR-02102-1 (Offline-PDF-Bereitstellung durch den Kursleiter; Ausgabe und Stand notieren) nach zulässigen Algorithmen und Schlüssellängen. Dokumentieren Sie drei zulässige Kombinationen aus Schlüssellänge und Verfahren (z. B. AES, RSA, ECC) mit Angabe der Fundstelle.

#### Kontrollfragen
1. Was besagt das Kerckhoffs'sche Prinzip und warum ist "Security by Obscurity" gefährlich?
2. Warum können Hashes nicht in die Gruppe der Ver- oder Entschlüsselungsverfahren eingeordnet werden?
3. Nennen Sie die in Einheit 1.1 behandelten Schutzziele und ordnen Sie jedem ein kryptografisches Verfahren zu, das es unterstützt (z. B. Vertraulichkeit durch Verschlüsselung). Welches klassische Schutzziel wird durch Kryptografie allein nicht gewährleistet?
4. Entschlüsseln Sie den Text „KHOOR“ (Caesar-Chiffre, Verschiebung um 3 Stellen) und erklären Sie, warum die Vigenère-Chiffre gegen eine einfache Häufigkeitsanalyse robuster ist.
5. Fassen Sie in drei Sätzen den Unterschied zwischen symmetrischen und asymmetrischen Verfahren zusammen (Schlüssel, Schlüsselverteilung, typische Verwendung).

### Modul 2: Symmetrische Verschlüsselung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktionsweise von Block- und Stromchiffren unterscheiden.
  * Nach Abschluss dieses Moduls kann der Lernende Dateien mittels OpenSSL über die Kommandozeile symmetrisch verschlüsseln und entschlüsseln.
  * Nach Abschluss dieses Moduls kann der Lernende die Bedeutung von Betriebsmodi (z. B. CBC, GCM) und Initialisierungsvektoren (IV) erklären.
* **Voraussetzungen:** Modul 1, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Funktionsweise symmetrischer Algorithmen (AES, ChaCha20) | 2 |
| 2.2 | Stromchiffren vs. Blockchiffren | 2 |
| 2.3 | Betriebsmodi (ECB, CBC, GCM) und Initialisierungsvektor (IV) | 3 |
| 2.4 | Praxis mit dem OpenSSL Kommandozeilenwerkzeug (enc) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Datei ver- und entschlüsseln:** Legen Sie `~/krypto/m02/` an und erstellen Sie dort die Textdatei `geheim.txt`. Verschlüsseln Sie sie mit `openssl enc -aes-256-cbc -salt -pbkdf2 -in geheim.txt -out geheim.enc` (das Passwort wird abgefragt). Löschen Sie `geheim.txt` und stellen Sie die Datei mit `openssl enc -d -aes-256-cbc -pbkdf2 -in geheim.enc -out geheim.txt` wieder her. Lassen Sie `-pbkdf2` einmal weg und dokumentieren Sie die Warnung („deprecated key derivation used“), die bei OpenSSL 3.0 erscheint.
2. **Modus-Vergleich (ECB vs. CBC):** Erzeugen Sie mit `yes "ABCDEFGHIJKLMNO" | head -n 100 > muster.txt` eine Datei, deren 16-Byte-Blöcke alle gleich sind (15 Zeichen plus Zeilenumbruch). Verschlüsseln Sie sie einmal mit `-aes-256-ecb` und einmal mit `-aes-256-cbc` (jeweils mit `-pbkdf2`). Vergleichen Sie die Dateigrößen (`ls -l`) und zählen Sie gleiche Blöcke mit `tail -c +17 <datei> | od -An -tx1 -w16 -v | sort | uniq -c | sort -rn | head -3` (`tail -c +17` überspringt den 16 Byte langen Kopf `Salted__` plus Salt). Dokumentieren Sie, was die Blockwiederholung bei ECB über die Daten verrät und warum CBC das nicht tut (IV).
3. **Grenze von `openssl enc`:** Versuchen Sie, dieselbe Datei mit `-aes-256-gcm` zu verschlüsseln. Dokumentieren Sie die Fehlermeldung („AEAD ciphers not supported“) und erklären Sie, was das für den Einsatz von GCM bedeutet (GCM ist ein authentifizierter Modus, ein sogenannter AEAD-Modus, und wird von `openssl enc` nicht unterstützt).

#### Kontrollfragen
1. Welches Problem ergibt sich bei der rein symmetrischen Verschlüsselung, wenn zwei Parteien erstmals über das Internet sicher kommunizieren wollen?
2. Warum wird vom Betriebsmodus Electronic Codebook (ECB) dringend abgeraten?
3. Was ist die Aufgabe eines Initialisierungsvektors (IV) im CBC-Modus?
4. Worin unterscheiden sich Block- und Stromchiffren, und zu welcher Gruppe gehören AES und ChaCha20?

### Modul 3: Asymmetrische Verschlüsselung
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Konzept asymmetrischer Schlüsselpaare (Public/Private Key) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende RSA- und ECC-Schlüsselpaare über OpenSSL generieren.
  * Nach Abschluss dieses Moduls kann der Lernende den Einsatz asymmetrischer Kryptografie für den Schlüsselaustausch verstehen.
* **Voraussetzungen:** Modul 2, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Konzept des Public/Private Key-Verfahrens | 2 |
| 3.2 | Mathematische Grundlagen im Überblick (RSA, Elliptische Kurven / ECC) | 3 |
| 3.3 | Schlüsselaustausch-Verfahren (Diffie-Hellman) | 2 |
| 3.4 | Schlüsselgenerierung und Verwaltung mit OpenSSL (genpkey) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **RSA-Schlüsselpaar generieren:** Legen Sie `~/krypto/m03/` an. Erzeugen Sie mit `openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out private.pem` einen 3072-Bit-RSA-Privatschlüssel und leiten Sie den öffentlichen Schlüssel mit `openssl pkey -in private.pem -pubout -out public.pem` ab. Betrachten Sie beide Dateien mit `openssl pkey -in <datei> -text -noout` (bei `public.pem` zusätzlich `-pubin`) und notieren Sie, welche Teile geheim sind.
2. **ECC-Schlüsselpaar generieren:** Zeigen Sie die unterstützten Kurven mit `openssl ecparam -list_curves` an. Erzeugen Sie mit `openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:secp384r1 -out ecc-private.pem` einen Schlüssel und leiten Sie `ecc-public.pem` ab. Vergleichen Sie die Dateigrößen der öffentlichen Schlüssel von RSA und ECC.
3. **Schlüssel sichern:** Erzeugen Sie aus dem RSA-Privatschlüssel mit `openssl pkey -in private.pem -aes256 -out private_enc.pem` eine passwortgeschützte Kopie. Prüfen Sie, dass die erste Zeile `BEGIN ENCRYPTED PRIVATE KEY` lautet. `private.pem` bleibt für Modul 5 unverändert erhalten (nur im Labor; in der Praxis wird die ungeschützte Kopie gelöscht).

#### Kontrollfragen
1. Welcher der beiden Schlüssel (Public oder Private) wird verwendet, um Daten so zu verschlüsseln, dass nur der Empfänger sie lesen kann?
2. Warum ist die Kombination (hybride Verschlüsselung) aus asymmetrischer und symmetrischer Kryptografie bei großen Datenmengen in der Praxis Standard?
3. Welche Vorteile bietet Elliptic Curve Cryptography (ECC) gegenüber RSA?
4. Welches Problem löst das Diffie-Hellman-Verfahren, und warum muss das gemeinsame Geheimnis dabei nie über die Leitung übertragen werden?

### Modul 4: Hashes und Message Authentication Codes
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Eigenschaften kryptografischer Hash-Funktionen nennen.
  * Nach Abschluss dieses Moduls kann der Lernende Dateiprüfsummen erzeugen und verifizieren.
  * Nach Abschluss dieses Moduls kann der Lernende die Funktion eines HMACs zur Integritäts- und Authentizitätsprüfung erklären.
* **Voraussetzungen:** Modul 1, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Funktionsweise und Eigenschaften von Hash-Algorithmen (Kollisionsresistenz, Einwegfunktion) | 2 |
| 4.2 | Übersicht aktueller Hash-Algorithmen (SHA-2, SHA-3) und veralteter Algorithmen (MD5, SHA-1) | 2 |
| 4.3 | Message Authentication Codes (HMAC) in der Theorie | 2 |
| 4.4 | Praxis mit OpenSSL dgst und sha256sum | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Integritätsprüfung:** Legen Sie `~/krypto/m04/` an, erstellen Sie die Konfigurationsdatei `app.conf` (Inhalt z. B. `port=8080`) und speichern Sie den Hashwert mit `sha256sum app.conf > app.conf.sha256`. Prüfen Sie ihn mit `sha256sum -c app.conf.sha256` (Ausgabe `OK`). Ändern Sie ein einzelnes Zeichen (z. B. `sed -i 's/8080/8081/' app.conf`), prüfen Sie erneut (Ausgabe `FAILED`) und vergleichen Sie beide Hashwerte, um den Avalanche-Effekt zu dokumentieren. Berechnen Sie den Hash zusätzlich mit `openssl dgst -sha256 app.conf` und zeigen Sie, dass das Ergebnis übereinstimmt.
2. **HMAC generieren und prüfen:** Berechnen Sie mit `openssl dgst -sha256 -hmac "geheimes-passwort" app.conf` einen HMAC. Die Prüfung besteht darin, den HMAC mit demselben Schlüssel neu zu berechnen und zu vergleichen. Führen Sie sie dreimal durch: mit richtigem Schlüssel (gleicher Wert), mit falschem Schlüssel und mit geänderter Datei (jeweils anderer Wert). Notieren Sie, warum der Schlüssel in der Praxis nicht auf der Kommandozeile stehen sollte (Shell-History).

#### Kontrollfragen
1. Warum sollte MD5 nicht mehr für kryptografische Zwecke eingesetzt werden?
2. Worin unterscheidet sich ein HMAC von einem regulären SHA-256 Hash?
3. Was versteht man in der Kryptografie unter dem Begriff „Kollision“?
4. Nennen Sie drei Eigenschaften einer kryptografischen Hash-Funktion (z. B. Einwegfunktion, Kollisionsresistenz, Avalanche-Effekt) und erklären Sie sie in je einem Satz.

### Modul 5: Digitale Signaturen
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den Zusammenhang aus Hashing und asymmetrischer Kryptografie zur Signaturerstellung erklären.
  * Nach Abschluss dieses Moduls kann der Lernende digitale Signaturen von Dateien über OpenSSL erstellen.
  * Nach Abschluss dieses Moduls kann der Lernende Fremdsignaturen prüfen und das Ziel der Nicht-Abstreitbarkeit nachvollziehen.
* **Voraussetzungen:** Modul 3, Modul 4, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Das Prinzip der digitalen Signatur (Private Key signiert den Hash) | 2 |
| 5.2 | Authentizität, Integrität und Non-Repudiation (Nicht-Abstreitbarkeit) | 2 |
| 5.3 | Praxis: Dateien signieren (OpenSSL dgst -sign) | 2 |
| 5.4 | Praxis: Signaturen verifizieren | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Datei signieren:** Legen Sie `~/krypto/m05/` an und erstellen Sie `vertrag.txt`. Erzeugen Sie mit dem RSA-Privatschlüssel aus Modul 3 eine Signatur: `openssl dgst -sha256 -sign ../m03/private.pem -out vertrag.sig vertrag.txt`.
2. **Signatur verifizieren:** Prüfen Sie die Signatur ausschließlich mit dem öffentlichen Schlüssel: `openssl dgst -sha256 -verify ../m03/public.pem -signature vertrag.sig vertrag.txt` (Ausgabe `Verified OK`).
3. **Integritätsbruch nachweisen:** Hängen Sie mit `echo "Zusatz" >> vertrag.txt` Text an die Datei an und wiederholen Sie die Prüfung. Dokumentieren Sie, dass sie nun mit `Verification failure` fehlschlägt.
4. **Fremdsignatur prüfen:** Erzeugen Sie ein zweites RSA-Schlüsselpaar `partner.pem` und `partner-public.pem`, das einen Kommunikationspartner darstellt. Signieren Sie `angebot.txt` mit `partner.pem` (`angebot.sig`). Prüfen Sie die Signatur einmal mit `partner-public.pem` (gültig) und einmal mit `../m03/public.pem` (ungültig). Notieren Sie, woher Sie sicher wissen könnten, dass `partner-public.pem` tatsächlich dem Partner gehört (Ausblick auf Modul 6).

#### Kontrollfragen
1. Warum wird beim Signieren nicht das gesamte Dokument, sondern lediglich der Hashwert des Dokuments mit dem Private Key verschlüsselt?
2. Kann mit einer digitalen Signatur die Vertraulichkeit eines Dokuments gesichert werden? Begründen Sie.
3. Welche Komponente (Public Key oder Private Key) benötigen Sie, um die Signatur eines Kommunikationspartners zu verifizieren?
4. Was bedeutet Nicht-Abstreitbarkeit (Non-Repudiation), und warum reicht eine Signatur allein nicht aus, um sie einer bestimmten Person zuzuordnen?

### Modul 6: Zertifikate und Vertrauenskette (PKI)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende den X.509-Standard und die Inhalte eines Zertifikats benennen.
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip der Vertrauenskette (Chain of Trust) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikate parsen, auslesen und Fehler (z. B. Ablaufdaten) identifizieren.
* **Voraussetzungen:** Modul 5, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Das Identitätsproblem bei Public Keys (Wer ist der Inhaber?) | 2 |
| 6.2 | Der X.509-Standard (RFC 5280) und das PEM-Format (RFC 7468) | 2 |
| 6.3 | Die Public Key Infrastructure (PKI): Root-CAs, Sub-CAs, End-Entity-Zertifikate | 3 |
| 6.4 | Certificate Revocation (CRLs und OCSP) | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Zertifikatsanalyse lokal:** Legen Sie `~/krypto/m06/` an. Wählen Sie ein Root-CA-Zertifikat aus `/etc/ssl/certs` auf der Linux-VM (z. B. `ls /etc/ssl/certs | head`) und kopieren Sie es in das Arbeitsverzeichnis. Lesen Sie es mit `openssl x509 -in <zertifikat> -text -noout` aus und dokumentieren Sie Subject, Issuer, Validity und die x509v3-Erweiterungen (Basic Constraints, Key Usage, Subject Key Identifier). Ein Root-CA-Zertifikat enthält in der Regel keinen Subject Alternative Name; die SAN-Erweiterung analysieren Sie in Modul 7 an einem Server-Zertifikat.
2. **Ablaufdaten prüfen:** Lesen Sie das Ablaufdatum mit `openssl x509 -in <zertifikat> -noout -enddate` aus. Prüfen Sie mit `openssl x509 -in <zertifikat> -noout -checkend 86400` und `echo $?`, ob das Zertifikat in den nächsten 24 Stunden abläuft (Rückgabewert 0 = nein, 1 = ja). Wiederholen Sie die Prüfung mit einem sehr großen Wert (z. B. `-checkend $((60*60*24*365*30))`, 30 Jahre) und erklären Sie das Ergebnis. Prüfen Sie außerdem, ob sich das Root-Zertifikat selbst verifiziert: `openssl verify -CAfile <zertifikat> <zertifikat>`.

#### Kontrollfragen
1. Wie löst ein digitales Zertifikat das Problem, dass Sie bei einem einfachen Public Key nicht wissen, wem dieser gehört?
2. Welche Funktion hat eine Certificate Revocation List (CRL)?
3. Was bedeutet der Fehler "Self-signed certificate in certificate chain" in der Praxis?
4. Wer vertraut in einer Kette aus Root-CA, Sub-CA und Server-Zertifikat wem, und welches Zertifikat muss auf dem Client bereits vorhanden sein?

### Modul 7: OpenSSL in der Praxis (lokale CA)
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Certificate Signing Request (CSR) erzeugen.
  * Nach Abschluss dieses Moduls kann der Lernende eine temporäre, lokale Root-CA aufbauen.
  * Nach Abschluss dieses Moduls kann der Lernende serverseitige Zertifikate für definierte Hostnamen ausstellen (SAN).
* **Voraussetzungen:** Modul 3, Modul 6, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | Der Certificate Signing Request (CSR) | 2 |
| 7.2 | Erstellung einer lokalen selbstsignierten Root-CA | 3 |
| 7.3 | Die Bedeutung des Subject Alternative Name (SAN) in der heutigen Zeit | 3 |
| 7.4 | Ausstellung und Validierung eines Server-Zertifikats | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Root-CA aufbauen:** Legen Sie `~/krypto/m07/` an. Erzeugen Sie den CA-Schlüssel (`openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out ca.key`) und das selbstsignierte, 10 Jahre gültige Root-Zertifikat: `openssl req -x509 -new -key ca.key -sha256 -days 3650 -subj "/CN=Lab Root CA" -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign" -out ca.crt`. Prüfen Sie es mit `openssl x509 -in ca.crt -noout -subject -issuer -dates`.
2. **CSR für Server erstellen:** Erzeugen Sie einen Schlüssel `server.key` (RSA 2048) und den CSR: `openssl req -new -key server.key -subj "/CN=server.example.internal" -addext "subjectAltName=DNS:server.example.internal,IP:192.168.10.10" -out server.csr`. Kontrollieren Sie den Inhalt mit `openssl req -in server.csr -noout -text` (SAN unter „Requested Extensions“).
3. **Zertifikat ausstellen:** `openssl x509 -req` übernimmt Erweiterungen aus dem CSR nicht von selbst. Legen Sie deshalb die Datei `server.ext` an (Inhalt: `subjectAltName=DNS:server.example.internal,IP:192.168.10.10`, `basicConstraints=CA:FALSE`, `keyUsage=critical,digitalSignature,keyEncipherment`, `extendedKeyUsage=serverAuth`, jeweils eine Zeile) und signieren Sie den CSR: `openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -days 365 -sha256 -extfile server.ext -out server.crt`. Zeigen Sie zum Vergleich, was ohne `-extfile` passiert: Stellen Sie `nosan.crt` ohne diese Option aus und prüfen Sie `openssl x509 -in nosan.crt -noout -ext subjectAltName` (Ausgabe „No extensions in certificate“). `nosan.crt` wird danach nicht mehr verwendet.
4. **Zertifikat validieren:** Prüfen Sie `server.crt` mit `openssl x509 -in server.crt -noout -ext subjectAltName` (beide Einträge vorhanden) und `openssl verify -CAfile ca.crt server.crt` (Ausgabe `server.crt: OK`). Die Dateien `ca.crt`, `server.key` und `server.crt` werden in Modul 8 und 9 benötigt, `ca.key` verlässt die Linux-VM nie.

#### Kontrollfragen
1. Warum sollte der private Schlüssel einer Root-CA im produktiven Betrieb extrem geschützt (oder sogar offline) aufbewahrt werden?
2. Enthält der Certificate Signing Request (CSR) den privaten Schlüssel des anfragenden Servers?
3. Warum lehnen moderne Webbrowser Zertifikate, die nur den „Common Name“ (CN) aber keinen „Subject Alternative Name“ (SAN) besitzen, meist ab?

### Modul 8: Der TLS-Handshake
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Phasen eines TLS-Verbindungsaufbaus erklären.
  * Nach Abschluss dieses Moduls kann der Lernende Cipher-Suites aufschlüsseln und interpretieren.
  * Nach Abschluss dieses Moduls kann der Lernende wesentliche Unterschiede zwischen TLS 1.2 (RFC 5246) und TLS 1.3 (RFC 8446) benennen.
* **Voraussetzungen:** Modul 7 (Dateien `ca.crt`, `server.crt`, `server.key`), Windows-11-VM, Linux-VM mit `tshark`

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Überblick Transport Layer Security (TLS) | 2 |
| 8.2 | Der TLS-Handshake (Client Hello, Server Hello, Key Exchange) | 3 |
| 8.3 | Cipher Suites (Aufbau und Bestandteile) | 2 |
| 8.4 | Unterschiede und Verbesserungen von TLS 1.3 gegenüber TLS 1.2 | 3 |

#### Praxisaufgaben (Hands-on Lab)
1. **Lokalen TLS-Server starten:** Wechseln Sie auf `linux01` nach `~/krypto/m07/` und starten Sie in einem eigenen Terminal `openssl s_server -accept 4433 -cert server.crt -key server.key -www`. Die Option `-www` lässt den Server auf HTTP-Anfragen mit einer Statusseite antworten; ohne sie erhält ein Browser keine verwertbare Antwort. Der Server läuft, bis er mit Strg+C beendet wird.
2. **Handshake aufzeichnen:** Ermitteln Sie auf `linux01` die Netzwerkschnittstelle (`ip -br link`) und starten Sie in einem zweiten Terminal `sudo tshark -i <Schnittstelle> -f "tcp port 4433" -w ~/krypto/m08/tls13.pcapng` (Ordner vorher anlegen). Rufen Sie auf `win11-01` `curl.exe -vk https://192.168.10.10:4433/` auf (`-k` ignoriert die noch nicht vertraute CA, siehe Modul 9) und öffnen Sie dieselbe Adresse im Browser; dokumentieren Sie die Zertifikatswarnung. Beenden Sie danach den Mitschnitt mit Strg+C.
3. **Paketanalyse:** Werten Sie den Mitschnitt auf `linux01` aus, z. B. mit `tshark -r ~/krypto/m08/tls13.pcapng -Y "tls.handshake.type == 2" -V`. Lokalisieren Sie „Client Hello“ und „Server Hello“, notieren Sie die ausgehandelte Version und Cipher Suite und vermerken Sie, dass bei TLS 1.3 das Server-Zertifikat im Mitschnitt nicht lesbar ist (Verschlüsselung nach dem Server Hello). Die Filtersyntax kann mit `tshark -G fields` geprüft werden.
4. **TLS 1.2 vergleichen:** Starten Sie den Server neu mit zusätzlicher Option `-tls1_2`, wiederholen Sie Mitschnitt (`tls12.pcapng`) und Aufruf und vergleichen Sie: Version, Cipher Suite, Sichtbarkeit des Zertifikats im Mitschnitt, Anzahl der Handshake-Nachrichten. Halten Sie drei Unterschiede zu TLS 1.3 schriftlich fest.
5. **Cipher Suites zerlegen:** Zeigen Sie die ausgehandelten Suites mit `openssl ciphers -v` an (z. B. `openssl ciphers -v 'ECDHE-RSA-AES256-GCM-SHA384'`) und zerlegen Sie sie in Schlüsselaustausch, Authentifizierung, Verschlüsselung und MAC bzw. AEAD. Notieren Sie, warum TLS-1.3-Suites (z. B. `TLS_AES_256_GCM_SHA384`) keine Angabe zu Schlüsselaustausch und Signatur enthalten.

#### Kontrollfragen
1. Welche Daten sendet der Server typischerweise in der "Server Hello" Nachricht zurück an den Client?
2. Wofür steht das Konzept "Perfect Forward Secrecy" (PFS) innerhalb eines TLS-Handshakes?
3. Warum ist der TLS 1.3 Handshake in der Regel performanter als der von TLS 1.2?
4. Zerlegen Sie die Cipher Suite `ECDHE-RSA-AES256-GCM-SHA384` in ihre Bestandteile und erklären Sie, welche davon für Perfect Forward Secrecy sorgt.

### Modul 9: Zertifikatsprüfung und Fehlersuche in TLS
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikatswarnungen auf Windows-Systemen interpretieren und lösen.
  * Nach Abschluss dieses Moduls kann der Lernende Root-CAs systemweit auf Windows-Clients als vertrauenswürdig hinterlegen.
  * Nach Abschluss dieses Moduls kann der Lernende TLS-Verbindungen mittels OpenSSL `s_client` diagnostizieren.
* **Voraussetzungen:** Modul 7 und Modul 8, Windows-11-VM, Linux-VM (der `s_server` aus Modul 8 läuft oder wird mit Befehl aus Modul 8 Aufgabe 1 neu gestartet)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | Zertifikats-Speicher unter Windows (certlm.msc / certmgr.msc) | 2 |
| 9.2 | Fehlerbilder (Name Mismatch, Untrusted Root, Expired) | 3 |
| 9.3 | Fehleranalyse mit OpenSSL s_client | 3 |
| 9.4 | Troubleshooting-Szenarien aus der Administration | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Fehleranalyse über Kommandozeile:** Führen Sie auf `linux01` `echo | openssl s_client -connect 192.168.10.10:4433` aus. Der Server sendet nur sein Server-Zertifikat, die Lab-CA ist nicht als vertrauenswürdig hinterlegt; die Ausgabe zeigt deshalb `Verify return code: 21 (unable to verify the first certificate)`. Wiederholen Sie den Aufruf mit `-CAfile ~/krypto/m07/ca.crt` (Ergebnis `0 (ok)`). Fehler 18 würde ein selbstsigniertes Server-Zertifikat melden, Fehler 19 eine selbstsignierte Root in der gesendeten Kette. Zeigen Sie mit `-showcerts` die gesendete Kette.
2. **Namen und Gültigkeit prüfen:** Prüfen Sie `-verify_hostname server.example.internal` (ok) und `-verify_hostname falsch.example.internal` (`62 (hostname mismatch)`) sowie `-verify_ip 192.168.10.10`. Simulieren Sie ein abgelaufenes Zertifikat mit `openssl verify -CAfile ca.crt -attime $(date -d '+2 years' +%s) server.crt` (Meldung „certificate has expired“).
3. **Root-CA übertragen und vertrauen:** Holen Sie auf `win11-01` in PowerShell `ca.crt` per `scp <benutzer>@192.168.10.10:krypto/m07/ca.crt $env:USERPROFILE\Downloads\ca.crt`. Prüfen Sie die Übertragung, indem Sie `certutil -hashfile ca.crt SHA256` auf Windows und `sha256sum ca.crt` auf Linux vergleichen. Importieren Sie das Zertifikat über `certlm.msc` in „Vertrauenswürdige Stammzertifizierungsstellen“ des lokalen Computers (alternativ in einer Administrator-PowerShell: `Import-Certificate -FilePath .\ca.crt -CertStoreLocation Cert:\LocalMachine\Root`).
4. **Erfolgsnachweis:** Rufen Sie in einem neu gestarteten Browser `https://192.168.10.10:4433` auf. Dokumentieren Sie, dass keine Warnung erscheint, und prüfen Sie in den Zertifikatdetails den SAN-Eintrag. `curl.exe -v https://192.168.10.10:4433/` (ohne `-k`) muss jetzt ebenfalls funktionieren.
5. **Fehlerbild Name Mismatch:** Tragen Sie in `C:\Windows\System32\drivers\etc\hosts` (Editor als Administrator) die Zeilen `192.168.10.10 server.example.internal` und `192.168.10.10 falsch.example.internal` ein. Rufen Sie `https://server.example.internal:4433` (ok) und `https://falsch.example.internal:4433` (Zertifikatsfehler zum Namen) auf. Entfernen Sie die Einträge anschließend wieder.
6. **Troubleshooting-Protokoll:** Erstellen Sie eine Tabelle mit den Fehlerbildern Untrusted Root, Name Mismatch und Expired: Fehlermeldung (Browser und `s_client`), Ursache, Prüfbefehl, Behebung.

#### Kontrollfragen
1. Wenn ein Browser meldet, dass das Zertifikat für die aufgerufene Domain nicht gültig ist (Name Mismatch), welcher Bestandteil des Zertifikats wurde vom System geprüft?
2. Warum löst das Importieren des Server-Zertifikats (`server.crt`) direkt in den Root-Store konzeptionell das Problem zwar für einen Dienst, skaliert in der Praxis aber nicht?
3. Welche Informationen liefert OpenSSL `s_client` bezüglich der vom Server angebotenen Vertrauenskette (Certificate Chain)?
4. Welche vier Prüfungen führt ein Client bei der Validierung eines Server-Zertifikats durch (Vertrauenskette, Gültigkeitszeitraum, Namensprüfung, Sperrstatus), und welche davon wurde in den Aufgaben 1 bis 5 jeweils ausgelöst?

### Modul 10: Verschlüsselung ruhender Daten: LUKS
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Funktion von Full-Disk-Encryption (FDE) unter Linux benennen.
  * Nach Abschluss dieses Moduls kann der Lernende einen LUKS-Container erstellen, öffnen und formatieren.
  * Nach Abschluss dieses Moduls kann der Lernende LUKS-Volumeschlüssel (Key Slots) verwalten.
* **Voraussetzungen:** Modul 2, Linux-VM mit zusätzlicher leerer virtueller Festplatte (VHDX, ca. 5 GB)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Konzepte der Data-at-Rest-Verschlüsselung | 2 |
| 10.2 | Architektur des Linux Unified Key Setup (LUKS) | 2 |
| 10.3 | Einrichtung und Verwaltung mit cryptsetup | 2 |
| 10.4 | Key-Slots, Backup und Wiederherstellung des LUKS-Headers | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Container erstellen:** Ermitteln Sie die zusätzliche Festplatte mit `lsblk` (ca. 5 GB, ohne Partitionen, z. B. `/dev/sdb`) und stellen Sie sicher, dass es nicht das Systemlaufwerk ist; `luksFormat` zerstört alle Daten darauf. Erstellen Sie vorab einen Prüfpunkt. Führen Sie `sudo cryptsetup luksFormat /dev/sdb` aus (Bestätigung mit `YES` in Großbuchstaben, sicheres Kennwort). Prüfen Sie mit `sudo blkid /dev/sdb`, dass der Typ `crypto_LUKS` ist.
2. **Mounten und Beschreiben:** Öffnen Sie den Container mit `sudo cryptsetup luksOpen /dev/sdb secure`, formatieren Sie `/dev/mapper/secure` mit `sudo mkfs.ext4`, legen Sie `/mnt/secure` an, mounten Sie dorthin und erstellen Sie die Testdatei `test.txt`. Hängen Sie mit `umount` aus und schließen Sie den Container mit `sudo cryptsetup luksClose secure`.
3. **Schlüsselverwaltung:** Fügen Sie mit `sudo cryptsetup luksAddKey /dev/sdb` ein zweites Kennwort hinzu und testen Sie den Zugriff damit. Zeigen Sie mit `sudo cryptsetup luksDump /dev/sdb` die belegten Key Slots an.
4. **Header sichern und wiederherstellen:** Sichern Sie den Header mit `sudo cryptsetup luksHeaderBackup /dev/sdb --header-backup-file ~/krypto/m10/luks-header.img`. Lesen Sie in `luksDump` die Größe bzw. den Offset des Datensegments ab (bei LUKS2 standardmäßig 16 MiB). Überschreiben Sie nur den Header-Bereich der Übungsplatte (`sudo dd if=/dev/zero of=/dev/sdb bs=1M count=16`, nicht mehr als der Offset) und zeigen Sie, dass `luksOpen` fehlschlägt. Stellen Sie den Header mit `sudo cryptsetup luksHeaderRestore /dev/sdb --header-backup-file ~/krypto/m10/luks-header.img` wieder her und prüfen Sie, dass `test.txt` wieder lesbar ist. Notieren Sie: Die Header-Sicherung enthält auch entfernte Key Slots und muss selbst geschützt werden.

#### Kontrollfragen
1. Warum schützt Full-Disk-Encryption (FDE) nicht vor laufzeitbasierten Angriffen (wie Ransomware), während das System läuft und das Laufwerk gemountet ist?
2. Was befindet sich im LUKS-Header, und warum führt eine Beschädigung des Headers zum vollständigen Datenverlust?
3. Wie ermöglicht LUKS, dass mehrere Benutzer mit jeweils eigenem Kennwort auf dieselbe verschlüsselte Partition zugreifen können?

### Modul 11: Verschlüsselung ruhender Daten: BitLocker
* **Priorität:** 2 (Vertiefung)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende das Prinzip von BitLocker unter Windows erklären.
  * Nach Abschluss dieses Moduls kann der Lernende ein Datenlaufwerk per Kennwort mit BitLocker verschlüsseln („BitLocker To Go“ bezeichnet die Variante für Wechseldatenträger).
  * Nach Abschluss dieses Moduls kann der Lernende BitLocker-Wiederherstellungsschlüssel verwalten und anwenden.
* **Voraussetzungen:** Modul 1, Windows-11-VM (Pro, Enterprise oder Education) mit zusätzlicher unformatierter virtueller Festplatte (VHDX, ca. 5 GB)

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | Architektur und Komponenten von BitLocker | 2 |
| 11.2 | Schutzmethoden (TPM vs. Kennwort vs. USB-Startup-Key) | 2 |
| 11.3 | Konfiguration von BitLocker auf Datenlaufwerken (ohne Systempartition) | 2 |
| 11.4 | Verwaltung von Recovery-Keys und Recovery-Szenarien | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Laufwerk vorbereiten:** Erstellen Sie einen Prüfpunkt von `win11-01`. Initialisieren Sie die zusätzliche Festplatte in der Datenträgerverwaltung (`diskmgmt.msc`, GPT), erstellen Sie ein NTFS-Volume mit einem freien Laufwerksbuchstaben (z. B. `E:`; `D:` ist in Hyper-V häufig vom virtuellen DVD-Laufwerk belegt) und legen Sie darauf die Datei `test.txt` ab.
2. **BitLocker aktivieren:** Aktivieren Sie BitLocker für das Datenlaufwerk (Rechtsklick im Explorer oder Systemsteuerung). Wählen Sie die Entsperrung per Kennwort (ein TPM ist für Datenlaufwerke nicht erforderlich). Speichern Sie den Wiederherstellungsschlüssel als Textdatei auf dem Systemlaufwerk `C:` (nicht auf dem verschlüsselten Laufwerk). Wählen Sie „Nur verwendeten Speicherplatz verschlüsseln“ und die übrigen Vorgaben des Assistenten, und prüfen Sie nach Abschluss mit `manage-bde -status E:` Verschlüsselungsmethode und Schutzstatus.
3. **Schutzmethoden prüfen:** Zeigen Sie mit `manage-bde -protectors -get E:` die Schlüsselschutzvorrichtungen (Kennwort, numerisches Kennwort) und ihre IDs an und vergleichen Sie die ID des numerischen Kennworts mit der ID in der gespeicherten Textdatei.
4. **Wiederherstellung testen:** Schließen Sie alle Fenster, die auf `E:` zugreifen, und sperren Sie das Laufwerk mit `manage-bde -lock E:`. Prüfen Sie, dass der Zugriff verweigert wird. Entsperren Sie nicht mit dem Kennwort, sondern mit dem 48-stelligen Wiederherstellungskennwort aus der Textdatei: `manage-bde -unlock E: -recoverypassword <Kennwort mit Bindestrichen>`. Prüfen Sie, dass `test.txt` wieder lesbar ist.

#### Kontrollfragen
1. Welche primäre Funktion hat ein Trusted Platform Module (TPM) im Zusammenhang mit BitLocker für die Windows-Systempartition?
2. Wozu dient der BitLocker-Wiederherstellungsschlüssel (Recovery Key) und wo sollte er in Produktivumgebungen abgelegt sein?
3. Worin unterscheiden sich BitLocker "Used Disk Space Only" Verschlüsselung und die vollständige Laufwerksverschlüsselung bei der Ersteinrichtung?

### Modul 12: Passwörter und Hashing
* **Priorität:** 1 (Pflicht)
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Konzepte "Salting" und "Key Derivation Functions (KDF)" erklären.
  * Nach Abschluss dieses Moduls kann der Lernende die Speicherung von Passwörtern unter Linux untersuchen.
  * Nach Abschluss dieses Moduls kann der Lernende Passwort-Hashes mit OpenSSL erzeugen und mit Einträgen in `/etc/shadow` vergleichen.
* **Voraussetzungen:** Modul 4, funktionsfähige Linux-VM

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Das Problem einfacher Hashes für Passwörter (Rainbow Tables) | 2 |
| 12.2 | Das Prinzip von Salt und Pepper | 2 |
| 12.3 | Key Derivation Functions und Work Factor (PBKDF2, Argon2, bcrypt, yescrypt) | 2 |
| 12.4 | Systemseitige Passwortspeicherung unter Linux (/etc/shadow) | 2 |

#### Praxisaufgaben (Hands-on Lab)
1. **Struktur von /etc/shadow analysieren:** Zeigen Sie die Rechte der Datei (`ls -l /etc/shadow`) und Ihren eigenen Eintrag (`sudo grep "^$(whoami):" /etc/shadow`). Dokumentieren Sie den Aufbau (Felder durch `:` getrennt). Identifizieren Sie anhand der Kennung (z. B. `$y$` für yescrypt, `$6$` für SHA-512) den Algorithmus sowie Parameter, Salt und Hash. Die Kennung unterscheidet sich je nach Distribution; dokumentieren Sie die auf Ihrer VM gefundene.
2. **Hashes mit OpenSSL erzeugen:** Erzeugen Sie mit `openssl passwd -6 'Kurs2026!'` zweimal einen Hash und vergleichen Sie die Salts. Erzeugen Sie ihn danach zweimal mit fest vorgegebenem Salt (`openssl passwd -6 -salt abcdefgh 'Kurs2026!'`) und erklären Sie das Ergebnis (gleiche Eingabe, gleicher Hash). Vergleichen Sie den Formataufbau (`$6$Salt$Hash`) mit dem Eintrag aus `/etc/shadow`.
3. **Work Factor messen:** Messen Sie mit `time openssl kdf -keylen 32 -kdfopt digest:SHA256 -kdfopt 'pass:Kurs2026!' -kdfopt salt:abcdefgh -kdfopt iter:1000 PBKDF2` und mit `iter:5000000` die Rechenzeit (Richtwert in der Testumgebung: wenige Millisekunden gegenüber ca. 1 Sekunde). Erklären Sie, warum ein hoher Work Factor Angreifer ausbremst, legitime Logins aber kaum.

#### Kontrollfragen
1. Warum schützt ein individuelles "Salt" vor der effizienten Nutzung von vorberechneten Rainbow Tables?
2. Warum werden für Passwörter Algorithmen wie Argon2 oder bcrypt verwendet anstelle von schnellen Hashes wie SHA-256?
3. Welche Angaben enthält ein Passwort-Eintrag in `/etc/shadow` zusätzlich zum Hash (Kennung, Salt, ggf. Parameter), damit das System einen Login überprüfen kann?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Stundensummen (110 UE), Prioritäten (10x P1, 2x P2) und Modulreihenfolge blieben unverändert. Die OpenSSL-Befehle der Module 2 bis 7, 9 und 12 wurden in einer Testumgebung mit OpenSSL 3.0.13 ausgeführt; die Ausgaben stehen so im Text. Die Befehle der Module 8, 10 und 11 (tshark, cryptsetup, manage-bde, Windows-Oberflächen) wurden nicht ausgeführt.

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf, A.2 | Vorkenntnisse und Out-of-Scope präzisiert; Quellen zu HMAC, OCSP, PKCS#1, PBKDF2, Argon2, ChaCha20, AES, SHA, GCM, LUKS und BitLocker ergänzt | Verfahren und Normen kamen im Plan vor, hatten aber keine Quelle |
| A.3 | Vorbereitung mit Internet, Edition Windows 11, Pakete, Hostnamen, Arbeitsverzeichnis, Dateiübertragung, Zeitsynchronisierung, Prüfpunkte | Der private Switch hat kein Internet, die Pakete waren also nicht installierbar; BitLocker braucht Pro oder höher; `ca.crt` konnte nicht auf Windows gelangen; `wireshark` auf einem Server ohne Oberfläche |
| Modul 1 | Kontrollfrage 3 umformuliert, Fragen 4 und 5 neu; BSI-Aufgabe ohne „2026+“ | Frage nach „drei primären Schutzzielen“ passte nicht zur Einheit mit vier Zielen (Verfügbarkeit fehlte); Lernziele zu historischen Verfahren und zum Unterschied sym./asym. hatten keine Frage |
| Modul 2 | `-pbkdf2`, Blockzählung mit `od`, Aufgabe 3 zu GCM, Frage 4 | Ohne `-pbkdf2` erscheint eine Warnung; „Bitmap-Bild“ war auf einem Server ohne Oberfläche nicht auswertbar; GCM war Lernziel ohne Übung (`openssl enc` unterstützt es nicht); Block-/Stromchiffre hatte keine Frage |
| Modul 3 | Befehle, Ordner, Passwortkopie als eigene Datei, Frage 4 | Die passwortgeschützte Kopie hätte den Schlüssel in Modul 5 unbrauchbar machen können; Diffie-Hellman hatte keine Frage |
| Modul 4 | Befehle, Prüfung des HMAC, Frage 4 | „Überprüfung“ des HMAC war nicht beschrieben; Eigenschaften von Hashes hatten keine Frage |
| Modul 5 | Aufgabe 4 (Fremdsignatur), Frage 4 | Lernziel „Fremdsignaturen prüfen“ und „Nicht-Abstreitbarkeit“ hatte keine Aufgabe bzw. Frage |
| Modul 6 | Aufgabe 1 ohne SAN-Erwartung, Aufgabe 2 zu Ablaufdaten, Frage 4 | Root-Zertifikate haben keinen SAN; Lernziel „Ablaufdaten identifizieren“ hatte keine Aufgabe; „Laden Sie ... in das Arbeitsverzeichnis“ war missverständlich |
| Modul 7 | `server.ext`, Vergleich ohne SAN, Validierung, Voraussetzung Modul 3, Frage 3 | `openssl x509 -req` übernimmt den SAN aus dem CSR nicht; das Zertifikat hätte in Modul 9 trotz Import einen Namensfehler gezeigt. Frage 3 sprach von „akzeptieren ... als fehlerhaft“ |
| Modul 8 | `-www`, `curl.exe` statt `Invoke-WebRequest`, Auswertung mit `tshark`, TLS-1.2-Vergleich, Cipher-Suite-Zerlegung, Frage 4 | `s_server` ohne `-www` antwortet Browsern nicht; `Invoke-WebRequest` in Windows PowerShell 5.1 kann Zertifikatsfehler nicht ignorieren; Wireshark war auf keiner VM verfügbar; Lernziele „Unterschiede 1.2/1.3“ und „Cipher Suites aufschlüsseln“ hatten keine Aufgabe |
| Modul 9 | Fehlercode 21 statt 18; Übertragung per `scp` mit Hashprüfung; Aufgaben zu Name Mismatch und Expired; Troubleshooting-Protokoll; Frage 4 | Die erste Fassung nannte „Fehler 18 ... self signed certificate in certificate chain“; tatsächlich meldet OpenSSL 21 (Fehler 18 steht für selbstsigniert, 19 für „in certificate chain“). Der Weg des Zertifikats auf die Windows-VM fehlte. Zwei der drei Fehlerbilder aus Einheit 9.2 wurden nie geübt |
| Modul 10 | Auswahl der Platte mit `lsblk`, Prüfpunkt, Befehle, Header-Backup und -Restore | Einheit 10.4 (Header-Backup und Wiederherstellung) hatte keine Aufgabe; `/dev/sdb` wurde ohne Prüfung vorgegeben (Risiko für das Systemlaufwerk) |
| Modul 11 | Voraussetzung Modul 1 statt Modul 10; Laufwerksbuchstabe `E:`; `manage-bde`-Befehle; Lernziel präzisiert | Modul 11 hing grundlos von Modul 10 (LUKS) ab; `D:` ist in Hyper-V oft das DVD-Laufwerk; „BitLocker To Go“ gilt für Wechseldatenträger; Protektoren und Recovery-ID wurden nicht geübt |
| Modul 12 | Aufgabe 3 (Work Factor), Salt-Vergleich, Lernziel 3 und Frage 3 umformuliert | Einheit 12.3 (KDF, Work Factor) hatte keine Aufgabe; „Passwort-Hashes zur Konfiguration simulieren“ und „Salt-Block“ waren unklar |

**Bewertung des Prüfvermerks der ersten Fassung:** Punkt 1 ist korrekt. Punkt 2 ist teilweise erfüllt (Pakete und Windows-Edition ohne Beschaffungsweg). Punkt 3 ist nicht erfüllt: mehrere Verfahren hatten keine Quelle. Punkt 4 ist nicht erfüllt: Das Zertifikat ohne SAN und der `s_server` ohne `-www` hätten Modul 8 und 9 behindert. Punkt 5 ist nicht erfüllt: Unter anderem hatten Einheit 8.4, 9.2, 10.4 und 12.3 keine Aufgabe, mehrere Lernziele keine Kontrollfrage. Punkt 6 ist teilweise erfüllt (Isolation ja, Beschaffung der Software nein). Punkt 7 ist nicht erfüllt: Dateiübertragung, Hostnamen, Internetphase und Windows-Edition fehlten.

**Hinweise und offene Punkte:**

* **Nicht bestätigt, vor Kursstart prüfen:** `tshark`-Filter und Schnittstellenname; Meldungen von Edge und `curl.exe` bei nicht vertrauter CA und bei Namensfehler; `scp`-Verfügbarkeit unter Windows 11; Assistenten und Menünamen von BitLocker in der deutschen Oberfläche; die Größe des LUKS2-Headers (16 MiB) und das Verhalten von `luksHeaderRestore`; die URLs der NIST- und cryptsetup-Quellen.
* Das Pflichtmodul 12 steht nach den Vertiefungsmodulen 10 und 11 (Priorität 2). Sie hängt nur von Modul 4 ab und kann übersprungen oder vorgezogen unterrichtet werden. Die Reihenfolge wurde nicht geändert.
* Die Erklärung „Der Private Key signiert den Hash“ (Einheit 5.1, Kontrollfrage 1) ist eine didaktische Vereinfachung; technisch ist eine Signatur keine Verschlüsselung des Hashwerts. Sie wurde belassen.
