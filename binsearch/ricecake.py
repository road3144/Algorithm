import sys

n, m = map(int, input().split())
rc = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(rc)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rc:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(n, m)
print(result)
