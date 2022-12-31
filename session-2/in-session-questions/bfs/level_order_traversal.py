'''

This solution first checks if the root node is null, and returns an empty list if it is. 
Otherwise, it creates a queue and adds the root node to it. 
Then, it enters a loop that continues until the queue is empty.

Inside the loop, the code first determines the size of the queue 
(which represents the number of nodes at the current level of the tree). 
It then creates a list to hold the values of the nodes at the current level 
and adds them to the list as it processes them.

For each node in the queue, the code adds its value to the list, 
and if it has a left or right child, 
it adds those children to the queue as well. 
This allows the algorithm to visit the nodes level by level, from left to right.

Finally, the code adds the list of values for the current level to the overall result, 
and the loop continues until the queue is empty, at which point the level order traversal is complete.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # initialize a parent list that will hold all the sublists -> the sublists are the nodes contained at each level
        result = []

        # edge case
        if not root:
            return result

        # initialize our core data structures
        container = deque()
        # add the root to the queue
        container.append(root)

        # while the queue is not empty
        while container:

            level_size = len(container)
            curr_level = [] # represents the current level

            for _ in range(level_size):
                curr_node = container.popleft()

                # add the node to the current level
                curr_level.append(curr_node.val)
                # insert the children of current node in the queue
                if curr_node.left:
                    container.append(curr_node.left)
                if curr_node.right:
                    container.append(curr_node.right)
            result.append(curr_level)

        return result

'''

Time complexity
The time complexity is O(N) where N is the total number of nodes in the tree.
* we traverse each node once.

Space complexity
The space complexity is O(N)
*in the worst case we are storing every node in a queue

'''