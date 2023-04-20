import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 100001
square = []

x = 1
while x ** 2 < 100000:
    square.append(x**2)
    x += 1
for i in range(1, n+1):
    min_n = int(1e9)
    for j in square:
        if j > i:
            break
        if dp[i-j] < min_n:
            min_n = dp[i-j]
    dp[i] = min_n + 1


print(dp[n])
