import math

def f(x):
  result = 0

  for i in range(1000):
    result += 1

  for i in range(x):
    result += x

  for i in range(x):
    for j in range(x):
      result += 1
      result += 1
  
  return result

def d(n):
  for i in range(n):
    print('\n')
    for j in range(n):
      print(i, j)

def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    return fibonacci(n-1) + fibonacci(n-2)

def num(n):
    return 1

def logarithm(n):
    return math.log10(n)

def lineal(n):
    return n

def n_logarithm(n):
    return n * math.log10(n)

def square(n):
    return n**2

def exponential(n):
    return 2**n


if __name__ == "__main__":
  n = [10, 100, 1000, 1000000]
  i = 0

  for numbers in n:
    print(num(n[i]))
    print(logarithm(n[i]))
    print(lineal(n[i]))
    print(n_logarithm(n[i]))
    print(square(n[i]))
    print(exponential(n[i]))
    print('\n')
    i+=1

