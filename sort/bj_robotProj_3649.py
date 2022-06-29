import sys

input = sys.stdin.readline

while True:
    try:
        x = 10000000 * int(input())
        n = int(input())
        legos = []
        for _ in range(n):
            legos.append(int(input()))

        legos.sort()
        flag = True
        i, j = 0, n-1

        while i < j:
            if legos[i] + legos[j] == x:
                print("yes " + str(legos[i]) + " " + str(legos[j]))
                flag = False
                break
            if legos[i] + legos[j] < x:
                i += 1
            elif legos[i] + legos[j] > x:
                j -= 1
        if flag:
            print("danger")
    except:
        break
