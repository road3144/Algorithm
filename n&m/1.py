# 순열

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = set()


def dfs():
    if len(s) == m:
        print(*s)

    for i in range(1, n + 1):
        if i not in s:
            s.add(i)
            dfs()
            s.remove(i)


dfs()
