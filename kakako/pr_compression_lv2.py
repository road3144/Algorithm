def solution(msg):
    answer = []
    mDic = {}
    for i in range(1, 27):
        mDic[i] = chr(i+64)
    i = 27
    while msg != '':
        w = msg[0]
        if len(msg) < 2:
            c = ''
        else:
            c = msg[1]
        cnt = 2
        while w + c in mDic.values() and len(msg) >= cnt:
            w += c
            if len(msg) == cnt:
                c = ''
            else:
                c = msg[cnt]
            cnt += 1
        for k, v in mDic.items():
            if v == w:
                answer.append(k)
        mDic[i] = w + c
        i += 1
        msg = msg[len(w):]

    return answer


msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))