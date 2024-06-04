def solution(s):
    answer = [0 for _ in range(len(s))]
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer[i] = -1
            # print("if", answer)
        elif s.find(s[i]) == i:
            answer[i] = -1
        else:
            a = s.find(s[i])
            # print(s[i+1:],a)
            answer[i] = i - a
    return answer