matriz = []
dicionario = {}

for i in range(10):
    lista = list(map(str, input().split()))
    matriz.append(lista)
    for index, j in enumerate(lista):
        if j not in dicionario:
            dicionario[j] = [(i, index)]
        else:
            dicionario[j].append((i, index))
    





def backtracking(matriz, current, x, y, string, indice, last):
    
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz):
        return False
    
    if "".join(current) == string:
        return True

    else:
        if matriz[x][y] != string[indice]:
            return False

        current.append(matriz[x][y])

        if last == "N":
            
            return backtracking(matriz, current, x, y - 1, string, indice + 1, "E") or backtracking(matriz, current, x, y + 1, string, indice + 1, "D")  or backtracking(matriz, current, x + 1, y, string,  indice + 1, "B") or backtracking(matriz, current, x - 1, y, string, indice + 1, "C")

        if last == "D":
            return backtracking(matriz, current, x, y + 1, string, indice + 1, "D")

        elif last == "E":
            return backtracking(matriz, current, x, y - 1, string, indice + 1, "E")

        elif last == "B":
            return backtracking(matriz, current, x + 1, y, string,  indice + 1, "B")

        elif last == "C":
            return backtracking(matriz, current, x - 1, y, string, indice + 1, "C")


           

    
      
      
      

while True:
  try:
    string = str(input())
    if string[0] in dicionario:
        achou = False
        for i in dicionario[string[0]]:
            if backtracking(matriz, [], i[0], i[1], string, 0, "N"):
                achou = True
                print(1)
                break
        if achou == False:
            print(0)
          

  except EOFError:
    break

