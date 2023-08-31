import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(201)] for _ in range(201)]
dp[0][0] = 1

for i in range(1, k+1):
    for j in range(n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % int(1e9)

print(dp[k][n])
