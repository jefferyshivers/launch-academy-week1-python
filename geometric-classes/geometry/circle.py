from math import pi

class Circle:
  def __init__(self, radius, coordinates = {'x': 0, 'y': 0}):
    self._radius = radius
    self._x = coordinates['x']
    self._y = coordinates['y']

  def radius(self):
    return self._radius

  def x(self):
    return self._x

  def y(self):
    return self._y

  def diameter(self):
    return self._radius * 2

  def area(self):
    return pi * (self._radius ** 2)

  def perimeter(self):
    return 2 * pi * self._radius