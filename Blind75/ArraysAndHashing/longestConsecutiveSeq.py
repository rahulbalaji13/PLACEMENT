class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert existing list to Hashset 
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1 #Initialize length = 1 when the condition true
            
                while num + length in numSet:
                    length += 1

                longest = max(length, longest)
        
        return longest 

# NOW THE SOLUTION ABOVE WORKS ON O(N) TC AND SATISFIES THE CONDITON OF THE PROBLEM
