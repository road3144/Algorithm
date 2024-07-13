from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(land, sx, sy):
    q = deque()
    q.append((sx, sy))
    temp[sx][sy] = 1
    area = 1
    land[sx][sy] = now
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i],
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if land[nx][ny] != 1 or temp[nx][ny] != 0:
                continue
            temp[nx][ny] = temp[x][y] + 1
            land[nx][ny] = now
            q.append((nx, ny))
            area += 1

    oil[now] = area


def solution(land):
    global now, oil, temp, n, m
    answer = 0
    n, m = len(land), len(land[0])
    now = 1
    oil = {}
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                now += 1
                bfs(land, i, j)

    for j in range(m):
        s = set()
        total = 0
        for i in range(n):
            if land[i][j] != 0:
                s.add(land[i][j])
        for k in s:
            total += oil[k]
        answer = max(answer, total)

    return answer


land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))
