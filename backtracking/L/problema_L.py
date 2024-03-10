

lista = list(map(int, input().split()))

lista.sort()


dicionario = {}

for i in lista:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1




for j in dicionario:
    print(j, dicionario[j])

