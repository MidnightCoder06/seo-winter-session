https://leetcode.com/problems/validate-binary-search-tree/ 

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.

'''

Example 1:

Input:

     2
   /   \
  1     3

Output: 

true

Example 2:

        5
      /   \
    1      4
         /   \
        3     6

        
output:

false
  ... the root node's value is 5 but its right child value is 4

Example 3:


            Input =         10
                         /      \
                        5        15
                      /  \      /  \
                     2    5   13    22
                    /          \
                   1            14

Output:

true

'''


''' Algorithm

Every node in the BST has a maxium possible value and minimum possible value.
In other words:
the value of any given node in the BST must be strictly smaller than some value
 *the value of its closest right parent
and must be greater than or equal to some other value
 *the value of its closest left parent

Given this information we can validate a BST by recursively calling the validateBST function on every node, passing in the correct maximum and minimum possible values to each.

We can intialize those values to be negative infinity and infinity.

'''

''' Big 0 Analysis

Worst Case:

0(n) time -> n is the number of nodes in the BST
0(d) space -> d is the depth (height) of the BST ... this maxium number of values in the recursive stack at any given time

'''

