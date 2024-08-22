def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n - 1, 3)
        if mod == 0:
            answer += '1'
        elif mod == 1:
            answer += '2'
        elif mod == 2:
            answer += '4'
    answer = answer[::-1]
    return answer