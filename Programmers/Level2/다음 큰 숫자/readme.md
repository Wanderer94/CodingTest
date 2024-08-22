```py
def solution(n):
    answer = 0
    # 이진수로 변환 format 사용
    n_count = format(n, 'b').count('1')
    # n보다 큰 숫자를 찾기위해 조건 투입
    for i in range(n+1 ,1000001):
        i_count = format(i, 'b').count('1')
        if i_count == n_count:
            answer = i
            break
    return answer
```

- 위 문제를 푸는데 처음 든 생각은 이진수를 찾는 함수를 만드는 것이었다.
- 하지만 레퍼런스에도 등장하듯이 이미 이진수를 만드는 함수가 존재하고 심지어 이를 문자열로 표기하는 방법도 있었다.
- 방법은 간단했다 n보다 큰 범위 부터 조건에 있는 1,000,000까지 for 문을 돌리는데 해당하는 수를 찾으면 break를 걸어주는 것이었다.
