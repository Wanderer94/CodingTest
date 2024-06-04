def solution(d, budget):
    answer = 0
    d = sorted(d)
    sum_d = 0
    i = 0
    while i < len(d):
        if sum_d <= budget:
            answer = i
        sum_d += d[i]
        i += 1
    if sum(d) <=budget:
        answer = len(d)
        
    return answer