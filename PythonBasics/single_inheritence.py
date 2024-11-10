class Animal():
    def sound(self):
        print("Animal makes sound")


class dog(Animal):
    def speak(self):
        print("bow bow")


jimmy = dog()
jimmy.sound()
jimmy.speak()