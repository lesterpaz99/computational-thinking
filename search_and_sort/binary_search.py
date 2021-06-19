import random


def binary_search(list_p, start, end, target, steps = 0):
  print(f'Looking for {target} between {list_p[start]} and {list_p[end]}')

  if start > end:
    return {'found': False, 'steps': steps}
  
  medio = (start + end) // 2

  if list_p[medio] == target:
    steps += 1
    return {'found': True, 'steps': steps}
  elif list_p[medio] < target:
    steps += 1
    return binary_search(list_p, medio + 1, end, target, steps)
  else:
    steps += 1
    return binary_search(list_p, start, medio - 1, target, steps)


if __name__ == '__main__':
  list_size = int(input("What size will be the list? "))
  target = int(input('What number are u looking for? '))

  my_list = sorted([random.randint(1, 100) for i in range(list_size)])

  found = binary_search(my_list, 0, len(my_list)-1, target)

  print(my_list)
  print(found)