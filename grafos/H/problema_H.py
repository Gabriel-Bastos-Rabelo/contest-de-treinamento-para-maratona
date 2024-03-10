
#solução 1
def diferenca(a, b):
    x = bin(a)[2:][::-1]
    y = bin(b)[2:][::-1]
    res = 0

    
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]:
            res += 1

    maior = x if len(x) > len(y) else y
    for i in range(min(len(x), len(y)), len(maior)):
        if maior[i] != '0':
            res += 1
    
    

    return res

while True:
    x, y = map(int, input().split())

    if x+y == 0:
        break

    print(diferenca(x, y))


#solução 2

def hamming_distance(a, b):
    xor = a ^ b
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    print(hamming_distance(x, y))

