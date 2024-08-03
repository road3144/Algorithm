import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
visited = [False] * n


def dfs():
    if len(s) == m:
        print(*s)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != arr[i]:
            s.append(arr[i])
            visited[i] = True
            prev = arr[i]
            dfs()
            s.pop()
            visited[i] = False


dfs()
