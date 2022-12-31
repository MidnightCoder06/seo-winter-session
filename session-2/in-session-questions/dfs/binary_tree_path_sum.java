/*

This solution uses recursion to traverse the tree and check if there is a path from the root to a leaf 
such that the sum of the values along the path equals targetSum. 
It does this by first checking if the current node is a leaf node. 
If it is, it checks if the targetSum is equal to the value of the current node. 
If the current node is not a leaf, it recursively checks the left and right children 
of the current node with a modified targetSum that is targetSum - root.val. 
This ensures that the sum is correctly computed along the path as the function traverses the tree.

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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        if (root.left == null && root.right == null) {
            return targetSum - root.val == 0;
        }
        return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    }
}