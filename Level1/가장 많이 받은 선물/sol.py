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
    for x in range(len(friends)):
        for y in range(len(friends)):
            if x != y:
                if gift_table[x][y] > gift_table[y][x]:
                    friend_point[x] += 1
                elif gift_table[x][y] == 0 and gift_table[y][x] == 0:
                    if col_sum[x] - row_sum[x] > col_sum[y] - row_sum[y]:
                        print(x,y)
                        friend_point[x] += 1
    answer = max(friend_point)
    return answer