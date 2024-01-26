#Define class
class animal:

    #Initialization function gives class its attributes, with default values of cat
    def __init__(self, name="Cat", legs=4, arms=0, eyes=2, tail=True, fur=True):
        self.name = name
        self.legs = legs
        self.arms = arms
        self.eyes = eyes
        self.tail = tail
        self.fur = fur

    #describe function prints the information about it
    def describe(self):
        print(self.name, " has:")
        print(self.legs, " legs")
        print(self.arms, " arms")
        print(self.eyes, " eyes")
        if(self.tail):
            print("a tail")
        if(self.fur):
            print("and fur")
        print("\n")


#test instances
rat = animal("Rat", 4, 0, 2, True, True)
rat.describe()

squid = animal("Squid", 0, 10, 2, False, False)
squid.describe()

#test for the defaults
cat = animal()
cat.describe()
