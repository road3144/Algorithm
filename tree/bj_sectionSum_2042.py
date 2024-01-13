import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
data = []
stree = [0 for _ in range(4 * n)]


def build(node, left, right):
    if left == right:
        stree[node] = data[left]
        return stree[node]
    mid = (left + right) // 2
    stree[node] = build(node*2, left, mid) + build(node*2+1, mid+1, right)
    return stree[node]


def query(start, end, node, left, right):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return stree[node]
    mid = (left + right) // 2
    return query(start, end, node*2, left, mid) + query(start, end, node*2+1, mid+1, right)


def update(idx, val, node, left, right):
    if idx < left or right < idx:
        return stree[node]
    if left == right:
        stree[node] = val
        return stree[node]
    mid = (left + right) // 2
    stree[node] = update(idx, val, node*2, left, mid) + update(idx, val, node*2+1, mid+1, right)
    return stree[node]


for _ in range(n):
    data.append(int(input()))

build(1, 0, n-1)

for _ in range(m+k):
    op, a, b = map(int, input().split())
    if op == 1:
        update(a-1, b, 1, 0, n-1)
    if op == 2:
        print(query(a-1, b-1, 1, 0, n-1))


