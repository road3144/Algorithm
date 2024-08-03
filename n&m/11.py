import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def dfs():
    if len(s) == m:
        print(*s)
        return
    prev = 0
    for i in range(n):
        if prev != arr[i]:
            s.append(arr[i])
            prev = arr[i]
            dfs()
            s.pop()


dfs()
