def solution(players, callings):
    answer = []
    linked = dict()
    linked[players[0]] = ["", players[1]]
    for i in range(1, len(players) - 1):
        linked[players[i]] = [players[i - 1], players[i + 1]]
    linked[players[len(players) - 1]] = [players[len(players) - 2], ""]

    for calling in callings:
        left_temp = linked[linked[calling][0]][0]
        right_temp = linked[calling][0]
        linked[linked[calling][0]][1] = linked[calling][1]
        if linked[calling][1] != "":
            linked[linked[calling][1]][0] = linked[calling][0]
        if left_temp != "":
            linked[left_temp][1] = calling
        linked[right_temp][0] = calling
        linked[calling][0] = left_temp
        linked[calling][1] = right_temp
    next = ""
    for k, v in linked.items():
        if v[0] == "":
            answer.append(k)
            next = v[1]
    while next != "":
        answer.append(next)
        next = linked[next][1]
    return answer