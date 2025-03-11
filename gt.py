class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Cat(Animal):
  def __init__(self, name, age, color, weight):
    super().__init__(name, age)
    self.color = color
    self.weight = weight

class Dog(Animal):
  def __init__(self, name, age, types):
   super().__init__(name.age)
   self.type = types