from abc import ABC, abstractmethod
import math
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

    def get_side(self):
        return self.__side

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_sides(self):
        return self.__width, self.__height


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def get_radius(self):
        return self.__radius

figures = [Square(2), Rectangle(4, 5), Circle(3)]

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Площа = {figure.area():.2f}")
    print(f"  Периметр = {figure.perimeter():.2f}")
    print("-" * 20)