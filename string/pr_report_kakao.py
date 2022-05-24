import sys
from collections import deque

input = sys.stdin.readline

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {id: [] for id in id_list}

    for i in set(report):
        history = i.split()
        reported[history[1]].append(history[0])

    for key, value in reported.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1
    return answer


print(solution(id_list, report, k))
