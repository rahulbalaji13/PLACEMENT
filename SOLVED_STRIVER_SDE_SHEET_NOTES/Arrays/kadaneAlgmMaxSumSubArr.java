class Solution 
{
    public int maxSubArray(int[] nums) 
    {
        int maxSofar = nums[0]; 
        int currSum = nums[0]; //Trace the current sum
        int ans = 0;
        int n = nums.length;
        
        for(int i = 1; i < n; i++)
        {
           if(currSum < 0)
           {
                 currSum = 0;
           }

           currSum = currSum + nums[i];
           
           if(currSum > maxSofar)
           {
             maxSofar = currSum;
           }
        }
        return maxSofar;
    }
}

//O(N) = TC
