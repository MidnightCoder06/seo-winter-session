# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):

        # we have to start at negative infinity to account for negative numbers
        max_sum = float('-inf')

        # using postorder for bottom up approach.
        # Returning max path up to the parent node
        def postOrderTraversal(node):
            # nonlocal is the python keyword to access a variable from an outer function
            nonlocal max_sum
            # when hit a leaf node you need a way to pop back up / something to return to the parent
            if not node:
                return 0

            # max sum on the left and right sub-trees of a given node
            # comparing against zero because anything less than zero will make the path smaller
            # which we don't want, we want to find the max, not take steps backwards
            left = max(postOrderTraversal(node.left), 0)
            right = max(postOrderTraversal(node.right), 0)

            # where to start a new path where `node` (i.e. the parent) is a highest node
            # this generates a path with a split ... we don't yet return to the parent
            #        x
            #       / \
            #      y   z
            newpath_start = node.val + left + right

            # update max_sum if it's better to start a new path (i.e. compute without no split)
            max_sum = max(max_sum, newpath_start)

            # pass up to parent
            # return the max if continuing along the same path
            # extending either the left or right side as far as you can go
            return node.val + max(left, right)


        postOrderTraversal(root)
        return max_sum