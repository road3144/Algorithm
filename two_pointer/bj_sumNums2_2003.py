import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

end = 0
tot = arr[0]
for start in range(n):
    while end < n and tot < m:
        end += 1
        if not end == n:
            tot += arr[end]
    if end == n:
        break
    if tot == m:
        ans += 1
    tot -= arr[start]

print(ans)
