def solution(s):
    stack = []
    for string in s:
        if len(stack) == 0 or stack[-1] != string : 
            stack.append(string)
        else:
            stack.pop()
    if len(stack) == 0:
        return 1
    return 0