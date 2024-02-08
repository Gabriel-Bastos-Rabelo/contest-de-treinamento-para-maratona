n = int(input())

for i in range(n):
    p, s = map(int, input().split())
    minimo = min(p, s)
    maximo = max(p, s)

    maior = 1
    for j in range(1, maximo):
        if p % j == 0 and s % j == 0:
            if j > maior:
                maior = j

    print(maior)