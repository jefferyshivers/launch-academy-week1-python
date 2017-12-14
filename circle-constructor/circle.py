# part 1
# Create a Circle class with a constructor that requires a single argument. 
# This argument should be the radius of the circle.

class Circle:
  def __init__(self, radius):
    self.radius = radius

circle = Circle(10)
print("circle, expecting '10' (radius):", circle.radius)

# part 2
# Create a completely different version of your Circle class that requires 
# a single argument. This time, allow the developer to specify whether the 
# value supplied is the diameter or the radius of the circle. 
# You should only store the Circle's radius.

class Circle2:
  def __init__(self, size = {}):
    if "radius" in size:
      self.radius = size["radius"]
    elif "diameter" in size:
      self.radius = size["diameter"] / 2
    else:
      self.radius = False

circle2withRadius = Circle2({"radius": 10})
circle2withDiameter = Circle2({"diameter": 22})
circle2withNoArg = Circle2()
circle2withBadKey = Circle2({"bad": 3})

print("circle 2, with radius, expecting '10' (radius):", circle2withRadius.radius)
print("circle 2, with diameter, expecting '11' (radius):", circle2withDiameter.radius)
print("circle 2, with no arg, expecting 'False' (radius):", circle2withNoArg.radius)
print("circle 2, with bad key, expecting 'False' (radius):", circle2withBadKey.radius)

# part 3
# - ruby instructions -
#   Modify your constructor to make use of the kind_of? method. 
#   Your Circle class supports both setting a radius as the exclusive, 
#   numeric argument to the constructor and the ability to specify a diameter 
#   or radius as an option. This portion will combine the functionalities of 
#   both parts I and II.
# - python version -
#   Same as above, but using Python's type checking: type(arg) is int/dict

class Circle3:
  def __init__(self, size = {}):
    if type(size) is dict:
      if "radius" in size:
        self.radius = size["radius"]
      elif "diameter" in size:
        self.radius = size["diameter"] / 2
      else:
        self.radius = False
    elif type(size) is int:
      self.radius = size
    else:
      self.radius = False

circle3withDict = Circle3({"radius": 10})
circle3withInt = Circle3(6)
circle3withNoArg = Circle3()

print("circle 3, given '{radius: 10}', expecting '10' (radius):", circle3withDict.radius)
print("circle 3, given '6', expecting '6' (radius):", circle3withInt.radius)
print("circle 3, given no args, expecting 'False' (radius):", circle3withNoArg.radius)