The worst case time complexity is 0(n) because at the worst case the 
tree will be skewed and we will have to traverse every node in the tree.
A skewed tree prevents us from using the properties of the BST to cut our number of choices in half every time, which is what leads to the 0(log n) time complexity.

Note that a skewed tree is essentially a Linked List.