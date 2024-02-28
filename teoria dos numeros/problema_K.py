import math

def divisores_primos(n):
    aux = n
    divisores_primos = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if(aux % i == 0):
            divisores_primos.append(i)
            while(aux % i == 0):
                aux = aux//i

    if aux != 1:
        divisores_primos.append(aux)

    return divisores_primos



n = int(input())
divisoresN = divisores_primos(n)
res = 0
for i in range(1, n):
    divisoresI = divisores_primos(i)

   
    aux = set(divisoresN)
    aux2 = set(divisoresI)

    c = aux & aux2
    lista = list(c)
    if len(lista) == 0:
        res += 1

    
print(res)
    