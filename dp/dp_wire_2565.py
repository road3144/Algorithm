import sys
input = sys.stdin.readline

n = int(input())
data = []
dp = [1 for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort()

for i in range(1, n):
    for j in range(i):
        if data[i][1] > data[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))