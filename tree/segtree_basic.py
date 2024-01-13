# 세그먼트 트리 기본

data = [1, 2, 5, 3, 9, 6, 5, 3, 2]
print("data : ", data)

stree = [0 for _ in range(4 * len(data))]


def build(node, left, right):
    if left == right:
        stree[node] = data[left]
        return stree[node]
    mid = (left + right) // 2
    stree[node] = build(node * 2, left, mid) + build(node * 2 + 1, mid + 1, right)
    return stree[node]


build(1, 0, len(data)-1)

print("==segment tree==")
print(stree[1])
print(stree[2], stree[3])
print(stree[4], stree[5], stree[6], stree[7])
print(stree[8], stree[9], stree[10], stree[11], stree[12], stree[13], stree[14], stree[15])
print(stree[16], stree[17])


def query(start, end, node, left, right):
    # 현재 탐색 구간에 target이 아예 없는 경우 무시
    if end < left or right < start:
        return 0

    # 현재 탐색 구간이 target에 모두 포함 되는 경우 현재 노드 반환
    if start <= left and right <= end:
        return stree[node]

    mid = (left + right) // 2
    return query(start, end, node*2, left, mid) + query(start, end, node*2+1, mid+1, right)


print("===query===")
print("sum 0 to 5 :", query(0, 5, 1, 0, len(data)-1))


def update(idx, val, node, left, right):
    # 현재 탐색 구간에 target이 없으면 그대로 반환
    if idx < left or right < idx:
        return stree[node]

    # target 발견
    if left == right:
        stree[node] = val
        return stree[node]

    mid = (left + right) // 2
    stree[node] = update(idx, val, node * 2, left, mid) + update(idx, val, node * 2 + 1, mid + 1, right)
    return stree[node]


update(3, 100, 1, 0, len(data)-1)
print("==update==")
print(stree[1])
print(stree[2], stree[3])
print(stree[4], stree[5], stree[6], stree[7])
print(stree[8], stree[9], stree[10], stree[11], stree[12], stree[13], stree[14], stree[15])
print(stree[16], stree[17])
