#Definiëren van een class
class Location:
#Functie Definiëren
    def __init__(self, name, country):
        self.name = name
        self.country = country
        
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " +
self.country + ".")

 
#Variabele loc declareren.
loc = Location("Your_Name", "Your_Country")

#Locatienaam printen
print(loc.name)
print(loc.country)

#Tonen van het datatype
print(type(loc))

