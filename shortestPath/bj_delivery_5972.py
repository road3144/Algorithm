import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
start = 1

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nex_cost, nex_node in graph[now]:
            total = dist + nex_cost
            if total < distance[nex_node]:
                distance[nex_node] = total
                heapq.heappush(q, (total, nex_node))


dijkstra(start)
print(distance[n])
