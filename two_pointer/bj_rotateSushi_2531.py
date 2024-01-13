import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = []
for _ in range(n):
    belt.append(int(input()))

su_cnt = [0] * (d+1)
start, end = 0, k-1
se = set()
result = -1
se.add(c)
su_cnt[c] += 1
for i in range(k):
    se.add(belt[i])
    su_cnt[belt[i]] += 1

while start < n:
    result = max(result, len(se))

    su_cnt[belt[start]] -= 1
    if su_cnt[belt[start]] == 0:
        se.remove(belt[start])
    start += 1

    end = (end + 1) % n
    su_cnt[belt[end]] += 1
    se.add(belt[end])

print(result)
