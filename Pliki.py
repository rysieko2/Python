
f = open("plik.txt","r+")
#f.write("Hello\n")
#f.write("Hello2\n")
#f.write("Hello3\n")

#print(f.readlines())

for line in f.readlines():
    print(line, end='')
    print(line.rstrip())
f.close()

linia = "\n   sde    \n\n  fdf ".rstrip()
print (linia,"\n")
print ("dodatek")
print ("Start")
print ("dodatek",end="")
print ("Stop")
print ("dodatek")