import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
t = int(input())
result = []

def cabbage(x, y, v):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = v
        cabbage(x - 1, y, v)
        cabbage(x + 1, y, v)
        cabbage(x, y + 1, v)
        cabbage(x, y - 1, v)
        return True
    return False


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    v = 2

    for i in range(n):
        for j in range(m):
            if cabbage(i, j, v):
                v = v + 1
                cabbage(i, j, v)

    v = v - 2
    result.append(v)

for i in result:
    print(i)
