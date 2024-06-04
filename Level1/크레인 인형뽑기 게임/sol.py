def solution(board, moves):
    answer = 0
    Q = []
    for i in moves:
        for j in range(5):
            if board[j][i-1] != 0 :
                Q.append(board[j][i-1])
                board[j][i-1] = 0
                a = len(Q)
                Q = Qcase(Q)
                b = len(Q)
                if a != b:
                    answer += 2
                break    
    return answer

def Qcase(Q):
    if len(Q) == 1:
        return Q
    a1 = Q.pop()
    a2 = Q.pop()
    if a1 == a2:
        return Q
    else:
        Q.append(a2)
        Q.append(a1)
    return Q