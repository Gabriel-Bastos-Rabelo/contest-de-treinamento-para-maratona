n, m = map(int, input().split())

matriz = []
visitados = []
for i in range(n):
    visitados.append([0] * m)
    aux = list(map(int, input().split()))
    matriz.append(aux)
    for index, j in enumerate(aux):
        if j == 2:
            inicio = (i, index)
        elif j == 3:
            final = (i, index)


def backtracking(matriz, visitados, x, y, final):
    
    
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]):
        return float('inf')
    
    if visitados[x][y] != 0:
        return float('inf')
    
    if matriz[x][y] == 0:
        return float('inf')
    
    if (x, y) == final:
        return 1
    
    visitados[x][y] = -1
    return min((1 + backtracking(matriz, visitados, x + 1, y, final)), (1 + backtracking(matriz, visitados, x - 1, y, final)), (1 + backtracking(matriz, visitados, x, y + 1, final)), (1 + backtracking(matriz, visitados, x, y - 1, final)))


    
print(backtracking(matriz, visitados, inicio[0], inicio[1], final))
    
    


