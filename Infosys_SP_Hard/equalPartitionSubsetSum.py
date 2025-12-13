"""
Partition Equal Subset Sum
Difficulty: MediumAccuracy: 30.24%Submissions: 280K+Points: 4
Given an array arr[], determine if it can be partitioned into two subsets such that the sum of elements in both parts is the same.

Note: Each element must be in exactly one subset.

Examples:

Input: arr = [1, 5, 11, 5]
Output: true
Explanation: The two parts are [1, 5, 5] and [11].
Input: arr = [1, 3, 5]
Output: false
Explanation: This array can never be partitioned into two such parts.
Constraints:
1 ≤ arr.size ≤ 100
1 ≤ arr[i] ≤ 200

"""
class Solution:
    def equalPartition(self, arr):
        
        n = len(arr)
        total = sum(arr)
        
        if total % 2 != 0:
            return False
            
        target = total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in arr:
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True 
                    
                    
        
        return dp[target]
        
