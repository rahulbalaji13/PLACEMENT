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
        // Get the number of elements in the array
        int n = arr.length;

        // Sort the array to make height modification easier
        Arrays.sort(arr);
        
        // Initialize result with the maximum possible height difference
        int res = arr[n - 1] - arr[0];
        
        // Iterate through the array starting from index 1
        for(int i = 1; i < n; i++)
        {
            // If reducing this height makes it negative, skip modification
            if(arr[i] - k < 0)  
                continue;
        
            // Calculate the possible new minimum height after modification
            int minH = Math.min(arr[0] + k, arr[i] - k);
            
            // Calculate the possible new maximum height after modification
            int maxH = Math.max(arr[i - 1] + k, arr[n - 1] - k);
            
            // Update the result with the smallest height difference found so far
            res = Math.min(res, maxH - minH);
        }
        
        // Return the minimized height difference
        return res;
    }
}

/**
Summary of Logic:
- Sort the array to ensure heights are processed in increasing order.
- Start with the initial maximum difference before modifications.
- Iterate through each element, skipping values where subtraction would create a negative height.
- Adjust heights both upwards and downwards, determining the new min and max values.
- Update the result with the minimum possible difference found in the process.
This approach efficiently minimizes the largest height difference by applying a balanced increase/decrease strategy to elements while ensuring no height becomes negative.


| Iteration (i) | arr\[i] | Condition `arr[i] - k < 0` | `minH = min(arr[0]+k, arr[i]-k)` | `maxH = max(arr[i-1]+k, arr[n-1]-k)` | `maxH - minH` | Updated `res`     |
| ------------- | ------- | -------------------------- | -------------------------------- | ------------------------------------ | ------------- | ----------------- |
| 1             | 9       | No (`9 - 3 = 6 >= 0`)      | `min(3+3, 9-3) = min(6,6) = 6`   | `max(3+3, 20-3) = max(6,17) = 17`    | `17 - 6 = 11` | `min(17,11) = 11` |
| 2             | 12      | No (`12 - 3 = 9 >= 0`)     | `min(3+3, 12-3) = min(6,9) = 6`  | `max(9+3, 20-3) = max(12,17) = 17`   | `17 - 6 = 11` | `min(11,11) = 11` |
| 3             | 16      | No (`16 - 3 = 13 >= 0`)    | `min(3+3, 16-3) = min(6,13) = 6` | `max(12+3, 20-3) = max(15,17) = 17`  | `17 - 6 = 11` | `min(11,11) = 11` |
| 4             | 20      | No (`20 - 3 = 17 >= 0`)    | `min(3+3, 20-3) = min(6,17) = 6` | `max(16+3, 20-3) = max(19,17) = 19`  | `19 - 6 = 13` | `min(11,13) = 11` |
**/
