import random

def merge_sort(list_p):
  if len(list_p) > 1:
    middle = len(list_p) // 2
    left = list_p[:middle]
    right = list_p[middle:]
    print(left, '*' * 5, right)

    #recursive call each middle
    merge_sort(left)
    merge_sort(right)

    #Iteraror to run every sub-list_size
    i = 0
    j = 0

    #iterator for main list
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        list_p[k] = left[i]
        i += 1
      else:
        list_p[k] = right[j]
        j += 1

      k += 1

    while i < len(left):
      list_p[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      list_p[k] = right[j]
      j += 1
      k += 1

    print(f'left {left}, right {right}')
    print(list_p)
    print('-' * 50)

  return list_p


if __name__ == '__main__':
  list_size = int(input("What size will be the list? "))

  my_list = [random.randint(1, 100) for i in range(list_size)]
  print(my_list)
  print('-' * 30)

  sorted_list = merge_sort(my_list)
  print(sorted_list)

  