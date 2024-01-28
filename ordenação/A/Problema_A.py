n = int(input())

lista = []
for i in range(n):
    s = input()
    lista.append(s)



for i in range(n):
    menor = i
    for j in range(i+1, n):
        if len(lista[j]) < len(lista[menor]):
            menor = j

        elif len(lista[j]) == len(lista[menor]):
            for k in range(min(len(lista[j]), len(lista[menor]))):
                if lista[j][k] < lista[menor][k]:
                    menor = j
                elif lista[j][k] > lista[menor][k]:
                    break
                else:
                    continue

    lista[i], lista[menor] = lista[menor], lista[i]


for i in lista:
    print(i)
