lista = list(map(int, input().split()))

lista1 = sorted(lista)
lista2 = sorted(lista, reverse=True)


for index, i in enumerate(lista1):
    if index == len(lista1) - 1:
        print(i)
    else:
        print(i, end=" ")

for index, i in enumerate(lista2):
    if index == len(lista1) - 1:
        print(i)
    else:
        print(i, end=" ")


