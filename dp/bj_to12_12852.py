import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

m = n
path = []
while m != 1:
    path.append(m)
    if m % 3 == 0 and dp[m] - 1 == dp[m//3]:
        m = m // 3
    elif m % 2 == 0 and dp[m] - 1 == dp[m//2]:
        m = m // 2
    else:
        m -= 1
path.append(1)
print(dp[n])
print(' '.join(map(str, path)))
