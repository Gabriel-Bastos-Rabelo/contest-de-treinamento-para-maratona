import math

def divisores(n):
    divisores = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisores.append(i)
            if n//i not in divisores and i != 1:
                divisores.append(n//i)


    return divisores

n = int(input())

divisoresN = divisores(n)
soma = sum(divisoresN)

if soma == n:
    print("sim")
else:
    print("nao")

for i in range(2, n+1):
    divi = divisores(i)
    soma = sum(divi)
    if soma == i:
        print(i, end = " ")
