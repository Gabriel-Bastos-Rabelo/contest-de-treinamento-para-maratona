dicionario = {}
n = int(input())

for i in range(n):
    s = int(input())
    if s in dicionario:
        dicionario[s] += 1
    else:
        dicionario[s] = 1

lista = []

for i in dicionario:
    lista.append([i, dicionario[i]])

lista.sort(reverse=True, key=lambda x: x[1])

min = lista[0][1]


for i in range(len(lista)):
    if lista[i][1] != min:
        break
    menor = i
    for j in range(i+1, len(lista)):
        if lista[j][1] != min:
            break
        if lista[j][0] > lista[menor][0]:
            menor = j

    lista[i], lista[menor] = lista[menor], lista[i]




print(lista[0][0], lista[0][1])