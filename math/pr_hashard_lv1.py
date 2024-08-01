def solution(x):
    answer = True
    arr = list(map(int, str(x)))
    if not x % sum(arr) == 0:
        answer = False
    return answer
