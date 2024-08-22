def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    board_map = [ [0]*(col+1) for _ in range(row+1)]
    for  i in range(row):
        for j in range(col):
            board_map[i+1][j+1] = board[i][j]
    for i in range(1, row+1):
        for j in range(1, col+1):
            if  board_map[i][j] != 0:
                board_map [i][j] = min(board_map[i-1][j], board_map[i][j-1], board_map[i-1][j-1]) + 1
                answer = max(answer, board_map[i][j])
    return answer**2