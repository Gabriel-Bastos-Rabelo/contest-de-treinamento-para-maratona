res = 0

def backtracking(peso, valor,  pesoAtual, index, valores):

    global res

    if pesoAtual > peso:
        return
    
    if valor > res:
        
        res = valor

    

    for i in range(index, len(valores)):
       
        backtracking(peso, valor + valores[i][0],  pesoAtual + valores[i][1], i + 1, valores)


    

while True:
    n = int(input())

    if n == 0:
        break

    lista = []
    for i in range(n):
        valores = list(map(int, input().split()))
        lista.append(valores)

    peso = int(input())



    res = 0
    backtracking(peso, 0,  0, 0, lista)
    print(res)

    
