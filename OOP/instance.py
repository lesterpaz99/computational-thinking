import math

class Coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, another_coordinate):
    x_diff = (self.x - another_coordinate.x)**2
    y_diff = (self.y - another_coordinate.y)**2

    return math.sqrt(x_diff + y_diff)


if __name__ == '__main__':
  coor_1 = Coordinates(2, 2)
  coor_2 = Coordinates(-2, -3)

  print(coor_1.distance(coor_2))
  print(isinstance(coor_1, Coordinates))