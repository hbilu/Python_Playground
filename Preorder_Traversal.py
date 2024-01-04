"""
Given a binary tree, find its preorder traversal.

Example:
    Input:          Output: 1 4 4 2
            1
          /
        4
      /    \
    4       2
    Input:          Output: 6 3 1 2 2
           6
         /   \
        3     2
         \   /
          1 2

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 104
0 <= Data of a node <= 105
"""

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def preorder(root):
    arr = []
    if root:
        arr.append(root.data)
        arr += preorder(root.left)
        arr += preorder(root.right)
    return arr
