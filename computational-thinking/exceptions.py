def divide_list_elements(list_p, divider):
  try:
   return [i / divider for i in list_p]
  except ZeroDivisionError as error:
    print(error);
    return list_p

def run():
  our_list = list(range(10))
  divider = 0

  print(divide_list_elements(our_list, divider))


if __name__ == '__main__':
  run()