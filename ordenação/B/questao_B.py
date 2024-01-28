qtd = int(input())
distancias = {}
for i in range(qtd):
    x, y = input().split(" ")
    x2 = int(x)
    y2 = int(y)

    distancia = (x2**2 + y2**2)**0.5
    distancias[f"{x} {y}"] = distancia

for k in sorted(distancias, key=distancias.get):
    print(k)
