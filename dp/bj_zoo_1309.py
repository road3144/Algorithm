import sys
input = sys.stdin.readline

n = int(input())
dp = [[1, 1]]
for _ in range(n):
    dp.append([0, 0])
for i in range(1, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 9901
    dp[i][1] = (dp[i][0] + dp[i-1][0]) % 9901

print(dp[n][1])
