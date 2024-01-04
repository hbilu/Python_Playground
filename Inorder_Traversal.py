"""
Given a Binary Tree, find the In-Order Traversal of it.

Example:
    Input:                  Output: 3 3 2 1 3 2 2
               1
            /   \
           3     2
         /  \  /  \
       3    2 3    2

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
0 <= Data of a node <= 105
"""

class Solution:
    def InOrder(self,root):
        arr = []
        if root:
            arr += self.InOrder(root.left)
            arr.append(root.data)
            arr += self.InOrder(root.right)
        return arr