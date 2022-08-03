import sys

input = sys.stdin.readline


def find_combine(idx, num):
    if idx == 6:
        print(*ans)
        return
    for i in range(num, k):
        if not visited[i]:
            ans[idx] = s[i]
            visited[i] = True
            find_combine(idx + 1, i + 1)
            visited[i] = False


while True:
    args = list(map(int, input().split(' ')))
    k = args[0]
    if k == 0:
        break
    s = args[1:]
    visited = [False] * k
    ans = [0] * 6
    find_combine(0, 0)
    print()

