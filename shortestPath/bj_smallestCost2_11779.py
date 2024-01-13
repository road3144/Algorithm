import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
pre = [0] * (n+1)
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        now_cost, now_node = heapq.heappop(q)
        if now_cost != distance[now_node]:
            continue
        for next_node, next_cost in graph[now_node]:
            total_cost = now_cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))
                pre[next_node] = now_node


start, termination = map(int, input().split())
dijkstra(start)
print(distance[termination])
path = []
cur = termination
while cur != start:
    path.append(cur)
    cur = pre[cur]
path.append(cur)
path.reverse()
print(len(path))
print(' '.join(map(str, path)))
