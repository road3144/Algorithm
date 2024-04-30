import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)

answer = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        now_cost, now_node = heapq.heappop(q)
        if now_cost != distance[now_node]:
            continue
        for next_node, cost in graph[now_node]:
            next_cost = now_cost + cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))


for s in range(1, n+1):
    distance = [INF] * (n + 1)
    dijkstra(s)
    if s == x:
        for i in range(1, n+1):
            answer[i] += distance[i]
    else:
        answer[s] += distance[x]

print(max(answer))
