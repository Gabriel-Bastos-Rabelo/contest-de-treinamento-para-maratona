mapeados = list(input().split(" "))
mapeados = [int(val) for val in mapeados]
verificar = list(input().split(" "))
verificar = [int(val) for val in verificar]
verificar.sort()
for i in verificar:
    if i not in mapeados:
        print(f"{i} Não está mapeado")
    else:
        print(f"{i} Está mapeado")
    