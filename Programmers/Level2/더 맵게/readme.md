```py
def solution(scoville, K):
    answer = 0
    scoville.sort()
    for idx in range(len(scoville)):
        ...
    return answer
```

- sort 되어야 한다고 생각을 버리지 못했다.
- K보다 작아질 때까지 반복해야 하므로, K보다 작은 인덱스를 찾아야 한다.
- 어떤 자료구조가 있을까 - 힙! 힙을 사용해보자
- heapq 모듈 사용하기!

```py
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # list를 min heap으로 변환
    while scoville[0] < K:
        answer += 1
        new_food = heapq.heappop(scoville) + (2 * heapq.heappop(scoville))
        heapq.heappush(scoville, new_food)
        if len(scoville) == 1 and scoville[0] < K: # 음식을 더 이상 만들 수 없는 경우
            return -1
    return answer

```
