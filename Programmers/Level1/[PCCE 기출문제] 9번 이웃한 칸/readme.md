```py
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
```

- 다음과 같이 결과를 도출 해 볼 수 있다.
- 순간 놓쳤던 부분은 보드의 길이가 1에서 7사이라는것
- 결국 비교할떄는 length를 사용해서 비교했어야 한다!
