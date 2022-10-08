import sys

input = sys.stdin.readline

k, n = map(int, input().split())
sick = []
for _ in range(k):
    sick.append(int(input()))

start = 0
end = max(sick)
ans = 0


def getTotal(mid, sick):
    cnt = 0
    if mid == 0:
        return sum(sick)
    for i in sick:
        cnt += i // mid
    return cnt


while start <= end:
    mid = (start + end) // 2
    total = getTotal(mid, sick)
    if total < n:
        end = mid - 1
    elif total >= n:
        ans = mid
        start = mid +1

print(ans)
