from math import sqrt

class Square:
  def __init__(self, side, center_coordinates = {'x': 0, 'y': 0}):
    self._side = side
    self._x = center_coordinates['x']
    self._y = center_coordinates['y']
  
  def x(self):
    return self._x

  def y(self):
    return self._y

  def length(self):
    return self._side

  def width(self):
    return self._side

  def diameter(self):
    return sqrt(2 * (self._side ** 2))

  def area(self):
    return self._side ** 2

  def perimeter(self):
    return self._side * 4

  def contains_point(self, x, y):
    half_length = self._side / 2
    left = self._x - half_length
    right = self._x + half_length
    top = self._y + half_length
    bottom = self._y - half_length

    return x >= left and x <= right and y <= top and y >= bottom
