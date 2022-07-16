import sys
input = sys.stdin.readline

stack1 = list(input().strip())
stack2 = []
n = int(input())

for i in range(n):
    args = input().split()
    commend = args[0].strip()
    if len(args) >= 2:
        item = args[1].strip()
    if commend == 'L' and stack1:
        stack2.append(stack1.pop())
    if commend == 'D' and stack2:
        stack1.append(stack2.pop())
    if commend == 'B' and stack1:
        stack1.pop()
    if commend == 'P':
        stack1.append(item)

print(''.join(stack1 + list(reversed(stack2))))
print('hi')
