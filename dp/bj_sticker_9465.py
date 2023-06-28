import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + sticker[0][i], dp[1][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + sticker[1][i], dp[0][i]-sticker[0][i])
    print(max(dp[0][n-1], dp[1][n-1]))
