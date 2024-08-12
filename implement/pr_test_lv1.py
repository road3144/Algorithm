def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    hits = [0] * 4
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            hits[1] += 1
        if answers[i] == second[i%8]:
            hits[2] += 1
        if answers[i] == third[i%10]:
            hits[3] += 1
    m = max(hits)
    for i in range(1, 4):
        if hits[i] == m:
            answer.append(i)
    return answer
