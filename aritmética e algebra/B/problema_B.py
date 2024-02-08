import math
n = int(input())

for i in range(n):
    t, i, a = map(int, input().split())

    cont = 0
    valorAdicional = a
    while i < t:  
        i += valorAdicional
        valorAdicional += a
        cont += 1

    print(cont)


math.ceil(3.4)




