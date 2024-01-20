qtd = int(input())
pares = 0
codigo = []
lado = []
for i in range(qtd):
    codigoEn, ladoEn = input().split(" ")
    codigoEn = int(codigoEn)
    if codigoEn not in codigo:
        codigo.append(codigoEn)
        lado.append(ladoEn)

    else:
        index = codigo.index(codigoEn)
        if lado[index] != ladoEn:
            pares += 1
            codigo.pop(index)
            lado.pop(index)
        else:
            codigo.append(codigoEn)
            lado.append(ladoEn)

print(pares)
