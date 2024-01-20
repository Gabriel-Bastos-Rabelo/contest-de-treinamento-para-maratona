s = input()

n = ["da", "de", "do", "dos", "e"]

l = s.split(" ")
if len(l) > 2:
    nome = []
    for i in l:
        if i not in n:
            nome.append(i)
    

    string = nome[0] + " "
    for j in range(1, len(nome)-1):
        string += nome[j][0] + ". "

    string += nome[len(nome)-1]

    print(string)

else:
    print(s)


