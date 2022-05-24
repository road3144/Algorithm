import heapq


def single(s, g, graph):
    q = []
    INF = int(1e9)
    distance = [INF] * len(graph)
    heapq.heappush(q, (s, 0))
    distance[s] = 0
    while q:
        node, fee = heapq.heappop(q)
        if distance[node] < fee:
            continue
        for i in graph[node]:
            next_node, next_fee = i
            next_fee += fee
            if next_fee < distance[next_node]:
                distance[next_node] = next_fee
                heapq.heappush(q, (next_node, next_fee))
    return distance[g]


def each(s, a, b, graph):
    return single(s, a, graph) + single(s, b, graph)


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for edge in fares:
        x, y, fare = edge
        graph[x].append((y, fare))
        graph[y].append((x, fare))
    visited = [0] * (n+1)
    visited[s] = 1
    queue = []
    heapq.heappush(queue, (s, 0))
    min_fee = each(s, a, b, graph)
    while queue:
        node, fee = heapq.heappop(queue)
        for i in graph[node]:
            next_node, next_fee = i
            next_fee += fee
            if visited[next_node] != 0:
                continue
            if min_fee > each(next_node, a, b, graph) + next_fee:
                visited[next_node] = 1
                min_fee = each(next_node, a, b, graph) + next_fee
                heapq.heappush(queue, (next_node, next_fee))
    answer = min_fee
    return answer


n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))