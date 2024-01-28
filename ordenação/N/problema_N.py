n = int(input())

maior = float("-inf")
menor = float("inf")
for i in range(n):
    s = int(input())
    if s > maior:
        maior = s
    elif s < menor:
        menor = s

print(maior - menor)