from collections import deque

n = int(input())
graph = []

visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(input()))


def bfsColor(v, color):
    while queue:
        x, y = queue.popleft()
        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != color:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = v
                queue.append((nx, ny))


queue = deque()
v = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            v += 1
            visited[i][j] = v
            queue.append((i, j))
            bfsColor(v, graph[i][j])

visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
v2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            v2 += 1
            visited[i][j] = v2
            queue.append((i, j))
            bfsColor(v2, graph[i][j])


print(v, v2)
