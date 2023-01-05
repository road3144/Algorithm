import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = int(3e9)
arr.sort()
mstart = arr[0]
mend = arr[n-1]

end = n-1
for start in range(n):
    while end - start > 1 and abs(arr[start] + arr[end]) > abs(arr[start] + arr[end-1]):
        end -= 1
    if start >= end:
        break
    if abs(ans) > abs(arr[start] + arr[end]):
        ans = arr[start] + arr[end]
        mstart = arr[start]
        mend = arr[end]

print(mstart, mend)
