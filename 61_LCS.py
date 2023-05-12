def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    # Create a table to store the lengths of LCS of substrings
    dp_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    # LCS length is the value in the bottom-right cell of the table
    return dp_table[m][n]
