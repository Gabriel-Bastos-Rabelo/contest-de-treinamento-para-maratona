lista = list(map(int, input().split()))

memo = [float('-inf')] * (len(lista) + 1)

memo[0] = lista[0]
maiorValor = float('-inf')

for i in range(1, len(lista)):
    valor = max(lista[i], lista[i] + memo[i - 1])


    memo[i] = valor

    if valor > maiorValor:
        maiorValor = valor

print(maiorValor)