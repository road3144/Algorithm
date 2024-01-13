import sys

input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit(0)
data = [False, False] + [True] * (n-1)
prime = []

for i in range(2, n+1):
    if data[i]:
        for j in range(i*2, n+1, i):
            data[j] = False

for i in range(2, n+1):
    if data[i]:
        prime.append(i)

left = right = 0
tmp = prime[0]
cnt = 0
while left <= right:
    if tmp > n:
        tmp -= prime[left]
        left += 1
    else:
        if tmp == n:
            cnt += 1
        right += 1

        if right >= len(prime):
            break
        tmp += prime[right]

print(cnt)