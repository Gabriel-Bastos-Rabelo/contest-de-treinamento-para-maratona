results = []
n = int(input())
for i in range(n):
    nums = list(map(int, input().split()))
    results.append(str(f"{(nums[3]-nums[1])/(nums[2]-nums[0]):.3f}"))

for result in results:
    print(result[:-1])