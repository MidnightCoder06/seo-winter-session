# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def validateBstHelper(self, currNode, minValue, maxValue):
        # base case
        # if we've reached a leaf node and haven't returned false
        # then we can see this path at least is valid so return true to our parent when we pop back up
        if currNode is None:
            return True

        # logic to check our upper and lower bound
        if currNode.val <= minValue or currNode.val >= maxValue:
            return False

        # make sure all the paths in our left and right subtree have continously returned true all the up to the root

        # most tree questions gaurentee positive values so the min could be zero
        # but I just made it negative infinity since could keep going left theoretically forever
        # that's the lower bound ^
        # the upper bound is the parent node
        leftIsValid = self.validateBstHelper(currNode.left, minValue, currNode.val)
        
        # when going to the right the numbers could theoretically keep growing forever 
        # so I put the upper bound as infinity
        # the lower bound is its parent node
        rightIsValid = self.validateBstHelper(currNode.right, currNode.val, maxValue)

        # both the left and right subtree must be valid
        return leftIsValid and rightIsValid
        # return true and true -> true
        # return true and false -> false 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBstHelper(root, float("-inf"), float("inf"))