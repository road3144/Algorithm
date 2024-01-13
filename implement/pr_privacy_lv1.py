def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_day = map(int, today.split('.'))
    term_dic = dict()
    for term in terms:
        kind, temp = term.split()
        term_dic[kind] = int(temp)
    n = len(privacies)

    for i in range(n):
        start_day, kind = privacies[i].split()
        s_year, s_month, s_day = map(int, start_day.split('.'))
        s_year += (s_month + term_dic[kind]) // 12
        s_month = (s_month + term_dic[kind]) % 12
        if s_month == 0:
            s_year -= 1
            s_month = 12
        if s_year < t_year:
            answer.append(i+1)
            continue
        elif s_year == t_year:
            if s_month < t_month:
                answer.append(i + 1)
                continue
            elif s_month == t_month:
                if s_day <= t_day:
                    answer.append(i + 1)
                    continue

    return answer


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today, terms, privacies))
