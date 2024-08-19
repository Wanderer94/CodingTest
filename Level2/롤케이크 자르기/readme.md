```py
def solution(topping):
    answer = 0
    for i in range(1,len(topping)):
        A = set(topping[0:i])
        B = set(topping[i:])
        if len(A) == len(B):
            answer += 1
    return answer
```

- 오랜만에 풀게된 문제라 더 어색했다.
- n^2의 시간복잡도를 가지는 set() 함수를 사용해서 품.
- 구현 자체는 시도했지만 시간 초과 문제에 걸리게 되었음.
- 이럴때는 역시 자료구조에 대해서 고민을 해보는게 맨 처음 시도
- dict자료형을 사용해보자!

```py
def solution(topping):
    answer = 0
    # 철수 케이크
    bro1 = {}
    for t in topping:
        if t in bro1:
            bro1[t] += 1
        else:
            bro1[t] = 1

    #동생 케이크
    bro2 = {}
    for t in topping:
        # 둘의 딕셔너리 크기가 같다면 동일한 크기로 나눈거
        if len(bro2) == len(bro1):
            answer += 1
        # 동생 케이크에 해당 토핑이 없다면 토핑 추가
        if t not in bro2:
            bro2[t] = 1

        # 철수 토핑에는 하나 빼주기
        bro1[t] -= 1
        # 만약 철수가 해당 토핑을 아예 가지고 있지 않다면 제거
        if bro1[t] == 0:
            del bro1[t]

    return answer

```
