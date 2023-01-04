'''
https://leetcode.com/problems/binary-tree-inorder-traversal/

'''

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#### Recursive

class Solution:

    # helper function
    def recursive_helper(self, currNode, result):
        # base case -> we need to check a leaf node
        if not currNode:
            return None
        self.recursive_helper(currNode.left, result)
        result.append(currNode.val)
        self.recursive_helper(currNode.right, result)

    # driver function
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] # holds all of the values
        self.recursive_helper(root, result)
        return result



'''

At iteration 0, stack = ['D']
At iteration 1, stack = ['D', 'B']
At iteration 2, stack = ['D', 'B', 'E']
At iteration 3, stack = ['D', 'B', 'E', 'A']
At iteration 4, stack = ['D', 'B', 'E', 'A', 'F']
At iteration 5, stack = ['D', 'B', 'E', 'A', 'F', 'C']
At iteration 6, stack = ['D', 'B', 'E', 'A', 'F', 'C', 'G']


'''


'''

The space complexity of a recursive DFS algorithm is O(h), 
where h is the maximum depth of the recursive call stack. 
This is because the algorithm uses a stack to store the state of the function at each recursive call, 
and the size of the stack is directly proportional to the maximum depth of the recursive call.

In a DFS algorithm, the depth of the recursive call stack can be at most the depth of the tree. 
Therefore, the space complexity is O(h) in the worst case, where h is the depth of the tree.

'''