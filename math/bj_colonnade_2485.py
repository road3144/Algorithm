import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
tree = []
interval = []
ans = 0
for i in range(n):
    tree.append(int(input()))
for i in range(1, n):
    interval.append(tree[i] - tree[i-1])

g = interval[0]
for i in range(1, n-1):
    g = gcd(g, interval[i])

for i in interval:
    ans += i // g - 1

print(ans)
