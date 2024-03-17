resultados = []
while True:

    qtd = int(input())
    if qtd == 0:
        break
    sus = input().split(" ")
    sus = [int(i) for i in sus]
    suspeitos = [int(i) for i in sus]
    suspeitos.sort()
    resultados.append(sus.index(suspeitos[-2]) + 1)

for i in resultados:
    print(i)