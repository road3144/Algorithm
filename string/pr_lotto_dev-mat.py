lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]

def solution(lottos, win_nums):
    answer = [0] * 2
    ansCnt = 0
    zeroCnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            ansCnt = ansCnt + 1
        if lotto == 0:
            zeroCnt = zeroCnt + 1
    zeroCnt = zeroCnt + ansCnt

    answer[1] = min(6, 7 - ansCnt)
    answer[0] = min(6, 7 - zeroCnt)
    return answer

print(solution(lottos, win_nums))

