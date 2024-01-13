import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

start = end = 0
vit = [False] * 100001

cnt = 0

while start != n and end != n:
    if not vit[data[end]]:
        vit[data[end]] = True
        end += 1
        cnt += end - start
    else:
        while vit[data[end]]:
            vit[data[start]] = False
            start += 1

print(cnt)
1