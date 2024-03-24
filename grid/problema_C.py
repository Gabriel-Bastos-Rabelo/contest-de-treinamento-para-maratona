dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(matriz, i, j, visitados):
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz[0]):
        return

    if matriz[i][j] == "X":
        return

    if visitados[i][j] != -1:
        return

    visitados[i][j] = 1
    matriz[i][j] = 'T'
    for k in range(4):
        new_i = i + dy[k]
        new_j = j + dx[k]
        dfs(matriz, new_i, new_j, visitados)


while True:
    l, c = map(int, input().split())

    if l + c == 0:
        break

    matriz = []

    posicoes = []

    for i in range(l):
        lista = list(input())

        for index, j in enumerate(lista):
            if j == 'T':
                posicoes.append((i, index))

        matriz.append(lista)

    # chamar funcao

    visitados = [[-1 for i in range(len(matriz[0]))]
                 for j in range(len(matriz))]

    for i in posicoes:
        dfs(matriz, i[0], i[1], visitados)

    for i in matriz:
        print("".join(i))

    print()
