import math


# Абстрактный класс Фигура
class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass

    def compare_area(self, other):
        if self.area() > other.area():
            return "мой площади больше"
        elif self.area() < other.area():
            return "мой площади меньше"
        else:
            return "площади равны"

    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return "мой периметр больше"
        elif self.perimeter() < other.perimeter():
            return "мой периметр меньше"
        else:
            return "периметры равны"


# Класс Квадрат наследуется от Фигура
class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Класс Прямоугольник наследуется от Фигура
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Класс Треугольник наследуется от Фигура
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        return math.sqrt(
            semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Класс Круг наследуется от Фигура
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Пример использования
square = Square(4)
rectangle = Rectangle(3, 4)
triangle = Triangle(3, 4, 5)
circle = Circle(5)

print(square.area())  # Площадь квадрата
print(square.perimeter())  # Периметр квадрата
print(square.compare_area(rectangle))  # Сравнение площади квадрата и прямоугольника
print(square.compare_perimeter(rectangle))  # Сравнение периметра квадрата и прямоугольника