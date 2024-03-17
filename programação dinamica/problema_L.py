n = int(input())
results = []
for i in range(n):
    numsum = list(map(int, input().split(" x ")))
    numsdois = list(map(int, input().split(" x ")))
    gols1 = numsum[0]+numsdois[1]
    gols2 = numsum[1]+numsdois[0]
    if(gols1>gols2 or (gols1== gols2 and numsdois[1]>numsum[1])):
        results.append("Time 1")
    elif(gols2>gols1 or (gols1==gols2 and numsdois[1]<numsum[1])):
        results.append("Time 2")
    else:
        results.append("Penaltis")

for result in results:
    print(result)