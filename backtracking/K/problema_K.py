def backtracking(x, y, final, matriz):
    
    if not (0 <= x < len(matriz) and 0 <= y < len(matriz)):
        return 0
    
    if matriz[x][y] != 0:
        return 0

    if (x, y) == final:
        return 1
    
    
    matriz[x][y] = -1

    if (x < len(matriz)-1 and backtracking(x+1, y, final, matriz)) or \
       (y < len(matriz)-1 and backtracking(x, y+1, final, matriz)) or \
       (x > 0 and backtracking(x-1, y, final, matriz)) or \
       (y > 0 and backtracking(x, y-1, final, matriz)):
        return 1

    

    return 0

# Leitura da entrada
n = int(input())
for _ in range(n):
    t = int(input())
    matriz = [list(map(int, input().split())) for _ in range(t)]

    # Chamada da função de backtracking
    print(backtracking(0, 0, (t-1, t-1), matriz))
