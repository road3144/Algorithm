import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    graph = [[] for _ in range(l)]
    cmap = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for i in range(l):
        for _ in range(r):
            graph[i].append(list(input().rstrip()))
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    start = (i, j, k)
                if graph[i][j][k] == 'E':
                    end = (i, j, k)
    queue = deque()
    queue.append(start)

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if (not 0 <= nz < l) or (not 0 <= nx < r) or (not 0 <= ny < c):
                continue
            if graph[nz][nx][ny] == '#':
                continue
            if (graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E') and cmap[nz][nx][ny] == 0:
                cmap[nz][nx][ny] = cmap[z][x][y] + 1
                queue.append((nz, nx, ny))

    ez, ex, ey = end
    if cmap[ez][ex][ey] == 0:
        print("Trapped!")
    else:
        print(f'Escaped in {cmap[ez][ex][ey]} minute(s).')
