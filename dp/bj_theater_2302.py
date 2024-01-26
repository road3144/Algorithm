import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = set()
dp = [0] * (n+1)
dp[0] = dp[1] = 1
ans = []
answer = 1
cnt = 0

for _ in range(m):
    vip.add(int(input()))

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(1, n+1):
    if i in vip:
        continue
    cnt += 1
    if i+1 in vip or i == n:
        ans.append(dp[cnt])
        cnt = 0

for i in ans:
    answer *= i

print(answer)
