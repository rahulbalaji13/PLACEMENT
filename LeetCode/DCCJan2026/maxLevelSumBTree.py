# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_sum = float('-inf')
        ans = 0
        level = 0

        q = collections.deque()
        q.append(root) # Push root into queue

        while q:
            level += 1
            curr_level_sum = 0

            # Iterate over all nodes in the curent level
            for _ in range(len(q)):
                node = q.popleft()
                curr_level_sum += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            if max_sum < curr_level_sum:
                max_sum = curr_level_sum
                ans = level

        return ans


"""
To get the answer, we compare the sum of all node values at the current level to the maximum sum of values we've already seen. If the current sum of node values is greater than what we've seen before, we update our answer to level, and the current sum becomes our largest sum of values seen thus far. Since we are traversing the higher levels first, by only updating the answer when the level sum is greater than what we've seen before, we handle the tiebreakers automatically.

Algorithm
Create an integer variable maxSum to keep track of the maximum sum of node values at any level. We start with a large negative value.
Create another variable ans to store the answer to the problem.
Create another integer variable level to store the current level through which we are iterating. We initialize it with 0.
Initialize a queue q of TreeNode and push root into it.
Perform a BFS traversal until the queue is empty:
Increment level by 1 and initialize sumAtCurrentLevel = 0 to compute the sum of all values of nodes at this level.
Iterate through all the nodes at level using only the q.size() number of nodes. Within this inner loop, pop out all the nodes at the current level one by one, adding their values to sumAtCurrentLevel and pushing the left and right children (if they exist) into the queue.
Realize that after traversing all of the nodes at level, the queue only has nodes at level + 1.
After traversing through all the nodes at level, we check if sumAtCurrentLevel is greater than maxSum. If maxSum < sumAtCurrentLevel, update our answer variable to ans = level and set maxSum = sumAtCurrentLevel.
Return ans.
"""

    
