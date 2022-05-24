def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(i+1, j+1, parent)
for i in range(0, m-1):
    if find_parent(plan[i], parent) != find_parent(plan[i+1], parent):
        print("NO")
        exit(0)
print("YES")
