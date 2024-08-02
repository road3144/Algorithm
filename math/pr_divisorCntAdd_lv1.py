def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        j = 1
        cnt = 0
        while j * j <= i:
            if j * j == i:
                cnt += 1
            else:
                cnt += 2
            j += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer
