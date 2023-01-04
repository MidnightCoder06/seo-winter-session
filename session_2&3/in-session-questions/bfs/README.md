Breath First Search:

Breadth means broad or wide ... our algorithm progress horizontally as far as possible before progressing vertically

Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using a BFS approach.

We use a Queue (FIFO) to keep track of all the nodes of a level before we jump onto the next level.

This also means that the space complexity of the algorithm will be O(W),
where ‘W’ is the maximum number of nodes on any level. (the width)

This is an iterative algorithm.