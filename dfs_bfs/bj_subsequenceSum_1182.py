# dfs
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
items = list(map(int, input().split()))
cnt = 0


def sub_seq(idx, sub_sum):
    global cnt
    if idx >= n:
        return
    sub_sum += items[idx]

    if sub_sum == s:
        cnt += 1
    sub_seq(idx + 1, sub_sum)
    sub_seq(idx + 1, sub_sum - items[idx])


sub_seq(0, 0)
print(cnt)

# combination
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n, s = map(int, input().split())
# items = list(map(int, input().split()))
# cnt = 0
# for i in range(1, n+1):
#     for j in combinations(items, i):
#         if sum(j) == s:
#             cnt += 1
#
# print(cnt)