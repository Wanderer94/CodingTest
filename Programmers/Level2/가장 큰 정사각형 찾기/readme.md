```py
def solution(board):
    answer = 1234
    length = min(len(board), len(board[0]))
    for n in range(1,length):
        for i in range(n):


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
```

- 위의 코드와 같이 length에 해당하는 크기가 가능한 최대 크기의 정사각형임을 확인 할 수 있다.
- board 테이블을 DP로 사용할 수 있지 않을까 하는 생각이 들었다.

```py
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

```

- 위의 코드로 최대의 정사각형을 구할 수 있다. 만약에 같은 값 3개로 뒤덮여 있다면 정사각형이 성립함을 알 수 있다.
