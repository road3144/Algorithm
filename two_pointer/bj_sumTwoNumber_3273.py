import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
ans = 0

end = n-1
for start in range(n):
    while end < n and arr[start] + arr[end] > x:
        end -= 1
    if end == 0 or start >= end:
        break
    if arr[start] + arr[end] == x:
        ans += 1

print(ans)
