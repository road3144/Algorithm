def check(result, count):
    for k in range(count):
        sliceTemp = result[k:]
        for i in range(1, len(sliceTemp) // 2 + 1):
            checkTemp = sliceTemp[:i]
            if checkTemp == sliceTemp[i:i+i]:
                return False
    return True


def backtrack(count):
    if not check(result, count):
        return -1
    if count == n:
        print(*result, sep='')
        return 0
    for i in range(1, 4):
        result.append(i)
        if backtrack(count + 1) == 0:
            return 0
        result.pop()


n = int(input())
result = []
backtrack(0)