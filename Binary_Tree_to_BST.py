"""
Given a Binary Tree, convert it to Binary Search Tree
in such a way that keeps the original structure of Binary Tree intact.

Example:
    Input:          Output: 1 2 3 4
          1
       /    \
     2       3
   /
 4
Explanation: The converted BST will be

        3
      /   \
    2     4
  /
 1

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
"""

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def inorder(self, root, arr):
        if not root:
            return
        if root:
            self.inorder(root.left, arr)
            arr.append(root.data)
            self.inorder(root.right, arr)

    def update(self, root, arr):
        if root is None:
            return
        self.update(root.left, arr)
        root.data = arr[0]
        arr.pop(0)
        self.update(root.right, arr)

    def binaryTreeToBST(self, root):
        arr = []
        self.inorder(root, arr)
        arr.sort()
        self.update(root, arr)
        return root