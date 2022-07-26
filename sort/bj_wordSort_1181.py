import sys
input = sys.stdin.readline

n = int(input())
data = set()
for _ in range(n):
    data.add(input().strip())

data = list(data)
data.sort(key=lambda x: (len(x), x))
for i in data:
    print(i)
