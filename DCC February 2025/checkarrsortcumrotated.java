class Solution 
{
    public boolean check(int[] nums) 
    {
         int n = nums.length;
         int x = 0;
         for(int i = 1; i < n; i++)
         
             if(nums[i] < nums[i - 1])
                  x++;
             
             if(nums[0] < nums[n - 1])
                  x++;

         return x <= 1;
       
    }
}
