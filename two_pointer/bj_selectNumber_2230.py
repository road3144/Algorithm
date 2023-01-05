import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
ans = int(2e9)

end = 0
for start in range(n):
    while end < n and arr[end] - arr[start] < m:
        end += 1
    if end == n:
        break
    ans = min(ans, arr[end] - arr[start])

print(ans)
