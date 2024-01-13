import sys

input = sys.stdin.readline

m, n = map(int, input().split())
snack = list(map(int, input().split()))


def get_total(mid, snack):
    total = 0
    if mid == 0:
        return sum(snack)
    for i in snack:
        total += i // mid
    return total


start = 0
end = max(snack)
ans = 0

while start <= end:
    mid = (start + end) // 2
    total = get_total(mid, snack)
    if total < m:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)
