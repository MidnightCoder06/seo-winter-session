When we delete a node in BST, we can encounter three cases:

* The node to be deleted is a leaf node: 
- Easiest case... remove the node from the tree

* The node to be deleted has only one child: 
- Replace the node by its child

* The node to be deleted has both a left and right child: 
- The node still needs to be replaced to maintain BST properties, making this the trickiest case b/c you have determine which node should replace this deleted node, which is not necessarily trivial
- the answer is the 'inorder successor' of this node would be the choice to replace this node as its inorder successor is the smallest element that is greater than this node. The inorder sucessor can be defined as the smallest element of its right subtree


Algorithm:

You need to delete the node with value item and then return the root of the modified tree. 
First, we need to find the node to be deleted and then secondly - replace it with the appropriate node if needed.

1. Check if the root is NULL, if it is, just return the root itself. This means it's an empty tree!
2. If root.val < item, recurse the right subtree.
3. If root.val > item, recurse the left subtree.
4. If both above conditions above false, this means root.val == item.
5. Now we first need to check how many child did root have.
* CASE 1: No Child
- delete root / deallocate space occupied by it
* CASE 2: One Child 
- Replace root by its child
* CASE 3: Two Children
- Find the inorder successor of the root... we'll call it new_root in this example.
- Replace root by its inorder successor
- Now recurse to the right subtree and delete new_root.
6. Return the root.


Complexity Analysis:

Same logic as search and insert.


Pseudo-Code:

TreeNode delete_element(TreeNode root, int item)
{
    if ( root == NULL )
        return root
    
    if ( root.val < item)
        root.right = delete_element(root.right, item)

    else if ( root.val > item )
        root.left = delete_element(root.left, item)

    else if ( root.val == item )
    {
        // No child
        if ( root.left == NULL and root.right == NULL )
            delete root

        // Only one child
        else if ( root.left == NULL or root.right == NULL )
        {
            if (root.left != NULL)
            {
                TreeNode new_root = root.left
                delete root
                return new_root
            }
            else
            {
                TreeNode new_root = root.right
                delete root
                return new_root
            }
        }
        // Both left and right child exist
        else
        {
            TreeNode new_root = find_inorder_successor(root.right)
            root.val = new_root.val
            root.right = delete_element(root.right, new_rot.val)
        }
    }
    return root
}

TreeNode find_inorder_successor(TreeNode root)
{
    TreeNode curr = root
    while ( curr.left != NULL )
        curr = curr.left
    
    return curr
}