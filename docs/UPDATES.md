# Actualizări LumaShot

Versiunea sursei din acest repository este **5.0.1**.
Încărcarea sursei nu publică automat un installer sau un update.

## Repository și verificarea actualizărilor

LumaShot.py conține APP_VERSION și adresa publică TOKKAB1/LumaShot.
Aplicația citește API-ul GitHub Releases. Nu este necesar un update.json,
latest.json sau alt manifest. Acest ghid nu este un manifest.
Verificarea se face la cerere sau la pornire dacă utilizatorul o activează;
verificarea automată este inițial oprită.

## Publicarea unei versiuni noi, când alegi să o distribui

1. Schimbă APP_VERSION o singură dată în LumaShot.py și actualizează sursele.
2. Rulează BUILD_LUMASHOT.bat pentru noul EXE, apoi construiește installerul
   cu proiectul Inno Setup separat. Versiunea installerului trebuie să fie
   identică cu cea a aplicației. Păstrează AppId pentru actualizări.
3. Pentru versiunea curentă, creează un Release stabil cu tagul **v5.0.1**,
   pe commitul care conține sursa 5.0.1.
4. Atașează **LumaShot-Setup-5.0.1-Windows-x64.exe**, sau
   **LumaShot-Setup-5.0.1-Windows-x64.zip** care conține acel installer.
   Nu folosi un executabil portabil redenumit sau ZIP-ul repository-ului.
5. Publică Release-ul ca Latest, fără Pre-release și fără a-l lăsa Draft.

Pentru o versiune viitoare 5.0.2, folosește APP_VERSION 5.0.2, installerul
LumaShot-Setup-5.0.2-Windows-x64.exe și tagul v5.0.2.
O versiune instalată detectează doar o versiune strict mai mare.

## Cum descarcă aplicația

- Se ia cel mai recent Release stabil din TOKKAB1/LumaShot.
- Pentru taguri complete vX.Y.Z, versiunea din numele installerului trebuie
  să corespundă. Tagurile vechi scurte v4/v5 sunt interpretate folosind
  versiunea reală din numele installerului.
- GitHub furnizează suma SHA-256; aplicația verifică descărcarea înainte
  de folosirea installerului. Nu ai nevoie de un fișier SHA separat.
- Descărcarea și pornirea installerului interactiv se fac numai la alegerea
  utilizatorului, după încheierea capturilor și filmărilor/ciornelor.
- Capturile, textul OCR și setările personale nu sunt trimise la GitHub.
- Se actualizează aplicația Windows instalată. Fișierul Python nu este
  rescris automat; sursa Python se descarcă separat.

Versiunile vechi fără updater necesită prima instalare manuală a v5.
