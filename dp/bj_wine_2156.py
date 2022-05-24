import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 10001
data = [0] * 10001
for i in range(1, n+1):
    data[i] = int(input())

dp[1] = data[1]
dp[2] = data[1] + data[2]
dp[3] = max(data[1] + data[3], data[2] + data[3], data[1] + data[2])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + data[i] + data[i-1], dp[i-2] + data[i], dp[i-1])

print(dp[n])