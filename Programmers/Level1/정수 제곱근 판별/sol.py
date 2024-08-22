import math
def solution(n):
    answer = 0
    n_sqrt = math.isqrt(n)
    if n_sqrt**2 == n:
        answer = (n_sqrt+1)**2
    else:
        answer = -1
    return answer