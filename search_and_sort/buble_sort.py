import random


def bubble_sort(list_p):
  length = len(list_p)

  for i in range(length):
    for j in range(0, (length - i) - 1):
      if list_p[j] > list_p[j+1]:
        # temp = list_p[j+1]
        # list_p[j+1] = list_p[j]
        # list_p[j] = temp
        # Python is elegant:
        list_p[j], list_p[j+1] = list_p[j+1], list_p[j]
  
  return list_p


if __name__ == '__main__':
  list_size = int(input("What size will be the list? "))

  my_list = [random.randint(1, 100) for i in range(list_size)]

  print(my_list)

  my_sorted_list = bubble_sort(my_list)
  print(my_sorted_list)