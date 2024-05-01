import sys

input = sys.stdin.readline

cnt = 0
INF = int(1e9)

while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    dp = [[INF for _ in range(3)] for _ in range(n)]
    dp[0][1] = data[0][1]
    dp[0][2] = dp[0][1] + data[0][2]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + data[i][0]
        dp[i][1] = min(dp[i-1] + [dp[i][0]]) + data[i][1]
        dp[i][2] = min(dp[i][1], dp[i-1][1], dp[i-1][2]) + data[i][2]
    print(f'{cnt}. {dp[n-1][1]}')
