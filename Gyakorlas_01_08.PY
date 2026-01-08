
import os
import random
import math
os.system("cls")  # Képernyő törlése (Windows rendszeren)

print("1. Feladat")
# Bekérünk egy egész számot a felhasználótól
szam = int(input("Kérlek adj megy egy egész számot: "))

# Megvizsgáljuk, hogy a szám pozitív páros, negatív páratlan, vagy egyik sem
if szam % 2 == 0 and szam > 0:
    print(f"A {szam} az Pozitív és Páros.")
elif szam % 2 != 0 and szam < 0:
    print(f"A {szam} Negatív és Páratlan.")
else:
    print(f"A {szam} egyik feltételnek se felet meg.")

print("2. Feladat:")

# Bekérjük, hogy Henrik és Hanna jönnek-e kosarazni
henrik = str(input("Jön Henrik ma kosarazni? (igen/nem) "))
Hanna = str(input("Jön Hanna ma kosarazni? (igen/nem) "))

# Kiértékeljük a válaszokat, és kiírjuk a megfelelő üzenetet
if henrik == "igen" and Hanna == "igen":
    print("Mindketten jönnek kosarazni.")
elif henrik == "igen" or Hanna == "igen":
    print("Csak egyikük jön kosarazni.")
else:
    print("Egyikük se jön kosarazni.")

print("3. Feladat")

# Bekérünk egy számot a felhasználótól
szam2 = int(input("Kérlek adj meg egy számot: "))
# Megvizsgáljuk, hogy 3-mal, 4-gyel, mindkettővel vagy egyikkel sem osztható
if szam2 % 3 == 0 and szam2 % 4 == 0:
    print("A szám 3-mal és 4-gyel is osztható")
elif szam2 % 3 == 0:
    print("A szám csak 3-mal osztható")
elif szam2 % 4 == 0:
    print("A szám csak 4-gyel osztható")
else:
    print("A szám sem 3-mal, sem 4-gyel nem osztható.")

print("4. feladat: ")
# Bekérünk egy számot 1 és 3 között
randombekeres = int(input("Kérlek adj meg egy számot 1-3 között: "))
# Generálunk egy véletlen számot 1 és 3 között
randomszam = random.randint(1,3)
print(f"A random szám: {randomszam}")
# Összehasonlítjuk a két számot
if randombekeres == randomszam:
    print("Megegyezik!")
else:
    print("Nem egyeik.")

print("5. feladat:")
# Létrehozunk egy listát a pénzérme oldalairól
penzerme = ["fej", "írás"]
# Bekérjük a felhasználó tippjét
penz = str(input("Kérlek add meg hogy (fej/írás): "))
# Véletlenszerűen kiválasztjuk az egyik oldalt
veletlenpenz = random.choice(penzerme)
print(veletlenpenz)
# Megnézzük, hogy eltalálta-e a felhasználó
if penz == veletlenpenz:
    print(f"Eltaláltad! {veletlenpenz}")
else:
    print("Nem találtad el... balfasz xD")

print("6. Feladat: ")
keresztnevek = []
# Addig kérünk be keresztneveket, amíg a felhasználó ENTER-t nem nyom
while True:
    keresztnev = input("Kérlek adj meg egy keresztnevet: ")
    if not keresztnev:
        break
    keresztnevek.append(keresztnev)
print(keresztnevek)

print("7. Feladat: ")
keresztnevek2 = []
# Maximum 3 keresztnevet kérünk be
while True:
    if len(keresztnevek2) == 3:
        break
    keresztnev2 = input("Kérlek adj meg egy keresztnevet: ")
    if not keresztnev2:
        break
    keresztnevek2.append(keresztnev2)
print(keresztnevek2)

print("8. Feladat: ")
aszavak = []
# Addig kérünk be szavakat, amíg a felhasználó ENTER-t nem nyom
while True:
    aszavakbekeres = str(input("Kérlek adj megy kis 'a' betűvel kezdődő szavakat. Amennyiben befejzted, nyomj ENTER-t: "))
    x = aszavakbekeres.startswith("a")  # Ellenőrizzük, hogy 'a'-val kezdődik-e
    if x == True:
        aszavak.append(aszavakbekeres)
    if not aszavakbekeres:
        break
print(aszavak)

print("9. Feladat: ")
aszavak2 = []
# Addig kérünk be szavakat, amíg a felhasználó ENTER-t nem nyom
while True:
    aszavakbekeres2 = str(input("Kérlek adj megy kis 'a' betűvel kezdődő szavakat. Amennyiben befejzted, nyomj ENTER-t: "))
    x2 = aszavakbekeres2.startswith("a")
    x3 = aszavakbekeres2.startswith("A")
    if x2 == True or x3 == True:  # Kis vagy nagy 'A'-val kezdődik
        aszavak2.append(aszavakbekeres2)
    if not aszavakbekeres2:
        break
print(aszavak2)

print("10. Feladat: ")
random50 = []
# Generálunk 10 darab 4-gyel osztható véletlenszámot [0;50] között
while True:
    randomszam2 = random.randint(0,50)
    if randomszam2 % 4 == 0:
        random50.append(randomszam2)
    if len(random50) == 10:
        break 
print(random50)

print("11. Feladat: ")
random3 = []
# Generálunk 10 darab 3-mal osztható véletlenszámot [1;40] között
while True:
    random32 = random.randint(1,40)
    if random32 % 3 == 0:
        random3.append(random32)
    if len(random3) == 10:
        break
print(random3)

print("12-13. Feladat: ")
szavakT = []
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
# Kiválogatjuk a 't' vagy 'T' betűvel kezdődő szavakat
for szo in szavak:
    if szo.startswith(('t', 'T')):
        szavakT.append(szo)
print(szavakT)

print("14. Feladat: ")
szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
# Kiírjuk a 3-mal osztható páros számokat a listából
for szo2 in szamok:
    if szo2 % 3 == 0 and szo2 % 2 == 0:
        print(szo2)

print("15. Feladat: ")
# Bekérünk egy mondatot a felhasználótól
mondat = str(input("Kérlek írj egy mondatot mondatvégi írásjellel a végén! "))
# Megvizsgáljuk, milyen írásjellel végződik
if mondat.endswith("!"):
    print("A mondat Felkiáltójellel végződik.")
elif mondat.endswith("?"):
    print("A mondat kérdőjellel végződik.")
elif mondat.endswith("."):
    print("A mondat ponttal végőzdik.")
else:
    print("Nincs mondatvégi írásjel...")

print("16. Feladat: ")
# Addig kérünk be mondatokat, amíg a felhasználó ENTER-t nem nyom
while True:
    mondatok = str(input("Kérlek adj meg mondatot, amíg nem nyomsz ENTER-T addig kérni fogja: "))
    if not mondatok:
        break
    if mondatok.endswith("!"):
        print("A mondat felkiáltó!")
    elif mondatok.endswith("?"):
        print("A mondat kérdő?")
    elif mondatok.endswith("."):
        print("A mondat kijelentő.")
    else:
        print("Nincs mondatvégi írásjel.")

print("17. Feladat: ")
randomlista = []
# Generálunk 5 darab véletlen számot [1;10] között, eltároljuk egy listában
while True:
    random15 = random.randint(1,10)
    randomlista.append(random15)
    if len(randomlista) == 5:
        break
print(f"A random lista: {randomlista}")
# Összeadjuk a lista elemeit
osszeg = sum(randomlista)
print(f"A random lista összege: {osszeg}")

print("18. Feldat: ")
randomlista2 = []
# Generálunk 5 darab páros véletlen számot [1;10] között
while True:
    random152 = random.randint(1,10)
    if random152 % 2 == 0:
        randomlista2.append(random152)
    if len(randomlista2) == 5:
        break
print(f"A random lista: {randomlista2}")
# Összeadjuk a lista elemeit
osszeg2 = sum(randomlista2)
print(f"A random lista összege: {osszeg2}")

print("19. Feladat:")
bekeres = []
# Addig kérünk be számokat 1-5 között, amíg a felhasználó intervallumon kívülit nem ír
while True:
    bekeres2 = int(input("Kérlek adj meg egy számot 1-5 között: "))
    if bekeres2 > 5 or bekeres2 < 1:
        break
    bekeres.append(bekeres2)
print(bekeres)    

print("20. Feladat: ")
# 1. Lista létrehozása és 5 véletlenszám generálása [1;7] között
szamok3 = []
for i in range(5):
    veletlen_szam = random.randint(1, 7)
    szamok3.append(veletlen_szam)
# 2. Szám bekérése a felhasználótól
user_szama = int(input("Kérlek adj meg egy számot 1 és 7 között: "))
# 3. Vizsgálat: előfordul-e a listában?
if user_szama in szamok3:
    print(f"Igen, a(z) {user_szama} szerepel a listában!")
else:
    print(f"Sajnos a(z) {user_szama} nem szerepel a listában.")
# 4. A lista elemeinek kiírása
print(f"A lista elemei: {szamok3}")

print("21. Feladat: ")
valtozo = "ezegykurvahosszuszo"
# Bekérünk egy betűt a felhasználótól
bekeres3 = input("Kérlek adj meg egy betűt: ")
x4 = valtozo.find(bekeres3)
# Megnézzük, hogy a betű megtalálható-e a szóban
if x4 != "":
    print(f"A keresett betű: {bekeres3} a szó pedig: {valtozo}")
else:
    print(f"Nem található benne a betű: {x4}")

print("22. Feladat: ")
sor = ["A", "B", "C"]
oszl = ["1", "2", "3"]
# Véletlenszerűen kiválasztunk egy sort és egy oszlopot
sorok = random.choice(sor)
oszlop = random.choice(oszl)
print(oszlop, sorok)
# Addig kérünk be tippeket, amíg el nem találja a hajó helyét
while True:
    sorok_jatekos = input("Kérlek add meg hogy melyik oszlopban van (A,B,C): ")
    oszlop_jatekos = input("Kérlek add meg melyik sorban van (1,2,3): ")
    if sorok == sorok_jatekos and oszlop == oszlop_jatekos:
        print("Sikeresen elsüllyesztetted a hajót!")
        break
    else: 
        print("Kérlek próbáld újra!")

print("23. Feladat: ")
lista2 = []
# Addig kérünk be számokat, amíg a felhasználó 99-et nem ír
while True:
    bekeres4 = int(input("Kérlek adj meg számokat, Kilépéshez 99: "))
    if bekeres4 == 99:
        break
    lista2.append(bekeres4)
# Összeadjuk a lista elemeit
x5 = sum(lista2)
print(f"A számok összege: {x5}")

print("24. Feladat: ")
# Függvény, amely megvizsgálja, van-e páros szám a listában
def paros_e(lista):
    for szam in lista:
        if szam % 2 == 0:  # Ha osztható 2-vel, páros
            return True
    return False  # Ha nem találtunk páros számot

# Példa használat
szamok = [1, 3, 5, 7]
print(paros_e(szamok))  # False, mert nincs páros szám

szamok2 = [1, 4, 7]
print(paros_e(szamok2))  # True, mert van páros szám (4)

print("25. Feladat: ")
# Függvény, amely megszámolja, hány hárommal osztható szám van a listában
def harommal_oszthatok(lista):
    darab = 0
    for szam in lista:
        if szam % 3 == 0:  # Ha osztható 3-mal
            darab += 1
    return darab

# Példa használat
szamok = [3, 6, 7, 9, 10, 12]
print(harommal_oszthatok(szamok))  # Eredmény: 4 (3, 6, 9, 12)

print("26. Feladat: ")
# Függvény, amely visszaadja a lista legkisebb elemét
def legkisebb_elem(szam_lista):
    return min(szam_lista)  # Visszaadja a legkisebb számot

pozitiv_szamok = []
print("Adj meg pozitív egész számokat! Kilépéshez írj be egy negatív számot.")
# Addig kérünk be számokat, amíg a felhasználó negatív számot nem ír
while True:
    bekeres_szam = int(input("Szám: "))
    if bekeres_szam < 0:
        break
    pozitiv_szamok.append(bekeres_szam)
# Ha van legalább egy szám, kiírjuk a legkisebbet
if pozitiv_szamok:
    legkisebb = legkisebb_elem(pozitiv_szamok)
    print(f"A megadott számok közül a legkisebb: {legkisebb}")
else:
    print("Nem adtál meg pozitív számot.")

print("27. Feladat:")
# Adatok bekérése a felhasználótól
kutya_nev = input("Add meg a kutya nevét: ")
kutya_kor = int(input("Add meg a kutya életkorát (év): "))
kutya_fajta = input("Add meg a kutya fajtáját: ")
kutya_oltas = input("Van érvényes veszettség elleni oltása? (igen/nem): ")
# Szótár létrehozása a kutya adataival
kutya_adatok = {
    "Név": kutya_nev,
    "Életkor": kutya_kor,
    "Fajta": kutya_fajta,
    "Veszettség elleni oltás": kutya_oltas
}
# Szépített kiírás: minden adat külön sorban
print("\nA megadott kutya adatai:")
for kulcs, ertek in kutya_adatok.items():
    print(f"{kulcs}: {ertek}")

print("28. Feladat:")
# Szótár létrehozása egy macska adataival
macska_adatok = {
    "Név": "Cirmi",
    "Kor": 3
}
# Kiírjuk az aktuális adatokat
print("Jelenlegi macska adatok:", macska_adatok)
# Felhasználó választása: melyik adatot módosítja?
valasztas = input("Melyik adatot szeretnéd módosítani? (Név/Kor): ")
# Ellenőrizzük, hogy létező kulcsot adott-e meg, és módosítjuk az értéket
if valasztas in macska_adatok:
    uj_ertek = input(f"Add meg az új értéket a(z) {valasztas} helyett: ")
# Ha a kor módosul, alakítsuk számmá
    if valasztas == "Kor":
        uj_ertek = int(uj_ertek)
    macska_adatok[valasztas] = uj_ertek
    print("Frissített macska adatok:", macska_adatok)
else:
     print("Hibás választás! Csak 'Név' vagy 'Kor' módosítható.")


print("29. Feladat:")

# Szótár létrehozása (int, str, bool típusú adatokkal)
adatok = {
    "Név": "Anna",
    "Kor": 25,
    "Aktív": True
}

# Kiírjuk az aktuális adatszerkezetet
print("Jelenlegi adatszerkezet:", adatok)

# Felhasználó bővítheti egy kulcs-érték párral
uj_kulcs = input("Add meg az új kulcs nevét: ")
uj_ertek = input("Add meg az új értéket: ")

# Az érték típusát nem tudjuk előre, így szövegként tároljuk
adatok[uj_kulcs] = uj_ertek

# Frissített adatszerkezet kiírása
print("Frissített adatszerkezet:", adatok)

print("30. Feladat:")

# Alap szótár (int, str, bool)
adatok = {
    "Név": "Anna",
    "Kor": 25,
    "Aktív": True
}

# Kiírjuk az aktuális adatszerkezetet
print("Jelenlegi adatszerkezet:", adatok)

# Többszöri bővítés lehetősége
while True:
    valasz = input("Szeretnél új kulcs-érték párt hozzáadni? (igen/nem): ").lower()
    if valasz != "igen":
        break

    uj_kulcs = input("Add meg az új kulcs nevét: ")
    uj_ertek = input("Add meg az új értéket: ")

    # Típusfelismerés (extra funkció)
    if uj_ertek.isdigit():
        uj_ertek = int(uj_ertek)
    elif uj_ertek.lower() in ["true", "false"]:
        uj_ertek = uj_ertek.lower() == "true"

    adatok[uj_kulcs] = uj_ertek
    print("Frissített adatszerkezet:", adatok)

print("Végleges adatszerkezet:", adatok)

print("31. Feladat:")

# Lista, amelyben a könyvek szótárként tárolódnak
konyvek = []

print("Adj meg könyvadatokat! (ENTER a szerzőnél = kilépés)")

while True:
    szerzo = input("Szerző: ")
    if not szerzo:  # Ha üres, kilépünk
        break
    cim = input("Cím: ")

    # Szótár létrehozása és hozzáadása a listához
    konyv_adat = {
        "Szerző": szerzo,
        "Cím": cim
    }
    konyvek.append(konyv_adat)

# Bevitt adatok listázása
print("\nBevitt könyvek adatai:")
for konyv in konyvek:
    print(f"Szerző: {konyv['Szerző']}, Cím: {konyv['Cím']}")
    
    

print("Kilépéshez nyomj entert.")
