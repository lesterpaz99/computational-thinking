import time
import sys

def factorial(n):
  result = 1

  while (n > 1):
    result *= n
    n -= 1

    return result

def recursive_factorial(n):
  if n == 1:
    return 1
  else:
    return n * recursive_factorial(n - 1)


if __name__ == "__main__":
  n = 10000
  print(sys.getrecursionlimit())
  sys.setrecursionlimit(n + 10)
  print(sys.getrecursionlimit())

  start = time.time()
  factorial(n)
  final = time.time()
  print(final - start)


  start = time.time()
  recursive_factorial(n)
  final = time.time()
  print(final - start)