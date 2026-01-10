class Solution(object):
    def subtreeWithAllDeepest(self, root):
        depth = {None : -1}
        def dfs(node, parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        max_depth = max(depth.iteratevalues())

        def answer():
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node  if L and R else L or R

        return answer(root)
            
