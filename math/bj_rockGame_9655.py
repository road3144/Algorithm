import sys
from collections import defaultdict
input = sys.stdin.readline

n = str(input().rstrip())
dic = defaultdict()

for i in n:
  dic[i] += 1

ma = max(dic.values())
ma_k = ''
flag = 0
for k, v in dic.items():
    if v == ma:
        ma_k = k
        flag += 1

if flag > 1:
    print('?')
else:
    print(ma_k)
