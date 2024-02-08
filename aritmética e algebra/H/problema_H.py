n = int(input())

for i in range(n):
    n1, n2, n3 = map(float, input().split())

    if n1 > n2 and n1 < n3:
        print("True")

    else:
        print("False")