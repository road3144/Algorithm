import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
cnt = 0

for i in data:
    temp = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            temp = 1
    if temp == 0:
        cnt += 1

print(cnt)