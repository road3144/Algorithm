import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
data2 = list(map(int, input().split(), ))
result = [0] * (m)


def search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


for i in range(m):
    if search(data2[i], data):
        result[i] = 1
for i in result:
    print(i)

# 자료구조 set 활용 가능 set의 원소 존재 여부 탐색은 O(1)다.
