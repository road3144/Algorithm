import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

k = int(input())
friends = list(map(int, input().split()))

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cities = [INF] + [0] * n
for i in range(1, n+1):
    max_dis = 0
    for j in friends:
        max_dis = max(max_dis, graph[j][i] + graph[i][j])
    cities[i] = max_dis

answer = []
for i, v in enumerate(cities):
    if v == min(cities):
        answer.append(i)

print(' '.join(map(str, answer)))
