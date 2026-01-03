class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        a = [0] * n
        b = [0] * n

        a[0] = 6
        b[0] = 6

        for i in range(1, n):
            a[i] = (2 * a[i - 1] + 2 * b[i - 1]) % MOD
            b[i] = (2 * a[i - 1] + 3 * b[i - 1]) % MOD

        return (a[n - 1] + b[n - 1]) % MOD        

"""
Intuition
We paint the grid one column at a time.
For one column (3 cells), there are only two valid ways to color it:

All three cells have different colors
Top and bottom have the same color, middle is different
No other pattern is allowed because adjacent cells cannot have the same color.
So instead of thinking about all colors, we just count how many ways these two patterns can appear.

Approach
We keep two counts:

a[i] → ways where column i uses three different colors
b[i] → ways where column i uses top and bottom same color
For the first column:

Both patterns have 6 possible ways
For each new column:

A column with different colors can come from both previous patterns in 2 ways each
A column with same top & bottom can come from:
different-color pattern in 2 ways
same-color pattern in 3 ways
We add these counts and apply modulo to avoid overflow.

Final answer is:

a[n-1] + b[n-1]

Complexity
Time complexity: O(n)

Space complexity: O(n)

"""
