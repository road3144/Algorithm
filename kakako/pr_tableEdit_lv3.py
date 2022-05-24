def up(k, dis, link):
    for _ in range(dis):
        k = link[k][1]
    return k


def down(k, dis, link):
    for _ in range(dis):
        k = link[k][0]
    return k


def delete(k, link, deleted, OX):
    prev, nex = link[k]
    deleted.append([prev, nex, k])
    OX[k - 1] = "X"

    if nex == len(OX) + 1:
        k = link[k][0]
    else:
        k = link[k][1]

    if prev == 0:
        link[nex][0] = prev
    elif nex == len(OX) + 1:
        link[prev][1] = nex
    else:
        link[prev][1] = nex
        link[nex][0] = prev
    return k


def cancel(deleted, OX, link):
    prev, nex, now = deleted.pop()
    OX[now - 1] = "O"

    if prev == 0:
        link[nex][0] = now
    elif nex == len(OX) + 1:
        link[prev][1] = now
    else:
        link[prev][1] = now
        link[nex][0] = now


def solution(n, k, cmd):
    answer = ''
    link = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    OX = ["O" for _ in range(n)]
    deleted = []
    k += 1
    for i in cmd:
        if len(i) > 2:
            cm, dis = i.split()
            dis = int(dis)
        else:
            cm = i
        if cm == 'D':
            k = down(k, dis, link)
        elif cm == 'U':
            k = up(k, dis, link)
        elif cm == 'C':
            k = delete(k, link, deleted, OX)
        elif cm == 'Z':
            cancel(deleted, OX, link)
        print(link, "////", k)
    for v in OX:
        if v == 'X':
            answer += 'X'
        else:
            answer += 'O'
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))

# def up(k, dis, dic):
#     dic[k] = 'O'
#     while dis != 0:
#         k -= 1
#         if dic[k] == 'X':
#             continue
#         dis -= 1
#     dic[k] = 'K'
#     return k
#
#
# def down(k, dis, dic):
#     dic[k] = 'O'
#     while dis != 0:
#         k += 1
#         if dic[k] == 'X':
#             continue
#         dis -= 1
#     dic[k] = 'K'
#     return k
#
#
# def delete(k, dic, deleted):
#     dic[k] = 'X'
#     deleted.append(k)
#     if is_bottom]:
#         dic[k-1] = 'K'
#         return k-1
#     else:
#         dic[k+1] = 'K'
#         return k+1
#
#
# def cancel(dic, deleted):
#     dic[deleted.pop()] = 'O'
#
#
# def solution(n, k, cmd):
#     answer = ''
#     dic = ['O' for i in range(n)]
#     dic[k] = 'K'
#     deleted = []
#     for i in cmd:
#         if len(i) > 2:
#             cm, dis = i.split()
#             dis = int(dis)
#         else:
#             cm = i
#         if cm == 'D':
#             k = down(k, dis, dic)
#         elif cm == 'U':
#             k = up(k, dis, dic)
#         elif cm == 'C':
#             k = delete(k, dic, deleted)
#         elif cm == 'Z':
#             cancel(dic, deleted)
#     for v in dic:
#         if v == 'X':
#             answer += 'X'
#         else:
#             answer += 'O'
#     return answer