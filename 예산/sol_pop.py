#pop에 대해서 생각해보기
def solution(d, budget):
    d = sorted(d)
    while sum(d) > budget:
        d.pop()   
    return len(d)