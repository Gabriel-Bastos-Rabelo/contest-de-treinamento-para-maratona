n = int(input())

input()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j, final, visitados, matriz):
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz[0]):
        return False

    if matriz[i][j] == 1:
        return False
    
    if visitados[i][j] != -1:
        return False
    
    if (i, j) == final:
        return True
    
    visitados[i][j] = 1
    
    for k in range(4):
        new_i = i + dy[k]
        new_j = j + dx[k]
        if(dfs(new_i, new_j, final, visitados, matriz)):
            return True
        
    return False

    


for i in range(n):
    matriz = []

    for j in range(5):
        lista = list(map(int, input().split()))

        matriz.append(lista)

    
    visitados = [[-1 for i in range(5)]
                 for j in range(5)]
    
    if i != n - 1:
        input()
    
    if(dfs(0, 0, (4, 4), visitados, matriz)):
        print(1)
    else:
        print(0)
    

