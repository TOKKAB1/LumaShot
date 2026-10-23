# Actualizări LumaShot v5

Versiunea curentă a aplicației și installerului este **5.0.0**, numită **v5**.
Numărul apare în aplicație și în proprietățile executabilului.

## Ce trebuie în repository

Codul LumaShot.py conține APP_VERSION = "5.0.0" și adresa publică a repository-ului.
Păstrează acest ghid împreună cu README-ul. **Nu este necesar un update.json,
latest.json sau alt manifest**: v5 citește direct API-ul GitHub Releases.
Acest ghid explică procesul; aplicația nu îl folosește ca manifest.

Încărcarea sursei în repository nu publică singură o actualizare pentru EXE.

## Cum publici versiunea v5

1. Actualizează fișierele din repository cu acest pachet.
2. Când decizi să distribui installerul, creează separat un Release stabil cu
   tagul **v5** și titlul **LumaShot v5**.
3. Atașează **LumaShot-Setup-5.0.0-Windows-x64.exe**, sau
   **LumaShot-Setup-5.0.0-Windows-x64.zip**, care conține acel EXE.
   Folosește installerul, nu executabilul portabil redenumit.
4. Adaugă modificările importante și publică Release-ul fără Draft/Pre-release.
   GitHub furnizează suma SHA-256 a fișierului; v5 o verifică la descărcare.

Pentru o versiune viitoare v6, crește APP_VERSION la **6.0.0**, reconstruiește
programul și installerul cu aceeași versiune și folosește tagul **v6**.
Numele installerului va fi **LumaShot-Setup-6.0.0-Windows-x64.exe** sau ZIP-ul
cu același nume. Pentru o corecție v5.0.1, folosește APP_VERSION 5.0.1 și
installerul 5.0.1. Păstrează AppId-ul Inno Setup pentru actualizările instalării.

## Cum verifică aplicația

- Se folosesc doar Release-uri stabile din TOKKAB1/LumaShot.
- Tagurile scurte v4/v5/v6 sunt acceptate: versiunea completă se citește din
  numele installerului. Astfel v4 cu installerul 0.4.0 nu este confundat cu 4.0.
- Pentru taguri complete vX.Y.Z, versiunea installerului trebuie să corespundă.
- Verificarea la pornire este opțională și inițial oprită.
- Utilizatorul alege descărcarea, apoi pornirea installerului interactiv.
- Capturile, textul OCR și setările personale nu sunt trimise la GitHub.
- Capturile/filmările și ciornele trebuie încheiate înainte de instalare.
- Funcția actualizează aplicația Windows instalată. Sursa Python se descarcă
  separat; nu este rescrisă automat.

Versiunile anterioare fără updater, precum 0.4.0, necesită prima instalare
manuală a v5. După aceea pot verifica versiunile viitoare din aplicație.
