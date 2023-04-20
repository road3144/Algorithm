import sys

input = sys.stdin.readline

k = int(input())
order = list(map(int, input().split()))
tree = [[]for _ in range(k)]


def make_tree(arr, level):
    mid = len(arr) // 2
    tree[level].append(arr[mid])
    if len(arr) == 1:
        return
    make_tree(arr[:mid], level+1)
    make_tree(arr[mid+1:], level+1)


make_tree(order, 0)
for i in range(k):
    print(*tree[i])

