```py
def solution(n, t, m, p):
    answer = '0'
    result = ''
    i = 0
    while (len(answer) < m*t):
        answer += cal(n, i)
        i += 1
    for i in range(m*t):
        if i % m == p - 1:
            result += answer[i]
            print(i)
    return result


def cal(n, idx):
    index = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    result = ''
    while(idx > 0):
        remainder = idx % n
        idx = idx // n # 몫 quotient
        result = index[remainder] + result
    return result
```

- 인덱스를 잡는데 애먹었던 문제
- 2 ~ 16진수까지 커버해야하기에 어떻게 해결할까 하다가 index배열을 생성해서 해결
- cal 함수는 n의 진법으로 idx를 변환하는 함수이고, 나머지를 index 배열에서 찾아서 result에 더해주는 방식으로 구현
- 0부터 숫자를 외치기 때문에 answer에 '0'을 추가하고 시작한다.
