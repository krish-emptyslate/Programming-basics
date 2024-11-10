from abc import ABC



class shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
       return 3.14 * self.radius ** 2 #area of circle formula

    def perimeter(self):
        return 2*3.14 * self.radius

class Rectangle(shape):
    def __init__(self,length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length+self.width)


laptop = Rectangle(4,5)
print("area of laptop = ",laptop.area())
print("perimeter of a laptop = ",laptop.perimeter())

coin = Circle(5)
print("area of a coin =",coin.area())
print("perimeter of a circle =",coin.perimeter())


