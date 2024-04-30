import sys

input = sys.stdin.readline

t, w = map(int, input().split())
data = [1]
for _ in range(t):
    data.append(int(input()))

dp = [[0 for _ in range(w+1)] for _ in range(t+1)]
dp[1][0] = data[1] % 2
dp[1][1] = data[1] // 2
for i in range(2, t+1):
    dp[i][0] = dp[i-1][0] + data[i] % 2
for i in range(2, t+1):
    for j in range(1, w+1):
        value = data[i] % 2 if j % 2 == 0 else data[i] // 2
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + value

print(max(dp[t]))
