def solution(numbers):
    answer = sum(range(0,10))
    n = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in n:
            answer -= i
    return answer