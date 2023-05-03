def solution(s):
    answer = 0
    same = 0
    dif = 0
    x = s[0]
    for i in s:
        if same == dif:
            answer += 1
            x = i
        if i == x:
            same += 1
        elif i != x:
            dif += 1
    return answer