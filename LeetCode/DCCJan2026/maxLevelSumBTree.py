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



    
