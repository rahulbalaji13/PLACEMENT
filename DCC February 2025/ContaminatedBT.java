/**

1261. Find Elements in a Contaminated Binary Tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class FindElements 
{
    HashSet rv = new HashSet<>();
    public FindElements(TreeNode root) 
    {
        dfs(root, 0);
    }
    
    public boolean find(int target) 
    {
       return rv.contains(target); // Contains checks the hashset whether the particular value is exist in them. Return true or false accordingly.       
    }

    public void dfs(TreeNode root, int element) // Helper function to recover tree values
    {
        if(root == null)
           return;
        
        root.val = element;
        rv.add(element);

        dfs(root.left, 2 * element + 1);
        dfs(root.right, 2 * element + 2);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
