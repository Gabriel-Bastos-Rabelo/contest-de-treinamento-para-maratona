lista = list(map(int, input().split()))

dicionario = { 1:"A", 11:"J", 12:"Q",  13:"K"}

lista.sort()

for index, i in enumerate(lista):
    if i in dicionario:
        if index == len(lista)-1:
            print(dicionario[i])
        else:
            print(dicionario[i], end = " ")
    else:
        if index == len(lista)-1:
            print(i)
        else:
            print(i, end = " ")
        