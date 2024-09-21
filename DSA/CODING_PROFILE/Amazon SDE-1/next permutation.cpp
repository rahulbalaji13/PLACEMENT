/**P(n,r) = n!/(n-r)!
where:

P(n,r) is the number of permutations of n objects taken r at a time
n is the total number of objects
r is the number of objects to be selected**/

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int k,j;
        for(k=nums.size()-2;k>=0;k--){/**This line starts a for loop that iterates over the array nums from the end to the beginning. The variable k is used to track the current index.**/
            if(nums[k]<nums[k+1])/**This line checks if the current element nums[k] is less than the next element nums[k+1]. If it is, then the loop is broken and the pivot index is set to k.**/
             break;
        }
        if(k<0){/** If the pivot index is less than zero, then it means that the array is already in the last permutation and the function returns.**/
            reverse(nums.begin(),nums.end()); /**Otherwise, the elements in the array are reversed from beginning to end. This is because the array is already in the last permutation, and reversing it will give us the first permutation.**/
        }
        else{ /**Otherwise, the pivot index k is valid and we can proceed to find the successor index.**/
            for(j=nums.size()-1;j>k;j--){/**This line starts a for loop that iterates over the array nums from the end to the pivot index k. The variable j is used to track the current index.**/
                if(nums[j]>nums[k]) /**This line checks if the current element nums[j] is greater than the pivot element nums[k]. If it is, then the loop is broken and the successor index is set to j.**/
                   break;
                }
                swap(nums[k],nums[j]); /**This line swaps the elements at indices k and j.**/
                reverse(nums.begin()+k+1,nums.end()); /**This line reverses the elements in the array from index k+1 to the end.**/
        }
    }
};
              
