```py
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
```

- 다음과 같은 구조로 시도 했지만 실패했다.
- 문제는 큐가 아니라 스택 구조로 시도했어야한다는점
- 따라서 다음과 같은 구조로 변경했다.

```py
def bracket(s):
        stack = []
        for i in s:
            if len(stack) == 0: stack.append(i)
            else:
                if i == ")" and stack[-1] == "(":   stack.pop()
                elif i == "]" and stack[-1] == "[":   stack.pop()
                elif i == "}" and stack[-1] == "{":   stack.pop()
                else: stack.append(i)
        return 1 if len(stack) == 0 else 0

def solution(s):
    answer = 0

    for i in range(len(s)):
        if bracket(s):  answer +=1
        s = s[1:] + s[:1]
    return answer
```
