import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 91
dp[1] = 1
for i in range(2, 91):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])