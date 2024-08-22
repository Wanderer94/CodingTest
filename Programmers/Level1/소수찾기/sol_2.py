def solution(n):
    answer = 0
    ans = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if ans[i] == True:
            for j in range(i+i,n+1,i):
                ans[j] = False
    answer = ans[2:].count(True)
    return answer