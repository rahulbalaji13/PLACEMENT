# MAXIMUM PRODUCT SPLIT BINARY TREE
class Solution(object):
    def maxProduct(self, root):
        total, sub = 0, []
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sub.append(s)
            return s
        total = dfs(root)
        return max(x * (total - x) for x in sub) % (10**9 + 7)
