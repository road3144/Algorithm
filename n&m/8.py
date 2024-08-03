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
    for i in arr:
        if len(s) == 0 or s[-1] <= i:
            s.append(i)
            dfs()
            s.pop()


dfs()
