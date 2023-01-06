import sys
from collections import deque
input = sys.stdin.readline


dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
ans = []


def bfs(w, h, k, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = k
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = k
                queue.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    k = 2
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(w, h, k, i, j)
                k += 1
    ans.append(k)
for i in ans:
    print(i-2)
