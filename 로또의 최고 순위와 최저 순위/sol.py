def solution(lottos, win_nums):
    answer = [] 
    c = 0
    for i in lottos:
        if i in win_nums:
            c += 1
    answer.append(c + lottos.count(0))
    answer.append(c)
    # rank = [6,6,5,4,3,2,1]
    # answer.append(rank[c + lottos.count(0)])
    # answer.append(rank[c])
    for i in range(2):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6        
    return answer
#case는 리스트로 저장해놓고 불러오면된다.
#append대신 닶,닶 이렇게 하면 바로 리스트로 생성됨
