```py
def solution(s):
    count = 0
    times = 0
    while len(s) > 1:
        count += s.count('0')
        s = len(s.replace('0',''))
        s = format(s, 'b')
        times += 1
    answer = [times,count]
    return answer
```

- 최초로 이진수를 주기 때문에 행동의 순서를 잘 생각 해 볼 필요가 있다.
- replace 함수를 사용하여 '0'을 제거하고 len() 함수를 사용하여 다시 이진수로 변환해야 하므로, times +=1을 해준다.
- count 함수를 사용하여 '0'의 갯수를 구한다.
- while 문을 사용하여 s가 1이 될 때까지 반복한다.
- return answer에 [times,count]를 넣어서 결과를 출력한다.
