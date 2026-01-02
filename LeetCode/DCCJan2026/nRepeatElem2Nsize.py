class Solution(object):
    def repeatedNTimes(self, nums):
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                 return nums[i]
        
        return nums[-1]


"""
Trick:
Since one element appears in exactly 50% of the array, it cannot stay more than 2 indices apart everywhere.

So in any 3 consecutive elements, the repeated number must appear at least twice.

Just scan once and check:
nums[i] == nums[i+1] or nums[i] == nums[i+2].

O(n) time, O(1) space. Simple & efficient.
"""
