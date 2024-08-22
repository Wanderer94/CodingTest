def solution(s):
    answer = True
    queue = list()
    queue.append(s[0])
    for i in range(1, len(s)):
        if s[i] == '(':
            queue.append(s[i])
        elif s[i] == ')' and queue[-1] == '(':
            queue.pop()
    if queue:
        answer = False
    return answer