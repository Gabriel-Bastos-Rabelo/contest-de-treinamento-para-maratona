n = int(input())

result = []

for _ in range(n):
    string1 = input()
    string2 = input()

    
    count_string1 = {char: string1.count(char) for char in set(string1)}
    count_string2 = {char: string2.count(char) for char in set(string2)}


    if count_string1 == count_string2:
        result.append('sim')
    else:
        result.append('nao')

for res in result:
    print(res)
