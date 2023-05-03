def solution(number, limit, power):
    answer = 0
    arr = [i+1 for i in range(number)]
    for i in arr:
        count = 1
        for j in range(1,i):
            if i % j == 0:
                count += 1
            if count > limit:
                break
        if count > limit:
            arr[arr.index(i)] = power
        else:
            arr[arr.index(i)] = count
            
    answer = sum(arr)
    return answer