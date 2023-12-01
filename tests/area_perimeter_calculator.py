# area_perimeter_calculator.py
class AreaCalculator:
    @staticmethod
    def calculate_area(length, width):
        return length * width

class PerimeterCalculator:
    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)
