import math

n = int(input())
lista = list(map(int, input().split()))
res = 0

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


for i in lista:
    if ehPrimo(i):
        res += 1


print(res)
