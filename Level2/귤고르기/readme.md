```py
def solution(k, tangerine):
    answer = 0
    T = {}
    for i in tangerine:
        if i in T:
            T[i] += 1
        else:
            T[i] = 1
    T = dict(sorted(T.items(), key=lambda x: x[1], reverse=True))
    for i in T:
        if k<=0:
            return answer
        k-=T[i]
        answer+=1
    return answer
    return answer
```

- 중복되는 귤을 크기 기준으로 dict자료형에 넣고 갯수를 확인한다
- 이후 sort과정을 통해서 정렬한다.
- sorted(T.items(), key=lambda x: x[1], reverse=True)
  - lambda 함수는 정렬 기준을 설정하는 부분으로, x[1]은 dict의 value를 기준으로 정렬을 수행한다.
  - reverse=True 는 내림차순으로 정렬을 수행한다.
- for문을 통해서 k가 0이하가 되면 break를 하고 answer를 return한다.
- 그렇지 않다면 k에서 value를 빼고 answer에 +1을 해준다.
- 이 과정을 반복하게되면 k가 0이하가 되는 순간 answer를 return한다.
