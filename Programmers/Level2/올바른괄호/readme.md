```py
def solution(s):
    answer = True
    queue = list()
    for word in s:
        if word == '(':
            queue.append(word)
        elif word == ')' and len(queue) != 0:
            if queue[-1] == '(':
                queue.pop()
    if queue:
        answer = False
    return answer
```

- 해당 방식에서 문제점은 최초로 ) 가 나오면, 이미 queue에 (가 존재하지 않아서 pop을 할 수 없다는 것입니다.
- 따라서, queue에 맨처음 요소를 입력하고 이후의 과정을 풀이하는 식으로 변형하였습니다.

```py
def solution(s):
    answer = True
    queue = list()
    queue.append(s[0])
    for i in range(1, len(s)):
        if s[i] == '(':
            queue.append(s[i])
        elif s[i] == ')' and len(queue) != 0:
            if queue[-1] == '(':
                queue.pop()
    if queue:
        answer = False
    return answer
```

- 이렇게 하면 , (가 나오기 전에 ) 가 나온 경우를 고려할 수 있게 되었습니다.
