# part 1
# Create a Person class with a constructor
# that requires two arguments, the first_name and the last_name 
# of the person.

class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

person = Person("John", "Doe")
print(person.first_name, person.last_name)

