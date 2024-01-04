"""
Given a binary tree, find its height.

Example:
    Input:
     2
     \
     1
    /
   3
Output: 3

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 109
"""

class Solution:
    def height(self, root):
        if root == None:
            return 0
        lHeight = self.height(root.left)
        rHeight = self.height(root.right)
        if lHeight > rHeight:
            return lHeight+1
        else:
            return rHeight+1