votos = {}
qtd = int(input())

for i in range(qtd):
    voto = input()
    if voto not in votos:
        votos[f"{voto}"] = 1
    else:
        votos[f"{voto}"] += 1


for i in sorted(votos, key=votos.get, reverse=True):
    print(i)
