def solution(n):
    answer = 0
    i = 0
    while i * i < n:
        i += 1
        if i * i == n:
            answer = (i+1) * (i+1)
    if answer == 0:
        answer -= 1
    return answer
