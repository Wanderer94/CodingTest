def solution(brown, yellow):
    answer = []
    ab = (brown + 4) // 2
    for i in range(ab):
        a = i
        b = ab - i
        if yellow == (a-2)*(b-2):
            answer = [a,b]
    return answer