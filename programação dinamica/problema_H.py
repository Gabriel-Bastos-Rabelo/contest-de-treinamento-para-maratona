import math

while True:
    entrada = list(map(int, input().split()))

    if entrada[0] == 0:
        break

    paginas = 0
    

    while True:
        
        diferenca = math.ceil(paginas/entrada[0]) - math.ceil(paginas/entrada[2])



        if diferenca >= entrada[1] and paginas % entrada[0] == 0:
            break

        paginas += entrada[2]

    print(paginas)

        
