def tworzPlansze():
    plansza = []
    for x in range(3):
        plansza.append([])
        for y in range(3):
            plansza[x].append('[ ]')
    return plansza

def printPlansza(plansza, gracz):
    print()
    print(f"Gra trwa. Następny ruch: {gracz}")
    for x in range(3):
        wiersz = ""
        for y in range(3):
            wiersz = wiersz + str(plansza[x][y])
        print(wiersz) 
