# 벨만 포드 알고리즘 처음이라 답 보고 품
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))


def bellman_ford(start):
    distance[start] = 0
    for i in range(1, n+1):
        for a, b, cost in edges:
            if distance[a] != INF and distance[b] > distance[a] + cost:
                distance[b] = distance[a] + cost
                if i == n:
                    return True
    return False


if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
