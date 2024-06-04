def solution(survey, choices):
    answer = ''
    case =[['R','T'], ['C','F'],['J','M'],['A','N']]
    result = [0 for _ in range(4)]
    for i in range(len(survey)):
        a = sorted(survey[i])
        print(a)
        if a != survey[i]:
            b = 4 - choices[i]
            if b < 0:
                result[case.index(a)] += b
            elif b > 0:
                result[case.index(a)] -= b
        if a == survey[i]:
            b = 4 - choices[i]
            if b < 0:
                result[case.index(a)] -= b
            elif b > 0:
                result[case.index(a)] += b
    print(result)
    for i in range(len(result)):
        if result[i] > 0:
            answer += case[i][1]
        elif result[i] < 0:
            answer += case[i][0]
        else:
            answer += min(case[i])
        
    return answer