'''

Given a binary tree and a number 'S',
find all paths from root-to-leaf such that the sum of all the node values of each path equals 'S'.

'''

'''

This problem follows a very similiar approach to how we solved Binary Tree Path Sum.
We can follow the same general DFS pattern.

There will be two differences:

Every time we find a root-to-leaf path, we will store it in a list.
We will traverse all paths and will not stop processing after finding the first path.

'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
  allPaths = []
  find_paths_recursive(root, required_sum, [], allPaths)
  return allPaths


def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
  if currentNode is None:
    return

  # add the current node to the path
  currentPath.append(currentNode.val)

  # if the current node is a leaf and its value is equal to required_sum, save the current path
  if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
    # without the (list) wrapper you get [[],[]] instead of [[1,2,5],[1,3]] ... the list wrapper makes a deep copy, without you are just peeking references which get overwritten
  else:
    # traverse the left sub-tree
    find_paths_recursive(currentNode.left, required_sum -
                         currentNode.val, currentPath, allPaths)
    # traverse the right sub-tree
    find_paths_recursive(currentNode.right, required_sum -
                         currentNode.val, currentPath, allPaths)

  # remove the current node from the path to backtrack,
  # we need to remove the current node while we are going up the recursive call stack.
  del currentPath[-1]


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))
  # Tree paths with required_sum 23: [[12, 7, 4], [12, 1, 10]]

main()


'''  Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, 
that incrementally builds candidates to the solutions, 
and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly 
be completed to a valid solution.

In the context of binary tree questions, backtracking can be used to find all possible solutions 
to a problem that involves traversing or searching a binary tree. 

For example, suppose you are asked to find all possible paths from the root node 
of a binary tree to a leaf node. 
One way to solve this problem using backtracking would be to start at the root node 
and explore each possible path one by one, 
going down the left child first and then the right child. 
At each node, you would decide whether to continue down that path or backtrack and explore a different path. When you reach a leaf node, 
you would save the path as a solution. 

If you reach a null node (i.e., a node that has no children), 
you would backtrack to the previous node and explore the other child.

This backtracking approach can be implemented using a recursive function that 
traverses the binary tree and returns all the paths from the root to the leaf nodes. 
The function would take the current node and the current path as arguments, 
and at each step it would add the current node to the path and call itself 
recursively on the left and right children of the current node. 
When it reaches a leaf node, it would add the path to the list of solutions and return. 
If it reaches a null node, it would simply return without adding the path to the list of solutions.

'''


''' Shallow copy vs. Deep copy

In Python, a deep copy of an object is a new object that is a copy of the original object and all of its contents. 
A shallow copy of an object is a new object that is a copy of the original object, 
but it does not include the objects contained within the original object.

'''

# Here is an example of a deep copy in Python:

import copy

original_list = [1, 2, [3, 4]]

deep_copy = copy.deepcopy(original_list)

# Modifying the original list
original_list[2][0] = 5

# The deep copy is not affected
print(deep_copy)  # [1, 2, [3, 4]]

# And here is an example of a shallow copy:

import copy

original_list = [1, 2, [3, 4]]

shallow_copy = copy.copy(original_list)

# Modifying the original list
original_list[2][0] = 5

# The shallow copy is also affected
print(shallow_copy)  # [1, 2, [5, 4]]

'''

In the deep copy example, even though we modified the original list by changing the value at index 2 to 5, 
the deep copy of the list remains unchanged. 

However, in the shallow copy example, the modification to the original list is 
reflected in the shallow copy as well, because the copy only includes a reference to the object and not a copy of the object itself.

'''


''' in python is the list() wrapper function the same as the .copy() function?

No, the list() function is used to create a new list from an iterable, 
while the copy() function from the copy module is used to create a shallow copy of an object.

'''

# Here is an example of using the list() function to create a new list:

original_list = [1, 2, 3]
new_list = list(original_list)

print(new_list)  # [1, 2, 3]


# And here is an example of using the copy() function to create a shallow copy of a list:

import copy

original_list = [1, 2, 3]
shallow_copy = copy.copy(original_list)

print(shallow_copy)  # [1, 2, 3]

'''

the list() function creates a new list with the same elements as the original list, 
while the copy() function creates a new list object that refers to the same elements as the original list.

'''