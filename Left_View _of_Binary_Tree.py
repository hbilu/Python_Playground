"""
Given a Binary Tree, print Left view of it.
Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
The task is to complete the function leftView(), which accepts root of the tree as argument,
and returns an array containing the nodes that are in the left view.
"""

# Node Class (which is given with the task):
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    res = []
    q = []
    if root is None:
        return res
    q.append(root)
    while len(q) != 0:
        n = len(q)
        for i in range(1, n + 1):
            temp = q[0]
            del q[0]
            if i == 1:
                res.append(temp.data)
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
    return res
