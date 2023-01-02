import sys
input = sys.stdin.readline

s = list(input())
n = int(input())
my_dict = dict()
ans = []

for i in range(len(s)):
    if s[i] not in my_dict.keys():
        my_dict[s[i]] = set()
    my_dict[s[i]].add(i)

for k in my_dict.keys():
    arr = [0]
    for i in range(len(s)):
        arr.append(arr[i])
        if i in my_dict[k]:
            arr[i+1] += 1
    my_dict[k] = arr

for _ in range(n):
    alpha, l, r = input().split()
    l, r = map(int, [l, r])
    if alpha in my_dict.keys():
        ans.append(my_dict[alpha][r+1] - my_dict[alpha][l])
    else:
        ans.append(0)
for i in ans:
    print(i)
# pypy3만 100점
