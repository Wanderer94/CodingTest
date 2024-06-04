def solution(s):
    answer = 0
    ss = ''
    ans = ''
    for i in s:
        if i.isdecimal():
            ans += i
            continue
        ss += i
        if ss == 'zero':
            ans += '0'
            ss = ''
        elif ss == 'one':
            ans += '1'
            ss = ''
        elif ss == 'two':
            ans += '2'
            ss = ''
        elif ss == 'three':
            ans += '3'
            ss = ''
        elif ss == 'four':
            ans += '4'
            ss = ''
        elif ss == 'five':
            ans += '5'
            ss = ''
        elif ss == 'six':
            ans += '6'
            ss = ''
        elif ss == 'seven':
            ans += '7'
            ss = ''
        elif ss == 'eight':
            ans += '8'
            ss = ''
        elif ss == 'nine':
            ans += '9'
            ss = ''
    answer = int(ans)
    return answer