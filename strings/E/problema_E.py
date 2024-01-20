s = input()
string = ""
cont = 1

#aaabbbccc
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cont += 1
    else:
        if cont > 1:
            string += s[i-1] + str(cont)
        else:
            string += s[i-1]
        cont = 1

if cont > 1:
    string += s[len(s) - 1] + str(cont)

else:
    string += s[len(s) - 1]

if len(string) >= len(s):
    print(s)
else:
    print(string)
        