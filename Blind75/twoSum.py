class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []

        
        
