def solution(elements):
    answer = 0
    arr = elements
    length = len(elements)
    elements += elements
    for case in range(length):
        for idx in range(length):
            result = sum(elements[idx:idx+case])
            arr.append(result)
    answer = len(set(arr))
    return answer