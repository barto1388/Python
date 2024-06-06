print("Gra w kółko i krzyżyk")
print("Zasady:")
print("Kolumny reprezentowane sa przez litery (A,B,C)")
print("Rzędy reprezentowane są przez cyfry (1,2,3)")

# player_1 = input("Gracz 1: podaj imię")
# player_2 = input("Gracz 2: podaj imię")

player_1 = "Bogdan"
player_2 = "Marian"

player_1_moves = []
player_2_moves = []

# plansza = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
plansza = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

player_1_turn = ""
player_2_turn = ""

#kombinacje do zwycięstwa
# "A1", "A2", "A3"
# "B1", "B2", "B3"
# "C1", "C2", "C3"
# "A1", "B1", "C1"
# "A2", "B2", "C2"
# "A3", "B3", "C3"
# "A1", "B2", "C3"
# "A3", "B2", "C1"

win = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"],
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"],
    ["A1", "B2", "C3"],
    ["A3", "B2", "C1"]
]

while True:
    print("\n", plansza[0], plansza[1], plansza[2], "\n", plansza[3], plansza[4], plansza[5], "\n", plansza[6], plansza[7], plansza[8])
    print(f"Dostępne pola: {plansza}")
    print(f"{player_1}, oto Twoje wybrane pola: {player_1_moves}")
    while player_1_turn not in plansza:
        player_1_turn = input(f"{player_1}, wybierz pole")
        if player_1_turn in plansza:
            for index, pole in enumerate(plansza):
                if pole == player_1_turn:
                    plansza[index] = "x"
                    player_1_moves.append(player_1_turn)
                    player_1_moves.sort()
            break
        else:
            print("Niewłaściwa wartość, podaj pole jeszcze raz")
    print(f"{player_1}, oto Twoje wybrane pola: {player_1_moves}")
    for kombinacja in win:
        if kombinacja[0] in player_1_moves and kombinacja[1] in player_1_moves and kombinacja[2] in player_1_moves:
            print(f"BRAWO, {player_1}, WYGRAŁEŚ! {player_2}, KIJ CI W OKO!")
            print(kombinacja)
            break
    if len(plansza) == 0:
        print("Remis")
        break
    #break

    print("\n", plansza[0], plansza[1], plansza[2], "\n", plansza[3], plansza[4], plansza[5], "\n", plansza[6], plansza[7], plansza[8])
    print(f"Dostępne pola: {plansza}")
    print(f"{player_2}, oto Twoje wybrane pola: {player_2_moves}")
    while player_2_turn not in plansza:
        player_2_turn = input(f"{player_2}, wybierz pole")
        if player_2_turn in plansza:
            for index, pole in enumerate(plansza):
                if pole == player_2_turn:
                    plansza[index] = "o"
                    player_2_moves.append(player_2_turn)
                    player_2_moves.sort()
            break
        else:
            print("Niewłaściwa wartość, podaj pole jeszcze raz")
    for kombinacja in win:
        if kombinacja[0] in player_2_moves and kombinacja[1] in player_2_moves and kombinacja[2] in player_2_moves:
            print(f"BRAWO, {player_2}, WYGRAŁEŚ! {player_1}, KIJ CI W OKO!")
            break
    if len(plansza) == 0:
        print("Remis")
        break
