r = int(input())


for j in range(r):


    n = str(input())




    


    lista = []
    a = n[0:8][::-1]

    lista.append(a)


    b = n[8: 16][::-1]
    lista.append(b)

    c = n[16:24][::-1]
    lista.append(c)


    d = n[24:32][::-1]

    lista.append(d)



    string = ""

    for index, i in enumerate(lista):
        res = 0

        for j in range(len(i)):
            res += (2 ** j) * int(i[j])

        if index < len(lista) - 1:
            string += str(res) + "."
        else:
            string += str(res)

    print(string)


