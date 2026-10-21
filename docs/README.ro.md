# LumaShot

**O captură. Exact cum o vrei.**

[English](../README.md) · **Română** · [Русский](README.ru.md)

Aplicație pentru Windows, scrisă în Python + PySide6. Selectezi o zonă, adaugi explicații și copiezi sau salvezi imaginea. Interfața este disponibilă în **română, rusă și engleză**, iar limba aleasă se păstrează.

![Interfața LumaShot în română](../assets/interface-ro.png)

## Pornire

Ai nevoie de Windows, Python 3.10 sau mai nou și PySide6. Descarcă [LumaShot.py](https://github.com/TOKKAB1/LumaShot/raw/refs/heads/main/LumaShot.py) și rulează din dosarul său:

```powershell
python -m pip install PySide6==6.12.0
python LumaShot.py
```

Aplicația este într-un singur fișier Python. Nu există încă o versiune `.exe`. Fișierul [LumaShot.ico](../LumaShot.ico) este opțional și poate fi folosit pentru pictograma unei scurtături Windows.

## Utilizare

Apasă **Selectează o zonă**, **Print Screen** sau **Ctrl+Shift+F9**. Trasează zona dorită și folosește bara de instrumente care apare lângă selecție.

| Tastă | Funcție |
|---|---|
| `V` | Mutarea selecției și redimensionarea din colțuri |
| `P`, `L`, `A` | Creion, linie, săgeată |
| `R` | Dreptunghi |
| `T` | Text; Enter îl confirmă |
| `H`, `N` | Evidențiere, număr de pas |
| `Ctrl+Z`, `Ctrl+Y` | Anulează, refă adnotarea |
| `Ctrl+C` sau `Enter` | Copiază imaginea |
| `Ctrl+S` | Salvează în PNG sau JPEG |
| `Esc` sau clic dreapta | Anulează captura |

În timpul introducerii textului, Esc renunță mai întâi la acel text. Adnotările rămân ancorate la ecran atunci când muți selecția.

Poți alege dosarul de salvare și scurtătura din filele **General** și **Scurtături globale**. Pentru o scurtătură personalizată, apasă în câmpul dedicat, tastează combinația dorită și apasă **Aplică**. Alegerea înlocuiește scurtăturile implicite și se păstrează între porniri. Dacă noua combinație este ocupată, cea anterioară rămâne activă. Dacă scurtătura salvată nu mai este disponibilă la pornire, folosește butonul de captură și alege alta.

Bara de unelte este verticală și compactă, cu acțiunile într-un rând dedesubt. Apasă pe culoarea curentă pentru a deschide paleta; se închide după alegerea unei culori. Acolo poți alege și o culoare personalizată sau grosimea liniei. Elipsa și mascarea au fost scoase din bară și din scurtăturile editorului.

Pictogramele [Lucide](https://lucide.dev/) sunt incluse în fișierul Python și reutilizate după prima randare. Nu necesită internet sau un pachet suplimentar. Licențele sunt păstrate în [notificările pentru componente terțe](../THIRD_PARTY_NOTICES.md) și în script.

## Setări și ecran complet

- **General:** limba, tema luminoasă/întunecată, notificările, memorarea zonei, includerea cursorului și dosarul de salvare.
- **Scurtături globale:** activezi sau dezactivezi separat scurtătura pentru zonă și pentru ecran complet. Tastează combinația și apasă **Aplică**. Scurtătura pentru ecran complet pornește dezactivată; propunerea este `Ctrl+Shift+F10`. Butoanele rămân disponibile.
- **Format:** PNG/JPEG, calitatea JPEG între 1 și 100 și comportamentul capturii complete.

**Ecran complet** capturează monitorul pe care se află cursorul, la rezoluția sa nativă. Inițial deschide editorul cu tot monitorul selectat. Poți alege **Salvează imediat în dosar** pentru salvare directă, fără editor sau dialog. Setarea se aplică butonului și scurtăturii pentru ecran complet.

Setările generale și de format se păstrează automat; scurtăturile se confirmă cu **Aplică**. Ultima zonă se memorează după copiere sau salvare și se restaurează pe același monitor. O captură completă nu înlocuiește zona memorată.

Clicul stâng pe pictograma de lângă ceas pornește selectarea unei zone. Clicul drept deschide cele trei opțiuni: captură, deschiderea aplicației și ieșire. Capturile rămân locale.

![Tema întunecată](../assets/interface-ro-dark.png)

## Pictograma de lângă ceas

Închiderea ferestrei păstrează aplicația în zona de notificări, când aceasta este disponibilă. Pentru închiderea completă, apasă clic dreapta pe pictograma verde petrol și alege **Ieșire**.

Pentru a vedea schimbările după înlocuirea fișierului Python, închide mai întâi aplicația din acest meniu, apoi pornește noul fișier. O a doua pornire, cât timp aplicația rulează, redeschide instanța existentă.

## Confidențialitate și limite

Aplicația nu trimite capturi pe internet și nu cere cont. Salvarea produce o imagine cu adnotările aplicate, fără originalul ascuns sau istoricul editării.

Clipboardul este cel standard Windows. Istoricul și sincronizarea sa, dacă sunt activate, sunt gestionate de Windows.

- O captură poate acoperi o zonă de pe un singur monitor.
- OCR, capturile cu derulare și selectarea automată a ferestrelor nu sunt incluse.
- Dacă o scurtătură este ocupată de alt program, folosește una dintre cele afișate sau butonul pentru captură.
- Monitoarele HDR și conținutul video protejat nu au fost validate.
- Programul nu se adaugă automat la pornirea Windows.

Cele 28 de teste locale verifică desenarea, selecția, traducerile, exportul, bara compactă și configurarea scurtăturilor. Dezvoltarea a fost verificată pe Windows cu Python 3.14 și PySide6 6.12.0.

[Raportează o problemă](https://github.com/TOKKAB1/LumaShot/issues) · [Înapoi la proiect](../README.md)

## Licență și contribuții

Codul original LumaShot, documentația și pictograma verde petrol a aplicației sunt publicate sub [licența MIT](../LICENSE), cu notificarea `Copyright (c) 2026 TOKKAB1`. Oricine le poate folosi, modifica și redistribui, inclusiv comercial, păstrând licența și notificarea de autor. Licența este inclusă și în fișierul Python.

Pictogramele Lucide păstrează licențele ISC/MIT. PySide6 și Qt se instalează separat și au propriile licențe, care nu sunt înlocuite de MIT. Vezi [notificările componentelor terțe](../THIRD_PARTY_NOTICES.md).

Proiectul este independent de Lightshot și Greenshot și nu include codul, logo-urile sau executabilele lor. Pentru întregul proiect, folosește **Code → Download ZIP** pe GitHub. Contribuțiile sunt binevenite: [ghid de contribuție](../CONTRIBUTING.md).
