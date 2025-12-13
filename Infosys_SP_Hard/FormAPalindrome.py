"""
IMPORTANT:                                                                                             DYNAMIC PROGRAMMING PATTERN

Form a palindrome
Difficulty: MediumAccuracy: 45.4%Submissions: 117K+Points: 4
Given a string, find the minimum number of characters to be inserted to convert it to a palindrome string.

Examples :

Input: str = "abcd"
Output: 3
Explanation: Inserted character marked with bold characters in dcbabcd, here we need minimum three characters to make it palindrome.
Input: str = "aa"
Output: 0
Explanation: "aa" is already a palindrome.
Constraints:
1 ≤ |str| ≤ 500
str contains only lowercase alphabets.

TC & SPACE COMP = O(N^2)
#User function Template for python3
"""

class Solution:
    def countMin(self, str):
        # code here
        n = len(str)
        rev_s = str[::-1]
        
        dp = [[0] * (n + 1) for _ in range(n + 1)] 
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == rev_s[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
            
        lps = dp[n][n]
        
        return n - lps
