```py
def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_i = ["code", "date", "maximum", "remain"].index(ext)
    sort_i = ["code", "date", "maximum", "remain"].index(sort_by)
    for d in data:
        # ext 조건이 성립하면 append
        if d[ext_i] < val_ext:
            answer.append(d)
    # sort_by에 해당하는 값을 기준으로 오름차순 정렬
    answer.sort(key=lambda x:x[sort_i])
    return answer
```

- 두가지 조건에 대한 구현문제.
- for루프를 통해 첫번째 조건을 성립하는지 확인
- 이차원 배열에서 기준이 되는 index를 정해주서 sort_by에 해당하는 값으로 정렬
- lambda 함수를 사용하여 sort_i에 해당하는 값을 기준으로 정렬

```py
def solution(data, ext, val_ext, sort_by):
    # 확장자 인덱스
    EXTENSION_INDEX = ["code", "date", "maximum", "remain"].index(ext)
    SORT_BY_INDEX = ["code", "date", "maximum", "remain"].index(sort_by)

    # ext 조건이 성립하는 데이터 필터링
    filtered_data = [d for d in data if d[EXTENSION_INDEX] < val_ext]

    # sort_by에 해당하는 값을 기준으로 오름차순 정렬
    sorted_data = sorted(filtered_data, key=lambda x:x[SORT_BY_INDEX])

    return sorted_data

```

- 위 코드는 리팩토링을 진행한 코드이다.
- ext 조건이 성립하는 데이터를 필터링하고, sort_by에 해당하는 값을 기준으로 오름차순 정렬한다.
- 확장자 인덱스와 sort_by에 해당하는 값의 인덱스를 사용하여 코드를 간결하게 작성하였다.
- 이렇게 하면 ext 조건과 sort_by에 해당하는 값을 기준으로 데이터를 정리할 수 있다.
