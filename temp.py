r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))
print(graph)


def alphaDFS(x, y, depth, path):
    print(graph[x][y])
    if x < 0 or x >= r or y < 0 or y >= c:
        return depth
    if not graph[x][y] in path:
        path.append(graph[x][y])
        nd = []
        nd.append(alphaDFS(x-1, y, depth, path))
        nd.append(alphaDFS(x+1, y, depth, path))
        nd.append(alphaDFS(x, y-1, depth, path))
        nd.append(alphaDFS(x, y+1, depth, path))
        return max(nd) + 1
    return depth


print(alphaDFS(0, 0, 0, []))






