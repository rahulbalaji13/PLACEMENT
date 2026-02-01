class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums[0] + sum(sorted(nums[1:]) [:2])
