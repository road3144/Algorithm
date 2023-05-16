for test_case in range(1, 10 + 1):
    n = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(n):
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

    answer = max(boxes) - min(boxes)
    print('#' + str(test_case), answer)

