import math

def ehPrimo(n):
    if n == 1:
        return False
    divisores = 1

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisores += 1
        if divisores > 1:
            return False
    return True

n = int(input())

for i in range(n):
    v = int(input())
    if v <= 3:
        print(0)
    elif v % 2 == 0:
        print(1)
    else:
        if ehPrimo(v - 2):
            print(1)
        else:
            print(0)






