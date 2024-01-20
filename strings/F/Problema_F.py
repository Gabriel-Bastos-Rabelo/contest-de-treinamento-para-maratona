str = str(input())
senha = True

alfabetomin = "abcdefghijklmnopqrstuvwxyz"
alfabetomax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"


if(len(str)<8):
    print("minimo de 8 caracteres")
    senha = False

cont = 0
for i in alfabetomax:
    if i in str:
        cont+=1
        break   
if cont ==0:
    print("letra maiuscula")
    senha = False


cont = 0
for i in alfabetomin:
    if i in str:
        cont+=1
        break
if cont ==0:
    print("letra minuscula")
    senha = False


cont = 0
for i in num:
    if i in str:
        cont+=1
        break
if cont == 0:
    print("numero")
    senha = False

if(senha):
    print("senha valida")
