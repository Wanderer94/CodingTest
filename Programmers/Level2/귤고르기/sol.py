def solution(k, tangerine):
    answer = 0
    T = {}
    for i in tangerine:
        if i in T:
            T[i] += 1
        else:
            T[i] = 1
    T = dict(sorted(T.items(), key=lambda x: x[1], reverse=True))
    for i in T:
        if k<=0:
            return answer
        k-=T[i]
        answer+=1
    return answer
    return answer