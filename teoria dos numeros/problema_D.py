import math

def ehInteressante(n):
    if ehPrimo(n) == False:
        return False
    else:
        somaDigitos = 0
        s = str(n)
        for i in s:
            somaDigitos += int(i)

        if ehPrimo(somaDigitos):
            return True
        return False



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



l ,r = map(int, input().split())



for i in range(l, r+ 1):
    if ehInteressante(i):
        print(i)
