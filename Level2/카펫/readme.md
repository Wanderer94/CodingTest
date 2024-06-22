```py
def solution(brown, yellow):
    answer = []
    ab = (brown + 4) // 2
    for i in range(ab):
        a = i
        b = ab - i
        if yellow == (a-2)*(b-2):
            answer = [a,b]
    return answer
```

- 수식으로 풀었을떄 brown과 yellow사이의 조건을 파악하고 해당경우에 대해서 모두 검색했다.
- 즉, 완전 탐색 알고리즘으로 구현했다.
