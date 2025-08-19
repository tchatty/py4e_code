#Definitions:
#Class - a template
#Attribute - a variable within a class
#Method - a function within a class
#Object - a particular instance of a class
#Constructor - code that runs when an object is created
#Inheritance - the ability to extend a class to make a new one

class PartyAnimal: #class is a reserved word that defines a template for making objects
    def __init__(self, z): #when an object is constructed, a specially named method is called to initialize and allocate attributes
        self.x = 0
        self.name = z
        #print("Constructed")
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)
        #print("So far", self.x)

class FootballFan(PartyAnimal): #derived class
    def __init__(self,nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points+=7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()
j = FootballFan("John")
j.party()
j.touchdown() #It has all the capabilities of Party Animal and more.

    # def __del__(self):
    #     print("Deleting", self.x)
# an = PartyAnimal() #construct a party animal object and store in an
# an.party() #tell the object to run the party() code within it
# # an.party()
# # an = 42
# print("an contains", an)
# print("Type", type(an))
# print("Dir", dir(an))
# print("Type", type(an.x))
# print("Type", type(an.party))

