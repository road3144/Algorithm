import sys
input = sys.stdin.readline

m, n = map(int, input().split())
data =[]
for _ in range(m):
    data.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[-1 for _ in range(n)] for _ in range(m)]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            if data[x][y] > data[nx][ny]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))
