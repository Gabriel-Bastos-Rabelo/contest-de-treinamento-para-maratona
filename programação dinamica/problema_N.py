n, k = map(int, input().split())

arabica = list(map(int, input().split()))
conilon = list(map(int, input().split()))

kilo = 0

atual = 1
while True:
    valor = 0
    for i in arabica:
        valor += (i * atual)

    for i in conilon:
        valor += (i * atual)

    if valor >= k:
        break

    atual += 1
    kilo += 1


print(kilo)
        