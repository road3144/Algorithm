def solution(a, b):
    answer = ''
    for i in range(1, a):
        if i == 2:
            b += 29
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            b += 31
        else:
            b += 30
    if b % 7 == 0:
        answer = "THU"
    elif b % 7 == 1:
        answer = "FRI"
    elif b % 7 == 2:
        answer = "SAT"
    elif b % 7 == 3:
        answer = "SUN"
    elif b % 7 == 4:
        answer = "MON"
    elif b % 7 == 5:
        answer = "TUE"
    elif b % 7 == 6:
        answer = "WED"

    return answer
