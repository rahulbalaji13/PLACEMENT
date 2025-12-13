"""
Wildcard Pattern Matching
Difficulty: MediumAccuracy: 31.13%Submissions: 96K+Points: 4
Given two strings pat and txt which may be of different sizes, You have to return true if the wildcard pattern i.e. pat, matches with txt else return false.

The wildcard pattern pat can include the characters '?' and '*'.

'?' – matches any single character.
'*' – matches any sequence of characters (including the empty sequence).
Note: The matching should cover the entire txt (not partial txt).

Examples:

Input: txt = "abcde", pat = "a?c*"
Output: true
Explanation: '?' matches with 'b' and '*' matches with "de".
Input: txt = "baaabab", pat = "a*ab"
Output: false
Explanation: The pattern starts with a, but the text starts with b, so the pattern does not match the text.
Input: txt = "abc", pat = "*"
Output: true
Explanation: '*' matches with whole text "abc".
Constraints:
1 ≤ txt.size(), pat.size() ≤ 100
"""
class Solution:
    def wildCard(self, txt, pat):
        n = len(pat)
        m = len(txt)
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        #Base case
        dp[0][0] = True 
        
        for i in range(1, n + 1):
        
            if pat[i - 1] == '*':
        
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = False
                
        # To fill the dp table
        for i in range(1, n + 1): # PATTERN
            for j in range(1, m + 1): # TEXT
                if pat[i - 1] == txt[j - 1] or pat[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                    
                elif pat[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
                    
                    
        return dp[n][m]
        
    
