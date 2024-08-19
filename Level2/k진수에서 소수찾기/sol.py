def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

def cal(n,k):
    result = ''
    index = ['0','1','2','3','4','5','6','7','8','9']
    while n > 0:
        result = index[n % k] + result
        n = n // k
    return result

def solution(n, k):
    answer = 0
    num = cal(n,k)
    nums = num.split('0')
    for x in nums:
    	#x가 비어있는 경우를 예외처리 한다
        if x and isPrime(int(x)):
            answer += 1
    return answer