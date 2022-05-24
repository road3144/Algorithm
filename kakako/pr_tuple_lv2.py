def solution(s):
    answer = []
    s = s[2:len(s)-2]
    data = s.split('},{')
    n = len(data)
    for i in range(n):
        data[i] = set(map(int, data[i].split(',')))
    data.sort()
    for i in data:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
