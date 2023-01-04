# https://leetcode.com/problems/minimum-depth-of-binary-tree/


# This problem follows the Binary Tree Level Order Traversal pattern.
# The difference is that instead of keeping track of all the nodes in a level,
# we will only track the depth of the tree.
# As soon as we find our first leaf node we know the minimum depth of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # edge case
        if not root:
            return 0

        # core logic
        container = deque()
        min_depth = 0
        container.append(root)

        while container:
            min_depth += 1

            level_size = len(container)
            for _ in range(level_size):
                curr_node = container.popleft()
                # identify if you've found a leaf node
                if not curr_node.left and not curr_node.right:
                    return min_depth

                # if not add its children
                if curr_node.left:
                    container.append(curr_node.left)

                if curr_node.right:
                    container.append(curr_node.right)


'''

Time complexity
The time complexity is O(N) where 'N' is the total number of nodes in the tree.
* in the worst case we traverse each node once.

Space complexity
The space complexity is O(N)
* in the worst case we are storing every node in a queue

'''
