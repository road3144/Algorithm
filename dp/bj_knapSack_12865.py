import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [[0, 0]]
for i in range(n):
    data.append(list(map(int, input().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        weight = data[i][0]
        value = data[i][1]
        if w < weight:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

print(dp[n][k])