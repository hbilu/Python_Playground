"""
Given a binary tree. Find the postorder traversal of the tree without using recursion.

Example:    Input:      Output: 10 7 1 6 10 6 5 8       Explanation: Postorder traversal (Left->Right->Root)
             8
          /      \
        1          5
         \       /   \
          7     10    6
           \   /
            10 6

Expected time complexity: O(N)
Expected auxiliary space: O(N)

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105
"""


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def postOrder(self,node):
        arr=[]
        if node == None:
            return arr
        stack = [node]
        while stack:
            temp = stack.pop()
            arr.append(temp.data)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        arr.reverse()
        return arr