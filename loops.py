lin = int(input("podaj liczbe linijek: "))
x = 1
s = int(lin)
while x<=(int(lin)*2):
    print(" "*s + ('*'*x))
    x+=2
    s-=1
else:
    print(lin*' '+'*')