import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
dp = [10001] * 10001
dp[0] = 0
for _ in range(n):
    data.append(int(input()))

for i in data:
    for j in range(i, k+1):
        if j >= i:
            dp[j] = min(dp[j], dp[j-i] + 1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
