n = int(input())

dicionario = {}
for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, b + 1):
        if j not in dicionario:
            dicionario[j] = 1
        else:
            dicionario[j] += 1

maior = 0
for i in dicionario:
    if dicionario[i] > maior:
        maior = dicionario[i]

print(maior)

    