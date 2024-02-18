lista = list(map(str, input().split(",")))

memo = {}
def bct(atual, lista, res, opcao):

    
    if str(opcao) in memo:
        return
    
    for i in range(atual, len(lista)):
        memo[str(opcao)] = 1
        opcao.append(lista[i])
        res.append(opcao.copy())
        bct(i+1, lista, res, opcao)
        opcao.pop()
        bct(i+1, lista, res, opcao)

    


res = []
bct(0, lista, res, [])
res.sort(key=len)


for i in res:
    print(",".join(i))



