import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    new_graph = [arr[:] for arr in graph]
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if new_graph[nx][ny] == 1 or new_graph[nx][ny] == 2:
                continue
            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                queue.append((nx, ny))
    global ans
    cnt = 0
    for i in range(n):
        cnt += new_graph[i].count(0)
    ans = max(ans, cnt)


def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
ans = 0
dfs(0)
print(ans)
