n, g = map(int, input().split())


def ehPrimo(numero):
    if numero != 2 and numero % 2 == 0:
        return False
    
    elif numero == 2:
        return True
    
    else:
        i = 1
        cont = 0

        while i < (numero//2)+1:
            if cont > 1:
                return False
            if numero % i == 0:
                cont += 1

            i += 1

        return True
    


for i in range(n, g + 1):

    if ehPrimo(i):
        print(i, end = " ")