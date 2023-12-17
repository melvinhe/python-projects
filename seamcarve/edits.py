def edit_distance_fwd(word1, word2):
    word1 = word1.casefold()  # Convert word1 to lowercase
    word2 = word2.casefold()  # Convert word2 to lowercase
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]            
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    
                                   dp[i][j-1],    
                                   dp[i-1][j-1])  

    return dp[m][n]

# ----------------------------------------------------------

def edit_distance_bwd(word1, word2):
    word1 = word1.casefold()  # Convert word1 to lowercase
    word2 = word2.casefold()  # Convert word2 to lowercase
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initializing the last row and column of the table
    for i in range(m+1):
        dp[i][n] = m - i
    for j in range(n+1):
        dp[m][j] = n - j

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # if characters are same the at indices (i for word1, j for word2) in both words, 
            # then no operation is required and the value at dp[i][j] will be same as dp[i+1][j+1] (bottom right stored value)
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]          
            else:
            # if characters are different at indices (i for word1, j for word2) in both words, 
            # then we need to find the minimum of the three values at dp[i+1][j], dp[i][j+1] and dp[i+1][j+1] and add 1
                dp[i][j] = 1 + min(dp[i][j+1],   # corresponds to stored distance value for next column (insertion cost)
                                    dp[i+1][j],   # corresponds to stored distance value for next row (deletion cost)
                                    dp[i+1][j+1]) # corresponds to stored distance value for next diagonal (substitution cost)

    return dp[0][0]