"""
Given a Binary Search Tree and a node value X. Delete the node with the given value X from the BST. If no node with value x exists, then do not make any change.

Example     Input: X = 9        Output: 1 2 4 5 7 8 11 12      Explanation: In the given input tree after
            1                                                               1
             \                                                               \
              2                                                               2
                \                                                              \
                 8                                                              8
               /    \                                                         /   \
              5      11                                                      5     11
            /  \    /  \                                                   /  \     \
           4    7  9   12                                                4    7     12

Note: The generated output will be the inorder traversal of the modified tree.

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= N <= 105
"""

def deleteNode(root, x):
    if root is None:
        return None
    if x<root.data:
        root.left=deleteNode(root.left,x)
    elif x>root.data:
        root.right=deleteNode(root.right,x)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        current = root.right
        while current.left:
            current = current.left
        root.data=current.data
        root.right=deleteNode(root.right,root.data)
    return root