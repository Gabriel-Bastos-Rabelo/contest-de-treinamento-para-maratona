def ehCapicua(n):
    return str(n) == str(n)[::-1]

n = 4
numero = int(input())
achou = False
for i in range(5):
    if ehCapicua(numero):
        print(numero)
        achou = True
        break
    else:
        aux = str(numero)[::-1]
        aux = int(aux)

        numero += aux
      


if achou == False:
    print(0)


    