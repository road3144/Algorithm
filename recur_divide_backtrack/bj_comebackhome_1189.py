import sys

input = sys.stdin.readline

dx = [0 , 0, 1, -1]
dy = [1, -1, 0, 0]

r, c, k = map(int, input().split())
graph = []
s = []
for _ in range(r):
    graph.append(list(input().rstrip()))
temp = [[0 for _ in range(c)] for _ in range(r)]
answer = 0


def dfs(x, y, distance):
    global answer
    if x == 0 and y == c-1:
        if temp[x][y] == k:
            answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= r or nx < 0 or ny < 0 or ny >= c:
            continue
        if (nx, ny) not in s and graph[nx][ny] != 'T':
            temp[nx][ny] = distance + 1
            s.append((nx, ny))
            dfs(nx, ny, distance+1)
            rx, ry = s.pop()
            temp[rx][ry] = 0


temp[r-1][0] = 1
s.append((r-1, 0))
dfs(r-1, 0, 1)
print(answer)
