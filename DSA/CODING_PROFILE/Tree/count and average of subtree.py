# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res=0
        def postorder(node):
            if not node:
                return (0,0)
            left=postorder(node.left)
            right=postorder(node.right)

            nonlocal res

            total_sum=left[0]+right[0]+node.val
            total_count=1+left[1]+right[1]
            res+=(node.val==total_sum // total_count)

            return (total_sum,total_count)
        
        postorder(root)

        return res
        
