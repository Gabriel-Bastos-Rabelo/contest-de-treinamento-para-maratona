def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


n = int(input())
lista = list(map(int, input().split()))
res = 0

for i in lista:
    res = mdc(res, i)


print(res)

