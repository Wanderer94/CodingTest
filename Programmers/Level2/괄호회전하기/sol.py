def solution(s):
    answer = 0
    length = len(s)
    s += s
    for idx in range(length):
        str_arr = s[idx:idx+length]
        if check_bracket(str_arr):
            answer += 1
    return answer

def check_bracket(s):
    queue = [s[0]]
    for bracket in s[1:]:
        if bracket == '{' or bracket == '(' or bracket == '[':
            queue.append(bracket)
        elif (queue[-1] == '{'and bracket == '}') or (queue[-1] == '('and bracket == ')') or (queue[-1] == '['and bracket == ']'):
            queue.pop()
    return len(queue) == 0