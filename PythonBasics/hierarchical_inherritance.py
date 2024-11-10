class things:
    def display_things(self):
        print("im from things")

class Living_things(things):
    def display_lthings(self):
        print("im from living things")

class Non_living_things(things):
    def display_nthings(self):
        print("im from non living things")


animal = Living_things()
chair = Non_living_things()

animal.display_things()
animal.display_lthings()
chair.display_things()
chair.display_nthings()