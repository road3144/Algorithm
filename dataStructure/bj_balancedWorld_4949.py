import sys

input = sys.stdin.readline


def is_balanced(s):
    stack = []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        if i == ")" or i == "]":
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if (i == ")" and temp != "(") or (i == "]" and temp != "["):
                return False
    if len(stack) >= 1:
        return False
    return True


while True:
    sentence = input().rstrip()[:-1]
    if sentence == "":
        break
    if is_balanced(sentence):
        print("yes")
    else:
        print("no")
