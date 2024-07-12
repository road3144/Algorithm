import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0
shark = 2
caught = 0
answer = 0


def search_path():
    q = deque()
    q.append((now_x, now_y))
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i], y + dy[i])
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if shark < graph[nx][ny]:
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    return visited


def search_fish(visited):
    x, y, dist = 0, 0, int(1e9)

    for i in range(n):
        for j in range(n):
            if shark <= graph[i][j]:
                continue
            if visited[i][j] == -1:
                continue
            if graph[i][j] == 0:
                continue
            if visited[i][j] < dist:
                dist = visited[i][j]
                x, y = i, j
    if dist == int(1e9):
        return False
    else:
        return x, y, dist


while True:
    found = search_fish(search_path())
    if not found:
        break
    now_x, now_y, cnt = found
    answer += cnt
    caught += 1
    if caught // shark == 1:
        caught = 0
        shark += 1
    graph[now_x][now_y] = 0

print(answer)
