import unittest

def is_older(age):
  if age >= 18:
    return True
  else:
    return False


class GlassTest(unittest.TestCase):
  def test_is_older(self):
    age = 20

    result = is_older(age)
    self.assertEqual(result, True)

  def test_is_younger(self):
    age = 17

    result = is_older(age)
    self.assertEqual(result, False)


if __name__ == '__main__':
  unittest.main()