import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
nums = [0] * m

for i in range(n):
    total += arr[i]
    nums[total % m] += 1
ans = nums[0]
for i in nums:
    ans += (i * (i-1)) // 2
print(ans)
