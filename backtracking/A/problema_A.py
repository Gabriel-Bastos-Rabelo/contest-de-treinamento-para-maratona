def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return (a*b)/mdc(a, b)


a = int(input())
b = int(input())
c = int(input())

res = mmc(a, b)
res = mmc(res, c)
print(int(res))