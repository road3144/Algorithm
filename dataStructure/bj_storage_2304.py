import sys
import heapq

input = sys.stdin.readline

n = int(input())
pillar = []
max_id = -1
result = 0
for i in range(n):
    l, h = map(int, input().split())
    pillar.append((l, h))

pillar.sort()

for i in range(n):
    if result < pillar[i][1]:
        result = pillar[i][1]
        max_id = i

height = pillar[0][1]
for i in range(max_id):
    result += height * (pillar[i + 1][0] - pillar[i][0])
    height = max(height, pillar[i+1][1])

height = pillar[-1][1]

for i in range(n-1, max_id, -1):
    result += height * (pillar[i][0] - pillar[i-1][0])
    height = max(height, pillar[i-1][1])

print(result)
