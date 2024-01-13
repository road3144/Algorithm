#경로복원

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
nxt = [[0 for _ in range(n+1)] for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)
    nxt[a][b] = b

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                nxt[a][b] = nxt[a][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
            continue
        path = []
        start = i
        while start != j:
            path.append(start)
            start = nxt[start][j]
        path.append(j)
        print(len(path), end=' ')
        print(' '.join(map(str, path)))
