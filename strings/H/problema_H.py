palavra = input()
codigo = int(input())

codigos = list("abcdefghijklmnopqrstuvwxyz")
codigosMaiusculos = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

codificado = ""
for i in palavra:
    if "a"<= i <= "z":
        val = codigos.index(i)
        val = (val + codigo) % 26
        codificado += codigos[val]
    elif "A"<= i <= "Z":
        val = codigosMaiusculos.index(i)
        val = (val + codigo) % 26
        codificado += codigosMaiusculos[val]
    else:
        codificado += i

print(codificado)