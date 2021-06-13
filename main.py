#Binary search

def main():
  target = int(input('Choose a number: '))
  epsilon = 0.01
  lower_limit = 0.0
  higher_limit = max(1.0, target)
  answer = (higher_limit + lower_limit) / 2

  while abs(answer**2 - target) >= epsilon:
    if (answer**2 < target):
      lower_limit = answer
    else:
      higher_limit = answer

    answer = (higher_limit + lower_limit) / 2

  print(f'The square root of {target} is {answer}')


if __name__ == '__main__':
  main()