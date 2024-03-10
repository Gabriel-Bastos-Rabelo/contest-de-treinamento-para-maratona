n = int(input())
lista = list(map(int, input().split()))

def backtracking(lista, posicao, visited):
    if posicao in visited:
        return float('inf')
    if posicao < 0 or posicao >= len(lista):
        return float('inf')
    
    if lista[posicao] == 0:
        return 0
    
    visited.add(posicao)
    
    res = min(1 + backtracking(lista, posicao + 1, visited), 1 + backtracking(lista, posicao - 1, visited))

    return res

res = []
for index, i in enumerate(lista):
    visited = set()
    res.append(backtracking(lista, index, visited))

for index, i in enumerate(res):
    if index == len(res)-1:
        print(i)
    else:
        print(i, end=" ")
    