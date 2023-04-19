def solution(a, b):
    answer = ''
    d = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    mon_d = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = mon_d[0:a-1]
    print (count)
    day = (sum(count) + b) % 7
    answer = d[day-1]
    return answer