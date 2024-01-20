s = input()
sa = input()
dicionario = {}

lista = s.split(" ")
s = "".join(lista)

for i in s:
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1


naoPode = True
for j in sa:
    if j in dicionario:
        if dicionario[j] > 0:
            dicionario[j] -= 1
        else:
            naoPode = False
            print("nao")
            break
    else:
        naoPode = False
        print("nao")

if naoPode:
    print("sim")
