import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

max_data = max(data)

dp = [0] * (max_data + 1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, max_data + 1):
    dp[i] = dp[i-1] + dp[i-5]

for i in data:
    print(dp[i])