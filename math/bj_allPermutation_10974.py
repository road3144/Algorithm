import sys
input = sys.stdin.readline

n = int(input())
s = []


def dfs():
    if len(s) == n:
        print(*s)
        return
    for i in range(1, n+1):
        if i in range(1, n+1):
            if i not in s:
                s.append(i)
                dfs()
                s.pop()


dfs()
