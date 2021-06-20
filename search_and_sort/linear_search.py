import random

def linear_search(list_p, target, steps = 0):
  match = {'found': False, 'steps': steps}

  for element in list_p: # O(n)
    steps += 1
    if element == target:
      match = {'found': True, 'steps': steps}
      break
  
  return match


if __name__ == '__main__':
  list_size = int(input("What size will be the list? "))
  target = int(input('What number are u looking for? '))

  my_list = [random.randint(1, 100) for i in range(list_size)]

  found = linear_search(my_list, target)

  print(my_list)
  print(found)