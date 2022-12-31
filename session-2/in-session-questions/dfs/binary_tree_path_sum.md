# https://leetcode.com/problems/path-sum/

'''

Given a binary tree and a number S, find if the tree has a path from root-to-leaf
such that the sum of all the node values of that path equals S.

'''

'''

As we are trying to search for a root-to-leaf path,
we can use the Depth First Search (DFS) technique to solve this problem.

To recursively traverse a binary tree in a DFS fashion,
we can start from the root (of a subtree) and at every step,
make two recursive calls: one for the left and one for the right child.

Here are the steps for our Binary Tree Path Sum problem:

1. Start DFS with the root of the tree.
2. If the current node is not a leaf node, do two things:
    2a. Subtract the value of the current node from the given number to get a new sum => S = S - node.value
    2b. Make two recursive calls for both the children of the current node with the new number calculated in the previous step.
3. At every step, see if the current node being visited is a leaf node and if its value is equal to the given number 'S'.
    If both these conditions are true, we have found the required root-to-leaf path, therefore return true.
4. If the current node is a leaf but its value is not equal to the given number 'S', return false.

'''