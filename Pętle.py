licznik,koniec=10,15

if 3 > 22:
    print("3")

elif 21 < 3:  # 2==2 jest równe      !# nie jest równe
    print("33")

else:
    print("NIE")


while licznik<=koniec:
    licznik+=1
    print(licznik-1)



for i in range(3): #od zera do ile liczb
    print (i)

for i in range(10,14): #od liczby do ile liczb
    print (i)

for i in range(0,5,3): #od liczby do ile liczb co 3 znak
    print (i)


bar = "Zdrabniamy literki"
for i in bar:
    print (i)

bar = ["foo", "bar", "yaz"]
for i in bar:
    print (i)

bar = {"imie" : "jurek", "nazwisko" : "lepper"}
print (bar["imie"])
for i in bar:
    print (i + " - " +bar[i])

print (bar["imie"])

lista = bar.keys()
print (lista)

for i in lista:
    print (i)

#del bar["imie"]
print (bar)

bar ["numer"] = "DW6C559"

#print (bar.keys["lepper"])

x,z,q,w=40,10,40,10
for i in range(10):
    print(x,"dBm =",z,"Vat")
    x += 3
    z = z*2

    print(q, "dBm =", w, "Vat")
    q -= 3
    w = w / 2