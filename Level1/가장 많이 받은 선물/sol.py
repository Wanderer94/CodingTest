import numpy as np

def solution(friends, gifts):
    answer = 0
    friend_point = [0 for i in range(len(friends))]
    gift_table = np.zeros((5,5))
    for gift in gifts:
        x = friends.index(gift.split(' ')[0])
        y = friends.index(gift.split(' ')[1])
        gift_table[x][y] += 1
    col_sum = gift_table.sum(axis = 1)
    row_sum = gift_table.sum(axis = 0)
    print(gift_table, col_sum, row_sum )
    for x in range(len(friends)):
        for y in range(len(friends)):
            if x != y:
                # 선물 주고 받은 기록으로 선물주기
                if gift_table[x][y] > gift_table[y][x]:
                    print(x, y)
                    friend_point[x] += 1
                # 선물기록이 없을때 혹은 같은경우
                if gift_table[x][y] == gift_table[y][x]:
                    if col_sum[x] - row_sum[x] > col_sum[y] - row_sum[y]:
                        print(x,y)
                        friend_point[x] += 1
    answer = max(friend_point)
    return answer