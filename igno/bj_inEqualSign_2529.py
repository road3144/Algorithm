from collections import deque

k = int(input())
ineq_sign = list(input().split())
maxSeq = []
minSeq = []
maxMake = 9
minMake = 0
maxStack = deque()
minStack = deque()
for i in ineq_sign:
    maxStack.append(maxMake)
    minStack.append(minMake)
    if i == '>':
        while maxStack:
            v = maxStack.pop()
            maxSeq.append(v)
    elif i == '<':
        while minStack:
            v = minStack.pop()
            minSeq.append(v)
    maxMake -= 1
    minMake += 1
maxStack.append(maxMake)
minStack.append(minMake)
while maxStack:
    v = maxStack.pop()
    maxSeq.append(v)
while minStack:
    v = minStack.pop()
    minSeq.append(v)

for i in maxSeq:
    print(i, end='')
print()
for i in minSeq:
    print(i, end='')