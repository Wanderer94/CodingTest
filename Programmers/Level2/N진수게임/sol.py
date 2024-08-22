def solution(n, t, m, p):
    answer = '0'
    result = ''
    i = 0
    while (len(answer) < m*t):
        answer += cal(n, i)
        i += 1
    for i in range(m*t):
        if i % m == p - 1:
            result += answer[i]
            print(i)
    return result


def cal(n, idx):
    index = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    result = '' 
    while(idx > 0):
        remainder = idx % n
        idx = idx // n # 몫 quotient
        result = index[remainder] + result
    return result