def solution(left, right):
    answer = 0
    nums = [x for x in range(left,right+1)]
    for i in nums:
        c = 0
        for j in range(1,i+1):
            if i % j == 0:
                c += 1
        if c % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer