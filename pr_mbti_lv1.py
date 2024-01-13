def solution(survey, choices):
    answer = ''
    n = len(survey)
    total = {id: 0 for id in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']}

    for i in range(n):
        score = choices[i]
        if score <= 3:
            total[survey[i][0]] += 4 - score
        else:
            total[survey[i][1]] += score - 4
    if total['R'] >= total['T']:
        answer += 'R'
    else:
        answer += 'T'
    if total['C'] >= total['F']:
        answer += 'C'
    else:
        answer += 'F'
    if total['J'] >= total['M']:
        answer += 'J'
    else:
        answer += 'M'
    if total['A'] >= total['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer