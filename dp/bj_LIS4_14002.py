import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [1] * n
pre = [n] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

path = []
order = max(dp)

for i in range(n-1, -1, -1):
    if dp[i] == order:
        path.append(data[i])
        order -= 1
path.reverse()
print(*path)
