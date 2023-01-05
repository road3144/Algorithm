import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = int(1e9)

end = 0
tot = arr[0]
for start in range(n):
    while end < n and tot < s:
        end += 1
        if end != n:
            tot += arr[end]
    if end == n:
        break
    ans = min(ans, end - start + 1)
    tot -= arr[start]
if ans == int(1e9):
    print(0)
else:
    print(ans)
