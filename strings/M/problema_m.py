email = input()
valido = 1
arroba = False
num = len(email)
for pos, i in enumerate(email):
    if i == "@":
        arroba = True
        break
    elif  'a' <= i <= 'z' or i == '_' or i=='.' or '0' <= i <= '9':
        continue
    else:
        valido = 0
        break

if arroba:
    while pos + 1 < num:
        i = email[pos+1]
        if 'a'<=i<="z" or i==".":
            pos += 1
            continue
        else:
            valido = 0
            break

if i == ".":
    valido = 0
print(valido)