import sys

n = int(input())
own = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
order = list(map(int, sys.stdin.readline().rstrip().split()))
own.sort()


def bisearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target == arr[mid]:
            return True
        else:
            start = mid + 1
    return False


for i in order:
    if bisearch(own, i, 0, len(own) -1):
        print("yes")
    else:
        print("no")