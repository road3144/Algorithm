import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
INF = float('inf')
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
items = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            cnt += items[j]
    answer = max(answer, cnt)

print(answer)
