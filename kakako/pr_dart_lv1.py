def bonus(score, sdt):
    if sdt == 'S':
        return score
    elif sdt == 'D':
        return score ** 2
    elif sdt == 'T':
        return score ** 3


def option(data, op, i, dartResult):
    if op == '#':
        data[i] *= -1
    elif op == '*':
        data[i] *= 2
        if i != 0:
            data[i - 1] *= 2
    return dartResult.lstrip(op)


def solution(dartResult):
    answer = 0
    data = [0, 0, 0]
    for i in range(3):
        if dartResult[1] == '0':
            data[i] = bonus(int(dartResult[0] + dartResult[1]), dartResult[2])
            dartResult = dartResult[3:]
        else:
            data[i] = bonus(int(dartResult[0]), dartResult[1])
            dartResult = dartResult[2:]
        if dartResult != '' and not dartResult[0].isalnum():
            dartResult = option(data, dartResult[0], i, dartResult)
    answer = sum(data)
    return answer


dartResult = '1D2S#10S'
print(solution(dartResult))
