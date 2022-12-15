"""
def powitanie():
    print(f"hej, {imie}")
    pass

x = input("podaj swoje imie: ")
powitanie(x)
y = input("podaj imie osoby, ktora siedzi obok cb: ")
powitanie(y)
"""
'''
def pole(x, y):
    print(f"pole wynosi: {x*y}")
    pass
a = int(input("Podaj dł pierwszego boku: "))
b = int(input("Podaj dł drugiego boku: "))
pole(a, b)
'''

import math

def pole(x):
    print(f"pole kola o promieniu {x} wynosi: {math.pi*math.pow(x,2)}")
    pass

print(pole(5))

