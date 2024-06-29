```py
def solution(elements):
    answer = 0
    arr = elements
    length = len(elements)
    elements += elements
    for case in range(length):
        for idx in range(length):
            result = sum(elements[idx:idx+case])
            arr.append(result)
    answer = len(set(arr))
    return answer

```

- 처음에는 링크드리스트를 만들어야하나 라는 생각을 했지만 문제를 푸는데 시간이 초과 될 것 같아 다른 방법을 생각했다.
- 예상을 해보았을때 elements에서 모두 더하는 경우만 해결 할 수 있으면 되기에 배열을 한번 더 더해서 연속되는 수열을 만들어 주었다.
- 아후 for loop를 두번돌려 첫번째는 몇개의 원소를 더할 것인지, 두번째는 더하기 시작할 인덱스를 구하는 것으로 정의내렸다.
- set()을 사용해서 중복된 수를 제거하고 answer에 저장하였다.
- 이렇게 하면 효과적으로 문제를 해결 할 수 있었다.
