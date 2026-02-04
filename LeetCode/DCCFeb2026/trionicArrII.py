class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = p = w = res = -float('inf')
        n = len(nums)
        for i in range(n - 1):
            v, u = nums[i], nums[i + 1]
            w = max(w, p) + u  if i > 1 and v < u else -float('inf')
            p = max(p, q) + u if i and v > u else -float('inf')
            q = max(q, v) + u if v < u else -float('inf')

            res = max(res, w)

        return res
