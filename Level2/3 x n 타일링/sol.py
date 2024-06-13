def solution(n):
    mod = 10**9+7
    # 홀수 제외
    n //= 2
    # 최초 값 설정
    dp = [0] * (n+1)
    dp[1]= 3
    dp[2]= 11
    for i in range(3, n+1):
            dp[i] = (3 * dp[i-1] + 2 * sum(dp[:i-1]) + 2) % mod
    return dp[-1]