n = int(input())

for i in range(n):
    s = input()
    t = len(s)

    p, s = s[:t//2], s[t//2:]

    string = "".join([p[::-1], s[::-1]])
    print(string)