import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
answer1 = 0
answer2 = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


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


dijkstra(1)
answer1, answer2 = distance[v1], distance[v2]
distance = [INF] * (n+1)
dijkstra(v1)
answer1 += distance[v2]
answer2 += distance[n]
distance = [INF] * (n+1)
dijkstra(v2)
answer1 += distance[n]
answer2 += distance[v1]

answer = min(answer1, answer2)
if answer >= INF:
    print(-1)
else:
    print(answer)
