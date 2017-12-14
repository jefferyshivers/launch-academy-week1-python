import unittest
from geometry.square import Square
from geometry.circle import Circle


class TestCircleClass(unittest.TestCase):

    def test_init(self):
        circle = Circle(5)
        self.assertIsInstance(circle, Circle)
    
    def test_instance_variables(self):
        circleWithNoCoordinatesGiven = Circle(6)
        self.assertEqual(circleWithNoCoordinatesGiven._radius, 6)
        self.assertEqual(circleWithNoCoordinatesGiven._x, 0)
        self.assertEqual(circleWithNoCoordinatesGiven._y, 0)

        circleWithCoordinatesGiven = Circle(7, {'x': 11, 'y': 22})
        self.assertEqual(circleWithCoordinatesGiven._radius, 7)
        self.assertEqual(circleWithCoordinatesGiven._x, 11)
        self.assertEqual(circleWithCoordinatesGiven._y, 22)

    def test_radius(self):
        circle = Circle(2)
        self.assertEqual(circle.radius(), 2)

    def test_x(self):
        circle = Circle(1, {'x': 8, 'y': 4})
        self.assertEqual(circle.x(), 8)

    def test_y(self):
        circle = Circle(1, {'x': 7, 'y': 3})
        self.assertEqual(circle.y(), 3)

    def test_diameter(self):
        circle = Circle(13)
        self.assertEqual(circle.diameter(), 26)
    
    def test_area(self):
        circle = Circle(2)
        # area = pi * (2 ** 2) = ~12.57
        self.assertEqual(round(circle.area(), 2), 12.57)

    def test_perimeter(self):
        circle = Circle(3)
        # perimeter = 2 * pi * 3 = ~18.85
        self.assertEqual(round(circle.perimeter(), 2), 18.85)


class TestSquareClass(unittest.TestCase):
    def test_init(self):
        square = Square(5)
        self.assertIsInstance(square, Square)
    
    def test_instance_variables(self):
        squareWithNoCoordinatesGiven = Square(5)
        self.assertEqual(squareWithNoCoordinatesGiven.x(), 0)
        self.assertEqual(squareWithNoCoordinatesGiven.y(), 0)

        squareWithCoordinatesGiven = Square(5, {'x': 3, 'y': 4})
        self.assertEqual(squareWithCoordinatesGiven.x(), 3)
        self.assertEqual(squareWithCoordinatesGiven.y(), 4)

    def test_x(self):
        square = Square(4, {'x': 1, 'y': 2})
        self.assertEqual(square.x(), 1)

    def test_y(self):
        square = Square(4, {'x': 4, 'y': 5})
        self.assertEqual(square.y(), 5)

    def test_length(self):
        square = Square(3)
        self.assertEqual(square.length(), 3)

    def test_width(self):
        square = Square(4)
        self.assertEqual(square.width(), 4)   

    def test_diameter(self):
        square = Square(7)
        # diameter = sqrt(2 * (7 ** 2)) = sqrt(98) = ~9.9
        self.assertEqual(round(square.diameter(), 1), 9.9)

    def test_area(self):
        square = Square(3)
        self.assertEqual(square.area(), 9)
    
    def test_perimeter(self):
        square = Square(5)
        self.assertEqual(square.perimeter(), 20)
    
    def test_contains_point(self):
        squareWithNoCoordinatesGiven = Square(4)
        self.assertEqual(squareWithNoCoordinatesGiven.contains_point(0, 0), True)
        self.assertEqual(squareWithNoCoordinatesGiven.contains_point(2, -2), True)
        self.assertEqual(squareWithNoCoordinatesGiven.contains_point(3, 0), False)

        squareWithCoordinatesGiven = Square(6, {'x': 1, 'y': 3})
        self.assertEqual(squareWithCoordinatesGiven.contains_point(1, 3), True)
        self.assertEqual(squareWithCoordinatesGiven.contains_point(4, 0), True)
        self.assertEqual(squareWithCoordinatesGiven.contains_point(-3, 0), False)   


if __name__ == '__main__':
    unittest.main()