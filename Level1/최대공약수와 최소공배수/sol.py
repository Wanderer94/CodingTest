import math
def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    answer.append(n*m/math.gcd(n,m))
    return answer

#유클리드 호제법에 대해서 생각해 보기