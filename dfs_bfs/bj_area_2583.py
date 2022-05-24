from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
v = 0
queue = deque()
m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)]for _ in range(m)]
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex):
        for j in range(m-ey, m-sy):
            graph[j][i] = -1


def area(graph, v):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[ny][nx] == -1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = v
                queue.append((nx, ny))


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            v = v + 1
            graph[i][j] = v
            queue.append((j, i))
            area(graph, v)

areaList = [0 for i in range(1, v+1)]
for i in range(m):
    for j in range(n):
        if graph[i][j] != -1:
            areaList[graph[i][j] - 1] += 1

print(v)
areaList.sort()
for i in areaList:
    print(i, end=' ')