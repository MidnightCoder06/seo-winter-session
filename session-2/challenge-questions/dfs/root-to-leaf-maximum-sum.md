'''
Given a binary tree, find the root-to-leaf path with the maximum sum.
A sum is defined as the sum of all the node's values in a given path.
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

# Brute force - calculate all paths and then return the largest

# instead we need to think of an efficient way to visit each subtree and compute a sum
# we can save time by starting at the bottom of tree and get a sum and then use that sum for parent node computations (by returning the child's node to its parent node)
# postOrder traversal can be used for this (since the root is visited last in postOrder traversal)

#####

# Time -> 0(n) -> N being the number of nodes in the tree. we touch each node once.
# Space -> 0(h) -> h is the hieght of the tree. Worst case is h recursive calls
    # in a a balanced tree the height is usually log(n)