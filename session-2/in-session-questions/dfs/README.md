Depth First Search:

We're going to go as deep as we can vertically before we proceed horizontally.

We use a stack to keep track of vertices we visit.

We use recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. This also means that the space complexity of the algorithm will be O(H), where ‘H’ is the maximum height of the tree.

This is most often implemented as recursive algorithm and in your interviews you should implement it in a recursive way unless you are in the very rare situation where your interviewer explicitly asks you implement it iteratively.

Note that inorder, preorder, postorder are variants of DFS.
