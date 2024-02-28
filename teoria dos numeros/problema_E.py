while(True):
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z == 0:
        break

    res1 = ((x + y)%z)
    res2 = ((x - y) % z)
    res3 = ((x * y) % z)

    print(f"{x} + {y} mod {z} = {res1}")
    print(f"{x} - {y} mod {z} = {res2}")
    print(f"{x} * {y} mod {z} = {res3}")