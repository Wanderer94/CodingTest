def solution(m, n, puddles):
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # Initialize home cell as 1
    dp[1][1] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (i == 1 and j == 1): continue
            
            # Ignore flooded cells
            if [i, j] in puddles: 
                dp[i][j] = 0
                
            else:
                # Add shortest distances from top or left cell
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
                # Take modulo to prevent overflow
                dp[i][j] %= 1000000007
                
    return dp[m][n]