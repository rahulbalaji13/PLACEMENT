/**
Minimize the Heights II
Difficulty: MediumAccuracy: 15.06%Submissions: 704K+Points: 4Average Time: 25m
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
Input: k = 3, arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11. 
Constraints
1 ≤ k ≤ 107
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 107

Expected Complexities
Company Tags
MicrosoftAdobe

**/
class Solution 
{
    int getMinDiff(int[] arr, int k) 
    {
        // code here
        int n = arr.length;
        Arrays.sort(arr);
        
        int res = arr[n - 1] - arr[0];
        
        for(int i = 1; i < n; i++)
        {
            if(arr[i] - k < 0)
              
                  continue;
        
            int minH = Math.min(arr[0] + k, arr[i] - k);
            
            int maxH = Math.max(arr[i - 1] + k, arr[n - 1] - k);
            
            res = Math.min(res, maxH - minH);
        }
        return res;
    }
}

/**
| Iteration (i) | arr\[i] | Condition `arr[i] - k < 0` | `minH = min(arr[0]+k, arr[i]-k)` | `maxH = max(arr[i-1]+k, arr[n-1]-k)` | `maxH - minH` | Updated `res`     |
| ------------- | ------- | -------------------------- | -------------------------------- | ------------------------------------ | ------------- | ----------------- |
| 1             | 9       | No (`9 - 3 = 6 >= 0`)      | `min(3+3, 9-3) = min(6,6) = 6`   | `max(3+3, 20-3) = max(6,17) = 17`    | `17 - 6 = 11` | `min(17,11) = 11` |
| 2             | 12      | No (`12 - 3 = 9 >= 0`)     | `min(3+3, 12-3) = min(6,9) = 6`  | `max(9+3, 20-3) = max(12,17) = 17`   | `17 - 6 = 11` | `min(11,11) = 11` |
| 3             | 16      | No (`16 - 3 = 13 >= 0`)    | `min(3+3, 16-3) = min(6,13) = 6` | `max(12+3, 20-3) = max(15,17) = 17`  | `17 - 6 = 11` | `min(11,11) = 11` |
| 4             | 20      | No (`20 - 3 = 17 >= 0`)    | `min(3+3, 20-3) = min(6,17) = 6` | `max(16+3, 20-3) = max(19,17) = 19`  | `19 - 6 = 13` | `min(11,13) = 11` |
**/
