class Osoba():
    def __init__(self, imie):
        self.imie = imie
        self.nazwisko = "Maksymenko"
        self.wiek = 25

class Pracownik(Osoba):
    def __init__(self, stanowisko):
        super().__init__ ("Krzyś")
        self.stanowisko = stanowisko
        self.specjalizacja = "Python"

class Klient(Osoba):
    def __init__(self, imie):
        super().__init__(imie)
        self.zamowienie = "Strona Internetowa"



pracownik = Pracownik("Programista")
print (pracownik.imie)
print (pracownik.stanowisko)

pracownik2 = Pracownik("Designer")
print (pracownik2.imie)
print (pracownik2.stanowisko)

pracownik3 = Pracownik("Tester")
print (pracownik3.imie)
print (pracownik3.stanowisko)

klient = Klient("Karolina")
print(klient.imie)
print (klient.zamowienie)

klient = Klient("Wika")
print(klient.imie)
print (klient.zamowienie)