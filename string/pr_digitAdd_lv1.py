def solution(n):
    answer = 0

    str_num = str(n)
    for i in str_num:
        answer += int(i)

    return answer
