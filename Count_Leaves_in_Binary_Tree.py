"""
Complete the function countLeaves() that takes root node of the given tree as parameter
and returns the count of leaves in tree.

Example:
Input: Given Tree is
               4
             /   \
            8     10
           /     /   \
          7     5     1
         /
        3
Output: 3
Explanation: Three leaves are 3 , 5 and 1.

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def countLeaves(root):
    if root==None:
        return 0
    elif (root.left==None and root.right==None):
        return 1
    else:
        return countLeaves(root.left)+countLeaves(root.right)