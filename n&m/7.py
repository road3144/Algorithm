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
        s.append(i)
        dfs()
        s.pop()


dfs()
