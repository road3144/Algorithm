def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    if not arr:
        arr = [-1]
    return arr
