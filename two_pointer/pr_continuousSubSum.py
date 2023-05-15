def solution(sequence, k):
    answer = []
    end = 0
    total = sequence[0]
    n = len(sequence)
    min_len = 1000001
    for start in range(n):
        while end < n and total < k:
            end += 1
            if end != n:
                total += sequence[end]

        if total == k and end - start + 1 < min_len:
            answer.clear()
            answer.append(start)
            answer.append(end)
            min_len = end - start + 1
        total -= sequence[start]

    return answer
