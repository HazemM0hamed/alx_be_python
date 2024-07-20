import math
class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        return {self.lenght}*{self.widht}
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
