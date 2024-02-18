n = int(input())
fib = [0] * (n+1)
if n > 2:
    fib[0] = 1
    fib[1] = 1
    fib[2] = 1

    for i in range(3, n):
        fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3]

    
    print(fib[n-1])

else:
    print(1)
