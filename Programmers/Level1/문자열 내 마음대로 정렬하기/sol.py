def solution(strings, n):
    answer = []
    
    for i in range(len(strings)):
        for j in range(i ,len(strings)):
            if strings[i][n] > strings[j][n]:
                ans = strings[i]
                strings[i] = strings[j]
                strings[j] = ans
            elif strings[i][n] == strings[j][n]:
                if strings[i] > strings[j]:
                    ans = strings[i]
                    strings[i] = strings[j]
                    strings[j] = ans
    answer = strings
    return answer
#람다에 대해서 ~ http://goo.gl/IjKPF6

