s = input()

lista = s.split(" ")
maior = ""

for i in lista:
    if len(i) > len(maior):
        maior = i

print(maior)