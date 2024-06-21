```py
def solution(n):
    answer = 0

    for i in range(1, n+1):
        sum_val = 0
        for j in range(i, n+1):
            sum_val += j
            if sum_val == n:
                answer += 1
            elif sum_val > n:
                break

    return answer
```

- 정수론에서 봤던 문제 같지만 공식이 생각나지 않아 완전탐색 알고리즘을 사용해서 풀었다.
- i부터 j까지의 합이 n과 같은 경우 answer에 1을 더하고, 합이 n보다 크면 break를 통해 다음 i로 이동한다.
- 이렇게 하면 i가 증가하면서 j의 범위가 줄어드는 것이므로 시간 복잡도는 O(n^2)이 된다.
