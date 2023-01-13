

Let’s assume we need to search for value item in a BST. When we compare it with the root of the tree, we are left with three cases:

* item == root.val: 
We terminate the search as the item is found

* item > root.val: 
We just check the right subtree because all the values in the left subtree are lesser than root.val

* item < root.val: Now we just check the left subtree as all values in the right subtree are greater than root.val

We keep on recursing in this manner and this decreases our search time complexity up to a great extent as we just need to look at one subtree and reject the other subtree saving us the trouble of comparing a batch of values.


Algorithm:

Our objective is to return True if a node exists with the value equal to the item, else return False.

* Check if the root is NULL, return False if it is NULL.

* Else, Compare root.val with item
- item == root.val: return True
- item > root.val: recurse for right subtree
- item < root.val: recurse for left subtree

Pseudo-Code:

bool search(TreeNode root, int item)
{
    if ( root == NULL )
        return False
    
    if ( item == root.val )
        return True
    
    else if ( item > root.val )
        return search(root.right, item)
    
    else if ( item < root.val )
        return search(root.left, item)
}

Complexity Analysis:

The above code scans the tree one level at a time. It works like a binary search in an array with the root of the tree is acting like the middle element of an array.
 
We just look at left or right subtree, saving us a lot of time, just like how in binary search we look at the left or right side of an element in a sorted array. 

Once we compare the node we select, we move on to either the left or right subtree, hence, moving one level down.

The time complexity is thefore O(H) - h being the total height of the tree.

So what is the height of BST in terms of N, with N being the total number of nodes?
A height-balanced BST has a maximum height of log(N).

But in a normal binary search tree, the worst-case time complexity of the searching operation is still O(N), same as the binary tree.

The tree structure that produces this worst-case is a left-skewed or right-skewed tree.


