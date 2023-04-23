def solution(a, b):
    answer = 0
    if a <= b:
        answer = sum(range(a,b+1))
        #for i in range(a, b+1): 
        #    answer = answer + i
    if b < a:
        answer = sum(range(b,a+1))
        #for i in range(b, a+1):
        #    answer = answer + i
    return answer
#sum(range) 에 대한 학습이 필요