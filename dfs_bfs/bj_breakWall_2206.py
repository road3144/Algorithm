import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().strip())))
visited = [[[0for _ in range(m)]for _ in range(n)] for _ in range(2)]


def wallbreak():
    skill = 1
    queue.append((0, 0, skill))
    visited[skill][0][0] = 1
    while queue:
        x, y, skill = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[skill][x][y]
        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                if skill == 1:
                    visited[0][nx][ny] = visited[skill][x][y] + 1
                    queue.append((nx, ny, 0))
                else:
                    continue
            if graph[nx][ny] == 0 and visited[skill][nx][ny] == 0:
                visited[skill][nx][ny] = visited[skill][x][y] + 1
                queue.append((nx, ny, skill))
    return -1


print(wallbreak())
