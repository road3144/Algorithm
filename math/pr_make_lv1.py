def solution(nums):
    answer = 0
    n = len(nums)
    data = [False, False] + [True] * 2999

    for i in range(2, 3001):
        if data[i]:
            for j in range(2 * i, 3000, i):
                data[j] = False

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i != j and j != k and i != k:
                    tmp = nums[i] + nums[j] + nums[k]
                    if data[tmp]:
                        answer += 1
    return answer
