import math

n = int(input())


def ehPrimo(n):
    if n == 1:
        return 0
    divisores = 1
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisores += 1
        if divisores > 1:
            return 0
    return 1


for i in range(n):
    numero = int(input())
    print(ehPrimo(numero))

