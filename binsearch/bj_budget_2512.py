import sys

input = sys.stdin.readline

n = int(input())
city = list(map(int, input().split()))
m = int(input())
ans = 0

start = 0
end = max(city)


def sumLimit(city, mid):
    total = 0
    for i in city:
        if mid < i:
            i = mid
        total += i
    return total


while start <= end:
    mid = (start + end) // 2
    if m < sumLimit(city, mid):
        end = mid - 1
    elif m >= sumLimit(city, mid):
        start = mid + 1
        ans = mid
    else:
        ans = mid

print(ans)
