n = int(input())
values = []
for i in range(n):
    values.append(input())


def braces(values):
    k = len(values)
    result = []

    for j in range(k):
        stack = []
        res = 0
        for brace in values[j]:
            if brace in '{[(':
                stack.append(brace)
            elif brace in '}])':
                if not stack:
                    result.append('NO')
                    res += 1
                    break
                else:
                    open_br = stack.pop()
                    if (open_br == '{' and brace != '}') or (open_br == '[' and brace != ']') or (
                            open_br == '(' and brace != ')'):
                        result.append('NO')
                        res += 1
                        break

        if res == 0:
            if not stack:
                result.append('YES')
            else:
                result.append('NO')
    return result


print(braces(values))
