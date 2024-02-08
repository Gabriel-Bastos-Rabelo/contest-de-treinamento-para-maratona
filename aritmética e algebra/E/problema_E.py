

m, s = map(int, input().split())

temp = (m * 60) + s

temp = temp/60



print(round((temp/10), 1))

print(round((temp)/10 * 21, 1))