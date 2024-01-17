import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

end = 0
answer = tmp = odd = 0

for start in range(n):
    while odd <= k and end < n:
        if a[end] % 2 != 0:
            odd += 1
        else:
            tmp += 1
        end += 1
        if start == 0 and end == n:
            answer = tmp
            break
    if odd == k+1:
        answer = max(answer, tmp)
    if a[start] % 2 != 0:
        odd -= 1
    else:
        tmp -= 1

print(answer)
