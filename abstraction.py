#You cannot create an object in an abstract class
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Area of shape")

    @abstractmethod
    def perimeter(self):
        print("Perimeter of shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.142 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.142 * self.radius


circle1=Circle(radius=10)
print(circle1.area())
print(circle1.perimeter())