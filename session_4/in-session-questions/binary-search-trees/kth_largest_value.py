class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, sortedNodeValues):

    # if we hit a leaf node just pop back up to parent
    if node is None: # is not node
        return

    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)