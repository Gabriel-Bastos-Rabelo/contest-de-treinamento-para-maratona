import math

p = input()
vogais = "AEIOU"
v = 0
c = 0
for i in p:
    if i in vogais:
        v += 1
    elif i != " ":
        c += 1

print(math.factorial(c) * math.factorial(v))
