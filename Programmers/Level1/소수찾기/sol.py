def solution(n):
    answer = 0
    ans = list(range(1,n+1))
    for i in range(1, n+1):
        for j in ans:
            if j % i == 0 and j != i:
                ans.remove(j)
    answer = len(ans)
    
    
    
    return answer

def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

#미해결 문제
