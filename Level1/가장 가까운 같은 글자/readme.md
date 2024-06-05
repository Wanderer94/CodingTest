```py
def solution(s):
    answer = [0 for _ in range(len(s))]
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer[i] = -1
            # print("if", answer)
        elif s.find(s[i]) == i:
            answer[i] = -1
        else:
            a = s.find(s[i])
            # print(s[i+1:],a)
            answer[i] = i - a
    return answer

```

1. 이전 코드에 있어서 가장 큰 문제 점은 적절한 자료형을 사용하지 못했다는 점
2. dict 자료형을 이용해서 매번 index값을 최신화 해주는 식으로 계산 가능
3. 앞에 몇번째에 있는지만 파악하면 되기에 뒤에 나온 것과 비교할 필요가 없어
   따라서 최종 답안은 sol에 있다.
