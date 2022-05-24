def floyd(graph, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def each(s, a, b, graph):
    return graph[s][a] + graph[s][b]


def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for edge in fares:
        x, y, fare = edge
        graph[x][y] = fare
        graph[y][x] = fare
    for i in range(n+1):
        graph[i][i] = 0
    floyd(graph, n)
    min_fee = each(s, a, b, graph)
    for i in range(1, n+1):
        if graph[s][i] != INF:
            min_fee = min(min_fee, each(i, a, b, graph) + graph[s][i])
    answer = min_fee
    return answer


n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n, s, a, b, fares))
