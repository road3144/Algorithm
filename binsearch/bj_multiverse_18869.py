import sys
from bisect import bisect_left
from collections import defaultdict

input = sys.stdin.readline

m, n = map(int, input().split())
verse = []
order = [[0 for _ in range(n)] for _ in range(m)]
universe = defaultdict(int)

for _ in range(m):
    verse.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        order[i][j] = bisect_left(verse[i], verse[i][j])
    universe[tuple(order[i])] += 1

sum = 0

for i in universe.values():
    sum += (i * (i-1)) // 2

print(sum)
