r, c = map(int, input().split())
alpha = []
for _ in range(r):
    alpha.append(list(input()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global answer
    queue = {(x, y, alpha[x][y])}
    while queue:
        x, y, path = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < r) and (0 <= ny < c) and (not alpha[nx][ny] in path):
                queue.add((nx, ny, path + alpha[nx][ny],))
                answer = max(answer, len(path) + 1)


answer = 1
bfs(0, 0)
print(answer)
