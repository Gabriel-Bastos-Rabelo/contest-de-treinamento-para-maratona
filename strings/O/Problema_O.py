s = input()

vogais = "aeiouAEIOU"
cont = 0
for i in s:
    if i in vogais:
        cont += 1

print(cont)