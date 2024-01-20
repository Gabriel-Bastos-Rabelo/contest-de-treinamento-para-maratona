blocos = 1
letras = 0
string = input()

for i in string:
  if i == " ":
    blocos += 1
  else:
    letras += 1

print(blocos)
print(letras)