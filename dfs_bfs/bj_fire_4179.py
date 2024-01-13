import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue_j = deque()
queue_f = deque()
visited_f = [[0] * c for _ in range(r)]
visited_j = [[0] * c for _ in range(r)]

for _ in range(r):
    graph.append(list(input().rstrip()))


for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            queue_j.append((j, i))
            visited_j[i][j] = 1

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            queue_f.append((j, i))
            visited_f[i][j] = 1


def bfs():
    while queue_f:
        x, y = queue_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if graph[ny][nx] == '#':
                continue
            if not visited_f[ny][nx]:
                visited_f[ny][nx] = visited_f[y][x] + 1
                queue_f.append((nx, ny))

    while queue_j:
        x, y = queue_j.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if not visited_j[ny][nx] and graph[ny][nx] != '#':
                    if not visited_f[ny][nx] or visited_f[ny][nx] > visited_j[y][x] + 1:
                        visited_j[ny][nx] = visited_j[y][x] + 1
                        queue_j.append((nx, ny))
            else:
                return visited_j[y][x]

    return "IMPOSSIBLE"


print(bfs())
