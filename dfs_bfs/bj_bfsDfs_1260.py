import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[s].sort()
    graph[e].append(s)
    graph[e].sort()


def dfs(dgraph, dv, dvisited):
    dvisited[dv] = True
    print(dv, end=' ')

    for i in dgraph[dv]:
        if not dvisited[i]:
            dfs(dgraph, i, dvisited)


def bfs(bgraph, start, bvisited):
    queue = deque([start])
    bvisited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in bgraph[v]:
            if not bvisited[i]:
                queue.append(i)
                bvisited[i] = True


dfs(graph, v, visited)
visited = [False] * (n+1)
print('')
bfs(graph, v, visited)
