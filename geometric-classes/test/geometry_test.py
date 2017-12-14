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


# class TestSquareClass(unittest.TestCase):
#     def test_init(self):
#         square = Square(5)



if __name__ == '__main__':
    unittest.main()