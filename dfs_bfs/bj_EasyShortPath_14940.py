import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
di_graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    di_graph.append([0 for _ in range(m)])
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i, j))


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or n <= nx:
                continue
            if ny < 0 or m <= ny:
                continue
            if di_graph[nx][ny] == 0 and graph[nx][ny] == 1:
                di_graph[nx][ny] = di_graph[x][y] + 1
                q.append((nx, ny))


bfs()
for i in range(n):
    for j in range(m):
        if di_graph[i][j] == 0 and graph[i][j] == 1:
            di_graph[i][j] = -1
for line in di_graph:
    print(' '.join(map(str, line)))
