class Solution 
{
    public int longestMonotonicSubarray(int[] nums) 
    {
        int ans = 0;
        int add = 1; // For counting the incremental value
        int subract = 1; //For counting decremental value

        if(nums.length == 1) // For satisfying condition,same numbers in subarray 
             return 1;

        for(int i = 0; i < nums.length - 1; i++)
        {
            if(nums[i] > nums[i + 1]) // strictly increasing
            {
                 subract += 1;
                 add = 1;
            }
            else if(nums[i] < nums[i + 1]) // strictly decreasing 
            {
                 add += 1;
                 subract = 1;
            }
            else
            {
                 add = 1;
                 subract = 1;      
            }
                 ans = Math.max(ans,Math.max(add,subract));
        }
          return ans;
    }
}
