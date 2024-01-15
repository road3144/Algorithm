import sys

input = sys.stdin.readline

s = str(input().rstrip())
t = str(input().rstrip())


def dfs(new_t):
    if new_t == s:
        print(1)
        exit(0)
    if new_t.startswith("B"):
        tmp = list(new_t.rstrip())
        tmp.reverse()
        dfs(''.join(tmp[:len(tmp)-1]))
    if new_t.endswith("A"):
        dfs(new_t[:len(new_t)-1])


dfs(t)

print(0)
