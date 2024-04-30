import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
graph = []
visited = [False] * n
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
answer = INF
s = []


def dfs(node):
    global answer
    if len(s) == n:
        answer = min(answer, sum(s))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            s.append(graph[node][i])
            dfs(i)
            s.pop()
            visited[i] = False


visited[m] = True
s.append(0)
dfs(m)
print(answer)
