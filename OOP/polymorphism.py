class Person:
  def __init__(self, name_person):
    self.name = name_person

  def move_forward(self):
    print('I\'m walking')


class Cyclist(Person):
  def __init__(self, name):
    super().__init__(name)

  def move_forward(self):
    print('I\'m cycling')


def main():
  obed = Person('Obed')
  obed.move_forward()

  katy = Cyclist('Katy')
  katy.move_forward()



if __name__ == '__main__':
  main()