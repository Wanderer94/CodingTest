def solution(s):
    answer = ''
    ans = list(s.split(' '))
    count_ans = 0
    for i in ans:
        count = 0
        for j in i:
            if count % 2 == 0:
                answer += j.upper()
            elif count % 2 == 1:
                answer += j.lower()
            count += 1
        count_ans += 1
        if count_ans < len(ans) :
            answer += ' '
    return answer