```py
def solution(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(ord('a'),ord('z')+1)]
    #알파벳 정리
    for i in skip:
        arr.remove(i)
    print(arr)
    #변환 시작
    for i in s:
        i = arr.index(i)
        if i + index >= len(arr):
            i = i + index - len(arr)
        else:
            i = i + index
        answer += arr[i]
    return answer
```

1. 위의 초기 코드의 경우 런타임 에러가 났다 index조건과 skip의 길이 차이인듯 하다.
2. 즉 예를 들어서 다음과 같은 상황이 날 수 있다는 것이다. 경계값에 대해 생각을 해보면 skip이 최대 10개의 단어, index는 최대 20이기 때문에 이 과정에서 범위를 벗어나 에러가 생길 수 있다
3. 예를 들어 skip이 10이라 10개의 단어를 없애 마지막 단어의 index가 alphabet[15]라고 가정 해보면 index가 20이라면 마지막 단어는 15+20=35 를 가리키게 되고 여기서 단어의 길이 만큼 빼면 35-16=19로 범위를 초과하게 된다.
4. 간단한 해결 방법은 arr을 두번 연속하여 충분한 길이의 배열을 만들어 주는 것이다.
