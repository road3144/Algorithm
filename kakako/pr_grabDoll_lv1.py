def grab(i, board):
    for j in range(len(board)):
        if board[j][i] != 0:
            item = board[j][i]
            board[j][i] = 0
            return item
    return 0


def solution(board, moves):
    answer = 0
    basket = []
    last_item = 0
    for i in moves:
        item = grab(i-1, board)
        if item != 0:
            if item == last_item:
                basket.pop()
                answer += 2
                if len(basket) != 0:
                    last_item = basket.pop()
                    basket.append(last_item)
            else:
                basket.append(item)
                last_item = item
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))