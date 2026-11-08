# Lehrplan: Zertifikatsdienste und PKI (AD CS)

| Kategorie | Details |
| :--- | :--- |
| **Zielgruppe** | Auszubildende, Quereinsteiger und angehende Systemadministratoren bzw. Systemtechniker (Raum Österreich/EU) |
| **Vorkenntnisse** | IT-Grundlagen, Grundkenntnisse Netzwerke (IP-Adressen, Subnetze), DNS-Grundlagen, Active-Directory-Grundlagen, Grundkenntnisse zu Gruppenrichtlinien (GPO anlegen und mit einer OU verknüpfen), erste Erfahrung mit PowerShell und Kommandozeile |
| **Gesamtumfang** | 12 Module, 116 Unterrichtseinheiten (UE) |
| **Fokus-Technologien** | Windows Server Active Directory Certificate Services (AD CS) |
| **Thematische Abgrenzung (Out of Scope)** | Kryptografie-Theorie (gehört in den Kurs „Kryptografie, Zertifikate und TLS“); Modul 1 vermittelt nur die für die Praxis nötigen PKI-Konzepte. Reiner Fokus auf die Praxis mit AD CS |

## A. Kursübersicht & Metadaten

### 1. Tabellarische Gesamtübersicht (Master-Tabelle)

| Modul-Nr. | Modultitel | Priorität (1/2) | Stunden (UE) |
| :--- | :--- | :--- | :--- |
| 1 | Grundlagen der Public Key Infrastructure (PKI) | 1 | 8 |
| 2 | Design und Vorbereitung einer zweistufigen PKI | 1 | 8 |
| 3 | Bereitstellung der Offline-Root-CA | 1 | 12 |
| 4 | Bereitstellung der ausstellenden Enterprise-CA | 1 | 12 |
| 5 | Verwaltung von Zertifikatvorlagen (Templates) | 1 | 10 |
| 6 | Zertifikatsausstellung und Autoenrollment | 1 | 10 |
| 7 | Sperrlisten (CRL) und Online Responder (OCSP) | 1 | 12 |
| 8 | Zertifikate für Webserver und Clients | 1 | 10 |
| 9 | Zertifikatsbasierte Authentifizierung (802.1X / NPS) | 2 | 10 |
| 10 | Sicherung, Wiederherstellung und Migrationskonzept der CA | 1 | 8 |
| 11 | Sicherheit, Fehlkonfigurationen und Best Practices | 1 | 8 |
| 12 | Troubleshooting und Diagnosewerkzeuge | 2 | 8 |
| **Gesamt** | **10x Prio 1, 2x Prio 2** | | **116** |

*Hinweis zur Priorisierung: Module mit Priorität 1 (Pflicht) bilden die Kernkompetenz. Module mit Priorität 2 (Vertiefung) erweitern das Wissen für komplexe Enterprise-Szenarien.*

### 2. Quellen

*   **Active Directory Certificate Services Overview**, Microsoft Corporation, Stand nicht geprüft, [https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview)
*   **RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile**, IETF, Mai 2008, [https://datatracker.ietf.org/doc/html/rfc5280](https://datatracker.ietf.org/doc/html/rfc5280)
*   **Securing Public Key Infrastructure (PKI)**, Microsoft Corporation, URL und Inhalt nicht geprüft, [https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/securing-pki](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/securing-pki)
*   **RFC 6960: X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP**, IETF, Juni 2013, [https://datatracker.ietf.org/doc/html/rfc6960](https://datatracker.ietf.org/doc/html/rfc6960)
*   **CAPolicy.inf Syntax**, Microsoft Corporation, abgerufen am 08.11.2026, [https://learn.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/prepare-the-capolicy-inf-file](https://learn.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/prepare-the-capolicy-inf-file)
*   **PKI design considerations using Active Directory Certificate Services** (CDP, AIA, Delta-CRL auf Offline-Root), Microsoft Corporation, abgerufen am 08.11.2026, [https://learn.microsoft.com/windows-server/identity/ad-cs/pki-design-considerations](https://learn.microsoft.com/windows-server/identity/ad-cs/pki-design-considerations)
*   **Operate certificate revocation, CRL publication, and CDP changes in AD CS**, Microsoft Corporation, abgerufen am 08.11.2026, [https://learn.microsoft.com/windows-server/identity/ad-cs/operate-certificate-revocation-crl-cdp](https://learn.microsoft.com/windows-server/identity/ad-cs/operate-certificate-revocation-crl-cdp)
*   **Configure AIA issuer retrieval and validate certificate endpoints** (OCSP-Erweiterung, Cryptnet-Cache), Microsoft Corporation, abgerufen am 08.11.2026, [https://learn.microsoft.com/windows-server/identity/ad-cs/configure-certificate-path-validation-revocation-policy](https://learn.microsoft.com/windows-server/identity/ad-cs/configure-certificate-path-validation-revocation-policy)
*   **Migrate a Certification Authority**, Microsoft Corporation, abgerufen am 08.11.2026, [https://learn.microsoft.com/windows-server/identity/ad-cs/migrate-certification-authority](https://learn.microsoft.com/windows-server/identity/ad-cs/migrate-certification-authority)
*   **certutil** (Befehlsreferenz), Microsoft Corporation, abgerufen am 08.11.2026, [https://learn.microsoft.com/windows-server/administration/windows-commands/certutil](https://learn.microsoft.com/windows-server/administration/windows-commands/certutil)
*   **Certified Pre-Owned: Abusing Active Directory Certificate Services (ESC1 bis ESC8)**, Will Schroeder und Lee Christensen, SpecterOps, 2021 (Jahr aus dem Gedächtnis, nicht geprüft), [https://specterops.io/assets/resources/Certified_Pre-Owned.pdf](https://specterops.io/assets/resources/Certified_Pre-Owned.pdf)

### 3. Labor-Setup & Rahmenbedingungen

Alle Praxisaufgaben finden in einer isolierten Hyper-V-Umgebung statt. Es existiert keine unkontrollierte Verbindung zum Heim- oder Produktivnetz (privater vSwitch).
*   **Privater virtueller Switch `vSwitch-PKI-Privat`:** Netz `192.168.60.0/24`, ohne Gateway, ohne DHCP, alle Adressen statisch. Erforderlich ab Modul 2.
*   **VM 1: Domain Controller (DC01):** Windows Server 2022 (Evaluation), IP `192.168.60.10`, DNS-Rolle, AD DS installiert (Domäne `corp.internal`). Der Aufbau von AD DS gehört nicht zum Kurs und wird vor Kursbeginn vorbereitet. Erforderlich ab Modul 2.
*   **VM 2: Offline-Root-CA (ROOTCA01):** Windows Server 2022 (Evaluation), keine Domänenmitgliedschaft und **ohne Netzwerkadapter** (offline). Der Datenaustausch läuft ausschließlich über die virtuelle Festplatte `Transfer.vhdx` (siehe unten). Erforderlich ab Modul 2 (CAPolicy.inf).
*   **VM 3: Enterprise Issuing CA (SUBCA01):** Windows Server 2022 (Evaluation), IP `192.168.60.20`, DNS `192.168.60.10`. Der Domänenbeitritt zu `corp.internal` erfolgt in Modul 4. Erforderlich ab Modul 4. Hostet in diesem Labor auch den Webserver (IIS) für CDP/AIA und den Online Responder; das ist eine Laborvereinfachung.
*   **VM 4: Client (CL01):** Windows 11 Enterprise (Evaluation), IP `192.168.60.50`, DNS `192.168.60.10`. Der Domänenbeitritt erfolgt in Modul 6. Erforderlich ab Modul 6.
*   **Transfer.vhdx:** Eine kleine virtuelle Festplatte (1 GB, dynamisch, NTFS, Laufwerk `T:`), die jeweils nur an eine laufende VM angeschlossen ist. Sie ersetzt das Netzwerk zwischen `ROOTCA01` und dem Rest des Labors (Anschluss und Abtrennen im laufenden Betrieb über einen SCSI-Controller).
*   **Namen:** Root-CA `Corp-Root-CA`, Issuing-CA `Corp-Issuing-CA`, CDP/AIA-Alias `pki.corp.internal` (CNAME auf `subca01.corp.internal`), Webalias `www.corp.internal`.
*   **Prüfpunkte:** Hyper-V-Prüfpunkte von `DC01`, `SUBCA01` und `CL01` am Ende von Modul 4 (`M4-PKI`) und vor Modul 10 und 11. `ROOTCA01` bekommt keinen Prüfpunkt, sondern eine Sicherung (Modul 10).

---

## B. Detaillierter Modulaufbau

### Modul 1: Grundlagen der Public Key Infrastructure (PKI)
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Komponenten einer PKI (CA, RA, Zertifikate, Schlüssel) erklären.
  * Nach Abschluss dieses Moduls kann der Lernende den Unterschied zwischen einer Standalone- und einer Enterprise-CA beschreiben.
* **Voraussetzungen:** Keine.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 1.1 | Einführung in PKI-Konzepte und X.509-Struktur (RFC 5280) | 4 |
| 1.2 | Architektur-Modelle in AD CS (Standalone vs. Enterprise) | 4 |

#### Praxisaufgaben (Hands-on Lab)
*Für dieses theoretische Modul ist kein technisches Labor erforderlich. Die Praxis wird durch eine Fallstudie ersetzt.*
1. **Fallstudie:** Skizzierung der Zertifikatsketten und Vertrauensstellungen eines fiktiven Unternehmens auf Papier/Whiteboard zur Vorbereitung der Labor-Installation.

#### Kontrollfragen
1. Warum benötigt eine Enterprise-CA zwingend eine Active Directory-Umgebung, während eine Standalone-CA auch in einer Arbeitsgruppe funktioniert?
2. Welche Informationen sind gemäß RFC 5280 zwingend in einem X.509-Zertifikat enthalten?
3. Welchen Zweck erfüllt die "Subject Alternative Name" (SAN)-Erweiterung in modernen Zertifikaten?
4. Nennen Sie drei Unterschiede zwischen einer Standalone- und einer Enterprise-CA (Active-Directory-Integration, Zertifikatvorlagen, Genehmigung von Anträgen).
5. Welche Aufgaben haben CA, RA und der private Schlüssel, und was bedeutet die Kompromittierung des Schlüssels einer Root-CA?

### Modul 2: Design und Vorbereitung einer zweistufigen PKI
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die `CAPolicy.inf` für die Root-CA erstellen und konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende die AD DS-Grundstruktur für die PKI-Integration vorbereiten.
* **Voraussetzungen:** Modul 1, funktionsfähiger DC (`DC01`), VM `ROOTCA01` (offline).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 2.1 | Planung von Sperrlisten-Verteilungspunkten (CDP) und AIA | 4 |
| 2.2 | Vorbereitung der Konfigurationsdatei (CAPolicy.inf) | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Infrastruktur-Check und Objekte anlegen:** Überprüfe auf `DC01` die DNS-Auflösung (`Resolve-DnsName dc01.corp.internal`). Lege die Organisationseinheiten `PKI-Server` (für die zukünftige Enterprise-CA) und `Clients` an, in `Clients` den Benutzer `user1`, sowie die Sicherheitsgruppen `SG-WebAdmins` und `SG-PKI-Users` (jeweils mit `user1` als Mitglied). Lege in der DNS-Zone `corp.internal` einen A-Record `subca01` (`192.168.60.20`) und die CNAME-Einträge `pki` und `www` auf `subca01.corp.internal` an.
2. **CAPolicy-Erstellung:** Erstelle auf der isolierten `ROOTCA01` (ohne Domäne, ohne Netzwerk) die Datei `C:\Windows\CAPolicy.inf` mit folgendem Inhalt (Kodierung ANSI, Dateiendung `.inf`, nicht `.txt`). Die Datei muss vor der Installation der Root-CA existieren (Quelle: *CAPolicy.inf Syntax*):
   ```ini
   [Version]
   Signature="$Windows NT$"
   [Certsrv_Server]
   RenewalKeyLength=4096
   RenewalValidityPeriod=Years
   RenewalValidityPeriodUnits=20
   CRLPeriod=Weeks
   CRLPeriodUnits=26
   ```
   Erkläre schriftlich, welche Werte nur bei einer Erneuerung und welche bei der Installation wirken. Die Gültigkeit des ersten Root-Zertifikats wird in Modul 3 bei der Installation festgelegt.
3. **Transfermedium:** Erstelle auf dem Hyper-V-Host `Transfer.vhdx` (z. B. `New-VHD -Path D:\VMs\Transfer.vhdx -SizeBytes 1GB -Dynamic`), schließe sie an `ROOTCA01` an, initialisiere und formatiere sie (NTFS, Laufwerk `T:`) und trenne sie wieder.

#### Kontrollfragen
1. Welche Auswirkungen hat das Fehlen einer `CAPolicy.inf` während der Installation einer Root-CA?
2. Warum sollten CDP- (CRL Distribution Point) und AIA-Pfad (Authority Information Access) idealerweise HTTP-basiert und nicht LDAP-basiert sein?
3. Welche AD-Gruppe berechtigt standardmäßig zur Verwaltung von Zertifikatvorlagen in der Domäne?

### Modul 3: Bereitstellung der Offline-Root-CA
* **Priorität:** 1
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Standalone-Root-CA installieren.
  * Nach Abschluss dieses Moduls kann der Lernende CDP- und AIA-Erweiterungen auf der Root-CA konfigurieren.
* **Voraussetzungen:** Modul 2, VM `ROOTCA01`.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 3.1 | Installation der Rolle AD CS als Standalone Root CA | 6 |
| 3.2 | Post-Installation: Konfiguration von CDP, AIA und CRL-Veröffentlichung | 6 |

#### Praxisaufgaben (Hands-on Lab)
1. **CA-Installation:** Installiere die Rolle AD CS auf `ROOTCA01` (`Install-WindowsFeature ADCS-Cert-Authority -IncludeManagementTools`) und konfiguriere sie als Standalone Root-CA, z. B. mit `Install-AdcsCertificationAuthority -CAType StandaloneRootCa -CACommonName "Corp-Root-CA" -CryptoProviderName "RSA#Microsoft Software Key Storage Provider" -KeyLength 4096 -HashAlgorithmName SHA256 -ValidityPeriod Years -ValidityPeriodUnits 10` (Parameter mit `Get-Help` prüfen; die Konsole ist eine gleichwertige Alternative). Das Root-Zertifikat ist 10 Jahre gültig.
2. **Laufzeiten festlegen:** Setze die Laufzeit der von der Root-CA ausgestellten Zertifikate auf 5 Jahre (`certutil -setreg CA\ValidityPeriodUnits 5`, `certutil -setreg CA\ValidityPeriod "Years"`), die Gültigkeit der Basis-CRL auf 26 Wochen (`certutil -setreg CA\CRLPeriodUnits 26`, `certutil -setreg CA\CRLPeriod "Weeks"`) und deaktiviere Delta-CRLs (`certutil -setreg CA\CRLDeltaPeriodUnits 0`). Microsoft empfiehlt, auf einer Offline-Root keine Delta-CRLs zu veröffentlichen (Quelle: *PKI design considerations*). Standardwerte würden das Zertifikat der Issuing-CA nur 1 Jahr gültig machen und die CRL schon nach 1 Woche ablaufen lassen.
3. **Erweiterungen anpassen:** Entferne die Standard-LDAP- und -HTTP-Pfade und füge die HTTP-Pfade hinzu, z. B. mit `Get-CACrlDistributionPoint | ForEach-Object { Remove-CACrlDistributionPoint -Uri $_.Uri -Force }`, `Add-CACrlDistributionPoint -Uri "http://pki.corp.internal/CertEnroll/<CAName><CRLNameSuffix>.crl" -AddToCertificateCdp -Force` sowie `Get-CAAuthorityInformationAccess | ForEach-Object { Remove-CAAuthorityInformationAccess -Uri $_.Uri -Force }` und `Add-CAAuthorityInformationAccess -Uri "http://pki.corp.internal/CertEnroll/<ServerDNSName>_<CaName><CertificateName>.crt" -AddToCertificateAia -Force` (alternativ in den CA-Eigenschaften, Registerkarte „Erweiterungen“). Starte danach den Dienst neu (`Restart-Service certsvc`). Die Änderung wirkt nur auf neu ausgestellte Zertifikate (Quelle: *PKI design considerations*), deshalb gehört sie vor die Ausstellung des SubCA-Zertifikats in Modul 4.
4. **CRL generieren und exportieren:** Veröffentliche die erste Basis-Sperrliste (`certutil -crl`). Die Dateien liegen in `C:\Windows\System32\CertSrv\CertEnroll`. Schließe `Transfer.vhdx` an `ROOTCA01` an und kopiere das Root-Zertifikat (`.crt`) und die CRL (`.crl`) darauf. Trenne die Festplatte danach wieder.

#### Kontrollfragen
1. Warum wird die Root-CA in der Praxis als "Offline"-CA betrieben?
2. Welcher Kommandozeilenbefehl wird genutzt, um die aktuelle CRL der CA manuell neu zu generieren?
3. Was geschieht, wenn ein Client ein Zertifikat überprüft, aber der definierte CDP-Pfad der Root-CA nicht erreichbar ist?

### Modul 4: Bereitstellung der ausstellenden Enterprise-CA
* **Priorität:** 1
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende eine Enterprise Issuing CA bereitstellen und an die Root-CA anbinden.
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikate ins Active Directory publizieren.
* **Voraussetzungen:** Modul 3, VM `SUBCA01`, VM `ROOTCA01`, VM `DC01`, `Transfer.vhdx`.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 4.1 | Veröffentlichung des Root-Zertifikats im Active Directory | 4 |
| 4.2 | Installation der Enterprise Subordinate CA | 4 |
| 4.3 | Anforderung, Signierung und Import des CA-Zertifikats | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **SubCA-Server und Webserver vorbereiten:** Nimm `SUBCA01` in die Domäne `corp.internal` auf und verschiebe das Computerkonto in die OU `PKI-Server`. Installiere IIS (`Install-WindowsFeature Web-Server -IncludeManagementTools`), lege den Ordner `C:\PKIData` an und erstelle in der Standardwebsite das virtuelle Verzeichnis `CertEnroll` mit dem physischen Pfad `C:\PKIData`. Prüfe von `DC01` aus mit `Test-NetConnection pki.corp.internal -Port 80`. Dieser HTTP-Pfad muss existieren, bevor die SubCA installiert wird, weil die Zertifikatskette der Root-CA schon bei der Installation über ihn geprüft wird.
2. **Root-Zertifikat verteilen:** Schließe `Transfer.vhdx` an `SUBCA01` an und kopiere `.crt` und `.crl` nach `C:\PKIData`. Veröffentliche das Root-Zertifikat auf `DC01` (mit Enterprise-Admin-Rechten) in den Configuration Naming Context: `certutil -f -dspublish <Pfad>\<Root-Zertifikat>.crt RootCA`. Die CRL muss nicht ins AD, weil für die Root-CA nur ein HTTP-CDP konfiguriert ist (Syntax der Veröffentlichung laut Microsoft Learn bestätigt). Führe auf `SUBCA01` `gpupdate /force` aus und prüfe mit `certutil -store root`, dass das Root-Zertifikat vertraut wird.
3. **SubCA installieren:** Installiere auf `SUBCA01` die AD-CS-Rolle (`Install-WindowsFeature ADCS-Cert-Authority -IncludeManagementTools`) als Enterprise Subordinate CA (Anmeldung mit Enterprise-Admin-Rechten), z. B. mit `Install-AdcsCertificationAuthority -CAType EnterpriseSubordinateCa -CACommonName "Corp-Issuing-CA" -CryptoProviderName "RSA#Microsoft Software Key Storage Provider" -KeyLength 4096 -HashAlgorithmName SHA256`. Der Assistent meldet, dass die Installation unvollständig ist, und legt den Zertifikatsrequest (`.req`) auf `C:\` ab. Kopiere ihn auf `Transfer.vhdx` und trenne die Festplatte.
4. **CA-Zertifikat signieren:** Schließe `Transfer.vhdx` an `ROOTCA01` an. Reiche den Request ein (`certreq -submit -config "ROOTCA01\Corp-Root-CA" <Request>.req`). Die Standalone-CA setzt ihn auf „Ausstehend“; stelle ihn in der CA-Konsole aus (Ausstehende Anforderungen > Ausstellen) oder mit `certutil -config "ROOTCA01\Corp-Root-CA" -resubmit <Anforderungs-ID>`. Rufe das Zertifikat ab (`certreq -retrieve -config "ROOTCA01\Corp-Root-CA" <Anforderungs-ID> SubCA.crt`), kopiere es auf die Festplatte und trenne sie. Schalte `ROOTCA01` anschließend aus.
5. **Installation abschließen:** Kopiere `SubCA.crt` nach `C:\PKIData` auf `SUBCA01` und schließe die Installation ab (`certutil -installcert C:\PKIData\SubCA.crt` oder in der CA-Konsole „CA-Zertifikat installieren“), danach `Start-Service certsvc`. Schlägt die Installation mit einem Sperrlistenfehler fehl, ist die Root-CRL nicht unter dem HTTP-Pfad erreichbar (siehe Kontrollfrage 3).
6. **CDP/AIA der Issuing-CA vor der Ausstellung festlegen:** Entferne die Standard-HTTP-Einträge mit dem Hostnamen `SUBCA01` und ergänze: Veröffentlichung nach `C:\PKIData\<CAName><CRLNameSuffix><DeltaCRLAllowed>.crl` (`-PublishToServer -PublishDeltaToServer`) sowie den Abrufpfad `http://pki.corp.internal/CertEnroll/<CAName><CRLNameSuffix><DeltaCRLAllowed>.crl` (`-AddToCertificateCdp -AddToFreshestCrl`) mit `Add-CACrlDistributionPoint`, und für die AIA `http://pki.corp.internal/CertEnroll/<ServerDNSName>_<CaName><CertificateName>.crt` (`Add-CAAuthorityInformationAccess -AddToCertificateAia`). Der LDAP-Eintrag kann bleiben. Starte `certsvc` neu, veröffentliche mit `certutil -crl`, kopiere das SubCA-Zertifikat (`.crt` aus `C:\Windows\System32\CertSrv\CertEnroll`) nach `C:\PKIData` und prüfe, dass `http://pki.corp.internal/CertEnroll/` Root- und SubCA-Dateien liefert. Die Einstellung wirkt nur für neue Zertifikate (Quelle: *PKI design considerations*).
7. **Prüfpunkt:** Erstelle Prüfpunkte `M4-PKI` für `DC01` und `SUBCA01` (nicht für `ROOTCA01`).

#### Kontrollfragen
1. Warum benötigt man bei der Installation der Enterprise-CA Enterprise-Admin-Rechte, bei der Standalone-CA jedoch nicht?
2. Was ist der Unterschied zwischen dem Configuration-Container und einem GPO, wenn es um die Verteilung von Root-Zertifikaten geht?
3. Welcher Fehler tritt häufig auf, wenn die Sperrliste der Root-CA beim Importieren des SubCA-Zertifikats abgelaufen oder nicht erreichbar ist?

### Modul 5: Verwaltung von Zertifikatvorlagen (Templates)
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikatvorlagen duplizieren und konfigurieren.
  * Nach Abschluss dieses Moduls kann der Lernende Berechtigungen (Enroll, Autoenroll) auf Vorlagen setzen.
* **Voraussetzungen:** Modul 4.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 5.1 | Aufbau und Funktion von Zertifikatvorlagen (V2, V3, V4) | 4 |
| 5.2 | Sicherheitseinstellungen und Ausstellungsvoraussetzungen | 6 |

#### Praxisaufgaben (Hands-on Lab)
1. **Template duplizieren:** Öffne auf `SUBCA01` die Konsole für Zertifikatvorlagen (`certtmpl.msc`). Dupliziere die Standardvorlage „Webserver“, wähle bei der Kompatibilität Windows Server 2012 R2 für die Zertifizierungsstelle und Windows 8.1/Server 2012 R2 für den Empfänger und benenne die Vorlage „Corp-Webserver-V1“ (Vorlagenname ohne Leerzeichen). Die Antragstellerangabe bleibt auf „Im Antrag angeben“ (Standard dieser Vorlage; siehe Modul 11).
2. **Sicherheit konfigurieren:** Ändere die Sicherheitseinstellungen so, dass die Gruppe `SG-WebAdmins` die Rechte „Lesen“ und „Registrieren“ besitzt. Gib zusätzlich dem Computerkonto `SUBCA01$` „Lesen“ und „Registrieren“ (Objekttyp „Computer“ auswählen), weil in Modul 8 der Computer selbst das Zertifikat anfordert.
3. **Template veröffentlichen:** Füge die neu erstellte Vorlage in der CA-Konsole unter „Zertifikatvorlagen“ hinzu (Neu > Auszustellende Zertifikatvorlage) und prüfe mit `certutil -CATemplates`, dass sie auftaucht.
4. **Autoenrollment-Recht setzen:** Dupliziere die Vorlage „Benutzer“ als „Corp-Benutzer-V1“. Deaktiviere im Reiter „Antragstellername“ die Optionen für die E-Mail-Adresse (der Benutzer `user1` hat kein Postfach-Attribut, die Anforderung würde sonst scheitern). Gib der Gruppe `SG-PKI-Users` „Lesen“, „Registrieren“ und „Automatisch registrieren“ und veröffentliche die Vorlage.

#### Kontrollfragen
1. Warum empfiehlt Microsoft, Standardvorlagen niemals direkt zu bearbeiten, sondern immer zu duplizieren?
2. Was ist der Unterschied zwischen Vorlagen der Version 2 und Version 3?
3. Welche AD-Partition speichert die Konfiguration der Zertifikatvorlagen?

### Modul 6: Zertifikatsausstellung und Autoenrollment
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikate manuell anfordern (MMC, certreq).
  * Nach Abschluss dieses Moduls kann der Lernende das Autoenrollment über Gruppenrichtlinien (GPO) konfigurieren.
* **Voraussetzungen:** Modul 5, VM `CL01`.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 6.1 | Manuelle Zertifikatsanforderung und MMC-Snap-ins | 4 |
| 6.2 | Konfiguration von Autoenrollment per GPO | 6 |

#### Praxisaufgaben (Hands-on Lab)
1. **CL01 vorbereiten:** Konfiguriere `CL01` mit der IP `192.168.60.50/24` und dem DNS-Server `192.168.60.10`, nimm sie in die Domäne `corp.internal` auf und verschiebe das Computerkonto in die OU `Clients`. Melde dich als `user1` an.
2. **Manuelle Anforderung:** Fordere als `user1` auf `CL01` mit `certmgr.msc` (Eigene Zertifikate > Alle Aufgaben > Neues Zertifikat anfordern) ein Zertifikat der Vorlage „Corp-Benutzer-V1“ an. Fordere ein zweites Zertifikat mit `certreq` an: Lege eine `request.inf` mit den Abschnitten `[NewRequest]` (`Subject = \"CN=user1\"`, `KeyLength = 2048`, `Exportable = FALSE`) und `[RequestAttributes]` (`CertificateTemplate = Corp-Benutzer-V1`) an, erzeuge den Request (`certreq -new request.inf request.req`), reiche ihn ein (`certreq -submit -config \"SUBCA01.corp.internal\Corp-Issuing-CA\" request.req`) und installiere die Antwort (`certreq -accept <Antwort>.cer`). Die genaue INF-Syntax ist nicht bestätigt und mit `certreq -?` zu prüfen.
3. **Autoenrollment-GPO:** Erstelle auf `DC01` ein GPO „PKI-AutoEnrollment“ und verknüpfe es mit der OU `Clients` (dort liegen `CL01` und `user1`). Aktiviere unter *Computerkonfiguration* und *Benutzerkonfiguration > Richtlinien > Windows-Einstellungen > Sicherheitseinstellungen > Richtlinien für öffentliche Schlüssel* die Richtlinie „Zertifikatdiensteclient – Automatische Registrierung“ (Aktiviert; Optionen „Abgelaufene Zertifikate erneuern, ausstehende Zertifikate aktualisieren und gesperrte Zertifikate entfernen“ und „Zertifikate, die Zertifikatvorlagen verwenden, aktualisieren“; Menünamen nicht bestätigt).
4. **Computer-Zertifikat automatisch verteilen:** Dupliziere die „Computer“-Vorlage als „Corp-Computer-V1“, gib der Gruppe „Domänencomputer“ „Lesen“, „Registrieren“ und „Automatisch registrieren“ und veröffentliche sie. Starte auf `CL01` `gpupdate /force` und `certutil -pulse` oder starte den Computer neu. Prüfe im Computerzertifikatsspeicher (`Get-ChildItem Cert:\LocalMachine\My`), ob das Zertifikat vollautomatisch bezogen wurde, und prüfe im Benutzerspeicher von `user1`, ob ein Benutzerzertifikat automatisch ausgestellt wurde.

#### Kontrollfragen
1. Welche zwei Voraussetzungen müssen auf der Zertifikatvorlage erfüllt sein, damit Autoenrollment funktioniert?
2. Wie kann ein Administrator auf dem Client das sofortige Beziehen von Autoenrollment-Zertifikaten erzwingen (Kommandozeile)?
3. Welche Gruppenrichtlinie schaltet das Autoenrollment ein, und welche Optionen dieser Richtlinie sorgen dafür, dass Zertifikate nach einer Änderung der Vorlage erneuert werden?

### Modul 7: Sperrlisten (CRL) und Online Responder (OCSP)
* **Priorität:** 1
* **Zeitaufwand:** 12 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende einen Webserver für die Verteilung von CRLs bereitstellen und für Delta-CRLs konfigurieren (Hochverfügbarkeit ist im Labor mit einem Server nicht abbildbar).
  * Nach Abschluss dieses Moduls kann der Lernende den Online Responder (OCSP) installieren und einrichten.
* **Voraussetzungen:** Modul 4 (IIS mit `CertEnroll`) und Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 7.1 | CRL-Architektur, Base-CRL und Delta-CRL | 4 |
| 7.2 | Implementierung eines OCSP-Responders (RFC 6960) | 8 |

#### Praxisaufgaben (Hands-on Lab)
1. **CRL-Laufzeiten und Delta-CRL:** Setze auf `SUBCA01` die Basis-CRL auf 1 Woche und die Delta-CRL auf 1 Tag (`certutil -setreg CA\CRLPeriodUnits 1`, `certutil -setreg CA\CRLPeriod "Weeks"`, `certutil -setreg CA\CRLDeltaPeriodUnits 1`, `certutil -setreg CA\CRLDeltaPeriod "Days"`), starte `certsvc` neu und veröffentliche (`certutil -crl`). Erlaube im IIS „Double Escaping“ (`%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -section:system.webServer/security/requestFiltering -allowDoubleEscaping:true`), weil der Name der Delta-CRL ein `+` enthält. Rufe von `CL01` im Browser `http://pki.corp.internal/CertEnroll/` auf und lade die Basis- und die Delta-CRL herunter (Dateiname der Delta-CRL mit `+`).
2. **Sperren und Veröffentlichen:** Sperre auf `SUBCA01` in der CA-Konsole das in Modul 6 ausgestellte Benutzerzertifikat mit dem Grund „Zertifikat angehalten“ (Certificate Hold), veröffentliche die CRLs und prüfe auf `CL01` mit `certutil -verify -urlfetch <Zertifikat>.cer`, dass der Status „gesperrt“ erkannt wird. Hebe die Sperre danach wieder auf (Zertifikat freigeben) und veröffentliche erneut.
3. **OCSP Installation:** Installiere auf `SUBCA01` die Rolle „Online Responder“ (`Install-WindowsFeature ADCS-Online-Cert -IncludeManagementTools`, `Install-AdcsOnlineResponder`). Füge in den CA-Eigenschaften auf der Registerkarte „Erweiterungen“ unter „Zugriff auf Stelleninformationen (AIA)“ die URL `http://pki.corp.internal/ocsp` hinzu, aktiviere nur „In die Erweiterung des Online Certificate Status Protocol (OCSP) einbeziehen“ und deaktiviere für diesen Eintrag „In die AIA-Erweiterung ausgestellter Zertifikate einbeziehen“ (Quelle: *Configure AIA issuer retrieval*). Ohne diesen Schritt enthält kein Zertifikat einen OCSP-Verweis; er wirkt nur für neu ausgestellte Zertifikate. Starte `certsvc` neu.
4. **OCSP-Template und Sperrkonfiguration:** Veröffentliche die Vorlage „OCSP Response Signing“ auf der CA, gib dem Computerkonto `SUBCA01$` „Lesen“, „Registrieren“ und „Automatisch registrieren“ und lege in der Online-Responder-Verwaltung eine Sperrkonfiguration für die Issuing-CA an (CA-Zertifikat aus dem AD wählen, Signaturzertifikat automatisch registrieren). Verifiziere, dass der Responder ein Signaturzertifikat bezieht und der Status „Funktioniert“ (grünes Symbol) angezeigt wird (Bezeichnung nicht bestätigt).
5. **OCSP prüfen:** Fordere als `user1` auf `CL01` ein neues Zertifikat der Vorlage „Corp-Benutzer-V1“ an (das neue Zertifikat enthält jetzt den OCSP-Verweis), exportiere es als `.cer` und prüfe mit `certutil -url <Zertifikat>.cer` (URL-Abruf-Werkzeug), dass der CDP-Abruf und die OCSP-Abfrage erfolgreich sind.

#### Kontrollfragen
1. Welchen signifikanten Vorteil bietet OCSP im Vergleich zu herkömmlichen Sperrlisten bei großen Umgebungen?
2. Warum müssen IIS-Webserver, die Delta-CRLs hosten, für "Double Escaping" konfiguriert werden?
3. Welche Lebensdauer hat eine typische Base-CRL im Vergleich zu einer Delta-CRL?
4. Worin unterscheidet sich „Zertifikat angehalten“ (Certificate Hold) von einer endgültigen Sperrung, und warum wird die Aufhebung in der CRL nicht sofort sichtbar?

### Modul 8: Zertifikate für Webserver und Clients
* **Priorität:** 1
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende SAN-Zertifikate für interne Webserver ausstellen und binden.
  * Nach Abschluss dieses Moduls kann der Lernende Zertifikate für Client-Authentifizierung nutzen.
* **Voraussetzungen:** Modul 7.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 8.1 | Erstellung und Nutzung von Webserver-Zertifikaten (SAN) | 5 |
| 8.2 | TLS-Implementierung im IIS | 5 |

#### Praxisaufgaben (Hands-on Lab)
1. **SAN-Zertifikat anfordern:** Beantrage auf `SUBCA01` über die MMC (Zertifikate, Lokaler Computer > Eigene Zertifikate > Neues Zertifikat anfordern, Active-Directory-Registrierungsrichtlinie) ein Zertifikat der Vorlage „Corp-Webserver-V1“. Trage in den Eigenschaften den gemeinsamen Namen `pki.corp.internal` und als alternative Namen (DNS) `pki.corp.internal`, `www.corp.internal` und `subca01.corp.internal` ein. Die Anforderung läuft über das Computerkonto `SUBCA01$`, dem in Modul 5 das Recht „Registrieren“ gegeben wurde.
2. **TLS-Bindung:** Binde das erhaltene Zertifikat im IIS-Manager an die Standardwebsite (HTTPS, Port 443).
3. **Client-Überprüfung:** Rufe von `CL01` aus über den Browser (Edge/Chrome) `https://pki.corp.internal` und `https://www.corp.internal` auf. Überprüfe, dass keine Zertifikatswarnung erscheint, da die Zertifikatskette über das AD vertrauenswürdig ist, und kontrolliere in den Zertifikatdetails die Einträge für CDP, AIA und OCSP.
4. **Client-Authentifizierung:** Setze im IIS unter „SSL-Einstellungen“ der Standardwebsite „Clientzertifikate“ auf „Erforderlich“. Rufe die Seite von `CL01` auf und wähle das Benutzerzertifikat von `user1` (Vorlage „Corp-Benutzer-V1“ enthält die Verwendung „Clientauthentifizierung“). Stelle danach „Clientzertifikate“ wieder auf „Ignorieren“. Das Browserverhalten ist nicht bestätigt.

#### Kontrollfragen
1. Warum reicht ein Zertifikat, das nur den NetBIOS-Namen im "Subject" hat, für moderne Webbrowser nicht mehr aus?
2. Was passiert, wenn ein Webserver-Zertifikat auf "Serverauthentifizierung" beschränkt ist, aber für eine Client-VPN-Einwahl verwendet werden soll?
3. Wie prüft der Client-Browser den Sperrstatus des IIS-Zertifikats?

### Modul 9: Zertifikatsbasierte Authentifizierung (802.1X / NPS)
* **Priorität:** 2
* **Zeitaufwand:** 10 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die Grundlagen von 802.1X mit EAP-TLS erläutern.
  * Nach Abschluss dieses Moduls kann der Lernende einen Network Policy Server (NPS) für zertifikatsbasierte Prüfungen konfigurieren.
* **Voraussetzungen:** Modul 6 (Autoenrollment Computer-Zertifikate) und Modul 8 (Serverzertifikat auf `SUBCA01`).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 9.1 | 802.1X-Konzepte und EAP-TLS Authentifizierung | 4 |
| 9.2 | NPS-Rolle (RADIUS) und Netzwerkrichtlinien konfigurieren | 6 |

#### Praxisaufgaben (Hands-on Lab)
1. **NPS-Installation:** Installiere die Rolle „Network Policy and Access Services“ (NPS) auf `SUBCA01` (`Install-WindowsFeature NPAS -IncludeManagementTools`). Das ist eine Laborvereinfachung; ein NPS gehört in der Praxis nicht auf eine CA.
2. **RADIUS-Konfiguration:** Registriere den NPS im Active Directory. Lege einen RADIUS-Client „Switch-Lab“ mit einer fiktiven IP (z. B. `192.168.60.99`) und einem gemeinsamen Geheimnis an. Erstelle eine Netzwerkrichtlinie, die den Zugriff nur für die Gruppe „Domänencomputer“ erlaubt und als Authentifizierungsmethode ausschließlich „Microsoft: Smartcard oder anderes Zertifikat“ (EAP-TLS) zulässt.
3. **Zertifikatsbindung:** Wähle in den EAP-TLS-Eigenschaften das in Modul 8 ausgestellte Serverzertifikat von `SUBCA01` aus (Verwendung „Serverauthentifizierung“).
4. **Konfigurationsprüfung:** Im Labor gibt es keinen Switch und keinen 802.1X-Supplicant, ein Ende-zu-Ende-Test ist daher nicht möglich und wird auch nicht simuliert; im NPS-Protokoll entstehen nur Einträge, wenn Anfragen eintreffen. Prüfe die Konfiguration in der NPS-Konsole, exportiere sie (`netsh nps export filename=C:\nps.xml exportPSK=NO`, Syntax nicht bestätigt) und beschreibe schriftlich, welche Prüfschritte in der Praxis am Switch folgen würden.
5. **Fallstudie 802.1X:** Zeichne den Ablauf einer 802.1X-Anmeldung mit EAP-TLS (Supplicant, Authenticator, RADIUS-Server, Zertifikatsprüfung beider Seiten).

#### Kontrollfragen
1. Warum gilt EAP-TLS im Vergleich zu PEAP-MSCHAPv2 als sicherer?
2. Welche Art von Zertifikat benötigt der NPS-Server zwingend für die EAP-TLS-Kommunikation?
3. Welche Rolle spielt das Computerzertifikat des Clients bei der 802.1X-Authentifizierung vor der Benutzeranmeldung?

### Modul 10: Sicherung, Wiederherstellung und Migrationskonzept der CA
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende die CA-Datenbank und die privaten Schlüssel sichern.
  * Nach Abschluss dieses Moduls kann der Lernende eine CA aus einem Backup wiederherstellen.
* **Voraussetzungen:** Modul 4 (die Aufgaben 1 bis 4 arbeiten auf `SUBCA01`, Aufgabe 5 auf `ROOTCA01`). Erstelle vorab Prüfpunkte von `SUBCA01` und `DC01`.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 10.1 | Backup-Strategien für Root- und Issuing-CAs | 4 |
| 10.2 | Wiederherstellung und Disaster Recovery der CA | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Backup durchführen:** Sichere in der Zertifizierungsstellen-Konsole auf `SUBCA01` (Alle Aufgaben > CA sichern) den privaten Schlüssel und das CA-Zertifikat sowie die Zertifikatdatenbank und das Datenbankprotokoll in den leeren Ordner `C:\CABackup` und vergib ein Kennwort für die Schlüsseldatei. Alternativ: `certutil -backupdb C:\CABackup` und `certutil -backupkey C:\CABackup` (Quelle: *Migrate a Certification Authority*). Die Schlüsseldatei (`.p12`) und ihr Kennwort sind hochsensibel.
2. **Registry und Vorlagenliste sichern:** Exportiere den Registrierungsschlüssel `HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration` (`reg export \"HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration\" C:\CABackup\CertSvcConfig.reg`) und speichere die Liste der veröffentlichten Vorlagen (`certutil -CATemplates > C:\CABackup\Vorlagen.txt`), denn die Vorlagenzuordnung der CA ist Teil des Backups, das nicht automatisch erfolgt.
3. **Disaster Recovery (Simulation):** Es dürfen zwischen Backup und Wiederherstellung keine Zertifikate ausgestellt werden, sie gingen verloren. Stoppe den Dienst `certsvc`. Kopiere die `.edb`-Datei der Datenbank (Standardpfad `C:\Windows\System32\CertLog`, Pfad in der Registry unter `DBDirectory` prüfen) an einen sicheren Ort und lösche sie. Der Start des Dienstes scheitert nun. Stelle die Datenbank aus dem Backup wieder her (Konsole „CA wiederherstellen“ oder `net stop certsvc`, `certutil -f -restoredb C:\CABackup`) und starte den Dienst. Prüfe die Wiederherstellung mit `certutil -ping`, `certutil -CAInfo` und der Liste der ausgestellten Zertifikate. Bei Fehlern stellst du den Prüfpunkt wieder her.
4. **Migrationskonzept (schriftlich):** Beschreibe auf einer Seite die Schritte einer Migration der Issuing-CA auf einen neuen Server nach *Migrate a Certification Authority* (Sicherung von Datenbank, Schlüssel, Registry, CAPolicy.inf und Vorlagenliste; CRL mit verlängerter Gültigkeit veröffentlichen; Rolle entfernen; Rolle auf dem Zielserver mit dem vorhandenen Schlüssel installieren; Datenbank und Registry wiederherstellen; Vorlagen neu zuordnen). Die Migration wird im Labor nicht ausgeführt, weil kein zweiter Server vorgesehen ist.
5. **Root-CA sichern:** Starte `ROOTCA01` kurz, schließe `Transfer.vhdx` an und sichere Schlüssel, Zertifikat und Datenbank (`certutil -backupdb T:\RootBackup`, `certutil -backupkey T:\RootBackup`). Bewahre die Festplatte getrennt auf und schalte `ROOTCA01` wieder aus.

#### Kontrollfragen
1. Welche beiden Hauptkomponenten müssen bei einem CA-Backup zwingend gesichert werden?
2. Warum ist die Sicherung des genannten Registry-Schlüssels bei einer Migration auf einen neuen Server essenziell?
3. Was ist der Unterschied zwischen einem Backup über die MMC und einem Backup auf VM-Ebene (Snapshot)?

### Modul 11: Sicherheit, Fehlkonfigurationen und Best Practices
* **Priorität:** 1
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende typische AD CS-Fehlkonfigurationen (z. B. ESC1-Szenarien) erkennen.
  * Nach Abschluss dieses Moduls kann der Lernende Best Practices zur Absicherung der PKI anwenden.
* **Voraussetzungen:** Modul 5, Modul 6.

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 11.1 | AD CS Angriffsvektoren (Fokus auf Templates und SANs) | 4 |
| 11.2 | Härtung der Zertifizierungsstelle | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **Risiko-Vorlage erstellen (nicht veröffentlichen):** Dupliziere die Vorlage „Webserver“ als „Corp-Risk-Web“, füge zur erweiterten Schlüsselverwendung „Clientauthentifizierung“ hinzu, gib „Domänen-Benutzern“ das Recht „Registrieren“, belasse „Im Antrag angeben“ (`CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT`) und lasse die Genehmigung durch einen Zertifikatmanager ausgeschaltet. **Veröffentliche die Vorlage nicht auf der CA.** Das Szenario wird nur analysiert, ein Angriff wird nicht durchgespielt.
2. **Audit & Analyse:** Prüfe die Vorlage im Reiter „Antragstellername“ und im Attribut `msPKI-Certificate-Name-Flag` in ADSI-Edit (Configuration > Services > Public Key Services > Certificate Templates; Bit für `ENROLLEE_SUPPLIES_SUBJECT`). Analysiere schriftlich, warum die Kombination aus Registrierungsrecht für Niedrigprivilegierte, vom Antragsteller bestimmten Namen, einer Clientauthentifizierungs-Verwendung und fehlender Genehmigung das Szenario ESC1 ermöglicht (Quelle: *Certified Pre-Owned*), und bewerte, ob `Corp-Webserver-V1` aus Modul 5 dieses Muster erfüllt (Registrierungsrecht, EKU).
3. **Härtung:** Lösche die Vorlage „Corp-Risk-Web“ wieder. Aktiviere in den CA-Eigenschaften (Registerkarte „Überwachung“) die Ereignisse und aktiviere auf `SUBCA01` die erweiterte Überwachung „Zertifikatdienste“ (z. B. per GPO „PKI-Audit“, verknüpft mit der OU `PKI-Server`, oder lokal mit `auditpol /set /subcategory:\"Certification Services\" /success:enable /failure:enable`). Fordere ein Testzertifikat an und finde die Anforderung im Sicherheitsprotokoll (Ereignis-IDs 4886/4887, nicht bestätigt).
4. **Root-CA offline nehmen:** Schalte `ROOTCA01` aus (falls noch an), notiere das Ablaufdatum der Root-CRL (Basis-CRL: 26 Wochen) und beschreibe den Ablauf zur CRL-Erneuerung (Start, `certutil -crl`, Kopieren auf `Transfer.vhdx`, Veröffentlichung im Verzeichnis `C:\PKIData`). Prüfe von `CL01` aus mit `certutil -verify -urlfetch`, dass die Kette trotz ausgeschalteter Root-CA vollständig geprüft wird. Prüfe außerdem auf der Registerkarte „Sicherheit“ der Issuing-CA, wer die CA verwalten und wer Zertifikate verwalten darf.

#### Kontrollfragen
1. Was bedeutet die Schwachstelle "ESC1" im Kontext von Zertifikatvorlagen?
2. Warum sollten Root-CAs nach dem Signieren der Sub-CA zwingend heruntergefahren ("Offline" genommen) werden?
3. Welchen Zweck erfüllt die Funktion "Ausstellungsvoraussetzungen" (Issuance Requirements) mit CA-Zertifikatmanager-Genehmigung bei hochsensiblen Vorlagen?

### Modul 12: Troubleshooting und Diagnosewerkzeuge
* **Priorität:** 2
* **Zeitaufwand:** 8 UE
* **Überprüfbare Lernziele:**
  * Nach Abschluss dieses Moduls kann der Lernende PKI-Strukturen auf Fehler prüfen.
  * Nach Abschluss dieses Moduls kann der Lernende `certutil` zur Fehlerbehebung von Ketten- und Sperrproblemen einsetzen.
* **Voraussetzungen:** Modul 7 und Modul 8 (IIS mit CDP und HTTPS-Webzertifikat auf `SUBCA01`).

#### Tabelle „Lerneinheiten laut Lehrplan“
| Einheit | Inhalt | Stunden |
| :--- | :--- | :--- |
| 12.1 | Nutzung von PKIView.msc und Ereignisanzeige | 4 |
| 12.2 | CLI-Troubleshooting mit Certutil | 4 |

#### Praxisaufgaben (Hands-on Lab)
1. **PKI-Gesundheitscheck:** Öffne auf `SUBCA01` das Tool Enterprise PKI (`pkiview.msc`). Überprüfe den Status des AIA- und CDP-Pfades beider Zertifizierungsstellen und notiere Auffälligkeiten.
2. **Testzertifikat bereitstellen:** Exportiere das Webserver-Zertifikat aus Modul 8 (ohne privaten Schlüssel) als `web.cer` nach `C:\PKIData` auf `SUBCA01` und lade es auf `CL01` herunter (`http://pki.corp.internal/CertEnroll/web.cer`) nach `C:\Temp\web.cer`.
3. **CRL-Fehler simulieren:** Lösche auf `CL01` den URL-Cache (`certutil -urlcache * delete`) und setze den Cache-Zeitpunkt zurück (`certutil -setreg chain\ChainCacheResyncFiletime @now`, in einer Administrator-Konsole). Stoppe danach den IIS-Webserver aus Modul 4/7 temporär (`Stop-Service W3SVC`). Beachte: Auch der Online Responder läuft über IIS, fällt also ebenfalls aus. Ohne das Löschen des Caches könnten zwischengespeicherte Sperrinformationen den Ausfall verbergen.
4. **Verifizierung:** Führe auf `CL01` `certutil -verify -urlfetch C:\Temp\web.cer` aus und analysiere die Fehler im Output (fehlgeschlagener CRL- und OCSP-Abruf, erwartet u. a. ein Fehler zu `Revocation Offline`, Code nicht bestätigt). Starte IIS wieder (`Start-Service W3SVC`), lösche den Cache erneut und prüfe, ob der Befehl erfolgreich durchläuft. Werte zusätzlich das Protokoll *Microsoft-Windows-CAPI2/Operational* aus (muss ggf. aktiviert werden).

#### Kontrollfragen
1. Welches graphische Standard-Tool in Windows Server bietet den schnellsten Überblick über die Erreichbarkeit aller Sperrlisten in der PKI?
2. Mit welchem `certutil`-Parameter lässt sich der Zertifikatscache auf einem Client leeren, um den erneuten Download einer Sperrliste zu erzwingen?
3. Worauf deutet die Fehlermeldung `CERT_E_REVOCATION_FAILURE` auf einem Client hin?
4. Warum können zwischengespeicherte CRLs oder OCSP-Antworten einen Ausfall des Webservers verbergen, und wie lässt sich der Effekt beim Testen vermeiden?

---

## C. Änderungsvermerk (Korrektur der ersten Gem-Fassung, 08.11.2026)

Die erste Fassung wurde geprüft und an den folgenden Stellen geändert. Stundensummen (116 UE), Prioritäten (10x P1, 2x P2) und Modulreihenfolge blieben unverändert. Mehrere Module enthalten nun mehr Aufgaben; der Zeitrahmen ist im Labor nicht erprobt (besonders Modul 4 und 7).

| Stelle | Änderung | Grund |
| :--- | :--- | :--- |
| Kopf, A.2 | Vorkenntnisse (DNS, GPO, PowerShell); Out-of-Scope präzisiert; Zeitaufwand mit „UE“; Quellen zu CAPolicy.inf, CDP/AIA, Migration, certutil, OCSP und ESC1 ergänzt; „Securing PKI“ als nicht geprüft markiert | Fachliche Aussagen hatten keine Quelle (ESC1, Migration), Einheit „UE“ fehlte |
| A.3 | IP-Plan, Windows Server 2022, `ROOTCA01` ohne Netzwerk und ab Modul 2, `Transfer.vhdx`, DNS-Alias, Prüfpunkte, Domänenbeitritte | Aufgaben in Modul 2 nutzen `ROOTCA01`, obwohl „ab Modul 3“ galt; Datenaustausch mit einer Offline-Root war nicht geregelt; Namen und Adressen fehlten |
| Modul 1 | Kontrollfragen 4 und 5 | Lernziele (Standalone vs. Enterprise, RA und Schlüssel) hatten keine Frage |
| Modul 2 | OUs, Benutzer, Gruppen, DNS-Einträge; CAPolicy.inf mit konkreten Werten; Transfermedium | `SG-WebAdmins`, Client-OU und Benutzer wurden später gebraucht, aber nie angelegt; der Alias `pki.corp.internal` existierte nirgends |
| Modul 3 | Konkrete Installation, Laufzeiten, CDP/AIA per Befehl, CRL-Export auf Transfermedium | Die Standardlaufzeit (1 Jahr) hätte das SubCA-Zertifikat nach einem Jahr ablaufen lassen, die CRL der Root-CA nach 1 Woche |
| Modul 4 | Neue Reihenfolge: IIS und CertEnroll vor der Installation, Domänenbeitritt und OU, `certreq`-Ablauf mit Ausstehend-Status, Installation des Zertifikats, CDP/AIA der Issuing-CA, Prüfpunkt | Der HTTP-Webserver (CDP) entstand erst in Modul 7, wurde aber bei der SubCA-Installation gebraucht; die CDP/AIA der Issuing-CA wurden nie konfiguriert; die Standalone-Root stellt Anträge nicht automatisch aus |
| Modul 5 | Vorlagen-Kompatibilität, Recht für `SUBCA01$`, Veröffentlichungsprüfung, neue Aufgabe mit Recht „Automatisch registrieren“ | Das Lernziel Autoenrollment-Recht wurde nicht geübt; in Modul 8 hätte der Computer keine Berechtigung gehabt |
| Modul 6 | Vorbereitung `CL01`, `certreq`-Anforderung, GPO an der OU `Clients`, Benutzer in dieser OU, Kontrollfrage 3 ersetzt | Lernziel `certreq` ohne Aufgabe; keine Client-OU; die Rolle des Dienstes „Certificate Propagation“ beim Autoenrollment ist nicht belegt |
| Modul 7 | Lernziel „hochverfügbar“ ersetzt; IIS-Teil aus Modul 4; CRL-Laufzeiten, Sperren, OCSP-Erweiterung in der AIA der CA, OCSP-Prüfung, Kontrollfrage 4 | Ohne OCSP-URL in der AIA nutzt kein Zertifikat den Responder; Base-/Delta-CRL und Sperren wurden nie geübt; ein einzelner Server ist nicht hochverfügbar |
| Modul 8 | Antrag über das Computerkonto, Zertifikatdetails, Aufgabe zur Clientauthentifizierung | Lernziel Clientauthentifizierung ohne Aufgabe; `www.corp.internal` hatte keinen DNS-Eintrag |
| Modul 9 | Voraussetzung Modul 8; RADIUS-Client; Konfigurationsprüfung statt Simulation; Fallstudie | Es gibt keinen Switch und keinen Supplicant, ein NPS-Protokoll entsteht ohne Anfragen nicht; Zertifikat stammte nur aus Modul 8 |
| Modul 10 | Titel auf „Migrationskonzept“; Registry und Vorlagenliste; Restore mit `certutil -restoredb`; Warnung vor Ausstellung zwischen Backup und Restore; schriftliche Migration; Root-Backup | Migration kam im Titel vor, aber nicht in den Aufgaben; ein Restore kann die Datenbank auf einen älteren Stand zurücksetzen |
| Modul 11 | Vorlage nicht veröffentlicht; ESC1-Voraussetzungen konkret (Registrierungsrecht statt Autoenrollment); Bewertung von `Corp-Webserver-V1`; Überwachung mit Audit-Kategorie; Root-Offline-Prozess und CA-Rollen | Autoenrollment funktioniert nicht mit Vorlagen mit „Im Antrag angeben“, das Szenario war so falsch beschrieben; es gab ein Risiko-Template im produktiven CA-Bestand; das Gem-Lernziel „Härtung“ ist jetzt prüfbar |
| Modul 12 | Testzertifikat, Cache leeren, IIS beendet auch OCSP, Kontrollfrage 4 | Ein Befehl mit `<PfadZumWebZertifikat>` ohne Datei; zwischengespeicherte CRLs hätten den Fehler nicht gezeigt |

**Bewertung des Prüfvermerks der ersten Fassung:** Punkt 1 ist korrekt (116 UE, 10x P1, 2x P2). Punkt 2 ist teilweise erfüllt (Zuordnung der VMs nicht widerspruchsfrei). Punkt 3 ist teilweise erfüllt: Die RFCs sind belegt, aber mehrere Microsoft-Seiten sind „Stand nicht geprüft“, ESC1 hatte keine Quelle. Punkt 4 ist nicht erfüllt (siehe Moduländerungen: IIS zu spät, SubCA-CDP/AIA fehlt, Autoenrollment mit „Im Antrag angeben“). Punkt 5 ist nicht erfüllt (Autoenrollment-Rechte, `certreq`, Clientauthentifizierung, Migration, Hochverfügbarkeit). Punkt 6 ist teilweise erfüllt (isoliert, aber die Offline-Root war nicht wirklich offline). Punkt 7 ist nicht erfüllt: Namen, Konten, DNS-Einträge und Transfermedium fehlten.

**Hinweise und offene Punkte:**

* Alle neuen Befehle und Einstellungen wurden gegen Microsoft Learn und den Wissensstand geprüft, **nicht im Labor ausgeführt**.
* **Nicht bestätigt, vor Kursstart zu klären:** Parameter und Platzhalter der Cmdlets `Install-AdcsCertificationAuthority` und `Add-CACrlDistributionPoint`/`Add-CAAuthorityInformationAccess`; INF-Syntax für `certreq -new`; Menü- und Gruppenrichtliniennamen in der deutschen Oberfläche; Dateinamen der CRL- und CRT-Dateien (`<ServerDNSName>_<CaName>`); `certutil -pulse` als Auslöser für die Verteilung des Root-Zertifikats; Bezeichnung des Status im Online Responder; Ereignis-IDs 4886/4887; Syntax von `netsh nps export`; Fehlercode bei Ausfall des Sperrstatus; Browserverhalten bei erforderlichem Clientzertifikat; Jahr und URL des SpecterOps-Papers.
* Das Labor hat eine einzige Issuing-CA, die zugleich Webserver, Online Responder und NPS ist. Das ist eine Laborvereinfachung und nicht als Produktivdesign gedacht. Eine echte Hochverfügbarkeit der CRL-Verteilung ist im Labor nicht abbildbar.
* Die Aufgaben zum Sichern und Zurückspielen der CA-Datenbank (Modul 10) können Zertifikate verlieren, wenn zwischen Backup und Wiederherstellung ausgestellt wird. Das ist im Text vermerkt; Prüfpunkte sind vorgesehen.