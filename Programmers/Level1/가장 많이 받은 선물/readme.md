```py
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
                # 선물 주고 받은 기록으로 선물주기
                if gift_table[x][y] > gift_table[y][x]:
                    print(x, y)
                    friend_point[x] += 1
                # 선물기록이 없을때 혹은 같은경우
                if gift_table[x][y] == gift_table[y][x]:
                    if col_sum[x] - row_sum[x] > col_sum[y] - row_sum[y]:
                        friend_point[x] += 1
    answer = max(friend_point)
    return answerimport numpy as np

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
                # 선물 주고 받은 기록으로 선물주기
                if gift_table[x][y] > gift_table[y][x]:
                    print(x, y)
                    friend_point[x] += 1
                # 선물기록이 없을때 혹은 같은경우
                if gift_table[x][y] == gift_table[y][x]:
                    if col_sum[x] - row_sum[x] > col_sum[y] - row_sum[y]:
                        friend_point[x] += 1
    answer = max(friend_point)
    return answer
```

- 최초로 제출한 답안이다
- 테스트 케이스들은 돌아갔지만 기본적으로 문제가 있다. for 루프가 2번 돌아가게 되어서 런타임에러가 나게 된다.
- 없는 값이 들어갔을때의 문제에 대해서 고민하지 못했다 dict형을 사용해서 해당 경우를 막았어야한다.

```py
def solution(friends, gifts):
    answer = 0
    length = len(friends)
    friend_point = [0 for _ in range(length)]
    # 선물내역 정리
    gift_table = [[0] * length for _ in range(length)]
    for gift in gifts:
        x = friends.index(gift.split(' ')[0])
        y = friends.index(gift.split(' ')[1])
        gift_table[x][y] += 1
    # 계산하기
    for x in range(length):
        for y in range(x + 1, length):
            give_score = gift_table[x][y]
            get_score = gift_table[y][x]
            # 선물을 주고 받은 경우
            if (give_score != get_score) and (give_score > 0 or get_score > 0):
                if give_score > get_score:
                     friend_point[x] += 1
                else:
                     friend_point[y] += 1
            # 선물 지수로 계산
            else:
                giver_score = sum(gift_table[x])
                getter_score = sum(gift_table[y])
                for k in range(length):
                    giver_score -= gift_table[k][x]
                    getter_score -= gift_table[k][y]
                if giver_score > getter_score:
                    friend_point[x] += 1
                elif giver_score < getter_score:
                    friend_point[y] += 1
    answer = max(friend_point)
    return answer
```

- 위의 결과는 for 루프를 돌릴때 위쪽에서만 계산하는 경우이다 즉, 서로간의 비교를 단 한번만 진행하여 횟수를 줄였다.
