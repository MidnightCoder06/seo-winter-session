Definition:

Binary Search Tree is a node-based binary tree data structure which has the following properties:

* The left subtree of a node contains only nodes with keys lesser than its parent (root) node's key.

* The right subtree of a node contains only nodes with keys greater than or equal to its parent (root) node's key.

* The left and right subtree each must also be a binary search tree.

Thus, BST divides all its sub-trees into two segments; the left sub-tree and the right sub-tree and can be defined as −

left_subtree (keys) < node (key) ≤ right_subtree (keys)

Take a look in the images folder within the supplemental material folder for examples



Basic Operations:

Following are the basic operations of a tree −

Search − Searches an element in a tree.

Insert − Inserts an element in a tree.

Deletion - Deletes an element in a tree.



Advantages:

Searching an element in the Binary search tree is easier as we always have a hint that which subtree has the desired element because of the strict properties of less than or greater than described above.

* speed
* accuracy 

As compared to array and linked lists, insertion and deletion operations are faster in BST.

Due to the fact that the binary search is in a branch-like format with parent-child relations, the algorithm knows in which location of the tree the elements need to be searched. This decreases the number of key-value comparisons the program has to make to locate the desired element.
 


Real world Applications:

* multilevel indexing in the database
* dynamic sorting
* managing virtual memory areas in Unix kernel
* graphics
* auto-complete activities 