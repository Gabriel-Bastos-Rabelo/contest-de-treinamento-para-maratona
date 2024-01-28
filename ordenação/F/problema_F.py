n = int(input())

lista = []

for i in range(n):
    a = list(input().split(","))

    a[1] = int(a[1])

    lista.append(a)

for i in range(n):
    menor = i
    for j in range(i+1, n):
        if lista[j][1] > lista[menor][1]:
            menor = j

        elif lista[j][1] == lista[menor][1]:
            
            
            for k in range(min(len(lista[j][0]), len(lista[menor][0]))):
                if lista[j][0][k] < lista[menor][0][k]:
                    menor = j
                    break
                elif lista[j][0][k] > lista[menor][0][k]:
                    break
                else:
                    continue

    lista[i], lista[menor] = lista[menor], lista[i]



for i in lista:
    print(i[0])
