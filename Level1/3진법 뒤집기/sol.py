def solution(n):
    answer = 0
    st = ''
    while n != 0:
        st = str(n%3) + st
        n = int(n / 3)
    st = list(st)
    for i in range(len(st)):
        answer += int(st[i]) * (3**i)
    return answer