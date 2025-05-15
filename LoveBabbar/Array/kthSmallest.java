/**
Kth Smallest
Difficulty: MediumAccuracy: 35.17%Submissions: 688K+Points: 4Average Time: 25m
Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.
Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.
Constraints:
1 <= arr.size <= 106
1<= arr[i] <= 106
1 <= k <= n
**/

class Solution 
{
    public static int kthSmallest(int[] arr, int k) 
    {
        // creates maximum priority queue with comparator as lambda function b - a
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);
        
        int n = arr.length;
        
        for(int i = 0; i < n; i++)
        {
            pq.offer(arr[i]); // Add all the element into the queue
        
        
            if(pq.size() > k) //when the priority queue size is more than kth value 
        
                pq.poll(); // then remove those greater element than position k value from the priority queue
        }
             
        return pq.peek(); //Show the top element from the queue 
    }    
}
