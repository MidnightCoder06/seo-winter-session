
Question:

Write a function that takes a Binary Search Tree (BST) and a positive integer k
and returns the kth largest integer contained in the BST.

You can assume there will only be integer values in the BST
and that k is less than or equal to the number of nodes in the tree.

Duplicate integers will be treeated as distinct values.
For example: the second largest value in a BST containing values: {5,7,7} will be 7 ... not 5.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
- its value is strictly greater than the values of every node to its left
- its value is less than or equal to the value of every node to its right
- its children nodes are either valid BST nodes themselves or None



''' Visual

Sample Input:

k = 3

            tree =          15
                         /      \
                        5        20
                      /  \      /  \
                     2    5   17    22
                    / \
                   1   3

Sample Output:

17

'''


''' Algorithm

Perform inorder traversal and store all of the node values in the order in which they were visited.
Since in-order traversal of a BST visits the nodes in ascending order,
the kth value from the end of the traversal order will be the kth largest value.

'''


''' Big 0 Analysis

Worst Case:

0(n) for both time and space where n is the number of nodes in the tree

'''