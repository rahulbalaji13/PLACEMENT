class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]
