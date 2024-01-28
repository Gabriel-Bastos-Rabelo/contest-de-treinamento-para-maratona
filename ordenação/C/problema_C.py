n = int(input())

lista = list(map(int, input().split()))

impares = []
pares = []

for i in lista:
    if i % 2 != 0:
        impares.append(i)
    else:
        pares.append(i)

impares.sort()
pares.sort()

for i in impares:
    print(i, end=" ")

for index, j in enumerate(pares):
    if index < len(pares)-1:
        print(j, end = " ")
    else:
        print(j)
