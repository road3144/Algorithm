import sys
input = sys.stdin.readline

graph = []
blanks = []

for _ in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blanks.append((i, j))


def check_row(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True


def check_col(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True


def check_section(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(k):
    if k == len(blanks):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blanks[k][0]
        y = blanks[k][1]
        if check_row(x, i) and check_col(y, i) and check_section(x, y, i):
            graph[x][y] = i
            dfs(k+1)
            graph[x][y] = 0


dfs(0)
# pypy3만 통과
