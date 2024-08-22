def solution(X, Y):
    answer = ''
    a = []
    #count num
    X_a = [0 for _ in range(10)]
    Y_a = [0 for _ in range(10)]
    for i in X:
        X_a[int(i)] += 1
    for i in Y:
        Y_a[int(i)] += 1
    #check num
    X = list(set(list(X)))
    Y = list(set(list(Y)))
    for i in X:
        if i in Y:
            count = min(X_a[int(i)],Y_a[int(i)])
            for j in range(count):
                a.append(i)
    if len(a) == 0:
        return "-1"
    a.sort(reverse = True)
    for i in a:
        answer += i
        if answer[-1] == '0':
            return answer
    return answer