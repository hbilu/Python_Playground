"""
Given a Binary Search Tree. The task is to find the minimum valued element in this given BST.

Example:
Input:              Output: 1
           5
         /    \
        4      6
       /        \
      3          7
     /
    1

Expected Time Complexity: O(Height of the BST)
Expected Auxiliary Space: O(1).

Constraints:
0 <= N <= 104
"""
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


# Function to find the minimum element in the given BST.

def inorder(root, arr):
    if not root:
        return
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)

def minValue(root):
    if root == None:
        return -1
    arr = []
    inorder(root, arr)
    return min(arr)
