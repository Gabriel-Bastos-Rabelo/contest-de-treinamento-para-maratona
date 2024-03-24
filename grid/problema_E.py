import math

n = int(input())


raiz = math.sqrt(n)


if(int(raiz) == raiz):
    print("Quadrado perfeito")
else:
    print("Nao eh quadrado perfeito")

raiz = int(raiz)

print(raiz ** 2)
print(raiz)