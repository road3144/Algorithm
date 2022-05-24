import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n)]

data = list(map(int, input().split()))

dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(data[i], data[i] + dp[i-1])

print(max(dp))
