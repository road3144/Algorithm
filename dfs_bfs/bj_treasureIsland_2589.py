from collections import deque

n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
origin = [[0 for _ in range(m)] for _ in range(n)]
queue =deque()
for i in range(n):
    graph.append(list(input()))


def treasure():
    v = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 'W':
                continue
            if graph[nx][ny] == 'L' and move[nx][ny] == 0:
                move[nx][ny] = move[x][y] + 1
                queue.append((nx, ny))
        v = move[x][y]
    return v - 1


ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            if 0 <= i-1 and i+1 < n:
                if graph[i-1][j] == 'L' and graph[i+1][j] == 'L':
                    continue
            if 0 <= j-1 and j+1 < m:
                if graph[i][j-1] == 'L' and graph[i][j+1] == 'L':
                    continue
            move = [[0 for _ in range(m)] for _ in range(n)]
            queue.append((i, j))
            move[i][j] = 1
            t = treasure()
            if ans < t:
                ans = t
print(ans)

