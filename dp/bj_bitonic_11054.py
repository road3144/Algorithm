import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data2 = data.copy()
data2.reverse()
dp = [1 for i in range(n)]
dp2 = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if data2[i] > data2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
result = [0 for _ in range(n)]

for i in range(n):
    result[i] = dp[i] + dp2[n-i-1] -1

print(max(result))