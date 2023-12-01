# rectangle.py
from shape import Shape
from area_perimeter_calculator import AreaCalculator, PerimeterCalculator

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.calculator = AreaPerimeterCalculator()

    def area(self):
        return self.calculator.calculate_area(self.length, self.width)

    def perimeter(self):
        return self.calculator.calculate_perimeter(self.length, self.width)
