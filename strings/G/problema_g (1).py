qtd = int(input())
conc = ""
for i in range(qtd):
  caractere = input()
  if i < qtd-1:
    conc += caractere + " "
  else:
    conc += caractere

print(conc)