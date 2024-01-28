simbolo = ["Paus", "Ouro", "Coração", "Espada"]
carta = ["Às", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

naipe, numero = input().split(" ")
naipe = int(naipe)
numero = int(numero) - 1

print(f"{carta[numero]} de {simbolo[naipe]}")