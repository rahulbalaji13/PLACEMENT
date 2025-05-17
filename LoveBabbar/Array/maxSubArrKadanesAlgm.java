/**
Kadane's Algorithm
Difficulty: MediumAccuracy: 36.28%Submissions: 1.1MPoints: 4Average Time: 20m
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.
Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
Constraints:
1 ≤ arr.size() ≤ 105
-109 ≤ arr[i] ≤ 104

Expected Complexities
Company Tags
ZohoFlipkartMorgan StanleyAccoliteAmazonMicrosoftSamsungSnapdeal24*7 Innovation LabsCitrixD-E-ShawFactSetHikeHousing.comMetLifeOla CabsOraclePayuTeradataVisaWalmartAdobeGoogleArcesium
**/

class Solution 
{
    int maxSubarraySum(int[] arr) 
    {
        // Your code here
        int n = arr.length;
        
        int maxEnd = arr[0];
        int ans = arr[0];
        
        for(int i = 1; i < n; i++)
        {
            maxEnd = Math.max(arr[i] + maxEnd, arr[i]);
            ans = Math.max(ans, maxEnd); 
        }
        return ans;
    }
}

/**
Example:
Input: arr = [3, -1, 2, -1, 6, -5, 4]

Initialization:
n = 7 (array length)

maxEnd = 3 (starts with the first element)

ans = 3 (stores the maximum sum found so far)

Iteration through the array:
Index	arr[i]	maxEnd = max(arr[i] + maxEnd, arr[i])	ans = max(ans, maxEnd)
1	-1	max(3 + (-1), -1) = 2	max(3, 2) = 3
2	2	max(2 + 2, 2) = 4	max(3, 4) = 4
3	-1	max(4 + (-1), -1) = 3	max(4, 3) = 4
4	6	max(3 + 6, 6) = 9	max(4, 9) = 9
5	-5	max(9 + (-5), -5) = 4	max(9, 4) = 9
6	4	max(4 + 4, 4) = 8	max(9, 8) = 9
Final Output:
return ans = 9

Explanation:
The algorithm maintains a running sum (maxEnd), ensuring we either extend the previous subarray or start a new one.

It updates the global maximum (ans) at each step.

The optimal subarray for this input is [3, -1, 2, -1, 6], which sums to 9.
**/
