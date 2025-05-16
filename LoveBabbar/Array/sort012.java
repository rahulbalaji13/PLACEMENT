/**
Sort 0s, 1s and 2s
Difficulty: MediumAccuracy: 50.58%Submissions: 770K+Points: 4Average Time: 10m
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 2

Expected Complexities
Company Tags
PaytmFlipkartMorgan StanleyAmazonMicrosoftOYO RoomsSamsungSnapdealHikeMakeMyTripOla CabsWalmartMAQ SoftwareAdobeYatra.comSAP LabsQualcomm
**/

//DUTCH NATIONAL FLAG ALGORITHM

class Solution 
{
    // Function to sort an array of 0s, 1s, and 2s
    public void sort012(int[] arr) 
    {
        // code here
        int temp = 0;
        int n = arr.length;
        
        int lo = 0;
        int hi = n - 1;
        int mid = 0;
        
        while(mid <= hi)
        {
           if(arr[mid] == 0)
           {
               swap(arr,mid,lo);
               lo++;
               mid++;
           }
           else if(arr[mid] == 1)
           {
               mid++;
           }
           else if(arr[mid] == 2)
           {
               swap(arr,mid,hi);
               hi--;
           }
        }
    }

    //TIME COMPLEXITY: O(N) 
    //SPACE COMPLEXITY: O(1)
