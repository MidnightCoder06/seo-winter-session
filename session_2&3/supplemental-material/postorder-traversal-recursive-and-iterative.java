// https://leetcode.com/problems/binary-tree-postorder-traversal/

// recursive solution in Java for postorder traversal of a binary tree:

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        postorder(root, result);
        return result;
    }

    private void postorder(TreeNode root, List<Integer> result) {
        if (root == null) {
            return;
        }

        postorder(root.left, result);
        postorder(root.right, result);
        result.add(root.val);
    }
}

/*
Explanation:

The postorderTraversal function takes in the root of the binary tree and returns a list of integers representing the postorder traversal of the tree. It does this by calling the postorder helper function which traverses the tree recursively and appends the nodes' values to the list.

The postorder function works as follows:

If the root is null, it returns immediately, as there is nothing to do.
Otherwise, it first calls itself recursively on the left subtree of the root.
Then, it calls itself recursively on the right subtree of the root.
Finally, it adds the value of the root node to the list.

For example, consider the following binary tree:
*/

      1
     / \
    2   3
   / \   \
  4   5   6

/*

The postorder traversal of this tree would be [4, 5, 2, 6, 3, 1].

When the postorder function is called on the root node (1), the following sequence of recursive calls is made:

postorder(2, result)
postorder(4, result)
postorder(5, result)
postorder(3, result)
postorder(6, result)
At this point, all the recursive calls have completed, and the function starts adding the values to the list:

result.add(2.val) => [2]
result.add(5.val) => [2, 5]
result.add(4.val) => [2, 5, 4]
result.add(6.val) => [2, 5, 4, 6]
result.add(3.val) => [2, 5, 4, 6, 3]
result.add(1.val) => [2, 5, 4, 6, 3, 1]
The final list [2, 5, 4, 6, 3, 1] is the postorder traversal of the tree.


In the recursive solution, the return statement serves as a backtracking step.

When a function returns, the function's call is removed from the call stack 
and control is returned to the calling function. 
In the case of the recursive solution for postorder traversal, 
this serves as a way to backtrack from the current node to its parent node in the tree.

*/






// here is the iterative solution for postorder traversal of a binary tree in Java:

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        TreeNode lastVisited = null;

        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                TreeNode peekNode = stack.peek();
                if (peekNode.right != null && lastVisited != peekNode.right) {
                    curr = peekNode.right;
                } else {
                    result.add(peekNode.val);
                    lastVisited = stack.pop();
                }
            }
        }

        return result;
    }
}

/*

Explanation:

The postorderTraversal function takes in the root of the binary tree 
and returns a list of integers representing the postorder traversal of the tree. 
It does this iteratively using a stack.

The algorithm works as follows:

1. Create an empty stack and push the root node to the stack. 
Initialize stack as [1] and curr as 1.

2. While the stack is not empty or curr is not null:
* If curr is not null:
    ** Push curr to the stack.
    ** Update curr to point to curr.left.
* If curr is null:
    ** Check the top element of the stack (peekNode).
    ** If peekNode.right is not null and it has not been visited yet (i.e., lastVisited != peekNode.right), then update curr to point to peekNode.right.
    ** If peekNode.right is null or it has already been visited, then add peekNode.val to the result list and mark lastVisited as peekNode. Pop peekNode from the stack.


For example, consider the following binary tree:

    1
   / \
  2   3
 / \   \
4   5   6
The postorder traversal of this tree would be [4, 5, 2, 6, 3, 1].

The algorithm would work as follows:

Initialize stack = [1], curr = 1

Push 1 to stack, curr = 2

Push 2 to stack, curr = 4

Push 4 to stack, curr = null

peekNode = 4, peekNode.right = null, lastVisited = null, so add 4 to result and mark lastVisited as 4. Pop 4 from stack. stack = [2, 1], curr = null, lastVisited = 4

peekNode = 2, peekNode.right = 5, lastVisited = 4, so update curr to 5. stack = [2, 1], curr = 5, lastVisited = 4

Push 5 to stack, curr = null

peekNode = 5, peekNode.right = null, lastVisited = 4, so add 5 to result and mark lastVisited as 5. Pop 5 from stack. stack = [2, 1], curr = null, lastVisited = 5

peekNode = 2, peekNode.right = null, lastVisited = 5, so add 2 to result and mark lastVisited as 2. Pop 2 from stack. stack = [1], curr = null, lastVisited = 2

Push 3 to stack, curr = 6

Push 6 to stack, curr = null

peekNode = 6, peekNode.right = null, lastVisited = 2, so add 6 to result and mark lastVisited as 6. Pop 6 from stack. stack = [1], curr = null, lastVisited = 6

peekNode = 3, peekNode.right = null, lastVisited = 6, so add 3 to result and mark lastVisited as 3. Pop 3 from stack. stack = [], curr = null, lastVisited = 3

peekNode = 1, peekNode.right = null, lastVisited = 3, so add 1 to result and mark lastVisited as 1. Pop 1 from stack. stack = [], curr = null, lastVisited = 1

At this point, the while loop ends and the function returns the result list [4, 5, 2, 6, 3, 1].

*/