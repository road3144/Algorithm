import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * (n+1)
data = []
ans = []

for k in range(1, n+1):
    sums[k] = sums[k-1] + nums[k-1]

for _ in range(m):
    i, j = map(int, input().split())
    ans.append(sums[j] - sums[i-1])

for k in range(m):
    print(ans[k])
