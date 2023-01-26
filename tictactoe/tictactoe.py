'''
0 - puste pole
1 - oznacza gracz x
2 - oznacza gracz o
'''

from board import *
from move import *

gracz = 'X'
czyKoniecGry = False

plansza = tworzPlansze()
printPlansza(plansza, gracz)

def czyKoniec(plansza):
    if plansza[0][0] != "[ ]" and plansza[0][0] == plansza [0][1] and plansza [0][1] == plansza [0][2]:
        return True
    elif plansza[1][0] != "[ ]" and plansza[1][0] == plansza [1][1] and plansza [1][1] == plansza [1][2]:
        return True
    elif plansza[2][0] != "[ ]" and plansza[2][0] == plansza [2][1] and plansza [2][1] == plansza [2][2]:
        return True
    elif plansza[0][0] != "[ ]" and plansza[0][0] == plansza [1][0] and plansza [1][0] == plansza [2][0]:
        return True
    elif plansza[0][1] != "[ ]" and plansza[0][1] == plansza [1][1] and plansza [1][1] == plansza [2][1]:
        return True
    elif plansza[0][2] != "[ ]" and plansza[0][2] == plansza [1][2] and plansza [1][2] == plansza [2][2]:
        return True
    elif plansza[0][0] != "[ ]" and plansza[0][0] == plansza [1][1] and plansza [1][1] == plansza [2][2]:
        return True
    elif plansza[0][2] != "[ ]" and plansza[0][2] == plansza [1][1] and plansza [1][1] == plansza [2][0]:
        return True
    else:
        return False

while czyKoniecGry == False:
    kolumna = int(input("podaj kolumne do ruchu [0-2]: "))
    wiersz = int(input("podaj wiersz do ruchu [0-2]: "))
    gracz = ruch(plansza, gracz, kolumna, wiersz)
    printPlansza(plansza, gracz)
    czyKoniecGry = czyKoniec(plansza)
    if czyKoniecGry:
        print("hurra! wygrałeś!")