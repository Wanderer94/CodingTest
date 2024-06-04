def solution(sizes):
    answer = 0
    w =[]
    h = []
    for i in sizes:
        i.sort()
        w.append(i[0])
        h.append(i[1])
    answer = max(w) * max (h)
    return answer