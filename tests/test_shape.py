import pytest
from shape import Shape

# 2
# Write

# different test cases inserted here: the diff test cases are defined as a list of tuples

class TestShape:
    @pytest.fixture
    def shape_instance(self):
        class TestShapeImpl(Shape):
            def area(self):
                return 0

            def perimeter(self):
                return 0

        return TestShapeImpl()

    def test_area(self, shape_instance):
        with pytest.raises(NotImplementedError):
            shape_instance.area()

    def test_perimeter(self, shape_instance):
        with pytest.raises(NotImplementedError):
            shape_instance.perimeter()


class TestShape:
    @pytest.fixture
    def shape_instance(self):
        class TestShapeImpl(Shape):
            def area(self):
                return 0

            def perimeter(self):
                return 0

        return TestShapeImpl()

    def test_area(self, shape_instance, capsys):
        shape_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 0" in captured.out

    def test_perimeter(self, shape_instance, capsys):
        shape_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 0" in captured.out

# test_shape.py
import pytest
from shape import Shape
from triangle import Triangle
from square import Square
from rectangle import Rectangle

class TestShape:
    @pytest.fixture
    def triangle_instance(self):
        return Triangle(base=3, height=4, side1=5, side2=5, side3=5)

    @pytest.fixture
    def square_instance(self):
        return Square(side=4)

    @pytest.fixture
    def rectangle_instance(self):
        return Rectangle(length=5, width=6)

    def test_triangle_area(self, triangle_instance, capsys):
        triangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 6.0" in captured.out

    def test_triangle_perimeter(self, triangle_instance, capsys):
        triangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 15" in captured.out

    def test_square_area(self, square_instance, capsys):
        square_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 16" in captured.out

    def test_square_perimeter(self, square_instance, capsys):
        square_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 16" in captured.out

    def test_rectangle_area(self, rectangle_instance, capsys):
        rectangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 30" in captured.out

    def test_rectangle_perimeter(self, rectangle_instance, capsys):
        rectangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 22" in captured.out

# test_shape.py
import pytest
from shape import Shape
from triangle import Triangle
from square import Square
from rectangle import Rectangle

class TestShape:
    @pytest.fixture
    def triangle_instance(self):
        return Triangle(base=3, height=4, side1=5, side2=5, side3=5)

    @pytest.fixture
    def square_instance(self):
        return Square(side=4)

    @pytest.fixture
    def rectangle_instance(self):
        return Rectangle(length=5, width=6)

    def test_triangle_area(self, triangle_instance, capsys):
        triangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 6.0" in captured.out

    def test_triangle_perimeter(self, triangle_instance, capsys):
        triangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 15" in captured.out

    def test_square_area(self, square_instance, capsys):
        square_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 16" in captured.out

    def test_square_perimeter(self, square_instance, capsys):
        square_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 16" in captured.out

    def test_rectangle_area(self, rectangle_instance, capsys):
        rectangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 30" in captured.out

    def test_rectangle_perimeter(self, rectangle_instance, capsys):
        rectangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 22" in captured.out

    def test_new_square_area(self, capsys):
        new_square_instance = NewSquare(side=4)
        new_square_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 16" in captured.out

    def test_new_square_perimeter(self, capsys):
        new_square_instance = NewSquare(side=4)
        new_square_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 16" in captured.out

    def test_new_rectangle_area(self, capsys):
        new_rectangle_instance = NewRectangle(length=5, width=6)
        new_rectangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Area: 30" in captured.out

    def test_new_rectangle_perimeter(self, capsys):
        new_rectangle_instance = NewRectangle(length=5, width=6)
        new_rectangle_instance.display_info()
        captured = capsys.readouterr()
        assert "Perimeter: 22" in captured.out
