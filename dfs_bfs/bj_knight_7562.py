import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def knight(x, y, gx, gy, n):
    queue = deque()
    queue.append([x, y])
    dis = [[0 for _ in range(n)] for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        if x == gx and y == gy:
            return dis[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dis[nx][ny] == 0:
                queue.append([nx, ny])
                dis[nx][ny] = dis[x][y] + 1


t = int(input())

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    print(knight(sx, sy, gx, gy, n))

