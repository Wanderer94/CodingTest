```py
def solution(s):
    answer = ''
    numbers = list(map(int, s.split(' ')))
    answer = str(min(numbers)) + ' ' + str(max(numbers))
    return answer
```

- split() 함수를 사용하여 공백을 기준으로 문자열을 분리하고, map() 함수와 int() 함수를 사용하여 문자열을 정수로 변환합니다.
- min()과 max() 함수를 사용하여 최소값과 최대값을 찾습니다.
- str() 함수를 사용하여 정수를 문자열로 변환하고, ' ' 기준으로 answer에 concatenate 합니다.
- return answer를 통해 결과를 출력합니다.
