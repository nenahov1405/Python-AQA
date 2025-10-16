# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні
# для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу
# та периметр кожної.

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

class Rectangle(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

s1 = Square(2)
r1 = Rectangle(4, 5)
c1 = Circle(3)
print(s1.area())
print(r1.area())
print(c1.area())
print(s1.perimeter())
print(r1.perimeter())
print(c1.perimeter())
