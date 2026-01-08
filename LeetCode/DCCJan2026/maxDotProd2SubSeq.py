# Define a Solution class that extends from object
class Solution(object):
    # Define the main function maxDotProduct with two input lists and return type int
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]  # First input array
        :type nums2: List[int]  # Second input array
        :rtype: int              # Return maximum dot product value
        """
        # Get the length (number of elements) of the first array
        m = len(nums1)
        # Get the length (number of elements) of the second array
        n = len(nums2)

        # Edge Case 1: If all elements in nums1 are negative and all in nums2 are positive
        # Then the maximum product would be: (largest/closest to zero in nums1) * (smallest/closest to zero in nums2)
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        # Edge Case 2: If all elements in nums1 are positive and all in nums2 are negative
        # Then the maximum product would be: (smallest element in nums1) * (largest element in nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        # Initialize 'prev' array of size (n+1) with zeros. This represents DP values for the previous iteration
        # Size is n+1 to handle boundary access when j+1 goes beyond n
        prev = [0] * (n + 1)
        
        # Outer loop: iterate through nums1 in reverse order (from last to first element)
        for i in range(m - 1, -1, -1):
            # Initialize 'dp' array of size (n+1) with zeros for the current row
            dp = [0] * (n + 1)
            
            # Inner loop: iterate through nums2 in reverse order (from last to first element)
            for j in range(n - 1, -1, -1):
                # Calculate the product of current elements plus the best value from the next position
                # prev[j+1] represents the optimal solution when both indices move forward
                use = nums1[i] * nums2[j] + prev[j + 1]
                
                # Update dp[j] with the maximum of three options:
                # 1. use: Include both nums1[i] and nums2[j] in the subsequence
                # 2. prev[j]: Skip nums1[i], keep nums2[j] for future consideration
                # 3. dp[j + 1]: Skip nums2[j], consider next element in nums2
                dp[j] = max(use, prev[j], dp[j + 1])
            
            # After processing all elements of nums2 for current nums1[i],
            # move to the next iteration by setting prev = dp
            prev = dp
        
        # Return the maximum dot product starting from position 0 in both arrays
        return prev[0]

