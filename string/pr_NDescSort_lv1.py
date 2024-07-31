def solution(n):
    answer = 0
    a = list(map(int, str(n)))
    a.sort()
    a.reverse()
    a = ''.join(map(str, a))
    answer = int(a)
    return answer
