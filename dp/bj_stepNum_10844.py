import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10
dp[0] = 0
dp2 = dp.copy()

for i in range(1, n):
    dp[0] = dp2[1]
    for j in range(1, 9):
        dp[j] = dp2[j-1] + dp2[j+1]
    dp[9] = dp2[8]
    dp2 = dp.copy()

print(sum(dp) % 1000000000)


