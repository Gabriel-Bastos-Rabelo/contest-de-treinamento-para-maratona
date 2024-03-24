import sys

sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



def valida(i, j, matriz):
    if i < 0 or i>= len(matriz) or j < 0 or j >= len(matriz[0]):
        return False
    
    return True 

def dfs(matriz, i, j, visitados):
    visitados[i][j] = 1
    
    for k in range(4):
        new_i = i + dy[k]
        new_j = j + dx[k]
        
        if 0 <= new_i < len(matriz) and 0 <= new_j < len(matriz[0]) and matriz[new_i][new_j] == 1 and visitados[new_i][new_j] == -1:
            return dfs(matriz, new_i, new_j, visitados)
    

    return i+1, j+1




    

            

l, c = map(int, input().split())

xInicio, yInicio = map(int, input().split())

xInicio, yInicio = xInicio - 1, yInicio - 1
matriz = []



for i in range(l):
    lista = list(map(int, input().split()))
    matriz.append(lista)

visitados = [[-1 for i in range(c)]
                 for j in range(l)]



res = dfs(matriz, xInicio, yInicio, visitados)
print(res[0], res[1])




