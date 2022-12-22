'''
def inf(nick, wiek, wzrost):
    print(f"{nick}, {wiek} lat, {wzrost} m wzrostu")
    pass
nick = input(str("podaj nick: "))
wiek = input(int("podaj wiek: "))
wzrost = input(float("podaj wzrost (w metrach): "))
inf(nick, wiek, wzrost)
'''

def kom(nick: str, wiek: int, wzrost: float) -> str:
    return(f"{nick}, {wiek} lat, {wzrost:.2f} m wzrostu")

print(kom("xenkii :)", 13, 1.65436))
