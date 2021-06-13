import unittest

def sum(num_1, num_2):
  return num_1 + num_2


def subtract(num_1, num_2):
  return num_1 - num_2

class BlackBoxTest(unittest.TestCase):
  def test_sum_two_positives(self):
    num_1 = 10
    num_2 = 5

    result = sum(num_1, num_2)
    self.assertEqual(result, 15)

  def test_subtract_two_positives(self):
    num_1 = 10
    num_2 = 5

    result = subtract(num_1, num_2)
    self.assertEqual(result, 5)  


if __name__ == '__main__':
  unittest.main()