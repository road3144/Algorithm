import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
ans = 0


def getCut(mid, tree):
    length = 0
    for i in tree:
        if i >= mid:
            length += i - mid
    return length


while start <= end:
    mid = (start + end) // 2
    cut = getCut(mid, tree)
    if cut < m:
        end = mid - 1
    elif cut > m:
        ans = mid
        start = mid + 1
    else:
        ans = mid
        break

print(ans)
