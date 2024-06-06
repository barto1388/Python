# zapytanie = input("elo byczqu, ile masz lat?")
# miesiace = int(zapytanie) * 12
#
# print("ociebaton, to będzie", miesiace, "miesięcy!")
#
# zapytanie2 = input("byczq, a ile kilometrów pokonałes w tym tydniu?")
# obwod = 40075 / int(zapytanie2)
#
# print("o ja pierdolę mordeczko, to w tym tempie okrazenie Ziemi zajmie ci", obwod, "tygodni. kurwa czaisz to?")

# oto mój dojebany komentarz
wartosc_poczatkowa_input = input("wprowadź wartość")
wartosc_poczatkowa_liczba = int(wartosc_poczatkowa_input)

procent_input = input("wprowadź procentaż")
procent_liczba = int(procent_input)

ilosc_lat_input = input("wprowadź dlugosc czasu trwania lokaty w latach")
ilosc_lat_liczba = int(ilosc_lat_input)

wartosc_poczatkowa = str(wartosc_poczatkowa_liczba)
procent = str(procent_liczba)
ilosc_lat = str(ilosc_lat_liczba)

wartosc = wartosc_poczatkowa_liczba * (1 + procent_liczba / 100) ** ilosc_lat_liczba
ilosc_procentow = wartosc * 1/100
print(wartosc)
print(ilosc_procentow)

# def liczymy_lokate(initial_value, percentage, years):
#
#     wartosc = initial_value * (1 + percentage / 100) ** years
#
#     return wartosc

#print("Jeśli wpłacisz", wartosc_poczatkowa, "złotych na oprocentowanie", procent + "%", "w skali roku na okres", ilosc_lat, "lat, to po tym czasie będziesz miał", str(liczymy_lokate(wartosc_poczatkowa_liczba,procent_liczba,ilosc_lat_liczba)))

# print(f"Jeśli wpłacisz {wartosc_poczatkowa} złotych na oprocentowanie {procent}% w skali roku na okres {ilosc_lat} lat, to po tym czasie będziesz miał {liczymy_lokate(wartosc_poczatkowa_liczba,procent_liczba,ilosc_lat_liczba):.2f}, zyla")

print(f"Jeśli wpłacisz {wartosc_poczatkowa} złotych na oprocentowanie {procent}% w skali roku na okres {ilosc_lat} lat, to po tym czasie będziesz miał {wartosc:.2f}, zyla")
print(f"czy łączna wartośc inwestycji wzrośnie o co najmniej 10% {ilosc_procentow >= 10}")