def ruch(plansza, gracz, kolumna, wiersz):
    if kolumna > 2 or wiersz > 2 or plansza[wiersz][kolumna] != '[ ]':
        print("Błędny ruch. Spróbuj ponownie.")
        return gracz
    plansza[wiersz][kolumna] = f'[{gracz}]'
    gracz = zmianaGracza(gracz)
    return gracz

def zmianaGracza(gracz):
    if gracz == 'X':
        gracz = 'O'
    elif gracz =='O':
        gracz = 'X'
    return gracz