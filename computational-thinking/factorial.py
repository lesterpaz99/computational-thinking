# FACTORIAL USING RECURSION

def factorial(number):
    if (number == 0):
        return 1
    
    return number * factorial(number - 1)


def main():
    number = int(input("Introduce a number: "))
    print(f'{number}! = {factorial(number)}')


if __name__ == '__main__':
    main()