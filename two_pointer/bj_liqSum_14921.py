import sys

input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))

start, end = 0, n-1

ans = liq[0] + liq[end]

while start < end:
    tmp = liq[start] + liq[end]
    if abs(ans) > abs(tmp):
        ans = tmp
    if tmp < 0:
        start += 1
    else:
        end -= 1
print(ans)
