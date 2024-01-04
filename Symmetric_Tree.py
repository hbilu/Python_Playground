"""
Given a Binary Tree. Check whether it is Symmetric or not,
i.e. whether the binary tree is a Mirror image of itself or not.

Example:
Input:              Output: True
         5
       /   \
      1     1
     /       \
    2         2
Input:              Output: False
         5
       /   \
      10     10
     /  \     \
    20  20     30

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0<=N<=105
"""


class Solution:
    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None or root1.data != root2.data:
            return False
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)

    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isMirror(root.left, root.right)