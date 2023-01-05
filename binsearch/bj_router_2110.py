import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start = 0
end = house[-1] - house[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    current = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] >= current + mid:
            cnt += 1
            current = house[i]
    if cnt < c:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)
