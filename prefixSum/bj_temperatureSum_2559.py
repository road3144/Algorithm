import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
ans = []

for i in range(1, n+1):
    sums.append(sums[i-1] + nums[i-1])

for i in range(n-k+1):
    ans.append(sums[k+i] - sums[i])

print(max(ans))
