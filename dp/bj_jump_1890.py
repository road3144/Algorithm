import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
board = []
dp = [([0] * n) for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))
start = board[0][0]
dp[0][start] = 1
dp[start][0] = 1

for i in range(n):
    for j in range(n):
        dis = board[i][j]
        if dis == 0:
            break
        if i + dis < n:
            dp[i+dis][j] += dp[i][j]

        if j + dis < n:
            dp[i][j+dis] += dp[i][j]

print(dp[n-1][n-1])
