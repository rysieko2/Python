import datetime

class Parent():


        def __init__(self):
            print("Parent 1-init")
            #teraz = datetime.datetime.now()
            f = open("plik.txt", "a")
            f.write("Import Klasy Parent: ")
            f.write(str(datetime.datetime.now()))
            f.write("\n")
            f.close()

        def parent(self):
            print("Parent 1-parent")

        def poke(self):
            print("Parent 1-poke")



class Child(Parent):

        def __init__(self):
            super().parent()
            print("Child 2-init")

        def poke(self):
            print("Child 2-poke przed")
            #super().poke()
            #print("Child 2-poke po")

#print (datetime.datetime.now())

o = Parent()

o.parent()


#o.poke()









# klasa.poke()

#par = Child()

#Child.poke()
#child.poke()
#child.parent()





