import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))


def tomato():
    while queue:
        x, y = queue.popleft()
        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


tomato()
day = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))

print(day-1)

