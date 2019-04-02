#Funkcje

def nasza_funkcja(argument1, argument2):
    argumenty = argument1+" - "+argument2
    return argumenty


print (nasza_funkcja("Poczatek", "Koniec"))
print (nasza_funkcja("Tak", "Nie"))


def dodawanie(x, y, z):
    q = x+y+z
    return q
    # lub
#    return (tupla, tupla, bla, bla, bla)

print(dodawanie(4,5,6))


def funkcja(a1, a2 = "Koniec"):
    global a
    argumenty = a1+" - "+a2
    a = 1
    return argumenty
print (funkcja("Poczatek"))
print (a)


def printme(liczba):
    print("siema: ",end=' ')
    print (liczba)

printme(5)

def dodaj(x,y):
    print(x+y)

dodaj(2,4)


def dziel(x,y=10):
    return x/y
wynik = dziel (y=4,x=2)
w2 = dziel(4)

print (wynik)
print (w2)

def dodaj(a,b=2,c=3):
    return a+b+c

wynik = dodaj (5, c=10)
print (wynik)