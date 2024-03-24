import math

n = int(input())
matriz = []

for i in range(n):
    matriz.append(list(map(int, input().split())))


soma1 = 0
soma2 = 0

for i in range(n):
    soma1 += matriz[i][i]
    soma2 += matriz[i][n - i - 1]


print(abs(soma1 - soma2))