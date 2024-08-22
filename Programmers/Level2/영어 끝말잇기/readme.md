```py
def solution(n, words):
    answer = [0,0]
    last_word = words[0]
    for i in range(len(words)):
        times = i // n
        player = i % n
        if words[i].startswith(last_word[-1]):
            answer[0] = player
            answer[1] = times
            break
    return answer
```

- 우선 시작글자와 끝 글자가 다른 경우에 대해서 생각해보려했는데 중복해서 나오는 경우에 시간 복잡도를 감당하기가 어려울 것 같아 데이터 구조를 뭘 써야할 지 고민했다.

```py
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]
```

- 앞에 있는 단어중에 존재하는 지만 확인하면 된다.
