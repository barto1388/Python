# print("siema zbyszek, jaka jest cena")
# ogorek = int(input("ogorka?"))
# papryka = int(input("papryki?"))
# # warzywa = int(input("warzyw?"))
# #
# # # print(f"ogorek jest drozszy od papryki chuju {ogorek > papryka}")
# # # print(f"papryka jest tansza od warzyw {papryka < warzywa}")
# # # print(f"ogorek jest tanszy od warzyw {ogorek < warzywa}")
# #
# # if ogorek > papryka:
# #     print("ogorek jest drozszy od papryki")
# # elif ogorek == papryka:
# #     print("ogorek kosztuje tyle samo co papryka")
# # else:
# #     print("ogorek jest tanszy od papryki")
# #
# # if papryka > warzywa:
# #     print("papryka jest drozsza od warzyw")
# # else:
# #     print("papryka jest tansza od warzyw")
# #
# # if ogorek > warzywa:
# #     print("ogorek jest drozszy od warzyw")
# # else:
# #     print("ogorek jest tanszy od warzyw")
#
#druge
# elementy = input("wprowadz elementy, oddzielajac je przecinkiem")
# lista_zakupow = elementy.split(",")
# print(lista_zakupow)
#
# czy_dluga_lista = len(lista_zakupow) > 3
#
# print(f"na liscie jest {len(lista_zakupow)} jebanych elementow")
# # print(f"czy lista jest dluga?  {czy_dluga_lista}")
#
# if len(lista_zakupow) > 3:
#     print("łokurwa ale dluga ta lista")
# else:
#     print("no spoko ta lista taka nie za dluga")


#naprawde drugie
# print("siema, ile miesiecznie wydajesz na")
# jedzenie_input = int(input("zarcie?"))
# rozrywka_input = int(input("rozrywke?"))
# oplaty_input = int(input("oplaty?"))
#
# suma = jedzenie_input + rozrywka_input + oplaty_input
# print(suma)
#
# wydatki = {
#     "jedzenie": 100 * jedzenie_input / suma,
#     "rozrywka": 100 * rozrywka_input / suma,
#     "oplaty": 100 * oplaty_input / suma
# }
#
# print(wydatki)
#
# udzial_procentowy = input("wybierz kategorie pls")
#
# print(f"wybrales kategorie {udzial_procentowy}, jego udzial procentowy to {wydatki[udzial_procentowy]:.2f}%")
#
# if jedzenie_input > (rozrywka_input and oplaty_input):
#     print("najwyięcej wydajesz na jedzenie")
# elif rozrywka_input > (jedzenie_input and oplaty_input):
#     print("najwięcej wydajesz na rozrywkę")
# elif oplaty_input > (jedzenie_input and rozrywka_input):
#     print("najwięcej wydajesz na oplaty")

#czecie
# oceny = {}
#
# matematyka_ocena = int(input("jaka masz ocene z matmy?"))
# oceny["matematyka"] = matematyka_ocena
# polski_ocena = int(input("jaka masz ocene z polaka?"))
# oceny["jezyk polski"] = polski_ocena
# pszyra_ocena = int(input("jaka masz ocene z pszyry?"))
# oceny["pszyroda"] = pszyra_ocena
# gegra_ocena = int(input("jaka masz ocene z gegry?"))
# oceny["geografia"] = gegra_ocena
#
# print(oceny)
#
# srednia = (oceny["matematyka"] + oceny["jezyk polski"] + oceny["pszyroda"] + oceny["geografia"]) / int(len(oceny))
# print(srednia)
#
# kapa = 1
#
# liczba_kap = 0
#
# if oceny["matematyka"] == kapa:
#     liczba_kap = (liczba_kap + kapa)
# if oceny["jezyk polski"] == kapa:
#     liczba_kap = (liczba_kap + kapa)
# if oceny["pszyroda"] == kapa:
#     liczba_kap = (liczba_kap + kapa)
# if oceny["geografia"] == kapa:
#     liczba_kap = (liczba_kap + kapa)
#
# if liczba_kap == 0:
#     print("brawo, zdales do nastepnej klasy")
# else:
#     if liczba_kap == 1:
#         if srednia > 3.5:
#             print("jedna kapa ale przechodzisz")
#         else:
#             print("sorki Winetou")
#     else:
#         print("sorki Winetou")

# if (oceny["matematyka"] != kapa) and (oceny["jezyk polski"] != kapa) and (oceny["pszyroda"] != kapa) and (oceny["geografia"] != kapa):
#     print("brawo, zdales do nastepnej klasy")
# elif ((oceny["matematyka"] == kapa or oceny["jezyk polski"] or oceny["pszyroda"] or oceny["geografia"]) == kapa) and (srednia > 3.5):
#     print("masz jedna jedynke, ale zdales")
# else:
#     print("siup, spadochron")


#czwarte
# imie = input("jak masz na imie?")
#
# if imie[-1] == "a":
#     print("jestes niewiastom")
# else:
#     print("jesteś menzszczyznom")

#TEST COOPERA
wiek = int(input("Podaj swój wiek"))
plec = input("Podaj płeć: wpisz M lub K")
wynik = int(input("Podaj swój wynik"))


if 20 <= wiek <= 29:
    if plec == "M":
        if wynik < 1600:
            print("Bardzo źle")
        elif 1600 <= wynik <= 2199:
            print("Źle")
        elif 2200 <= wynik <= 2399:
            print("Średnio")
        elif 2400 <= wynik <= 2800:
            print("Dobrze")
        elif 2800 <= wynik:
            print("Bardzo dobrze")
    elif plec == "K":
        if wynik < 1500:
            print("Bardzo źle")
        elif 1500 <= wynik <= 1799:
            print("Źle")
        elif 1800 <= wynik <= 2199:
            print("Średnio")
        elif 2200 <= wynik <= 2700:
            print("Dobrze")
        elif 2700 <= wynik:
            print("Bardzo dobrze")
    else:
        print("niewlasciwe dane, wybierz M lub K")
elif 30 <= wiek <= 39:
    if plec == "M":
        if wynik < 1500:
            print("Bardzo źle")
        elif 1500 <= wynik <= 1899:
            print("Źle")
        elif 1900 <= wynik <= 2299:
            print("Średnio")
        elif 2300 <= wynik <= 2700:
            print("Dobrze")
        elif 2700 <= wynik:
            print("Bardzo dobrze")
    elif plec == "K":
        if wynik < 1400:
            print("Bardzo źle")
        elif 1400 <= wynik <= 1699:
            print("Źle")
        elif 1700 <= wynik <= 1999:
            print("Średnio")
        elif 2000 <= wynik <= 2500:
            print("Dobrze")
        elif 250 <= wynik:
            print("Bardzo dobrze")
    else:
        print("niewlasciwe dane, wybierz M lub K")
else:
    print("jestes za mlody lub za stary")

#LOKATA PLUS HIPOTEKA
# zapytanie = input("byczqu, wybierz jedną z dwóch opcji: \nobliczanie jebanej lokaty \nobliczanie pierdolonej hipoteki")
#
# if zapytanie == "obliczanie jebanej lokaty":
#     wartosc_poczatkowa_input = input("wprowadź wartość")
#     wartosc_poczatkowa_liczba = int(wartosc_poczatkowa_input)
#
#     procent_input = input("wprowadź procentaż")
#     procent_liczba = int(procent_input)
#
#     ilosc_lat_input = input("wprowadź dlugosc czasu trwania lokaty w latach")
#     ilosc_lat_liczba = int(ilosc_lat_input)
#
#     wartosc_poczatkowa = str(wartosc_poczatkowa_liczba)
#     procent = str(procent_liczba)
#     ilosc_lat = str(ilosc_lat_liczba)
#
#     wartosc = wartosc_poczatkowa_liczba * (1 + procent_liczba / 100) ** ilosc_lat_liczba
#     ilosc_procentow = wartosc * 1 / 100
#
#     print(wartosc)
#     print(ilosc_procentow)
#     print(f"Jeśli wpłacisz {wartosc_poczatkowa} złotych na oprocentowanie {procent}% w skali roku na okres {ilosc_lat} lat, to po tym czasie będziesz miał {wartosc:.2f}, zyla")
#     print(f"czy łączna wartośc inwestycji wzrośnie o co najmniej 10% {ilosc_procentow >= 10}")
#
# elif zapytanie == "obliczanie pierdolonej hipoteki":
#     kwota_kredytu = float(input("podaj kwote kredytu"))
#     oprocentowanie_kredytu = float(input("podaj wysokosc oprocentowania"))
#     wklad_wlasny = float(input("podaj wklad wlasny"))
#     liczba_lat = float(input("podaj okres"))
#     miesieczny_przychod = float(input("podaj miesiewczny przychod"))
#     suma_miesiecznych_wydatkow = float(input("podaj sume miesiecznych wydatkow"))
#
#     rata = ((kwota_kredytu * oprocentowanie_kredytu/100) / 12) + (kwota_kredytu / (liczba_lat * 12))
#     print(f"rata{rata}")
#
#     dostepne_srodki = miesieczny_przychod - suma_miesiecznych_wydatkow
#     print(f"dostepne srodki{dostepne_srodki}")
#
#     wartosc_nieruchomosci = wklad_wlasny + kwota_kredytu
#     print(f"wartosc nieruchomosci{wartosc_nieruchomosci}")
#
#     naleznosc = rata * (liczba_lat * 12)
#     print(f"naleznosc{naleznosc}")
#
#     if wklad_wlasny >= (wartosc_nieruchomosci * 10/100):
#         wklad = True
#     else:
#         wklad = False
#
#     print(f"10% wartosci nieruchomosci{wartosc_nieruchomosci * 10/100}")
#
#     if (dostepne_srodki >= rata) and wklad:
#         print("mozna udzielic kredytu")
#     else:
#         print("sorki")
#
# else:
#     print("podana opcja nie istnieje, upewnij sie że wybrałeś jedną z dwóch podanych opcji")

# elementy = input("wprowadz elementy, oddzielajac je przecinkiem")
# lista_zakupow = elementy.split(",")
# print(lista_zakupow)
#
# czy_dluga_lista = len(lista_zakupow) > 3
#
# print(f"na liscie jest {len(lista_zakupow)} jebanych elementow")
# # print(f"czy lista jest dluga?  {czy_dluga_lista}")
#
# if len(lista_zakupow) > 3:
#     print("łokurwa ale dluga ta lista")
# else:
#     print("no spoko ta lista taka nie za dluga")
#
#
# # if "chleb" in lista_zakupow or "bułki" in lista_zakupow:
# #     print("na liscie jest pieczywo")
# # else:
# #     print("na liscie nie ma pieczywa")
#

#drugie
# tel = input("podaj swoj numer")
#
# if "0" in tel:
#     print("w numerze jest 0")
# else:
#     print("w numerze nie ma 0")

#trzecie
value = 3

print(type(value))

if value is True:
    print("to prawda")
elif value is False:
    print("to nieprawda")
elif value is None:
    print("to jest nic")
else:
    print("to inna wartosc")

# counter = 1
# liczba = int(input("podaj parzystą liczbę"))
#
# while counter < 10 and liczba % 2 != 0:
#     liczba = int(input("podaj jeszcze raz"))
#     counter += 1
#     if counter == 10:
#         print("zuzyles 10 prob")
#
# if liczba % 2 == 0:
#     print("brawo")


# #wczytaj nr tel i rozdziel myslnikami (format XXX-XXX-XXX)
# tel = input("podaj numer telefonu")
# formatted_tel = ""
# index = 0
# while index < len(tel):
#     if index % 3 == 0 and index != 0:
#         formatted_tel += "-"
#     formatted_tel += tel[index]
#     index += 1
# print(formatted_tel)

#trzecie
pytanie = "spageti,lasange,pizza"
lista = pytanie.split(",")
print(lista)
index = 0

while index < len(lista):
    print(f"pozycja {index + 1} to {lista[index]}")
    index += 1


# oceny = []
# zapytanie = input("podaj ocenę lub wcisnij x")
#
# while zapytanie != "x":
#     ocena = int(zapytanie)
#     oceny.append(ocena)
#     zapytanie = input("podaj ocenę lub wcisnij x")
#
# print(oceny)
#
# suma = 0
# for grade in oceny:
#     suma += grade
#
# print(suma)
#
# srednia = suma / len(oceny)
#
# print(srednia)

#drugie kurwa
#wczytaj nr tel i rozdziel myslnikami (format XXX-XXX-XXX)
# tel = input("podaj numer telefonu")
# formatted_tel = ""
# index = 0
#
# for index, letter in enumerate(tel):
#     if index % 3 == 0 and index != 0:
#         formatted_tel += "-"
#     formatted_tel += tel[index]
# print(formatted_tel)

#trzecie
wydatki = {}
kontynuacja = ""

while kontynuacja != "n":
    kategoria = input("podaj kategorię")
    koszt = int(input("podaj koszt"))
    wydatki[kategoria] = koszt
    kontynuacja = input("czy chcesz podac kolejna kategorie? T/N")

suma = sum(wydatki.values())
print(suma)
print(wydatki)

# for percent in wydatki.values():
#     procentaż = 100 * percent / suma
#     print(procentaż)

for category, percent in wydatki.items():
    category = str(category)
    procentaż = 100 * percent / suma
    print(procentaż)



wazny = max(wydatki.values())
print(wazny)
print(f"Widzę Zbysiu, że najwięcej wydajesz na {kategoria}, przeznaczasz na to {procentaż}%")

# oceny = {}
#
# matematyka_ocena = int(input("jaka masz ocene z matmy?"))
# oceny["matematyka"] = matematyka_ocena
# polski_ocena = int(input("jaka masz ocene z polaka?"))
# oceny["jezyk polski"] = polski_ocena
# pszyra_ocena = int(input("jaka masz ocene z pszyry?"))
# oceny["pszyroda"] = pszyra_ocena
# gegra_ocena = int(input("jaka masz ocene z gegry?"))
# oceny["geografia"] = gegra_ocena
#
# print(oceny)
#
# srednia = (oceny["matematyka"] + oceny["jezyk polski"] + oceny["pszyroda"] + oceny["geografia"]) / int(len(oceny))
# print(srednia)
#
# kapa = 1
#
# for ocena in oceny.values():
#     print(ocena)
#     if ocena == kapa:
#         print("siup")
#         break
# else:
#     print("brawo")

#trzecie
# lista = ["prad", "woda", "gaz", "media", "mass", "banany", "owoce", "qwerty"]
#
# for index, x in enumerate(lista):
#     #print(x)
#     if index % 2 != 0:
#         continue
#     print(x)

# wydatki = {}
#
# kategoria = input("podaj kategorię lub wciśnij x aby zakończyć podawanie")
#
# while kategoria != "x":
#     wydatek = int(input("podaj koszt"))
#     wydatki[kategoria] = wydatek
#     kategoria = input("podaj kategorię lub wciśnij x aby zakończyć podawanie")
#
# print(f"nasza lista wydatkow to: {wydatki}")
#
# suma = sum(wydatki.values())
#
# print(f"suma wydatkow to: {suma}")
#
# wydatki_procent = {}
#
# for category, expens in wydatki.items():
#     wydatki_procent[category] = 100 * expens / suma
#
# print(f"wydatki procent: {wydatki_procent}")
#
# best = 0
# for category, procent in wydatki_procent.items():
#     if procent > best:
#         best = procent
#         kategoria = category
# print(f"najwiekszy procentowy udzial ma kategoria {kategoria}, jej udzial to {best}")


#WERSJA Z FUNKCJAMI

# wydatki = {}
#
#
# def kat_ex(cat, exp):
#     wydatki[cat] = exp
#
#
# kategoria = input("podaj kategorię lub wciśnij x aby zakończyć podawanie")
#
# while True:
#     wydatek = int(input("podaj koszt"))
#     kat_ex(kategoria, wydatek)
#     kategoria = input("podaj kategorię lub wciśnij x aby zakończyć podawanie")
#     if kategoria == "x":
#         break
# #print(f"no fajnie, podaj kategorię {kat_ex(kategoria, wydatek)}")
#
#
# print(f"nasza lista wydatkow to: {wydatki}")
#
# suma = sum(wydatki.values())
#
# print(f"suma wydatkow to: {suma}")
#
# wydatki_procent = {}
#
# for category, expens in wydatki.items():
#     wydatki_procent[category] = 100 * expens / suma
#
# print(f"wydatki procent: {wydatki_procent}")
#
# best = 0
# for category, procent in wydatki_procent.items():
#     if procent > best:
#         best = procent
#         kategoria = category
# print(f"najwiekszy procentowy udzial ma kategoria {kategoria}, jej udzial to {best}")
