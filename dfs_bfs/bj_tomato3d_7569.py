import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque()
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((j, k, i))


def tomato():
    while queue:
        x, y, z = queue.popleft()
        for c in range(6):
            nx = x + dx[c]
            ny = y + dy[c]
            nz = z + dz[c]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nx, ny, nz))


tomato()
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day-1)

