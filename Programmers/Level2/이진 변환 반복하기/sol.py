def solution(s):
    count = 0
    times = 0
    while len(s) > 1:
        count += s.count('0')
        s = len(s.replace('0',''))
        s = format(s, 'b')
        times += 1
    answer = [times,count]
    return answer