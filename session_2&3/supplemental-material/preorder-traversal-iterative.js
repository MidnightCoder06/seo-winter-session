// https://leetcode.com/problems/binary-tree-preorder-traversal/


// Definition for a binary tree node.
class TreeNode {
    constructor(val) {
      this.val = val;
      this.left = null;
      this.right = null;
    }
  };



/*

sample tree:
   1
  /  \
 2     3
/ \   / \
4   5 6   7

*/

// Example of how to build a tree.
var root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);

root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);


root.right.left = new TreeNode(6);
root.right.right = new TreeNode(7);

console.log(`Level order traversal: ${yourFunction(root)}`);



// iterative example
var preorderTraversal = function(root) {
  if (!root) {
      return []
  }

  let stack = [root]
  let arr = []

  while (stack.length) {
      let curr = stack.pop()
      arr.push(curr.val)

      if (curr.right) {
          stack.push(curr.right)
      }

      if (curr.left) {
          stack.push(curr.left)
      }
  }

  return arr
};

/*

tree:
  1
2   3
4  5 6  7

1st iteration:
stack: [1]
arr: []

2nd iteration:
current node = stack pop last element = 1
arr: [1]
current node:
 1
2   3
stack push right of current node first then followed by left
stack: [3, 2]

3rd iteration:
current node = stack pop last element = 2
arr: [1,2]
current node:
 2
4   5
stack push right current node first then followed by left
stack: [3, 5, 4]

4th iteration:
current node = stack pop last element = 4
arr: [1,2,4]
current node:
  4
null null
stack push right current node first then followed by left
stack: [3, 5]

5th iteration:
current node = stack pop last element = 5
arr: [1,2,4,5]
current node:
  5
null null
stack push right current node first then followed by left
stack: [3]

6th iteration:
current node = stack pop last element = 3
arr: [1,2,4,5,3]
current node:
3
6   7
stack push right current node first then followed by left
stack: [7, 6]

7th iteration:
current node = stack pop last element = 6
arr: [1,2,4,5,3,6]
current node:
   6
null   null
stack push right current node first then followed by left
stack: [7]

8th iteration:
current node = stack pop last element = 6
arr: [1,2,4,5,3,6,7]
current node:
   7
null   null
stack push right current node first then followed by left
stack: []
stack.length === 0, false thereby terminating the while loop

*/
