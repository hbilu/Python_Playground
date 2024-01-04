"""
Given a binary tree, find if it is height balanced or not.
A tree is height balanced if difference between heights of left and right subtrees
is not more than one for all nodes of tree.

A height balanced tree      An unbalanced tree
        1                           1
     /     \                       /
   10      39                    10
  /                             /
5                              5

Example:

Input:             Output: 0     Explanation: The max difference in height of left subtree and right subtree is 2
      1
    /
   2
    \
     3

Input:             Output: 1     Explanation: The max difference in height of left subtree and right subtree is 1.
       10
     /   \
    20   30
  /   \
 40   60


Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 109

Expected time complexity: O(N)
Expected auxiliary space: O(h) , where h = height of tree
"""


class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if root == None:
            return True
        if (abs(self.height(root.left) - self.height(root.right)) <= 1) and self.isBalanced(
                root.left) and self.isBalanced(root.right):
            return True
        return False