import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
n, k = map(int, input().split())
queue.append(n)
dx = [-1, 1, 0]
dis = [0] * 100001


def sumba():
    while queue:
        s = queue.popleft()
        if s == k:
            return dis[s]
        for i in dx:
            if i == 0:
                ns = s * 2
            else:
                ns = s + i
            if ns < 0 or ns > 100000:
                continue
            if dis[ns] == 0:
                dis[ns] = dis[s] + 1
                queue.append(ns)


print(sumba())
