def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if i in cards1 and cards1.index(i) == 0:
            cards1.pop(0)
        elif i in cards2 and cards2.index(i) == 0 :
            cards2.pop(0)
        else:
            answer = 'No'
            break
    return answer