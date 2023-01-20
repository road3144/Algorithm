import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
opp = list(map(int, input().split()))
arr = {'+': opp[0], '-': opp[1], '*': opp[2], '/': opp[3]}
arr2 = []

minAns = int(1e9)
maxAns = -int(1e9)


def dfs(k):
    global minAns
    global maxAns
    if k == n-1:
        ans = data[0]
        for i in range(n-1):
            if arr2[i] == '+':
                ans += data[i+1]
            if arr2[i] == '-':
                ans -= data[i+1]
            if arr2[i] == '*':
                ans *= data[i+1]
            if arr2[i] == '/':
                if ans < 0:
                    ans = -(abs(ans) // data[i+1])
                else:
                    ans = ans // data[i+1]

        if minAns > ans:
            minAns = ans
        if maxAns < ans:
            maxAns = ans
        return
    for i in arr.keys():
        if arr[i] > 0:
            arr[i] -= 1
            arr2.append(i)
            dfs(k+1)
            arr2.pop()
            arr[i] += 1


dfs(0)
print(maxAns)
print(minAns)
