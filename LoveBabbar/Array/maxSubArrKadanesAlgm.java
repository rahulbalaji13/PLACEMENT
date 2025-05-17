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
