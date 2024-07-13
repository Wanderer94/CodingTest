```py
def solution(msg):
    answer = []
    diction = { 1: 'A'}
    for l in range(1, len(msg)):
        // loop 두번을 돌리지 않을 수 없을까
        for idx in range(len(msg)) :
            if msg[idx]  in diction:
                msg[idx] + msg[idx + 1] 추가
    return answer
```

- 다음과 같은 구조로 코드를 작성했다
- 가장 큰 고민은 for문을 두번 돌리는것
- 메모이제이션에서 메모리를 사용하는것을 생각해서 for루프를 한번만 돌릴수는 없을지 고민했다.
- 결과는 다음과 같다.

```py
def solution(msg):
    dic = {}

    for i in range(26):
        dic[chr(65+i)] = i+1
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer
```
