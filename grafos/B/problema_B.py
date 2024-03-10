n, c = map(int, input().split())


g = {node: [] for node in range(1, n + 1)}
for i in range(c):
    lista = list(map(int, input().split()))
    infectante = lista[0]
    cadeia = lista[2:]
    for j in cadeia:
        if j not in g:
            g[j] = []
        g[j].append(infectante)


for i in g:
    if len(g[i]) == 0:
        print(i)
        break

