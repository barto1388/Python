#Dlaczego w poniższym przykładzie podawanie kategorii w pętli musi być przed inputem

wydatki = {}

kategoria = input("podaj kategorię lub wciśnij x aby zakończyć podawanie")

while kategoria != "x":
    wydatki[kategoria] = ""
    kategoria = input("podaj kategorię lub wciśnij x aby zakończyć podawanie")