'''

Question:
Given a binary tree and a node, find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after the given node in the level order traversal.

Algorith:
This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach.
The only difference will be that we will not keep track of all the levels.
Instead we will keep inserting child nodes to the queue.
As soon as we find the given node, we will return the next node from the queue as the level order successor.
'''


from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if not root:
    return None
  
  queue = deque()
  return_next_node = False
  queue.append(root)

  while queue:
    level_size = len(queue)
    for _ in range(level_size):
      curr = queue.popleft()
      if return_next_node:
        return curr
      if curr.val == key:
        return_next_node = True
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
  
  return None
  
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val) # 7
  result = find_successor(root, 9)
  if result:
    print(result.val) # 10


main()





'''

Time complexity
The time complexity of the above algorithm is O(N),
where 'N' is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.

Space complexity
The space complexity of the above algorithm will be O(N) which is required for the queue.
The node we are looking for may be the last node so worse can we will need to store all the nodes in the queue.

'''
