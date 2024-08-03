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
        if prev != arr[i] and (len(s) == 0 or s[-1] <= arr[i]):
            s.append(arr[i])
            prev = arr[i]
            dfs()
            s.pop()


dfs()
