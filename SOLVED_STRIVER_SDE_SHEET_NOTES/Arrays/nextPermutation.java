/**
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
        
        if i >= 0:
             j = n - 1
        
             while nums[j] <= nums[i]:
                  j -= 1

             nums[i], nums[j] = nums[j], nums[i]
    
        nums[i + 1:] = reversed(nums[i + 1:])
**/




//JAVA

class Solution 
{
    public void nextPermutation(int[] nums) 
    {
       int n = nums.length;
       int i = n - 1;

       while(i > 0 && nums[i - 1] >= nums[i]) // To compare last element with first prefix
       {
          i--; // Move back the iteration
       }

       if(i == 0)
       {
          reverse(nums, 0, n - 1); //when iteration i reached 0th position then reverse and print the result
          return;
       }
       
       int j = n - 1;
       
       while(j >= i && nums[j] <= nums[i - 1]) // Compare again after find sequence and then sort and reverse to obtain final result
       {
           j--;
       }
       swap(nums, i - 1, j);
       reverse(nums, i, n - 1);
    }

    private void swap(int[] nums, int i, int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int[] nums, int start, int end)
    {
        while(start < end)
        {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}


