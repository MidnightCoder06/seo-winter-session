# https://leetcode.com/problems/binary-tree-level-order-traversal/

'''
algorithm:

1. push the root node to the queue.
2. iterate over the queue until it is empty.
3. within each iteration, count the elements in the queue
    * this is how many nodes will be in the current level.
4. remove a number of nodes from the queue equal to the count calculated in the previous step and push their value in an array representing the current level.
5. insert the children of each node being processed into the queue.
6. repeat from step 3 for the next level if the queue is not empty.
'''