def solution(s):
    answer = False
    if s.isdecimal() and (len(s) == 4 or len(s) == 6):
        answer = True
    return answer
