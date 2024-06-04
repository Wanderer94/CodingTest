def solution(name, yearning, photo):
    answer = []
    point = dict(zip(name,yearning))    # 검색을 위한 자료형 dict
    for i in photo:
        sum_yearning = 0
        for j in i:
            n = point.get(j)
            if n != None:
                sum_yearning += n
        answer.append(sum_yearning)
    return answer