def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort()
    wide = 0
    height = 0
    for size in sizes:
        wide = max(wide, size[0])
        height = max(height, size[1])
    answer = wide * height
    return answer
