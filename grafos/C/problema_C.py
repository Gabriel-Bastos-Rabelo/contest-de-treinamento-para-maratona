n , m = map(int, input().split())

matriz = []

posicaoInicial = ()
achou = False
for i in range(n):
    lista = list(input())
    
    if achou == False:
        for j in range(len(lista)):
            if lista[j] == 'o':
                posicaoInicial = (i, j)
                achou = True
                break

    matriz.append(lista)

visited = set()
def backtracking(matriz, posicao):
    if posicao in visited:
        return
    if posicao[0] < 0 or posicao[0] >= n or posicao[1] < 0 or posicao[1] >= m:
        return
    
    matriz[posicao[0]][posicao[1]] = 'o'
    visited.add(posicao)
    
    if posicao[0] < n-1 and matriz[posicao[0] + 1][posicao[1]] == '#':
        backtracking(matriz, (posicao[0], posicao[1] + 1))
        backtracking(matriz, (posicao[0], posicao[1] - 1))

    else:
        backtracking(matriz, (posicao[0] + 1, posicao[1]))



backtracking(matriz, posicaoInicial)

for i in matriz:
    string = "".join(map(str, i))
    print(string)