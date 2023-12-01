# shape.py
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# shape.py
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in subclasses")

    def perimeter(self):
        raise NotImplementedError("Perimeter method must be implemented in subclasses")

    def display_info(self):
        print(f"Area: {self.area()}\nPerimeter: {self.perimeter()}")


# shape.py
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in subclasses")

    def perimeter(self):
        raise NotImplementedError("Perimeter method must be implemented in subclasses")

    def display_info(self):
        print(f"Area: {self.area()}\nPerimeter: {self.perimeter()}")
