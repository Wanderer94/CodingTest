def solution(n):
    answer = 0
    # 이진수로 변환 format 사용
    n_count = format(n, 'b').count('1')
    # n보다 큰 숫자를 찾기위해 조건 투입
    for i in range(n+1 ,1000001):
        i_count = format(i, 'b').count('1')
        if i_count == n_count:
            answer = i
            break
    return answer