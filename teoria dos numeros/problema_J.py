import math


def divisores_primos(n):
    aux = n
    divisores_primos = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if (aux % i == 0):
            divisores_primos.append(i)
            while (aux % i == 0):
                aux = aux//i

    if aux != 1:
        divisores_primos.append(aux)

    return divisores_primos


n = int(input())

divi = divisores_primos(n)



if len(divi) == 2:
    if divi[0] * divi[1] == n:
        print(1)
    else:
        print(0)
else:
    if len(divi) == 1:
        if divi[0] ** 2 == n:
            print(1)
        else:
            print(0)
    else:
        print(0)

