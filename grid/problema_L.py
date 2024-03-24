def verificarColuna(matriz, n):
    for i in range(n):
        lista = [matriz[j][i] for j in range(n)]
        dicionario = {}

        for i in lista:
            if i not in dicionario:
                dicionario[i] = 1
            else:
                return False

    return True

n = int(input())

for i in range(n):
    c = int(input())

    achou = False
    matriz = []
    for j in range(c):
        lista = list(input().split())
        
        dicionario = {}

        for i in lista:
            if i not in dicionario:
                dicionario[i] = 1
            else:
                achou = True
                break
        matriz.append(lista)

    if achou:
        print("nao")
        continue

    if(verificarColuna(matriz, c)):
        print("sim")
    
    else:
        print("nao")

    
        


