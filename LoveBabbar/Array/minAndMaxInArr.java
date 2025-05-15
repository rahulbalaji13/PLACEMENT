/**
Min and Max in Array
Difficulty: BasicAccuracy: 68.55%Submissions: 340K+Points: 1Average Time: 10m
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

Examples:

Input: arr[] = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: minimum and maximum elements of array are 1 and 10000.
Input: arr[] = [1, 345, 234, 21, 56789]
Output: 1 56789
Explanation: minimum and maximum element of array are 1 and 56789.
Input: arr[] = [56789]
Output: 56789 56789
Explanation: Since the array contains only one element so both min & max are same.
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <=109

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

| Iteration (i) | `arr[i]` | `min` Before | `max` Before | Condition `arr[i] < min` | `min` After | Condition `arr[i] > max` | `max` After |
| ------------- | -------- | ------------ | ------------ | ------------------------ | ----------- | ------------------------ | ----------- |
| -             | -        | -            | -            | -                        | 1           | -                        | 1           |
| 1             | 345      | 1            | 1            | false                    | 1           | true                     | 345         |
| 2             | 234      | 1            | 345          | false                    | 1           | false                    | 345         |
| 3             | 21       | 1            | 345          | false                    | 1           | false                    | 345         |
| 4             | 56789    | 1            | 345          | false                    | 1           | true                     | 56789       |

**/

class Solution {
    public Pair<Integer, Integer> getMinMax(int[] arr) 
    {
        // Code Here
        int min = arr[0];
        int max = arr[0];
        int n = arr.length;
        
        for(int i = 0; i < n; i++)
        {
          if(arr[i] < min)
          {
              min = arr[i];
          }
          
          if(arr[i] > max)
          {
              max = arr[i];
          }
        }
        return new Pair<>(min,max);
    }
}
