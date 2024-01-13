import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1

result = [1000000000, 1000000000]
while start < end:
    if abs(arr[start] + arr[end]) <= abs(sum(result)):
        result[0] = arr[start]
        result[1] = arr[end]
    if arr[start] + arr[end] > 0:
        end -= 1
    elif arr[start] + arr[end] < 0:
        start += 1
    else:
        break

print(*result)
