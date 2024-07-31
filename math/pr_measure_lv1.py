def solution(n):
    answer = 0
    s = set()

    for i in range(1, n + 1):
        if n % i == 0 and i not in s:
            answer += i
            s.add(i)

    return answer
