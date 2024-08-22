```py
def solution(cards1, cards2, goal):
    answer = ''
    ans = True
    c1 = []
    c2 = []
    for i in goal:
        if i in cards1 :
            c1.append(cards1.index(i))
        elif i in cards2:
            c2.append(cards2.index(i))
    c1_s = sorted(list(set(c1)))
    c2_s = sorted(list(set(c2)))
    if c1 == c1_s and c2 == c2_s:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer
```

1. 우선 논리상 맞지 않는 부분은 한번 사용하면 다시 사용할 수 없기 때문에 pop해주면 된다. 해당하는 단어가 없으면 바로 break하면 된다.
2. if문의 in조건문에 대해서 고민해 보자
3. 해당 문제의 조건에서 가장 중요한 부분은 '먼저 사용' 되어야한다는 점이다.
4. 따라서 index의 값이 0일때 pop을 하며 논리와 형식을 맞출 필요가 있다.
