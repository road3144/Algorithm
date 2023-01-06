import sys
from collections import deque
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
ans = []


def bfs(k, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = k
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] <= k:
                continue
            if k < graph[nx][ny] < 102:
                graph[nx][ny] = 102
                queue.append((nx, ny))


n = int(input())
base_graph = []
for i in range(n):
    base_graph.append(list(map(int, input().split())))

max_area = 1
for k in range(0, 101):
    area = 0
    graph = [arr[:] for arr in base_graph]
    for i in range(n):
        for j in range(n):
            if k < graph[i][j] < 102:
                bfs(k, i, j)
                area += 1
    max_area = max(max_area, area)

print(max_area)
