"""
Given a Binary Search Tree (with all values unique) and two node values n1 and n2 (n1!=n2).
Find the Lowest Common Ancestors of the two nodes in the BST.

Example:
    Input:  n1 = 7, n2 = 8
                  5
                /   \
              4      6
             /        \
            3          7
                        \
                         8
Output: 7

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= N <= 104
"""
# first way with recursive
def LCA(root, n1, n2):
    if root == None:
        return
    if root.data>n1 and root.data>n2:
        return LCA(root.left, n1, n2)
    if root.data<n1 and root.data<n2:
        return LCA(root.right, n1, n2)
    return root

# second way
def LCA(root, n1, n2):
    if root == None:
        return
    while root:
        if root.data>n1 and root.data>n2:
            root = root.left
        elif root.data<n1 and root.data<n2:
            root = root.right
        else:
            return root