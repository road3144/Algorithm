import sys
input = sys.stdin.readline

n = int(input())
graph = []
res = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


def quad_tree(x, y, size):
    color = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != graph[i][j]:
                res.append("(")
                quad_tree(x, y, size//2)
                quad_tree(x, y + size // 2, size // 2)
                quad_tree(x+size//2, y, size//2)
                quad_tree(x+size//2, y+size//2, size//2)
                res.append(")")
                return
    res.append(color)


quad_tree(0, 0, n)
print("".join(map(str, res)))
