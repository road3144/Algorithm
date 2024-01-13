import sys
import heapq

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    raw = list(input().rstrip())
    left = []
    right = []

    for i in raw:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    right.reverse()
    print("".join(map(str, left + right)))
