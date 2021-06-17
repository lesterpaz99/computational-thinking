class Rectangle:
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return self.base * self.height


class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)


if __name__ == '__main__':
  my_rectangle = Rectangle(3, 4);
  print(my_rectangle.area())
  
  my_square = Square(2)
  print(my_square.area())