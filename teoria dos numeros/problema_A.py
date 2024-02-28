n = int(input())
valores = list(map(int, input().split()))

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return (a * b)//mdc(a, b)


ans = valores[0]
for i in range(1, n):
    ans = mmc(ans, valores[i])


print(ans)