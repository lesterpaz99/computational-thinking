class Car:
  def __init__(self, color, model='s', brand='Tesla'):
    self.model = model
    self.brand = brand
    self.color = color
    self.gasoline = 500
    self._state = 'off'
    self._engine = Engine(4)

  def start(self):
    self._engine._temperature = 10
    self.gasoline -= 2
    self._state = 'on'

  def turn_off(self):
    self._state = 'off'

  def move_backward(self):
    self._state = 'Moving backward'

  def move_forward(self):
    self._state = 'Moving forward'

  def stop(self):
    self._state = 'in parking'

  def speed_up(self, type_speed):
    if type_speed == 'fast':
      self._engine.inject_gasoline(10)
      self.gasoline -= 10
    else:
      self.slow_down()
    self._state = 'Moving forward'

  def slow_down(self):
    self._engine.inject_gasoline(3)
    self.gasoline -= 5

class Engine:
  def __init__(self, cylinders, type_engine='gasoline'):
    self.cylinders = cylinders
    self.type_engine = type_engine
    self._temperature = 0

  def inject_gasoline(self, amount):
    pass


def run():
  my_car = Car('gray')

  print(my_car.gasoline)
  print(my_car._state)
  print(my_car.start())
  print(my_car._state)
  print(my_car.move_forward())
  print(my_car._state)
  print(my_car.speed_up('fast'))
  print(my_car._state)
  print(my_car.slow_down())
  print(my_car._state)
  print(my_car.stop())
  print(my_car._state)
  print(my_car.turn_off())
  print(my_car._state)


if __name__ == '__main__':
  run()
