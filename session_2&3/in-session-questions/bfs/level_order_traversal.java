/*

This solution first checks if the root node is null, and returns an empty list if it is. 
Otherwise, it creates a queue and adds the root node to it. 
Then, it enters a loop that continues until the queue is empty.

Inside the loop, the code first determines the size of the queue 
(which represents the number of nodes at the current level of the tree). 
It then creates a list to hold the values of the nodes at the current level 
and adds them to the list as it processes them.

For each node in the queue, the code adds its value to the list, 
and if it has a left or right child, 
it adds those children to the queue as well. 
This allows the algorithm to visit the nodes level by level, from left to right.

Finally, the code adds the list of values for the current level to the overall result, 
and the loop continues until the queue is empty, at which point the level order traversal is complete.

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.add(level);
        }

        return result;
    }
}

/*

This solution first checks if the root node is null, and returns an empty list if it is. 
Otherwise, it creates a queue and adds the root node to it. 
Then, it enters a loop that continues until the queue is empty.

Inside the loop, the code first determines the size of the queue 
(which represents the number of nodes at the current level of the tree). 
It then creates a list to hold the values of the nodes at the current level 
and adds them to the list as it processes them.

For each node in the queue, the code adds its value to the list, 
and if it has a left or right child, 
it adds those children to the queue as well. 
This allows the algorithm to visit the nodes level by level, from left to right.

Finally, the code adds the list of values for the current level to the overall result, 
and the loop continues until the queue is empty, at which point the level order traversal is complete.

*/