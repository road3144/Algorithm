import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
INF = 1000000001

lis_bin = [-INF]
lis = [(-INF, 0)]


def binary(lis_bin, num):
    low = -1
    high = len(lis_bin)

    while low + 1 < high:
        mid = (low + high) // 2

        if num > lis_bin[mid]:
            low = mid
        else:
            high = mid
    return high


for i in data:
    if i > lis_bin[-1]:
        lis.append((i, len(lis_bin)))
        lis_bin.append(i)
    else:
        idx = binary(lis_bin, i)
        lis_bin[idx] = i
        lis.append((i, idx))

lis_length = len(lis_bin)-1
path = []

while lis and lis_length:
    num, idx = lis.pop()
    if idx == lis_length:
        path.append(num)
        lis_length -= 1

print(len(path))
print(*path[::-1])
