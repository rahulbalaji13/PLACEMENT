/* CAN PLACE FLOWERS: You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length*/

class Solution 
{
    public boolean canPlaceFlowers(int[] flowerbed, int n) 
    {
         if(n == 0)
             return true;

         for(int i = 0; i < flowerbed.length; i++)
         {
             if(flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) 
             {
                 flowerbed[i] = 1; 
                 n--;

                 if(n == 0) 
                     return true;
             }
         } 
         return false;
    }    
}

/* 
flowerbed[i] == 0 - checks the flower bed is empty 
i == 0 - points to intial postion, in which flowerbed is empty
flowerbed[i-1] == 0 - check last end of flower bed or adjacent left is empty 
flowerbed.length - 1 -> checks whether the flowerbed on rear or last end (i.e) n - 1
flowerbed[i+1] == 0 - checks whether adjacent right of flowerbed is empty

when all the above condition satisfy then we place new flower: flowerbed[i] = 1
then we update n number of flower by decremeting n-- after flower was placed to show it.
*/
