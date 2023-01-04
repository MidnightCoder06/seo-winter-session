// https://leetcode.com/problems/minimum-depth-of-binary-tree/

/*

This solution uses a queue to perform a breadth-first search on the binary tree. 

It starts by adding the root node to the queue, and then enters a loop. 

On each iteration of the loop, it increments the depth by 1 
and examines all of the nodes at the current depth (which are stored in the queue). 

If any of these nodes are leaf nodes (have no children), it returns the current depth. 
Otherwise, it adds the children of the current nodes to the queue and continues the loop.

*/

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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            depth++;
            for (int i = 0; i < size; i++) {
                TreeNode current = queue.poll();
                if (current.left == null && current.right == null) {
                    return depth;
                }
                if (current.left != null) {
                    queue.offer(current.left);
                }
                if (current.right != null) {
                    queue.offer(current.right);
                }
            }
        }
        return depth;
    }
}
