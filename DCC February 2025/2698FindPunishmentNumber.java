
/* https://leetcode.com/problems/find-the-punishment-number-of-an-integer/solutions/6399433/Figures/2698/2698.png*/

/* Non Optimized recursive solution */

class Solution {
    public int punishmentNumber(int n) {
        //to store punishment number
        int punishmentNum = 0;

        //traverse the array
        for(int curr = 1;curr <= n ;curr++){

            //finding square
            int square = curr*curr;
            
            if(canPartition(square,curr))
              punishmentNum += square;
        }

        return punishmentNum;

    }
    public boolean canPartition(int num, int target){
        //invalid
        if(num < target || target < 0)
          return false;

        if(num == target)
          return true;

        return (canPartition(num/10,target-(num%10)) || canPartition(num/100,target-(num%100)) || canPartition(num/1000,target-(num%1000)));
    }
}

/* Optimized solution*/

class Solution 
{
    public int punishmentNumber(int n) 
    {
         int[] a = {1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,657,675,703,756,792,909,918,945,964,990,991,999,1000};  //Predetermined array value
         int sum = 0;
         for(int i = 0; i < a.length; i++)
         {
             if(a[i] <= n)
                   sum += a[i] * a[i];
             else if(a[i] > n)
                      break;
         }
         return sum;       
    }
}
