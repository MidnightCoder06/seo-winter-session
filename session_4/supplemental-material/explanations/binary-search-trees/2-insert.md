
We need to insert a node in BST with value item and return the root of the new modified tree.

* If the root is NULL, create a new node with value item and return it.

* Else, Compare item with root.val
- If root.val < item, recurse for right subtree
- If root.val > item, recurse for left subtree


Pseudo-Code

TreeNode insert_element(TreeNode root, item)
{
    if ( root == NULL )
    {
        root = TreeNode(item)
        return root
    }
    if ( root.val < item )
        root.right = insert_element(root.right, item)
    else if ( root.val > item )
        root.left = insert_element(root.left, item)
    return root
}


Algorithm

1. Compare current node's key with K.
2. If K is less than the current node,
- If left child of current node is Null, we insert K as the left child of current node and return.
- If the left child is not Null, the left child becomes the new current node, and we repeat the process from step 1.
3. If K is greater than the current node,
- If right child of current node is Null, we insert K as the right child of the current node and return.
- If the right child is not Null, the right child becomes the new current node, and we repeat the process from step 1.



Complexity Analysis

Since the new node is inserted at the leaf, the highest value possible for this is the height of the tree. Same analogy to the binary search algorithm as with search.

The worst-case complexity for this is O(N) for the same reasons as with search.
