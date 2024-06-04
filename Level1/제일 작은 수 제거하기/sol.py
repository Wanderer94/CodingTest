def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
    return answer