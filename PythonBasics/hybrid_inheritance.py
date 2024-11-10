class things:
    def display_things(self):
        print("im from things")

class Living_things(things):
    def display_lthings(self):
        print("im from living things")

class Non_living_things(things):
    def display_nthings(self):
        print("im from non living things")

class Mammal(Living_things):
    def display_mammal(self):
        print("Im a mammal")

class Elephant(Mammal):
    def elephant(self):
        print("im an elephant")


Guruvayoor_kesavan = Elephant()
Guruvayoor_kesavan.elephant()
Guruvayoor_kesavan.display_mammal()
Guruvayoor_kesavan.display_lthings()
Guruvayoor_kesavan.display_things()
print("\n")
animal = Living_things()
chair = Non_living_things()

animal.display_things()
animal.display_lthings()
chair.display_things()
chair.display_nthings()