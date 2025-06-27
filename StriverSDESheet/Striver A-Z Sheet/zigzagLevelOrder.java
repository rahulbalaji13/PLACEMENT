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
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        
        boolean flag = true; // Used to track and switch from l to r and r to l
        
        //edge case
        if(root == null)
               return res;
               
        q.offer(root); // Insert all the nodes into queue
        
        while(!q.isEmpty())
        {
            int level = q.size(); 
            /** 
- Use **int[]** when:
- You need performance and low memory usage
- You don’t need to store null values
- You're doing heavy numerical computation
- Use **Integer[]** when:
- You need to use the array with collections or generics (e.g., List<Integer>)
- You need to store nullable values
- You want to use methods from the Integer class (e.g., compareTo(), toString())

            **/
            Integer[] list = new Integer[level];
            
            for(int i = 0; i < level; i++)
            {
                TreeNode temp = q.poll(); // Remove all queue element and store on temp
                int idx = flag ? i : level - i - 1; // i refers to left to right traversal : level - i - 1 refers to right to left node traversal
                
                list[idx] = temp.val; // Store node value into certian flag switched index
                if(temp.left != null)
                       q.offer(temp.left);
                if(temp.right != null)
                       q.offer(temp.right);
            }
            res.add(Arrays.asList(list)); // Converts array into fixed sized list
            flag = !flag;
        }
        return res;
    }
}
