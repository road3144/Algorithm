for test_case in range(1, 10 + 1):
    n = int(input())
    building = list(map(int, input().split()))
    answer = 0
    for i in range(2, n-2):
        max_near = max(building[i-2], building[i-1], building[i+1], building[i+2])
        if building[i] >= max_near:
            answer += building[i] - max_near

    print('#' + str(test_case), answer)