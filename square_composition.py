# square.py
from shape import Shape
from area_perimeter_calculator import AreaCalculator, PerimeterCalculator

class Square(Shape):
    def __init__(self, side):
        self.side = side
        self.calculator = AreaPerimeterCalculator()

    def area(self):
        return self.calculator.calculate_area(self.side, self.side)

    def perimeter(self):
        return self.calculator.calculate_perimeter(self.side, self.side)
