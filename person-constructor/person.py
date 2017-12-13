# part 1
# Create a Person class with a constructor
# that requires two arguments, the first_name and the last_name 
# of the person.

class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
  
  # full_name is an instance method that string interpolates the two instance variables first_name and last_name:
  def full_name(self):
    return "{} {}".format(self.first_name, self.last_name)

person = Person("John", "Doe")
print("Person, Part 1:", person.full_name())

# part 2
# Modify your Person class constructor so that it takes one or two arguments. 
# If I specify one argument, assume the person's entire name is specified. 
# If I specify two arguments, assume the first_name and last_name are specified.

class Person2:
  def __init__(self, first_name, last_name = False):
    self.first_name = first_name
    self.last_name = last_name

  def full_name(self):
    # I am using ternary here just to see how it looks/feels. The following would also work fine:
    #   if self.last_name:
    #     return "{} {}".format(self.first_name, self.last_name)
    #   else:
    #     return self.first_name
    # Ternary:
    return "{} {}".format(self.first_name, self.last_name) if self.last_name else self.first_name

person2 = Person2("John Doe")
person2withTwoArgs = Person2("John", "Doe")
print("Person, Part 2 with one arg, expecting 'John Doe':", person2.full_name())
print("Person, Part 2 with two args, expecting 'John Doe':", person2withTwoArgs.full_name())

# part 3
# As an extra challenge, modify your constructor so that it can support one, two, 
# or three arguments, with the last argument being an optional middle_name. 
# Modify the case where if one argument is supplied, your constructor attempts to 
# figure out the first name, last name, and middle name.

class Person3:
  def __init__(self, first_name, last_name = False, middle_name = False):
    if not last_name and not middle_name:
      full_name_array = first_name.split(" ")
      self.first_name = full_name_array[0]

      if len(full_name_array) == 3:
        self.middle_name = full_name_array[1]
        self.last_name = full_name_array[2]
      elif len(full_name_array) == 2:
        self.middle_name = False
        self.last_name = full_name_array[1]

    else:
      self.first_name = first_name
      self.last_name = last_name
      self.middle_name = middle_name
  
  def full_name(self):
    names = list(filter(lambda x: x != False, [self.first_name, self.middle_name, self.last_name]))
    return (" ").join(names)

person3withOneArg = Person3("John Doe")
person3withTwoArgs = Person3("John", "Doe")
person3withThreeArgs = Person3("John", "Doe", "Jacob")
print("Person, Part 3 with one arg, expecting 'John Doe':", person3withOneArg.full_name())
print("Person, Part 3 with two args, expecting 'John Doe':", person3withTwoArgs.full_name())
print("Person, Part 3 with three args, expecting 'John Jacob Doe':", person3withThreeArgs.full_name())