import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [0] * (n+1)
ans = []
for i in range(n + 1):
    parent[i] = i


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def is_same(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a == b:
        return "YES"
    else:
        return "NO"


for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(a, b, parent)
    if op == 1:
        ans.append(is_same(a, b, parent))
for i in ans:
    print(i)