n = int(input())

lista = list(map(int, input().split()))

soma = sum(lista)

print(soma % 12)