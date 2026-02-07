class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()

        ans = n
        right = 0

        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1

            ans = min(ans, n - (right - left))

        return ans
