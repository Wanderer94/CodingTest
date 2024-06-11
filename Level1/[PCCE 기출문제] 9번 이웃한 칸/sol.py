def solution(board, h, w):
    answer = 0
    length = len(board)
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        # 좌표값이 0과 보드의 길이 사이의 값일 경우 확인
        if 0 <= h_check < length and 0 <= w_check < length:
            # 같은 색인지 확인한다.
            if board[h][w] == board[h_check][w_check]:
                answer += 1
    return answer