import sys

input = sys.stdin.readline

n, k = map(int, input().split())

data = list(map(int, input().split()))
vit = [k] * (max(data) + 1)

start = end = 0
ans = 0

while start != n and end != n:
    if vit[data[end]] > 0:
        vit[data[end]] -= 1
        end += 1
        ans = max(ans, end - start)
    else:
        while vit[data[end]] <= 0:
            vit[data[start]] += 1
            start += 1
            ans = max(ans, end - start)

print(ans)
