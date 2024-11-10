class Animal():
    def sound(self):
        return "some sound"

class Dog(Animal):
    def sound(self):
        return "Barks"

class Cat(Animal):
    def sound(self):
        return "Meow Meow"

Tom = Cat()
print(f"tom says {Tom.sound()}")
Jack = Dog()
print(f"Jack {Jack.sound()}")
