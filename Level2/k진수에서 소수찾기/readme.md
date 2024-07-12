```py
def solution(n, k):
    answer = -1
    nk = cal(n,k)
    return answer

def cal(n,k):
    result = ''
    index = ['0','1','2','3','4','5','6','7','8','9']
    while n > 0:
        result = index[n % k] + result
        n = n // k
    return result
```

- 우선 k진수로 변환하기 위해 cal 함수를 사용한다.
- 조건을 살펴보면 다음과 같은 3가지 경우에 대해서 출력하면 된다.
  - 0P0처럼 소수 양쪽에 0이 있는 경우
  - P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
  - 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
  - P처럼 소수 양쪽에 아무것도 없는 경우
- 하지만 문제는 소수여야한다는 점.
- 따라서 에라토네스의 체에 관련된 알고리즘도 함께 사용해야한다.
- 수정된 코드는 다음과 같다

```py
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

def cal(n,k):
    result = ''
    index = ['0','1','2','3','4','5','6','7','8','9']
    while n > 0:
        result = index[n % k] + result
        n = n // k
    return result

def solution(n, k):
    answer = 0
    num = cal(n,k)
    nums = num.split('0')
    for x in nums:
    	#x가 비어있는 경우를 예외처리 한다
        if x and isPrime(int(x)):
            answer += 1
    return answer
```
