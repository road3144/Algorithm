import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[s].sort()
    graph[e].append(s)
    graph[e].sort()


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

print(visited.count(True)-1)
