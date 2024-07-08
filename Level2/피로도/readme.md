```py
def solution(k, dungeons):
    answer = -1
    dungeons.sort
    # for d in 던전 해서 모든 던전의 경우의 수를 계산한다.
    return answer
```

- 해당 방식을 구현 해보려 했는데 문제가 발생했다. 시간내에 다 작성이 안되는 문제가 발색
- 이런 경우 백트래킹으로 풀었어야하는것을 기억하고 적용

```py
answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer
출처: https://alreadyusedadress.tistory.com/294 [ :티스토리]
```
