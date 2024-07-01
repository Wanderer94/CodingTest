```py
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        check = discount[i:i+10]
        join = True
        for j in range(len(want)):
            if check.count(want[j]) < number[j]:
                join = False
                break
        if join:
            answer += 1
    return answer
```

- 다음과 같이 해결했다.
- discount의 10개씩 잘라서 want와 number를 비교한다.
- count가 number보다 작으면 join을 False로 바꾼다.
- join이 True면 answer에 1을 더한다. 가입이 가능한 날이라는 뜻이다.
- return answer를 하면 된다.
