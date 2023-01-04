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

 /*

 This solution uses a depth-first search approach. 
 
 It first calculates the maximum path sum of the left and right subtrees and stores it in the variables left and right. 
 
 It then calculates the maximum path sum of the current path by adding the value of the root node 
 and the maximum path sum of either the left or right subtree (whichever is larger). 
 
 Finally, it updates the global maximum path sum by comparing the current path sum to the current maximum.

 */
 
class Solution {
    public int dfs(TreeNode root, int[] max) {
        // first check if the root is null.
        if (root == null) {
            // If it is, it returns 0, since a path sum of a null node is 0. 
            return 0;
            /*
            This is because a null node represents an empty subtree, 
            and the path sum of an empty subtree is defined to be 0.
            
            This definition is used in the dfs function to ensure that the path sum of a null node 
            is not included in the overall path sum calculation. 
            If the path sum of a null node were not defined as 0, 
            the path sum calculation would include the value of a null node, which would not make sense.
            */
        }

        /*
        Otherwise, it calculates the maximum path sum of the left and right subtrees 
        and stores it in the variables left and right. 
        It does this by calling itself recursively on the left and right child nodes.
        */

        int left = Math.max(0, dfs(root.left, max));
        int right = Math.max(0, dfs(root.right, max));


        /*
        Next, it calculates the maximum path sum of the current path 
        by adding the value of the root node and the maximum path sum of either the left or right subtree 
        (whichever is larger). This is done using the Math.max function. 
        
        The Math.max function returns the larger of the two values passed to it, 
        so it ensures that only the larger of the left and right subtree path sums is used.
        */
        max[0] = Math.max(max[0], left + right + root.val);

        // Finally, the dfs function updates the global maximum path sum by comparing the current path sum to the current maximum. 
        // This is done using the Math.max function again.
        return Math.max(left, right) + root.val;
    }

    // The maxPathSum function takes in the root of a binary tree and returns the maximum path sum of any non-empty path.
    public int maxPathSum(TreeNode root) {
        int[] max = new int[]{Integer.MIN_VALUE};
        // using a helper function called dfs, which stands for depth-first search. 
        // The dfs function takes in a tree node and an array, 
        dfs(root, max);
        // and returns the maximum path sum of any non-empty path that includes the given tree node.
        return max[0];
        
    }
}

///////////// why is the variable max an array and not just an integer?

/*

The variable max is an array because it is passed as a reference to the dfs function. 
This means that when the value of max is updated inside the dfs function, 
the change is reflected in the original max array in the maxPathSum function.

If max were just an integer, the value of max would be passed by value to the dfs function. 
This means that any changes to max inside the dfs function would not be reflected in the original 
max in the maxPathSum function. 
The original max would remain unchanged, and the maxPathSum function would always return 
the initial value of max.

Using an array allows the value of max to be updated and returned correctly.

*/


///////////// what is the difference between passed by reference and passed by value?

/*

In Java, when an object (such as an array) is passed as an argument to a function, 
it is passed by reference. 
This means that the function is given a reference to the object, rather than a copy of the object. If the object is modified inside the function, the changes are reflected in the original object outside the function.

On the other hand, when a primitive data type (such as an int or a double) 
is passed as an argument to a function, it is passed by value. 
This means that the function is given a copy of the value, rather than a reference to the original value. 
If the value is modified inside the function, 
the original value outside the function remains unchanged.

*/

// Here is an example to illustrate the difference between pass by reference and pass by value:

public void passByValue(int x) {
    x = 5;
}

public void passByReference(int[] x) {
    x[0] = 5;
}

int a = 3;
int[] b = new int[]{3};

passByValue(a);
passByReference(b);

System.out.println(a); // Outputs 3
System.out.println(b[0]); // Outputs 5

/*
In the example above, the variable a is passed by value to the passByValue function, 
while the variable b is passed by reference to the passByReference function. 

As a result, the value of a remains unchanged after the function call, 
while the value of b[0] is modified.
*/



///////////// why is the path sum of a null node zero?

/*
In this problem, the path sum of a null node is defined to be 0. This is because a null node represents an empty subtree, and the path sum of an empty subtree is defined to be 0.

This definition is used in the dfs function to ensure that the path sum of a null node is not included in the overall path sum calculation. If the path sum of a null node were not defined as 0, the path sum calculation would include the value of a null node, which would not make sense.

*/




///////////// how are you defining an empty subtree?

/*

An empty subtree is a subtree that does not contain any nodes. In the context of this problem, an empty subtree is represented by a null tree node.

For example, consider the following binary tree:

*/

    1
   / \
  2   3
 /   / \
4   5   6

/*

In this tree, the subtree rooted at the node with value 2 is an empty subtree, 
because it does not contain any nodes. 
The subtree rooted at the node with value 3 is not an empty subtree, 
because it contains nodes with values 5 and 6.

*/