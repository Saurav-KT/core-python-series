from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        # Method to calculate the area
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width= width
        self.height= height

    def area(self):
        return self.width* self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example Usage
circle = Circle(5)
print("Circle Area:", circle.area())          # Output: 78.5
print("Circle Perimeter:", circle.perimeter())  # Output: 31.4

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())          # Output: 24
print("Rectangle Perimeter:", rectangle.perimeter())  # Output: 20
