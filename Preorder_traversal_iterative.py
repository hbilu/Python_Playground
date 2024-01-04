"""
Given a binary tree. Find the preorder traversal of the tree without using recursion.

Example:
    Input:            Output: 1 2 4 5 3   Explanation: Preorder traversal (Root->Left->Right) of  the tree is 1 2 4 5 3.
               1
             /   \
            2     3
          /  \
         4    5

Expected time complexity: O(N)
Expected auxiliary space: O(N

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105
"""

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
# first way
class Solution:
    def preOrder(self, root):
        arr = []
        if root is None:
            return arr
        nodeStack = [root]
        while nodeStack:
            node = nodeStack.pop()
            arr.append(node.data)
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)
        return arr

# second way
class Solution:
    def preOrder(self, root):
        arr = []
        if root == None:
            return arr
        current = root
        stack = []
        while True:
            if current:
                stack.append(current)
                arr.append(current.data)
                current = current.left
            elif stack:
                current = stack.pop()
                current = current.right
            else:
                break
        return arr