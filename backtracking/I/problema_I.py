tabuleiro = [[0 for _ in range(8)] for _ in range(8)]
visitados = [[0 for _ in range(8)] for _ in range(8)]
 
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x, y = map(str, input().split())


#ultima jogada, veio da horizontal ou vertical?
def backtracking(x, y, final, visitados):

   
    
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return float('inf')
    
    if visitados[x][y] != 0:
        return float('inf')
    

    if (x, y) == final:
        return 0
    
    else:

        visitados[x][y] = -1
        lista = []
        lista.append(1 + backtracking(x - 2, y + 1, final, visitados))
        lista.append(1 + backtracking(x - 2, y - 1, final, visitados))
        lista.append(1 + backtracking(x - 1, y + 2, final, visitados))
        lista.append(1 + backtracking(x + 2, y - 1, final, visitados))
        lista.append(1 + backtracking(x + 2, y + 1, final, visitados))
        lista.append(1 + backtracking(x - 1, y - 2, final, visitados))
        lista.append(1 + backtracking(x + 1, y - 2, final, visitados))
        lista.append(1 + backtracking(x + 1, y + 2, final, visitados))
            




    return min(lista)



inicio = (8 - int(x[1:2]), dicionario[x[:1]]-1)
final = (8 - int(y[1:2]), dicionario[y[:1]]-1)


print(backtracking(inicio[0], inicio[1], final,  visitados))










