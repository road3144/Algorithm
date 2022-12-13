def solution(survey, choices):
    answer = ''
    n = len(survey)
    indicator = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(n):
        front, rear = survey[i]
        score = choices[i]
        if score < 4:
            indicator[front] += abs(score-4)
        elif score > 4:
            indicator[rear] += score - 4
    if indicator['R'] < indicator['T']:
        answer += 'T'
    else:
        answer += 'R'
    if indicator['C'] < indicator['F']:
        answer += 'F'
    else:
        answer += 'C'
    if indicator['J'] < indicator['M']:
        answer += 'M'
    else:
        answer += 'J'
    if indicator['A'] < indicator['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer


survey = ["TR", "RT", "TR"]
choice = [7, 1, 3]
print(solution(survey, choice))
