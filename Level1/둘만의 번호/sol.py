def solution(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(ord('a'),ord('z')+1)]
    #알파벳 정리
    for i in skip:
        arr.remove(i)
    # index조건 정리
    arr += arr
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