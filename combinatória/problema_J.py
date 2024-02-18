import math

n = int(input())

res = []

repMedica = n * 37/100


n -= repMedica
n = int(n)

res.append(n)

nAssumem = n * 20/100

n -= nAssumem
n = int(n)

res.append(n)

n = int(n)

cabos = int(n * 30/100)
sargentos = int(n * 5/100)


combinacoes = int(math.factorial(cabos + sargentos)/(math.factorial((cabos + sargentos) - 8)))

res.append(combinacoes)

print(res)

