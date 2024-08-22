```py
def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = lcm(answer,arr[i])
    return answer

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
```

- 다음과 같이 최소공배수와 다음 수사이의 최소공배수를 계속해서 구해주는 식으로 구현이 가능하다.
- lcm(A,B) = (A\*B)/gcd(A,B)
- gcd(A,B)는 A와 B의 공약수 중 최대값을 의미한다.
- lcm(A,B)는 A와 B의 곱을 구한 후, A와 B를 나누어주면 된다.
