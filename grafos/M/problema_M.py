n, k = map(int, input().split())

lista = list(map(int, input().split()))

lista.sort()

maior = lista[len(lista) - 1]
segundoMaior = lista[len(lista) - 2]

res = 0
soma = 0
while True:
    if soma >= k:
        break
    if res % 2 == 0:
        soma += maior
    else:
        soma += segundoMaior

    res += 1

print(res)



