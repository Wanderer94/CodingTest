```py
# 최초
def solution(number, limit, power):
    answer = 0
    arr = [i+1 for i in range(number)]
    for i in arr:
        count = 1
        for j in range(1,i):
            if i % j == 0:
                count += 1
            if count > limit:
                break
        if count > limit:
            arr[arr.index(i)] = power
        else:
            arr[arr.index(i)] = count

    answer = sum(arr)
    return answer
```

1. index를 굳이 활용할 필요가 없었다
2. 두번째 for문의 범위가 중요했는데 중간지점, 즉 제곱근까지의 범위만 실행하면 나머지는 다 알 수 있는 구조였다.
3. break는 적절했다 limit을 넘어가게 되면 power로 선언해주기만 하면 된다

sol.py가 최종 수정 답안
