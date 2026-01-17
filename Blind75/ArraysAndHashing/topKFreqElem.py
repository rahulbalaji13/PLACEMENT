from collections import Counter 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        if k == n:
          return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
