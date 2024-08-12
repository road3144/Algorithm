def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    box = []
    for i in score:
        if len(box) < m:
            box.append(i)
        if len(box) == m:
            answer += box[-1] * m
            box = []
    return answer
