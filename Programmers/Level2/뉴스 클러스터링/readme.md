- 간단한 문제라고 생각했는데 다음 내용이 문제였다.
- 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다.
- 구현에는 어려움이 없으나 적절한 데이터 구조를 어떤 것을 선택해야할 지에 대한 고민이 커졌다.
- Counter 타입을 선언해서 dict로 갯수를 파악하면 되겠다고 생각해 다음과 같이 구현했다.

```py
from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    # 문자열 정제 , 대문자 소문자 같이 upper
    # 문자열 배열화 2개씩 합쳐서 만약에 특수문자있으면 pass
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i]+str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            arr2.append(str2[j]+str2[j+1])
    # 자카드 유사도 계산
    Counter1 = Counter(arr1)
    Counter2 = Counter(arr2)
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

```
