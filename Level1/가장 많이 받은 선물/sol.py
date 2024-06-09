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