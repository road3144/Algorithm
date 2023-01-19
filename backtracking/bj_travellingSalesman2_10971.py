import sys
input = sys.stdin.readline

n = int(input())
data = []
s = []
minAns = int(2e9)
for _ in range(n):
    data.append(list(map(int, input().split())))

def dfs():
    global minAns
    if len(s) == n:
        ans = 0
        for q in range(n-1):
            if data[s[q]][s[q+1]] == 0:
                ans += minAns
            ans += data[s[q]][s[q+1]]
        if data[s[n-1]][s[0]] == 0:
            ans += minAns
        ans += data[s[n-1]][s[0]]
        minAns = min(ans, minAns)
        return

    for i in range(n):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
print(minAns)
# pypy3 only
