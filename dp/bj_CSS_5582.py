import sys
input = sys.stdin.readline

data1 = list(input().strip().upper())
data2 = list(input().strip().upper())

n = len(data1)
k = len(data2)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
answer = 0
for i in range(1, n+1):
    for j in range(1, k+1):
        if data1[i-1] == data2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)
