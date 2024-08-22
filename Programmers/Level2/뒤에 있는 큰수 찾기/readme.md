```py
def solution(numbers):
    answer = []
    num_len = len(numbers)
    for i in range(num_len):
        number = numbers[i]
        for j in range(i,num_len):
            if number < numbers[j]:
                answer.append(numbers[j])
                break
            elif j == num_len - 1:
                answer.append(-1)
    return answer
```

- 2중 for문을 사용하여 numbers의 i번째 인덱스부터 j번째 인덱스까지의 요소를 비교합니다.
- 대신 중복을 피하기 위해서 break를 사용하였습니다.
- 하지만 시간 초과가 떠 새로문 방법을 생각해봐야합니다.
- 자료구조? dp?
- stack을 이용해서 문제에 접근해 봅시다.

```py
def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for i in range(len(numbers)):
        target = numbers[i]
       while stack and target > numbers[stack[-1]]:
        answer[stack.pop()] = target
       stack.append(i)
    return answer
```

- stack에 인덱스를 넣어주고, target이 stack의 마지막 요소보다 크면 answer에 target을 넣어주고 pop을 해줍니다.
- 이렇게 하면 시간복잡도가 O(n)으로 줄어듭니다.
