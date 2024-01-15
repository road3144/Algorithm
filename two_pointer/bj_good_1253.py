# 투포인터 이분탐색인데 난 다르게 품

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
good_se = set()
dic = defaultdict(int)

result = 0

for i in range(n):
    dic[data[i]] += 1

for i in range(n):
    for j in range(i+1, n):
        dic[data[i]] -= 1
        dic[data[j]] -= 1
        if data[i] + data[j] in dic.keys() and dic[data[i] + data[j]] != 0:
            good_se.add(data[i] + data[j])
        dic[data[i]] += 1
        dic[data[j]] += 1

for i in good_se:
    result += dic[i]

print(result)
